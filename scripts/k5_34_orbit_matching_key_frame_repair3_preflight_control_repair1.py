#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/k5_34_orbit_matching_key_frame_repair3_preflight.py'
CORE = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py'
CONTROL_PREREG = ROOT / 'prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_CONTROL_REPAIR_1.md'
CONTROL_REPAIR2_PREREG = ROOT / 'prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_CONTROL_REPAIR_2_NAMESPACE.md'
CRITIC_PROVENANCE = ROOT / 'status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md'

PARENT_PREREG_COMMIT = '4ee6c6f3056c5934a5209a4f05616b73354b4e6e'
CONTROL_REPAIR_PREREG_COMMIT = 'a05e1e29d2f39b678b2cf5f6b187cc165c787f9d'
CONTROL_REPAIR2_PREREG_COMMIT = 'e4ecce03cbe5df09afcb858480e582fa7b0c9b9e'
REPAIRED_CORE_COMMIT = '6691528d556247f1e8f9cae41f5559993077e15e'
CRITIC_PROVENANCE_COMMIT = '81b85171bb2432438b853bca37cca7bafa3c8d2e'
CRITIC_RUN = 35412815680
CRITIC_JOB = 105815631932
CRITIC_RESULT_SHA256 = '7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13'
CRITIC_RAW_AUTH_COMMIT = 'daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7'

PASS = 'PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT'
INVALID = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'
MISMATCH = 'MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_SCIENTIFIC_MISMATCH'


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--raw-output', required=True)
    args = ap.parse_args()

    out_path = Path(args.output)
    raw_path = Path(args.raw_output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    proc = subprocess.run(
        [sys.executable, str(BASE), '--output', str(raw_path)],
        cwd=str(ROOT), text=True, capture_output=True, check=False,
    )

    if not raw_path.exists():
        result = {
            'gate': 'K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT',
            'classification': INVALID,
            'reason': 'base preflight did not materialize raw JSON',
            'base_returncode': proc.returncode,
            'base_stdout_tail': proc.stdout[-4000:],
            'base_stderr_tail': proc.stderr[-4000:],
            'q18_values_used': False,
            'N_B_orders_or_coefficients_used': False,
            'heavy_resolver_launched': False,
        }
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        return 2

    raw_bytes = raw_path.read_bytes()
    raw_sha = sha256_bytes(raw_bytes)
    raw = json.loads(raw_bytes.decode())
    provenance_text = CRITIC_PROVENANCE.read_text(encoding='utf-8')

    repaired_validity = dict(raw.get('validity', {}))
    repaired_validity['core_commit_locked'] = REPAIRED_CORE_COMMIT == '6691528d556247f1e8f9cae41f5559993077e15e'
    repaired_validity['critic_run_locked'] = (
        CRITIC_PROVENANCE_COMMIT == '81b85171bb2432438b853bca37cca7bafa3c8d2e'
        and f'run `{CRITIC_RUN}`' in provenance_text
        and f'job `{CRITIC_JOB}`' in provenance_text
        and CRITIC_RESULT_SHA256 in provenance_text
        and CRITIC_RAW_AUTH_COMMIT in provenance_text
    )
    repaired_validity['control_repair1_prereg_locked'] = (
        CONTROL_REPAIR_PREREG_COMMIT == 'a05e1e29d2f39b678b2cf5f6b187cc165c787f9d'
    )
    repaired_validity['control_repair1_prereg_present'] = (
        CONTROL_PREREG.exists()
        and 'control-only repair 1' in CONTROL_PREREG.read_text(encoding='utf-8')
    )
    repaired_validity['control_repair2_prereg_locked'] = (
        CONTROL_REPAIR2_PREREG_COMMIT == 'e4ecce03cbe5df09afcb858480e582fa7b0c9b9e'
    )
    repaired_validity['control_repair2_prereg_present'] = (
        CONTROL_REPAIR2_PREREG.exists()
        and 'authority namespace binding' in CONTROL_REPAIR2_PREREG.read_text(encoding='utf-8')
    )
    # The base preflight's static aggregate excludes the two intentionally false
    # data/firewall fields. Under control repair2 it must now be true without any
    # scientific or matching-table criterion change.
    repaired_validity['static_repair3_controls'] = raw.get('validity', {}).get('static_repair3_controls') is True

    census = raw.get('census_and_relations', {})
    stages = raw.get('g8_stages', {})
    malformed = raw.get('malformed_controls', {})

    implementation_ok = (
        bool(repaired_validity)
        and all(bool(v) for v in repaired_validity.values())
        and bool(malformed)
        and all(bool(v) for v in malformed.values())
        and raw.get('q18_values_used') is False
        and raw.get('N_B_orders_or_coefficients_used') is False
        and raw.get('heavy_resolver_launched') is False
    )
    exact_ok = bool(census) and all(bool(v) for v in census.values()) and bool(stages) and all(bool(v) for v in stages.values())

    if not implementation_ok:
        classification = INVALID
    elif exact_ok:
        classification = PASS
    else:
        classification = MISMATCH

    result = {
        'gate': 'K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT',
        'classification': classification,
        'scientific_verdict': None,
        'parent_prereg_commit': PARENT_PREREG_COMMIT,
        'control_repair1_prereg_commit': CONTROL_REPAIR_PREREG_COMMIT,
        'control_repair2_prereg_commit': CONTROL_REPAIR2_PREREG_COMMIT,
        'repaired_core_commit': REPAIRED_CORE_COMMIT,
        'repaired_core_blob': git_blob_sha1(CORE),
        'critic_provenance_commit': CRITIC_PROVENANCE_COMMIT,
        'base_preflight_returncode': proc.returncode,
        'raw_base_sha256': raw_sha,
        'raw_base_classification': raw.get('classification'),
        'validity': repaired_validity,
        'census_and_relations': census,
        'g8_stages': stages,
        'malformed_controls': malformed,
        'frozen_lane': raw.get('frozen_lane'),
        'hashes': raw.get('hashes'),
        'first_mismatches': raw.get('first_mismatches'),
        'q18_values_used': False,
        'N_B_orders_or_coefficients_used': False,
        'heavy_resolver_launched': False,
        'heavy_resolver_authorized_by_this_result': classification == PASS,
        'resolver_scientific_authority_components': 0,
        'interpretation_ceiling': 'implementation-only matching-key frame preflight; no N/B scientific result',
    }
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')

    print('CLASSIFICATION=' + classification)
    print('RAW_BASE_CLASSIFICATION=' + str(raw.get('classification')))
    print('RAW_BASE_SHA256=' + raw_sha)
    print('VALIDITY=' + json.dumps(repaired_validity, sort_keys=True))
    print('CENSUS=' + json.dumps(census, sort_keys=True))
    print('G8_STAGES=' + json.dumps(stages, sort_keys=True))
    print('MALFORMED=' + json.dumps(malformed, sort_keys=True))
    return 0 if classification == PASS else 2


if __name__ == '__main__':
    raise SystemExit(main())
