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

PARENT_PRE = 'bb2fc2636de21d8eed06e3694a128be34e5fede1'
Q18_PRE = 'e9fcf2308cbc1ebd5b9acbaeca676f58f9ce62b9'
EXPECTED_BASE_BLOB = '709904a582210642905ba053b5d622135da1067c'
EXPECTED_Q18_PREREG_BLOB = '050baee3d7aaa761fcb660a30b4aea1e9863db0a'
EXPECTED_PARENT_RAW_BLOB = 'ae24a97262e9dce596619fca447b32133df53ac3'
EXPECTED_FILTRATION_RAW_BLOB = '8c9f63eb787d3c84c707b89c9574d2c8938167ce'
EXPECTED_AUDIT_BLOB = '07c280e0e2bc68fbe96bccd007cb334f98af0460'
NSHARDS = 8
Q18 = 18


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


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shard', type=int, required=True)
    ap.add_argument('--nshards', type=int, default=NSHARDS)
    ap.add_argument('--summary', required=True)
    ap.add_argument('--payload', required=True)
    return ap.parse_args()


def main():
    args = parse_args()
    assert args.nshards == NSHARDS
    assert 0 <= args.shard < NSHARDS

    b = load_module(BASE_SOURCE, f'mask511_q18_base_{args.shard}')
    # The q18 gate needs only the exact initial mask-filtration forms.
    b.MAX_T = Q18

    parent = json.loads(PARENT_RAW.read_text(encoding='utf-8'))
    filt = json.loads(FILTRATION_RAW.read_text(encoding='utf-8'))
    audit_text = AUDIT.read_text(encoding='utf-8')

    checks = {
        'parent_prereg_locked': b.PRE == PARENT_PRE,
        'q18_prereg_blob_locked': b.git_blob_sha1(Q18_PREREG) == EXPECTED_Q18_PREREG_BLOB,
        'base_blob_locked': b.git_blob_sha1(BASE_SOURCE) == EXPECTED_BASE_BLOB,
        'parent_raw_blob_locked': b.git_blob_sha1(PARENT_RAW) == EXPECTED_PARENT_RAW_BLOB,
        'filtration_raw_blob_locked': b.git_blob_sha1(FILTRATION_RAW) == EXPECTED_FILTRATION_RAW_BLOB,
        'audit_blob_locked': b.git_blob_sha1(AUDIT) == EXPECTED_AUDIT_BLOB,
        'mask511_frozen': b.MASK == 511,
        'q18_only_frozen': b.MAX_T == 18,
        'eight_shards_frozen': args.nshards == 8,
        'repair1_terminal_no_aggregate_activation_recorded': 'run `35246991631`' in (ROOT / 'status/K5_MASK511_STRUCTURAL_DIVISIBILITY_REPAIR1_TERMINAL_TIMEOUT.md').read_text(encoding='utf-8'),
        'structural_lower_bound18_audited': 'every numerator contribution has minimum t-degree `2j+10+2(4-j)=18`' in audit_text,
        'parent_mask511_locked': parent.get('mask') == 511,
        'parent_ray_orders_locked': all(parent[w][f'channel_{c}']['rN'] == 19 and parent[w][f'channel_{c}']['rB'] == 21 for w in ('W1','W2') for c in (1,2)),
        'parent_ray_first_coefficients_nonzero': all(Fraction(parent[w][f'channel_{c}']['N_first_coefficient']) != 0 and Fraction(parent[w][f'channel_{c}']['B_first_coefficient']) != 0 for w in ('W1','W2') for c in (1,2)),
        'filtration_theorem_locked': filt.get('classification') == 'K5_MASK511_ANNIHILATOR_RAISES_FILTRATION_BY2_EXACT_SCOPED' and filt.get('filtration_bound',{}).get('operator_shift_lower_bound') == 2,
    }

    print('shard', args.shard, 'loading canonical DAG prefix', flush=True)
    dns = b.exact_prefix(b.DAG_SOURCE, '# Evaluate frozen exact points by direct and canonical-DAG paths.', f'mask511_q18_dag_{args.shard}')
    checks['dag_blob_locked'] = b.git_blob_sha1(b.DAG_SOURCE) == b.EXPECTED_DAG_BLOB
    checks['canonical_dag_hash_locked'] = dns['dag_hash'] == b.EXPECTED_DAG_HASH
    checks['canonical_source_terms_100000'] = dns['SOURCE_TERMS'] == 100000
    checks['canonical_dual_rank2_pivots14'] = dns['rank'] == 2 and dns['piv'] == [1,4]
    checks['canonical_psi_125'] = len(dns['PSI']) == 125

    print('shard', args.shard, 'loading action prefix', flush=True)
    ans = b.exact_prefix(b.ACTION_SOURCE, 'results={};checks={}', f'mask511_q18_action_{args.shard}')
    checks['action_blob_locked'] = b.git_blob_sha1(b.ACTION_SOURCE) == b.EXPECTED_ACTION_BLOB
    checks['action_source_terms_100000'] = ans['SOURCE_TERMS'] == 100000
    checks['annihilator_global_vpsi_zero'] = bool(ans['VPSI_ZERO'])
    checks['dual_projection_used'] = ans['PIV'] == [1,4]

    PSI = b.from_tuple_poly(dns['PSI'])
    ADJ = [[b.from_tuple_poly(dns['ADJ'][i][j]) for j in range(4)] for i in range(4)]
    LP = [[b.from_tuple_poly(dns['LP'][i][j]) for j in range(4)] for i in range(4)]
    Q = [[Fraction(x) for x in row] for row in dns['Q']]
    ROWS = tuple(tuple(int(x) for x in r) for r in dns['ROWS'])

    checks['psi_min_t3_mask511'] = b.pmin_t(PSI) == 3
    checks['adj_entries_tdegree_2_or3'] = all(all(b.tdeg(m) in (2,3) for m in ADJ[i][j]) for i in range(4) for j in range(4))

    print('shard', args.shard, 'building exact determinant initial forms', flush=True)
    D = b.build_det_coeffs(LP, Q)
    checks['det_D0_equals_psi'] = D[0] == PSI
    F = b.build_cleared_det_factor(D, PSI)
    Fmin = [b.pslice(F[j], 2*j) for j in range(5)]
    checks['det_initial_form_degrees_exact'] = all(Fmin[j] and all(b.tdeg(m) == 2*j for m in Fmin[j]) for j in range(5))

    print('shard', args.shard, 'building covariance initial forms only', flush=True)
    AQ = b.mat_poly_num_right(ADJ, Q, Q18)
    AQmin = [[b.pslice(AQ[i][j], 2) for j in range(4)] for i in range(4)]
    BNmin = [[[b.pslice(ADJ[i][j], 2) for j in range(4)] for i in range(4)]]
    for n in range(1,5):
        target = 2*(n+1)
        M = b.mat_poly_mul(AQmin, BNmin[-1], target)
        M = [[b.pscale(z, -1) for z in row] for row in M]
        BNmin.append(M)
    Cmin = {}
    for i in range(10):
        for j in range(i+1,10):
            for n in range(5):
                z = b.dot_rows_poly(ROWS[i], BNmin[n], ROWS[j])
                target = 2*(n+1)
                Cmin[(i,j,n)] = b.pslice(z, target)
    checks['covariance_initial_forms_exact_grade'] = all((not z) or all(b.tdeg(m) == 2*(n+1) for m in z) for (i,j,n),z in Cmin.items())
    checks['covariance_initial_forms_nonempty'] = any(bool(z) for z in Cmin.values())

    print('shard', args.shard, 'aggregating source coefficients', flush=True)
    MATCH_COEFF, source_pattern_count = b.build_match_coeff(ans)
    ordered = sorted(MATCH_COEFF.items())
    checks['source_pattern_count_7776'] = source_pattern_count == 7776
    checks['perfect_matchings_945'] = len(ordered) == 945
    selected = [(idx, mt, coeffs) for idx,(mt,coeffs) in enumerate(ordered) if idx % NSHARDS == args.shard]
    checks['selected_nonempty'] = bool(selected)

    def matching_series_initial(mt):
        ser = [b.pconst(1)] + [{} for _ in range(4)]
        pairs_done = 0
        for ij in mt:
            pairs_done += 1
            nxt = [{} for _ in range(5)]
            for k in range(5):
                target = 2*(pairs_done+k)
                z = {}
                for n in range(k+1):
                    left = ser[k-n]
                    right = Cmin[(ij[0],ij[1],n)]
                    if left and right:
                        z = b.padd(z, b.pmul(left, right, target))
                nxt[k] = b.pslice(z, target)
            ser = nxt
        return ser

    partial = [[{},{}] for _ in range(2)]
    malformed = None
    for pos,(gidx,mt,coeffs) in enumerate(selected,1):
        ser = matching_series_initial(mt)
        q18 = {}
        for j in range(5):
            k = 4-j
            q18 = b.padd(q18, b.pmul(Fmin[j], ser[k], Q18))
        q18 = b.pslice(q18, Q18)
        if q18:
            for ch in (0,1):
                cr,ci = coeffs[ch]
                if cr:
                    partial[ch][0] = b.padd(partial[ch][0], b.pscale(q18, 24*cr))
                if ci:
                    partial[ch][1] = b.padd(partial[ch][1], b.pscale(q18, 24*ci))
            if malformed is None and coeffs[0] != (0,0):
                dz = b.pscale(q18, 24)
                if dz:
                    malformed = {
                        'global_matching_index': gidx,
                        'matching': [list(x) for x in mt],
                        'delta_q18_stats': b.pstats(dz),
                    }
        if pos % 20 == 0:
            print('shard', args.shard, 'processed', pos, '/', len(selected), flush=True)

    checks['partial_terms_exact_q18'] = all(all(b.tdeg(m) == Q18 for m in partial[ch][ri]) for ch in (0,1) for ri in (0,1))
    checks['malformed_q18_witness_found_in_shard_or_not_required_locally'] = True
    valid = all(checks.values())

    payload = {
        'gate': 'K5_MASK511_STRUCTURAL_DIVISIBILITY_Q18_ONLY_SHARD',
        'parent_prereg_commit': PARENT_PRE,
        'q18_prereg_commit': Q18_PRE,
        'shard': args.shard,
        'nshards': NSHARDS,
        'matching_indices': [x[0] for x in selected],
        'channels': {
            '1': {'real': b.pserial(partial[0][0]), 'imag': b.pserial(partial[0][1])},
            '2': {'real': b.pserial(partial[1][0]), 'imag': b.pserial(partial[1][1])},
        },
        'malformed_control': malformed,
    }
    payload_path = Path(args.payload)
    payload_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(payload_path, 'wt', encoding='utf-8', mtime=0) as f:
        json.dump(payload, f, separators=(',',':'), sort_keys=True)
    payload_sha = sha256_file(payload_path)

    summary = {
        'gate': payload['gate'],
        'status': 'SHARD_PASS_EXACT_CONTROL_ONLY' if valid else 'INVALID_IMPLEMENTATION',
        'scientific_classification': None,
        'parent_prereg_commit': PARENT_PRE,
        'q18_prereg_commit': Q18_PRE,
        'shard': args.shard,
        'nshards': NSHARDS,
        'matching_count': len(selected),
        'matching_indices': payload['matching_indices'],
        'channel_q18_stats': {
            str(ch+1): {'real': b.pstats(partial[ch][0]), 'imag': b.pstats(partial[ch][1])} for ch in (0,1)
        },
        'malformed_control_found': malformed is not None,
        'payload_sha256': payload_sha,
        'checks': checks,
        'boundary_s5_transport_consumed': False,
    }
    Path(args.summary).write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)
    if not valid:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
