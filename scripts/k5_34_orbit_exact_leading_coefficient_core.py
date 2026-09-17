#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT_CORE = ROOT / 'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
CRITIC_AUTH = ROOT / 'results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json'
MASK511_AUTH = ROOT / 'results/raw/k5_mask511_physical_numerator_action_exact_corner_witness_authoritative.json'
U_AUTH = ROOT / 'results/raw/k5_projective_normal_32orbit_exact_corner_order_authoritative.json'
PRE = 'd6b0e805101c8590eafac71398cc2b1466691752'
CRITIC_CLASS = 'CONFIRMED_EXACT_SCOPED'
N_DEG = 27
B_DEG = 31
ORDER = 4

spec = importlib.util.spec_from_file_location('k5_34_resolver_parent_core', PARENT_CORE)
core = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(core)

EDGES = tuple(core.EDGES)
ROWS = tuple(tuple(int(x) for x in r) for r in core.ROWS)
Q = [[Fraction(x) for x in row] for row in core.Q]
MATCH_COEFF = core.MATCH_COEFF
SOURCE_TERMS = core.SOURCE_TERMS
W1 = tuple(Fraction(x) for x in core.W1)
W2 = tuple(Fraction(x) for x in core.W2)
CYCLE = tuple(core.CYCLE)
WP1 = tuple(Fraction(x) for x in core.WP1)
WP2 = tuple(Fraction(x) for x in core.WP2)

assert len(EDGES) == 10
assert SOURCE_TERMS == 100000
assert len(MATCH_COEFF) == 945


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def qstr(q) -> str:
    q = Fraction(q)
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


class P:
    __slots__ = ('d',)
    def __init__(self, d=None):
        if d is None:
            self.d = {}
        elif isinstance(d, P):
            self.d = dict(d.d)
        elif isinstance(d, dict):
            self.d = {int(k): Fraction(v) for k, v in d.items() if Fraction(v)}
        else:
            q = Fraction(d)
            self.d = {} if not q else {0: q}

    @staticmethod
    def c(x):
        return x if isinstance(x, P) else P(x)

    @staticmethod
    def mon(deg, coeff=1):
        q = Fraction(coeff)
        return P({int(deg): q}) if q else P()

    def __add__(self, o):
        o = P.c(o); z = dict(self.d)
        for k, v in o.d.items():
            q = z.get(k, Fraction(0)) + v
            if q: z[k] = q
            elif k in z: del z[k]
        return P(z)
    __radd__ = __add__

    def __neg__(self): return P({k: -v for k, v in self.d.items()})
    def __sub__(self, o): return self + (-P.c(o))
    def __rsub__(self, o): return P.c(o) - self

    def __mul__(self, o):
        o = P.c(o)
        if not self.d or not o.d: return P()
        z = {}
        for i, a in self.d.items():
            for j, b in o.d.items():
                k = i + j
                z[k] = z.get(k, Fraction(0)) + a*b
        return P(z)
    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        z = P(1); b = self; k = n
        while k:
            if k & 1: z = z*b
            k >>= 1
            if k: b = b*b
        return z

    def iszero(self): return not self.d
    def coeff(self, k): return self.d.get(int(k), Fraction(0))
    def minord(self): return min(self.d) if self.d else None
    def maxdeg(self): return max(self.d) if self.d else None
    def vector(self, ceiling): return [self.coeff(i) for i in range(ceiling+1)]


class D:
    __slots__ = ('v','d')
    def __init__(self, v=0, d=0): self.v=P.c(v); self.d=P.c(d)
    @staticmethod
    def c(o): return o if isinstance(o, D) else D(o)
    def __add__(self, o): o=D.c(o); return D(self.v+o.v, self.d+o.d)
    __radd__ = __add__
    def __neg__(self): return D(-self.v, -self.d)
    def __sub__(self, o): return self + (-D.c(o))
    def __rsub__(self, o): return D.c(o) - self
    def __mul__(self, o): o=D.c(o); return D(self.v*o.v, self.d*o.v + self.v*o.d)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        if n == 0: return D(1)
        return D(self.v**n, P(n)*(self.v**(n-1))*self.d)


def det_d(A):
    n=len(A); z=D(0)
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        q=D(-1 if inv%2 else 1)
        for i,j in enumerate(p): q=q*A[i][j]
        z=z+q
    return z


def adj_d(A):
    n=len(A); out=[[D(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
            out[i][j]=(-1 if (i+j)%2 else 1)*det_d(M)
    return out


def mm_d(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),D(0)) for j in range(len(B[0]))] for i in range(len(A))]


def dot_d(r,M,s):
    return sum((M[i][j]*(r[i]*s[j]) for i in range(4) for j in range(4)),D(0))


def build_l_d(alpha):
    L=[[D(0) for _ in range(4)] for _ in range(4)]
    for a,r in zip(alpha,ROWS):
        for i in range(4):
            for j in range(4): L[i][j]=L[i][j]+a*(r[i]*r[j])
    return L


def s_mul_d(a,b):
    out=[D(0) for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER: out[i+j]=out[i+j]+x*y
    return out


def det_coeffs_d(L):
    out=[D(0) for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        ser=[D(1)]+[D(0) for _ in range(ORDER)]
        for i,j in enumerate(p):
            ser=s_mul_d(ser,[L[i][j],D(Q[i][j])]+[D(0) for _ in range(ORDER-1)])
        sgn=-1 if inv%2 else 1
        out=[x+sgn*y for x,y in zip(out,ser)]
    return out


def binom_frac(p,n):
    z=Fraction(1)
    for k in range(n): z=z*(p-k)/Fraction(k+1)
    return z


def det_factors_d(Ds,psi):
    memo={}
    def tail(m,j):
        key=(m,j)
        if key in memo:return memo[key]
        if m==0: z=D(1) if j==0 else D(0)
        else:
            z=D(0)
            for r in range(1,min(ORDER,j)+1): z=z+Ds[r]*tail(m-1,j-r)
        memo[key]=z; return z
    F=[D(1)]
    for j in range(1,ORDER+1):
        z=D(0)
        for m in range(1,j+1): z=z+binom_frac(Fraction(-3,2),m)*(psi**(j-m))*tail(m,j)
        F.append(z)
    return F


def matching_series_d(mt,C):
    ser=[D(1)]+[D(0) for _ in range(ORDER)]
    for ij in mt:
        nxt=[D(0) for _ in range(ORDER+1)]
        for k in range(ORDER+1):
            for n in range(k+1): nxt[k]=nxt[k]+ser[k-n]*C[(ij[0],ij[1],n)]
        ser=nxt
    return ser


def psi_tree_poly(alpha):
    z=P()
    for mon,c in core.PSI_POLY.items():
        q=P(c)
        assert len(mon)==10
        for e,power in enumerate(mon):
            if power: q=q*(alpha[e]**power)
        z=z+q
    return z


def route_a(mask:int, weights):
    Z={i for i in range(10) if (mask>>i)&1}
    aval=[P.mon(1,weights[i]) if i in Z else P(weights[i]) for i in range(10)]
    q,v,divv=core.ann_data(tuple(aval))
    s1=sum(aval,P()); S=sum(v,P()); sumq=sum(q,P())
    K=s1*(divv+Fraction(1,2)*sumq)-3*S
    aa=[D(aval[i],v[i]) for i in range(10)]
    L=build_l_d(aa); psi=det_d(L)
    tree=psi_tree_poly(aval)
    ADJ=adj_d(L)
    Ds=det_coeffs_d(L)
    F=det_factors_d(Ds,psi)
    AQ=[[sum((ADJ[i][k]*Q[k][j] for k in range(4)),D(0)) for j in range(4)] for i in range(4)]
    BN=[ADJ]
    for _ in range(1,ORDER+1):
        BN.append([[-x for x in row] for row in mm_d(AQ,BN[-1])])
    C={}
    for i in range(10):
        for j in range(i+1,10):
            for n in range(ORDER+1): C[(i,j,n)]=dot_d(ROWS[i],BN[n],ROWS[j])
    N=[[D(0),D(0)] for _ in range(2)]
    for mt,coeffs in MATCH_COEFF.items():
        ser=matching_series_d(mt,C)
        base=D(0)
        for j in range(ORDER+1): base=base+F[j]*ser[ORDER-j]
        base=math.factorial(ORDER)*base
        for ch in (0,1):
            cr,ci=coeffs[ch]
            if cr:N[ch][0]=N[ch][0]+cr*base
            if ci:N[ch][1]=N[ch][1]+ci*base
    checks={
        'psi_tree_exact': psi.v==tree,
        'annihilator_vpsi_zero': psi.d.iszero(),
        'det_D0_equals_psi': Ds[0].v==psi.v and Ds[0].d==psi.d,
        'physical_imaginary_N_cancel_exact': all(N[ch][1].v.iszero() and N[ch][1].d.iszero() for ch in (0,1)),
    }
    lanes=[]
    for ch in (0,1):
        n=N[ch][0]
        b=s1*n.d+K*n.v
        checks[f'ch{ch+1}_N_degree_le27']=(n.v.maxdeg() is None or n.v.maxdeg()<=N_DEG)
        checks[f'ch{ch+1}_B_degree_le31']=(b.maxdeg() is None or b.maxdeg()<=B_DEG)
        lanes.append({'N':n.v,'vN':n.d,'B':b})
    return {'checks':checks,'channels':lanes,'psi':psi.v,'K':K}


# Independent scalar-dual route for exact interpolation validation.
class SD:
    __slots__=('v','d')
    def __init__(self,v=0,d=0):self.v=Fraction(v);self.d=Fraction(d)
    @staticmethod
    def c(o):return o if isinstance(o,SD) else SD(o)
    def __add__(self,o):o=SD.c(o);return SD(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return SD(-self.v,-self.d)
    def __sub__(self,o):return self+(-SD.c(o))
    def __rsub__(self,o):return SD.c(o)-self
    def __mul__(self,o):o=SD.c(o);return SD(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return SD(1)
        return SD(self.v**n,Fraction(n)*(self.v**(n-1))*self.d)


def det_s(A):
    n=len(A);z=SD(0)
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));q=SD(-1 if inv%2 else 1)
        for i,j in enumerate(p):q=q*A[i][j]
        z=z+q
    return z


def adj_s(A):
    n=len(A);out=[[SD(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
            out[i][j]=(-1 if (i+j)%2 else 1)*det_s(M)
    return out


def mm_s(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),SD(0)) for j in range(len(B[0]))] for i in range(len(A))]
def dot_s(r,M,s):return sum((M[i][j]*(r[i]*s[j]) for i in range(4) for j in range(4)),SD(0))

def build_l_s(alpha):
    L=[[SD(0) for _ in range(4)] for _ in range(4)]
    for a,r in zip(alpha,ROWS):
        for i in range(4):
            for j in range(4):L[i][j]=L[i][j]+a*(r[i]*r[j])
    return L

def s_mul_s(a,b):
    out=[SD(0) for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER:out[i+j]=out[i+j]+x*y
    return out

def det_coeffs_s(L):
    out=[SD(0) for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));ser=[SD(1)]+[SD(0) for _ in range(ORDER)]
        for i,j in enumerate(p):ser=s_mul_s(ser,[L[i][j],SD(Q[i][j])]+[SD(0) for _ in range(ORDER-1)])
        sgn=-1 if inv%2 else 1;out=[x+sgn*y for x,y in zip(out,ser)]
    return out

def det_factors_s(Ds,psi):
    memo={}
    def tail(m,j):
        key=(m,j)
        if key in memo:return memo[key]
        if m==0:z=SD(1) if j==0 else SD(0)
        else:
            z=SD(0)
            for r in range(1,min(ORDER,j)+1):z=z+Ds[r]*tail(m-1,j-r)
        memo[key]=z;return z
    F=[SD(1)]
    for j in range(1,ORDER+1):
        z=SD(0)
        for m in range(1,j+1):z=z+binom_frac(Fraction(-3,2),m)*(psi**(j-m))*tail(m,j)
        F.append(z)
    return F

def matching_series_s(mt,C):
    ser=[SD(1)]+[SD(0) for _ in range(ORDER)]
    for ij in mt:
        nxt=[SD(0) for _ in range(ORDER+1)]
        for k in range(ORDER+1):
            for n in range(k+1):nxt[k]=nxt[k]+ser[k-n]*C[(ij[0],ij[1],n)]
        ser=nxt
    return ser


def scalar_eval(mask:int, weights, t:int):
    Z={i for i in range(10) if (mask>>i)&1}
    aval=[Fraction(weights[i])*(Fraction(t) if i in Z else 1) for i in range(10)]
    q,v,divv=core.ann_data(tuple(aval));s1=sum(aval,Fraction(0));S=sum(v,Fraction(0));sumq=sum(q,Fraction(0))
    K=s1*(divv+Fraction(1,2)*sumq)-3*S
    aa=[SD(aval[i],v[i]) for i in range(10)]
    L=build_l_s(aa);psi=det_s(L);ADJ=adj_s(L);Ds=det_coeffs_s(L);F=det_factors_s(Ds,psi)
    AQ=[[sum((ADJ[i][k]*Q[k][j] for k in range(4)),SD(0)) for j in range(4)] for i in range(4)]
    BN=[ADJ]
    for _ in range(1,ORDER+1):BN.append([[-x for x in row] for row in mm_s(AQ,BN[-1])])
    C={(i,j,n):dot_s(ROWS[i],BN[n],ROWS[j]) for i in range(10) for j in range(i+1,10) for n in range(ORDER+1)}
    N=[[SD(0),SD(0)] for _ in range(2)]
    for mt,coeffs in MATCH_COEFF.items():
        ser=matching_series_s(mt,C);base=SD(0)
        for j in range(ORDER+1):base=base+F[j]*ser[ORDER-j]
        base=math.factorial(ORDER)*base
        for ch in (0,1):
            cr,ci=coeffs[ch]
            if cr:N[ch][0]=N[ch][0]+cr*base
            if ci:N[ch][1]=N[ch][1]+ci*base
    out=[]
    for ch in (0,1):
        assert N[ch][1].v==0 and N[ch][1].d==0
        n=N[ch][0];b=s1*n.d+K*n.v
        out.append((n.v,b))
    return out


def interpolate_equispaced(values):
    vals=[Fraction(x) for x in values];diff=list(vals);newton=[]
    for k in range(len(vals)):
        newton.append(diff[0]/Fraction(math.factorial(k)))
        diff=[diff[i+1]-diff[i] for i in range(len(diff)-1)]
        if not diff and k+1<len(vals):raise AssertionError('difference table ended early')
    z=P();basis=P(1)
    for k,a in enumerate(newton):
        z=z+a*basis
        basis=basis*P({1:1,0:-k})
    return z


def route_b_interpolation(mask:int, weights):
    vals=[scalar_eval(mask,weights,t) for t in range(B_DEG+1)]
    out=[]
    for ch in (0,1):
        np=interpolate_equispaced([vals[t][ch][0] for t in range(N_DEG+1)])
        bp=interpolate_equispaced([vals[t][ch][1] for t in range(B_DEG+1)])
        out.append({'N':np,'B':bp})
    return out


def vector_strings(p:P,ceiling:int):return [qstr(x) for x in p.vector(ceiling)]
def vector_hash(p:P,ceiling:int):return hashlib.sha256(json.dumps(vector_strings(p,ceiling),separators=(',',':')).encode()).hexdigest()

def lane_serial(ch):
    return {
        'N_coefficients':vector_strings(ch['N'],N_DEG),
        'B_coefficients':vector_strings(ch['B'],B_DEG),
        'N_sha256':vector_hash(ch['N'],N_DEG),
        'B_sha256':vector_hash(ch['B'],B_DEG),
        'rN':ch['N'].minord(),
        'rB':ch['B'].minord(),
        'N_exact_zero':ch['N'].iszero(),
        'B_exact_zero':ch['B'].iszero(),
    }


def proper_orbits():
    reps=core.orbit_reps()
    return [(i,m,size,int(m).bit_count()) for i,(m,size) in enumerate(reps[1:-1])]


def class_representatives():
    out={}
    for idx,m,size,k in proper_orbits():
        key=(size,k)
        if key not in out or m<out[key][1]:out[key]=(idx,m)
    return out


def static_checks():
    critic=json.loads(CRITIC_AUTH.read_text(encoding='utf-8'))
    ua=json.loads(U_AUTH.read_text(encoding='utf-8'))
    m511=json.loads(MASK511_AUTH.read_text(encoding='utf-8'))
    po=proper_orbits()
    return {
        'parent_prereg_locked':PRE=='d6b0e805101c8590eafac71398cc2b1466691752',
        'critic_independent_transport_confirmed':critic.get('classification')==CRITIC_CLASS,
        'critic_q18_not_used':critic.get('q18_values_used') is False,
        'projective_normal_authority_exact':ua.get('classification')=='K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDERS_RESOLVED_SCOPED',
        'projective_normal_degree5':ua.get('degree_ceiling')==5,
        'mask511_parent_run_locked':m511.get('source',{}).get('run_id')==35226938480,
        'source_terms_100000':SOURCE_TERMS==100000,
        'retained_matchings_945':len(MATCH_COEFF)==945,
        'proper_orbits_32':len(po)==32,
        'proper_orbit_sizes_sum_1022':sum(size for _,_,size,_ in po)==1022,
        'degree_N_27':N_DEG==27,
        'degree_B_31':B_DEG==31,
        'weights_frozen':tuple(int(x) for x in W1)==(2,3,5,7,11,13,17,19,23,29) and tuple(int(x) for x in W2)==(31,37,41,43,47,53,59,61,67,71),
    }
