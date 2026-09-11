#!/usr/bin/env python3
"""Linear toy realization of the Causal Analyticity--RG Commutator (CARC) gate.

Let P+ be the positive-frequency causal projector and R a linearized coarse-graining
kernel. Causal-sector stability requires [P+,R]=0, equivalently P+ R P-=P- R P+=0.
This supplies an executable MSQGR target; it is not yet a physical spin-foam RG result.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
MODES=[-3,-2,-1,1,2,3];N=len(MODES)
def zeros(): return [[0j for _ in range(N)] for __ in range(N)]
def projector_plus():
    P=zeros()
    for i,k in enumerate(MODES): P[i][i]=1+0j if k>0 else 0j
    return P
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def matsub(A,B): return [[A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
def frob(A): return math.sqrt(sum(abs(A[i][j])**2 for i in range(N) for j in range(N)))
def comm(A,B): return matsub(matmul(A,B),matmul(B,A))
def kernel(kind):
    R=zeros()
    if kind=="diagonal":
        for i,k in enumerate(MODES): R[i][i]=1/(1+0.15*abs(k))
    elif kind=="same_sign_mixing":
        for i,k in enumerate(MODES):
            R[i][i]=0.8
            for j,q in enumerate(MODES):
                if i!=j and k*q>0: R[i][j]=0.04/(1+abs(k-q))
    elif kind=="cross_sign_mixing":
        R=kernel("same_sign_mixing")
        for i,k in enumerate(MODES):
            for j,q in enumerate(MODES):
                if k*q<0 and abs(k)==abs(q): R[i][j]=0.06
    elif kind=="parity_mixing":
        for i,k in enumerate(MODES): R[i][i]=0.75;R[i][MODES.index(-k)]=0.25
    else: raise ValueError(kind)
    return R
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/causal_rg_commutator.json");args=ap.parse_args();P=projector_plus();rows=[]
    for kind in ["diagonal","same_sign_mixing","cross_sign_mixing","parity_mixing"]:
        c=frob(comm(P,kernel(kind)));rows.append({"kernel":kind,"commutator_frobenius":c,"passes":c<1e-12})
    out={"equation":"C_+ = P_+ R - R P_+ = 0","equivalent_cross_blocks":["P_+ R P_- = 0","P_- R P_+ = 0"],"mode_basis":MODES,"results":rows,"verdict":"LINEAR_RG_CAUSAL_STABILITY_REQUIRES_BLOCK_DIAGONALITY","next_physical_test":"Construct the actual boundary coarse-graining/embedding map for a causal Toller/EPRL realization and evaluate the causal-projector/RG commutator.","scope":"finite-mode linear toy; candidate synthesis constraint, not a physical spinfoam RG result"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    if not rows[0]["passes"] or not rows[1]["passes"] or rows[2]["passes"] or rows[3]["passes"]: raise SystemExit(1)
if __name__=="__main__":main()
