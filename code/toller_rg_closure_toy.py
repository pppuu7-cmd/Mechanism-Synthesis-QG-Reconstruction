#!/usr/bin/env python3
"""Toy test of Toller-like analytic-class closure under naive blocking.

Toller branches are characterized in part by finite simple poles and half-plane
analytic/asymptotic conditions.  A rational surrogate shows that naive multiplication
of local branch factors generically raises pole order, so the simple-pole class is not
closed under that blocking map.  This is not an actual spin-foam RG calculation; it
identifies the correct next target: full gluing/summing followed by an analyticity test.
"""
from __future__ import annotations
import argparse, json, math, random
from pathlib import Path
POLES=[1j,2j,3j]
def branch(z,residues): return sum(r/(z-p) for p,r in zip(POLES,residues))
def estimate_order(func,p):
    e1=1e-4;e2=5e-5;y1=abs(func(p+e1));y2=abs(func(p+e2));return math.log(y2/y1)/math.log(e1/e2)
def trial(seed):
    rng=random.Random(seed);r1=[complex(rng.uniform(.4,1.4),rng.uniform(-.5,.5)) for _ in POLES];r2=[complex(rng.uniform(.4,1.4),rng.uniform(-.5,.5)) for _ in POLES];f1=lambda z:branch(z,r1);f2=lambda z:branch(z,r2);prod=lambda z:f1(z)*f2(z)
    return {"seed":seed,"single_orders":[estimate_order(f1,p) for p in POLES],"blocked_product_orders":[estimate_order(prod,p) for p in POLES]}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/toller_rg_closure_toy.json");ap.add_argument("--trials",type=int,default=32);args=ap.parse_args();trials=[trial(i+17) for i in range(args.trials)];avg_single=sum(sum(t["single_orders"]) for t in trials)/(len(trials)*len(POLES));avg_block=sum(sum(t["blocked_product_orders"]) for t in trials)/(len(trials)*len(POLES))
    verdict="NAIVE_MULTIPLICATIVE_BLOCKING_NOT_CLOSED_IN_SIMPLE_POLE_CLASS" if avg_single<1.1 and avg_block>1.8 else "INCONCLUSIVE"
    out={"trials":args.trials,"average_single_pole_order":avg_single,"average_naive_blocked_pole_order":avg_block,"verdict":verdict,"research_consequence":"Define the CRQN RG map on the fully glued/summed amplitude and test whether the effective causal branch projects back to the unique Toller analytic class without new independent pole data.","scope":"rational surrogate / structural obstruction; not an actual Toller or spin-foam RG computation","sample":trials[:5]}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    if verdict=="INCONCLUSIVE": raise SystemExit(1)
if __name__=="__main__": main()
