#!/usr/bin/env python3
"""Frozen aggregate for Iter072A."""
from __future__ import annotations
import argparse,json
from pathlib import Path
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir); rows=[]
    for s in SIGMAS:
        matches=list(root.rglob(f'iter072a-{s}.json'))
        if len(matches)!=1: raise SystemExit(f'expected exactly one artifact for {s}, found {len(matches)}')
        rows.append(json.loads(matches[0].read_text(encoding='utf-8')))
    all_valid=all(r.get('valid') is True for r in rows)
    neg=any(r.get('negative_control_disagrees') is True for r in rows)
    strong=[r['sigma'] for r in rows if r['strongly_connected']]
    nonstrong=[r['sigma'] for r in rows if not r['strongly_connected']]
    strict=[r['sigma'] for r in rows if r['strict_positive_circulation']]
    p5=all(all(b['max_proper_collision_degree']<3 for b in r['basis'].values()) for r in rows)
    passed=bool(all_valid and neg and strong==strict and p5)
    cls='ITER072A_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_STRONG_TOURNAMENT_SCOPED' if passed else 'ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL'
    out={'iteration':'Iter072A','gate':'K4_COMMON_EPSILON_LEADING_COLLISION_SCHWINGER_CONE_THEOREM',
         'frozen_prereg_commit':'1e011e9804ee2cde41260039c551f77562c68a4c','lanes':len(rows),'all_exact_lanes_valid':all_valid,
         'global_negative_control_pass':neg,'proper_stratum_power_separation':p5,'strong_sigma_classes':strong,
         'non_strong_sigma_classes':nonstrong,'strict_positive_circulation_classes':strict,'classification':cls,
         'claim_lock':'Reduced K4 common-epsilon leading full-collision asymptotic only. No physical sector selection, complete causal-vertex theorem, K5 extension, or G3/F9/G8 promotion.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(8)
if __name__=='__main__': main()
