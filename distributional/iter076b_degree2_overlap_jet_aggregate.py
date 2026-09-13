#!/usr/bin/env python3
from __future__ import annotations
import argparse, glob, json
from pathlib import Path

EXPECTED={'++++','+++-','++--','+---'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-glob',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows=[json.loads(Path(p).read_text()) for p in sorted(glob.glob(a.input_glob))]
    labels={r['label'] for r in rows}
    p0=(labels==EXPECTED and len(rows)==4)
    p1=all(r['predicates']['P1'] for r in rows); p2=all(r['predicates']['P2'] for r in rows)
    p3=all(r['predicates']['P3'] for r in rows); p4=all(r['predicates']['P4'] for r in rows)
    p6=all(r['predicates']['P6'] for r in rows); p7=all(r['predicates']['P7'] for r in rows)
    sigs=[tuple(tuple(x) for x in r['signature']) for r in rows]; p5=(len(sigs)==4 and all(s==sigs[0] for s in sigs))
    ok=bool(p0 and p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out={'iteration':'Iter076B','labels':sorted(labels),'predicates':{
        'P0_ALL_FOUR_INDEPENDENT_LANES_PRESENT':p0,
        'P1_ITER076A_POSET_MOBIUS_REPRODUCED':p1,
        'P2_QUADRATIC_RESTRICTION_RANK_MONOTONE':p2,
        'P3_COMPARABLE_RESTRICTIONS_COMMUTE_EXACTLY':p3,
        'P4_CYCLE_BASIS_SIGNATURE_INVARIANT':p4,
        'P5_TRANSITIVE_S4_ORBIT_SIGNATURE_EQUAL':p5,
        'P6_DEGREE2_DATA_NONTRIVIAL_NEGATIVE_CONTROL':p6,
        'P7_NONTRANSITIVE_CONTROL_EMPTY':p7},
        'classification':'ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_EXACT_COVARIANT_SCOPED' if ok else 'ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_OBSTRUCTED_SCOPED',
        'claim_lock':'Quadratic overlap-jet bookkeeping only; no epsilon^-1 coefficient, physical subtraction, K5/G3/F9/G8 promotion, complete QG or new physics.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
