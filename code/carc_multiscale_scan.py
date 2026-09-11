#!/usr/bin/env python3
"""Monte-Carlo multiscale scan for causal-sector leakage under repeated RG maps.

The scan compares exactly block-diagonal maps with maps containing controlled +/-
sector mixing. It quantifies how tiny violations of the CARC/CCI condition can accumulate
under repeated coarse-graining. This is a structural surrogate, not a physical RG flow.
"""
from __future__ import annotations
import argparse, json, math, random
from pathlib import Path
NPLUS=NMINUS=3;N=6

def eye(): return [[1.0 if i==j else 0.0 for j in range(N)] for i in range(N)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def frob_cross(A):
    return math.sqrt(sum(A[i][j]**2 for i in range(N) for j in range(N) if (i<NPLUS)!=(j<NPLUS)))
def norm(A): return math.sqrt(sum(v*v for row in A for v in row))
def one_map(rng,eps):
    R=[[0.0]*N for _ in range(N)]
    for i in range(N):
      for j in range(N):
        same=(i<NPLUS)==(j<NPLUS)
        if same:
            R[i][j]=(0.78 if i==j else 0.0)+rng.uniform(-0.04,0.04)
        else:
            R[i][j]=eps*rng.uniform(-1.0,1.0)
    return R
def trial(seed,eps,steps):
    rng=random.Random(seed);C=eye();curve=[]
    for s in range(1,steps+1):
        C=mm(one_map(rng,eps),C)
        curve.append(frob_cross(C)/(norm(C)+1e-30))
    return curve
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/carc_multiscale_scan.json");ap.add_argument("--trials",type=int,default=200);ap.add_argument("--steps",type=int,default=12);args=ap.parse_args()
    eps_values=[0.0,1e-8,1e-6,1e-4,1e-3,1e-2]
    rows=[]
    for eps in eps_values:
        curves=[trial(1000+t,eps,args.steps) for t in range(args.trials)]
        means=[sum(c[s] for c in curves)/len(curves) for s in range(args.steps)]
        maxima=[max(c[s] for c in curves) for s in range(args.steps)]
        rows.append({"epsilon":eps,"mean_relative_leakage_by_step":means,"max_relative_leakage_by_step":maxima,"final_mean":means[-1],"final_max":maxima[-1]})
    verdict="EXACT_CCI_STABLE__SMALL_VIOLATIONS_ACCUMULATE"
    if rows[0]["final_max"]>1e-14 or not all(rows[i]["final_mean"]>rows[i-1]["final_mean"] for i in range(2,len(rows))): verdict="INCONCLUSIVE"
    out={"trials_per_epsilon":args.trials,"steps":args.steps,"rows":rows,"verdict":verdict,"interpretation":"Exact block preservation remains exact under composition. Cross-sector contamination produces accumulated effective leakage whose scale grows with the microscopic violation.","scope":"random finite-dimensional surrogate; no physical beta function inferred"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps({"verdict":verdict,"finals":[[r['epsilon'],r['final_mean']] for r in rows]},indent=2))
    if verdict=="INCONCLUSIVE": raise SystemExit(1)
if __name__=="__main__":main()
