#!/usr/bin/env python3
import glob, json

files=sorted(glob.glob('iter062_lanes/**/iter062_lane_*.json',recursive=True))
rows=[]
for fn in files:
    with open(fn) as f: rows.append(json.load(f))
keys={(r['sigma_mask'],r['global_c']) for r in rows}
expected={(m,c) for m in range(8) for c in (-1,1)}
structural=(len(rows)==16 and keys==expected and all(r.get('all_valid') for r in rows))
pair_ok=True
for m in range(8):
    rp=next((r for r in rows if r['sigma_mask']==m and r['global_c']==1),None)
    rm=next((r for r in rows if r['sigma_mask']==m and r['global_c']==-1),None)
    pair_ok &= bool(rp and rm and rp['base_strong']==rm['base_strong'])
strong_plus=sum(1 for r in rows if r['global_c']==1 and r['base_strong'])
strong_minus=sum(1 for r in rows if r['global_c']==-1 and r['base_strong'])
census_invariant=(strong_plus==strong_minus)
all_valid=bool(structural and pair_ok and census_invariant)
classification='K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED' if all_valid else 'K4_ORDERED_ORIENTATION_BRIDGE_COVARIANCE_FAIL'
out={
 'iteration':'Iter062','classification':classification,'all_valid':all_valid,'lane_files':len(rows),
 'pairwise_global_convention_status_invariant':pair_ok,'strong_sigma_classes_c_plus':strong_plus,
 'strong_sigma_classes_c_minus':strong_minus,'non_strong_sigma_classes_c_plus':8-strong_plus,
 'non_strong_sigma_classes_c_minus':8-strong_minus,'census_invariant':census_invariant,
 'interpretation':'minimal ordered-wedge eta bridge covariance only; global branch convention remains unfixed',
 'claim_locks':['no physical causal-sector selection','no contour-existence or vertex-finiteness theorem','no K5/G3/F9/G8 promotion','no NEW_PHYSICS_FOUND']
}
with open('iter062_ordered_orientation_bridge_aggregate.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if not all_valid: raise SystemExit(2)
