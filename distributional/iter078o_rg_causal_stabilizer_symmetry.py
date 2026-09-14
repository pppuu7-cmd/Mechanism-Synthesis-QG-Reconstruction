#!/usr/bin/env python3
"""Iter078O-RG: exact S5 causal-stabilizer action on five j=1/2 intertwiner nodes.

Arithmetic is over Q(sqrt(3)); local permutation matrices are derived directly
from the normalized repository intertwiner tensors.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
from fractions import Fraction
from pathlib import Path

# Field element a+b*sqrt(3)
Z = (Fraction(0), Fraction(0))
O = (Fraction(1), Fraction(0))
S3 = (Fraction(0), Fraction(1))


def fadd(x,y): return (x[0]+y[0], x[1]+y[1])
def fsub(x,y): return (x[0]-y[0], x[1]-y[1])
def fneg(x): return (-x[0],-x[1])
def fmul(x,y): return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def fscale(q,x): return (q*x[0],q*x[1])
def fiszero(x): return x[0]==0 and x[1]==0

def finv(x):
    den=x[0]*x[0]-3*x[1]*x[1]
    if den==0: raise ZeroDivisionError
    return (x[0]/den,-x[1]/den)

def fdiv(x,y): return fmul(x,finv(y))

def fstr(x):
    a,b=x
    return f"{a}+({b})*sqrt3"

# normalized local invariant tensors in bit basis (-,+) -> 0,1
T0={
    (0,1,0,1): fscale(Fraction(1,2),O),
    (0,1,1,0): fscale(Fraction(-1,2),O),
    (1,0,0,1): fscale(Fraction(-1,2),O),
    (1,0,1,0): fscale(Fraction(1,2),O),
}
T1_INT={
    (0,0,1,1):2,(0,1,0,1):-1,(0,1,1,0):-1,
    (1,0,0,1):-1,(1,0,1,0):-1,(1,1,0,0):2,
}
T1={k:fscale(Fraction(v,6),S3) for k,v in T1_INT.items()}
TENS=[T0,T1]
BITS=list(itertools.product((0,1),repeat=4))


def tval(T,b): return T.get(tuple(b),Z)

def inner(A,B):
    s=Z
    for b in BITS: s=fadd(s,fmul(tval(A,b),tval(B,b)))
    return s


def permuted_tensor(T, old_to_new):
    out={}
    for newbits in BITS:
        oldbits=[0]*4
        for oldp,newp in enumerate(old_to_new): oldbits[oldp]=newbits[newp]
        v=tval(T,oldbits)
        if not fiszero(v): out[newbits]=v
    return out


def local_matrix(old_to_new):
    # columns old k, rows new k
    M=[[Z,Z],[Z,Z]]
    for oldk,T in enumerate(TENS):
        PT=permuted_tensor(T,old_to_new)
        for newk,U in enumerate(TENS): M[newk][oldk]=inner(U,PT)
    return M


def m2mul(A,B):
    return [[fadd(fmul(A[i][0],B[0][j]),fmul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]

def m2transpose(A): return [[A[j][i] for j in range(2)] for i in range(2)]
def m2eq(A,B): return A==B
I2=[[O,Z],[Z,O]]

PERM4=list(itertools.permutations(range(4)))
LOCAL={p:local_matrix(p) for p in PERM4}


def compose_map(p,q):
    # old->new maps, apply p then q: old -> q[p[old]]
    return tuple(q[p[i]] for i in range(len(p)))

NEIGH={a:[b for b in range(5) if b!=a] for a in range(5)}
BASIS5=list(itertools.product((0,1),repeat=5)); INDEX5={k:i for i,k in enumerate(BASIS5)}
PERM5=list(itertools.permutations(range(5)))


def local_slot_map(pi,a):
    d=pi[a]; dest=NEIGH[d]
    return tuple(dest.index(pi[b]) for b in NEIGH[a])


def global_matrix(pi):
    M=[[Z for _ in range(32)] for _ in range(32)]
    locals_=[LOCAL[local_slot_map(pi,a)] for a in range(5)]
    for old in BASIS5:
        col=INDEX5[old]
        for choices in BASIS5: # choice per old node, becomes k at destination pi[a]
            coeff=O; new=[0]*5
            for a in range(5):
                nk=choices[a]; new[pi[a]]=nk
                coeff=fmul(coeff,locals_[a][nk][old[a]])
                if fiszero(coeff): break
            if not fiszero(coeff):
                row=INDEX5[tuple(new)]; M[row][col]=fadd(M[row][col],coeff)
    return M


def matmul(A,B):
    n=len(A); m=len(B[0]); mid=len(B)
    out=[[Z for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(mid):
            if fiszero(A[i][k]): continue
            for j in range(m):
                if not fiszero(B[k][j]): out[i][j]=fadd(out[i][j],fmul(A[i][k],B[k][j]))
    return out

def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def mateq(A,B): return A==B

def compose5(p,q): return tuple(q[p[i]] for i in range(5))

def trace(M):
    s=Z
    for i in range(len(M)): s=fadd(s,M[i][i])
    return s


def rref_rank(rows,ncol=32):
    m=[list(row) for row in rows if any(not fiszero(x) for x in row)]
    r=0; piv=[]
    for c in range(ncol):
        p=next((rr for rr in range(r,len(m)) if not fiszero(m[rr][c])),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        inv=finv(m[r][c]); m[r]=[fmul(inv,x) for x in m[r]]
        for rr in range(len(m)):
            if rr==r or fiszero(m[rr][c]): continue
            q=m[rr][c]; m[rr]=[fsub(x,fmul(q,y)) for x,y in zip(m[rr],m[r])]
        piv.append(c); r+=1
        if r==len(m): break
    return len(piv)


def stabilizer(sig):
    return [p for p in PERM5 if all(sig[p[a]]==sig[a] for a in range(5))]


def serialize_field(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]


def lane_a():
    norms=[inner(T,T) for T in TENS]; cross=inner(TENS[0],TENS[1])
    orth=[]; distinct=[]
    for p in PERM4:
        M=LOCAL[p]; ok=m2eq(m2mul(m2transpose(M),M),I2); orth.append(ok)
        if M not in distinct: distinct.append(M)
    comp=True
    for p in PERM4:
        for q in PERM4:
            if not m2eq(m2mul(LOCAL[q],LOCAL[p]),LOCAL[compose_map(p,q)]): comp=False; break
        if not comp: break
    valid=norms==[O,O] and fiszero(cross) and all(orth) and comp
    return {
        "iteration":"Iter078O-RG","lane":"A","valid":valid,
        "basis_norms":[serialize_field(x) for x in norms],"basis_cross":serialize_field(cross),
        "all_24_orthogonal":all(orth),"composition_all_24x24":comp,
        "distinct_local_matrices":len(distinct),
        "local_matrices":[[[serialize_field(x) for x in row] for row in M] for M in distinct],
    }


def class_lane(name,sig):
    G=stabilizer(sig); mats={p:global_matrix(p) for p in G}
    # full stacked fixed-space constraints
    rows=[]
    I=eye(32)
    for p in G:
        M=mats[p]
        for i in range(32): rows.append([fsub(M[i][j],I[i][j]) for j in range(32)])
    cr=rref_rank(rows,32); fixed=32-cr
    tsum=Z; chars=[]
    for p in G:
        tr=trace(mats[p]); tsum=fadd(tsum,tr); chars.append((p,tr))
    avg=fscale(Fraction(1,len(G)),tsum)
    char_dim=avg[0] if avg[1]==0 and avg[0].denominator==1 else None
    # deterministic composition controls: all group pairs (sizes <=120 => acceptable)
    comp=True
    for p in G:
        for q in G:
            pq=compose5(p,q)
            if pq not in mats or not mateq(matmul(mats[q],mats[p]),mats[pq]): comp=False; break
        if not comp: break
    serial=[([*p],serialize_field(tr)) for p,tr in chars]
    digest=hashlib.sha256(json.dumps(serial,separators=(",", ":")).encode()).hexdigest()
    valid=comp and char_dim is not None and fixed==int(char_dim)
    return {
        "iteration":"Iter078O-RG","lane":name,"valid":valid,"sigma":list(sig),
        "stabilizer_size":len(G),"constraint_rank":cr,"fixed_subspace_dimension":fixed,
        "character_average_dimension":int(char_dim) if char_dim is not None else None,
        "composition_all_pairs":comp,"character_sha256":digest,
        "character_sum":serialize_field(tsum),
    }


def lane_b(): return class_lane("B",(-1,-1,-1,-1,-1))
def lane_c(): return class_lane("C",(-1,1,1,1,1))
def lane_d(): return class_lane("D",(-1,-1,1,1,1))
LANES={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if obj.get('iteration')=='Iter078O-RG' and obj.get('lane') in LANES: got[obj['lane']]=obj
    complete=set(got)==set(LANES); valid=complete and all(bool(got[k].get('valid')) for k in LANES)
    if not valid: return {"iteration":"Iter078O-RG","execution_valid":False,"verdict":"INVALID_IMPLEMENTATION","lanes_found":sorted(got)}
    dims={"0<->5":got['B']['fixed_subspace_dimension'],"1<->4":got['C']['fixed_subspace_dimension'],"2<->3":got['D']['fixed_subspace_dimension']}
    return {
        "iteration":"Iter078O-RG","execution_valid":True,"verdict":"CONTROL_RESULT",
        "classification":"ITER078O_RG_CAUSAL_STABILIZER_RECOUPLING_SYMMETRY_REDUCES_LABELLED_FULL32_BOUNDARY_DUAL_EXACT_CONTROL_SCOPED",
        "fixed_subspace_dimensions":dims,
        "stabilizer_sizes":{"0<->5":got['B']['stabilizer_size'],"1<->4":got['C']['stabilizer_size'],"2<->3":got['D']['stabilizer_size']},
        "local_distinct_S4_matrices":got['A']['distinct_local_matrices'],
        "character_checksums":{"0<->5":got['B']['character_sha256'],"1<->4":got['C']['character_sha256'],"2<->3":got['D']['character_sha256']},
        "interpretation_ceiling":"Exact invariant dimensions under the frozen tensor/leg permutation convention for labelled equal-spin fixed-causal boundary controls; not yet a theorem that the physical extension functional must lie in these invariant subspaces.",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose lane or aggregate')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(obj,indent=2,sort_keys=True))
    if args.lane and not obj.get('valid',False): raise SystemExit(1)
    if args.aggregate_dir and not obj.get('execution_valid',False): raise SystemExit(1)

if __name__=='__main__': main()
