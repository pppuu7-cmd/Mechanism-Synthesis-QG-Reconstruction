#!/usr/bin/env python3
import itertools, json
V=range(4); E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
rows=[]
for tail in itertools.product((-1,1), repeat=3):
    sigma=(1,)+tail
    kappa=tuple(sigma[a]*sigma[b] for a,b in E)
    for global_sign in (1,-1):
        s=tuple(global_sign*k for k in kappa)
        required_reversed=tuple(-x for x in s)
        recomputed_same_kappa=tuple(global_sign*k for k in kappa)
        rows.append({'sigma':sigma,'candidate':'s=kappa' if global_sign==1 else 's=-kappa','kappa':kappa,'required_reversed':required_reversed,'recomputed_same_kappa':recomputed_same_kappa,'compatible':required_reversed==recomputed_same_kappa})
# exhaustive edge-local maps f:{-1,+1}->{-1,+1}
functions=[]
for fm,fp in itertools.product((-1,1), repeat=2):
    ok=True
    for k in (-1,1):
        f= fm if k==-1 else fp
        if f != -f: ok=False
    functions.append({'f_minus':fm,'f_plus':fp,'reversal_covariant':ok})
all_direct_incompatible=all(not r['compatible'] for r in rows)
no_edge_local_map=all(not x['reversal_covariant'] for x in functions)
valid=(len(rows)==16 and all_direct_incompatible and no_edge_local_map)
classification='K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_OBSTRUCTED' if valid else 'K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_COMPATIBLE'
out={'iteration':'Iter061','classification':classification,'all_valid':valid,'physical_sigma_classes':8,'direct_identification_lanes':len(rows),'compatible_direct_lanes':sum(r['compatible'] for r in rows),'edge_local_functions_tested':len(functions),'reversal_covariant_edge_local_functions':sum(x['reversal_covariant'] for x in functions),'scope':'orientation-blind direct bridge only; orientation-sensitive eta bridge remains open','claim_locks':['no physical sector selection','no contour/finiteness theorem','no K5/G3/F9/G8 promotion','no NEW_PHYSICS_FOUND']}
print(json.dumps(out,indent=2,sort_keys=True))
with open('iter061_kappa_spectral_bridge_audit.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
