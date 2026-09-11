#!/usr/bin/env python3
"""Exact linearized rank test for the naive local-character branch.

For log F=(a+i b)x+(c+i d)x^2, unit modulus plus multiplicative local gluing
has rank 3 in (a,b,c,d); the phase b survives.  This diagnoses only the naive
scalar branch.  Toller matrices do not obey a representation multiplication law,
so this result is not imposed on the physical causal-spinfoam branch.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
VARS=["a","b","c","d"]

def rref(matrix):
    A=[row[:] for row in matrix]; m=len(A); n=len(A[0]) if m else 0; pivots=[]; r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c] != 0),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]; p=A[r][c]; A[r]=[v/p for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        pivots.append(c); r+=1
        if r==m: break
    return A,pivots

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",default="results/constraint_rank.json"); args=ap.parse_args()
    rows=[]
    for x in [Fraction(1,2),Fraction(1),Fraction(3,2)]: rows.append([x,Fraction(0),x*x,Fraction(0)])
    for x,y in [(Fraction(1,2),Fraction(1,2)),(Fraction(1,2),Fraction(1))]:
        rows.append([Fraction(0),Fraction(0),2*x*y,Fraction(0)]); rows.append([Fraction(0),Fraction(0),Fraction(0),2*x*y])
    rr,pivots=rref(rows); free=[i for i in range(len(VARS)) if i not in pivots]
    fmt=lambda q: str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
    out={"variables":VARS,"rank":len(pivots),"nullity":len(VARS)-len(pivots),"pivot_variables":[VARS[i] for i in pivots],"free_variables":[VARS[i] for i in free],"rref":[[fmt(x) for x in row] for row in rr],"verdict":"ONE_PHASE_DIRECTION_REMAINS" if free==[1] else "UNEXPECTED","scope":"naive scalar multiplicative local-factor branch only"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    if out["verdict"]=="UNEXPECTED": raise SystemExit(1)
if __name__=="__main__": main()
