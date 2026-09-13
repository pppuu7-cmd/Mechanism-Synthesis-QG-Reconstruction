#!/usr/bin/env python3
import argparse,json
from pathlib import Path
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows=[]
    for s in SIGMAS:
        m=list(Path(a.input_dir).rglob(f'iter072b-{s}.json'))
        if len(m)!=1: raise SystemExit(f'{s}: expected one artifact, got {len(m)}')
        rows.append(json.loads(m[0].read_text()))
    valid=all(r['valid'] for r in rows)
    neg=any(r['negative_control_disagrees'] for r in rows)
    trans=[r['sigma'] for r in rows if r['transitive']]
    strict=[r['sigma'] for r in rows if r['independent_realizing_order'] is not None]
    passed=bool(valid and neg and trans==strict)
    out={'iteration':'Iter072B','frozen_prereg_commit':'b334f75f4ffa15a1148a178fca20bc6def465ecf','lanes':8,
         'all_exact_lanes_valid':valid,'global_negative_control_pass':neg,'transitive_sigma_classes':trans,
         'strict_signed_cutspace_classes':strict,
         'classification':'ITER072B_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_TRANSITIVE_TOURNAMENT_SCOPED' if passed else 'ITER072B_SIGNED_CUTSPACE_THEOREM_FAIL',
         'claim_lock':'Reduced K4 common-epsilon full-collision leading coefficient only; no physical sector selection/full vertex/K5/G3/F9/G8 claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(10)
if __name__=='__main__': main()
