#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json
from fractions import Fraction
from collections import defaultdict
import sympy as sp

V=tuple(range(5))
E=tuple((a,b) for a in V for b in V if a<b)
EI={e:i for i,e in enumerate(E)}
N=len(E)
PRE='27ffc236cf2f7e3b555811f2a1b2aa1684a61ddf'
C_NON='K5_S5_FACE_TANGENT_LOG_IBP_DEG3_NONRADIAL_EXISTS_EXACT_SCOPED'
C_RAD='K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED'
C_INC='K5_S5_FACE_TANGENT_LOG_IBP_DEG3_INCONCLUSIVE_SCOPED'
ZERO=(0,)*N

def ep(p,i):
    a,b=E[i]; x,y=p[a],p[b]
    return EI[(min(x,y),max(x,y))]

P=list(itertools.permutations(V))
H=[p for p in P if {p[0],p[1]}=={0,1}]
base=EI[(0,1)]

def act_mon(m,p):
    q=[0]*N
    for i,x in enumerate(m): q[ep(p,i)]+=x
    return tuple(q)

def mons_deg(d):
    out=[]
    def rec(k,left,a):
        if k==N-1:
            out.append(tuple(a+[left])); return
        for x in range(left+1): rec(k+1,left-x,a+[x])
    rec(0,d,[])
    return out

M2=mons_deg(2)

def orbits(items,group):
    unseen=set(items); out=[]
    while unseen:
        x=min(unseen)
        o={act_mon(x,p) for p in group}
        out.append(tuple(sorted(o))); unseen-=o
    return out

Horb=orbits(M2,H)
Gorb=orbits(M2,P)
nv=len(Horb); nh=len(Gorb)
transports=[next(p for p in P if ep(p,base)==e) for e in range(N)]
Q=[]
for e in range(N):
    p=transports[e]
    Q.append([tuple(act_mon(m,p) for m in o) for o in Horb])

def treepoly():
    out={}
    for c in itertools.combinations(range(N),4):
        adj={v:set() for v in V}
        for i in c:
            a,b=E[i]; adj[a].add(b); adj[b].add(a)
        seen={0}; stack=[0]
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in seen: seen.add(w); stack.append(w)
        if len(seen)==5:
            m=[0]*N
            for i in c:m[i]=1
            out[tuple(m)]=Fraction(1)
    return out

PSI=treepoly()
PSI_SYN={(1,)*N:Fraction(1)}

def deriv(poly,i):
    out={}
    for m,c in poly.items():
        if m[i]:
            q=list(m); z=q[i]; q[i]-=1
            out[tuple(q)]=c*z
    return out

def addterm(dst,m,c):
    if c:
        dst[m]+=c
        if dst[m]==0: del dst[m]

def degree(poly):
    ds={sum(m) for m in poly}
    assert len(ds)==1
    return next(iter(ds))

def build_matrix(poly):
    D=[deriv(poly,i) for i in range(N)]
    cols=[defaultdict(Fraction) for _ in range(nv+nh)]
    for j in range(nv):
        for e in range(N):
            for qmon in Q[e][j]:
                for m,c in D[e].items():
                    z=list(m); z[e]+=1
                    for i,x in enumerate(qmon):z[i]+=x
                    addterm(cols[j],tuple(z),c)
    for j,o in enumerate(Gorb):
        for qmon in o:
            for m,c in poly.items():
                z=tuple(m[i]+qmon[i] for i in range(N))
                addterm(cols[nv+j],z,-c)
    allm=sorted(set().union(*(set(c) for c in cols)))
    A=sp.MutableSparseMatrix(len(allm),len(cols),{})
    for r,m in enumerate(allm):
        for c,col in enumerate(cols):
            x=col.get(m,0)
            if x:A[r,c]=sp.Rational(x.numerator,x.denominator)
    return A,allm

def radial_vectors(poly_degree):
    out=[]
    for gj,go in enumerate(Gorb):
        v=[sp.Rational(0)]*(nv+nh)
        for j,ho in enumerate(Horb):
            v[j]=1 if ho[0] in go else 0
        v[nv+gj]=poly_degree
        out.append(sp.Matrix(v))
    return out

def solve(poly):
    A,allm=build_matrix(poly)
    ns=A.nullspace(); rank=A.rank()
    B=sp.Matrix.hstack(*ns) if ns else sp.zeros(nv+nh,0)
    rad=radial_vectors(degree(poly))
    R=sp.Matrix.hstack(*rad) if rad else sp.zeros(nv+nh,0)
    rad_in=all(B.row_join(r).rank()==B.rank() for r in rad)
    qdim=B.rank()-R.rank() if rad_in else -1
    sub_ok=all((A*x).is_zero_matrix for x in ns)
    return {'A':A,'rows':len(allm),'rank':rank,'ns':ns,'B':B,'R':R,'rad_in':rad_in,'qdim':qdim,'sub_ok':sub_ok}

def orbit_index(mon,orbs):
    for j,o in enumerate(orbs):
        if mon in o:return j
    raise KeyError(mon)

def poly_add(p,m,c=1):
    p=dict(p); p[m]=p.get(m,Fraction(0))+Fraction(c)
    if p[m]==0:del p[m]
    return p

def act_poly(poly,p):
    out={}
    for m,c in poly.items():
        mm=act_mon(m,p); out[mm]=out.get(mm,Fraction(0))+c
    return {m:c for m,c in out.items() if c}

def field_components(vcoeff):
    comps=[]
    for e in range(N):
        pe={}
        for j,c in enumerate(vcoeff):
            if not c:continue
            cq=Fraction(int(c.p),int(c.q)) if isinstance(c,sp.Rational) else Fraction(c)
            for qmon in Q[e][j]:
                z=list(qmon); z[e]+=1
                pe=poly_add(pe,tuple(z),cq)
        comps.append(pe)
    return comps

def face_tangent(comps):
    return all(all(m[e]>=1 for m in comps[e]) for e in range(N))

def equivariant(comps):
    for p in P:
        for e in range(N):
            if act_poly(comps[e],p)!=comps[ep(p,e)]:return False
    return True

# Orbit construction completeness/covariance.
eq_basis=True
for p in P:
    for e in range(N):
        ee=ep(p,e)
        for j in range(nv):
            if {act_mon(m,p) for m in Q[e][j]}!=set(Q[ee][j]):
                eq_basis=False; break
        if not eq_basis:break
    if not eq_basis:break

k5=solve(PSI)
syn=solve(PSI_SYN)

# Real malformed-control execution.
# Start from a valid radial K5 field.
rad0=k5['R'][:,0]
base_comps=field_components(list(rad0[:nv,0]))
malformed_face=[dict(x) for x in base_comps]
malformed_face[0]=poly_add(malformed_face[0],ZERO,1)
non_face_rejected=not face_tangent(malformed_face)

broken=[{} for _ in range(N)]
m=[0]*N; m[0]=3
broken[0]={tuple(m):Fraction(1)}
s5_breaking_rejected=face_tangent(broken) and (not equivariant(broken))

fake=sp.zeros(nv+nh,1); fake[nv,0]=1
fake_log_rejected=not (k5['A']*fake).is_zero_matrix

# Synthetic fixture through the same exact builder/solver.
sq=[0]*N; sq[base]=2; sq=tuple(sq)
jh=orbit_index(sq,Horb); jg=orbit_index(sq,Gorb)
known=sp.zeros(nv+nh,1); known[jh,0]=1; known[nv+jg,0]=1
known_syn_identity=(syn['A']*known).is_zero_matrix
known_syn_nonradial=syn['R'].row_join(known).rank()>syn['R'].rank()
synthetic_same_engine=(syn['qdim']>0 and known_syn_identity and known_syn_nonradial)

checks={
 'edges_10':N==10,
 'trees_125':len(PSI)==125,
 'coeff_one':all(c==1 for c in PSI.values()),
 'psi_degree4':all(sum(m)==4 for m in PSI),
 'fixed_edge_stabilizer_12':len(H)==12,
 'fixed_edge_degree2_orbits_complete':sum(len(o) for o in Horb)==len(M2),
 's5_degree2_orbits_complete':sum(len(o) for o in Gorb)==len(M2),
 'all120_equivariant_orbit_basis':eq_basis,
 'k5_exact_nullspace_substitution':k5['sub_ok'],
 'k5_full_radial_subspace_in_nullspace':k5['rad_in'],
 'synthetic_same_engine_positive_control':synthetic_same_engine,
}
controls={
 'non_face_tangent_rejected':non_face_rejected,
 's5_breaking_rejected':s5_breaking_rejected,
 'fake_logarithmic_rejected':fake_log_rejected,
 'synthetic_known_nonradial_identity_exact':known_syn_identity,
 'synthetic_known_direction_not_radial':known_syn_nonradial,
 'no_period_verdict':True,
}
valid=all(checks.values()) and all(controls.values())
classification='INVALID_IMPLEMENTATION' if not valid else (C_NON if k5['qdim']>0 else C_RAD if k5['qdim']==0 else C_INC)
out={
 'gate':'K5_ORDER8_S5_DEG3_FACE_TANGENT_LOG_IBP_SYZYGY_CONTROL_ONLY_REPAIR',
 'prereg_commit':PRE,
 'status':'PASS_EXACT_SCOPED' if valid else 'INVALID_IMPLEMENTATION',
 'classification':classification,
 'checks':checks,
 'controls':controls,
 'orbit_data':{
   'fixed_edge_degree2_orbit_count':nv,
   'fixed_edge_degree2_orbit_sizes':[len(o) for o in Horb],
   's5_invariant_quadratic_dimension':nh,
   's5_degree2_orbit_sizes':[len(o) for o in Gorb],
 },
 'k5_exact':{
   'system_rows':k5['rows'],'system_cols':nv+nh,'rank':k5['rank'],'nullity':len(k5['ns']),
   'radial_dimension':k5['R'].rank(),'nonradial_quotient_dimension':k5['qdim'],
 },
 'synthetic_exact':{
   'polynomial':'prod_e alpha_e','degree':10,'system_rows':syn['rows'],'system_cols':nv+nh,
   'rank':syn['rank'],'nullity':len(syn['ns']),'radial_dimension':syn['R'].rank(),
   'nonradial_quotient_dimension':syn['qdim'],
   'known_direction':'v_e=alpha_e^3; H2=sum_e alpha_e^2',
 },
 'scientific_invariant_dual_period_verdict':None,
}
ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
with open(args.output,'w',encoding='utf-8') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(out,indent=2,sort_keys=True))
if not valid:raise SystemExit(2)
