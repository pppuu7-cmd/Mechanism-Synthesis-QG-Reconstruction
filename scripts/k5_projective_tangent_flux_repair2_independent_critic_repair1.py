import argparse, hashlib, json, os, re
import sympy as sp

N = 10
a = sp.symbols('a0:10')
t = sp.symbols('t')

PARENT_JSON_SHA = '017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3'


def canon(x):
    return sp.cancel(sp.together(x))


def zero(x):
    return canon(x) == 0


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def omega_form(alpha_vals):
    # Omega_9 = i_E(da0^...^da9)
    return {tuple(j for j in range(N) if j != i): ((-1) ** i) * alpha_vals[i] for i in range(N)}


def interior(form, vec):
    out = {}
    for basis, coeff in form.items():
        for pos, idx in enumerate(basis):
            key = basis[:pos] + basis[pos + 1:]
            out[key] = out.get(key, 0) + ((-1) ** pos) * coeff * vec[idx]
    return {k: canon(v) for k, v in out.items() if not zero(v)}


def forms_equal(f, g):
    return all(zero(f.get(k, 0) - g.get(k, 0)) for k in set(f) | set(g))


def q_generic(alpha):
    return [sp.Integer(i + 3) + 2 * alpha[(i + 2) % N] - alpha[(i + 5) % N] for i in range(N)]


def q_exception(alpha):
    return [sp.Integer(2) + (i + 1) ** 2 * alpha[0] for i in range(N)]


def q_generic_permuted(alpha, p):
    q = [None] * N
    for i in range(N):
        q[p[i]] = sp.Integer(i + 3) + 2 * alpha[p[(i + 2) % N]] - alpha[p[(i + 5) % N]]
    return q


def tangent(alpha, q):
    v = [canon(alpha[i] * q[i]) for i in range(N)]
    S = canon(sum(v))
    s1 = canon(sum(alpha))
    u = [canon(v[i] - (S / s1) * alpha[i]) for i in range(N)]
    return v, u, S, s1


def chart(Z, variant, tag):
    Z = tuple(sorted(Z))
    O = tuple(i for i in range(N) if i not in Z)
    k = len(Z)
    bdep = Z[-1] if variant == 0 or k == 1 else Z[0]
    odep = O[-1] if variant == 0 or len(O) == 1 else O[0]
    bind = [i for i in Z if i != bdep]
    oind = [i for i in O if i != odep]
    bs = list(sp.symbols(f'b{tag}_0:{len(bind)}'))
    ys = list(sp.symbols(f'y{tag}_0:{len(oind)}'))
    amap = {}
    bcoord = {}
    ycoord = {}
    for i, x in zip(bind, bs):
        amap[i] = t * x
        bcoord[i] = x
    amap[bdep] = t * (1 - sum(bs))
    for i, x in zip(oind, ys):
        amap[i] = x
        ycoord[i] = x
    amap[odep] = 1 - t - sum(ys)
    return {
        'Z': Z, 'O': O, 'bdep': bdep, 'odep': odep,
        'bind': bind, 'oind': oind, 'bs': bs, 'ys': ys,
        'face': bs + ys, 'amap': amap, 'bcoord': bcoord, 'ycoord': ycoord,
    }


def frozen_point(c):
    sub = {}
    m = len(c['bs'])
    if m:
        sw = sum(range(1, m + 1))
        for j, x in enumerate(c['bs']):
            sub[x] = sp.Rational(j + 1, 2 * sw)
    m = len(c['ys'])
    if m:
        sw = sum(range(1, m + 1))
        for j, x in enumerate(c['ys']):
            sub[x] = sp.Rational(j + 1, 3 * sw)
    return sub


def full_witness(c, qbuilder):
    alpha = [canon(c['amap'][i]) for i in range(N)]
    if not zero(sum(alpha) - 1):
        raise RuntimeError('chart does not lie on s1=1')
    q = qbuilder(alpha)
    v, u, _, _ = tangent(alpha, q)
    E = sp.Matrix(alpha)
    T = sp.Matrix([sp.diff(c['amap'][i], t) for i in range(N)])
    F = [sp.Matrix([sp.diff(c['amap'][i], z) for i in range(N)]) for z in c['face']]
    scalar = canon(sp.Matrix.hstack(E, T, *F).det(method='domain-ge'))
    flux = canon(sp.Matrix.hstack(E, sp.Matrix(u), *F).det(method='domain-ge'))
    normal = canon(sum(u[i] for i in c['Z']))
    return scalar, flux, normal


def point_witness(c, qbuilder):
    S, F, U = full_witness(c, qbuilder)
    pt = frozen_point(c)
    return canon(S.subs(pt, simultaneous=True)), canon(F.subs(pt, simultaneous=True)), canon(U.subs(pt, simultaneous=True))


def order(expr):
    expr = canon(expr)
    if expr == 0:
        return None, sp.Integer(0)
    num, den = sp.fraction(expr)
    Pn = sp.Poly(sp.expand(num), t)
    Pd = sp.Poly(sp.expand(den), t)
    on = min(m[0] for m, c in Pn.terms() if c != 0)
    od = min(m[0] for m, c in Pd.terms() if c != 0)
    lead = canon(Pn.coeff_monomial(t ** on) / Pd.coeff_monomial(t ** od))
    return int(on - od), lead


def transition(c0, c1, include_t):
    sub = {t: t} if include_t else {}
    for i, x in c1['bcoord'].items():
        sub[x] = canon(c0['amap'][i] / t)
    for i, x in c1['ycoord'].items():
        sub[x] = c0['amap'][i]
    src = ([t] + c0['face']) if include_t else c0['face']
    dst = ([t] + c1['face']) if include_t else c1['face']
    mapped = [sub.get(x, x) for x in dst]
    J = sp.Matrix([[sp.diff(mapped[i], x) for x in src] for i in range(len(dst))])
    return sub, canon(J.det(method='domain-ge'))


def edge_perm():
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    idx = {e: i for i, e in enumerate(edges)}
    vp = (1, 2, 3, 4, 0)
    p = []
    for i, j in edges:
        x, y = sorted((vp[i], vp[j]))
        p.append(idx[(x, y)])
    return vp, p


def audit_source(text):
    pats = [
        r'\bjac_exp\s*=\s*k\s*-\s*1\b',
        r'\bscalar_valuation\s*=\s*k\s*-\s*1\b',
        r'\bsv\s*=\s*k\s*-\s*1\b',
        r"['\"]scalar_valuation['\"]\s*:\s*k\s*-\s*1",
    ]
    bad = [p for p in pats if re.search(p, text)]
    req = ['def pullback_top_coeff', 'def valuation', 'sp.Matrix', 'sp.diff', 'transition_relation']
    miss = [x for x in req if x not in text]
    return not bad and not miss, {'forbidden_assignment_patterns': bad, 'missing_mechanical_markers': miss}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parent-json', required=True)
    ap.add_argument('--researcher-source', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    parent = json.load(open(args.parent_json, encoding='utf-8'))
    source_text = open(args.researcher_source, encoding='utf-8').read()

    provenance = {
        'parent_json_sha': sha256(args.parent_json) == PARENT_JSON_SHA,
        'parent_classification': parent.get('classification') == 'K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED',
        'parent_status': parent.get('status') == 'PASS_EXACT_SCOPED',
    }
    hard_ok, hard_detail = audit_source(source_text)
    coverage = {
        '18_parent_witnesses': len(parent.get('witnesses', [])) == 18,
        '9_parent_chart_relations': len(parent.get('chart_relations', [])) == 9,
        '9_parent_permutation_witnesses': len(parent.get('permutation_witnesses', [])) == 9,
        'parent_exceptional_present': isinstance(parent.get('exceptional_witness'), dict),
        'empty_firewall_nonphysical': parent.get('firewalls', {}).get('empty_set', {}).get('physical_boundary_verdict') is None,
        'full_firewall_nonphysical': parent.get('firewalls', {}).get('full_set', {}).get('physical_boundary_verdict') is None,
        'no_forbidden_kminus1_assignment': hard_ok,
    }

    alpha0 = [sp.Rational(i + 1, 55) for i in range(N)]
    q0 = q_generic(alpha0)
    v0, u0, _, _ = tangent(alpha0, q0)
    Om0 = omega_form(alpha0)
    fr = sp.Rational(7, 5)
    vsh = [v0[i] + fr * alpha0[i] for i in range(N)]
    math = {
        'ambient_u_s1': zero(sum(u0)),
        'ambient_iE_zero': forms_equal(interior(Om0, alpha0), {}),
        'ambient_iv_eq_iu': forms_equal(interior(Om0, v0), interior(Om0, u0)),
        'ambient_radial_shift': forms_equal(interior(Om0, vsh), interior(Om0, u0)),
    }

    witnesses = []
    relations = []
    scalar_orders = []
    symbolic_relations_ok = True
    face_identity_ok = True

    for k in range(1, 10):
        Z = tuple(range(k))
        charts = [chart(Z, v, f'k{k}v{v}') for v in (0, 1)]
        full = []
        for variant, c in enumerate(charts):
            S, F, U = full_witness(c, q_generic)
            Sp, Fp, Up = point_witness(c, q_generic)
            so, sl = order(Sp)
            fo, fl = order(Fp)
            no, nl = order(Up)
            identity = zero(F - S * U)
            face_identity_ok &= identity
            scalar_orders.append(so)
            full.append((S, F, U))
            witnesses.append({
                'k': k, 'chart': variant, 'bdep': c['bdep'], 'odep': c['odep'],
                'scalar_order': so, 'flux_order': fo, 'normal_order': no,
                'scalar_lead_at_frozen_angular_point': str(sl),
                'flux_lead_at_frozen_angular_point': str(fl),
                'normal_lead_at_frozen_angular_point': str(nl),
                'full_face_identity': identity,
            })

        c0, c1 = charts
        S0, F0, _ = full[0]
        S1, F1, _ = full[1]
        sub9, j9 = transition(c0, c1, True)
        sub8, j8 = transition(c0, c1, False)
        scalar_diff = canon(S0 - S1.subs(sub9, simultaneous=True) * j9)
        flux_diff = canon(F0 - F1.subs(sub8, simultaneous=True) * j8)
        scalar_equal = zero(scalar_diff)
        flux_equal = zero(flux_diff)
        distinct = (c0['bdep'], c0['odep']) != (c1['bdep'], c1['odep'])
        symbolic_relations_ok &= scalar_equal and flux_equal and distinct
        relations.append({
            'k': k,
            'distinct_charts': distinct,
            'scalar_transition_det': str(sp.factor(j9)),
            'flux_transition_det': str(sp.factor(j8)),
            'scalar_full_symbolic_difference': str(sp.factor(scalar_diff)),
            'flux_full_symbolic_difference': str(sp.factor(flux_diff)),
            'scalar_full_symbolic_equal': scalar_equal,
            'flux_full_symbolic_equal': flux_equal,
        })

    math['18_explicit_differential_form_witnesses'] = len(witnesses) == 18 and face_identity_ok
    math['mechanical_scalar_orders_0_to_8'] = scalar_orders == [j for j in range(9) for _ in (0, 1)]
    math['9_full_symbolic_chart_relations'] = len(relations) == 9 and symbolic_relations_ok

    vp, ep = edge_perm()
    perm_controls = []
    perm_ok = True
    for k in range(1, 10):
        Z = tuple(range(k))
        Zp = tuple(sorted(ep[i] for i in Z))
        c = chart(Z, 0, f'o{k}')
        cp = chart(Zp, 0, f'p{k}')
        S, F, _ = point_witness(c, q_generic)
        def qP(alpha, ep=ep):
            return q_generic_permuted(alpha, ep)
        SP, FP, _ = point_witness(cp, qP)
        so, _ = order(S); fo, _ = order(F)
        spv, _ = order(SP); fpv, _ = order(FP)
        ok = (so, fo) == (spv, fpv)
        perm_ok &= ok
        perm_controls.append({'k': k, 'Z': list(Z), 'Zp': list(Zp), 'scalar_orders': [so, spv], 'flux_orders': [fo, fpv], 'ok': ok})
    math['9_s5_permutation_controls'] = perm_ok

    ce = chart((0,), 0, 'ex')
    SG, FG, UG = point_witness(ce, q_generic)
    SX, FX, UX = point_witness(ce, q_exception)
    go, _ = order(FG)
    xo, xl = order(FX)
    exceptional = {
        'generic_order': go,
        'exceptional_order': xo,
        'exceptional_lead': str(xl),
        'advanced_to_higher_finite_order': go is not None and xo is not None and xo > go and not zero(FX),
    }
    math['independent_exceptional_advance'] = exceptional['advanced_to_higher_finite_order']

    prov_ok = all(provenance.values())
    cov_ok = all(coverage.values())
    math_ok = all(math.values())
    if not prov_ok:
        verdict = 'INVALID_PROVENANCE'
    elif not cov_ok:
        verdict = 'INVALID_IMPLEMENTATION'
    elif math_ok:
        verdict = 'CONFIRMED_SCOPED'
    else:
        verdict = 'SCIENTIFIC_FAIL_CONFIRMED'

    out = {
        'verdict': verdict,
        'control_repair': 1,
        'superseded_historical_critic_run': 35148773201,
        'superseded_historical_critic_result_commit': '9c3100676e2975629921c05c66799b4d59a07a88',
        'provenance_checks': provenance,
        'coverage_checks': coverage,
        'source_hardcode_audit': hard_detail,
        'math_checks': math,
        'explicit_witnesses': witnesses,
        'full_symbolic_chart_relations': relations,
        'permutation': {'vertex_perm': list(vp), 'edge_perm': ep, 'witnesses': perm_controls},
        'exceptional': exceptional,
        'interpretation_ceiling': {
            'physical_34_orbit_classification': None,
            'global_stokes_ibp': None,
            'integrated_k5_period': None,
            'F8_reduction': None,
            'finite_part_selector': None,
            'regulator_independence': None,
            'F9_G3_G8': None,
            'new_physics_found': None,
            'complete_qg': None,
        },
    }
    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
    print('VERDICT=' + verdict)
    print('PROVENANCE_OK=' + str(prov_ok).lower())
    print('COVERAGE_OK=' + str(cov_ok).lower())
    print('MATH_OK=' + str(math_ok).lower())
    print('FULL_SYMBOLIC_CHART_RELATIONS=' + str(math['9_full_symbolic_chart_relations']).lower())
    print('EXCEPTIONAL_ORDERS=' + str((go, xo)))
    raise SystemExit(0 if verdict == 'CONFIRMED_SCOPED' else 2)


if __name__ == '__main__':
    main()
