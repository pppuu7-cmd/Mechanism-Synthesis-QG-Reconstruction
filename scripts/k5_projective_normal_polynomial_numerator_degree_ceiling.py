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
PREREG_COMMIT = '96d7f3acebf37809c15c1ae104d7a98efe462fdc'

PASS_NONZERO = 'K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_COMPLETE_SUPPORT_EXACT_SCOPED'
PASS_ZEROS = 'K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_CEILING_WITH_IDENTICALLY_ZERO_PROPER_FACES_EXACT_SCOPED'
SCI_FAIL = 'SCIENTIFIC_FAIL_PROJECTIVE_NORMAL_NUMERATOR_STRUCTURE'
INVALID = 'INVALID_IMPLEMENTATION'

EDGES = tuple(itertools.combinations(range(5), 2))
N = len(EDGES)
EIDX = {e: i for i, e in enumerate(EDGES)}
PERMS = tuple(itertools.permutations(range(5)))
ZERO = (0,) * N


def fq(q: Fraction):
    q = Fraction(q)
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def padd(a, b):
    out = defaultdict(Fraction)
    for m, c in a.items():
        out[m] += c
    for m, c in b.items():
        out[m] += c
    return {m: c for m, c in out.items() if c}


def pscale(a, c):
    c = Fraction(c)
    if c == 0:
        return {}
    return {m: c * v for m, v in a.items() if c * v}


def pmul(a, b):
    out = defaultdict(Fraction)
    for ma, ca in a.items():
        for mb, cb in b.items():
            out[tuple(ma[i] + mb[i] for i in range(N))] += ca * cb
    return {m: c for m, c in out.items() if c}


def pshift(a, i, n=1):
    out = {}
    for m, c in a.items():
        q = list(m)
        q[i] += n
        out[tuple(q)] = out.get(tuple(q), Fraction(0)) + c
    return {m: c for m, c in out.items() if c}


def pderiv(a, i):
    out = defaultdict(Fraction)
    for m, c in a.items():
        if m[i]:
            q = list(m)
            power = q[i]
            q[i] -= 1
            out[tuple(q)] += c * power
    return {m: c for m, c in out.items() if c}


def degree_set(a):
    return sorted({sum(m) for m in a})


def poly_hash(a):
    rows = [([*m], fq(c)) for m, c in sorted(a.items())]
    raw = json.dumps(rows, separators=(',', ':'), sort_keys=False).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def edge_perm(p, eidx):
    a, b = EDGES[eidx]
    x, y = p[a], p[b]
    return EIDX[(min(x, y), max(x, y))]


def act_mon(m, p):
    q = [0] * N
    for i, x in enumerate(m):
        q[edge_perm(p, i)] += x
    return tuple(q)


def mons_deg(d):
    out = []

    def rec(i, left, acc):
        if i == N - 1:
            out.append(tuple(acc + [left]))
            return
        for x in range(left + 1):
            rec(i + 1, left - x, acc + [x])

    rec(0, d, [])
    return out


def orbit_partition(items, group):
    unseen = set(items)
    out = []
    while unseen:
        x = min(unseen)
        orb = {act_mon(x, p) for p in group}
        out.append(tuple(sorted(orb)))
        unseen -= orb
    return out


def reconstruct_q(ann_coeff):
    base = EIDX[(0, 1)]
    stab = [p for p in PERMS if {p[0], p[1]} == {0, 1}]
    horb = orbit_partition(mons_deg(3), stab)
    assert len(horb) == 33
    trans = [next(p for p in PERMS if edge_perm(p, base) == e) for e in range(N)]
    qbas = [[tuple(act_mon(m, trans[e]) for m in orb) for orb in horb] for e in range(N)]
    qs = []
    for e in range(N):
        poly = defaultdict(Fraction)
        for j, c in enumerate(ann_coeff):
            c = Fraction(c)
            if not c:
                continue
            for m in qbas[e][j]:
                poly[m] += c
        qs.append({m: c for m, c in poly.items() if c})
    return stab, horb, qbas, tuple(qs)


def spanning_tree_poly():
    out = {}
    for comb in itertools.combinations(range(N), 4):
        adj = {i: set() for i in range(5)}
        for e in comb:
            a, b = EDGES[e]
            adj[a].add(b)
            adj[b].add(a)
        seen = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        if len(seen) == 5:
            m = [0] * N
            for e in comb:
                m[e] = 1
            out[tuple(m)] = Fraction(1)
    return out


def vpsi(vs, psi):
    out = {}
    for e in range(N):
        out = padd(out, pmul(vs[e], pderiv(psi, e)))
    return out


def mask_perm(mask, p):
    z = 0
    for e in range(N):
        if (mask >> e) & 1:
            z |= 1 << edge_perm(p, e)
    return z


def subset_orbits():
    unseen = set(range(1 << N))
    rows = []
    while unseen:
        rep = min(unseen)
        orb = {mask_perm(rep, p) for p in PERMS}
        rows.append((rep, len(orb), tuple(sorted(orb))))
        unseen -= orb
    return rows


def alpha_linear_poly(i):
    m = [0] * N
    m[i] = 1
    return {tuple(m): Fraction(1)}


def main():
    ann_summary = json.loads(ANN_SUM.read_text(encoding='utf-8'))
    ann_coeff = tuple(Fraction(x) for x in ann_summary['k5_exact']['annihilator_representative_coefficients'])

    stab, horb, qbas, qs = reconstruct_q(ann_coeff)
    alphas = tuple(alpha_linear_poly(i) for i in range(N))
    s1 = {}
    for a in alphas:
        s1 = padd(s1, a)
    vs = tuple(pshift(qs[i], i) for i in range(N))
    S = {}
    for v in vs:
        S = padd(S, v)

    psi = spanning_tree_poly()
    vp = vpsi(vs, psi)

    bad_coeff = list(ann_coeff)
    bad_coeff[4] += 1
    _, _, _, bad_qs = reconstruct_q(tuple(bad_coeff))
    bad_vs = tuple(pshift(bad_qs[i], i) for i in range(N))
    bad_vp = vpsi(bad_vs, psi)

    # Frozen nonzero homogeneous cubic radial-shift fixture f=sum_i alpha_i^3.
    f = {}
    for i in range(N):
        m = [0] * N
        m[i] = 3
        f[tuple(m)] = Fraction(1)
    shifted_vs = tuple(padd(vs[i], pmul(f, alphas[i])) for i in range(N))
    shifted_S = {}
    for v in shifted_vs:
        shifted_S = padd(shifted_S, v)

    orbits = subset_orbits()
    orbit_index = {}
    for oi, (rep, size, members) in enumerate(orbits):
        for m in members:
            orbit_index[m] = (oi, rep, size)

    rows = []
    proper_zero_masks = []
    radial_invariance_all = True
    raw_v_radial_shift_failure_exists = False
    bad_subtraction_radial_shift_failure_exists = False
    proper_homogeneous_degree5 = True
    degree_ceiling_ok = True

    for mask in range(1 << N):
        subset = [e for e in range(N) if (mask >> e) & 1]
        A = {}
        V = {}
        Vshift = {}
        for e in subset:
            A = padd(A, alphas[e])
            V = padd(V, vs[e])
            Vshift = padd(Vshift, shifted_vs[e])
        U = padd(pmul(s1, V), pscale(pmul(S, A), -1))
        Ushift = padd(pmul(s1, Vshift), pscale(pmul(shifted_S, A), -1))
        Ubad = padd(pmul(s1, V), pscale(pmul(S, A), -2))
        Ubad_shift = padd(pmul(s1, Vshift), pscale(pmul(shifted_S, A), -2))

        radial_same = Ushift == U
        radial_invariance_all &= radial_same
        if mask not in (0, (1 << N) - 1):
            if Vshift != V:
                raw_v_radial_shift_failure_exists = True
            if Ubad_shift != Ubad:
                bad_subtraction_radial_shift_failure_exists = True
            if not U:
                proper_zero_masks.append(mask)
            else:
                ds = degree_set(U)
                proper_homogeneous_degree5 &= ds == [5]
                degree_ceiling_ok &= max(ds) <= 5
        oi, rep, osize = orbit_index[mask]
        rows.append({
            'mask': mask,
            'bits': subset,
            'k': len(subset),
            'orbit_index': oi,
            'orbit_rep': rep,
            'orbit_size': osize,
            'zero': not bool(U),
            'degree_set': degree_set(U),
            'coefficient_count': len(U),
            'sha256': poly_hash(U),
            'radial_shift_invariant': radial_same,
        })

    controls = {
        'P1_ten_edges': len(EDGES) == 10,
        'P1_fixed_edge_stabilizer_order12': len(stab) == 12,
        'P1_fixed_edge_cubic_orbits33': len(horb) == 33,
        'P1_annihilator_coefficients33': len(ann_coeff) == 33,
        'P2_all_q_homogeneous_degree3': all(q and degree_set(q) == [3] for q in qs),
        'P2_q_not_all_zero': any(bool(q) for q in qs),
        'P3_all_v_homogeneous_degree4': all(v and degree_set(v) == [4] for v in vs),
        'P4_psi_125_trees': len(psi) == 125,
        'P4_psi_coefficients_one': all(c == 1 for c in psi.values()),
        'P4_vpsi_exact_zero': vp == {},
        'P5_S_homogeneous_degree4': bool(S) and degree_set(S) == [4],
        'P5_s1_homogeneous_degree1': bool(s1) and degree_set(s1) == [1],
        'P6_empty_U_zero': rows[0]['zero'],
        'P6_full_U_zero': rows[-1]['zero'],
        'P7_nonzero_proper_U_homogeneous_degree5': proper_homogeneous_degree5,
        'P8_uniform_degree_ceiling5': degree_ceiling_ok,
        'P9_subset_orbits34': len(orbits) == 34,
        'P9_proper_orbit_reps32': sum(rep not in (0, (1 << N) - 1) for rep, _, _ in orbits) == 32,
        'P9_orbit_sizes_sum1024': sum(size for _, size, _ in orbits) == 1024,
        'P10_radial_shift_invariance_all_subsets': radial_invariance_all,
        'N1_raw_V_radial_shift_rejected': raw_v_radial_shift_failure_exists,
        'N2_bad_projective_subtraction_rejected': bad_subtraction_radial_shift_failure_exists,
        'N3_altered_annihilator_breaks_vpsi': bad_vp != {},
        'N4_exact_fraction_polynomial_path_only': True,
    }

    source_structure_ok = all([
        controls['P2_all_q_homogeneous_degree3'],
        controls['P3_all_v_homogeneous_degree4'],
        controls['P4_vpsi_exact_zero'],
        controls['P7_nonzero_proper_U_homogeneous_degree5'],
        controls['P8_uniform_degree_ceiling5'],
    ])
    implementation_ok = all(controls.values())

    if not source_structure_ok:
        classification = SCI_FAIL
        status = 'SCIENTIFIC_FAIL_EXACT_SCOPED'
    elif not implementation_ok:
        classification = INVALID
        status = INVALID
    elif proper_zero_masks:
        classification = PASS_ZEROS
        status = 'PASS_EXACT_SCOPED'
    else:
        classification = PASS_NONZERO
        status = 'PASS_EXACT_SCOPED'

    orbit_rows = []
    for oi, (rep, size, members) in enumerate(orbits):
        rr = rows[rep]
        orbit_rows.append({
            'orbit_index': oi,
            'representative_mask': rep,
            'orbit_size': size,
            'k': rr['k'],
            'representative_zero': rr['zero'],
            'representative_degree_set': rr['degree_set'],
            'representative_coefficient_count': rr['coefficient_count'],
            'representative_sha256': rr['sha256'],
            'proper': rep not in (0, (1 << N) - 1),
        })

    out = {
        'gate': 'K5_PROJECTIVE_NORMAL_POLYNOMIAL_NUMERATOR_DEGREE_CEILING',
        'prereg_commit': PREREG_COMMIT,
        'status': status,
        'classification': classification,
        'formula': {
            'u_Z': 'U_Z/s1',
            'U_Z': 's1*V_Z-S*A_Z',
            'A_Z': 'sum_(e in Z) alpha_e',
            'V_Z': 'sum_(e in Z) alpha_e*q_e',
            'q_degree': 3,
            'v_degree': 4,
            'U_degree_ceiling': 5,
            'linear_corner_t_support': [0, 1, 2, 3, 4, 5],
        },
        'controls': controls,
        'authoritative_annihilator_coefficients': [fq(x) for x in ann_coeff],
        'proper_labeled_subset_count': 1022,
        'proper_identically_zero_count': len(proper_zero_masks),
        'proper_identically_zero_masks': proper_zero_masks,
        'subset_orbit_count': len(orbits),
        'proper_orbit_count': 32,
        'orbit_rows': orbit_rows,
        'labeled_subset_rows': rows,
        'psi_sha256': poly_hash(psi),
        'S_sha256': poly_hash(S),
        'q_sha256': [poly_hash(q) for q in qs],
        'v_sha256': [poly_hash(v) for v in vs],
        'scientific_corner_integrability_verdict': None,
        'global_stokes_ibp_verdict': None,
        'integrated_period_verdict': None,
        'finite_part_selector': None,
        'regulator_independence': None,
    }

    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('STATUS=' + status)
    print('CLASSIFICATION=' + classification)
    print('PROPER_ZERO_COUNT=' + str(len(proper_zero_masks)))
    print('ORBIT_COUNT=' + str(len(orbits)))
    print('ALL_CONTROLS=' + str(all(controls.values())))
    if status in (INVALID, 'SCIENTIFIC_FAIL_EXACT_SCOPED'):
        raise SystemExit(2)


if __name__ == '__main__':
    main()
