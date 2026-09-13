#!/usr/bin/env python3
"""Iter073D: exact extreme-ray geometry of transitive source proper faces."""
from __future__ import annotations
import argparse,itertools,json,math
from collections import Counter
from pathlib import Path
import sympy as sp
from distributional.iter073a_k4_signed_cutspace_face_atlas import (
    TREES,Lmat,source_signs,dag_feasible
)

TRANS=['++++','+++-','++--','+---']

def primitive_positive(vec):
    den=1
    for v in vec: den=sp.ilcm(den,int(sp.denom(v)))
    vals=[int(v*den) for v in vec]
    if all(v<0 for v in vals): vals=[-v for v in vals]
    if not all(v>0 for v in vals): return None
    g=0
    for v in vals: g=math.gcd(g,abs(v))
    return tuple(v//g for v in vals)

def extreme_rays(A):
    """Positive support-minimal circuits of A, embedded in full active coordinates."""
    m=A.cols; rays=[]; supports=[]
    for r in range(1,m+1):
        for U in itertools.combinations(range(m),r):
            B=A[:,list(U)]
            if r-int(B.rank())!=1: continue
            ns=B.nullspace()
            if len(ns)!=1: continue
            pv=primitive_positive(list(ns[0]))
            if pv is None: continue
            su=frozenset(U)
            if any(old < su for old in supports):
                continue
            full=[0]*m
            for i,v in zip(U,pv): full[i]=v
            t=tuple(full)
            if t not in rays:
                rays.append(t); supports.append(su)
    pairs=sorted(zip(rays,supports),key=lambda z:z[0])
    return [p[0] for p in pairs],[p[1] for p in pairs]

def face_record(S,signs,L):
    A=L[list(S),:].T*sp.diag(*[signs[e] for e in S])
    rank=int(A.rank()); nu=len(S)-rank
    rays,supp=extreme_rays(A)
    if rays:
        w=[sum(ray[i] for ray in rays) for i in range(len(S))]
        strict=all(v>0 for v in w)
        sw=sum(w); norm=[sp.Rational(v,sw) for v in w]
        if len(rays)==1:
            aff=0
        else:
            R=sp.Matrix([[sp.Rational(v) for v in ray] for ray in rays])
            # Normalize each extreme ray to the simplex section before affine-rank calculation.
            NR=[]
            for ray in rays:
                sr=sum(ray); NR.append([sp.Rational(v,sr) for v in ray])
            base=sp.Matrix(NR[0])
            D=sp.Matrix.hstack(*[sp.Matrix(v)-base for v in NR[1:]]) if len(NR)>1 else sp.zeros(len(S),0)
            aff=int(D.rank())
    else:
        w=[]; strict=False; norm=[]; aff=-1
    return {
        'S':list(S),'m':len(S),'rank':rank,'nu':nu,
        'ray_count':len(rays),'rays':[list(v) for v in rays],
        'ray_support_sizes':[len(s) for s in supp],
        'strict_sum_witness':w,'strict_relative_interior':strict,
        'normalized_witness':[str(v) for v in norm],
        'normalized_affine_dim':aff,
    }

def records_for(label,tree):
    signs=source_signs(label); L,_=Lmat(tree); out=[]
    for m in range(1,6):
        for S in itertools.combinations(range(6),m):
            if dag_feasible(S,signs): out.append(face_record(S,signs,L))
    return out

def canonical_records(rows):
    return tuple((tuple(r['S']),r['m'],r['rank'],r['nu'],tuple(tuple(x) for x in r['rays']),r['normalized_affine_dim']) for r in rows)

def orbit_signature(rows):
    return tuple(sorted((r['m'],r['nu'],r['ray_count'],tuple(sorted(r['ray_support_sizes'])),r['normalized_affine_dim']) for r in rows))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    source={}; p1=p2=p3=p4=p5=True; osigs=[]
    for lab in TRANS:
        ref=None; basis={}
        for tr in TREES:
            rows=records_for(lab,tr); can=canonical_records(rows)
            if ref is None: ref=can
            else: p5 &= (can==ref)
            p1 &= (len(rows)==6 and Counter((r['m'],r['nu']) for r in rows)==Counter({(3,1):2,(4,1):1,(5,2):3}))
            p2 &= all(r['ray_count']>=1 and r['strict_relative_interior'] for r in rows)
            p3 &= all(r['normalized_affine_dim']==r['nu']-1 for r in rows)
            p4 &= all((r['ray_count']>=2 and r['normalized_affine_dim']==1) for r in rows if (r['m'],r['nu'])==(5,2))
            basis[tr]=rows
        sig=orbit_signature(basis['S0']); osigs.append(sig)
        source[lab]={'orbit_signature':[list(x) for x in sig],'basis':basis}
    p6=all(s==osigs[0] for s in osigs)
    neg=records_for('++-+','S0'); p7=(len(neg)==0)
    ok=bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out={
        'iteration':'Iter073D','source_classes':TRANS,
        'predicates':{
            'P1_ITER073A_FACES_EXACTLY_RECOVERED':bool(p1),
            'P2_EXTREME_RAYS_AND_STRICT_WITNESS':bool(p2),
            'P3_NORMALIZED_DIM_EQUALS_NU_MINUS_ONE':bool(p3),
            'P4_FIVE_EDGE_NULLITY2_SECTION_NONDEGENERATE':bool(p4),
            'P5_BASIS_CANONICAL_RAYS_CONSISTENT':bool(p5),
            'P6_TRANSITIVE_S4_ORBIT_SIGNATURE_EQUAL':bool(p6),
            'P7_NONTRANSITIVE_NEGATIVE_CONTROL_EMPTY':bool(p7)},
        'negative_control_faces':len(neg),
        'classification':'ITER073D_TRANSITIVE_PROPER_FACE_CONES_NONDEGENERATE_EXACT_SCOPED' if ok else 'ITER073D_PROPER_FACE_CONE_GEOMETRY_FAIL',
        'source':source,
        'claim_lock':'Nondegenerate positive-face cone geometry only; no nonzero epsilon coefficient or distributional boundary-value theorem.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps({k:v for k,v in out.items() if k!='source'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
