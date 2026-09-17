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


def pparse(rows):
    out = {}
    for mon, q in rows:
        out[tuple(int(x) for x in mon)] = Fraction(q)
    return out


def load_json_gz(path: Path):
    with gzip.open(path, 'rb') as f:
        return json.loads(f.read().decode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shard-dir', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--coefficients', required=True)
    args = ap.parse_args()
    b = load_module(BASE_SOURCE, 'mask511_struct_aggregate_base')

    checks = {
        'parent_prereg_locked': b.PRE == PRE,
        'repair_commit_locked': REPAIR == '16aac0291d9f129b61a3cfecadbab0803e83590a',
        'base_blob_locked': b.git_blob_sha1(BASE_SOURCE) == EXPECTED_BASE_BLOB,
        'mask511_frozen': b.MASK == 511,
        'eight_shards_frozen': NSHARDS == 8,
    }

    shard_dir = Path(args.shard_dir)
    summaries = []
    payloads = []
    for sid in range(NSHARDS):
        sp = shard_dir / f'shard_{sid}_summary.json'
        pp = shard_dir / f'shard_{sid}_payload.json.gz'
        s = json.loads(sp.read_text(encoding='utf-8'))
        p = load_json_gz(pp)
        summaries.append(s); payloads.append(p)
        checks[f'shard_{sid}_terminal_control_pass'] = s['status'] == 'SHARD_PASS_EXACT_CONTROL_ONLY' and all(s['checks'].values())
        checks[f'shard_{sid}_payload_hash'] = hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest() == s['payload_sha256']
        checks[f'shard_{sid}_identity'] = s['shard'] == sid and p['shard'] == sid and s['nshards'] == NSHARDS and p['nshards'] == NSHARDS
        checks[f'shard_{sid}_locks'] = s['prereg_commit'] == PRE and s['repair_commit'] == REPAIR and p['prereg_commit'] == PRE and p['repair_commit'] == REPAIR
        checks[f'shard_{sid}_no_s5'] = s['boundary_s5_transport_consumed'] is False

    all_indices = [idx for s in summaries for idx in s['matching_indices']]
    checks['matching_coverage_exact_0_944'] = sorted(all_indices) == list(range(945))
    checks['matching_coverage_no_duplicates'] = len(all_indices) == len(set(all_indices)) == 945
    checks['source_pattern_count_7776_all_shards'] = all(s['source_pattern_count'] == 7776 for s in summaries)
    checks['perfect_matchings_945_all_shards'] = all(s['perfect_matchings_total'] == 945 for s in summaries)

    # Exact aggregate of the eight disjoint matching partitions.
    partial = [[{} for _ in range(2)] for _ in range(2)]  # channel, real/imag
    for p in payloads:
        for ch in (0,1):
            for ri, name in ((0,'real'),(1,'imag')):
                for qv in range(KEEP_LO, KEEP_HI+1):
                    partial[ch][ri] = b.padd(partial[ch][ri], pparse(p['channels'][str(ch+1)][name][str(qv)]))

    # Aggregate physical imaginary cancellation is itself an exact control.
    checks['physical_numerator_imaginary_parts_cancel_exact_18_21'] = all(not partial[ch][1] for ch in (0,1))
    N = [partial[ch][0] for ch in (0,1)]
    checks['N_structural_min_t18'] = all((not N[ch]) or b.pmin_t(N[ch]) >= 18 for ch in (0,1))
    checks['N_degree27'] = all(all(b.totaldeg(m) == 27 for m in N[ch]) for ch in (0,1))

    print('aggregate loading action prefix', flush=True)
    ans = b.exact_prefix(b.ACTION_SOURCE, 'results={};checks={}', 'mask511_struct_aggregate_action')
    checks['action_blob_locked'] = b.git_blob_sha1(b.ACTION_SOURCE) == b.EXPECTED_ACTION_BLOB
    checks['action_source_terms_100000'] = ans['SOURCE_TERMS'] == 100000
    checks['annihilator_global_vpsi_zero'] = bool(ans['VPSI_ZERO'])
    checks['dual_projection_used'] = ans['PIV'] == [1,4]
    q = b.build_q_polys(ans)
    checks['q_degree3'] = all(all(b.totaldeg(m) == 3 for m in q[e]) for e in range(10))

    print('aggregate building exact annihilator action on summed numerator', flush=True)
    B = []
    for ch in (0,1):
        z, _ = b.action_on_poly(N[ch], q)
        B.append(z)
    checks['B_structural_min_t18'] = all((not B[ch]) or b.pmin_t(B[ch]) >= 18 for ch in (0,1))
    checks['B_degree31'] = all(all(b.totaldeg(m) == 31 for m in B[ch]) for ch in (0,1))

    parent = json.loads(b.PARENT_RAW.read_text(encoding='utf-8'))
    checks['parent_authority_run_locked'] = parent['source']['run_id'] == 35226938480
    checks['parent_orders_locked'] = all(parent[w][f'channel_{ch}']['rN'] == 19 and parent[w][f'channel_{ch}']['rB'] == 21 for w in ('W1','W2') for ch in (1,2))

    nslices = [{qv:b.pslice(N[ch],qv) for qv in range(KEEP_LO,KEEP_HI+1)} for ch in (0,1)]
    bslices = [{qv:b.pslice(B[ch],qv) for qv in range(KEEP_LO,KEEP_HI+1)} for ch in (0,1)]
    checks['all_targeted_lower_N_coefficients_zero_exact'] = all(not nslices[ch][18] for ch in (0,1))
    checks['all_targeted_lower_B_coefficients_zero_exact'] = all(not bslices[ch][qv] for ch in (0,1) for qv in (18,19,20))
    checks['N_q19_nonzero_both'] = all(bool(nslices[ch][19]) for ch in (0,1))
    checks['B_q21_nonzero_both'] = all(bool(bslices[ch][21]) for ch in (0,1))

    ray_checks = []
    for ch in (0,1):
        for wname, W in (('W1',b.W1),('W2',b.W2)):
            en = b.peval(nslices[ch][19], W)
            eb = b.peval(bslices[ch][21], W)
            okn = en == b.exact_expected(parent,wname,ch+1,'N_first_coefficient')
            okb = eb == b.exact_expected(parent,wname,ch+1,'B_first_coefficient')
            ray_checks.append({'channel':ch+1,'weight':wname,'N_q19':b.qstr(en),'B_q21':b.qstr(eb),'N_match':okn,'B_match':okb})
    checks['W1_W2_parent_first_coefficients_reproduced'] = all(r['N_match'] and r['B_match'] for r in ray_checks)

    candidates = []
    for p in payloads:
        m = p.get('malformed_control')
        if m is not None:
            dz = pparse(m['delta_N_q18'])
            if dz:
                candidates.append((int(m['global_matching_index']), m['matching'], dz))
    candidates.sort(key=lambda x:x[0])
    malformed = candidates[0] if candidates else None
    control_delta = {} if malformed is None else malformed[2]
    controls = {
        'perturbed_retained_source_coefficient_breaks_lower_zero': bool(control_delta),
        'perturbed_lower_q18_is_exact_nonzero': bool(control_delta) and b.pmin_t(control_delta) == 18,
        'wrong_mask_not_promoted': b.MASK == 511,
        'no_s5_transport_consumed': True,
        'no_numerical_identity_proof': True,
        'no_global_integrability_or_stokes_claim': True,
        'all_shards_required_before_classification': len(summaries) == NSHARDS and checks['matching_coverage_exact_0_944'],
    }

    lower_nonzero = []
    for ch in (0,1):
        if nslices[ch][18]: lower_nonzero.append({'channel':ch+1,'family':'N','order':18,'stats':b.pstats(nslices[ch][18])})
        for qv in (18,19,20):
            if bslices[ch][qv]: lower_nonzero.append({'channel':ch+1,'family':'B','order':qv,'stats':b.pstats(bslices[ch][qv])})

    scientific_keys = {'all_targeted_lower_N_coefficients_zero_exact','all_targeted_lower_B_coefficients_zero_exact','N_q19_nonzero_both','B_q21_nonzero_both'}
    valid_provenance = all(v for k,v in checks.items() if k not in scientific_keys) and all(controls.values())
    theorem = checks['all_targeted_lower_N_coefficients_zero_exact'] and checks['all_targeted_lower_B_coefficients_zero_exact'] and checks['N_q19_nonzero_both'] and checks['B_q21_nonzero_both']
    if not valid_provenance:
        status=b.CLASS_INVALID; classification=b.CLASS_INVALID
    elif theorem:
        status='PASS_EXACT_SCOPED'; classification=b.CLASS_PASS
    elif lower_nonzero:
        status='SCIENTIFIC_FAIL_EXACT_SCOPED'; classification=b.CLASS_FAIL
    else:
        status='BLOCKED_OBJECT_DEFINITION'; classification=b.CLASS_BLOCK

    coeff_payload = {'gate':'K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS','prereg_commit':PRE,'repair_commit':REPAIR,'channels':{}}
    channel_reports = []
    for ch in (0,1):
        coeff_payload['channels'][str(ch+1)] = {'N_q19':b.pserial(nslices[ch][19]),'B_q21':b.pserial(bslices[ch][21])}
        channel_reports.append({
            'channel':ch+1,
            'N_orders_0_19': {str(qv): b.pstats({}) for qv in range(0,18)} | {'18':b.pstats(nslices[ch][18]),'19':b.pstats(nslices[ch][19])},
            'B_orders_0_21': {str(qv): b.pstats({}) for qv in range(0,18)} | {str(qv):b.pstats(bslices[ch][qv]) for qv in (18,19,20,21)},
            'N_first_nonzero_target':b.pstats(nslices[ch][19]),
            'B_first_nonzero_target':b.pstats(bslices[ch][21]),
        })
    coeff_payload['malformed_control'] = {
        'matching_index': None if malformed is None else malformed[0],
        'matching': None if malformed is None else malformed[1],
        'delta_N_q18': b.pserial(control_delta),
    }
    coeff_raw = json.dumps(coeff_payload,sort_keys=True,separators=(',',':')).encode()
    coeff_sha = hashlib.sha256(coeff_raw).hexdigest()
    cp = Path(args.coefficients); cp.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(cp,'wb',compresslevel=9) as f: f.write(coeff_raw)

    out = {
        'gate':'K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS',
        'prereg_commit':PRE,'repair_commit':REPAIR,'status':status,'classification':classification,
        'scope':{'mask':511,'channels':[1,2],'boundary_s5_transport_consumed':False,'exact_t_window_materialized':[18,21],'structural_zero_window_N':[0,17],'structural_zero_window_B':[0,17]},
        'authority':{'parent_witness_run':parent['source']['run_id'],'parent_witness_full_json_sha256':parent['source']['full_json_sha256'],'action_git_blob_sha1':b.git_blob_sha1(b.ACTION_SOURCE)},
        'checks':checks,'controls':controls,'source_pattern_count':7776,'perfect_matchings_retained':945,
        'shard_count':NSHARDS,'channel_reports':channel_reports,'ray_reproduction':ray_checks,'lower_nonzero_witnesses':lower_nonzero,
        'malformed_control':None if malformed is None else {'matching_index':malformed[0],'matching':malformed[1],'delta_N_q18_stats':b.pstats(control_delta)},
        'coefficient_payload_sha256':coeff_sha,'coefficient_payload_gzip':cp.name,
        'scientific_corner_integrability_verdict':None,'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,'finite_part_selector':None,'regulator_independence':None,
    }
    op = Path(args.output); op.parent.mkdir(parents=True,exist_ok=True)
    op.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STATUS='+status)
    print('N_MIN_ORDERS=',[b.pmin_t(N[ch]) for ch in (0,1)])
    print('B_MIN_ORDERS=',[b.pmin_t(B[ch]) for ch in (0,1)])
    print('N_Q19_TERMS=',[len(nslices[ch][19]) for ch in (0,1)])
    print('B_Q21_TERMS=',[len(bslices[ch][21]) for ch in (0,1)])
    print('COEFF_SHA256='+coeff_sha)
    if status == b.CLASS_INVALID:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
