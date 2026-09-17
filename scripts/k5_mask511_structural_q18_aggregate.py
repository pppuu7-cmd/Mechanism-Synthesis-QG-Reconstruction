#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SOURCE = ROOT / 'scripts/k5_mask511_structural_divisibility_lower_coefficients.py'
Q18_PREREG = ROOT / 'prereg/K5_MASK511_STRUCTURAL_DIVISIBILITY_Q18_REDUCTION_IF_NEEDED.md'
PARENT_RAW = ROOT / 'results/raw/k5_mask511_physical_numerator_action_exact_corner_witness_authoritative.json'
FILTRATION_RAW = ROOT / 'results/raw/k5_mask511_annihilator_filtration_shift_authoritative.json'
AUDIT = ROOT / 'status/K5_MASK511_STRUCTURAL_DIVISIBILITY_REPAIR1_PRETERMINAL_CODE_AUDIT.md'
TERMINAL_REPAIR1 = ROOT / 'status/K5_MASK511_STRUCTURAL_DIVISIBILITY_REPAIR1_TERMINAL_TIMEOUT.md'

PARENT_PRE = 'bb2fc2636de21d8eed06e3694a128be34e5fede1'
Q18_PRE = 'e9fcf2308cbc1ebd5b9acbaeca676f58f9ce62b9'
EXPECTED_BASE_BLOB = '709904a582210642905ba053b5d622135da1067c'
EXPECTED_Q18_PREREG_BLOB = '050baee3d7aaa761fcb660a30b4aea1e9863db0a'
EXPECTED_PARENT_RAW_BLOB = 'ae24a97262e9dce596619fca447b32133df53ac3'
EXPECTED_FILTRATION_RAW_BLOB = '8c9f63eb787d3c84c707b89c9574d2c8938167ce'
EXPECTED_AUDIT_BLOB = '07c280e0e2bc68fbe96bccd007cb334f98af0460'
NSHARDS = 8
Q18 = 18
CLASS_PASS = 'K5_MASK511_LOWER_COEFFICIENTS_STRUCTURAL_DIVISIBILITY_EXACT_SCOPED'
CLASS_FAIL = 'K5_MASK511_RAY_CANCELLATION_NOT_ANGULAR_UNIFORM_EXACT_SCOPED'
CLASS_INVALID = 'K5_MASK511_STRUCTURAL_DIVISIBILITY_INVALID'


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def from_serial(rows):
    out = {}
    for mon, c in rows:
        m = tuple(int(x) for x in mon)
        z = Fraction(c)
        if z:
            out[m] = out.get(m, Fraction(0)) + z
    return {m:c for m,c in out.items() if c}


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shard-dir', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--coefficients', required=True)
    return ap.parse_args()


def main():
    args = parse_args()
    b = load_module(BASE_SOURCE, 'mask511_q18_aggregate_base')
    b.MAX_T = Q18

    parent = json.loads(PARENT_RAW.read_text(encoding='utf-8'))
    filt = json.loads(FILTRATION_RAW.read_text(encoding='utf-8'))
    audit_text = AUDIT.read_text(encoding='utf-8')
    timeout_text = TERMINAL_REPAIR1.read_text(encoding='utf-8')

    controls = {
        'q18_prereg_blob_locked': b.git_blob_sha1(Q18_PREREG) == EXPECTED_Q18_PREREG_BLOB,
        'base_blob_locked': b.git_blob_sha1(BASE_SOURCE) == EXPECTED_BASE_BLOB,
        'parent_raw_blob_locked': b.git_blob_sha1(PARENT_RAW) == EXPECTED_PARENT_RAW_BLOB,
        'filtration_raw_blob_locked': b.git_blob_sha1(FILTRATION_RAW) == EXPECTED_FILTRATION_RAW_BLOB,
        'audit_blob_locked': b.git_blob_sha1(AUDIT) == EXPECTED_AUDIT_BLOB,
        'repair1_terminal_cancelled_recorded': 'terminal status `completed`, conclusion `cancelled`' in timeout_text and 'aggregate job `105310317955` was `skipped`' in timeout_text,
        'structural_lower_bound18_audited': 'every numerator contribution has minimum t-degree `2j+10+2(4-j)=18`' in audit_text,
        'filtration_theorem_locked': filt.get('classification') == 'K5_MASK511_ANNIHILATOR_RAISES_FILTRATION_BY2_EXACT_SCOPED' and filt.get('filtration_bound',{}).get('operator_shift_lower_bound') == 2,
        'parent_ray_orders_locked': all(parent[w][f'channel_{c}']['rN'] == 19 and parent[w][f'channel_{c}']['rB'] == 21 for w in ('W1','W2') for c in (1,2)),
        'parent_ray_first_coefficients_nonzero': all(Fraction(parent[w][f'channel_{c}']['N_first_coefficient']) != 0 and Fraction(parent[w][f'channel_{c}']['B_first_coefficient']) != 0 for w in ('W1','W2') for c in (1,2)),
        'no_boundary_s5_transport_consumed': True,
    }

    shard_dir = Path(args.shard_dir)
    summaries = []
    payloads = []
    for sid in range(NSHARDS):
        sp = shard_dir / f'shard_{sid}_summary.json'
        pp = shard_dir / f'shard_{sid}_payload.json.gz'
        assert sp.exists(), sp
        assert pp.exists(), pp
        s = json.loads(sp.read_text(encoding='utf-8'))
        raw = gzip.decompress(pp.read_bytes())
        p = json.loads(raw.decode('utf-8'))
        controls[f'shard_{sid}_summary_pass'] = s.get('status') == 'SHARD_PASS_EXACT_CONTROL_ONLY' and all(s.get('checks',{}).values())
        controls[f'shard_{sid}_payload_hash'] = sha256_file(pp) == s.get('payload_sha256')
        controls[f'shard_{sid}_identity'] = s.get('shard') == sid and p.get('shard') == sid and s.get('q18_prereg_commit') == Q18_PRE and p.get('q18_prereg_commit') == Q18_PRE
        controls[f'shard_{sid}_no_scientific_verdict'] = s.get('scientific_classification') is None and s.get('boundary_s5_transport_consumed') is False
        summaries.append(s)
        payloads.append(p)

    all_indices = [idx for s in summaries for idx in s['matching_indices']]
    controls['complete_945_matching_coverage'] = sorted(all_indices) == list(range(945))
    controls['no_duplicate_matching_indices'] = len(all_indices) == len(set(all_indices)) == 945
    controls['all_eight_shards_present'] = len(summaries) == NSHARDS

    total = [[{},{}] for _ in range(2)]
    malformed_controls = []
    for p in payloads:
        for ch in (0,1):
            total[ch][0] = b.padd(total[ch][0], from_serial(p['channels'][str(ch+1)]['real']))
            total[ch][1] = b.padd(total[ch][1], from_serial(p['channels'][str(ch+1)]['imag']))
        if p.get('malformed_control') is not None:
            malformed_controls.append(p['malformed_control'])

    controls['physical_imaginary_q18_cancels_exactly'] = not total[0][1] and not total[1][1]
    controls['all_aggregate_terms_exact_q18'] = all(all(b.tdeg(m) == Q18 for m in total[ch][ri]) for ch in (0,1) for ri in (0,1))
    controls['malformed_plus1_source_coefficient_exposes_nonzero_q18'] = bool(malformed_controls) and all(x['delta_q18_stats']['terms'] > 0 for x in malformed_controls)

    valid = all(controls.values())
    q18_zero = [not total[ch][0] and not total[ch][1] for ch in (0,1)]
    if not valid:
        classification = CLASS_INVALID
        status = 'INVALID_IMPLEMENTATION'
    elif all(q18_zero):
        classification = CLASS_PASS
        status = 'PASS_EXACT_SCOPED'
    else:
        classification = CLASS_FAIL
        status = 'FAIL_EXACT_SCOPED'

    coeff = {
        'gate': 'K5_MASK511_STRUCTURAL_DIVISIBILITY_Q18_REDUCTION',
        'parent_prereg_commit': PARENT_PRE,
        'q18_prereg_commit': Q18_PRE,
        'mask': 511,
        'q': Q18,
        'channels': {
            '1': {'real': b.pserial(total[0][0]), 'imag': b.pserial(total[0][1])},
            '2': {'real': b.pserial(total[1][0]), 'imag': b.pserial(total[1][1])},
        },
    }
    coeff_path = Path(args.coefficients)
    coeff_path.parent.mkdir(parents=True, exist_ok=True)
    coeff_raw = json.dumps(coeff, separators=(',',':'), sort_keys=True).encode('utf-8')
    coeff_path.write_bytes(gzip.compress(coeff_raw, compresslevel=6, mtime=0))
    coeff_sha = sha256_file(coeff_path)

    channel_stats = {
        str(ch+1): {
            'q18_zero_exact': q18_zero[ch],
            'q18_real': b.pstats(total[ch][0]),
            'q18_imag': b.pstats(total[ch][1]),
            'structural_rN': 19 if valid and all(q18_zero) else None,
            'structural_rB': 21 if valid and all(q18_zero) else None,
        } for ch in (0,1)
    }

    out = {
        'gate': 'K5_MASK511_STRUCTURAL_DIVISIBILITY_Q18_REDUCTION',
        'parent_prereg_commit': PARENT_PRE,
        'q18_prereg_commit': Q18_PRE,
        'status': status,
        'classification': classification,
        'scope': {
            'mask': 511,
            'physical_channels': 2,
            'q18_only': True,
            'matching_count': 945,
            'boundary_s5_transport_consumed': False,
        },
        'activation_authority': {
            'repair1_run': 35246991631,
            'repair1_valid_complete_aggregate': False,
            'filtration_run': 35250988892,
            'parent_ray_run': 35226938480,
            'structural_minimum_before_cancellation': 18,
        },
        'channel_results': channel_stats,
        'logical_consequence_if_pass': 'Exact N_q18=0 plus structural q<18 impossibility and locked nonzero N_q19 rays imply N_c has exact global mask511 filtration order 19. The independently confirmed +2 annihilator theorem then gives B_v[N_c] in F^21, while locked nonzero B_q21 rays imply exact global action filtration order 21.',
        'controls': controls,
        'malformed_control_witness_count': len(malformed_controls),
        'coefficient_payload_sha256': coeff_sha,
        'scientific_corner_integrability_verdict': None,
        'global_stokes_ibp_verdict': None,
        'integrated_period_verdict': None,
        'finite_part_selector': None,
        'regulator_independence': None,
    }
    op = Path(args.output)
    op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True), flush=True)
    if not valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
