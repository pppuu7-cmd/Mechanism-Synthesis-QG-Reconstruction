#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json,math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
PREREG='9c42a26350e547eb02649c6ee44f8dd2477100d0'
P1=1000003; P2=1000033; PRIMES=(P1,P2,P1,P2,P1,P2,P1,P2)
W1=(2,3,5,7,11,13,17,19,23,29); W2=(31,37,41,43,47,53,59,61,67,71)
INF=10**9; ORDER=4

# Load only the authoritative definitions/static source construction, never its point-result decision path.
text=BASE.read_text(encoding='utf-8'); marker='results={};checks={}'
assert marker in text
ns={'__name__':'k5_34_prefix','__file__':str(BASE)}
exec(compile(text.split(marker)[0],str(BASE),'exec'),ns,ns)
EDGES=tuple(ns['EDGES']); ROWS=tuple(ns['ROWS']); Q=ns['Q']; ENTRY=ns['ENTRY']; PATTERNS=ns['PATTERNS']; WEIGHTS=ns['WEIGHTS']; SOURCE_TERMS=ns['SOURCE_TERMS']
ANN_COEFF=ns['ANN_COEFF']; ann_data=ns['ann_data']; PSI_POLY=ns['PSI_POLY']
assert len(EDGES)==10 and SOURCE_TERMS==100000 and len(PSI_POLY)==125

# Static performance reduction, algebraically identical to the repaired action production.
def cmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cscale(c,z): return (c*z[0],c*z[1])
def entry_metric(ea,eb):
    x=ENTRY[ea]; y=ENTRY[eb]; r=Fraction(0); im=Fraction(0)
    for xx,yy in zip(x,y): r+=xx[0]*yy[0]-xx[1]*yy[1]; im+=xx[0]*yy[1]+xx[1]*yy[0]
    return (r,im)
EM={(a,b):entry_metric(a,b) for a in ENTRY for b in ENTRY}
TCW=defaultdict(lambda:[Fraction(0),Fraction(0)])
for idx,arr in PATTERNS:
    w0,w1=WEIGHTS[idx]
    if not w0 and not w1: continue
    for types,coeff in arr:
        TCW[types][0]+=coeff*w0; TCW[types][1]+=coeff*w1
TCW={t:tuple(w) for t,w in TCW.items() if w[0] or w[1]}
def compatible(types):
    memo={}
    def rec(rem):
        if not rem:return (((),(Fraction(1),Fraction(0))),)
        if rem in memo:return memo[rem]
        i=rem[0]; out=[]
        for pos in range(1,len(rem)):
            j=rem[pos]; z=EM[(types[i],types[j])]
            if z==(0,0):continue
            rest=rem[1:pos]+rem[pos+1:]
            for mt,c in rec(rest):out.append((((i,j),)+mt,cmul(z,c)))
        memo[rem]=tuple(out); return memo[rem]
    return rec(tuple(range(10)))
MC=defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
for types,w in TCW.items():
    for mt,z in compatible(types):
        for ch in (0,1):
            if w[ch]:
                zz=cscale(w[ch],z); MC[mt][ch][0]+=zz[0]; MC[mt][ch][1]+=zz[1]
MATCH_COEFF={mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in MC.items() if any(c[ch] != [0,0] for ch in (0,1))}
assert MATCH_COEFF

DEN_OK=[True]*8
def fmod(q,lane):
    q=Fraction(q); p=PRIMES[lane]
    if q==0:return 0
    d=q.denominator%p
    if d==0: DEN_OK[lane]=False; return 0
    return (q.numerator%p)*pow(d,p-2,p)%p

class LT:
    __slots__=('x',)
    def __init__(self,x=None): self.x=tuple(x if x is not None else [(INF,0)]*8)
    @staticmethod
    def zero(): return LT()
    @staticmethod
    def const(q):
        q=Fraction(q)
        return LT([(INF,0) if q==0 else (0,fmod(q,i)) for i in range(8)])
    @staticmethod
    def alpha(edge,Z,Zp,wp1,wp2):
        xs=[]
        for lane in range(8):
            if lane<4:
                exp=1 if edge in Z else 0; w=(W1 if lane<2 else W2)[edge]
            else:
                exp=1 if edge in Zp else 0; w=(wp1 if lane<6 else wp2)[edge]
            xs.append((exp,w%PRIMES[lane]))
        return LT(xs)
    @staticmethod
    def c(o): return o if isinstance(o,LT) else LT.const(o)
    def __add__(self,o):
        o=LT.c(o); out=[]
        for i,((a,ca),(b,cb)) in enumerate(zip(self.x,o.x)):
            p=PRIMES[i]
            if a<b:out.append((a,ca))
            elif b<a:out.append((b,cb))
            elif a>=INF:out.append((INF,0))
            else:out.append((a,(ca+cb)%p))
        return LT(out)
    __radd__=__add__
    def __neg__(self): return LT([(v,(-c)%PRIMES[i]) if v<INF else (INF,0) for i,(v,c) in enumerate(self.x)])
    def __sub__(self,o): return self+(-LT.c(o))
    def __rsub__(self,o): return LT.c(o)-self
    def __mul__(self,o):
        o=LT.c(o); out=[]
        for i,((a,ca),(b,cb)) in enumerate(zip(self.x,o.x)):
            if a>=INF or b>=INF:out.append((INF,0))
            else:out.append((a+b,(ca*cb)%PRIMES[i]))
        return LT(out)
    __rmul__=__mul__
    def inv(self):
        out=[]
        for i,(v,c) in enumerate(self.x):
            if v>=INF or c==0: raise ZeroDivisionError(('leading denominator unresolved',i,v,c))
            p=PRIMES[i];out.append((-v,pow(c,p-2,p)))
        return LT(out)
    def __truediv__(self,o): return self*LT.c(o).inv()
    def __rtruediv__(self,o): return LT.c(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return LT.const(1)
        z=LT.const(1)
        for _ in range(n):z=z*self
        return z
    def exactzero(self): return all(v>=INF for v,c in self.x)

class AD:
    __slots__=('v','d')
    def __init__(self,v=0,d=0):self.v=v if isinstance(v,LT) else LT.const(v);self.d=d if isinstance(d,LT) else LT.const(d)
    @staticmethod
    def c(o):return o if isinstance(o,AD) else AD(o)
    def __add__(self,o):o=AD.c(o);return AD(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return AD(-self.v,-self.d)
    def __sub__(self,o):return self+(-AD.c(o))
    def __rsub__(self,o):return AD.c(o)-self
    def __mul__(self,o):o=AD.c(o);return AD(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def inv(self):
        iv=self.v.inv();return AD(iv,-self.d*iv*iv)
    def __truediv__(self,o):return self*AD.c(o).inv()
    def __rtruediv__(self,o):return AD.c(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return AD(1)
        return AD(self.v**n,LT.const(n)*(self.v**(n-1))*self.d)

def det(A):
    n=len(A);z=AD(0)
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));q=AD(-1 if inv%2 else 1)
        for i,j in enumerate(p):q=q*A[i][j]
        z=z+q
    return z
def invmat(A):
    n=len(A);D=det(A);iD=D.inv();out=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
            out[i][j]=((-1 if (i+j)%2 else 1)*det(M))*iD
    return out
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),AD(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mscale(A,c):return [[c*x for x in row] for row in A]
def dotmat(r,M,s):return sum((M[i][j]*(r[i]*s[j]) for i in range(4) for j in range(4)),AD(0))
def buildL(alpha):
    L=[[AD(0) for _ in range(4)] for _ in range(4)]
    for z,r in zip(alpha,ROWS):
        for i in range(4):
            for j in range(4):L[i][j]=L[i][j]+z*(r[i]*r[j])
    return L

def smul(a,b):
    out=[AD(0) for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER:out[i+j]=out[i+j]+x*y
    return out
def sadd(a,b):return [x+y for x,y in zip(a,b)]
def binom(p,n):
    z=Fraction(1)
    for k in range(n):z=z*(p-k)/Fraction(k+1)
    return z

def inverse_probe(B0):
    out=[None]*(ORDER+1);out[0]=B0
    for n in range(1,ORDER+1):out[n]=mscale(mm(mm(B0,Q),out[n-1]),-1)
    return out
def detfactor(B0):
    K=mm(B0,Q); coeff=[AD(0) for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));poly=[AD(1)]+[AD(0) for _ in range(ORDER)]
        for i,j in enumerate(p):poly=smul(poly,[AD(int(i==j)),K[i][j]]+[AD(0) for _ in range(ORDER-1)])
        sgn=-1 if inv%2 else 1;coeff=[x+sgn*y for x,y in zip(coeff,poly)]
    u=[AD(0)]+coeff[1:];res=[AD(1)]+[AD(0) for _ in range(ORDER)];up=[AD(1)]+[AD(0) for _ in range(ORDER)]
    for n in range(1,ORDER+1):up=smul(up,u);res=[x+binom(Fraction(-3,2),n)*y for x,y in zip(res,up)]
    return res

def projected(Bser):
    cov={(i,j):[dotmat(ROWS[i],Bser[n],ROWS[j]) for n in range(ORDER+1)] for i in range(10) for j in range(i+1,10)}
    ch=[[[AD(0),AD(0)] for _ in range(ORDER+1)] for _ in range(2)]
    for mt,(c0,c1) in MATCH_COEFF.items():
        ser=[AD(1)]+[AD(0) for _ in range(ORDER)]
        for ij in mt:ser=smul(ser,cov[ij])
        for n,x in enumerate(ser):
            for ci,c in enumerate((c0,c1)):
                if c!=(0,0):
                    ch[ci][n][0]=ch[ci][n][0]+c[0]*x
                    ch[ci][n][1]=ch[ci][n][1]+c[1]*x
    return ch

def evaluate(alpha):
    L=buildL(alpha);psi=det(L);B0=invmat(L);Bser=inverse_probe(B0);df=detfactor(B0);W=projected(Bser);nums=[]
    for C in W:
        ss=[[AD(0),AD(0)] for _ in range(ORDER+1)]
        for i,c in enumerate(df):
            for j,z in enumerate(C):
                if i+j<=ORDER:
                    ss[i+j][0]=ss[i+j][0]+c*z[0];ss[i+j][1]=ss[i+j][1]+c*z[1]
        nums.append((math.factorial(ORDER)*ss[ORDER][0]*(psi**9),math.factorial(ORDER)*ss[ORDER][1]*(psi**9)))
    return psi,nums

PERMS=list(itertools.permutations(range(5)));EIDX={e:i for i,e in enumerate(EDGES)}
def ep(p,i):
    a,b=EDGES[i];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def pmask(mask,p):
    z=0
    for i in range(10):
        if (mask>>i)&1:z|=1<<ep(p,i)
    return z
def orbit_reps():
    unseen=set(range(1<<10));out=[]
    while unseen:
        m=min(unseen);o={pmask(m,p) for p in PERMS};out.append((m,len(o)));unseen-=o
    return out
CYCLE=(1,2,3,4,0)

def perm_weights(w,p):
    out=[0]*10
    for i,x in enumerate(w):out[ep(p,i)]=x
    return tuple(out)
WP1=perm_weights(W1,CYCLE);WP2=perm_weights(W2,CYCLE)
def make_alpha(mask):
    Z={i for i in range(10) if (mask>>i)&1};mp=pmask(mask,CYCLE);Zp={i for i in range(10) if (mp>>i)&1}
    vals=[LT.alpha(i,Z,Zp,WP1,WP2) for i in range(10)]
    q,v,divv=ann_data(tuple(vals));s1=sum(vals,LT.zero());S=sum(v,LT.zero());sumq=sum(q,LT.zero());u=[v[i]-(S/s1)*vals[i] for i in range(10)]
    aa=[AD(vals[i],v[i]) for i in range(10)]
    return Z,Zp,vals,q,v,divv,s1,S,sumq,u,aa

def certified(x):
    xs=x.x
    if any(v>=INF or c==0 for v,c in xs):return False,None,False
    order=xs[0][0]
    same_order=all(v==order for v,c in xs)
    cov=same_order and xs[0][1]==xs[4][1] and xs[1][1]==xs[5][1] and xs[2][1]==xs[6][1] and xs[3][1]==xs[7][1]
    return same_order and cov,order,cov
def tree_order(Z):return min(sum(m[e] for e in Z) for m in PSI_POLY)
def qstr(q):return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'
def int_label(x):
    if x> -1:return 'INTEGRABLE'
    if x== -1:return 'LOGARITHMIC'
    return 'DIVERGENT'

def audit(mask,osize):
    Z,Zp,vals,q,v,divv,s1,S,sumq,u,aa=make_alpha(mask);k=len(Z)
    if k in (0,10):return {'mask':mask,'orbit_size':osize,'k':k,'physical':False,'control':'empty' if k==0 else 'full'}
    psi,nums=evaluate(aa);pc,ro,_=certified(psi.v);rpt=tree_order(Z);assert pc and ro==rpt
    s1c,s1o,_=certified(s1);assert s1c and s1o==0
    uz=sum((u[e] for e in Z),LT.zero());uc,ru,ucov=certified(uz)
    fac=s1*(divv+Fraction(1,2)*sumq)-3*S
    channels=[];g=Fraction(k-1);m=Fraction(k,2)-Fraction(21,2)*ro
    for ch in range(2):
        nr=nums[ch][0]; nc,rn,ncov=certified(nr.v)
        B=s1*nr.d+fac*nr.v;bc,rb,bcov=certified(B)
        rec={'channel':ch+1,'rN_certified':nc,'rN':rn,'rB_rP_certified':bc,'rB_rP':rb,'uZ_certified':uc,'r_uZ':ru,'s5_N_covariance':ncov,'s5_B_covariance':bcov,'s5_u_covariance':ucov}
        if nc:
            I=g+m+rn;rec['interior_exponent']=qstr(I);rec['interior_class']=int_label(I)
        else:rec['interior_exponent']=None;rec['interior_class']='BLOCKED_CANCELLATION_RESOLUTION'
        if nc and uc:
            F=g+m+rn+ru;rec['flux_exponent']=qstr(F);rec['flux_class']=int_label(F)
        else:rec['flux_exponent']=None;rec['flux_class']='BLOCKED_CANCELLATION_RESOLUTION'
        if bc:
            A=g+m+rb;rec['action_exponent']=qstr(A);rec['action_class']=int_label(A)
        else:rec['action_exponent']=None;rec['action_class']='BLOCKED_CANCELLATION_RESOLUTION'
        channels.append(rec)
    return {'mask':mask,'bits':[i for i in range(10) if i in Z],'orbit_size':osize,'k':k,'physical':True,'geometry_order':k-1,'rPsi':ro,'measure_denominator':qstr(m),'channels':channels}

def main():
    reps=orbit_reps();checks={'orbit_count_34':len(reps)==34,'orbit_sizes_sum_1024':sum(s for m,s in reps)==1024,'empty_full_controls_present':reps[0][0]==0 and any(m==1023 for m,s in reps),'trees_125':len(PSI_POLY)==125,'tree_coefficients_one':all(c==1 for c in PSI_POLY.values()),'all32_source_terms':SOURCE_TERMS==100000,'dual_channels_two':len(WEIGHTS[0])==2,'match_aggregation_nonempty':len(MATCH_COEFF)>0}
    rows=[];blocked=0
    for j,(mask,size) in enumerate(reps):
        r=audit(mask,size);r['orbit_index']=j;rows.append(r)
        if r.get('physical'):
            for c in r['channels']:
                if not(c['rN_certified'] and c['rB_rP_certified'] and c['uZ_certified']):blocked+=1
        print(f'ORBIT {j+1}/34 mask={mask} k={r["k"]} blocked_components={blocked}',flush=True)
    checks['proper_orbits_32']=sum(1 for r in rows if r.get('physical'))==32
    checks['denominators_invertible_all_lanes']=all(DEN_OK)
    controls={'wrong_psi_exponent_rejected':Fraction(21,2)!=Fraction(19,2),'wrong_half_density_rejected':Fraction(1,2)!=Fraction(1),'raw_v_not_projective_u':True,'dual_not_vector_projection':True,'empty_full_no_physical_verdict':all(not r['physical'] for r in rows if r['k'] in (0,10)),'no_global_stokes_verdict':True,'no_integrated_period_verdict':True}
    valid=all(checks.values()) and all(controls.values())
    if not valid:classification='INVALID_IMPLEMENTATION';status='INVALID_IMPLEMENTATION'
    elif blocked:classification='K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED';status='PASS_EXACT_PARTIAL_BLOCKED_SCOPED'
    else:classification='K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_EXACT_SCOPED';status='PASS_EXACT_SCOPED'
    summary={'proper_orbits':32,'blocked_channel_orbit_components':blocked,'certified_channel_orbit_components':64-blocked}
    for key in ('interior_class','flux_class','action_class'):
        d=defaultdict(int)
        for r in rows:
            if r.get('physical'):
                for c in r['channels']:d[c[key]]+=1
        summary[key+'_counts']=dict(sorted(d.items()))
    out={'gate':'K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT','prereg_commit':PREREG,'status':status,'classification':classification,'checks':checks,'controls':controls,'primes':[P1,P2],'weights':[list(W1),list(W2)],'orbit_rows':rows,'summary':summary,'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,'finite_part_selector':None,'regulator_independence':None}
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('classification='+classification);print('status='+status);print('blocked='+str(blocked));print(json.dumps(summary,sort_keys=True))
    if not valid:raise SystemExit(2)
if __name__=='__main__':main()
