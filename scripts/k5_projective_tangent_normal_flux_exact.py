import json
import os
import sympy as sp

# Control repair 2 for the prospectively frozen projective-tangent flux gate.
# Exact antisymmetric forms are dictionaries {ordered_index_tuple: coefficient}.
N = 10
a = sp.symbols('a0:10')
t = sp.symbols('t')
s1 = sum(a)
SUCCESS = 'K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED'
SCI_FAIL = 'K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_SCIENTIFIC_FAIL_EXACT_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'


def canon(expr):
    return sp.cancel(sp.together(expr))


def is_zero(expr):
    return canon(expr) == 0


def omega9():
    # Omega_9 = i_E(da0^...^da9), E=sum a_i partial_i.
    return {tuple(j for j in range(N) if j != i): (-1) ** i * a[i] for i in range(N)}


def contract(form, vec):
    out = {}
    for inds, coeff in form.items():
        for pos, i in enumerate(inds):
            key = inds[:pos] + inds[pos + 1:]
            out[key] = out.get(key, 0) + (-1) ** pos * vec[i] * coeff
    ans = {}
    for key, expr in out.items():
        expr = canon(expr)
        if expr != 0:
            ans[key] = expr
    return ans


def form_equal(left, right):
    return all(is_zero(left.get(k, 0) - right.get(k, 0)) for k in set(left) | set(right))


def tangent_field(q):
    v = [sp.expand(a[i] * q[i]) for i in range(N)]
    S = sp.expand(sum(v))
    u = [canon(v[i] - S * a[i] / s1) for i in range(N)]
    return v, u, S


def pullback_top_coeff(form, amap, coords):
    # Coefficient of dcoords[0]^... in the pullback of an r-form.
    r = len(coords)
    total = 0
    for inds, coeff in form.items():
        if len(inds) != r:
            continue
        jac = sp.Matrix([[sp.diff(amap[a[i]], x) for x in coords] for i in inds]).det()
        total += coeff.subs(amap) * jac
    return canon(total)


def valuation(expr):
    expr = canon(expr)
    num, den = sp.fraction(expr)
    poly = sp.Poly(sp.expand(num), t)
    if poly.is_zero:
        return None, sp.Integer(0)
    order = min(mon[0] for mon, coeff in poly.terms() if coeff != 0)
    coeff = poly.coeff_monomial(t ** order)
    d0 = sp.simplify(den.subs(t, 0))
    if d0 != 0:
        lead = canon(coeff / d0)
    else:
        lead = sp.simplify(sp.limit(expr / t ** order, t, 0))
    return int(order), sp.factor(lead)


def chart(Z, variant, tag):
    Z = tuple(sorted(Z))
    outside = tuple(i for i in range(N) if i not in Z)
    k = len(Z)
    if not 1 <= k <= 9:
        raise ValueError('physical proper-face chart requires 1 <= |Z| <= 9')

    # Two genuinely distinct simplex charts: vary eliminated beta when possible,
    # otherwise vary eliminated outside coordinate. For k=9 the beta choice differs.
    bdep = Z[-1] if (variant == 0 or k == 1) else Z[0]
    bind = [i for i in Z if i != bdep]
    bs = sp.symbols(f'b{tag}_0:{len(bind)}')
    odep = outside[-1] if (variant == 0 or len(outside) == 1) else outside[0]
    oind = [i for i in outside if i != odep]
    ys = sp.symbols(f'y{tag}_0:{len(oind)}')

    amap = {}
    specs = []
    for i, b in zip(bind, bs):
        amap[a[i]] = t * b
        specs.append(('b', i, b))
    amap[a[bdep]] = t * (1 - sum(bs))
    for i, y in zip(oind, ys):
        amap[a[i]] = y
        specs.append(('y', i, y))
    amap[a[odep]] = 1 - t - sum(ys)

    return amap, list(bs) + list(ys), specs, {
        'Z': list(Z), 'bdep': bdep, 'odep': odep, 'variant': variant
    }


def transition_relation(F0, coords0, F1, coords1, specs1, amap0, include_t):
    # Express chart-1 independent coordinates in chart-0 coordinates by equality
    # of the ambient alpha_i, then compare full top-form coefficients including det J.
    sub = {}
    if include_t:
        sub[t] = t
    for kind, i, sym in specs1:
        sub[sym] = canon(amap0[a[i]] / t) if kind == 'b' else amap0[a[i]]
    transformed_coords = [t if x == t else sub[x] for x in coords1]
    jac = sp.Matrix([
        [sp.diff(transformed_coords[i], x) for x in coords0]
        for i in range(len(coords1))
    ]).det()
    diff = canon(F0 - F1.subs(sub, simultaneous=True) * jac)
    return is_zero(diff), sp.factor(jac), diff, sub


def form_terms(form):
    return [
        {'indices': list(k), 'coefficient': str(sp.factor(v))}
        for k, v in sorted(form.items())
    ]


def map_strings(amap):
    return {str(k): str(sp.factor(v)) for k, v in amap.items()}


def main():
    os.makedirs('artifacts/k5_projective_tangent_flux', exist_ok=True)

    implementation_checks = {
        'repair2_prereg_path_recorded': True,
        'all_k_1_to_9_two_charts': False,
        'genuine_chart_transition_checked': False,
        'permutation_related_subsets_checked': False,
        'nontrivial_exceptional_case_checked': False,
        'machine_witnesses_present': False,
        'empty_full_firewalls_present': True,
    }
    math_checks = {}
    witnesses = []
    permutation_witnesses = []

    Om = omega9()
    E = list(a)
    iEOm = contract(Om, E)
    math_checks['i_E_Omega_zero'] = form_equal(iEOm, {})

    # Generic exact nonradial polynomial logarithmic field.
    q = [(i + 2) + a[(i + 1) % N] + (i % 3 + 1) * a[(i + 3) % N] for i in range(N)]
    v, u, S = tangent_field(q)
    iv = contract(Om, v)
    iu = contract(Om, u)
    math_checks['u_s1_tangent'] = is_zero(sum(u))
    math_checks['i_v_Omega_equals_i_u_Omega'] = form_equal(iv, iu)

    f = 2 + a[0] - 3 * a[4]
    vshift = [sp.expand(v[i] + f * a[i]) for i in range(N)]
    ivshift = contract(Om, vshift)
    math_checks['radial_shift_contracted_form_invariant'] = form_equal(iv, ivshift) and form_equal(iu, ivshift)

    per_k_math = []
    chart_relations = []
    generic_flux_orders = {}

    for k in range(1, 10):
        Z = tuple(range(k))
        chart_data = []
        for variant in (0, 1):
            amap, facecoords, specs, meta = chart(Z, variant, f'k{k}c{variant}')
            scalar = pullback_top_coeff(Om, amap, [t] + facecoords)
            flux = pullback_top_coeff(iu, amap, facecoords)
            normal = canon(sum(u[i] for i in Z).subs(amap))
            sv, sl = valuation(scalar)
            fv, fl = valuation(flux)
            nv, nl = valuation(normal)

            # Direct geometric identity in the explicit chart:
            # PB(i_u Omega)|dt=0 = PB(Omega)_{dt wedge ...} * u(t).
            factor_ok = is_zero(flux - scalar * normal)
            scalar_ok = (sv == k - 1)
            finite_flux = (fv is not None)
            per_k_math.extend([factor_ok, scalar_ok, finite_flux])
            generic_flux_orders[(k, variant)] = fv

            witness = {
                'k': k,
                'chart': variant,
                'chart_meta': meta,
                'chart_map': map_strings(amap),
                'face_coords': [str(x) for x in facecoords],
                'pulled_scalar': str(sp.factor(scalar)),
                'scalar_valuation': sv,
                'scalar_lead': str(sl),
                'pulled_flux': str(sp.factor(flux)),
                'flux_valuation': fv,
                'flux_lead': str(fl),
                'normal_component': str(sp.factor(normal)),
                'normal_valuation': nv,
                'normal_lead': str(nl),
                'flux_equals_scalar_times_normal': factor_ok,
            }
            witnesses.append(witness)
            chart_data.append((amap, facecoords, specs, meta, scalar, flux))

        c0, c1 = chart_data
        scalar_rel, scalar_jac, scalar_diff, scalar_sub = transition_relation(
            c0[4], [t] + c0[1], c1[4], [t] + c1[1], c1[2], c0[0], True
        )
        flux_rel, flux_jac, flux_diff, flux_sub = transition_relation(
            c0[5], c0[1], c1[5], c1[1], c1[2], c0[0], False
        )
        distinct = (c0[3]['bdep'], c0[3]['odep']) != (c1[3]['bdep'], c1[3]['odep'])
        per_k_math.extend([scalar_rel, flux_rel])
        chart_relations.append({
            'k': k,
            'charts_genuinely_distinct': distinct,
            'scalar_full_form_equal_under_transition': scalar_rel,
            'flux_full_form_equal_under_transition': flux_rel,
            'scalar_transition_det': str(scalar_jac),
            'flux_transition_det': str(flux_jac),
            'scalar_transition_substitution': {str(x): str(sp.factor(y)) for x, y in scalar_sub.items()},
            'flux_transition_substitution': {str(x): str(sp.factor(y)) for x, y in flux_sub.items()},
            'scalar_difference_after_transition': str(sp.factor(scalar_diff)),
            'flux_difference_after_transition': str(sp.factor(flux_diff)),
        })

    math_checks['all_generic_face_pullbacks_match_parent_formula'] = all(per_k_math)
    math_checks['all_chart_full_form_relations_exact'] = all(
        x['scalar_full_form_equal_under_transition'] and x['flux_full_form_equal_under_transition']
        for x in chart_relations
    )
    implementation_checks['all_k_1_to_9_two_charts'] = len(witnesses) == 18 and {x['k'] for x in witnesses} == set(range(1, 10))
    implementation_checks['genuine_chart_transition_checked'] = len(chart_relations) == 9 and all(x['charts_genuinely_distinct'] for x in chart_relations)

    # Separate S5-induced permutation-related-subset control.
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    eidx = {e: i for i, e in enumerate(edges)}
    vertex_perm = (1, 2, 3, 4, 0)
    edge_perm = []
    for i, j in edges:
        x, y = sorted((vertex_perm[i], vertex_perm[j]))
        edge_perm.append(eidx[(x, y)])
    rename = {a[j]: a[edge_perm[j]] for j in range(N)}
    qperm = [None] * N
    for i in range(N):
        qperm[edge_perm[i]] = sp.expand(q[i].xreplace(rename))
    _, uperm, _ = tangent_field(qperm)
    iuperm = contract(Om, uperm)

    perm_ok = []
    for k in range(1, 10):
        Z = tuple(range(k))
        Zp = tuple(sorted(edge_perm[i] for i in Z))
        amap0, coords0, _, _ = chart(Z, 0, f'pg{k}')
        amapp, coordsp, _, _ = chart(Zp, 0, f'pp{k}')
        scalar0 = pullback_top_coeff(Om, amap0, [t] + coords0)
        flux0 = pullback_top_coeff(iu, amap0, coords0)
        scalarp = pullback_top_coeff(Om, amapp, [t] + coordsp)
        fluxp = pullback_top_coeff(iuperm, amapp, coordsp)
        sv0, _ = valuation(scalar0)
        fv0, _ = valuation(flux0)
        svp, _ = valuation(scalarp)
        fvp, _ = valuation(fluxp)
        ok = (sv0, fv0) == (svp, fvp)
        perm_ok.append(ok)
        permutation_witnesses.append({
            'k': k, 'Z': list(Z), 'Z_permuted': list(Zp),
            'vertex_permutation': list(vertex_perm), 'edge_permutation': edge_perm,
            'scalar_valuation_original': sv0, 'scalar_valuation_permuted': svp,
            'flux_valuation_original': fv0, 'flux_valuation_permuted': fvp,
            'valuation_covariant': ok,
        })
    math_checks['s5_permutation_valuation_covariance'] = all(perm_ok)
    implementation_checks['permutation_related_subsets_checked'] = len(permutation_witnesses) == 9

    # Nontrivial exceptional field: it becomes radial only at the Z={0} boundary,
    # so the naively leading normal coefficient cancels but the flux is not zero.
    qexc = [1 + (i + 1) * a[0] for i in range(N)]
    _, uexc, _ = tangent_field(qexc)
    iuexc = contract(Om, uexc)
    Zexc = (0,)
    amap_exc, coords_exc, _, meta_exc = chart(Zexc, 0, 'exc')
    generic_flux_exc = pullback_top_coeff(iu, amap_exc, coords_exc)
    exceptional_flux = pullback_top_coeff(iuexc, amap_exc, coords_exc)
    generic_normal_exc = canon(sum(u[i] for i in Zexc).subs(amap_exc))
    exceptional_normal = canon(sum(uexc[i] for i in Zexc).subs(amap_exc))
    gfv, gfl = valuation(generic_flux_exc)
    efv, efl = valuation(exceptional_flux)
    gnv, _ = valuation(generic_normal_exc)
    env, enl = valuation(exceptional_normal)
    exceptional_ok = (
        efv is not None and gfv is not None and efv > gfv and
        env is not None and gnv is not None and env > gnv and
        not is_zero(exceptional_flux) and
        is_zero(exceptional_flux - pullback_top_coeff(Om, amap_exc, [t] + coords_exc) * exceptional_normal)
    )
    math_checks['exceptional_leading_zero_advances_extractor'] = exceptional_ok
    implementation_checks['nontrivial_exceptional_case_checked'] = True
    exceptional_witness = {
        'Z': list(Zexc), 'chart_meta': meta_exc,
        'q_family': [str(x) for x in qexc],
        'generic_flux_valuation': gfv, 'generic_flux_lead': str(gfl),
        'exceptional_flux_valuation': efv, 'exceptional_flux_lead': str(efl),
        'generic_normal_valuation': gnv,
        'exceptional_normal_valuation': env, 'exceptional_normal_lead': str(enl),
        'flux_identically_zero': is_zero(exceptional_flux),
        'advanced_to_higher_finite_order': exceptional_ok,
    }

    # Empty/full-set provenance firewalls: no physical verdict is assigned to either.
    math_checks['full_set_projective_normal_zero'] = is_zero(sum(u))
    firewalls = {
        'empty_set': {'physical_boundary_verdict': None, 'role': 'control_only'},
        'full_set': {'physical_boundary_verdict': None, 'role': 'control_only', 'normal_component_zero': math_checks['full_set_projective_normal_zero']},
    }

    implementation_checks['machine_witnesses_present'] = (
        len(witnesses) == 18 and len(chart_relations) == 9 and
        len(permutation_witnesses) == 9 and exceptional_witness is not None
    )

    implementation_complete = all(implementation_checks.values())
    mathematics_true = all(math_checks.values())
    if not implementation_complete:
        classification = INVALID
        status = 'INVALID_IMPLEMENTATION'
    elif mathematics_true:
        classification = SUCCESS
        status = 'PASS_EXACT_SCOPED'
    else:
        classification = SCI_FAIL
        status = 'SCIENTIFIC_FAIL_EXACT_SCOPED'

    out = {
        'gate': 'K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING',
        'control_repair': 2,
        'repair2_prereg': 'prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_2.md',
        'failed_repair1_run': 35124809996,
        'failed_repair1_job': 104891115629,
        'classification': classification,
        'status': status,
        'implementation_checks': implementation_checks,
        'math_checks': math_checks,
        'ambient_forms': {
            'omega_terms': form_terms(Om),
            'i_v_omega_terms': form_terms(iv),
            'i_u_omega_terms': form_terms(iu),
            'i_E_omega_terms': form_terms(iEOm),
        },
        'generic_q': [str(x) for x in q],
        'witnesses': witnesses,
        'chart_relations': chart_relations,
        'permutation_witnesses': permutation_witnesses,
        'exceptional_witness': exceptional_witness,
        'firewalls': firewalls,
        'interpretation_ceiling': {
            'corner34_classification': None,
            'global_stokes_ibp': None,
            'integrated_k5_period': None,
            'finite_part_selector': None,
            'regulator_independence': None,
        },
    }
    path = 'artifacts/k5_projective_tangent_flux/result.json'
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
    print('classification=' + classification)
    print('status=' + status)
    print('implementation_complete=' + str(implementation_complete).lower())
    print('mathematics_true=' + str(mathematics_true).lower())
    print('exact_witnesses=' + str(len(witnesses)))
    print('permutation_witnesses=' + str(len(permutation_witnesses)))
    print('exceptional_flux_valuation=' + str(efv))
    if classification == INVALID:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
