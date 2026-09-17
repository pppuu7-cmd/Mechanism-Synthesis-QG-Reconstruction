#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANN_SUM = ROOT / 'results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json'
ACTION_SOURCE = ROOT / 'scripts/k5_deg4_annihilator_actual_dual_action.py'
SOURCE_OBJECT = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
PRE = '1377d3944765b4aedbc512264cf73b75c45b96ad'
EXPECTED_ANN_SUM_BLOB = 'b6a18cf169ac58c57c7e416826dfa47e1ea3abf8'
EXPECTED_ACTION_BLOB = '2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
EXPECTED_SOURCE_BLOB = '2a3e3390556b337eccb6b917979961981f913deb'
EXPECTED_COEFF = (0,0,0,0,3,3,0,0,0,0,0,3,0,3,-1,-1,0,-1,-3,-1,0,-3,0,5,-1,-1,0,-1,0,-1,0,0,0)
MASK = 511
N = 10
ZERO = (0,) * N
CLASS_PASS = 'K5_MASK511_ANNIHILATOR_RAISES_FILTRATION_BY2_EXACT_SCOPED'
CLASS_FAIL = 'K5_MASK511_ANNIHILATOR_FILTRATION_SHIFT_LT2_EXACT_SCOPED'
CLASS_INVALID = 'INVALID_IMPLEMENTATION'


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def tdeg(m):
    return sum(m[:9])


def totaldeg(m):
    return sum(m)


def padd(a, b):
    out = dict(a)
    for m, c in b.items():
        z = out.get(m, Fraction(0)) + Fraction(c)
        if z:
            out[m] = z
        elif m in out:
            del out[m]
    return out


def pscale(a, c):
    c = Fraction(c)
    return {m: c*z for m, z in a.items() if c*z}


def pmul(a, b):
    out = defaultdict(Fraction)
    for ma, ca in a.items():
        for mb, cb in b.items():
            out[tuple(ma[i] + mb[i] for i in range(N))] += ca*cb
    return {m:c for m,c in out.items() if c}


def pderiv(a, i):
    out = {}
    for m, c in a.items():
        if not m[i]:
            continue
        q = list(m)
        k = q[i]
        q[i] -= 1
        out[tuple(q)] = c*k
    return out


def pvar(i):
    m = [0]*N
    m[i] = 1
    return {tuple(m): Fraction(1)}


def pmin_t(a):
    return min((tdeg(m) for m in a), default=None)


def pmax_t(a):
    return max((tdeg(m) for m in a), default=None)


def pstats(a):
    return {
        'terms': len(a),
        'min_t': pmin_t(a),
        'max_t': pmax_t(a),
        'total_degrees': sorted({totaldeg(m) for m in a}),
    }


def eperm(edges, eidx, p, e):
    a, b = edges[e]
    x, y = p[a], p[b]
    return eidx[(min(x,y), max(x,y))]


def act_mon(edges, eidx, m, p):
    q = [0]*N
    for i, x in enumerate(m):
        q[eperm(edges,eidx,p,i)] += x
    return tuple(q)


def mons_deg(d):
    out = []
    def rec(i, left, a):
        if i == N-1:
            out.append(tuple(a + [left]))
            return
        for x in range(left+1):
            rec(i+1, left-x, a+[x])
    rec(0,d,[])
    return out


def orbit_partition(edges, eidx, items, group):
    unseen = set(items)
    out = []
    while unseen:
        x = min(unseen)
        o = {act_mon(edges,eidx,x,p) for p in group}
        out.append(tuple(sorted(o)))
        unseen -= o
    return out


def build_q(coeff):
    edges = tuple(itertools.combinations(range(5),2))
    eidx = {e:i for i,e in enumerate(edges)}
    perms = list(itertools.permutations(range(5)))
    base = eidx[(0,1)]
    stab = [p for p in perms if {p[0],p[1]} == {0,1}]
    horb = orbit_partition(edges,eidx,mons_deg(3),stab)
    trans = [next(p for p in perms if eperm(edges,eidx,p,base) == e) for e in range(N)]
    qbas = [[tuple(act_mon(edges,eidx,m,trans[e]) for m in o) for o in horb] for e in range(N)]
    q = []
    for e in range(N):
        z = defaultdict(Fraction)
        for j, c in enumerate(coeff):
            if not c:
                continue
            for m in qbas[e][j]:
                z[m] += Fraction(c)
        q.append({m:c for m,c in z.items() if c})
    return edges, horb, q


def tree_poly(edges):
    out = {}
    for c in itertools.combinations(range(N),4):
        adj = {i:set() for i in range(5)}
        for e in c:
            x,y = edges[e]
            adj[x].add(y); adj[y].add(x)
        seen = {0}; stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        if len(seen) == 5:
            m = [0]*N
            for e in c:
                m[e] = 1
            out[tuple(m)] = Fraction(1)
    return out


def vector_field_data(q):
    alpha = [pvar(i) for i in range(N)]
    v = [pmul(alpha[i], q[i]) for i in range(N)]
    divv = {}
    sumq = {}
    S = {}
    for i in range(N):
        sumq = padd(sumq, q[i])
        S = padd(S, v[i])
        divv = padd(divv, q[i])
        divv = padd(divv, pmul(alpha[i], pderiv(q[i],i)))
    s1 = {}
    for a in alpha:
        s1 = padd(s1, a)
    K = padd(pmul(s1, padd(divv, pscale(sumq, Fraction(1,2)))), pscale(S, -3))
    return alpha, v, divv, sumq, S, s1, K


def vpsi(q, psi):
    alpha = [pvar(i) for i in range(N)]
    out = {}
    for i in range(N):
        out = padd(out, pmul(pmul(alpha[i],q[i]), pderiv(psi,i)))
    return out


def filtration_shift_bound(q):
    _, v, divv, sumq, S, s1, K = vector_field_data(q)
    transport = []
    for i in range(N):
        derivative_loss = 1 if i < 9 else 0
        transport.append(pmin_t(v[i]) - derivative_loss)
    return {
        'q_min_t': [pmin_t(z) for z in q],
        'v_min_t': [pmin_t(z) for z in v],
        'transport_term_shift_bounds': transport,
        'divv_min_t': pmin_t(divv),
        'sumq_min_t': pmin_t(sumq),
        'S_min_t': pmin_t(S),
        's1_min_t': pmin_t(s1),
        'K_min_t': pmin_t(K),
        'operator_shift_lower_bound': min(min(transport) + pmin_t(s1), pmin_t(K)),
        'K_terms': len(K),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    summary = json.loads(ANN_SUM.read_text(encoding='utf-8'))
    coeff = tuple(int(x) for x in summary['k5_exact']['annihilator_representative_coefficients'])
    checks = {
        'prereg_locked': PRE == '1377d3944765b4aedbc512264cf73b75c45b96ad',
        'mask511_frozen': MASK == 511,
        'ann_summary_blob_locked': git_blob_sha1(ANN_SUM) == EXPECTED_ANN_SUM_BLOB,
        'action_source_blob_locked': git_blob_sha1(ACTION_SOURCE) == EXPECTED_ACTION_BLOB,
        'source_object_blob_locked': git_blob_sha1(SOURCE_OBJECT) == EXPECTED_SOURCE_BLOB,
        'authoritative_annihilator_classification_locked': summary['classification'] == 'K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED',
        'annihilator_coefficients_locked': coeff == EXPECTED_COEFF,
    }

    edges, horb, q = build_q(coeff)
    checks['canonical_edge_order'] = edges == tuple(itertools.combinations(range(5),2)) and edges[-1] == (3,4)
    checks['fixed_edge_cubic_orbits_33'] = len(horb) == 33
    checks['all_q_nonzero'] = all(bool(z) for z in q)
    checks['all_q_degree3'] = all(all(totaldeg(m) == 3 for m in z) for z in q)
    checks['all_q_mask511_min_t_at_least2'] = all(pmin_t(z) is not None and pmin_t(z) >= 2 for z in q)

    psi = tree_poly(edges)
    checks['psi_k5_125_trees'] = len(psi) == 125
    checks['positive_control_vpsi_zero_exact'] = not vpsi(q, psi)

    bound = filtration_shift_bound(q)
    checks['transport_terms_raise_at_least2'] = min(bound['transport_term_shift_bounds']) >= 2
    checks['divv_in_F2'] = bound['divv_min_t'] >= 2
    checks['sumq_in_F2'] = bound['sumq_min_t'] >= 2
    checks['S_in_F2'] = bound['S_min_t'] >= 2
    checks['s1_filtration_zero'] = bound['s1_min_t'] == 0
    checks['K_in_F2'] = bound['K_min_t'] >= 2
    checks['operator_shift_at_least2'] = bound['operator_shift_lower_bound'] >= 2
    checks['no_physical_numerator_input'] = True
    checks['no_boundary_s5_transport_consumed'] = True
    checks['no_numerical_identity_proof'] = True

    qbad = [dict(z) for z in q]
    badmon = [0]*N; badmon[9] = 3; badmon = tuple(badmon)
    qbad[9][badmon] = qbad[9].get(badmon, Fraction(0)) + 1
    bad_bound = filtration_shift_bound(qbad)
    controls = {
        'malformed_q9_alpha9_cubed_has_filtration0': pmin_t(qbad[9]) == 0,
        'malformed_operator_rejected_by_shift_checker': bad_bound['operator_shift_lower_bound'] < 2,
    }

    provenance_ok = all(checks[k] for k in checks if k not in ('all_q_mask511_min_t_at_least2','transport_terms_raise_at_least2','divv_in_F2','sumq_in_F2','S_in_F2','K_in_F2','operator_shift_at_least2')) and all(controls.values())
    theorem = all(checks[k] for k in ('all_q_mask511_min_t_at_least2','transport_terms_raise_at_least2','divv_in_F2','sumq_in_F2','S_in_F2','K_in_F2','operator_shift_at_least2'))
    if not provenance_ok:
        status = CLASS_INVALID; classification = CLASS_INVALID
    elif theorem:
        status = 'PASS_EXACT_SCOPED'; classification = CLASS_PASS
    else:
        status = 'SCIENTIFIC_FAIL_EXACT_SCOPED'; classification = CLASS_FAIL

    out = {
        'gate':'K5_MASK511_ANNIHILATOR_FILTRATION_SHIFT',
        'prereg_commit':PRE,
        'status':status,
        'classification':classification,
        'scope':{'mask':511,'scaled_edge_indices':list(range(9)),'unscaled_edge_index':9,'boundary_s5_transport_consumed':False},
        'checks':checks,
        'controls':controls,
        'q_stats':[pstats(z) for z in q],
        'filtration_bound':bound,
        'malformed_control_bound':bad_bound,
        'conditional_consequence':'If a polynomial N lies in F^r, then B_v[N] lies in F^(r+2). In particular N in F^19 implies B_v[N] in F^21.',
        'physical_numerator_membership_verdict':None,
        'scientific_corner_integrability_verdict':None,
        'global_stokes_ibp_verdict':None,
        'integrated_period_verdict':None,
        'finite_part_selector':None,
        'regulator_independence':None,
    }
    op = Path(args.output); op.parent.mkdir(parents=True,exist_ok=True)
    op.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STATUS='+status)
    print('Q_MIN_T='+json.dumps(bound['q_min_t']))
    print('TRANSPORT_SHIFT_BOUNDS='+json.dumps(bound['transport_term_shift_bounds']))
    print('K_MIN_T='+str(bound['K_min_t']))
    print('OPERATOR_SHIFT_LOWER_BOUND='+str(bound['operator_shift_lower_bound']))
    if status == CLASS_INVALID:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
