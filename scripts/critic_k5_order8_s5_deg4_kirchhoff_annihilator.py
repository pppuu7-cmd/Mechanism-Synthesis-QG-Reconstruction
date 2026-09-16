#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
SUMMARY=ROOT/'results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json'
VTX=tuple(range(5))
EDGES=tuple((a,b) for a in VTX for b in VTX if a<b)
EIDX={e:i for i,e in enumerate(EDGES)}
N=10; ROOTV=0; NR=(1,2,3,4); ZERO=(0,)*N
PRE='7cde5bd6838e40b7d10fe7dd9707f04cc3198662'
EXPECTED_CLASS='K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED'

# ---------- exact polynomial utilities ----------
def padd(a,b):
    out=dict(a)
    for m,c in b.items():
        out[m]=out.get(m,Fraction(0))+c
        if out[m]==0:del out[m]
    return out

def pmul(a,b):
    out={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb))
            out[m]=out.get(m,Fraction(0))+ca*cb
            if out[m]==0:del out[m]
    return out

def pscale(a,c):return {m:c*x for m,x in a.items() if c*x}
def mono(i,c=1):
    m=[0]*N;m[i]=1
    return {tuple(m):Fraction(c)}
def pderiv(a,i):
    out={}
    for m,c in a.items():
        if m[i]:
            q=list(m);z=q[i];q[i]-=1;out[tuple(q)]=c*z
    return out

def pshift(a,s):
    out={}
    for m,c in a.items():
        q=tuple(m[i]+s[i] for i in range(N));out[q]=out.get(q,Fraction(0))+c
    return out

def psign(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def incidence(edge):
    a,b=edge;r=[0]*4
    if a!=0:r[a-1]-=1
    if b!=0:r[b-1]+=1
    return tuple(r)

def laplacian_poly():
    L=[[{} for _ in range(4)] for _ in range(4)]
    for e,edge in enumerate(EDGES):
        r=incidence(edge)
        for i in range(4):
            for j in range(4):
                if r[i]*r[j]:L[i][j]=padd(L[i][j],mono(e,r[i]*r[j]))
    return L

def det4(M):
    out={}
    for p in itertools.permutations(range(4)):
        t={ZERO:Fraction(psign(p))}
        for i,j in enumerate(p):t=pmul(t,M[i][j])
        out=padd(out,t)
    return out

def is_tree(c):
    adj={v:set() for v in VTX}
    for e in c:
        a,b=EDGES[e];adj[a].add(b);adj[b].add(a)
    seen={0};st=[0]
    while st:
        v=st.pop()
        for w in adj[v]:
            if w not in seen:seen.add(w);st.append(w)
    return len(c)==4 and len(seen)==5

def tree_poly():
    out={}
    for c in itertools.combinations(range(N),4):
        if is_tree(c):
            m=[0]*N
            for e in c:m[e]=1
            out[tuple(m)]=Fraction(1)
    return out

# ---------- group/orbit reconstruction ----------
PERMS=list(itertools.permutations(VTX))
def eperm(p,eidx):
    a,b=EDGES[eidx];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def act_mon(m,p):
    q=[0]*N
    for i,x in enumerate(m):q[eperm(p,i)]+=x
    return tuple(q)
def monomials(d):
    out=[]
    def rec(i,left,a):
        if i==N-1:out.append(tuple(a+[left]));return
        for x in range(left+1):rec(i+1,left-x,a+[x])
    rec(0,d,[]);return out
def orbit_partition(items,group):
    unseen=set(items);out=[]
    while unseen:
        x=min(unseen);o={act_mon(x,p) for p in group};out.append(tuple(sorted(o)));unseen-=o
    return out
BASE=EIDX[(0,1)]
STAB=[p for p in PERMS if {p[0],p[1]}=={0,1}]
M3=monomials(3)
HORB=orbit_partition(M3,STAB);GORB=orbit_partition(M3,PERMS)
NV=len(HORB);NH=len(GORB)
TRANS=[next(p for p in PERMS if eperm(p,BASE)==e) for e in range(N)]
QBAS=[]
for e,p in enumerate(TRANS):QBAS.append([tuple(act_mon(m,p) for m in o) for o in HORB])

# ---------- independently built exact identity matrices ----------
def add(dst,m,c):
    if c:
        dst[m]+=c
        if dst[m]==0:del dst[m]
def build(poly):
    d=[pderiv(poly,e) for e in range(N)]
    cols=[defaultdict(Fraction) for _ in range(NV+NH)]
    for j in range(NV):
        for e in range(N):
            for q in QBAS[e][j]:
                shift=list(q);shift[e]+=1
                for m,c in d[e].items():add(cols[j],tuple(m[i]+shift[i] for i in range(N)),c)
    for j,o in enumerate(GORB):
        for q in o:
            for m,c in poly.items():add(cols[NV+j],tuple(m[i]+q[i] for i in range(N)),-c)
    mons=sorted(set().union(*(set(x) for x in cols)))
    A=sp.MutableSparseMatrix(len(mons),NV+NH,{})
    for r,m in enumerate(mons):
        for c,col in enumerate(cols):
            x=col.get(m,Fraction(0))
            if x:A[r,c]=sp.Rational(x.numerator,x.denominator)
    return A,mons

def radial(polydeg):
    vecs=[]
    for gj,go in enumerate(GORB):
        v=sp.zeros(NV+NH,1)
        for j,ho in enumerate(HORB):v[j,0]=1 if ho[0] in go else 0
        v[NV+gj,0]=polydeg
        vecs.append(v)
    return vecs

def solve(poly):
    A,mons=build(poly);V=A[:,:NV]
    ns=A.nullspace();anns=V.nullspace();rv=radial(next(iter({sum(m) for m in poly})))
    R=sp.Matrix.hstack(*rv)
    B=sp.Matrix.hstack(*ns)
    rin=all(B.row_join(x).rank()==B.rank() for x in rv)
    return {'A':A,'V':V,'rows':len(mons),'rank':A.rank(),'nullity':len(ns),'anns':anns,
            'ann_rank':V.rank(),'ann_dim':len(anns),'R':R,'rad_dim':R.rank(),
            'qdim':B.rank()-R.rank() if rin else -1,'rad_in':rin,'ns':ns}

def field_from_coeff(coeff):
    comps=[]
    for e in range(N):
        p={}
        for j,c in enumerate(coeff):
            if not c:continue
            for q in QBAS[e][j]:
                s=list(q);s[e]+=1;s=tuple(s);p[s]=p.get(s,Fraction(0))+Fraction(c)
                if p[s]==0:del p[s]
        comps.append(p)
    return comps
def act_poly(ply,p):
    out={}
    for m,c in ply.items():
        q=act_mon(m,p);out[q]=out.get(q,Fraction(0))+c
    return {m:c for m,c in out.items() if c}
def face_tangent(comps):return all(all(m[e]>=1 for m in comps[e]) for e in range(N))
def equivariant(comps):
    for p in PERMS:
        for e in range(N):
            if act_poly(comps[e],p)!=comps[eperm(p,e)]:return False
    return True

def idx(mon,orbs):
    return next(i for i,o in enumerate(orbs) if mon in o)

summary=json.loads(SUMMARY.read_text(encoding='utf-8'))
reported=summary['k5_exact']
rep=[sp.Rational(x) for x in reported['annihilator_representative_coefficients']]

psi_det=det4(laplacian_poly());psi_tree=tree_poly()
k5=solve(psi_det)
fullrep=sp.Matrix(rep+[sp.Rational(0)]*NH)
repV=sp.Matrix(rep)
comps=field_from_coeff([int(x) for x in rep])

# Synthetic reconstruction, not using Researcher synthetic values.
syn={(1,)*N:Fraction(1)};ss=solve(syn)
pure=[0]*N;pure[BASE]=3;pure=tuple(pure)
adj=[0]*N;adj[EIDX[(0,2)]]=3;adj=tuple(adj)
dis=[0]*N;dis[EIDX[(2,3)]]=3;dis=tuple(dis)
known=sp.zeros(NV,1);known[idx(pure,HORB),0]=9;known[idx(adj,HORB),0]=-1;known[idx(dis,HORB),0]=-1

# Malformed independent controls.
nonface=[dict(x) for x in comps];nonface[0][ZERO]=Fraction(1)
broken=[{} for _ in range(N)];mm=[0]*N;mm[0]=4;broken[0]={tuple(mm):Fraction(1)}
fake_log=sp.zeros(NV+NH,1);fake_log[NV,0]=1
fake_ann=sp.zeros(NV,1);fake_ann[0,0]=1

checks={
 'summary_source_matches_frozen_run':summary['source']['run_id']==35043883583 and summary['source']['head_sha']=='53bdd4d6adb5e470192292d7ef2616a57e15fc6e',
 'summary_classification_expected':summary['classification']==EXPECTED_CLASS,
 'determinant_equals_independent_tree_polynomial':psi_det==psi_tree,
 'tree_count_125':len(psi_tree)==125,
 'all_tree_coefficients_one':all(c==1 for c in psi_tree.values()),
 'cubic_monomial_count_220':len(M3)==220,
 'stabilizer_order_12':len(STAB)==12,
 'fixed_edge_orbit_census_matches_reported':len(HORB)==33 and [len(o) for o in HORB]==summary['orbit_data']['fixed_edge_cubic_orbit_sizes'],
 'global_orbit_census_matches_reported':len(GORB)==7 and [len(o) for o in GORB]==summary['orbit_data']['s5_cubic_orbit_sizes'],
 'independent_system_dimensions_match':k5['rows']==reported['system_rows'] and (NV+NH)==reported['system_cols'],
 'independent_rank_nullity_match':k5['rank']==reported['rank'] and k5['nullity']==reported['nullity'],
 'independent_radial_dimension_match':k5['rad_dim']==reported['radial_dimension'] and k5['qdim']==reported['nonradial_quotient_dimension'],
 'independent_annihilator_dimension_match':k5['ann_rank']==reported['vector_only_rank'] and k5['ann_dim']==reported['annihilator_dimension'],
 'reported_annihilator_direct_zero':(k5['V']*repV).is_zero_matrix and (k5['A']*fullrep).is_zero_matrix,
 'reported_annihilator_nonradial':k5['R'].row_join(fullrep).rank()>k5['R'].rank(),
 'reported_annihilator_face_tangent':face_tangent(comps),
 'reported_annihilator_all120_s5_equivariant':equivariant(comps),
 'synthetic_known_annihilator_direct_zero':(ss['V']*known).is_zero_matrix,
 'synthetic_annihilator_kernel_nontrivial':ss['ann_dim']>0 and ss['qdim']>0,
}
controls={
 'non_face_tangent_rejected':not face_tangent(nonface),
 's5_breaking_rejected':face_tangent(broken) and not equivariant(broken),
 'fake_logarithmic_rejected':not (k5['A']*fake_log).is_zero_matrix,
 'fake_annihilator_rejected':not (k5['V']*fake_ann).is_zero_matrix,
}
valid=all(checks.values()) and all(controls.values())
verdict='CONFIRMED_SCOPED' if valid else 'INVALID_IMPLEMENTATION'
out={
 'gate':'K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC',
 'prereg_commit':PRE,
 'status':'PASS_EXACT_SCOPED' if valid else 'FAIL_REVIEW',
 'verdict':verdict,
 'checks':checks,'controls':controls,
 'independent_k5':{'system_rows':k5['rows'],'system_cols':NV+NH,'rank':k5['rank'],'nullity':k5['nullity'],
                   'radial_dimension':k5['rad_dim'],'nonradial_quotient_dimension':k5['qdim'],
                   'vector_only_rank':k5['ann_rank'],'annihilator_dimension':k5['ann_dim']},
 'reviewed_researcher':{'classification':summary['classification'],'run_id':summary['source']['run_id'],
                        'artifact_id':summary['source']['artifact_id'],'production_json_sha256':summary['source']['production_json_sha256']},
 'scientific_invariant_dual_period_verdict':None,
}
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
Path(args.output).parent.mkdir(parents=True,exist_ok=True)
Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if not valid:raise SystemExit(2)
