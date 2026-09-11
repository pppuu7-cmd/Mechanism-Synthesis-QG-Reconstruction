#!/usr/bin/env python3
"""Count the finite-dimensional codimension imposed by causal-sector RG closure.

For H=H_+ direct-sum H_-, a generic complex linear RG map has (n_++n_-)^2
complex entries. CCI/CARC sets the two off-diagonal blocks to zero, imposing
2 n_+ n_- complex conditions. This is an exact structural count, not a claim
about independent physical couplings in a concrete spin-foam truncation.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

def row(p,m):
    total=(p+m)**2; constrained=2*p*m; remaining=p*p+m*m
    return {"n_plus":p,"n_minus":m,"generic_complex_parameters":total,"cci_complex_constraints":constrained,"remaining_block_diagonal_parameters":remaining,"constrained_fraction":constrained/total}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/carc_codimension.json");args=ap.parse_args()
    rows=[row(p,m) for p in range(1,9) for m in range(1,9)]
    equal=[r for r in rows if r["n_plus"]==r["n_minus"]]
    out={"formula":{"generic":"(n_plus+n_minus)^2 complex parameters","constraints":"2 n_plus n_minus complex cross-sector conditions","remaining":"n_plus^2+n_minus^2 complex parameters"},"equal_sector_fraction":[[r["n_plus"],r["constrained_fraction"]] for r in equal],"rows":rows,"verdict":"CCI_REMOVES_HALF_OF_GENERIC_LINEAR_MAP_SPACE_FOR_EQUAL_SECTORS","scope":"linear finite-dimensional parameter count; concrete truncations may correlate parameters and reduce the independent count"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps({"verdict":out["verdict"],"equal_sector_fraction":out["equal_sector_fraction"]},indent=2))
if __name__=="__main__":main()
