#!/usr/bin/env python3
"""Iter036A: exact K5 causal-orbit stabilizer / finite-part ambiguity audit.

The source causal data are five signs sigma_a=+-1 modulo global reversal.  The
16 inequivalent classes split under S5 into the three partition types
5+0, 4+1 and 3+2.  For each type we compute, exactly over Q:

* orbit size and stabilizer order;
* the dimension of the stabilizer-invariant symmetric bilinear forms on the
  six-dimensional K5 cycle space;
* the number of determinant-normalized shape parameters (dimension minus one);
* whether averaging every stabilizer-invariant form over the full S5 orbit
  collapses it onto the unique S5-invariant cycle metric.

The cycle representation is constructed in an integer fundamental-cycle basis,
so no floating-point rank decision enters this lane.

If the orbit average is one-dimensional, a source-covariant *equal-within-orbit*
sum can remove cycle-metric shape ambiguity even when a fixed causal sector
allows several invariant finite-part tensors.  This is a symmetry theorem for
the finite K5 surrogate; it does NOT establish that the physical Toller/Feynman
extension supplies the assumed covariant sector tensors or equal orbit weights.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sympy as sp

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
EIDX={e:k for k,e in enumerate(EDGES)}
PERMS=list(itertools.permutations(range(N)))


def cycle_basis():
    # Tree edges are (0,i). Each chord (i,j), 1<=i<j<=4, closes one triangle.
    cols=[]
    for i in range(1,N):
        for j in range(i+1,N):
            v=[sp.Integer(0)]*len(EDGES)
            v[EIDX[(0,i)]] += 1
            v[EIDX[(i,j)]] += 1
            v[EIDX[(0,j)]] -= 1
            cols.append(v)
    C=sp.Matrix.hstack(*[sp.Matrix(v) for v in cols])
    assert C.shape==(10,6) and C.rank()==6
    return C


def edge_rep(p):
    P=sp.zeros(10,10)
    for col,(i,j) in enumerate(EDGES):
        a,b=p[i],p[j]; sign=1
        if a>b: a,b=b,a; sign=-1
        P[EIDX[(a,b)],col]=sign
    return P


def cycle_rep(p,C,L):
    P=edge_rep(p)
    R=sp.simplify(L*P*C)
    assert C*R==P*C
    return R


def transform_sigma(sig,p):
    out=[0]*N
    for i in range(N): out[p[i]]=sig[i]
    return tuple(out)


def canonical_sigma(sig):
    return sig if sig[0]==1 else tuple(-x for x in sig)


def stabilizer(sig):
    return [p for p in PERMS if canonical_sigma(transform_sigma(sig,p))==canonical_sigma(sig)]


def orbit(sig):
    return sorted({canonical_sigma(transform_sigma(sig,p)) for p in PERMS})


def sym_basis():
    out=[]
    for i in range(6):
        for j in range(i,6):
            B=sp.zeros(6,6);B[i,j]=1;B[j,i]=1 if i!=j else 1
            out.append(B)
    assert len(out)==21
    return out


def invariant_basis(reps):
    basis=sym_basis(); rows=[]
    for R in reps:
        diffs=[R.T*B*R-B for B in basis]
        for i in range(6):
            for j in range(i,6):
                rows.append([D[i,j] for D in diffs])
    A=sp.Matrix(rows)
    ns=A.nullspace()
    mats=[]
    for v in ns:
        M=sp.zeros(6,6)
        for c,B in zip(v,basis): M += c*B
        mats.append(sp.simplify(M))
    return mats,A.rank()


def proportional(A,B):
    # exact test for A=lambda B using any nonzero B entry
    lam=None
    for i in range(B.rows):
        for j in range(B.cols):
            if B[i,j]!=0:
                q=sp.simplify(A[i,j]/B[i,j])
                if lam is None: lam=q
                elif sp.simplify(q-lam)!=0:return False,None
            elif A[i,j]!=0:return False,None
    return True,lam


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    C=cycle_basis(); gram=C.T*C; L=gram.inv()*C.T
    reps={p:cycle_rep(p,C,L) for p in PERMS}
    # exact representation sanity
    gram_ok=all(sp.simplify(R.T*gram*R-gram)==sp.zeros(6,6) for R in reps.values())

    types={
      '5+0':(1,1,1,1,1),
      '4+1':(1,-1,-1,-1,-1),
      '3+2':(1,1,-1,-1,-1),
    }
    rows=[]; all_pass=True
    for name,sig in types.items():
        H=stabilizer(sig); O=orbit(sig); Hreps=[reps[p] for p in H]
        inv,rank=invariant_basis(Hreps)
        avg_checks=[]
        for B in inv:
            avg=sp.zeros(6,6)
            for p in PERMS: avg += reps[p].T*B*reps[p]
            avg=avg/sp.Integer(len(PERMS))
            ok,lam=proportional(sp.simplify(avg),gram)
            avg_checks.append({'proportional_to_unique_S5_metric':bool(ok),'lambda':str(lam)})
        row={
          'causal_partition':name,'sigma_representative':list(sig),
          'orbit_size':len(O),'stabilizer_order':len(H),
          'orbit_stabilizer_product':len(O)*len(H),
          'invariant_symmetric_dimension':len(inv),
          'shape_parameters_after_fixing_scale':max(len(inv)-1,0),
          'orbit_average_checks':avg_checks,
          'all_invariant_basis_orbit_averages_isotropic':all(x['proportional_to_unique_S5_metric'] for x in avg_checks),
        }
        rows.append(row)
        all_pass &= row['orbit_stabilizer_product']==120 and row['all_invariant_basis_orbit_averages_isotropic']

    full_inv,_=invariant_basis(list(reps.values()))
    all_pass &= gram_ok and len(full_inv)==1
    out={
      'iteration':'Iter036A','cycle_dimension':6,'edge_count':10,
      'source_sector_count_mod_global_flip':16,
      'S5_order':120,'cycle_gram':[[str(x) for x in gram.row(i)] for i in range(6)],
      'representation_preserves_cycle_gram_exactly':bool(gram_ok),
      'full_S5_invariant_symmetric_dimension':len(full_inv),
      'causal_orbit_rows':rows,
      'pass':bool(all_pass),
      'verdict':'SOURCE_CAUSAL_ORBIT_SYMMETRY_ISOTROPIZES_ANY_STABILIZER_INVARIANT_CYCLE_METRIC' if all_pass else 'CAUSAL_ORBIT_SYMMETRY_AUDIT_REVIEW',
      'claim_lock':('Exact finite K5 representation-theory result. It does not prove that the physical multi-wedge '
                    'Feynman extension is stabilizer-covariant or that its sector weights are constant within an S5 orbit.'),
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if not all_pass:raise SystemExit(1)
if __name__=='__main__':main()
