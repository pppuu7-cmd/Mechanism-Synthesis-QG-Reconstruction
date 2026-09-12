#!/usr/bin/env python3
"""Iter037A: exact oriented-4-simplex A5 symmetry audit on K5 cycle space.

Iter036 showed that the *full* S5 action isotropizes any stabilizer-compatible
cycle metric for each source causal orbit.  An oriented 4-simplex, however,
need not identify odd vertex permutations with orientation-preserving relabelings.
The physically conservative subgroup is A5.

This script uses exact rational arithmetic to determine:
  * dim Sym^2(Cycle(K5))^A5;
  * the residual shape dimension after fixing one overall scale;
  * causal orbit sizes/stabilizers under A5;
  * for each causal type, the dimension of the image obtained by A5-averaging
    every stabilizer-invariant symmetric tensor;
  * whether adjoining a single odd permutation reduces the A5-invariant metric
    space to the unique S5-invariant line.

A two-dimensional A5-invariant symmetric space would mean one determinant-
normalized shape parameter survives orientation-preserving symmetry alone.
That would make odd-permutation/orientation-reversal covariance a genuinely
physical gate rather than a cosmetic convention.
"""
from __future__ import annotations

import argparse,itertools,json
from pathlib import Path
import sympy as sp

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
EIDX={e:k for k,e in enumerate(EDGES)}
PERMS=list(itertools.permutations(range(N)))

def parity(p):
    inv=sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))
    return inv%2
A5=[p for p in PERMS if parity(p)==0]
ODD=[p for p in PERMS if parity(p)==1]

def cycle_basis():
    cols=[]
    for i in range(1,N):
        for j in range(i+1,N):
            v=[sp.Integer(0)]*10
            v[EIDX[(0,i)]]+=1;v[EIDX[(i,j)]]+=1;v[EIDX[(0,j)]]-=1
            cols.append(sp.Matrix(v))
    C=sp.Matrix.hstack(*cols);assert C.shape==(10,6) and C.rank()==6
    return C

def edge_rep(p):
    P=sp.zeros(10,10)
    for col,(i,j) in enumerate(EDGES):
        a,b=p[i],p[j];sgn=1
        if a>b:a,b=b,a;sgn=-1
        P[EIDX[(a,b)],col]=sgn
    return P

def cycle_rep(p,C,L):
    R=sp.simplify(L*edge_rep(p)*C);assert C*R==edge_rep(p)*C;return R

def sym_basis():
    out=[]
    for i in range(6):
        for j in range(i,6):
            M=sp.zeros(6,6);M[i,j]=1;M[j,i]=1
            out.append(M)
    return out
SYM=sym_basis()

def invariant_basis(reps):
    rows=[]
    for R in reps:
        ds=[R.T*B*R-B for B in SYM]
        for i in range(6):
            for j in range(i,6):rows.append([D[i,j] for D in ds])
    A=sp.Matrix(rows);ns=A.nullspace();mats=[]
    for v in ns:
        M=sp.zeros(6,6)
        for c,B in zip(v,SYM):M+=c*B
        mats.append(sp.simplify(M))
    return mats

def flat_sym(M):return sp.Matrix([M[i,j] for i in range(6) for j in range(i,6)])
def span_dim(mats):
    if not mats:return 0
    return sp.Matrix.hstack(*[flat_sym(M) for M in mats]).rank()
def average(M,reps):
    out=sp.zeros(6,6)
    for R in reps:out+=R.T*M*R
    return sp.simplify(out/sp.Integer(len(reps)))
def canon(s):return s if s[0]==1 else tuple(-x for x in s)
def transform(s,p):
    out=[0]*N
    for i in range(N):out[p[i]]=s[i]
    return canon(tuple(out))
def stabilizer(s,group):return [p for p in group if transform(s,p)==canon(s)]
def orbit(s,group):return {transform(s,p) for p in group}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    C=cycle_basis();G=C.T*C;L=G.inv()*C.T
    reps={p:cycle_rep(p,C,L) for p in PERMS};A5r=[reps[p] for p in A5]
    a5_inv=invariant_basis(A5r);s5_inv=invariant_basis(list(reps.values()))
    odd=ODD[0];a5_plus_odd=invariant_basis(A5r+[reps[odd]])
    types={'5+0':(1,1,1,1,1),'4+1':(1,-1,-1,-1,-1),'3+2':(1,1,-1,-1,-1)}
    rows=[]
    for name,s in types.items():
        H=stabilizer(s,A5);O=orbit(s,A5);hinv=invariant_basis([reps[p] for p in H])
        avgs=[average(M,A5r) for M in hinv]
        rows.append({
          'type':name,'A5_orbit_size':len(O),'A5_stabilizer_order':len(H),
          'stabilizer_invariant_symmetric_dimension':len(hinv),
          'stabilizer_shape_parameters_after_scale':max(len(hinv)-1,0),
          'A5_average_image_dimension':span_dim(avgs),
          'A5_average_shape_parameters_after_scale':max(span_dim(avgs)-1,0),
        })
    gates={
      'A5_order_is_60':len(A5)==60,
      'S5_invariant_metric_line':len(s5_inv)==1,
      'odd_generator_restores_S5_line':len(a5_plus_odd)==1,
      'orbit_stabilizer_products_are_60':all(r['A5_orbit_size']*r['A5_stabilizer_order']==60 for r in rows),
    }
    passed=all(gates.values())
    out={
      'iteration':'Iter037A','A5_order':len(A5),'S5_order':120,
      'A5_invariant_symmetric_dimension':len(a5_inv),
      'A5_shape_parameters_after_fixing_scale':max(len(a5_inv)-1,0),
      'S5_invariant_symmetric_dimension':len(s5_inv),
      'A5_plus_one_odd_invariant_dimension':len(a5_plus_odd),
      'causal_rows':rows,'gates':gates,'pass':passed,
      'verdict':('ORIENTED_A5_LEAVES_RESIDUAL_CYCLE_SHAPE' if passed and len(a5_inv)>1
                 else 'ORIENTED_A5_FULLY_ISOTROPIZES' if passed else 'ORIENTED_A5_AUDIT_REVIEW'),
      'claim_lock':('Exact finite K5 representation theory only. Which odd permutations are physical symmetries of the causal '
                    'Toller vertex must be decided from the actual oriented amplitude, not assumed from this surrogate.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
