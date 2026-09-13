#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from distributional.iter073d_transitive_face_cones import records_for, TREES
from distributional.iter076b_degree2_overlap_jet_complex import audit, NEG

EXPECTED_MU=[(-1,4),(0,5),(1,4)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--label',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    basis={}; ref=None; p1=p2=p3=p4=p6=True
    for tr in TREES:
        rec=audit(a.label,tr); basis[tr]=rec
        p1 &= (rec['face_count']==6 and rec['closure_size']==13 and rec['mobius_identity_ok'] and rec['top_mu_histogram']==EXPECTED_MU)
        p2 &= rec['rank_monotonicity_exact']; p3 &= rec['restriction_compatibility_exact']; p6 &= rec['nonzero_proper_quadratic_rank']
        sig=tuple(tuple(x) for x in rec['restriction_records'])
        if ref is None: ref=sig
        else: p4 &= (sig==ref)
    neg={tr:len(records_for(NEG,tr)) for tr in TREES}; p7=all(v==0 for v in neg.values())
    ok=bool(p1 and p2 and p3 and p4 and p6 and p7)
    out={'iteration':'Iter076B','label':a.label,'predicates':{'P1':bool(p1),'P2':bool(p2),'P3':bool(p3),'P4':bool(p4),'P6':bool(p6),'P7':bool(p7)},'signature':[list(x) for x in ref],'basis':basis,'negative_control_face_counts':neg,'lane_ok':ok}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True))
    print(json.dumps({k:v for k,v in out.items() if k!='basis'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
