#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input-dir',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    lanes=[]
    for f in sorted(Path(a.input_dir).rglob('iter073a-*.json')):
        if f.name!='iter073a-aggregate.json': lanes.append(json.loads(f.read_text()))
    expected={'++++','+++-','++-+','++--','+-++','+-+-','+--+','+---'}
    all_valid=len(lanes)==8 and {x.get('sigma') for x in lanes}==expected and all(x.get('valid') for x in lanes)
    neg=any(x.get('negative_control_disagrees') for x in lanes)
    ok=bool(all_valid and neg)
    out={'iteration':'Iter073A','lanes':len(lanes),'all_exact_lanes_valid':all_valid,'global_negative_control_pass':neg,
         'max_feasible_proper_nullity_by_sigma':{x['sigma']:x['max_feasible_proper_nullity'] for x in lanes},
         'proper_histogram_by_sigma':{x['sigma']:x['proper_histogram'] for x in lanes},
         'full_set_crosscheck':{x['sigma']:x['full_set'] for x in lanes},
         'classification':'ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_EXACT_SCOPED' if ok else 'ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_FAIL',
         'frozen_prereg_commit':'8b87abc4aea6636b9e554729bba4670b91d9e7f3'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
