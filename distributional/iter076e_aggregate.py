#!/usr/bin/env python3
import argparse, glob, json, os
ap=argparse.ArgumentParser(); ap.add_argument('--input-root',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
rows={}
for p in glob.glob(os.path.join(a.input_root,'iter076e-*','*.json')):
    with open(p) as f: d=json.load(f)
    if d.get('lane') in 'ABCD': rows[d['lane']]=d
lanes=sorted(rows)
all_valid=(lanes==list('ABCD') and all(rows[k].get('valid') is True for k in 'ABCD'))
out={
 'iteration':'Iter076E',
 'lanes_found':lanes,
 'lane_valid':{k:rows[k].get('valid') for k in lanes},
 'scope_guard_ok':all('no physical pushforward' in rows[k].get('claim_lock','').lower() or 'structural tangent-space audit only' in rows[k].get('claim_lock','').lower() for k in lanes),
}
out['valid']=bool(all_valid and out['scope_guard_ok'])
out['classification']='ITER076E_SOURCE_RELATIVE_TANGENT_IS_CUT_SPACE_K4_CYCLE_IDENTIFICATION_REQUIRES_EXTRA_MAP_SCOPED' if out['valid'] else 'ITER076E_STRUCTURAL_HYPOTHESIS_FAIL'
out['claim_lock']='No physical source-to-K4 pushforward is defined; no epsilon^-1 coefficient; no causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion.'
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if not out['valid']: raise SystemExit(2)
