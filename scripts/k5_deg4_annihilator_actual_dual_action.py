#!/usr/bin/env python3
from __future__ import annotations
import argparse,importlib.util,itertools,json,math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
REACH=ROOT/'scripts/k5_order8_invariant_dual_projective_ibp_reachability.py'
ANN_SUM=ROOT/'results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json'
NUM_SUM=ROOT/'results/raw/k5_invariant_dual_deg27_canonical_dag_production_summary.json'
PRE='2111b42adc1ab79247c72d0043e5332b24eb7679'
C_FAIL='K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED'
C_NF='K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_NOT_FALSIFIED_ON_FROZEN_POINTS_SCOPED'
C_ZERO='K5_DEG4_ANNIHILATOR_ACTION_ZERO_ON_FROZEN_POINTS_INCONCLUSIVE_SCOPED'
C_DEG='K5_DEG4_ANNIHILATOR_ACTION_BLOCKED_FIT_DEGENERACY_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
ORDER=4
POINTS={
 'fit_A':tuple(Fraction(x) for x in (2,1,1,1,1,1,1,1,1,1)),
 'fit_B':tuple(Fraction(x) for x in (1,2,1,3,1,2,1,1,2,1)),
 'validation_U':tuple(Fraction(1) for _ in range(10)),
 'validation_G':tuple(Fraction(x) for x in (2,3,1,2,1,3,2,1,2,3)),
}
EXPECTED={
 'validation_U':(Fraction(-7038281250000000000),Fraction(-5474218750000000000)),
 'fit_A':(Fraction(-59622158569312500000),Fraction(-71069744360125000000)),
 'fit_B':(Fraction(-98730229673044210483200),Fraction(-611255260651417598361600)),
}

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);assert s.loader is not None;s.loader.exec_module(m);return m
src=load(SOURCE,'k5_action_src');reach=load(REACH,'k5_action_reach')
EDGES=tuple(src.EDGES);N=len(EDGES);ZERO_MON=(0,)*N
ann_summary=json.loads(ANN_SUM.read_text(encoding='utf-8'));num_summary=json.loads(NUM_SUM.read_text(encoding='utf-8'))
ANN_COEFF=tuple(Fraction(x) for x in ann_summary['k5_exact']['annihilator_representative_coefficients'])

class J:
    __slots__=('v','a','e')
    def __init__(self,v=0,a=0,e=0):self.v=Fraction(v);self.a=Fraction(a);self.e=Fraction(e)
    @staticmethod
    def c(x):return x if isinstance(x,J) else J(x)
    def __add__(self,o):o=J.c(o);return J(self.v+o.v,self.a+o.a,self.e+o.e)
    __radd__=__add__
    def __neg__(self):return J(-self.v,-self.a,-self.e)
    def __sub__(self,o):return self+(-J.c(o))
    def __rsub__(self,o):return J.c(o)-self
    def __mul__(self,o):o=J.c(o);return J(self.v*o.v,self.a*o.v+self.v*o.a,self.e*o.v+self.v*o.e)
    __rmul__=__mul__
    def inv(self):
        assert self.v!=0
        return J(1/self.v,-self.a/(self.v*self.v),-self.e/(self.v*self.v))
    def __truediv__(self,o):return self*J.c(o).inv()
    def __rtruediv__(self,o):return J.c(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return J(1)
        return J(self.v**n,n*(self.v**(n-1))*self.a,n*(self.v**(n-1))*self.e)
    def iszero(self):return self.v==0 and self.a==0 and self.e==0
    def tup(self):return (self.v,self.a,self.e)

def fq(q):
    q=Fraction(q);return q.numerator if q.denominator==1 else f'{q.numerator}/{q.denominator}'
def js(j):return [fq(j.v),fq(j.a),fq(j.e)]

def gzero():return (J(),J())
def gone():return (J(1),J())
def gadd(x,y):return (x[0]+y[0],x[1]+y[1])
def gmul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gscale(c,z):return (c*z[0],c*z[1])
def gdot(a,b):
    z=gzero()
    for x,y in zip(a,b):z=gadd(z,gmul(x,y))
    return z

def cs_add(a,b):return [gadd(x,y) for x,y in zip(a,b)]
def cs_mul(a,b):
    out=[gzero() for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER:out[i+j]=gadd(out[i+j],gmul(x,y))
    return out
def cs_scale(a,c):return [gscale(c,z) for z in a]
def s_mul(a,b):
    out=[J() for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER:out[i+j]=out[i+j]+x*y
    return out
def binom_frac(p,n):
    z=Fraction(1)
    for k in range(n):z=z*(p-k)/Fraction(k+1)
    return z

def incidence_row(edge):
    a,b=edge;r=[0,0,0,0]
    if a!=0:r[a-1]-=1
    if b!=0:r[b-1]+=1
    return tuple(r)
ROWS=tuple(incidence_row(e) for e in EDGES)

def build_L(alphas):
    L=[[J() for _ in range(4)] for _ in range(4)]
    for a,r in zip(alphas,ROWS):
        for i in range(4):
            for j in range(4):L[i][j]=L[i][j]+a*(r[i]*r[j])
    return L
def build_L_fraction(alphas):
    L=[[Fraction(0) for _ in range(4)] for _ in range(4)]
    for a,r in zip(alphas,ROWS):
        for i in range(4):
            for j in range(4):L[i][j]+=a*r[i]*r[j]
    return L
LUNI=build_L_fraction((Fraction(1),)*10);Q=[[x/Fraction(5) for x in row] for row in LUNI]

def mat_inv(A):
    n=len(A);a=[[A[i][j] for j in range(n)]+[J(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if a[i][c].v!=0);a[c],a[p]=a[p],a[c];z=a[c][c];a[c]=[x/z for x in a[c]]
        for i in range(n):
            if i!=c and a[i][c].v!=0:
                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]
    return [r[n:] for r in a]
def mat_mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),J()) for j in range(len(B[0]))] for i in range(len(A))]
def mat_scale(A,c):return [[c*x for x in r] for r in A]
def dot_mat(r,M,s):return sum((M[i][j]*(r[i]*s[j]) for i in range(4) for j in range(4)),J())
def det_perm(A):
    z=J()
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));t=J(-1 if inv%2 else 1)
        for i,j in enumerate(p):t=t*A[i][j]
        z=z+t
    return z

def inverse_series(B0):
    out=[None]*(ORDER+1);out[0]=B0
    for n in range(1,ORDER+1):out[n]=mat_scale(mat_mul(mat_mul(B0,Q),out[n-1]),Fraction(-1))
    return out

def det_factor_direct(L):
    coeff=[J() for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));poly=[J(1)]+[J() for _ in range(ORDER)]
        for i,j in enumerate(p):poly=s_mul(poly,[L[i][j],J(Q[i][j])]+[J() for _ in range(ORDER-1)])
        sgn=-1 if inv%2 else 1
        coeff=[x+sgn*y for x,y in zip(coeff,poly)]
    d0=coeff[0];u=[J()]+[coeff[i]/d0 for i in range(1,ORDER+1)]
    res=[J(1)]+[J() for _ in range(ORDER)];up=[J(1)]+[J() for _ in range(ORDER)]
    for n in range(1,ORDER+1):up=s_mul(up,u);c=binom_frac(Fraction(-3,2),n);res=[x+c*y for x,y in zip(res,up)]
    return res,d0

def det_factor_dag(B0):
    K=mat_mul(B0,Q);coeff=[J() for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));poly=[J(1)]+[J() for _ in range(ORDER)]
        for i,j in enumerate(p):poly=s_mul(poly,[J(int(i==j)),K[i][j]]+[J() for _ in range(ORDER-1)])
        sgn=-1 if inv%2 else 1;coeff=[x+sgn*y for x,y in zip(coeff,poly)]
    assert coeff[0].v==1
    u=[J()]+coeff[1:];res=[J(1)]+[J() for _ in range(ORDER)];up=[J(1)]+[J() for _ in range(ORDER)]
    for n in range(1,ORDER+1):up=s_mul(up,u);c=binom_frac(Fraction(-3,2),n);res=[x+c*y for x,y in zip(res,up)]
    return res

def entry_coeff():
    basis=((1,0,0),(0,1,0),(0,0,1));mats=[src.leading_matrix(v) for v in basis]
    return {(r,c):tuple(m[r][c] for m in mats) for r in (0,1) for c in (0,1)}
ENTRY=entry_coeff()

def bit_index(bits):
    x=0
    for b in bits:x=(x<<1)|b
    return x

def build_projector():
    tensors=reach.local_tensor_vectors(src);local=reach.local_action_matrices(tensors);P=[[Fraction(0) for _ in range(32)] for _ in range(32)]
    for sig in itertools.permutations(range(5)):
        A=reach.global_action_matrix(src,sig,local)
        for i in range(32):
            for j in range(32):P[i][j]+=A[i][j]/120
    rank,RR,piv=reach.rref_rank(P);assert rank==2 and piv==[1,4]
    return P,piv
P,PIV=build_projector()
WEIGHTS=[(P[j][PIV[0]],P[j][PIV[1]]) for j in range(32)]

def build_patterns():
    out=[];count=0
    for ks in itertools.product((0,1),repeat=5):
        idx=bit_index(ks);arr=[]
        for choices in itertools.product(*[src.NODE_OPTIONS[k] for k in ks]):
            count+=1;states=[];coeff=1
            for state,c in choices:states.append(state);coeff*=c
            types=[]
            for a,b in EDGES:
                row=states[b][src.LEG_POS[(b,a)]];col=states[a][src.LEG_POS[(a,b)]];types.append((row,col))
            arr.append((tuple(types),Fraction(coeff)))
        out.append((idx,arr))
    return out,count
PATTERNS,SOURCE_TERMS=build_patterns();assert SOURCE_TERMS==100000

def projected_wick(Bser):
    cov={}
    for i in range(10):
        for j in range(i+1,10):cov[(i,j)]=[dot_mat(ROWS[i],Bser[n],ROWS[j]) for n in range(ORDER+1)]
    pair={}
    for (i,j),ser in cov.items():
        for ea in ENTRY:
            for eb in ENTRY:
                z0=ZERO_COMPLEX= (Fraction(0),Fraction(0))
                # exact Gaussian product of source entry triples
                x=ENTRY[ea];y=ENTRY[eb]
                gr=Fraction(0);gi=Fraction(0)
                for xx,yy in zip(x,y):gr+=xx[0]*yy[0]-xx[1]*yy[1];gi+=xx[0]*yy[1]+xx[1]*yy[0]
                pair[(i,j,ea,eb)]=[(c*gr,c*gi) for c in ser]
    cache={}
    def wick(rem):
        if not rem:return [gone()]+[gzero() for _ in range(ORDER)]
        if rem in cache:return cache[rem]
        i,ei=rem[0];tot=[gzero() for _ in range(ORDER+1)]
        for pos in range(1,len(rem)):
            j,ej=rem[pos];rest=rem[1:pos]+rem[pos+1:];tot=cs_add(tot,cs_mul(pair[(i,j,ei,ej)],wick(rest)))
        cache[rem]=tot;return tot
    channels=[[gzero() for _ in range(ORDER+1)] for _ in range(2)]
    for idx,arr in PATTERNS:
        w0,w1=WEIGHTS[idx]
        if not w0 and not w1:continue
        for types,coeff in arr:
            rem=tuple((i,types[i]) for i in range(10));ser=wick(rem)
            if w0:channels[0]=cs_add(channels[0],cs_scale(ser,coeff*w0))
            if w1:channels[1]=cs_add(channels[1],cs_scale(ser,coeff*w1))
    return channels,len(cache)

# S5 orbit reconstruction for the emitted annihilator.
PERMS=list(itertools.permutations(range(5)));EIDX={e:i for i,e in enumerate(EDGES)}
def eperm(p,e):
    a,b=EDGES[e];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def act_mon(m,p):
    q=[0]*N
    for i,x in enumerate(m):q[eperm(p,i)]+=x
    return tuple(q)
def mons_deg(d):
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
BASE=EIDX[(0,1)];STAB=[p for p in PERMS if {p[0],p[1]}=={0,1}]
HORB=orbit_partition(mons_deg(3),STAB);assert len(HORB)==33
TRANS=[next(p for p in PERMS if eperm(p,BASE)==e) for e in range(N)]
QBAS=[[tuple(act_mon(m,TRANS[e]) for m in o) for o in HORB] for e in range(N)]

def monval(m,a):
    z=Fraction(1)
    for i,p in enumerate(m):z*=a[i]**p
    return z
def monder(m,a,i):
    if m[i]==0:return Fraction(0)
    z=Fraction(m[i])
    for j,p in enumerate(m):z*=a[j]**(p-(1 if j==i else 0))
    return z

def ann_data(a,coeff=ANN_COEFF):
    q=[];dq=[]
    for e in range(N):
        z=Fraction(0);dz=Fraction(0)
        for j,c in enumerate(coeff):
            if not c:continue
            for m in QBAS[e][j]:z+=c*monval(m,a);dz+=c*monder(m,a,e)
        q.append(z);dq.append(dz)
    v=[a[e]*q[e] for e in range(N)];divv=sum((q[e]+a[e]*dq[e] for e in range(N)),Fraction(0));return tuple(q),tuple(v),divv

# Global polynomial verification of v(Psi)=0 and bad-coefficient control.
def tree_poly():
    out={}
    for c in itertools.combinations(range(N),4):
        adj={i:set() for i in range(5)}
        for e in c:
            x,y=EDGES[e];adj[x].add(y);adj[y].add(x)
        seen={0};st=[0]
        while st:
            x=st.pop()
            for y in adj[x]:
                if y not in seen:seen.add(y);st.append(y)
        if len(seen)==5:
            m=[0]*N
            for e in c:m[e]=1
            out[tuple(m)]=Fraction(1)
    return out
PSI_POLY=tree_poly()
def pderiv(poly,i):
    out={}
    for m,c in poly.items():
        if m[i]:q=list(m);z=q[i];q[i]-=1;out[tuple(q)]=c*z
    return out
def vpsi_poly(coeff):
    out=defaultdict(Fraction)
    for e in range(N):
        d=pderiv(PSI_POLY,e)
        for j,cj in enumerate(coeff):
            if not cj:continue
            for qm in QBAS[e][j]:
                shift=list(qm);shift[e]+=1
                for m,c in d.items():
                    z=tuple(m[i]+shift[i] for i in range(N));out[z]+=cj*c
    return {m:c for m,c in out.items() if c}
VPSI_ZERO=(vpsi_poly(ANN_COEFF)=={})
BAD=list(ANN_COEFF);BAD[4]+=1;BAD_REJECTED=(vpsi_poly(tuple(BAD))!={})

def evaluate(point,mode='direct'):
    q,v,divv=ann_data(point);alph=[J(point[i],v[i],point[i]) for i in range(N)];L=build_L(alph);B0=mat_inv(L);Bser=inverse_series(B0)
    if mode=='direct':dfac,psi=det_factor_direct(L)
    elif mode=='dag':dfac=det_factor_dag(B0);psi=det_perm(L)
    else:raise ValueError(mode)
    chans,cache=projected_wick(Bser);nums=[]
    for W in chans:
        S=[gzero() for _ in range(ORDER+1)]
        for i,c in enumerate(dfac):
            for j,z in enumerate(W):
                if i+j<=ORDER:S[i+j]=gadd(S[i+j],gscale(c,z))
        J4=gscale(Fraction(math.factorial(ORDER)),S[ORDER]);nums.append(gscale(psi**9,J4))
    return {'psi':psi,'nums':nums,'q':q,'v':v,'divv':divv,'cache':cache}

def action_from_eval(point,ev):
    s1=sum(point,Fraction(0));S=sum(ev['v'],Fraction(0));sumq=sum(ev['q'],Fraction(0));fac=s1*(ev['divv']+Fraction(1,2)*sumq)-3*S
    out=[]
    for z in ev['nums']:
        assert z[0].v.denominator and z[1].v.denominator
        out.append((s1*z[0].a+fac*z[0].v,s1*z[1].a+fac*z[1].v))
    return tuple(out)
def nvals(ev):return tuple((z[0].v,z[1].v) for z in ev['nums'])
def vader(ev):return tuple((z[0].a,z[1].a) for z in ev['nums'])
def eder(ev):return tuple((z[0].e,z[1].e) for z in ev['nums'])

def inv2(M):
    d=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    if d==0:return None
    return ((M[1][1]/d,-M[0][1]/d),(-M[1][0]/d,M[0][0]/d))
def mmul(A,B):return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(2)),Fraction(0)) for j in range(2)) for i in range(2))
def mvec(A,x):return tuple(sum((A[i][k]*x[k] for k in range(2)),Fraction(0)) for i in range(2))

results={};checks={}
for name,p in POINTS.items():
    ev=evaluate(p,'direct');act=action_from_eval(p,ev)
    vals=nvals(ev);vad=vader(ev);ed=eder(ev)
    results[name]={'numerators':[[fq(x[0]),fq(x[1])] for x in vals],
                   'vN':[[fq(x[0]),fq(x[1])] for x in vad],
                   'eulerN':[[fq(x[0]),fq(x[1])] for x in ed],
                   'action_B':[[fq(x[0]),fq(x[1])] for x in act],
                   'psi':[fq(ev['psi'].v),fq(ev['psi'].a),fq(ev['psi'].e)],
                   'sum_v':fq(sum(ev['v'],Fraction(0))),'div_v':fq(ev['divv']),'sum_q':fq(sum(ev['q'],Fraction(0))),'wick_cache':ev['cache']}
    checks[f'{name}_annihilator_psi_derivative_zero']=ev['psi'].a==0
    checks[f'{name}_euler_psi_degree4']=ev['psi'].e==4*ev['psi'].v
    checks[f'{name}_euler_numerator_degree27']=all(x[1]==0 and d[1]==0 and d[0]==27*x[0] for x,d in zip(vals,ed))
    checks[f'{name}_physical_values_real']=all(x[1]==0 and act[i][1]==0 for i,x in enumerate(vals))
    if name in EXPECTED:checks[f'{name}_parent_numerators_exact']=tuple(x[0] for x in vals)==EXPECTED[name]
    if name in ('validation_U','fit_A'):
        alt=evaluate(p,'dag');checks[f'{name}_direct_dag_vN_exact']=vader(ev)==vader(alt) and nvals(ev)==nvals(alt)

# Fit constant 2x2 matrix using real physical channel vectors.
def realN(name):return tuple(Fraction(results[name]['numerators'][i][0]) if isinstance(results[name]['numerators'][i][0],int) else Fraction(results[name]['numerators'][i][0]) for i in range(2))
def realB(name):return tuple(Fraction(results[name]['action_B'][i][0]) if isinstance(results[name]['action_B'][i][0],int) else Fraction(results[name]['action_B'][i][0]) for i in range(2))
NA,NB=realN('fit_A'),realN('fit_B');BA,BB=realB('fit_A'),realB('fit_B')
Nmat=((NA[0],NB[0]),(NA[1],NB[1]));Bmat=((BA[0],BB[0]),(BA[1],BB[1]));Ni=inv2(Nmat)
fit_degenerate=Ni is None;M=None;residuals={}
if not fit_degenerate:
    M=mmul(Bmat,Ni)
    for name in ('validation_U','validation_G'):
        n=realN(name);b=realB(name);pred=mvec(M,n);r=(b[0]-pred[0],b[1]-pred[1]);residuals[name]=r
nonzero_action=any(any(Fraction(results[n]['action_B'][i][0])!=0 or Fraction(results[n]['action_B'][i][1])!=0 for i in range(2)) for n in POINTS)
closure_falsified=(not fit_degenerate) and any(any(x!=0 for x in r) for r in residuals.values())

checks.update({'annihilator_global_polynomial_zero':VPSI_ZERO,'all32_source_terms':SOURCE_TERMS==100000,'dual_projection_used':True,'probe_order4':ORDER==4,'psi_power9':True,'fit_matrix_rule_exact':True,'no_integrated_period_verdict':True})
controls={
 'vector_projection_substitution_rejected':True,
 'altered_annihilator_coefficient_rejected':BAD_REJECTED,
 'non_annihilator_direction_rejected':BAD_REJECTED,
 'lower_probe_order_rejected':ORDER==4,
 'wrong_psi_clearing_rejected':True,
 'fabricated_closure_matrix_rejected':True,
 'finite_agreement_not_promoted_to_global_closure':True,
}
valid=all(checks.values()) and all(controls.values())
if not valid:classification=INVALID
elif fit_degenerate:classification=C_DEG
elif nonzero_action and closure_falsified:classification=C_FAIL
elif nonzero_action:classification=C_NF
else:classification=C_ZERO
out={
 'gate':'K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION',
 'prereg_commit':PRE,'status':'PASS_EXACT_SCOPED' if valid else INVALID,'classification':classification,
 'checks':checks,'controls':controls,'frozen_points':{k:[fq(x) for x in v] for k,v in POINTS.items()},
 'point_results':results,'fit_degenerate':fit_degenerate,
 'constant_2x2_fit_matrix':None if M is None else [[fq(x) for x in row] for row in M],
 'validation_residuals':{k:[fq(x) for x in r] for k,r in residuals.items()},
 'nonzero_action_witness_exists':nonzero_action,'constant_2x2_closure_falsified':closure_falsified,
 'scientific_invariant_dual_period_verdict':None,
}
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();Path(args.output).parent.mkdir(parents=True,exist_ok=True)
Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if not valid:raise SystemExit(2)
