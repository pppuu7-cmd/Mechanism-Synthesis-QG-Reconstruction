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
PRE = 'bb2fc2636de21d8eed06e3694a128be34e5fede1'
REPAIR = '16aac0291d9f129b61a3cfecadbab0803e83590a'
EXPECTED_BASE_BLOB = '709904a582210642905ba053b5d622135da1067c'
NSHARDS = 8
KEEP_LO = 18
KEEP_HI = 21


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


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
    assert 0 <= args.shard < args.nshards
    b = load_module(BASE_SOURCE, 'mask511_struct_base')
    checks = {
        'parent_prereg_locked': b.PRE == PRE,
        'repair_commit_locked': REPAIR == '16aac0291d9f129b61a3cfecadbab0803e83590a',
        'base_blob_locked': b.git_blob_sha1(BASE_SOURCE) == EXPECTED_BASE_BLOB,
        'mask511_frozen': b.MASK == 511,
        'max_t21_frozen': b.MAX_T == 21,
        'eight_shards_frozen': args.nshards == 8,
    }

    print('shard', args.shard, 'loading canonical DAG prefix', flush=True)
    dns = b.exact_prefix(b.DAG_SOURCE, '# Evaluate frozen exact points by direct and canonical-DAG paths.', f'mask511_shard_dag_{args.shard}')
    checks['dag_blob_locked'] = b.git_blob_sha1(b.DAG_SOURCE) == b.EXPECTED_DAG_BLOB
    checks['canonical_dag_hash_locked'] = dns['dag_hash'] == b.EXPECTED_DAG_HASH
    checks['canonical_source_terms_100000'] = dns['SOURCE_TERMS'] == 100000
    checks['canonical_dual_rank2_pivots14'] = dns['rank'] == 2 and dns['piv'] == [1,4]
    checks['canonical_psi_125'] = len(dns['PSI']) == 125

    print('shard', args.shard, 'loading action prefix', flush=True)
    ans = b.exact_prefix(b.ACTION_SOURCE, 'results={};checks={}', f'mask511_shard_action_{args.shard}')
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

    print('shard', args.shard, 'building determinant factor polynomials', flush=True)
    D = b.build_det_coeffs(LP, Q)
    checks['det_D0_equals_psi'] = D[0] == PSI
    F = b.build_cleared_det_factor(D, PSI)
    checks['cleared_det_degrees'] = all(all(b.totaldeg(m) == 3*j for m in F[j]) for j in range(5))
    checks['cleared_det_min_t'] = all(b.pmin_t(F[j]) == 2*j for j in range(1,5))

    print('shard', args.shard, 'building inverse/covariance numerator series', flush=True)
    AQ = b.mat_poly_num_right(ADJ, Q)
    BN = [ADJ]
    for n in range(1,5):
        maxt = min(b.MAX_T, 2*(n+1)+3)
        BN.append([[b.pscale(z,-1) for z in row] for row in b.mat_poly_mul(AQ, BN[-1], maxt)])
    C = {}
    for i in range(10):
        for j in range(i+1,10):
            for n in range(5):
                C[(i,j,n)] = b.dot_rows_poly(ROWS[i], BN[n], ROWS[j])
    checks['covariance_degree_locks'] = all(all(b.totaldeg(m) == 3*(n+1) for m in C[(i,j,n)])
        for i in range(10) for j in range(i+1,10) for n in range(5))
    checks['covariance_min_t_locks'] = all(b.pmin_t(C[(i,j,n)]) >= 2*(n+1)
        for i in range(10) for j in range(i+1,10) for n in range(5) if C[(i,j,n)])

    print('shard', args.shard, 'aggregating full all32/100000 source coefficients', flush=True)
    MATCH_COEFF, source_pattern_count = b.build_match_coeff(ans)
    ordered = sorted(MATCH_COEFF.items())
    checks['source_pattern_count_7776'] = source_pattern_count == 7776
    checks['perfect_matchings_945'] = len(ordered) == 945
    selected = [(idx, mt, coeffs) for idx, (mt, coeffs) in enumerate(ordered) if idx % args.nshards == args.shard]
    checks['selected_nonempty'] = bool(selected)
    print('shard', args.shard, 'selected matchings', len(selected), 'of', len(ordered), flush=True)

    # Exact partial numerator dictionaries. The Wick sum is linear in the retained matching
    # coefficients, so these partial dictionaries may be summed exactly after all shards finish.
    partial = [[{}, {}] for _ in range(2)]
    malformed = None
    for pos, (gidx, mt, coeffs) in enumerate(selected, 1):
        ser = b.matching_series(mt, C)
        prods = []
        for j in range(5):
            k = 4-j
            prods.append(b.pmul(F[j], ser[k], b.MAX_T))
        for ch in (0,1):
            cr, ci = coeffs[ch]
            if cr:
                z = {}
                for p in prods:
                    z = b.padd(z, b.pscale(p, 24*cr))
                partial[ch][0] = b.padd(partial[ch][0], z)
            if ci:
                z = {}
                for p in prods:
                    z = b.padd(z, b.pscale(p, 24*ci))
                partial[ch][1] = b.padd(partial[ch][1], z)
        if malformed is None and coeffs[0] != (0,0):
            dz = {}
            for p in prods:
                dz = b.padd(dz, p)
            dz = b.pscale(b.pslice(dz, 18), 24)
            if dz:
                malformed = {'global_matching_index': gidx, 'matching': [list(x) for x in mt], 'delta_N_q18': dz}
        if pos % 25 == 0:
            print('shard', args.shard, 'processed', pos, '/', len(selected), flush=True)

    # Retain only the frozen exact window. q<18 is structurally impossible by the checked
    # determinant/covariance lower-degree bounds; q>21 cannot feed the parent B<=21 target.
    payload = {
        'gate': 'K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS_SHARD',
        'prereg_commit': PRE,
        'repair_commit': REPAIR,
        'shard': args.shard,
        'nshards': args.nshards,
        'matching_indices': [x[0] for x in selected],
        'channels': {},
        'malformed_control': None,
    }
    for ch in (0,1):
        payload['channels'][str(ch+1)] = {'real': {}, 'imag': {}}
        for ri, name in ((0,'real'),(1,'imag')):
            for qv in range(KEEP_LO, KEEP_HI+1):
                payload['channels'][str(ch+1)][name][str(qv)] = b.pserial(b.pslice(partial[ch][ri], qv))
    if malformed is not None:
        payload['malformed_control'] = {
            'global_matching_index': malformed['global_matching_index'],
            'matching': malformed['matching'],
            'delta_N_q18': b.pserial(malformed['delta_N_q18']),
        }

    raw = json.dumps(payload, sort_keys=True, separators=(',',':')).encode()
    payload_sha = hashlib.sha256(raw).hexdigest()
    pp = Path(args.payload); pp.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(pp, 'wb', compresslevel=6) as f:
        f.write(raw)

    summary = {
        'gate': payload['gate'], 'status': 'SHARD_PASS_EXACT_CONTROL_ONLY',
        'prereg_commit': PRE, 'repair_commit': REPAIR,
        'shard': args.shard, 'nshards': args.nshards,
        'checks': checks,
        'source_pattern_count': source_pattern_count,
        'perfect_matchings_total': len(ordered),
        'matching_count': len(selected),
        'matching_indices': payload['matching_indices'],
        'payload_sha256': payload_sha,
        'payload_gzip': pp.name,
        'malformed_candidate_index': None if malformed is None else malformed['global_matching_index'],
        'scientific_classification': None,
        'boundary_s5_transport_consumed': False,
    }
    assert all(checks.values()), checks
    sp = Path(args.summary); sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print('SHARD_STATUS=SHARD_PASS_EXACT_CONTROL_ONLY')
    print('SHARD=', args.shard, 'MATCHINGS=', len(selected), 'PAYLOAD_SHA256=', payload_sha)


if __name__ == '__main__':
    main()
