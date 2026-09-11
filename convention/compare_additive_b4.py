#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load(path):
    out={}
    with open(path,newline="") as f:
        for r in csv.DictReader(f,delimiter="\t"):
            key=(r["case"],int(r["two_j"]),int(r["two_l"]),int(r["two_i"]),int(r["two_k"]))
            out[key]=float(r["value"])
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--baseline",required=True)
    ap.add_argument("--toller",required=True)
    ap.add_argument("--output",default="results/additive_b4_comparison.json")
    ap.add_argument("--threshold",type=float,default=5e-7)
    args=ap.parse_args()
    a,b=load(args.baseline),load(args.toller)
    common=sorted(set(a)&set(b)); missing_a=sorted(set(b)-set(a));missing_b=sorted(set(a)-set(b))
    rows=[];worst=0.0;worst_case=None
    for k in common:
        va,vb=a[k],b[k]
        scale=max(abs(va),abs(vb),1e-30)
        err=abs(vb-va)/scale
        rec={"case":k[0],"two_j":k[1],"two_l":k[2],"two_i":k[3],"two_k":k[4],"baseline":va,"toller_sum_b4":vb,"relative_symmetric_error":err}
        rows.append(rec)
        if err>worst:worst=err;worst_case=rec
    passed=(not missing_a and not missing_b and bool(common) and worst<args.threshold)
    out={"entries":len(common),"threshold":args.threshold,"worst_relative_symmetric_error":worst,"worst_case":worst_case,"missing_baseline":[list(x) for x in missing_a],"missing_toller":[list(x) for x in missing_b],"passed":passed,"verdict":"ADDITIVE_TOLLER_B4_RECONSTRUCTS_UPSTREAM_B4" if passed else "ADDITIVE_TOLLER_B4_GATE_OPEN","interpretation":"A full sl2cfoam_b4_accurate calculation was repeated after replacing each raw dsmall in the four-leg QAGP integrand by native (t+ + t-). The existing Lorentzian measure, adaptive integrator, recoupling contractions and downstream Speziale phase were otherwise unchanged.","scope":"additive plumbing/integration gate only; branch-resolved causal B4 and F9 remain open","rows":rows}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k!="rows"},indent=2))
    if not passed: raise SystemExit(4)

if __name__=="__main__":main()
