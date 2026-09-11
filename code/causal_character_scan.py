#!/usr/bin/env python3
"""Numerically falsify/diagnose a naive multiplicative scalar causal-factor ansatz.

log F_+(x)=(a+i b)x+(c+i d)x^2.  We test local semigroup gluing and unit modulus.
Passing this branch is not sufficient for CRQN and is not imposed on Toller matrices;
it is retained as a negative control because modern Toller branches are not group representations.
"""
from __future__ import annotations
import argparse, cmath, csv, json, math
from pathlib import Path
X=[0.125,0.25,0.5,0.75,1.0,1.5]
PAIRS=[(x,y) for x in X for y in X if x+y<=2.0+1e-12]
def F(x,a,b,c,d): return cmath.exp(complex(a,b)*x+complex(c,d)*x*x)
def metrics(a,b,c,d):
    comp=[abs(F(x+y,a,b,c,d)-F(x,a,b,c,d)*F(y,a,b,c,d)) for x,y in PAIRS]
    norm=[abs(abs(F(x,a,b,c,d))-1.0) for x in X]
    return {"composition_max":max(comp),"composition_rms":math.sqrt(sum(v*v for v in comp)/len(comp)),"unit_modulus_max":max(norm),"score":max(comp)+max(norm)}
def grid():
    for a in [-.2,-.1,0,.1,.2]:
      for b in [-2,-1.5,-1,-.5,0,.5,1,1.5,2]:
       for c in [-.2,-.1,0,.1,.2]:
        for d in [-.2,-.1,0,.1,.2]: yield {"a":a,"b":b,"c":c,"d":d,**metrics(a,b,c,d)}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/causal_character_scan.json");ap.add_argument("--csv",default="results/causal_character_ranked.csv");ap.add_argument("--tol",type=float,default=1e-10);args=ap.parse_args()
    rows=sorted(grid(),key=lambda r:(r["score"],abs(r["b"]),r["a"],r["c"],r["d"]));surv=[r for r in rows if r["composition_max"]<=args.tol and r["unit_modulus_max"]<=args.tol];bs=sorted({r["b"] for r in surv})
    verdict="UNDERDETERMINED_PHASE_FAMILY" if len(bs)>1 else ("UNIQUE_ON_GRID" if len(bs)==1 else "NO_SURVIVOR")
    out={"ansatz":"log F_+(x)=(a+i b)x+(c+i d)x^2","grid_points":len(rows),"survivor_count":len(surv),"surviving_b_values":bs,"best_20":rows[:20],"verdict":verdict,"interpretation":"Naive multiplicative gluing removes quadratic log terms and norm preservation removes damping, but the linear phase remains free.","claim_scope":"negative-control scalar branch; not a physical Toller/spinfoam vertex derivation"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");cp=Path(args.csv);cp.parent.mkdir(parents=True,exist_ok=True)
    with cp.open("w",newline="",encoding="utf-8") as fh:
      w=csv.DictWriter(fh,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows[:500])
    print(json.dumps({k:out[k] for k in ["grid_points","survivor_count","surviving_b_values","verdict"]},indent=2))
    if verdict!="UNDERDETERMINED_PHASE_FAMILY": raise SystemExit(1)
if __name__=="__main__": main()
