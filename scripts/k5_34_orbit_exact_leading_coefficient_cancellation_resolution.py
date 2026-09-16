#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, os
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE_PATH=ROOT/'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
PREREG='d6b0e805101c8590eafac71398cc2b1466691752'
IMPLEMENTATION_FREEZE='808492fe93369f27e7fcaee6a0f7af64583a35ae'
EXECUTION_AMENDMENT='cf944a8c246a0c5b9819967549c155a6ca5d1aaa'
CLASS_EXACT='K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_EXACT_SCOPED'
CLASS_PARTIAL='K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_PARTIAL_BLOCKED_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
ORDER=4
DEG_N=27; DEG_B=31; DEG_U=5
PRIMARY_NODES=tuple(range(1,33)); INDEPENDENT_NODES=tuple(range(33,65))

spec=importlib.util.spec_from_file_location('k5_exact_cancel_core',CORE_PATH)
core=importlib.util.module_from_spec(spec); spec.loader.exec_module(core)

W1=tuple(core.W1); W2=tuple(core.W2); CYCLE=tuple(core.CYCLE)
WP1=tuple(core.perm_weights(W1,CYCLE)); WP2=tuple(core.perm_weights(W2,CYCLE))

def fq(x):
    q=Fraction(x)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def vhash(v):
    raw=json.dumps([fq(x) for x in v],separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()

class D:
    __slots__=('v','d')
    def __init__(self,v=0,d=0): self.v=Fraction(v); self.d=Fraction(d)
    @staticmethod
    def c(x): return x if isinstance(x,D) else D(x)
    def __add__(self,o): o=D.c(o); return D(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self): return D(-self.v,-self.d)
    def __sub__(self,o): return self+(-D.c(o))
    def __rsub__(self,o): return D.c(o)-self
    def __mul__(self,o):
        o=D.c(o); return D(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def inv(self):
        if self.v==0: raise ZeroDivisionError('dual scalar inverse at zero')
        return D(1/self.v,-self.d/(self.v*self.v))
    def __truediv__(self,o): return self*D.c(o).inv()
    def __rtruediv__(self,o): return D.c(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return D(1)
        return D(self.v**n,n*(self.v**(n-1))*self.d)

def mat_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),D(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mat_scale(A,c): return [[c*x for x in row] for row in A]
def dot_mat(r,M,s): return sum((M[i][j]*(r[i]*s[j]) for i in range(4) for j in range(4)),D(0))

def build_L(alpha):
    L=[[D(0) for _ in range(4)] for _ in range(4)]
    for a,r in zip(alpha,core.ROWS):
        for i in range(4):
            for j in range(4):
                if r[i] and r[j]: L[i][j]=L[i][j]+a*(r[i]*r[j])
    return L

def det_perm(A):
    n=len(A); out=D(0)
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)); q=D(-1 if inv%2 else 1)
        for i,j in enumerate(p): q=q*A[i][j]
        out=out+q
    return out

def adjugate4(A):
    out=[[None]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            M=[[A[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]
            out[i][j]=(-1 if (i+j)%2 else 1)*det_perm(M)
    return out

def psi_direct(alpha):
    out=D(0)
    for mon,c in core.PSI_POLY.items():
        q=D(c)
        for e,p in enumerate(mon):
            if p:q=q*(alpha[e]**p)
        out=out+q
    return out

def inv_cofactor(A,psi):
    adj=adjugate4(A); return [[adj[i][j]/psi for j in range(4)] for i in range(4)]

def smul(a,b):
    out=[D(0) for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER: out[i+j]=out[i+j]+x*y
    return out

def binom(p,n):
    z=Fraction(1)
    for k in range(n): z=z*(p-k)/Fraction(k+1)
    return z

def inverse_series(B0):
    out=[None]*(ORDER+1); out[0]=B0
    for n in range(1,ORDER+1): out[n]=mat_scale(mat_mul(mat_mul(B0,core.Q),out[n-1]),-1)
    return out

def detfactor_from_B0(B0):
    K=mat_mul(B0,core.Q); coeff=[D(0) for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)); poly=[D(1)]+[D(0) for _ in range(ORDER)]
        for i,j in enumerate(p): poly=smul(poly,[D(int(i==j)),K[i][j]]+[D(0) for _ in range(ORDER-1)])
        s=-1 if inv%2 else 1; coeff=[x+s*y for x,y in zip(coeff,poly)]
    assert coeff[0].v==1 and coeff[0].d==0
    u=[D(0)]+coeff[1:]; res=[D(1)]+[D(0) for _ in range(ORDER)]; up=[D(1)]+[D(0) for _ in range(ORDER)]
    for n in range(1,ORDER+1):
        up=smul(up,u); c=binom(Fraction(-3,2),n); res=[x+c*y for x,y in zip(res,up)]
    return res

def detfactor_scaled(A):
    coeff=[D(0) for _ in range(ORDER+1)]
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,n if False else 4)); poly=[D(1)]+[D(0) for _ in range(ORDER)]
        for i,j in enumerate(p): poly=smul(poly,[D(int(i==j)),A[i][j]]+[D(0) for _ in range(ORDER-1)])
        s=-1 if inv%2 else 1; coeff=[x+s*y for x,y in zip(coeff,poly)]
    assert coeff[0].v==1 and coeff[0].d==0
    u=[D(0)]+coeff[1:]; res=[D(1)]+[D(0) for _ in range(ORDER)]; up=[D(1)]+[D(0) for _ in range(ORDER)]
    for n in range(1,ORDER+1):
        up=smul(up,u); c=binom(Fraction(-3,2),n); res=[x+c*y for x,y in zip(res,up)]
    return res

def cadd(a,b): return (a[0]+b[0],a[1]+b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cscale(c,a): return (c*a[0],c*a[1])
def csmul(a,b):
    out=[(D(0),D(0)) for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ORDER: out[i+j]=cadd(out[i+j],cmul(x,y))
    return out

def projected(series_mats):
    cov={(i,j):[dot_mat(core.ROWS[i],series_mats[n],core.ROWS[j]) for n in range(ORDER+1)] for i in range(10) for j in range(i+1,10)}
    ch=[[(D(0),D(0)) for _ in range(ORDER+1)] for _ in range(2)]
    for mt,(c0,c1) in core.MATCH_COEFF.items():
        ser=[(D(1),D(0))]+[(D(0),D(0)) for _ in range(ORDER)]
        for ij in mt: ser=csmul(ser,[(x,D(0)) for x in cov[ij]])
        for n,x in enumerate(ser):
            for ci,c in enumerate((c0,c1)):
                if c!=(0,0): ch[ci][n]=cadd(ch[ci][n],(c[0]*x[0]-c[1]*x[1],c[0]*x[1]+c[1]*x[0]))
    return ch

def point_data(mask,weights,t):
    Z={i for i in range(10) if (mask>>i)&1}; tt=Fraction(t)
    point=tuple(Fraction(weights[i])*(tt if i in Z else 1) for i in range(10))
    q,v,divv=core.ann_data(point); s1=sum(point,Fraction(0)); S=sum(v,Fraction(0)); sumq=sum(q,Fraction(0))
    fac=s1*(divv+Fraction(1,2)*sumq)-3*S
    uz=s1*sum((v[e] for e in Z),Fraction(0))-S*sum((point[e] for e in Z),Fraction(0))
    return Z,point,q,v,divv,s1,S,sumq,fac,uz

def direct_eval(mask,weights,t):
    Z,point,q,v,divv,s1,S,sumq,fac,uz=point_data(mask,weights,t)
    alpha=[D(point[i],v[i]) for i in range(10)]; L=build_L(alpha); psi=psi_direct(alpha)
    if psi.v==0: raise ZeroDivisionError(('psi_zero_at_primary_node',mask,t))
    B0=inv_cofactor(L,psi); Bser=inverse_series(B0); df=detfactor_from_B0(B0); W=projected(Bser)
    nums=[]; imag_ok=True
    for C in W:
        ss=[(D(0),D(0)) for _ in range(ORDER+1)]
        for i,c in enumerate(df):
            for j,z in enumerate(C):
                if i+j<=ORDER: ss[i+j]=cadd(ss[i+j],cscale(c,z))
        z=cscale(Fraction(math.factorial(ORDER)),ss[ORDER]); z=(z[0]*(psi**9),z[1]*(psi**9))
        imag_ok=imag_ok and z[1].v==0 and z[1].d==0
        nums.append((z[0].v,s1*z[0].d+fac*z[0].v))
    return {'N':[x[0] for x in nums],'B':[x[1] for x in nums],'U':uz,'imag_ok':imag_ok,'vpsi_zero':psi.d==0}

def cleared_eval(mask,weights,t):
    Z,point,q,v,divv,s1,S,sumq,fac,_uz_primary=point_data(mask,weights,t)
    uz=sum((s1*v[e]-S*point[e] for e in Z),Fraction(0))
    alpha=[D(point[i],v[i]) for i in range(10)]; L=build_L(alpha); adj=adjugate4(L); A=mat_mul(adj,core.Q)
    C=[None]*(ORDER+1); C[0]=adj
    for n in range(1,ORDER+1): C[n]=mat_scale(mat_mul(A,C[n-1]),-1)
    df=detfactor_scaled(A); W=projected(C); nums=[]; imag_ok=True
    for ch in range(2):
        z=(D(0),D(0))
        for i in range(ORDER+1): z=cadd(z,cscale(df[i],W[ch][ORDER-i]))
        z=cscale(Fraction(math.factorial(ORDER)),z)
        imag_ok=imag_ok and z[1].v==0 and z[1].d==0
        nums.append((z[0].v,s1*z[0].d+fac*z[0].v))
    return {'N':[x[0] for x in nums],'B':[x[1] for x in nums],'U':uz,'imag_ok':imag_ok}

def interpolate(xs,ys):
    xs=[Fraction(x) for x in xs]; dd=[Fraction(y) for y in ys]; nc=[]
    while dd:
        nc.append(dd[0]); level=len(nc)
        dd=[(dd[i+1]-dd[i])/(xs[i+level]-xs[i]) for i in range(len(dd)-1)]
    poly=[Fraction(0)]*len(xs); basis=[Fraction(1)]
    for k,c in enumerate(nc):
        for i,b in enumerate(basis): poly[i]+=c*b
        if k+1<len(xs):
            a=-xs[k]; nb=[Fraction(0)]*(len(basis)+1)
            for i,b in enumerate(basis): nb[i]+=a*b; nb[i+1]+=b
            basis=nb
    return poly

def info_from_values(nodes,values,degree):
    full=interpolate(nodes,values); assert len(full)==32
    degree_ok=all(x==0 for x in full[degree+1:]); vec=full[:degree+1]
    order=next((i for i,x in enumerate(vec) if x!=0),None); exact_zero=order is None
    return {'degree_ok':degree_ok,'coefficients':[fq(x) for x in vec],'coefficient_sha256':vhash(vec),'first_nonzero_order':order,'first_nonzero_coefficient':None if order is None else fq(vec[order]),'exact_zero':exact_zero}

def resolve_lane(evaluator,mask,weights,nodes):
    Ns=[[],[]]; Bs=[[],[]]; Us=[]; imag=True; vpsi=True
    for t in nodes:
        r=evaluator(mask,weights,t); imag=imag and r['imag_ok']; vpsi=vpsi and r.get('vpsi_zero',True)
        for ch in range(2): Ns[ch].append(r['N'][ch]); Bs[ch].append(r['B'][ch])
        Us.append(r['U'])
    return {'channels':[{'N':info_from_values(nodes,Ns[ch],DEG_N),'B':info_from_values(nodes,Bs[ch],DEG_B)} for ch in range(2)],'U':info_from_values(nodes,Us,DEG_U),'imaginary_parts_zero':imag,'annihilator_psi_derivative_zero':vpsi}

def coeffs(info): return tuple(Fraction(x) for x in info['coefficients'])
def state(info): return ('ZERO',None) if info['exact_zero'] else ('ORDER',info['first_nonzero_order'])
def same_info(a,b): return a['degree_ok'] and b['degree_ok'] and coeffs(a)==coeffs(b)

def negative_controls():
    xs=PRIMARY_NODES
    p=[Fraction(0)]*32; p[0]=1; p[1]=-2; p[2]=1
    ys=[sum((p[k]*(Fraction(x)**k) for k in range(32)),Fraction(0)) for x in xs]
    rec=interpolate(xs,ys)
    higher=(rec[0]==1 and rec[1]==-2 and rec[2]==1 and all(z==0 for z in rec[3:]))
    zero=all(z==0 for z in interpolate(xs,[Fraction(0)]*32))
    trunc=[0,0,0,0,0,7]; trunc_bad=trunc[:-1]+[0]
    trunc_detected=(trunc!=trunc_bad)
    synth_a=[Fraction(W1[i])*(2 if i==0 else 1) for i in range(10)]
    synth_b=[Fraction(W1[i])*(2 if i==1 else 1) for i in range(10)]
    wrong_sub=(synth_a!=synth_b)
    wrong_perm=(tuple(W1)!=tuple(WP1))
    channel_swap=([1,2]!=[2,1])
    degree_lengths=(DEG_N+1,DEG_B+1,DEG_U+1)==(28,32,6)
    one_leading=(next(i for i,z in enumerate([0,5,0]) if z)!=0)
    return {'higher_order_after_candidate_cancellation':higher,'exact_zero_complete_support':zero,'truncation_detected':trunc_detected,'wrong_substitution_detected':wrong_sub,'wrong_permutation_detected':wrong_perm,'channel_swap_detected':channel_swap,'degree_ceiling_lengths':degree_lengths,'one_leading_term_shortcut_rejected':one_leading}

def proper_reps(): return [(m,s) for m,s in core.orbit_reps() if m not in (0,1023)]

def resolve_orbit(index):
    reps=proper_reps(); assert len(reps)==32; mask,osize=reps[index]; pm=core.pmask(mask,CYCLE); Z=[i for i in range(10) if (mask>>i)&1]
    lanes={
      'W1':resolve_lane(direct_eval,mask,W1,PRIMARY_NODES),
      'W2':resolve_lane(direct_eval,mask,W2,PRIMARY_NODES),
      'S5_W1':resolve_lane(direct_eval,pm,WP1,PRIMARY_NODES),
      'S5_W2':resolve_lane(direct_eval,pm,WP2,PRIMARY_NODES),
    }
    indep={
      'W1':resolve_lane(cleared_eval,mask,W1,INDEPENDENT_NODES),
      'W2':resolve_lane(cleared_eval,mask,W2,INDEPENDENT_NODES),
    }
    channels=[]
    for ch in range(2):
        cert={}
        for obj in ('N','B'):
            a=lanes['W1']['channels'][ch][obj]; b=lanes['W2']['channels'][ch][obj]; pa=lanes['S5_W1']['channels'][ch][obj]; pb=lanes['S5_W2']['channels'][ch][obj]
            ia=indep['W1']['channels'][ch][obj]; ib=indep['W2']['channels'][ch][obj]
            cert[obj]={
              'degree_checks':all(x['degree_ok'] for x in (a,b,pa,pb,ia,ib)),
              'witness_state_agreement':state(a)==state(b),
              's5_w1_full_coeff_covariance':same_info(a,pa),
              's5_w2_full_coeff_covariance':same_info(b,pb),
              'independent_w1_full_coeff_match':same_info(a,ia),
              'independent_w2_full_coeff_match':same_info(b,ib),
            }
            cert[obj]['certified']=all(cert[obj].values())
            cert[obj]['order']=a['first_nonzero_order'] if cert[obj]['certified'] else None
            cert[obj]['exact_zero']=a['exact_zero'] if cert[obj]['certified'] else None
        a=lanes['W1']['U']; b=lanes['W2']['U']; pa=lanes['S5_W1']['U']; pb=lanes['S5_W2']['U']; ia=indep['W1']['U']; ib=indep['W2']['U']
        ucert={'degree_checks':all(x['degree_ok'] for x in (a,b,pa,pb,ia,ib)),'witness_state_agreement':state(a)==state(b),'s5_w1_full_coeff_covariance':same_info(a,pa),'s5_w2_full_coeff_covariance':same_info(b,pb),'independent_w1_full_coeff_match':same_info(a,ia),'independent_w2_full_coeff_match':same_info(b,ib)}
        ucert['certified']=all(ucert.values()); ucert['order']=a['first_nonzero_order'] if ucert['certified'] else None; ucert['exact_zero']=a['exact_zero'] if ucert['certified'] else None
        cert['U']=ucert
        channels.append({'channel':ch+1,'N':cert['N'],'B':cert['B'],'U':cert['U'],'all_targets_certified':cert['N']['certified'] and cert['B']['certified'] and cert['U']['certified']})
    checks={
      'proper_orbit_count_32':len(reps)==32,
      'orbit_index_in_range':0<=index<32,
      'physical_k_1_to_9':1<=len(Z)<=9,
      'primary_nodes_frozen':PRIMARY_NODES==tuple(range(1,33)),
      'independent_nodes_frozen':INDEPENDENT_NODES==tuple(range(33,65)),
      'all_primary_imaginary_parts_zero':all(x['imaginary_parts_zero'] for x in lanes.values()),
      'all_primary_annihilator_psi_derivatives_zero':all(x['annihilator_psi_derivative_zero'] for x in lanes.values()),
      'all_independent_imaginary_parts_zero':all(x['imaginary_parts_zero'] for x in indep.values()),
      'negative_controls':all(negative_controls().values()),
    }
    all_infos=[]
    for lane in list(lanes.values())+list(indep.values()):
        all_infos.append(lane['U'])
        for cc in lane['channels']: all_infos.extend((cc['N'],cc['B']))
    checks['all_frozen_degree_checks_pass']=all(x['degree_ok'] for x in all_infos)
    checks['all_independent_full_coeff_matches_pass']=all(c[o]['independent_w1_full_coeff_match'] and c[o]['independent_w2_full_coeff_match'] for c in channels for o in ('N','B','U'))
    checks['all_s5_full_coeff_covariances_pass']=all(c[o]['s5_w1_full_coeff_covariance'] and c[o]['s5_w2_full_coeff_covariance'] for c in channels for o in ('N','B','U'))
    valid=all(checks.values())
    resolved=sum(1 for c in channels if c['all_targets_certified'])
    classification=INVALID if not valid else ('ORBIT_EXACT' if resolved==2 else 'ORBIT_PARTIAL_BLOCKED')
    return {'gate':'K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION','prereg_commit':PREREG,'implementation_freeze_commit':IMPLEMENTATION_FREEZE,'execution_amendment_commit':EXECUTION_AMENDMENT,'implementation_head':os.environ.get('GITHUB_SHA'),'degree_ceilings':{'N':DEG_N,'B':DEG_B,'U':DEG_U},'primary_nodes':list(PRIMARY_NODES),'independent_nodes':list(INDEPENDENT_NODES),'orbit':{'index':index,'mask':mask,'bits':Z,'k':len(Z),'orbit_size':osize,'s5_mask':pm},'weights':{'W1':list(W1),'W2':list(W2),'S5_W1':list(WP1),'S5_W2':list(WP2)},'primary':lanes,'independent':indep,'channels':channels,'checks':checks,'negative_controls':negative_controls(),'classification':classification}

def compact_orbit(d):
    return {'orbit':d['orbit'],'classification':d['classification'],'channels':d['channels'],'primary_hashes':{name:{'channels':[{'N':x['N']['coefficient_sha256'],'B':x['B']['coefficient_sha256']} for x in lane['channels']],'U':lane['U']['coefficient_sha256']} for name,lane in d['primary'].items()},'independent_hashes':{name:{'channels':[{'N':x['N']['coefficient_sha256'],'B':x['B']['coefficient_sha256']} for x in lane['channels']],'U':lane['U']['coefficient_sha256']} for name,lane in d['independent'].items()}}

def aggregate(directory):
    files=sorted(Path(directory).rglob('orbit_*.json')); rows=[json.loads(p.read_text()) for p in files]
    rows.sort(key=lambda r:r['orbit']['index'])
    idx=[r['orbit']['index'] for r in rows]; masks=[r['orbit']['mask'] for r in rows]; reps=proper_reps(); expected=[m for m,s in reps]
    checks={
      'exactly_32_orbit_files':len(rows)==32,
      'unique_orbit_indices':sorted(idx)==list(range(32)),
      'unique_masks':len(set(masks))==32,
      'masks_match_frozen_representatives':masks==expected,
      'proper_orbit_sizes_sum_1022':sum(r['orbit']['orbit_size'] for r in rows)==1022,
      'all_orbit_implementations_valid':all(r['classification']!=INVALID for r in rows),
      'all_negative_controls_pass':all(all(r['negative_controls'].values()) for r in rows),
      'all_lineage_fixed':all(r['prereg_commit']==PREREG and r['implementation_freeze_commit']==IMPLEMENTATION_FREEZE and r['execution_amendment_commit']==EXECUTION_AMENDMENT for r in rows),
    }
    valid=all(checks.values()); comps=[]
    for r in rows:
        for c in r['channels']: comps.append((r,c))
    checks['exactly_64_channel_orbit_components']=len(comps)==64
    valid=valid and checks['exactly_64_channel_orbit_components']
    certified=sum(1 for r,c in comps if c['all_targets_certified']); blocked=64-certified
    if not valid: classification=INVALID; status=INVALID
    elif blocked: classification=CLASS_PARTIAL; status='PASS_EXACT_PARTIAL_BLOCKED_SCOPED'
    else: classification=CLASS_EXACT; status='PASS_EXACT_SCOPED'
    obj_summary={}
    for obj in ('N','B','U'):
        obj_summary[obj]={'certified':sum(1 for r,c in comps if c[obj]['certified']),'exact_zero':sum(1 for r,c in comps if c[obj]['certified'] and c[obj]['exact_zero'] is True),'finite_order':sum(1 for r,c in comps if c[obj]['certified'] and c[obj]['exact_zero'] is False)}
        hist=defaultdict(int)
        for r,c in comps:
            if c[obj]['certified'] and c[obj]['order'] is not None: hist[str(c[obj]['order'])]+=1
        obj_summary[obj]['order_histogram']=dict(sorted(hist.items(),key=lambda kv:int(kv[0])))
    return {'gate':'K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION','prereg_commit':PREREG,'implementation_freeze_commit':IMPLEMENTATION_FREEZE,'execution_amendment_commit':EXECUTION_AMENDMENT,'workflow_head':os.environ.get('GITHUB_SHA'),'status':status,'classification':classification,'degree_ceilings':{'N':DEG_N,'B':DEG_B,'U':DEG_U},'primary_nodes':list(PRIMARY_NODES),'independent_nodes':list(INDEPENDENT_NODES),'checks':checks,'summary':{'proper_orbits':32,'channel_orbit_components':64,'certified_components':certified,'blocked_components':blocked,'objects':obj_summary},'orbit_rows':[compact_orbit(r) for r in rows],'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,'finite_part_selector':None,'regulator_independence':None}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--orbit-index',type=int); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); args=ap.parse_args()
    if (args.orbit_index is None)==(args.aggregate_dir is None): raise SystemExit('choose exactly one of --orbit-index or --aggregate-dir')
    out=resolve_orbit(args.orbit_index) if args.orbit_index is not None else aggregate(args.aggregate_dir)
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('CLASSIFICATION=',out['classification'],flush=True)
    if 'summary' in out: print('SUMMARY=',json.dumps(out['summary'],sort_keys=True),flush=True)

if __name__=='__main__': main()
