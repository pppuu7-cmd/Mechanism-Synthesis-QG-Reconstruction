#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/critic_k5_full_source_boundary_s5_symbolic_independent_reconstruction.py'
REPAIR_PREREG = ROOT / 'prereg/K5_FULL_SOURCE_BOUNDARY_S5_CRITIC_CLASSIFIER_EXECUTION_REPAIR.md'
PARENT_PREREG = 'cf8576acb7237b751c26d5b5942aa60874bcd00e'
BASE_IMPLEMENTATION_COMMIT = '64a4f4935d0238d67e2d60e0b202f81f1195330a'
BASE_EXPECTED_BLOB = '948f32653872e0920b4450d60d56d48a2a0cc24d'
REPAIR_PREREG_COMMIT = '2d510ae4ef0dab2e15a763a520864869eff2d71b'


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def all_named(d: dict, names: tuple[str, ...]) -> bool:
    return all(bool(d.get(k, False)) for k in names)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--raw-output', required=True)
    args = ap.parse_args()

    raw_path = Path(args.raw_output)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    prechecks = {
        'parent_prereg_locked': PARENT_PREREG == 'cf8576acb7237b751c26d5b5942aa60874bcd00e',
        'repair_prereg_locked': REPAIR_PREREG_COMMIT == '2d510ae4ef0dab2e15a763a520864869eff2d71b',
        'repair_prereg_present': REPAIR_PREREG.exists(),
        'base_implementation_commit_locked': BASE_IMPLEMENTATION_COMMIT == '64a4f4935d0238d67e2d60e0b202f81f1195330a',
        'base_blob_locked': BASE.exists() and git_blob_sha1(BASE) == BASE_EXPECTED_BLOB,
    }

    proc = subprocess.run(
        [sys.executable, str(BASE), '--output', str(raw_path)],
        cwd=str(ROOT), text=True, capture_output=True, check=False,
    )

    if not raw_path.exists():
        result = {
            'gate': 'FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_INDEPENDENT_CRITIC',
            'parent_critic_prereg_commit': PARENT_PREREG,
            'repair_prereg_commit': REPAIR_PREREG_COMMIT,
            'base_implementation_commit': BASE_IMPLEMENTATION_COMMIT,
            'base_implementation_blob': None if not BASE.exists() else git_blob_sha1(BASE),
            'prechecks': prechecks,
            'base_returncode': proc.returncode,
            'base_stdout': proc.stdout[-4000:],
            'base_stderr': proc.stderr[-4000:],
            'classification': 'INVALID_IMPLEMENTATION',
            'status': 'INVALID_IMPLEMENTATION',
            'reason': 'base reconstruction did not materialize raw JSON',
            'q18_values_used': False,
        }
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        return 2

    raw_bytes = raw_path.read_bytes()
    raw_sha = sha256_bytes(raw_bytes)
    try:
        raw = json.loads(raw_bytes.decode())
    except Exception as exc:
        result = {
            'gate': 'FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_INDEPENDENT_CRITIC',
            'prechecks': prechecks,
            'base_returncode': proc.returncode,
            'raw_sha256': raw_sha,
            'classification': 'INVALID_IMPLEMENTATION',
            'status': 'INVALID_IMPLEMENTATION',
            'reason': f'base raw JSON parse failed: {exc!r}',
            'q18_values_used': False,
        }
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        return 2

    # Frozen BLOCKED branch: missing source/prereg/erratum/derivation primitive.
    missing = raw.get('missing')
    if missing:
        result = {
            'gate': raw.get('gate'),
            'parent_critic_prereg_commit': PARENT_PREREG,
            'repair_prereg_commit': REPAIR_PREREG_COMMIT,
            'base_implementation_commit': BASE_IMPLEMENTATION_COMMIT,
            'base_implementation_blob': git_blob_sha1(BASE),
            'raw_sha256': raw_sha,
            'base_returncode': proc.returncode,
            'prechecks': prechecks,
            'classification': 'BLOCKED',
            'status': 'BLOCKED',
            'missing': missing,
            'q18_values_used': False,
            'raw_base_verdict': raw.get('verdict'),
        }
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        return 0

    source = raw.get('source_checks', {})
    group = raw.get('group_checks', {})
    poly = raw.get('polynomial_checks', {})
    boundary = raw.get('boundary_checks', {})
    neg = raw.get('negative_controls', {})
    forbidden = raw.get('forbidden_checks', {})
    cov = raw.get('covariance_results', {})
    gen = raw.get('generator_results', {})
    matching = raw.get('matching_sign_checks', {})

    static_group_names = (
        'canonical_ten_edge_order_exact', 'node_norms_4_12_cross0',
        'all_24_local_actions_exact', 'C5_identity', 'T2_identity',
        'generated_group_120', 'reynolds_rank2_pivots_1_4', 'reynolds_idempotent',
    )
    static_poly_names = (
        'spanning_tree_count_125', 'tree_coefficients_all_one',
        'laplacian_determinant_equals_independent_tree_enumeration', 'psi_degree4',
    )
    static_boundary_names = (
        'all_32_components', 'exactly_100000_original_source_terms',
        'source_module_expected_total', 'source_matrix_reversal_exact',
    )

    A = {
        'wrapper_prechecks': all(prechecks.values()),
        'source_checks': bool(source) and all(bool(v) for v in source.values()),
        'static_group_reconstruction': all_named(group, static_group_names),
        'static_kirchhoff_reconstruction': all_named(poly, static_poly_names),
        'static_boundary_source_coverage': all_named(boundary, static_boundary_names),
        'mandatory_malformed_controls': bool(neg) and all(bool(v) for v in neg.values()),
        'forbidden_methods_absent': bool(forbidden) and all(bool(v) for v in forbidden.values()),
        'q18_not_used': forbidden.get('q18_values_used') is False and raw.get('interpretation_ceiling', {}).get('q18_result') is None,
    }

    B = {
        'C_source_boundary_contragredient': bool(gen.get('C', {}).get('exact', False)),
        'T_source_boundary_contragredient': bool(gen.get('T', {}).get('exact', False)),
        'C_source_inverse_roundtrip': bool(gen.get('C', {}).get('inverse_roundtrip_exact', False)),
        'T_source_inverse_roundtrip': bool(gen.get('T', {}).get('inverse_roundtrip_exact', False)),
        'C_boundary_inverse': bool(gen.get('C', {}).get('boundary_inverse_exact', False)),
        'T_boundary_inverse': bool(gen.get('T', {}).get('boundary_inverse_exact', False)),
        'boundary_representation_composes_all120': bool(group.get('boundary_representation_composes_all120', False)),
        'edge_orientation_maps_compose_all120': bool(group.get('edge_orientation_maps_compose_all120', False)),
        'C_psi_covariance_transport': bool(poly.get('C_psi_and_covariance_exact', False)),
        'T_psi_covariance_transport': bool(poly.get('T_psi_and_covariance_exact', False)),
        'C_matching_orientation_all945': bool(poly.get('C_matching_orientation_factor_all945', False)),
        'T_matching_orientation_all945': bool(poly.get('T_matching_orientation_factor_all945', False)),
    }

    failed_B = [k for k, v in B.items() if not v]
    witness = {
        'C_source_dictionary': gen.get('C', {}).get('first_mismatch'),
        'T_source_dictionary': gen.get('T', {}).get('first_mismatch'),
        'C_covariance_bad_pairs': cov.get('C', {}).get('bad_pairs'),
        'T_covariance_bad_pairs': cov.get('T', {}).get('bad_pairs'),
        'C_matching_bad': matching.get('C', {}).get('bad'),
        'T_matching_bad': matching.get('T', {}).get('bad'),
    }

    witness_sufficient = True
    if not B['C_source_boundary_contragredient']:
        witness_sufficient &= witness['C_source_dictionary'] is not None
    if not B['T_source_boundary_contragredient']:
        witness_sufficient &= witness['T_source_dictionary'] is not None
    if not B['C_psi_covariance_transport']:
        witness_sufficient &= bool(witness['C_covariance_bad_pairs'])
    if not B['T_psi_covariance_transport']:
        witness_sufficient &= bool(witness['T_covariance_bad_pairs'])
    if not B['C_matching_orientation_all945']:
        witness_sufficient &= bool(witness['C_matching_bad'])
    if not B['T_matching_orientation_all945']:
        witness_sufficient &= bool(witness['T_matching_bad'])

    # Current base payload does not emit matrix-level exact mismatch witnesses for these branches.
    no_payload_witness_branches = (
        'C_source_inverse_roundtrip', 'T_source_inverse_roundtrip',
        'C_boundary_inverse', 'T_boundary_inverse',
        'boundary_representation_composes_all120', 'edge_orientation_maps_compose_all120',
    )
    if any(k in failed_B for k in no_payload_witness_branches):
        witness_sufficient = False

    if not all(A.values()):
        classification = 'INVALID_IMPLEMENTATION'
        status = 'INVALID_IMPLEMENTATION'
        reason = 'implementation/provenance validity set A failed'
    elif all(B.values()):
        classification = 'CONFIRMED_EXACT_SCOPED'
        status = 'PASS_EXACT_SCOPED'
        reason = 'all frozen substantive theorem conditions B pass exactly'
    elif witness_sufficient:
        classification = 'REFUTED_EXACT_SCOPED'
        status = 'SCIENTIFIC_FAIL_EXACT_SCOPED'
        reason = 'valid implementation with exact substantive counterexample'
    else:
        classification = 'INVALID_IMPLEMENTATION'
        status = 'INVALID_IMPLEMENTATION'
        reason = 'substantive condition failed but frozen exact refutation witness is not fully materialized'

    result = {
        'gate': 'FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_INDEPENDENT_CRITIC',
        'parent_critic_prereg_commit': PARENT_PREREG,
        'repair_prereg_commit': REPAIR_PREREG_COMMIT,
        'base_implementation_commit': BASE_IMPLEMENTATION_COMMIT,
        'base_implementation_blob': git_blob_sha1(BASE),
        'repair_runner_blob': git_blob_sha1(Path(__file__)),
        'raw_sha256': raw_sha,
        'base_returncode': proc.returncode,
        'raw_base_verdict': raw.get('verdict'),
        'raw_base_contract_classification': raw.get('critic_contract_classification'),
        'prechecks': prechecks,
        'implementation_validity_A': A,
        'substantive_theorem_B': B,
        'failed_substantive_conditions': failed_B,
        'refutation_witness_sufficient': witness_sufficient,
        'counterexample': witness if failed_B else None,
        'negative_controls': neg,
        'classification': classification,
        'status': status,
        'reason': reason,
        'q18_values_used': False,
        'independent_reconstruction': raw.get('independent_reconstruction'),
        'interpretation_ceiling': raw.get('interpretation_ceiling'),
    }
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')

    print('CLASSIFICATION=' + classification)
    print('STATUS=' + status)
    print('RAW_SHA256=' + raw_sha)
    print('A=' + json.dumps(A, sort_keys=True))
    print('B=' + json.dumps(B, sort_keys=True))
    return 2 if classification == 'INVALID_IMPLEMENTATION' else 0


if __name__ == '__main__':
    raise SystemExit(main())
