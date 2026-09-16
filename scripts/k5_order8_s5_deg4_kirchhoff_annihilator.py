#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json,math
from fractions import Fraction
from collections import defaultdict
import sympy as sp

V=tuple(range(5))
E=tuple((a,b) for a in V for b in V if a<b)
EI={e:i for i,e in enumerate(E)}
N=len(E); ZERO=(0,)*N
PRE='00b5ddf78474179281380606fbc3f62ca260e337'
C_ANN='K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED'
C_LOG='K5_S5_DEG4_NONRADIAL_LOG_NO_ANNIHILATOR_EXACT_SCOPED'
C_RAD='K5_S5_DEG4_RADIAL_ONLY_EXACT_SCOPED'
C_INC='K5_S5_DEG4_INCONCLUSIVE_SCOPED'

P=list(itertools.permutations(V))
def ep(p,i):
    a,b=E[i]; x,y=p[a],p[b]
    return EI[(min(x,y),max(x,y))]
def act_mon(m,p):
    q=[0]*N
    for i,x in enumerate(m):q[ep(p,i)]+=x
    return tuple(q)
def mons_deg(d):
    out=[]
    def rec(k,left,a):
        if k==N-1:out.append(tuple(a+[left]));return
        for x in range(left+1):rec(k+1,left-x,a+[x])
    rec(0,d,[]);return out
def orbits(items,group):
    unseen=set(items);out=[]
    while unseen:
        x=min(unseen);o={act_mon(x,p) for p in group};out.append(tuple(sorted(o)));unseen-=o
    return out

base=EI[(0,1)]
H=[p for p in P if {p[0],p[1]}=={0,1}]
M3=mons_deg(3)
Horb=orbits(M3,H);Gorb=orbits(M3,P)
nv=len(Horb);nh=len(Gorb)
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
            a,b=E[i];adj[a].add(b);adj[b].add(a)
        seen={0};stack=[0]
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in seen:seen.add(w);stack.append(w)
        if len(seen)==5:
            m=[0]*N
            for i in c:m[i]=1
            out[tuple(m)]=Fraction(1)
    return out
PSI=treepoly(); PSI_SYN={(1,)*N:Fraction(1)}

def deriv(poly,i):
    out={}
    for m,c in poly.items():
        if m[i]:
            q=list(m);z=q[i];q[i]-=1;out[tuple(q)]=c*z
    return out
def degree(poly):
    d={sum(m) for m in poly};assert len(d)==1;return next(iter(d))
def addterm(dst,m,c):
    if c:
        dst[m]+=c
        if dst[m]==0:del dst[m]
def build_matrix(poly):
    D=[deriv(poly,i) for i in range(N)]
    cols=[defaultdict(Fraction) for _ in range(nv+nh)]
    for j in range(nv):
        for e in range(N):
            for qmon in Q[e][j]:
                for m,c in D[e].items():
                    z=list(m);z[e]+=1
                    for i,x in enumerate(qmon):z[i]+=x
                    addterm(cols[j],tuple(z),c)
    for j,o in enumerate(Gorb):
        for qmon in o:
            for m,c in poly.items():
                z=tuple(m[i]+qmon[i] for i in range(N));addterm(cols[nv+j],z,-c)
    mons=sorted(set().union(*(set(c) for c in cols)))
    A=sp.MutableSparseMatrix(len(mons),nv+nh,{})
    for r,m in enumerate(mons):
        for c,col in enumerate(cols):
            x=col.get(m,0)
            if x:A[r,c]=sp.Rational(x.numerator,x.denominator)
    return A,mons
def radial_vectors(poly_degree):
    out=[]
    for gj,go in enumerate(Gorb):
        v=[sp.Rational(0)]*(nv+nh)
        for j,ho in enumerate(Horb):v[j]=1 if ho[0] in go else 0
        v[nv+gj]=poly_degree
        out.append(sp.Matrix(v))
    return out
def solve(poly):
    A,mons=build_matrix(poly);ns=A.nullspace();rank=A.rank()
    B=sp.Matrix.hstack(*ns) if ns else sp.zeros(nv+nh,0)
    rad=radial_vectors(degree(poly));R=sp.Matrix.hstack(*rad) if rad else sp.zeros(nv+nh,0)
    rad_in=all(B.row_join(r).rank()==B.rank() for r in rad)
    qdim=B.rank()-R.rank() if rad_in else -1
    Vmat=A[:,:nv];anns=Vmat.nullspace();ann_rank=Vmat.rank()
    sub_ok=all((A*x).is_zero_matrix for x in ns)
    ann_ok=all((Vmat*x).is_zero_matrix for x in anns)
    return {'A':A,'V':Vmat,'rows':len(mons),'rank':rank,'ns':ns,'B':B,'R':R,'rad_in':rad_in,'qdim':qdim,'anns':anns,'ann_rank':ann_rank,'sub_ok':sub_ok,'ann_ok':ann_ok}

def orbit_index(mon,orbs):
    for j,o in enumerate(orbs):
        if mon in o:return j
    raise KeyError(mon)
def poly_add(poly,m,c=1):
    out=dict(poly);out[m]=out.get(m,Fraction(0))+Fraction(c)
    if out[m]==0:del out[m]
    return out
def act_poly(poly,p):
    out={}
    for m,c in poly.items():
        mm=act_mon(m,p);out[mm]=out.get(mm,Fraction(0))+c
    return {m:c for m,c in out.items() if c}
def field_components(vcoeff):
    comps=[]
    for e in range(N):
        pe={}
        for j,c in enumerate(vcoeff):
            if not c:continue
            q=sp.Rational(c);cq=Fraction(int(q.p),int(q.q))
            for mon in Q[e][j]:
                z=list(mon);z[e]+=1;pe=poly_add(pe,tuple(z),cq)
        comps.append(pe)
    return comps
def face_tangent(comps):
    return all(all(m[e]>=1 for m in comps[e]) for e in range(N))
def equivariant(comps):
    for p in P:
        for e in range(N):
            if act_poly(comps[e],p)!=comps[ep(p,e)]:return False
    return True
def primitive_int(v):
    den=1
    for x in v:
        q=sp.Rational(x);den=math.lcm(den,int(q.q))
    ints=[int(sp.Rational(x)*den) for x in v]
    g=0
    for x in ints:g=math.gcd(g,abs(x))
    if g:ints=[x//g for x in ints]
    first=next((x for x in ints if x),1)
    if first<0:ints=[-x for x in ints]
    return ints

# Exact covariance of the complete transported basis.
eq_basis=True
for p in P:
    for e in range(N):
        ee=ep(p,e)
        for j in range(nv):
            if {act_mon(m,p) for m in Q[e][j]}!=set(Q[ee][j]):eq_basis=False;break
        if not eq_basis:break
    if not eq_basis:break

k5=solve(PSI);syn=solve(PSI_SYN)

# Deterministic K5 annihilator representative if present.
ann_rep=None;ann_rep_nonrad=False
if k5['anns']:
    ann_rep=primitive_int(list(k5['anns'][0]))
    full=sp.Matrix([sp.Rational(x) for x in ann_rep]+[sp.Rational(0)]*nh)
    ann_rep_nonrad=k5['R'].row_join(full).rank()>k5['R'].rank()

# Malformed controls.
rad0=k5['R'][:,0]
base_comps=field_components(list(rad0[:nv,0]))
malformed=[dict(x) for x in base_comps];malformed[0]=poly_add(malformed[0],ZERO,1)
non_face_rejected=not face_tangent(malformed)
broken=[{} for _ in range(N)];m=[0]*N;m[0]=4;broken[0]={tuple(m):Fraction(1)}
s5_breaking_rejected=face_tangent(broken) and not equivariant(broken)
fake_log=sp.zeros(nv+nh,1);fake_log[nv,0]=1
fake_log_rejected=not (k5['A']*fake_log).is_zero_matrix
cube=[0]*N;cube[base]=3;cube=tuple(cube);j_same=orbit_index(cube,Horb)
fake_ann=sp.zeros(nv,1);fake_ann[j_same,0]=1
fake_ann_rejected=not (k5['V']*fake_ann).is_zero_matrix

# Synthetic same-engine known annihilator:
# Q_e=9 alpha_e^3 - sum_(f != e) alpha_f^3.
adj=EI[(0,2)];dis=EI[(2,3)]
def pure_cube(edge_index):
    m=[0]*N;m[edge_index]=3;return tuple(m)
j_adj=orbit_index(pure_cube(adj),Horb);j_dis=orbit_index(pure_cube(dis),Horb)
known_syn=sp.zeros(nv,1);known_syn[j_same,0]=9;known_syn[j_adj,0]=-1;known_syn[j_dis,0]=-1
known_syn_zero=(syn['V']*known_syn).is_zero_matrix
known_syn_nonzero=any(x!=0 for x in known_syn)
synthetic_positive=(syn['qdim']>0 and len(syn['anns'])>0 and known_syn_zero and known_syn_nonzero)

checks={
 'edges_10':N==10,
 'trees_125':len(PSI)==125,
 'tree_coefficients_one':all(c==1 for c in PSI.values()),
 'psi_degree4':all(sum(m)==4 for m in PSI),
 'fixed_edge_stabilizer_12':len(H)==12,
 'degree3_monomial_count_220':len(M3)==220,
 'fixed_edge_cubic_orbits_complete':sum(len(o) for o in Horb)==220,
 's5_cubic_orbits_complete':sum(len(o) for o in Gorb)==220,
 'all120_equivariant_orbit_basis':eq_basis,
 'k5_exact_nullspace_substitution':k5['sub_ok'],
 'k5_full_radial_subspace_in_nullspace':k5['rad_in'],
 'k5_annihilator_basis_substitution':k5['ann_ok'],
 'annihilator_rep_nonradial_if_present':(ann_rep is None) or ann_rep_nonrad,
 'synthetic_same_engine_positive_control':synthetic_positive,
}
controls={
 'non_face_tangent_rejected':non_face_rejected,
 's5_breaking_rejected':s5_breaking_rejected,
 'fake_logarithmic_rejected':fake_log_rejected,
 'fake_annihilator_rejected':fake_ann_rejected,
 'synthetic_known_annihilator_exact':known_syn_zero,
 'synthetic_nonradial_logarithmic_positive':syn['qdim']>0,
 'synthetic_annihilator_kernel_positive':len(syn['anns'])>0,
 'no_period_verdict':True,
}
valid=all(checks.values()) and all(controls.values())
if not valid:classification='INVALID_IMPLEMENTATION'
elif k5['qdim']==0:classification=C_RAD
elif len(k5['anns'])>0:classification=C_ANN
elif k5['qdim']>0:classification=C_LOG
else:classification=C_INC

rep_sparse=[]
if ann_rep is not None:
    for j,c in enumerate(ann_rep):
        if c:
            rep_sparse.append({'orbit_index':j,'coefficient':c,'orbit_size':len(Horb[j]),'representative':list(Horb[j][0])})
out={
 'gate':'K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR',
 'prereg_commit':PRE,
 'status':'PASS_EXACT_SCOPED' if valid else 'INVALID_IMPLEMENTATION',
 'classification':classification,
 'checks':checks,'controls':controls,
 'orbit_data':{
   'fixed_edge_cubic_orbit_count':nv,'fixed_edge_cubic_orbit_sizes':[len(o) for o in Horb],
   's5_invariant_cubic_dimension':nh,'s5_cubic_orbit_sizes':[len(o) for o in Gorb],
 },
 'k5_exact':{
   'system_rows':k5['rows'],'system_cols':nv+nh,'rank':k5['rank'],'nullity':len(k5['ns']),
   'radial_dimension':k5['R'].rank(),'nonradial_quotient_dimension':k5['qdim'],
   'vector_only_rank':k5['ann_rank'],'annihilator_dimension':len(k5['anns']),
   'annihilator_representative_coefficients':ann_rep,
   'annihilator_representative_sparse_orbits':rep_sparse,
   'annihilator_logarithmic_quotient_zero':ann_rep is not None,
 },
 'synthetic_exact':{
   'polynomial':'prod_e alpha_e','degree':10,'system_rows':syn['rows'],'system_cols':nv+nh,
   'rank':syn['rank'],'nullity':len(syn['ns']),'radial_dimension':syn['R'].rank(),
   'nonradial_quotient_dimension':syn['qdim'],'annihilator_dimension':len(syn['anns']),
   'known_annihilator':'Q_e=9 alpha_e^3 - sum_(f != e) alpha_f^3',
 },
 'scientific_invariant_dual_period_verdict':None,
}
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
with open(args.output,'w',encoding='utf-8') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(out,indent=2,sort_keys=True))
if not valid:raise SystemExit(2)
