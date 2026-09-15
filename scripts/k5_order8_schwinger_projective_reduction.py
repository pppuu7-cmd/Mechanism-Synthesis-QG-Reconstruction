#!/usr/bin/env python3
import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

VERTICES = tuple(range(5))
ROOT = 0
NONROOT = (1, 2, 3, 4)
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def parity(perm):
    inv = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inv += perm[i] > perm[j]
    return -1 if inv % 2 else 1


def poly_add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + c
        if out[m] == 0:
            del out[m]
    return out


def poly_mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(sorted(ma + mb))
            out[m] = out.get(m, 0) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def poly_scale(a, s):
    if s == 0:
        return {}
    return {m: s * c for m, c in a.items() if s * c != 0}


def linear_monomial(edge_idx, coeff=1):
    return {(edge_idx,): coeff} if coeff else {}


def reduced_incidence_row(edge):
    a, b = edge
    row = [0, 0, 0, 0]
    # Orientation a -> b. Sign is immaterial for the quadratic form but fixed.
    if a != ROOT:
        row[NONROOT.index(a)] -= 1
    if b != ROOT:
        row[NONROOT.index(b)] += 1
    return tuple(row)


def laplacian_polynomial_matrix():
    L = [[{} for _ in NONROOT] for _ in NONROOT]
    for ei, edge in enumerate(EDGES):
        r = reduced_incidence_row(edge)
        for i in range(4):
            for j in range(4):
                c = r[i] * r[j]
                if c:
                    L[i][j] = poly_add(L[i][j], linear_monomial(ei, c))
    return L


def determinant_poly_4x4(M):
    out = {}
    for p in itertools.permutations(range(4)):
        term = {(): parity(p)}
        for i, j in enumerate(p):
            term = poly_mul(term, M[i][j])
            if not term:
                break
        out = poly_add(out, term)
    return out


def connected_tree(edge_indices):
    adj = {v: set() for v in VERTICES}
    for ei in edge_indices:
        a, b = EDGES[ei]
        adj[a].add(b)
        adj[b].add(a)
    seen = {ROOT}
    stack = [ROOT]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(edge_indices) == 4 and len(seen) == 5


def spanning_tree_monomials():
    return {
        tuple(sorted(c))
        for c in itertools.combinations(range(len(EDGES)), 4)
        if connected_tree(c)
    }


def edge_permutation(vertex_perm):
    out = {}
    for ei, (a, b) in enumerate(EDGES):
        x, y = vertex_perm[a], vertex_perm[b]
        e2 = (x, y) if x < y else (y, x)
        out[ei] = EDGE_INDEX[e2]
    return out


def transport_monomial(m, ep):
    return tuple(sorted(ep[i] for i in m))


def validate_candidate(c):
    checks = {}
    checks['ten_edges'] = c['edge_count'] == 10
    checks['normal_dimension_12'] = c['normal_dimension'] == 12
    checks['edge_denominator_power_3_over_2'] = c['denominator_power'] == Fraction(3, 2)
    checks['leading_numerator_degree_10'] = c['leading_numerator_degree'] == 10
    checks['probe_degree_8'] = c['probe_degree'] == 8
    checks['total_degree_18'] = c['leading_numerator_degree'] + c['probe_degree'] == 18
    checks['wick_order_9'] = (c['leading_numerator_degree'] + c['probe_degree']) == 2 * c['wick_order'] == 18
    checks['laplacian_rank_4'] = c['laplacian_size'] == 4
    checks['kirchhoff_degree_4'] = c['kirchhoff_degree'] == 4
    checks['tree_count_125'] = c['tree_count'] == 125
    checks['determinant_matches_tree_polynomial'] = c['determinant_matches_tree_polynomial']
    checks['s5_tree_covariance'] = c['s5_tree_covariance']
    checks['common_scale_exponent_minus_one'] = c['common_scale_exponent'] == -1
    checks['no_one_parameter_physical_regulator_claim'] = not c['claims_one_parameter_physical_regulator']
    checks['no_k5_zero_nonzero_claim'] = not c['claims_k5_zero_nonzero']
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    L = laplacian_polynomial_matrix()
    det_poly = determinant_poly_4x4(L)
    trees = spanning_tree_monomials()

    det_support = set(det_poly)
    determinant_matches = (
        det_support == trees
        and all(len(m) == 4 and len(set(m)) == 4 for m in det_support)
        and all(det_poly[m] == 1 for m in det_support)
    )

    s5_failures = []
    for p in itertools.permutations(VERTICES):
        ep = edge_permutation(p)
        transported = {transport_monomial(m, ep) for m in trees}
        if transported != trees:
            s5_failures.append(p)

    numerator_degree = 10
    probe_degree = 8
    wick_order = (numerator_degree + probe_degree) // 2
    edge_alpha_half_total = Fraction(len(EDGES), 2)  # ten factors alpha^(1/2)
    radial_jacobian_power = len(EDGES) - 1
    determinant_scale_power = -Fraction(3, 2) * 4
    wick_scale_power = -wick_order
    common_scale_exponent = (
        edge_alpha_half_total
        + radial_jacobian_power
        + determinant_scale_power
        + wick_scale_power
    )

    candidate = {
        'edge_count': len(EDGES),
        'normal_dimension': 12,
        'denominator_power': Fraction(3, 2),
        'leading_numerator_degree': numerator_degree,
        'probe_degree': probe_degree,
        'wick_order': wick_order,
        'laplacian_size': 4,
        'kirchhoff_degree': next(iter({len(m) for m in det_support}), -1),
        'tree_count': len(trees),
        'determinant_matches_tree_polynomial': determinant_matches,
        's5_tree_covariance': not s5_failures,
        'common_scale_exponent': common_scale_exponent,
        'claims_one_parameter_physical_regulator': False,
        'claims_k5_zero_nonzero': False,
    }
    checks = validate_candidate(candidate)

    # Malformed lanes go through the same decision path. No hard-coded reject booleans.
    mutations = {
        'omit_one_edge': {'edge_count': 9},
        'wrong_denominator_power': {'denominator_power': Fraction(1, 1)},
        'representative_lower_probe_order': {'probe_degree': 6},
        'wrong_wick_order': {'wick_order': 8},
        'wrong_kirchhoff_degree': {'kirchhoff_degree': 5},
        'fake_tree_count': {'tree_count': 126},
        'determinant_tree_mismatch': {'determinant_matches_tree_polynomial': False},
        'break_s5_tree_covariance': {'s5_tree_covariance': False},
        'promote_common_scale_to_physical_regulator': {'claims_one_parameter_physical_regulator': True},
        'assign_k5_verdict_from_reduction': {'claims_k5_zero_nonzero': True},
    }
    controls = {}
    for name, changes in mutations.items():
        bad = dict(candidate)
        bad.update(changes)
        bchecks = validate_candidate(bad)
        controls[name] = not all(bchecks.values())

    exact = {
        'edges': [list(e) for e in EDGES],
        'edge_count': len(EDGES),
        'reduced_laplacian_dimension': 4,
        'determinant_monomial_count': len(det_poly),
        'spanning_tree_count': len(trees),
        'all_determinant_coefficients_one': all(c == 1 for c in det_poly.values()),
        'determinant_matches_spanning_tree_polynomial': determinant_matches,
        's5_permutations_checked': 120,
        's5_covariance_failures': len(s5_failures),
        'numerator_degree': numerator_degree,
        'probe_degree': probe_degree,
        'gaussian_total_degree': numerator_degree + probe_degree,
        'wick_order': wick_order,
        'scale_terms': {
            'prod_alpha_half': str(edge_alpha_half_total),
            'ten_parameter_radial_jacobian': str(radial_jacobian_power),
            'det_L_minus_3_over_2': str(determinant_scale_power),
            'wick_contraction': str(wick_scale_power),
        },
        'common_scale_exponent': str(common_scale_exponent),
    }

    implementation_ok = all(checks.values()) and all(controls.values())
    out = {
        'gate': 'K5_ORDER8_SCHWINGER_PROJECTIVE_REDUCTION_VALIDATION',
        'parent_scientific_gate': 'ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE',
        'status': 'REDUCTION_VALIDATED_EXACT' if implementation_ok else 'INVALID_IMPLEMENTATION',
        'scientific_k5_zero_nonzero_verdict': None,
        'checks': checks,
        'controls': controls,
        'exact': exact,
        'next_object': 'PROJECTIVE_K5_ORDER8_INVARIANT_DUAL_PERIODS',
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if implementation_ok else 2


if __name__ == '__main__':
    raise SystemExit(main())
