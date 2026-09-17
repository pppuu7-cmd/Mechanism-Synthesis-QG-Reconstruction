#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SOURCE = ROOT / 'scripts/k5_mask511_structural_divisibility_lower_coefficients.py'
PREREG = ROOT / 'prereg/K5_MASK511_UNSCALED_EDGE_LEADING_COVARIANCE_ZERO.md'

PRE = 'e2a9fa293e9d442c3261a816aaef1b4a6b4d5aef'
EXPECTED_PREREG_BLOB = '6805d6500804b0a302dc6b80619fb87c82f4ab17'
EXPECTED_BASE_BLOB = '709904a582210642905ba053b5d622135da1067c'
EXPECTED_DAG_BLOB = '5a224105472d022d2357b811e820d66ccfb17a6f'
MASK = 511
UNSCALED_EDGE_INDEX = 9
CLASS_PASS = 'K5_MASK511_UNSCALED_EDGE_FORCES_Q18_ZERO_EXACT_SCOPED'
CLASS_FAIL = 'K5_MASK511_UNSCALED_EDGE_Q18_ZERO_THEOREM_REFUTED_EXACT_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'


def load_base():
    import importlib.util
    spec = importlib.util.spec_from_file_location('mask511_edge_kernel_base', BASE_SOURCE)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def poly_mat_vec(b, A, v):
    out = []
    for i in range(len(A)):
        z = {}
        for j, c in enumerate(v):
            if c:
                z = b.padd(z, b.pscale(A[i][j], Fraction(c)))
        out.append(z)
    return out


def poly_vec_mat(b, v, A):
    out = []
    for j in range(len(A[0])):
        z = {}
        for i, c in enumerate(v):
            if c:
                z = b.padd(z, b.pscale(A[i][j], Fraction(c)))
        out.append(z)
    return out


def enumerate_matchings(rem):
    rem = tuple(rem)
    if not rem:
        yield ()
        return
    i = rem[0]
    for pos in range(1, len(rem)):
        j = rem[pos]
        rest = rem[1:pos] + rem[pos+1:]
        for tail in enumerate_matchings(rest):
            yield ((i, j),) + tail


def matrix_stats(b, A):
    return [[b.pstats(A[i][j]) for j in range(len(A[i]))] for i in range(len(A))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    b = load_base()
    provenance = {
        'prereg_blob_locked': b.git_blob_sha1(PREREG) == EXPECTED_PREREG_BLOB,
        'base_blob_locked': b.git_blob_sha1(BASE_SOURCE) == EXPECTED_BASE_BLOB,
        'dag_blob_locked': b.git_blob_sha1(b.DAG_SOURCE) == EXPECTED_DAG_BLOB,
        'mask511_frozen': b.MASK == MASK,
        'unscaled_edge_index_frozen': UNSCALED_EDGE_INDEX == 9,
        'q18_partial_artifacts_consumed_false': True,
        'boundary_s5_transport_consumed_false': True,
        'numerical_sampling_consumed_false': True,
    }

    print('loading frozen canonical DAG prefix', flush=True)
    dns = b.exact_prefix(
        b.DAG_SOURCE,
        '# Evaluate frozen exact points by direct and canonical-DAG paths.',
        'mask511_edge_kernel_dag',
    )
    provenance['canonical_dag_hash_locked'] = dns['dag_hash'] == b.EXPECTED_DAG_HASH
    provenance['canonical_source_terms_100000'] = dns['SOURCE_TERMS'] == 100000
    provenance['canonical_edge_count_10'] = len(dns['EDGES']) == 10
    provenance['canonical_edge9_is_34'] = tuple(dns['EDGES'][9]) == (3, 4)

    EDGES = tuple(tuple(e) for e in dns['EDGES'])
    ROWS = tuple(tuple(int(x) for x in r) for r in dns['ROWS'])
    PSI = b.from_tuple_poly(dns['PSI'])
    ADJ = [[b.from_tuple_poly(dns['ADJ'][i][j]) for j in range(4)] for i in range(4)]
    LP = [[b.from_tuple_poly(dns['LP'][i][j]) for j in range(4)] for i in range(4)]
    Q = [[Fraction(x) for x in row] for row in dns['Q']]

    rstar = ROWS[UNSCALED_EDGE_INDEX]
    alpha9 = b.pvar(UNSCALED_EDGE_INDEX)

    print('checking degree-zero Laplacian face', flush=True)
    L0 = [[b.pslice(LP[i][j], 0) for j in range(4)] for i in range(4)]
    L0_expected = [[b.pscale(alpha9, rstar[i] * rstar[j]) for j in range(4)] for i in range(4)]

    A2 = [[b.pslice(ADJ[i][j], 2) for j in range(4)] for i in range(4)]
    right_kernel = poly_mat_vec(b, A2, rstar)
    left_kernel = poly_vec_mat(b, rstar, A2)

    theorem = {
        'psi_min_filtration_degree_3': b.pmin_t(PSI) == 3,
        'adjugate_has_degree2_leading_part': any(bool(A2[i][j]) for i in range(4) for j in range(4)),
        'adjugate_no_terms_below_degree2': all((not ADJ[i][j]) or b.pmin_t(ADJ[i][j]) >= 2 for i in range(4) for j in range(4)),
        'degree0_laplacian_exactly_unscaled_edge_rank1': L0 == L0_expected,
        'leading_adjugate_symmetric': all(A2[i][j] == A2[j][i] for i in range(4) for j in range(4)),
        'leading_adjugate_right_annihilates_unscaled_incidence': all(not z for z in right_kernel),
        'leading_adjugate_left_annihilates_unscaled_incidence': all(not z for z in left_kernel),
    }

    print('checking minimum covariance hierarchy', flush=True)
    AQ2 = b.mat_poly_num_right(A2, Q, 2)
    BN = [A2]
    for n in range(1, 5):
        target = 2 * (n + 1)
        M = b.mat_poly_mul(AQ2, BN[-1], target)
        BN.append([[b.pscale(z, -1) for z in row] for row in M])

    covariance_edge9 = {}
    all_edge9_zero = True
    nontrivial_other = False
    for n in range(5):
        target = 2 * (n + 1)
        for j in range(10):
            if j == UNSCALED_EDGE_INDEX:
                continue
            i, k = sorted((UNSCALED_EDGE_INDEX, j))
            z = b.dot_rows_poly(ROWS[i], BN[n], ROWS[k])
            z = b.pslice(z, target)
            covariance_edge9[f'n{n}_pair_{i}_{k}'] = b.pstats(z)
            all_edge9_zero &= not z
        for i in range(9):
            for j in range(i + 1, 9):
                z = b.dot_rows_poly(ROWS[i], BN[n], ROWS[j])
                z = b.pslice(z, target)
                if z:
                    nontrivial_other = True
                    break
            if nontrivial_other:
                break

    theorem['all_minimum_covariances_incident_to_unscaled_edge_zero_n0_n4'] = all_edge9_zero
    theorem['minimum_covariance_hierarchy_not_trivially_all_zero'] = nontrivial_other

    print('checking perfect-matching combinatorics', flush=True)
    matchings = list(enumerate_matchings(tuple(range(10))))
    incident_counts = [sum(UNSCALED_EDGE_INDEX in pair for pair in mt) for mt in matchings]
    theorem['perfect_matching_count_945'] = len(matchings) == 945
    theorem['every_perfect_matching_pairs_unscaled_slot_exactly_once'] = all(x == 1 for x in incident_counts)

    print('checking malformed leading-adjugate control', flush=True)
    x0sq = b.pmul(b.pvar(0), b.pvar(0), 2)
    A2_bad = [[dict(A2[i][j]) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if rstar[i] and rstar[j]:
                A2_bad[i][j] = b.padd(A2_bad[i][j], b.pscale(x0sq, rstar[i] * rstar[j]))
    bad_right = poly_mat_vec(b, A2_bad, rstar)
    controls = {
        'malformed_rstar_direction_breaks_kernel': any(bool(z) for z in bad_right),
        'unique_unscaled_edge_row_nonzero': any(rstar),
        'scaled_edge_row_not_all_in_same_kernel': any(
            any(bool(z) for z in poly_mat_vec(b, A2, ROWS[e])) for e in range(9)
        ),
        'no_q18_partial_scientific_value_consumed': True,
        'no_boundary_s5_theorem_consumed': True,
    }

    valid_provenance = all(provenance.values()) and all(controls.values())
    theorem_pass = all(theorem.values())
    if not valid_provenance:
        status = INVALID
        classification = INVALID
    elif theorem_pass:
        status = 'PASS_EXACT_SCOPED'
        classification = CLASS_PASS
    else:
        status = 'FAIL_EXACT_SCOPED'
        classification = CLASS_FAIL

    result = {
        'gate': 'K5_MASK511_UNSCALED_EDGE_LEADING_COVARIANCE_ZERO',
        'prereg_commit': PRE,
        'status': status,
        'classification': classification,
        'scope': {
            'mask': MASK,
            'scaled_edge_indices': list(range(9)),
            'unscaled_edge_index': UNSCALED_EDGE_INDEX,
            'unscaled_edge': list(EDGES[UNSCALED_EDGE_INDEX]),
            'physical_channels': [1, 2],
            'q18_partial_artifacts_consumed': False,
            'boundary_s5_transport_consumed': False,
        },
        'provenance': provenance,
        'theorem_checks': theorem,
        'controls': controls,
        'unscaled_incidence_row': list(rstar),
        'leading_adjugate_stats': matrix_stats(b, A2),
        'edge9_minimum_covariance_stats': covariance_edge9,
        'perfect_matching_count': len(matchings),
        'scientific_implication': {
            'N_channel_1_q18_zero_exact': theorem_pass,
            'N_channel_2_q18_zero_exact': theorem_pass,
            'reason': 'every naive-minimum five-pair Wick product contains a minimum covariance incident to the unique unscaled edge, and all such covariances vanish exactly',
        },
        'scientific_corner_integrability_verdict': None,
        'global_stokes_ibp_verdict': None,
        'physical_finite_part_selector': None,
        'regulator_independence': None,
    }

    raw = json.dumps(result, indent=2, sort_keys=True) + '\n'
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(raw, encoding='utf-8')
    print('CLASSIFICATION=' + classification)
    print('STATUS=' + status)
    print('MATCHINGS=', len(matchings))
    print('RESULT_SHA256=' + hashlib.sha256(raw.encode()).hexdigest())
    if status == INVALID:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
