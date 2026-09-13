#!/usr/bin/env python3
import glob,json
files=sorted(glob.glob('iter063a_lanes/**/iter063a_lane_*.json',recursive=True))
rows=[json.load(open(f)) for f in files]
expected={(m,c) for m in range(8) for c in (-1,1)}
keys={(r['mask'],r['global_c']) for r in rows}
structural=len(rows)==16 and keys==expected and all(r.get('all_valid') and r.get('tree_cycle_independent') and r.get('reversal_covariant') and r.get('cases')==384 for r in rows)
pair_ok=True
for m in range(8):
    a=next((r for r in rows if r['mask']==m and r['global_c']==1),None)
    b=next((r for r in rows if r['mask']==m and r['global_c']==-1),None)
    pair_ok &= bool(a and b and a['strong_permutations']==b['strong_permutations'] and a['non_strong_permutations']==b['non_strong_permutations'])
all_valid=bool(structural and pair_ok)
classification='K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENT' if all_valid else 'K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_DEPENDENCE_FAIL'
out={'iteration':'Iter063A','classification':classification,'all_valid':all_valid,'lane_files':len(rows),'total_tree_cases':sum(r.get('cases',0) for r in rows),'global_convention_pair_invariant':pair_ok,'interpretation':'exact K4 ordered-sign tree/fundamental-cycle representation independence prerequisite only; no causal amplitude/EPRL amplitude claim','claim_locks':['no physical causal-sector selection','no causal-vertex finiteness/divergence theorem','no K5/G3/F9/G8 promotion','no NEW_PHYSICS_FOUND']}
open('iter063a_tree_cycle_prescription_aggregate.json','w').write(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
if not all_valid: raise SystemExit(2)
