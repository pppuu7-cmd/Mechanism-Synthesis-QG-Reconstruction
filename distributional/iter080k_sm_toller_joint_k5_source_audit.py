#!/usr/bin/env python3
import argparse, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/'prereg'/'ITER080K_SM_NEW_TOLLER_ANALYTICITY_JOINT_K5_SELECTOR_AUDIT.md'
S=ROOT/'sources'/'ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md'
PASS_BLOCK='ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_UNIQUELY_FIXES_ONE_WEDGE_BRANCHES_BUT_DOES_NOT_EXPLICITLY_SELECT_JOINT_K5_EXTENSION_SOURCE_BRIDGE_BLOCKED_SCOPED'
PASS_FOUND='ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_SUPPLIES_EXPLICIT_JOINT_K5_EXTENSION_SELECTOR_SOURCE_CANDIDATE_SCOPED'
FAIL='SCIENTIFIC_FAIL_SOURCE_CHARACTERIZATION_SCOPED'

def wr(o,p): pathlib.Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def A():
 t=P.read_text(); s=S.read_text()
 c={'source_id': 'arXiv:2604.24945' in t and 'arXiv:2604.24945' in s,
    'new_primary_route_frozen':'NEW_PRIMARY_AUTHORITY' in t,
    'joint_question_frozen':'joint ten-wedge K5 distributional extension' in t}
 return {'lane':'A','checks':c,'pass':all(c.values())}
def B():
 s=S.read_text()
 c={'p1_true':'P1 `ONE_WEDGE_UNIQUENESS_EXPLICIT` = **true**' in s,
    'analytic_uniqueness_evidence':'Eqs. (17)–(20)' in s and 'Uniqueness' in s,
    'p5_true':'P5 `NO_REPRESENTATION_COMPOSITION_ASSUMPTION` = **true**' in s,
    'nonrepresentation_evidence':'do **not** provide a representation' in s}
 return {'lane':'B','checks':c,'pass':all(c.values())}
def C():
 s=S.read_text()
 c={'systematic_audit':'Systematic audit for a joint-K5 collision-extension selector' in s,
    'p2_false':'P2 `JOINT_K5_OBJECT_EXPLICIT` = **false**' in s,
    'p3_false':'P3 `CORRELATED_JOINT_K5_EXTENSION_RULE_EXPLICIT` = **false**' in s,
    'p4_false':'P4 `ITER077Q_TANGENTIAL_SELECTION_POWER_EXPLICIT` = **false**' in s,
    'term_families':all(x in s for x in ['`K5`','`multi-wedge`','simultaneous collision','correlated multi-wedge prescription','wavefront/microlocal extension rule'])}
 return {'lane':'C','checks':c,'pass':all(c.values())}
def D():
 p=P.read_text(); s=S.read_text()
 c={'no_rep_comp':'cannot be inferred by ordinary representation multiplication/composition' in s,
    'one_vs_joint_distinct':'One-wedge analytic uniqueness and joint-K5 distributional-extension uniqueness are distinct objects.' in p,
    'claim_locks':all(x in p for x in ['NEW_PHYSICS_FOUND','no CRQN v0.3','no G3 PASS','no F9/G8/K5 promotion'])}
 return {'lane':'D','checks':c,'pass':all(c.values())}
def agg(root):
 ds=[]
 for f in pathlib.Path(root).rglob('*.json'):
  try:
   d=json.loads(f.read_text())
   if d.get('lane') in 'ABCD': ds.append(d)
  except: pass
 by={d['lane']:d for d in ds}; complete=set(by)==set('ABCD')
 ok=complete and all(by[k].get('pass') for k in 'ABCD')
 # Source matrix freezes P1/P5 true and P2-P4 false; if lanes validate it, source bridge is blocked.
 cl=PASS_BLOCK if ok else FAIL; verdict='BLOCKED_SOURCE_BRIDGE_SCOPED' if ok else FAIL
 return {'lane':'aggregate','complete':complete,'execution_valid':complete,'lane_pass':{k:by.get(k,{}).get('pass') for k in 'ABCD'},'classification':cl,'verdict':verdict}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); ap.add_argument('--input-root',default='.'); a=ap.parse_args()
 fs={'A':A,'B':B,'C':C,'D':D}; o=fs[a.lane]() if a.lane in fs else agg(a.input_root); wr(o,a.out); print(json.dumps(o,indent=2,sort_keys=True))
 if a.lane in fs and not o['pass']: sys.exit(2)
 if a.lane=='aggregate' and not o['execution_valid']: sys.exit(3)
if __name__=='__main__': main()
