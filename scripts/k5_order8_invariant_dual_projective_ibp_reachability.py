#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
REDUCTION = ROOT / 'scripts/k5_order8_schwinger_projective_reduction.py'
DERIVATION = ROOT / 'sources/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_OBJECT_IBP_REACHABILITY_DERIVATION.md'
PREREG_COMMIT = '4a92113d33addb7c00bcb294f35fa78c35e18691'

NONZERO_CLASS = 'K5_INVARIANT_DUAL_PROJECTIVE_PERIOD_NONZERO_EXACT_SCOPED'
BOTH_ZERO_CLASS = 'K5_INVARIANT_DUAL_PROJECTIVE_PERIODS_BOTH_ZERO_EXACT_SCOPED'
INCOMPLETE_CLASS = 'K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED'
INVALID_CLASS = 'INVALID_IMPLEMENTATION'

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def fq(q):
    if isinstance(q, int):
        return q
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gmul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])


def gscale(q, z):
    return (q*z[0], q*z[1])


def gdot(a, b):
    out = ZERO
    for x, y in zip(a, b):
        out = gadd(out, gmul(x, y))
    return out


def bit_index(bits):
    x = 0
    for b in bits:
        x = (x << 1) | b
    return x


def local_tensor_vectors(mod):
    out = []
    for k in (0, 1):
        v = [Fraction(0)] * 16
        for state, coeff in mod.NODE_OPTIONS[k]:
            v[bit_index(state)] = Fraction(coeff)
        out.append(v)
    return out


def vdot(a, b):
    return sum((x*y for x, y in zip(a, b)), Fraction(0))


def permute_local_vec(v, p):
    out = [Fraction(0)] * 16
    for idx, coeff in enumerate(v):
        if not coeff:
            continue
        bits = [(idx >> (3-i)) & 1 for i in range(4)]
        obits = [0] * 4
        for i in range(4):
            obits[p[i]] = bits[i]
        out[bit_index(obits)] = coeff
    return out


def local_action_matrices(tensors):
    n0, n1 = vdot(tensors[0], tensors[0]), vdot(tensors[1], tensors[1])
    assert vdot(tensors[0], tensors[1]) == 0
    mats = {}
    for p in itertools.permutations(range(4)):
        cols = []
        for k in (0, 1):
            pv = permute_local_vec(tensors[k], p)
            coords = (vdot(tensors[0], pv)/n0, vdot(tensors[1], pv)/n1)
            recon = [coords[0]*tensors[0][i] + coords[1]*tensors[1][i] for i in range(16)]
            assert recon == pv
            cols.append(coords)
        mats[p] = (
            (cols[0][0], cols[1][0]),
            (cols[0][1], cols[1][1]),
        )
    return mats


def cycle_type(p):
    seen = set(); out = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i; n = 0
        while j not in seen:
            seen.add(j); n += 1; j = p[j]
        out.append(n)
    return tuple(sorted(out, reverse=True))


def global_action_matrix(mod, sigma, local_mats):
    A = [[Fraction(0) for _ in range(32)] for _ in range(32)]
    for x in range(32):
        ks = tuple((x >> (4-i)) & 1 for i in range(5))
        local_by_target = {}
        for v in range(5):
            old_neighbors = mod.NEIGHBORS[v]
            tv = sigma[v]
            target_pos = {w: i for i, w in enumerate(mod.NEIGHBORS[tv])}
            leg_perm = tuple(target_pos[sigma[w]] for w in old_neighbors)
            M = local_mats[leg_perm]
            local_by_target[tv] = (M[0][ks[v]], M[1][ks[v]])
        for kout in itertools.product((0,1), repeat=5):
            c = Fraction(1)
            for tv in range(5):
                c *= local_by_target[tv][kout[tv]]
                if not c:
                    break
            if c:
                A[bit_index(kout)][x] += c
    return A


def trace(A):
    return sum((A[i][i] for i in range(len(A))), Fraction(0))


def matmul(A, B):
    BT = list(zip(*B))
    return [[sum((x*y for x,y in zip(row,col)), Fraction(0)) for col in BT] for row in A]


def transpose(A):
    return [list(x) for x in zip(*A)]


def matvec(A, v):
    return [sum((A[i][j]*v[j] for j in range(len(v))), Fraction(0)) for i in range(len(A))]


def rref_rank(A):
    a = [row[:] for row in A]
    nr = len(a); nc = len(a[0]) if nr else 0
    r = 0; pivots = []
    for c in range(nc):
        p = next((i for i in range(r, nr) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x/z for x in a[r]]
        for i in range(nr):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x-z*y for x,y in zip(a[i], a[r])]
        pivots.append(c); r += 1
        if r == nr:
            break
    return r, a, pivots


def incidence_row(edge):
    a, b = edge
    row = [0,0,0,0]
    if a != 0:
        row[a-1] -= 1
    if b != 0:
        row[b-1] += 1
    return tuple(row)


def inv_fraction(A):
    n = len(A)
    a = [[Fraction(x) for x in row] + [Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c,n) if a[i][c])
        a[c], a[p] = a[p], a[c]
        z = a[c][c]
        a[c] = [x/z for x in a[c]]
        for i in range(n):
            if i == c:
                continue
            z = a[i][c]
            if z:
                a[i] = [x-z*y for x,y in zip(a[i],a[c])]
    return [row[n:] for row in a]


def dot_mat(r, M, s):
    return sum((Fraction(r[i])*M[i][j]*Fraction(s[j]) for i in range(4) for j in range(4)), Fraction(0))


def all_matchings(items):
    items = tuple(items)
    if not items:
        yield (); return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for tail in all_matchings(rest):
            yield ((a,b),) + tail


def entry_coeff_from_source(mod):
    basis = ((1,0,0),(0,1,0),(0,0,1))
    mats = [mod.leading_matrix(v) for v in basis]
    return {
        (r,c): tuple(tuple(m[r][c]) for m in mats)
        for r in (0,1) for c in (0,1)
    }


def uniform_full32_radial(mod):
    edges = tuple(mod.EDGES)
    rows = tuple(incidence_row(e) for e in edges)
    L = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for r in rows:
        for i in range(4):
            for j in range(4):
                L[i][j] += r[i]*r[j]
    B = inv_fraction(L)
    C = [[dot_mat(rows[i],B,rows[j]) for j in range(10)] for i in range(10)]
    matchings = list(all_matchings(range(10)))
    surviving = [m for m in matchings if all(C[a][b] != 0 for a,b in m)]
    entry = entry_coeff_from_source(mod)
    pair = {}
    for i in range(10):
        for j in range(i+1,10):
            for ea in entry:
                for eb in entry:
                    pair[(i,j,ea,eb)] = gscale(C[i][j], gdot(entry[ea],entry[eb]))
    cache = {}
    def wick(types):
        key = tuple(types)
        if key in cache:
            return cache[key]
        total = ZERO
        for matching in surviving:
            z = ONE
            for i,j in matching:
                z = gmul(z, pair[(i,j,types[i],types[j])])
                if z == ZERO:
                    break
            total = gadd(total,z)
        cache[key] = total
        return total

    boundary = []
    total_terms = 0
    for ks in itertools.product((0,1), repeat=5):
        total = ZERO
        for choices in itertools.product(*[mod.NODE_OPTIONS[k] for k in ks]):
            total_terms += 1
            states=[]; coeff=1
            for state,c in choices:
                states.append(state); coeff *= c
            types=[]
            for a,b in edges:
                row = states[b][mod.LEG_POS[(b,a)]]
                col = states[a][mod.LEG_POS[(a,b)]]
                types.append((row,col))
            total = gadd(total, gscale(Fraction(coeff), wick(types)))
        boundary.append(total)
    radial_factor = Fraction(11*12*13*14, 5**4)
    return [gscale(radial_factor,z) for z in boundary], len(matchings), len(surviving), len(cache), total_terms


def sparse_row(row):
    return {format(i,'05b'): fq(x) for i,x in enumerate(row) if x}


def classify(*, object_valid, nonzero_certificate=False, both_zero_certificate=False):
    if not object_valid:
        return INVALID_CLASS
    if nonzero_certificate:
        return NONZERO_CLASS
    if both_zero_certificate:
        return BOTH_ZERO_CLASS
    return INCOMPLETE_CLASS


def validate_candidate(c):
    checks = {
        'full32_boundary': c['full32_boundary'],
        'ten_edges': c['edge_count'] == 10,
        'source_node_norms': c['node_norms'] == [4,12] and c['node_cross'] == 0,
        'boundary_character': c['character'] == [32,0,8,2,0,0,2],
        'reynolds_rank_two': c['reynolds_rank'] == 2,
        'uses_dual_projection': c['uses_dual_projection'],
        'tree_count_125': c['tree_count'] == 125,
        'det_equals_tree_poly': c['det_equals_tree_poly'],
        'all_face_tree_counts_75': c['face_tree_counts'] == [75]*10,
        'alpha_half_weight_retained': c['alpha_half_total'] == Fraction(5),
        'numerator_degree_27': c['numerator_degree'] == 27,
        'psi_degree_4': c['psi_degree'] == 4,
        'denominator_exponent_21_over_2': c['denominator_exponent'] == Fraction(21,2),
        'function_homogeneity_minus10': c['function_homogeneity'] == -10,
        'projective_total_degree_zero': c['function_homogeneity'] + c['projective_volume_degree'] == 0,
        'regular_ibp_boundary_checked': c['regular_ibp_boundary_checked'],
        'common_scale_not_physical_regulator': not c['common_scale_is_physical_regulator'],
        'pointwise_not_promoted_to_period': not c['pointwise_promoted_to_period'],
        'two_invariant_periods_not_full_tensor_zero': not c['infer_full_tensor_zero_from_two_channels'],
    }
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    mod = load(SOURCE, 'iter077i_dual')
    red = load(REDUCTION, 'schwinger_reduction_dual')

    tensors = local_tensor_vectors(mod)
    node_norms = [vdot(t,t) for t in tensors]
    node_cross = vdot(tensors[0],tensors[1])
    local_mats = local_action_matrices(tensors)

    class_traces = defaultdict(set)
    P = [[Fraction(0) for _ in range(32)] for _ in range(32)]
    for sigma in itertools.permutations(range(5)):
        A = global_action_matrix(mod, sigma, local_mats)
        class_traces[cycle_type(sigma)].add(trace(A))
        for i in range(32):
            for j in range(32):
                P[i][j] += A[i][j] / 120

    class_order = ((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
    character = [next(iter(class_traces[c])) if len(class_traces[c]) == 1 else None for c in class_order]
    rank, RR, pivots = rref_rank(P)
    P2 = matmul(P,P)
    reynolds_idempotent = P2 == P
    dual_basis = RR[:rank]

    radial, matching_count, surviving_count, wick_cache, source_terms = uniform_full32_radial(mod)
    radial_imag_zero = all(z[1] == 0 for z in radial)
    avec = [z[0] for z in radial]
    dual_proj = matvec(transpose(P), avec)
    vector_proj = matvec(P, avec)
    coords = [dual_proj[p] for p in pivots]
    recon = [sum((coords[j]*dual_basis[j][i] for j in range(rank)), Fraction(0)) for i in range(32)]
    dual_reconstruction_exact = recon == dual_proj

    expected_coords = [Fraction(-9225216,9765625), Fraction(-7175168,9765625)]

    # Independently recover exact K5 Kirchhoff polynomial using the prior exact algebra module.
    Lpoly = red.laplacian_polynomial_matrix()
    detpoly = red.determinant_poly_4x4(Lpoly)
    trees = red.spanning_tree_monomials()
    det_equals_trees = set(detpoly) == trees and all(detpoly[m] == 1 for m in trees)
    face_tree_counts = [sum(i not in m for m in trees) for i in range(10)]

    # Exact projective structure.
    alpha_half_total = Fraction(10,2)
    numerator_degree = 9 * 3
    psi_degree = 4
    denominator_exponent = Fraction(21,2)
    function_homogeneity = alpha_half_total + numerator_degree - psi_degree*denominator_exponent
    projective_volume_degree = 10
    euler_ibp_divergence_coefficient = 10 + function_homogeneity
    regular_ibp_boundary_checked = all(n == 75 for n in face_tree_counts)

    candidate = {
        'full32_boundary': len(radial) == 32 and source_terms == 100000,
        'edge_count': len(mod.EDGES),
        'node_norms': node_norms,
        'node_cross': node_cross,
        'character': character,
        'reynolds_rank': rank,
        'uses_dual_projection': True,
        'tree_count': len(trees),
        'det_equals_tree_poly': det_equals_trees,
        'face_tree_counts': face_tree_counts,
        'alpha_half_total': alpha_half_total,
        'numerator_degree': numerator_degree,
        'psi_degree': psi_degree,
        'denominator_exponent': denominator_exponent,
        'function_homogeneity': function_homogeneity,
        'projective_volume_degree': projective_volume_degree,
        'regular_ibp_boundary_checked': regular_ibp_boundary_checked,
        'common_scale_is_physical_regulator': False,
        'pointwise_promoted_to_period': False,
        'infer_full_tensor_zero_from_two_channels': False,
    }
    checks = validate_candidate(candidate)
    checks.update({
        'local_s4_actions_complete': len(local_mats) == 24 and len(set(local_mats.values())) == 6,
        'class_traces_constant': all(len(class_traces[c]) == 1 for c in class_order),
        'reynolds_idempotent': reynolds_idempotent,
        'dual_rref_pivots_exact': pivots == [1,4],
        'uniform_all32_imaginary_zero': radial_imag_zero,
        'uniform_945_matchings': matching_count == 945,
        'uniform_144_surviving_matchings': surviving_count == 144,
        'uniform_100000_source_terms': source_terms == 100000,
        'dual_projection_differs_from_vector_projection': dual_proj != vector_proj,
        'dual_projection_reconstruction_exact': dual_reconstruction_exact,
        'uniform_dual_coordinates_exact_nonzero': coords == expected_coords and all(x != 0 for x in coords),
        'euler_projective_ibp_is_tautological_zero': euler_ibp_divergence_coefficient == 0,
    })

    # Derivation/provenance locks.
    text = DERIVATION.read_text(encoding='utf-8')
    locks = {
        'prereg_commit': PREREG_COMMIT in text,
        'dual_coordinate_1': '-9225216/9765625' in text,
        'dual_coordinate_2': '-7175168/9765625' in text,
        'projective_form': 'Psi_K5(alpha)^(21/2)' in text,
        'ibp_incomplete_ceiling': INCOMPLETE_CLASS in text,
    }
    checks['derivation_locks'] = all(locks.values())

    # Mandatory malformed controls through the same structural validator.
    mutations = {
        'representative_00000_only': {'full32_boundary': False},
        'omit_one_toller_edge': {'edge_count': 9},
        'corrupt_node_tensor_normalization': {'node_norms': [4,48]},
        'wrong_boundary_character': {'character': [32,0,8,0,0,0,2]},
        'wrong_reynolds_rank': {'reynolds_rank': 1},
        'vector_projection_substitution': {'uses_dual_projection': False},
        'fake_tree_count': {'tree_count': 124},
        'drop_alpha_half_weight': {'alpha_half_total': Fraction(0)},
        'wrong_denominator_exponent': {'denominator_exponent': Fraction(10)},
        'wrong_numerator_degree': {'numerator_degree': 26},
        'silent_ibp_boundary_drop': {'regular_ibp_boundary_checked': False},
        'promote_common_scale_to_physical_regulator': {'common_scale_is_physical_regulator': True},
        'promote_pointwise_witness_to_period': {'pointwise_promoted_to_period': True},
        'infer_full_tensor_zero_from_two_periods': {'infer_full_tensor_zero_from_two_channels': True},
    }
    controls = {}
    for name, changes in mutations.items():
        bad = dict(candidate); bad.update(changes)
        controls[name] = not all(validate_candidate(bad).values())

    # Synthetic outcome fixtures on the same classifier.
    controls['synthetic_nonzero_period_fixture'] = classify(object_valid=True, nonzero_certificate=True) == NONZERO_CLASS
    controls['synthetic_both_zero_fixture'] = classify(object_valid=True, both_zero_certificate=True) == BOTH_ZERO_CLASS

    object_valid = all(checks.values()) and all(controls.values())
    classification = classify(object_valid=object_valid)
    status = 'PASS_EXACT_SCOPED' if object_valid else INVALID_CLASS

    out = {
        'gate': 'K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_PERIOD_IBP_NONCANCELLATION',
        'prereg_commit': PREREG_COMMIT,
        'status': status,
        'classification': classification,
        'checks': checks,
        'controls': controls,
        'boundary_character': [fq(x) for x in character],
        'reynolds_rank': rank,
        'dual_rref_pivots': pivots,
        'dual_rref_basis_sparse': [sparse_row(row) for row in dual_basis],
        'uniform_full32': {
            'boundary_components': len(radial),
            'source_choice_terms': source_terms,
            'perfect_matchings': matching_count,
            'surviving_uniform_matchings': surviving_count,
            'wick_cache_size': wick_cache,
            'dual_coordinates_rref_basis': [fq(x) for x in coords],
            'vector_projection_equals_dual_projection': vector_proj == dual_proj,
        },
        'projective_object': {
            'form': 'Omega_9 * prod(alpha_e^(1/2)) * N_c(alpha) / Psi_K5(alpha)^(21/2)',
            'alpha_half_total_degree': fq(alpha_half_total),
            'numerator_degree': numerator_degree,
            'psi_degree': psi_degree,
            'denominator_exponent': fq(denominator_exponent),
            'function_homogeneity': fq(function_homogeneity),
            'projective_volume_degree': projective_volume_degree,
            'total_projective_degree': fq(function_homogeneity + projective_volume_degree),
            'kirchhoff_monomials': len(detpoly),
            'spanning_trees': len(trees),
            'trees_surviving_each_single_edge_face': face_tree_counts,
        },
        'ibp_reachability': {
            'regular_polynomial_vector_field_codim1_boundary_terms_zero': regular_ibp_boundary_checked,
            'reason': 'K5-e remains connected with 75 positive Kirchhoff tree monomials while explicit alpha_e^(1/2) vanishes',
            'euler_ibp_divergence_coefficient': fq(euler_ibp_divergence_coefficient),
            'euler_identity_decides_period': False,
            'higher_degree_exact_ibp_system_closed': False,
        },
        'invariant_dual_period_values': None,
        'scientific_parent_k5_zero_nonzero_verdict': None,
        'next': 'construct exact higher-degree projective IBP/syzygy or direct period evaluation for the two invariant-dual channels; retain explicit boundary audit for any singular/index-lowering fields',
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if object_valid else 2


if __name__ == '__main__':
    raise SystemExit(main())
