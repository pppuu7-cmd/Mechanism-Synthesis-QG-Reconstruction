import argparse,itertools,json,math,os
from fractions import Fraction as Q

N=tuple(range(5)); P5=tuple(itertools.permutations(N))
def invcount(p): return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def sgnperm(p): return -1 if invcount(p)%2 else 1
def sign(x,tol=0): return 1 if x>tol else (-1 if x<-tol else 0)

def det_exact(A):
    A=[[Q(x) for x in r] for r in A]; n=len(A); d=Q(1)
    for i in range(n):
        k=next((k for k in range(i,n) if A[k][i]),None)
        if k is None:return Q(0)
        if k!=i:A[i],A[k]=A[k],A[i];d=-d
        piv=A[i][i];d*=piv
        for j in range(i,n):A[i][j]/=piv
        for k in range(i+1,n):
            f=A[k][i]
            for j in range(i,n):A[k][j]-=f*A[i][j]
    return d

def detf(A):
    A=[list(map(float,r)) for r in A]; n=len(A); d=1.0
    for i in range(n):
        k=max(range(i,n),key=lambda z:abs(A[z][i]))
        if abs(A[k][i])<1e-12:return 0.0
        if k!=i:A[i],A[k]=A[k],A[i];d=-d
        piv=A[i][i];d*=piv
        for k in range(i+1,n):
            f=A[k][i]/piv
            for j in range(i+1,n):A[k][j]-=f*A[i][j]
    return d

def hyper_q(u):
    ss=sum(x*x for x in u); d=1-ss
    return ((1+ss)/d,)+tuple(2*x/d for x in u)
def delta_exact(F,s): return det_exact([[1]*5]+[[Q(s[a])*F[a][m] for a in N] for m in range(4)])
def delta(F,s): return detf([[1]*5]+[[s[a]*F[a][m] for a in N] for m in range(4)])
def relabel(F,s,p):
    FF=[None]*5; ss=[None]*5
    for a in N: FF[p[a]]=F[a]; ss[p[a]]=s[a]
    return FF,ss

def boostx(F,c,s):
    return [(c*f[0]+s*f[1],s*f[0]+c*f[1],f[2],f[3]) for f in F]
def parity(F): return [(f[0],-f[1],f[2],f[3]) for f in F]

def lane_a():
    us=[(Q(0),Q(0),Q(0)),(Q(1,3),0,0),(0,Q(1,4),0),(0,0,Q(1,5)),(Q(1,6),Q(1,7),Q(1,8))]
    F=[hyper_q(u) for u in us]; s=(-1,-1,1,-1,1); D=delta_exact(F,s)
    pchecks=0
    for p in P5:
        FF,ss=relabel(F,s,p)
        if delta_exact(FF,ss)!=sgnperm(p)*D: return {'iteration':'Iter076M','lane':'A','pass':False,'failure':'S5'}
        pchecks+=1
    rev=delta_exact(F,tuple(-x for x in s))==D
    B=boostx(F,Q(5,3),Q(4,3)); gauge=delta_exact(B,s)==D
    roots=True
    for r in N:
        others=[a for a in N if a!=r]
        M=[[Q(s[a])*F[a][m]-Q(s[r])*F[r][m] for a in others] for m in range(4)]
        if ((-1)**r)*det_exact(M)!=D: roots=False
    ok=D!=0 and pchecks==120 and rev and gauge and roots
    return {'iteration':'Iter076M','lane':'A','pass':ok,'delta':str(D),'S5_checks':pchecks,
            'global_sigma_reversal_invariant':rev,'proper_lorentz_gauge_invariant':gauge,'five_root_cofactor_identity':roots}

def confs():
    dirs=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    F1=[(math.sqrt(2),)+tuple(x/math.sqrt(3) for x in v) for v in dirs]+[(1,0,0,0)]
    s1=(1,1,1,1,-1); w1=(1,1,1,1,4*math.sqrt(2))
    us=[(.15,.02,.01),(-.12,.11,.03),(.04,-.16,.09),(.08,.07,-.14)]
    def hf(u):
        ss=sum(x*x for x in u); d=1-ss
        return ((1+ss)/d,)+tuple(2*x/d for x in u)
    F2=[hf(u) for u in us]; S=[sum(f[m] for f in F2) for m in range(4)]
    n=math.sqrt(S[0]*S[0]-sum(x*x for x in S[1:])); F2.append(tuple(x/n for x in S))
    return [('sym',F1,s1,w1),('generic',F2,s1,(1,1,1,1,n))]

def lane_b():
    details={}; allok=True
    for name,F,s,w in confs():
        D=delta(F,s); closure=max(abs(sum(w[a]*s[a]*F[a][m] for a in N)) for m in range(4))
        rel=all(sign(delta(*relabel(F,s,p)))==sgnperm(p)*sign(D) for p in P5)
        Bg=boostx(F,1.25,.75); gauge=sign(delta(Bg,s))==sign(D) # c^2-s^2=1
        par=sign(delta(parity(F),s))==-sign(D)
        ok=abs(D)>1e-9 and closure<1e-10 and rel and gauge and par
        allok &= ok; details[name]={'delta':D,'closure_residual':closure,'S5_120':rel,'boost_invariant':gauge,'parity_flips':par}
    return {'iteration':'Iter076M','lane':'B','pass':allok,'configurations':details}

def lane_c():
    allok=True; details={}
    for name,F,s,w in confs():
        E=[]
        for a in N:
            oth=[j for j in N if j!=a]
            E.append(detf([[F[j][m] for j in oth] for m in range(4)]))
        Ep=[]
        PF=parity(F)
        for a in N:
            oth=[j for j in N if j!=a]
            Ep.append(detf([[PF[j][m] for j in oth] for m in range(4)]))
        individual_odd=all(sign(Ep[a])==-sign(E[a]) for a in N)
        beta_ok=True; beta_even=True
        for a in N:
            for b in range(a+1,5):
                cde=[j for j in N if j not in (a,b)]
                A=[b]+cde; B=[a]+cde
                x=detf([[F[j][m] for j in A] for m in range(4)])*detf([[F[j][m] for j in B] for m in range(4)])
                xp=detf([[PF[j][m] for j in A] for m in range(4)])*detf([[PF[j][m] for j in B] for m in range(4)])
                beta_ok &= sign(x)==-s[a]*s[b]
                beta_even &= sign(xp)==sign(x)
        omega_odd=sign(delta(PF,s))==-sign(delta(F,s))
        ok=individual_odd and beta_ok and beta_even and omega_odd
        allok &= ok; details[name]={'individual_E_orientation_odd':individual_odd,'beta_pair_orientation_even':beta_even,
                                    'beta_equals_minus_epsilon_a_epsilon_b':beta_ok,'Omega_orientation_odd':omega_odd}
    return {'iteration':'Iter076M','lane':'C','pass':allok,'configurations':details,
            'proper_vertex_projector_imported':False}

def lane_d():
    name,F,s,w=confs()[1]; FD=list(F); FD[4]=FD[3]; sd=list(s); sd[4]=sd[3]
    deg=abs(delta(FD,sd))<1e-12; omega=None if deg else sign(delta(FD,sd))
    weighted=sign(delta(F,s)); raw=sign(delta(F,(1,1,1,1,1)))
    changes=(weighted!=raw)
    if not changes:
        # deterministic exact control where sigma weighting is known to alter the affine determinant sign.
        Fe=[tuple(float(x) for x in hyper_q(u)) for u in [(Q(0),Q(0),Q(0)),(Q(1,3),0,0),(0,Q(1,4),0),(0,0,Q(1,5)),(Q(1,6),Q(1,7),Q(1,8))]]
        se=(-1,-1,1,-1,1); changes=sign(delta(Fe,se))!=sign(delta(Fe,(1,1,1,1,1)))
    ok=deg and omega is None and changes
    return {'iteration':'Iter076M','lane':'D','pass':ok,'degenerate_delta_zero':deg,'omega_on_degenerate':omega,
            'sigma_weights_can_change_selector':changes,'raw_label_order_not_physical':True,'regularization_or_fit_used':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}
def dump(o,p): os.makedirs(os.path.dirname(p) or '.',exist_ok=True); open(p,'w').write(json.dumps(o,indent=2,sort_keys=True))
def aggregate(root):
    got={}
    for b,_,fs in os.walk(root):
        for f in fs:
            if f.endswith('.json'):
                try:o=json.load(open(os.path.join(b,f)))
                except:continue
                if o.get('iteration')=='Iter076M' and o.get('lane') in LANES:got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    if valid: c='ITER076M_SOURCE_GROUP_AND_CAUSAL_DATA_DEFINE_NONDEGENERATE_GLOBAL_ORIENTATION_PSEUDOSCALAR_REVIEW_P3_SCOPED'
    elif got.get('C') and not got['C'].get('pass'): c='ITER076M_PROPER_VERTEX_ORIENTATION_COMPATIBILITY_FAIL_SCOPED'
    else: c='ITER076M_CANDIDATE_ORIENTATION_PSEUDOSCALAR_REJECTED_SCOPED'
    return {'iteration':'Iter076M','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'classification':c,
            'claim_lock':'Candidate exists as a function of exact source variables; physical P3 still requires amplitude-selection provenance.'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir):raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir);dump(o,a.output);print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')):raise SystemExit(2)
if __name__=='__main__':main()
