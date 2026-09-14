#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SNAP=ROOT/'sources'/'ITER079B_SM_EPRL_KKL_CAUSAL_COMPOSITION_INHERITANCE_SNAPSHOT.md'
PREREG=ROOT/'prereg'/'ITER079B_SM_EPRL_KKL_CAUSAL_COMPOSITION_INHERITANCE.md'
CUR=ROOT/'status'/'CURRENT.md'

def read(p): return p.read_text(encoding='utf-8')

def lane_a():
 s=read(SNAP)
 locks={
  'arbitrary_2cell':'arbitrary linear 2-cell spin foams' in s,
  'generic_boundaries':'generic LQG spin-network boundaries' in s,
  'arbitrary_valence':'arbitrary valency' in s,
  'orientation_duality':'dualizing the representation' in s,
  'parent_not_causal':'not a causal-Toller composition theorem' in s,
 }
 return {'iteration':'Iter079B-SM','lane':'A','valid':all(locks.values()),'scientific_outcome':'PASS' if all(locks.values()) else 'INVALID_SOURCE_LOCK','locks':locks}

def lane_b():
 s=read(SNAP); c=read(CUR)
 locks={
  'E1_source_explicit':'E1 arbitrary-2-complex causal orientation' in s and 'SOURCE_EXPLICIT' in s,
  'E2_source_explicit':'E2 generalized local causal vertex' in s,
  'iter079a_partial_bridge':'PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_BLOCKED' in c,
  'no_complete_multivertex':'no explicit complete multi-vertex causal distributional functional' in s,
 }
 return {'iteration':'Iter079B-SM','lane':'B','valid':all(locks.values()),'scientific_outcome':'PASS' if all(locks.values()) else 'INVALID_SOURCE_LOCK','locks':locks}

def lane_c():
 s=read(SNAP)
 missing=[]
 for eid in ('E3','E4','E5','E6'):
  row=next((x for x in s.splitlines() if x.startswith(f'| {eid} ')), '')
  if 'MISSING_REQUIRED_OBJECT' in row: missing.append(eid)
 locks={'all_E3_E6_missing':missing==['E3','E4','E5','E6'],'parent_not_silent_causal_bridge':'not by itself `CAUSAL_INHERITANCE_AUTHORITY`' in s,'scope_lock':'without adding a new physical choice' in s}
 return {'iteration':'Iter079B-SM','lane':'C','valid':all(locks.values()),'scientific_outcome':'BLOCKED' if all(locks.values()) else 'INVALID','locks':locks,'missing_required_elements':missing}

def lane_d():
 s=read(SNAP); c=read(CUR)
 missing=[]
 for eid in ('E7','E8'):
  row=next((x for x in s.splitlines() if x.startswith(f'| {eid} ')), '')
  if 'MISSING_REQUIRED_OBJECT' in row: missing.append(eid)
 locks={
  'E7_E8_missing':missing==['E7','E8'],
  'linear_transport_identity':'G(A_ext + h) = G(A_ext) + G(h)' in s,
  'selector_condition':'G|_H = 0' in s and 'independent selector fixes `h`' in s,
  'infinite_H':'countably infinite-dimensional' in c,
  'function_space_blocker':'FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR' in c,
 }
 return {'iteration':'Iter079B-SM','lane':'D','valid':all(locks.values()),'scientific_outcome':'BLOCKED' if all(locks.values()) else 'INVALID','locks':locks,'missing_required_elements':missing}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def aggregate(root):
 got={}
 for base,_,files in os.walk(root):
  for fn in files:
   if fn.endswith('.json'):
    try:o=json.loads(Path(base,fn).read_text())
    except Exception:continue
    if o.get('iteration')=='Iter079B-SM' and o.get('lane') in LANES: got[o['lane']]=o
 present=set(got)==set(LANES)
 valid=present and all(got[x].get('valid') for x in LANES)
 missing=sorted(set(got.get('C',{}).get('missing_required_elements',[])+got.get('D',{}).get('missing_required_elements',[])))
 if valid and missing==['E3','E4','E5','E6','E7','E8']:
  verdict='BLOCKED'; classification='ITER079B_SM_PARENT_COMPOSITION_SKELETON_EXISTS_BUT_CAUSAL_INHERITANCE_REQUIRES_NEW_BRIDGE_E3_E8_BLOCKED_EXACT_SOURCE_AUDIT'
 elif valid and not missing:
  verdict='PASS'; classification='ITER079B_SM_CAUSAL_COMPOSITION_INHERITANCE_EXACT_SOURCE_THEOREM_SCOPED'
 else:
  verdict='INVALID'; classification='ITER079B_SM_INVALID_SOURCE_OR_IMPLEMENTATION'
 return {'iteration':'Iter079B-SM','execution_valid':valid,'lane_scientific_outcomes':{k:got.get(k,{}).get('scientific_outcome') for k in LANES},'missing_required_elements':missing,'verdict':verdict,'classification':classification,'new_scientific_fact':'The parent EPRL-KKL algebraic composition skeleton does not by itself remove the need for a causal E3-E8 bridge; ordinary linear gluing transports supported extension ambiguity unless an annihilation theorem or selector is supplied.','next_admissible_gate':'Separate E3-E6 algebraic inheritance from E7-E8 distributional transport. Search for a source-derived causal gluing functional or prove a no-new-choice obstruction on a minimal two-vertex foam.','claim_lock':'No full causal multivertex amplitude theorem, no unique extension, no regulator independence, no RG/G3/F9/G8/K5 promotion, no new physics.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
 if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
 obj=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
 p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(obj,indent=2,sort_keys=True))
 if a.lane and not obj['valid']: raise SystemExit(1)
 if a.aggregate_dir and not obj['execution_valid']: raise SystemExit(1)
if __name__=='__main__': main()
