import argparse,cmath,itertools,json,math,os
from fractions import Fraction as Q

N=tuple(range(5))
EDGES=tuple((a,b) for a in N for b in N if a<b)
SIGMA=(-1,1,1,1,1)
TOL=1e-12
MARGIN=1e-8
SOURCE='sources/CAUSAL_SPINFOAM_VERTEX_2026_OFF_SADDLE_TOLLER_SUPPORT_SNAPSHOT.md'
US=(
    (Q(0),Q(0),Q(0)),
    (Q(1,3),Q(0),Q(0)),
    (Q(0),Q(1,4),Q(0)),
    (Q(0),Q(0),Q(1,5)),
    (Q(1,6),Q(1,7),Q(1,8)),
)

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

def hyper_q(u):
    ss=sum(x*x for x in u); d=1-ss
    return ((1+ss)/d,)+tuple(2*x/d for x in u)

def delta(F,sigma=SIGMA):
    return det_exact([[1]*5]+[[Q(sigma[a])*F[a][m] for a in N] for m in range(4)])

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def dag(A):
    return [[A[j][i].conjugate() for j in range(2)] for i in range(2)]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def inv2(A):
    d=det2(A)
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def boost(u):
    ux,uy,uz=(float(x) for x in u); r2=ux*ux+uy*uy+uz*uz
    c=1.0/math.sqrt(1.0-r2)
    return [[c*(1+uz),c*(ux-1j*uy)],[c*(ux+1j*uy),c*(1-uz)]]

def hermitian_error(H):
    return max(abs(H[i][j]-H[j][i].conjugate()) for i in range(2) for j in range(2))

def spectral(rel):
    H=mm(rel,dag(rel))
    trc=H[0][0]+H[1][1]
    tr=trc.real
    dh=det2(H)
    disc=tr*tr-4.0*dh.real
    if disc<0 and abs(disc)<1e-13:disc=0.0
    if disc<0:return H,tr,dh,float('nan'),float('nan')
    sd=math.sqrt(disc)
    return H,tr,dh,(tr-sd)/2.0,(tr+sd)/2.0

def configs():
    Gp=[boost(u) for u in US]
    Fp=[hyper_q(u) for u in US]
    order=(0,2,1,3,4)
    Gm=[Gp[i] for i in order]
    Fm=[Fp[i] for i in order]
    return {'X+':(Gp,Fp),'X-':(Gm,Fm)}

def wedge_spectrum(G,a,b):
    rel=mm(inv2(G[b]),G[a])
    H,tr,dh,lmin,lmax=spectral(rel)
    return rel,H,tr,dh,lmin,lmax

def lane_a():
    checks=[]; ok=True
    for name,(G,_) in configs().items():
        for a,b in EDGES:
            rel,H,tr,dh,lmin,lmax=wedge_spectrum(G,a,b)
            dr=det2(rel)
            herm=hermitian_error(H)
            positive=(H[0][0].real>0 and dh.real>0 and lmin>0)
            passed=(abs(dr-1)<TOL and herm<TOL and abs(dh-1)<TOL and positive and tr>2+TOL
                    and lmax>1+TOL and lmin<1-TOL and abs(lmax*lmin-1)<TOL)
            ok=ok and passed
            checks.append({'config':name,'edge':[a,b],'pass':passed,'det_rel_error':abs(dr-1),
                           'hermitian_error':herm,'det_H_error':abs(dh-1),'trace_H':tr,
                           'lambda_min':lmin,'lambda_max':lmax,'lambda_product_error':abs(lmax*lmin-1)})
    return {'iteration':'Iter076O','lane':'A','pass':ok,'instances':len(checks),
            'instances_passed':sum(c['pass'] for c in checks),'tolerance':TOL,'checks':checks}

def pairwise_distinct(F):
    return len(set(F))==len(F)

def lane_b():
    C=configs(); Fp=C['X+'][1]; Fm=C['X-'][1]
    Dp=delta(Fp); Dm=delta(Fm)
    op=1 if Dp>0 else -1 if Dp<0 else 0
    om=1 if Dm>0 else -1 if Dm<0 else 0
    ok=(Dp!=0 and Dm!=0 and Dm==-Dp and om==-op and pairwise_distinct(Fp) and pairwise_distinct(Fm))
    return {'iteration':'Iter076O','lane':'B','pass':ok,'sigma':list(SIGMA),
            'causal_class':'1->4','delta_plus':str(Dp),'delta_minus':str(Dm),
            'exact_opposite_delta':Dm==-Dp,'omega_plus':op,'omega_minus':om,
            'opposite_omega':om==-op,'same_fixed_sigma':True,
            'Xplus_pairwise_distinct':pairwise_distinct(Fp),'Xminus_pairwise_distinct':pairwise_distinct(Fm)}

def lane_c():
    all_ok=True; out={}; global_min=float('inf')
    for name,(G,_) in configs().items():
        rows=[]; config_ok=True
        for a,b in EDGES:
            _,_,_,_,lmin,lmax=wedge_spectrum(G,a,b)
            k=SIGMA[a]*SIGMA[b]
            B=math.log(lmax) if k==1 else math.log(lmin)
            signed=k*B
            passed=(signed>MARGIN)
            config_ok=config_ok and passed; global_min=min(global_min,abs(B))
            rows.append({'edge':[a,b],'kappa':k,'B_extremal':B,'kappa_times_B':signed,'pass':passed})
        out[name]={'pass':config_ok,'wedges':rows,'min_abs_B':min(abs(r['B_extremal']) for r in rows)}
        all_ok=all_ok and config_ok
    try: txt=open(SOURCE,encoding='utf-8').read()
    except Exception: txt=''
    independent_lock=('independent integration variables' in txt and 'ten `z_ab`' in txt)
    ok=all_ok and global_min>MARGIN and independent_lock
    return {'iteration':'Iter076O','lane':'C','pass':ok,'sigma':list(SIGMA),
            'independent_wedge_spinor_source_lock':independent_lock,
            'boundary_distribution_used':False,'frozen_margin':MARGIN,
            'global_min_abs_B':global_min,'configurations':out}

def lane_d():
    I=[[1+0j,0j],[0j,1+0j]]
    H,tr,dh,lmin,lmax=spectral(I)
    unitary_bulk_rejected=(abs(tr-2)<TOL and abs(lmin-1)<TOL and abs(lmax-1)<TOL)
    locks={
        'exact_bulk_support_global_Omega_projector':False,
        'both_Omega_sectors_in_same_fixed_causal_bulk_support':True,
        'boundary_distribution_used_for_counterexample':False,
        'full_amplitude_interference_conclusion':'UNTESTED',
        'generic_finite_spin_signed_P3_promoted':False,
        'Iter076N_saddle_selection_unchanged':True,
        'epsilon_minus1_coefficient_established':False,
    }
    ok=(unitary_bulk_rejected and not locks['exact_bulk_support_global_Omega_projector']
        and locks['both_Omega_sectors_in_same_fixed_causal_bulk_support']
        and not locks['boundary_distribution_used_for_counterexample']
        and locks['full_amplitude_interference_conclusion']=='UNTESTED'
        and not locks['generic_finite_spin_signed_P3_promoted']
        and locks['Iter076N_saddle_selection_unchanged']
        and not locks['epsilon_minus1_coefficient_established'])
    return {'iteration':'Iter076O','lane':'D','pass':ok,'unitary_control_trace_H':tr,
            'unitary_lambda_min':lmin,'unitary_lambda_max':lmax,
            'strict_bulk_rejects_unitary_control':unitary_bulk_rejected,'locks':locks}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def dump(o,p):
    os.makedirs(os.path.dirname(p) or '.',exist_ok=True)
    with open(p,'w',encoding='utf-8') as f:json.dump(o,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for b,_,fs in os.walk(root):
        for f in fs:
            if not f.endswith('.json'):continue
            try:
                with open(os.path.join(b,f),encoding='utf-8') as h:o=json.load(h)
            except Exception:continue
            if o.get('iteration')=='Iter076O' and o.get('lane') in LANES:got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    if valid: cls='ITER076O_EXACT_TOLLER_BULK_SUPPORT_CONTAINS_BOTH_OMEGA_SECTORS_OFF_SADDLE_NO_GLOBAL_FINITE_SPIN_SELECTOR_SCOPED'
    elif got.get('A') and not got['A'].get('pass'):cls='ITER076O_SINGLE_WEDGE_SPECTRAL_SUPPORT_FAIL'
    elif got.get('B') and not got['B'].get('pass'):cls='ITER076O_OPPOSITE_OMEGA_CONTROL_FAIL'
    elif got.get('C') and not got['C'].get('pass'):cls='ITER076O_MULTI_WEDGE_SUPPORT_FAIL'
    else:cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL'
    return {'iteration':'Iter076O','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},
            'classification':cls,'fixed_causal_class':'1->4','exact_bulk_support_global_Omega_projector':False if valid else None,
            'generic_finite_spin_signed_P3_promoted':False,
            'full_amplitude_interference_conclusion':'UNTESTED',
            'claim_lock':'Exact Heaviside bulk support alone is not a global off-saddle Omega projector if valid; Iter076N saddle selection remains unchanged, and full-amplitude sector survival is untested.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir):raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    dump(o,a.output);print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')):raise SystemExit(2)

if __name__=='__main__':main()
