#!/usr/bin/env python3
"""Finite-dimensional executable test of Causal Cylindrical Intertwining (CCI).

We construct coarse, intermediate and fine boundary spaces with +/- causal sectors.
Sector-preserving embeddings satisfy both cylindrical consistency and
P_f iota = iota P_c.  A controlled cross-sector contamination violates CCI while
leaving ordinary cylindrical composition intact, showing that CCI is an independent gate.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def z(r,c): return [[0.0 for _ in range(c)] for __ in range(r)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def frob(A): return math.sqrt(sum(v*v for row in A for v in row))
def proj(n,nplus):
    P=z(n,n)
    for i in range(nplus): P[i][i]=1.0
    return P
def injection(nc,np_c,nf,np_f,eps=0.0):
    """Map + basis into + basis and - basis into - basis, with optional cross leakage."""
    I=z(nf,nc)
    nm_c=nc-np_c
    for j in range(np_c): I[j][j]=1.0
    for j in range(nm_c): I[np_f+j][np_c+j]=1.0
    if eps:
        # symmetric cross-sector contamination on first +/- basis vectors
        I[np_f][0]+=eps
        I[0][np_c]+=eps
    return I
def cci(Pf,I,Pc): return frob(sub(mm(Pf,I),mm(I,Pc)))
def cyl(I_fm,I_mc,I_fc): return frob(sub(mm(I_fm,I_mc),I_fc))
def run(eps):
    # H_c: 2+2-, H_m: 3+3-, H_f: 4+4-
    Pc=proj(4,2);Pm=proj(6,3);Pf=proj(8,4)
    I_mc=injection(4,2,6,3,eps=eps)
    I_fm=injection(6,3,8,4,eps=eps)
    I_fc=mm(I_fm,I_mc)  # enforce ordinary cylindrical consistency exactly
    return {
      "epsilon":eps,
      "cci_coarse_to_mid":cci(Pm,I_mc,Pc),
      "cci_mid_to_fine":cci(Pf,I_fm,Pm),
      "cci_coarse_to_fine":cci(Pf,I_fc,Pc),
      "cylindrical_residual":cyl(I_fm,I_mc,I_fc)
    }
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/causal_embedding_consistency.json");args=ap.parse_args()
    eps=[0.0,1e-8,1e-6,1e-4,1e-2,0.1]
    rows=[run(e) for e in eps]
    clean=rows[0]
    verdict="CCI_INDEPENDENT_OF_ORDINARY_CYLINDRICAL_CONSISTENCY"
    if clean["cci_coarse_to_fine"]>1e-14 or any(r["cylindrical_residual"]>1e-14 for r in rows): verdict="UNEXPECTED"
    if not all(r["cci_coarse_to_fine"]>0 for r in rows[1:]): verdict="UNEXPECTED"
    out={"equations":["iota_fc = iota_fm iota_mc","P_f iota_fc = iota_fc P_c"],"rows":rows,"verdict":verdict,"interpretation":"Ordinary cylindrical consistency can hold exactly while causal-sector intertwining fails. CCI is therefore an additional, independently testable RG/causality condition.","scope":"finite-dimensional surrogate, not a physical EPRL/Toller coarse-graining computation"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    if verdict=="UNEXPECTED": raise SystemExit(1)
if __name__=="__main__":main()
