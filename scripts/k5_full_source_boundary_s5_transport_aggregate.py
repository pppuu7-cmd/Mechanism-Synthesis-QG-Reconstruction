#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

ROOT=Path(__file__).resolve().parents[1]
ACTION=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
REPAIR5_RAW=ROOT/'results/raw/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic_repair5_authoritative.json'
PREREG='6ac6e7749783b78fb0966450a91d8042c1ad0ca4'
ACTION_BLOB='2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
MARKER='results={};checks={}'
LABELS=('W1_C','W1_Cinv','W1_T','W2_C','W2_Cinv','W2_T')
C=(1,2,3,4,0);CI=(4,0,1,2,3);T=(1,0,2,3,4)

C_TRIV='K5_FULL_SOURCE_BOUNDARY_S5_CONTRAGREDIENT_TRIVIAL_CHARACTER_EXACT_SCOPED'
C_ORIENT='K5_FULL_SOURCE_BOUNDARY_S5_CONTRAGREDIENT_ORIENTATION_CHARACTER_EXACT_SCOPED'
C_FAIL='K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBSTRUCTION_EXACT_SCOPED'
C_BLOCK='BLOCKED_OBJECT_DEFINITION'
INVALID='INVALID_IMPLEMENTATION'

def git_blob_sha(path):
    raw=path.read_bytes();return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def load_action_prefix():
    assert git_blob_sha(ACTION)==ACTION_BLOB
    text=ACTION.read_text(encoding='utf-8');assert text.count(MARKER)==1
    ns={'__name__':'k5_full_source_agg_prefix','__file__':str(ACTION),'__package__':None}
    exec(compile(text.split(MARKER,1)[0],str(ACTION),'exec'),ns,ns)
    assert 'results' not in ns
    return SimpleNamespace(**ns)
act=load_action_prefix()

def mm(A,B):
    BT=list(zip(*B));return [[sum((x*y for x,y in zip(row,col)),Fraction(0)) for col in BT] for row in A]
def eye(n):return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def eq(A,B):return A==B
def load_shards(path):
    out={}
    for f in Path(path).glob('*.json'):
        d=json.loads(f.read_text(encoding='utf-8'))
        if d.get('gate')=='K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBJECT_DEFINITION_SHARD':
            lab=d['label'];assert lab not in out;out[lab]=d
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--shards',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    shards=load_shards(args.shards)
    tensors=act.reach.local_tensor_vectors(act.src);local=act.reach.local_action_matrices(tensors)
    AC=act.reach.global_action_matrix(act.src,C,local);ACI=act.reach.global_action_matrix(act.src,CI,local);AT=act.reach.global_action_matrix(act.src,T,local);P=act.P
    r5=json.loads(REPAIR5_RAW.read_text(encoding='utf-8'))
    checks={
      'prereg_locked':PREREG=='6ac6e7749783b78fb0966450a91d8042c1ad0ca4',
      'action_blob_locked':git_blob_sha(ACTION)==ACTION_BLOB,
      'exact_six_labels':set(shards)==set(LABELS),
      'all_shards_pass':len(shards)==6 and all(d['status']=='PASS_EXACT_SHARD' and all(d['checks'].values()) for d in shards.values()),
      'all_shards_full_32_100000':len(shards)==6 and all(d['boundary_components']==32 and d['source_terms']==100000 for d in shards.values()),
      'all_route_A_B_exact':len(shards)==6 and all(d['route_A_B_exact'] for d in shards.values()),
      'cycle_inverse_group_exact':mm(AC,ACI)==eye(32) and mm(ACI,AC)==eye(32),
      'odd_transposition_square_exact':mm(AT,AT)==eye(32),
      'cycle_reynolds_bilateral_invariance':mm(AC,P)==P and mm(P,AC)==P,
      'reynolds_pivots_14':list(act.PIV)==[1,4],
      'repair5_source_fixed_classification_retained':r5['classification']=='BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT' and r5['unique_consistent_law'] is None,
      'repair5_coordinate_extraction_was_exact':r5['coordinate_extraction_exact_all'] is True,
      'odd_transposition_negative_no_transpose_control':bool(shards.get('W1_T',{}).get('checks',{}).get('naive_no_transpose_negative_control_fails_law',False)),
      'no_physical_corner_coefficients':len(shards)==6 and all(d['physical_corner_coefficients_used'] is False for d in shards.values()),
    }
    valid=all(checks.values())
    triv=valid and all(shards[l]['trivial_character_contragredient_exact'] for l in LABELS)
    orient=valid and all(shards[l]['orientation_character_contragredient_exact'] for l in LABELS)
    if not valid:cls=INVALID
    elif triv and not orient:cls=C_TRIV
    elif orient and not triv:cls=C_ORIENT
    elif not triv and not orient:cls=C_FAIL
    else:cls=C_BLOCK
    lane_summary={l:{
      'permutation_sign':shards[l]['permutation_sign'],
      'orientation_reversals':shards[l]['orientation_reversals'],
      'route_A_B_exact':shards[l]['route_A_B_exact'],
      'trivial_character_exact':shards[l]['trivial_character_contragredient_exact'],
      'orientation_character_exact':shards[l]['orientation_character_contragredient_exact'],
      'base_dual_coordinates':shards[l]['base_dual_coordinates'],
      'target_dual_coordinates':shards[l]['target_dual_coordinates'],
    } for l in LABELS}
    out={
      'gate':'K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBJECT_DEFINITION',
      'prereg_commit':PREREG,'classification':cls,
      'checks':checks,'lane_summary':lane_summary,
      'trivial_character_global_exact':triv,'orientation_character_global_exact':orient,
      'source_fixed_repair5_classification':r5['classification'],
      'scientific_verdict':cls if cls not in (INVALID,C_BLOCK) else None,
      'physical_corner_coefficients_used':False,
      'interpretation_ceiling':'Full-source order-zero S5 transport only; no corner exponent, Stokes/IBP, K5 period, finite part, regulator independence, downstream QG promotion or complete-QG claim.',
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'classification':cls,'trivial_character_global_exact':triv,'orientation_character_global_exact':orient,'checks_all':valid,'lanes':{k:{'trivial':v['trivial_character_exact'],'orientation':v['orientation_character_exact']} for k,v in lane_summary.items()}},indent=2,sort_keys=True))
    return 2 if cls==INVALID else 0
if __name__=='__main__':raise SystemExit(main())
