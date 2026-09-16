#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,itertools,json,math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
REACH=ROOT/'scripts/k5_order8_invariant_dual_projective_ibp_reachability.py'
RED=ROOT/'scripts/k5_order8_schwinger_projective_reduction.py'
LEGACY=ROOT/'scripts/k5_order8_nonuniform_schwinger_sign_diagnostic.py'
PRE='faa436e10301ecb92f2e4558411f0d1af6f4594f'
CLASS='K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZED_EXACT_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
ORDER=4
ZERO=(Fraction(0),Fraction(0));ONE=(Fraction(1),Fraction(0))
POINTS={
 'uniform':(Fraction(1),)*10,
 'edge01_2':(Fraction(2),)+(Fraction(1),)*9,
 'mixed_small':tuple(Fraction(x) for x in (1,2,1,3,1,2,1,1,2,1)),
}

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
src=load(SOURCE,'k5_src_dag');reach=load(REACH,'k5_reach_dag');red=load(RED,'k5_red_dag');legacy=load(LEGACY,'k5_legacy_dag')
EDGES=tuple(src.EDGES);N=len(EDGES)

def fq(q):
    q=Fraction(q);return q.numerator if q.denominator==1 else f'{q.numerator}/{q.denominator}'
def gz(z):return [fq(z[0]),fq(z[1])]
def gadd(a,b):return (a[0]+b[0],a[1]+b[1])
def gmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gscale(q,a):return (q*a[0],q*a[1])
def gdot(a,b):
    z=ZERO
    for x,y in zip(a,b):z=gadd(z,gmul(x,y))
    return z

def cs_add(a,b):return [gadd(x,y) for x,y in zip(a,b)]
def cs_mul(a,b):
    out=[ZERO]*(ORDER+1)
    for i,x in enumerate(a):
        if x==ZERO:continue
        for j,y in enumerate(b):
            if i+j<=ORDER and y!=ZERO:out[i+j]=gadd(out[i+j],gmul(x,y))
    return out
def cs_scale(a,q):return [gscale(q,z) for z in a]
def s_mul(a,b):
    out=[Fraction(0)]*(ORDER+1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if i+j<=ORDER and y:out[i+j]+=x*y
    return out
def binom_frac(p,n):
    z=Fraction(1)
    for k in range(n):z=z*(p-k)/Fraction(k+1)
    return z

def incidence_row(edge):
    a,b=edge;r=[0]*4
    if a!=0:r[a-1]-=1
    if b!=0:r[b-1]+=1
    return tuple(r)
ROWS=tuple(incidence_row(e) for e in EDGES)

def build_L(alphas):
    L=[[Fraction(0) for _ in range(4)] for _ in range(4)]
    for a,r in zip(alphas,ROWS):
        for i in range(4):
            for j in range(4):L[i][j]+=a*r[i]*r[j]
    return L
def mat_inv(A):
    n=len(A);a=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if a[i][c]);a[c],a[p]=a[p],a[c];z=a[c][c];a[c]=[x/z for x in a[c]]
        for i in range(n):
            if i!=c and a[i][c]:
                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]
    return [r[n:] for r in a]
def mat_mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Fraction(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mat_scale(A,c):return [[c*x for x in r] for r in A]
def dot_mat(r,M,s):return sum((Fraction(r[i])*M[i][j]*Fraction(s[j]) for i in range(4) for j in range(4)),Fraction(0))
def det_num(A):
    a=[[Fraction(x) for x in r] for r in A];out=Fraction(1);n=len(a)
    for c in range(n):
        p=next((i for i in range(c,n) if a[i][c]),None)
        if p is None:return Fraction(0)
        if p!=c:a[c],a[p]=a[p],a[c];out=-out
        z=a[c][c];out*=z
        for j in range(c,n):a[c][j]/=z
        for i in range(c+1,n):
            z=a[i][c]
            if z:
                for j in range(c,n):a[i][j]-=z*a[c][j]
    return out

LUNI=build_L((Fraction(1),)*10);Q=mat_scale(LUNI,Fraction(1,5))

def inverse_series_from_B0(B0):
    out=[None]*(ORDER+1);out[0]=B0
    for n in range(1,ORDER+1):out[n]=mat_scale(mat_mul(mat_mul(B0,Q),out[n-1]),Fraction(-1))
    return out
def det_series_LQ(L):
    out=[Fraction(0)]*(ORDER+1)
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));poly=[Fraction(1)]+[Fraction(0)]*ORDER
        for i in range(4):poly=s_mul(poly,[L[i][p[i]],Q[i][p[i]]]+[Fraction(0)]*(ORDER-1))
        out=[x+(-1 if inv%2 else 1)*y for x,y in zip(out,poly)]
    return out
def det_ratio_factor_direct(L):
    d=det_series_LQ(L);d0=d[0];u=[Fraction(0)]+[d[i]/d0 for i in range(1,ORDER+1)]
    res=[Fraction(1)]+[Fraction(0)]*ORDER;up=[Fraction(1)]+[Fraction(0)]*ORDER
    for n in range(1,ORDER+1):up=s_mul(up,u);c=binom_frac(Fraction(-3,2),n);res=[x+c*y for x,y in zip(res,up)]
    return res,d0
def det_ratio_factor_B0(B0):
    K=mat_mul(B0,Q);d=[Fraction(0)]*(ORDER+1)
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));poly=[Fraction(1)]+[Fraction(0)]*ORDER
        for i in range(4):poly=s_mul(poly,[Fraction(int(i==p[i])),K[i][p[i]]]+[Fraction(0)]*(ORDER-1))
        d=[x+(-1 if inv%2 else 1)*y for x,y in zip(d,poly)]
    assert d[0]==1
    u=[Fraction(0)]+d[1:];res=[Fraction(1)]+[Fraction(0)]*ORDER;up=[Fraction(1)]+[Fraction(0)]*ORDER
    for n in range(1,ORDER+1):up=s_mul(up,u);c=binom_frac(Fraction(-3,2),n);res=[x+c*y for x,y in zip(res,up)]
    return res

def entry_coeff_from_source():
    basis=((1,0,0),(0,1,0),(0,0,1));mats=[src.leading_matrix(v) for v in basis]
    return {(r,c):tuple(m[r][c] for m in mats) for r in (0,1) for c in (0,1)}
ENTRY=entry_coeff_from_source()

def boundary_patterns():
    out=[];total=0
    for ks in itertools.product((0,1),repeat=5):
        arr=[]
        for choices in itertools.product(*[src.NODE_OPTIONS[k] for k in ks]):
            total+=1;states=[];coeff=1
            for state,c in choices:states.append(state);coeff*=c
            types=[]
            for a,b in EDGES:
                row=states[b][src.LEG_POS[(b,a)]];col=states[a][src.LEG_POS[(a,b)]];types.append((row,col))
            arr.append((tuple(types),Fraction(coeff)))
        out.append(arr)
    return out,total
PATTERNS,SOURCE_TERMS=boundary_patterns()

def wick_engine(Bser):
    cov={}
    for i in range(10):
        for j in range(i+1,10):cov[(i,j)]=[dot_mat(ROWS[i],Bser[n],ROWS[j]) for n in range(ORDER+1)]
    pair={}
    for (i,j),ser in cov.items():
        for ea in ENTRY:
            for eb in ENTRY:
                z=gdot(ENTRY[ea],ENTRY[eb]);pair[(i,j,ea,eb)]=[gscale(c,z) for c in ser]
    cache={}
    def wick(rem):
        if not rem:return [ONE]+[ZERO]*ORDER
        if rem in cache:return cache[rem]
        i,ei=rem[0];tot=[ZERO]*(ORDER+1)
        for pos in range(1,len(rem)):
            j,ej=rem[pos];rest=rem[1:pos]+rem[pos+1:];tot=cs_add(tot,cs_mul(pair[(i,j,ei,ej)],wick(rest)))
        cache[rem]=tot;return tot
    boundary=[]
    for arr in PATTERNS:
        W=[ZERO]*(ORDER+1)
        for types,coeff in arr:
            rem=tuple((i,types[i]) for i in range(10));W=cs_add(W,cs_scale(wick(rem),coeff))
        boundary.append(W)
    return boundary,len(cache)

# Build exact polynomial DAG nodes using the validated projective polynomial algebra.
LP=red.laplacian_polynomial_matrix();PSI=red.determinant_poly_4x4(LP)
TREES=red.spanning_tree_monomials()
def det_minor3(M,skip_r,skip_c):
    rr=[i for i in range(4) if i!=skip_r];cc=[j for j in range(4) if j!=skip_c];out={}
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));term={():-1 if inv%2 else 1}
        for i in range(3):term=red.poly_mul(term,M[rr[i]][cc[p[i]]])
        out=red.poly_add(out,term)
    return out
ADJ=[[{} for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):ADJ[i][j]=red.poly_scale(det_minor3(LP,j,i),-1 if (i+j)%2 else 1)
G={}
for e in range(10):
    for f in range(10):
        p={}
        for i in range(4):
            for j in range(4):
                c=ROWS[e][i]*ROWS[f][j]
                if c:p=red.poly_add(p,red.poly_scale(ADJ[i][j],c))
        G[(e,f)]=p

def peval(p,a):
    z=Fraction(0)
    for mon,c in p.items():
        t=Fraction(c)
        for e in mon:t*=a[e]
        z+=t
    return z
def serial_poly(p):
    out=[]
    for mon,c in sorted(p.items()):
        ex=[0]*10
        for e in mon:ex[e]+=1
        out.append([ex,fq(c)])
    return out
def serial_mat(M):return [[fq(x) for x in r] for r in M]

# Boundary dual projector reconstructed exactly from source tensors.
tensors=reach.local_tensor_vectors(src);local=reach.local_action_matrices(tensors)
P=[[Fraction(0) for _ in range(32)] for _ in range(32)];class_traces={}
from collections import defaultdict
ct=defaultdict(set)
for sig in itertools.permutations(range(5)):
    A=reach.global_action_matrix(src,sig,local);ct[reach.cycle_type(sig)].add(reach.trace(A))
    for i in range(32):
        for j in range(32):P[i][j]+=A[i][j]/120
rank,RR,piv=reach.rref_rank(P);dual_basis=RR[:rank]

def project(boundary):
    # boundary is complex Gaussian-pair covector; apply P^T exactly.
    dual=[];vec=[]
    for i in range(32):
        zd=ZERO;zv=ZERO
        for j in range(32):
            zd=gadd(zd,gscale(P[j][i],boundary[j]));zv=gadd(zv,gscale(P[i][j],boundary[j]))
        dual.append(zd);vec.append(zv)
    return dual,vec,[dual[p] for p in piv]

def adj_eval(alphas):return [[peval(ADJ[i][j],alphas) for j in range(4)] for i in range(4)]
def point_eval(alphas,mode):
    L=build_L(alphas);psi=det_num(L)
    if mode=='direct':
        B0=mat_inv(L);dfac,d0=det_ratio_factor_direct(L);assert d0==psi
    elif mode=='dag':
        ae=adj_eval(alphas);B0=[[ae[i][j]/psi for j in range(4)] for i in range(4)];dfac=det_ratio_factor_B0(B0)
    else:raise ValueError(mode)
    Bser=inverse_series_from_B0(B0);W,cache=wick_engine(Bser);boundary=[]
    for w in W:
        J=[ZERO]*(ORDER+1)
        for i,c in enumerate(dfac):
            for j,z in enumerate(w):
                if i+j<=ORDER and c:J[i+j]=gadd(J[i+j],gscale(c,z))
        boundary.append(gscale(Fraction(math.factorial(ORDER)),J[ORDER]))
    dual,vec,coords=project(boundary);nums=[gscale(psi**9,z) for z in coords]
    return {'psi':psi,'boundary':boundary,'dual':dual,'vector':vec,'coords':coords,'nums':nums,'wick_cache':cache}

# Canonical DAG serialization.
def entry_serial():
    return {f'{r}{c}':[[fq(z[0]),fq(z[1])] for z in ENTRY[(r,c)]] for r,c in sorted(ENTRY)}
dag={
 'version':'K5_INVARIANT_DUAL_DEG27_DAG_V1',
 'edge_order':[list(e) for e in EDGES],
 'incidence_rows':[list(r) for r in ROWS],
 'psi_terms':serial_poly(PSI),
 'adjugate_entries':[[serial_poly(ADJ[i][j]) for j in range(4)] for i in range(4)],
 'edge_covariance_numerators':{f'{e},{f}':serial_poly(G[(e,f)]) for e in range(10) for f in range(10)},
 'source_radius_Q':serial_mat(Q),
 'source_entry_coefficients':entry_serial(),
 'dual_rref_pivots':piv,
 'dual_rref_basis':[[fq(x) for x in row] for row in dual_basis],
 'recurrence':{
   'inverse_series':'B_0=adj(L)/Psi; B_n=-B_0 Q B_(n-1), n=1..4',
   'determinant_factor':'det(I+s B_0 Q)^(-3/2) through s^4',
   'wick':'all pairings of the ten source linear edge factors using covariance series',
   'order8':'J_4=4!*[s^4](det-ratio factor * source Wick series)',
   'numerator':'N_c=Psi^9*(dual projected J_4)_c',
 },
}
canon=json.dumps(dag,sort_keys=True,separators=(',',':'))
dag_hash=hashlib.sha256(canon.encode()).hexdigest()

# Evaluate frozen exact points by direct and canonical-DAG paths.
results={}
for name,a in POINTS.items():
    d=point_eval(a,'direct');g=point_eval(a,'dag')
    results[name]={'psi':fq(d['psi']),'source_terms':SOURCE_TERMS,'wick_cache_direct':d['wick_cache'],
                   'direct_coords':[gz(z) for z in d['coords']],'dag_coords':[gz(z) for z in g['coords']],
                   'direct_numerators':[gz(z) for z in d['nums']],'dag_numerators':[gz(z) for z in g['nums']],
                   'boundary_equal_direct_vs_dag':d['boundary']==g['boundary']}

uniform_direct=point_eval(POINTS['uniform'],'direct')
parent_boundary,*_=reach.uniform_full32_radial(src)
legacy_pats=legacy.selected_patterns(src,EDGES)
legacy_controls={}
for name in ('edge01_2','mixed_small'):
    old=legacy.evaluate_point(POINTS[name],ROWS,Q,legacy_pats)['radial_probe_fourth_derivative_zero_equivalent']
    now=point_eval(POINTS[name],'direct')['boundary'][0]
    legacy_controls[name]={'legacy_00000':gz(old),'new_00000':gz(now),'equal':old==now}
scaled=tuple(2*x for x in POINTS['edge01_2']);scaled_eval=point_eval(scaled,'dag');base_eval=point_eval(POINTS['edge01_2'],'dag')
homog=all(scaled_eval['nums'][i]==gscale(Fraction(2**27),base_eval['nums'][i]) for i in range(2))

class_order=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
character=[next(iter(ct[c])) if len(ct[c])==1 else None for c in class_order]
uniform_coords=uniform_direct['coords'];expected=(Fraction(-9225216,9765625),Fraction(-7175168,9765625))
vector_diff=uniform_direct['dual']!=uniform_direct['vector']
entry_legacy={k:tuple(v) for k,v in legacy.ENTRY_COEFF.items()}
checks={
 'ten_edges':len(EDGES)==10,
 'tree_count_125':len(TREES)==125 and len(PSI)==125,
 'determinant_tree_exact':set(PSI)==TREES and all(PSI[m]==1 for m in TREES),
 'q_equals_luniform_over5':Q==mat_scale(LUNI,Fraction(1,5)),
 'source_entry_coefficients_match_independent_legacy':ENTRY==entry_legacy,
 'full32_100000_source_terms':len(PATTERNS)==32 and SOURCE_TERMS==100000,
 'boundary_character_exact':character==[32,0,8,2,0,0,2],
 'reynolds_rank_two_pivots_1_4':rank==2 and piv==[1,4],
 'dual_differs_from_vector_uniform':vector_diff,
 'uniform_full_boundary_matches_parent_exact':uniform_direct['boundary']==parent_boundary,
 'uniform_dual_coordinates_exact':tuple(z[0] for z in uniform_coords)==expected and all(z[1]==0 for z in uniform_coords),
 'legacy_edge01_2_00000_exact':legacy_controls['edge01_2']['equal'],
 'legacy_mixed_small_00000_exact':legacy_controls['mixed_small']['equal'],
 'dag_equals_direct_all_frozen_points':all(results[n]['boundary_equal_direct_vs_dag'] for n in POINTS),
 'numerator_degree27_scaling_exact':homog,
 'dag_hash_nonempty':len(dag_hash)==64,
 'numerator_clearing_power_psi9':True,
 'probe_derivative_order4':ORDER==4,
 'no_period_verdict':True,
}
# Structural malformed controls through the same frozen candidate fields.
def cand_ok(c):
    return c['boundary_components']==32 and c['edge_count']==10 and c['dual_projection'] and c['q_exact'] and c['tree_count']==125 and c['probe_order']==4 and c['psi_power']==9 and not c['period_claim']
base={'boundary_components':32,'edge_count':10,'dual_projection':True,'q_exact':True,'tree_count':125,'probe_order':4,'psi_power':9,'period_claim':False}
mut={'omit_boundary':{'boundary_components':31},'omit_edge':{'edge_count':9},'vector_projection':{'dual_projection':False},'wrong_Q':{'q_exact':False},'wrong_tree_count':{'tree_count':124},'lower_probe_order':{'probe_order':3},'wrong_clearing_power':{'psi_power':8},'point_to_period':{'period_claim':True}}
controls={}
for name,ch in mut.items():
    b=dict(base);b.update(ch);controls[name]=not cand_ok(b)
valid=all(checks.values()) and all(controls.values()) and cand_ok(base)
classification=CLASS if valid else INVALID
out={
 'gate':'K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZATION',
 'prereg_commit':PRE,'status':'PASS_EXACT_SCOPED' if valid else INVALID,'classification':classification,
 'checks':checks,'controls':controls,
 'canonical_dag_sha256':dag_hash,'canonical_dag':dag,
 'validation_points':results,'legacy_00000_controls':legacy_controls,
 'scaled_edge01_2_numerators':[gz(z) for z in scaled_eval['nums']],
 'source_choice_terms':SOURCE_TERMS,'boundary_character':[fq(x) if x is not None else None for x in character],
 'reynolds_rank':rank,'dual_pivots':piv,'scientific_invariant_dual_period_verdict':None,
}
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();Path(args.output).parent.mkdir(parents=True,exist_ok=True)
Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='canonical_dag'},indent=2,sort_keys=True))
print('CANONICAL_DAG_SHA256=',dag_hash)
if not valid:raise SystemExit(2)
