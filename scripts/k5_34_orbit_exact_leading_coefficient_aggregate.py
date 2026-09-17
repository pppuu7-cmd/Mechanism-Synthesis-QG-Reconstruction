#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PRE='d6b0e805101c8590eafac71398cc2b1466691752'
CLASS_PASS='K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_EXACT_SCOPED'
CLASS_PART='K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_PARTIAL_BLOCKED_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
MASK511_AUTH=ROOT/'results/raw/k5_mask511_physical_numerator_action_exact_corner_witness_authoritative.json'
CRITIC_AUTH=ROOT/'results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json'


def fq(x):return Fraction(x)
def sha_obj(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--shard-dir',required=True);ap.add_argument('--u-result',required=True);ap.add_argument('--output',required=True);ap.add_argument('--coefficients',required=True);args=ap.parse_args()
    sd=Path(args.shard_dir);shards=[]
    for s in range(8):
        p=sd/f'shard_{s}.json';assert p.exists(),p
        d=json.loads(p.read_text(encoding='utf-8'));shards.append(d)
    rows=[r for d in shards for r in d['rows']];rows.sort(key=lambda r:r['orbit_index'])
    masks=[r['mask'] for r in rows];indices=[r['orbit_index'] for r in rows]
    static_all=all(all(d['static_checks'].values()) for d in shards)
    shard_contract=all(d['prereg_commit']==PRE and d['shard']==s and d['nshards']==8 and d['status']=='SHARD_COMPLETE_EXACT_CONTROL_ONLY' and d['scientific_classification'] is None for s,d in enumerate(shards))
    coverage=(indices==list(range(32)) and len(set(masks))==32)
    expected_masks=[1,3,7,15,19,20,21,23,28,29,31,54,55,58,59,62,63,126,127,183,184,185,187,191,207,220,221,223,254,255,495,511]
    coverage=coverage and masks==expected_masks
    route_all=all(all(r['route_checks'].values()) for r in rows)
    s5_all=all(all(r['s5_full_coefficient_checks'].values()) for r in rows)
    second=[r['second_path'] for r in rows if r['second_path'] is not None]
    second_classes=sorted(tuple(x['class']) for x in second)
    expected_classes=sorted(set((r['orbit_size'],r['k']) for r in rows))
    second_all=(second_classes==expected_classes and len(second)==len(expected_classes) and all(x['all_exact'] for x in second))
    complete_vectors=True
    agreements=True
    component_rows=[]
    for r in rows:
        for ch in r['channels']:
            for w in ('W1','W2'):
                complete_vectors &= len(ch[w]['N_coefficients'])==28 and len(ch[w]['B_coefficients'])==32
            agr=ch['W1_W2_N_state_order_agree'] and ch['W1_W2_B_state_order_agree'];agreements &= agr
            component_rows.append({
                'orbit_index':r['orbit_index'],'mask':r['mask'],'k':r['k'],'orbit_size':r['orbit_size'],'channel':ch['channel'],
                'rN':ch['W1']['rN'] if agr else None,'rB':ch['W1']['rB'] if agr else None,
                'N_exact_zero':ch['W1']['N_exact_zero'] if agr else None,'B_exact_zero':ch['W1']['B_exact_zero'] if agr else None,
                'W1_N_sha256':ch['W1']['N_sha256'],'W2_N_sha256':ch['W2']['N_sha256'],
                'W1_B_sha256':ch['W1']['B_sha256'],'W2_B_sha256':ch['W2']['B_sha256'],
                'certified':bool(agr),
            })

    u=json.loads(Path(args.u_result).read_text(encoding='utf-8'))
    u_controls=all(u.get('controls',{}).values())
    u_valid=(u.get('classification')=='K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDERS_RESOLVED_SCOPED' and u.get('degree_ceiling')==5 and len(u.get('orbit_rows',[]))==32 and u_controls and u.get('summary',{}).get('route_a_b_exact',True))
    umap={r['mask']:r for r in u['orbit_rows']}
    u_complete=True
    for m in masks:
        ur=umap.get(m);u_complete &= ur is not None
        if ur is None:continue
        lanes=ur.get('lanes',{})
        for w in ('W1','W2','S5_W1','S5_W2'):
            u_complete &= w in lanes and len(lanes[w]['coefficients'])==6
        u_complete &= lanes['W1']['first_nonzero_order']==lanes['W2']['first_nonzero_order']
    for cr in component_rows:
        ur=umap.get(cr['mask']);cr['rU']=None if ur is None else ur['lanes']['W1']['first_nonzero_order'];cr['U_certified']=ur is not None

    m511=json.loads(MASK511_AUTH.read_text(encoding='utf-8'))
    row511=next(r for r in rows if r['mask']==511)
    mask511_checks=[]
    for ch in (1,2):
        rr=next(x for x in row511['channels'] if x['channel']==ch)
        for w in ('W1','W2'):
            auth=m511[w][f'channel_{ch}'];nv=rr[w]['N_coefficients'];bv=rr[w]['B_coefficients']
            rN=rr[w]['rN'];rB=rr[w]['rB']
            mask511_checks.append(rN==auth['rN'] and rB==auth['rB'] and fq(nv[rN])==fq(auth['N_first_coefficient']) and fq(bv[rB])==fq(auth['B_first_coefficient']))
    mask511_parent_reproduced=all(mask511_checks)

    critic=json.loads(CRITIC_AUTH.read_text(encoding='utf-8'))
    critic_locked=(critic.get('classification')=='CONFIRMED_EXACT_SCOPED' and critic.get('production',{}).get('run_id')==35267432939 and critic.get('q18_values_used') is False)

    controls={
        'parent_prereg_locked':all(d['prereg_commit']==PRE for d in shards),
        'eight_shards_complete':len(shards)==8,
        'shard_contract_exact':shard_contract,
        'static_source_authority_all_shards':static_all,
        'proper_orbit_coverage_exact_32':coverage,
        'complete_N0_27_B0_31_vectors_all64_both_weights':complete_vectors,
        'route_internal_exact_controls_all':route_all,
        'S5_full_coefficient_covariance_all':s5_all,
        'second_path_all_orbit_size_collision_size_classes':second_all,
        'W1_W2_zero_state_and_first_order_agree_all64':agreements,
        'projective_normal_full_degree5_authority_recomputed':u_valid and u_complete,
        'mask511_parent_N19_B21_reproduced_exact':mask511_parent_reproduced,
        'independent_boundary_s5_critic_authority_locked':critic_locked,
        'no_global_stokes_or_period_claim':True,
        'no_finite_part_or_regulator_claim':True,
    }
    implementation_valid=all(controls.values())
    all_certified=all(r['certified'] and r['U_certified'] for r in component_rows) and len(component_rows)==64
    if not implementation_valid:
        status=INVALID;classification=INVALID
    elif all_certified:
        status='PASS_EXACT_SCOPED';classification=CLASS_PASS
    else:
        status='PASS_EXACT_PARTIAL_BLOCKED_SCOPED';classification=CLASS_PART

    coeff_payload={
        'gate':'K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION',
        'prereg_commit':PRE,'N_degree_ceiling':27,'B_degree_ceiling':31,'U_degree_ceiling':5,
        'orbit_rows':rows,'projective_normal_result':u,
    }
    raw=json.dumps(coeff_payload,sort_keys=True,separators=(',',':')).encode();coeff_sha=hashlib.sha256(raw).hexdigest()
    cp=Path(args.coefficients);cp.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(cp,'wb',compresslevel=9) as f:f.write(raw)
    out={
        'gate':'K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION','prereg_commit':PRE,
        'status':status,'classification':classification,'controls':controls,
        'proper_orbits':32,'physical_channel_orbit_components':64,'certified_components':sum(r['certified'] and r['U_certified'] for r in component_rows),
        'component_rows':component_rows,'second_path_classes':[list(x) for x in expected_classes],
        'coefficient_payload_sha256':coeff_sha,'coefficient_payload_gzip':cp.name,
        'projective_normal_source_run':u.get('source',{}).get('run_id'),'boundary_s5_critic_run':critic.get('production',{}).get('run_id'),
        'physical_corner_finiteness_verdict':None,'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,
        'finite_part_selector':None,'regulator_independence':None,
    }
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification);print('STATUS='+status);print('CERTIFIED=',out['certified_components'],'/64');print('COEFF_SHA256='+coeff_sha)

if __name__=='__main__':main()
