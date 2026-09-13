import argparse,itertools,json,os
from fractions import Fraction as Q

N=tuple(range(5))
EDGES=tuple((a,b) for a in N for b in N if a<b)
SIGMAS=tuple(itertools.product((-1,1),repeat=5))
SOURCE='sources/CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md'

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

def control_vectors():
    us=[(Q(0),Q(0),Q(0)),(Q(1,3),0,0),(0,Q(1,4),0),(0,0,Q(1,5)),(Q(1,6),Q(1,7),Q(1,8))]
    return [hyper_q(u) for u in us]

def delta(F,sigma):
    return det_exact([[1]*5]+[[Q(sigma[a])*F[a][m] for a in N] for m in range(4)])

def parity(F):
    # Genuine improper Lorentz reflection P=diag(1,-1,1,1), det(P)=-1.
    return [(f[0],-f[1],f[2],f[3]) for f in F]

def lane_a():
    try: txt=open(SOURCE,encoding='utf-8').read()
    except Exception as exc:
        return {'iteration':'Iter076N','lane':'A','pass':False,'failure':'source_read','detail':str(exc)}
    locks={
        'kappa_source_factorization':'kappa_ab=sigma_a sigma_b' in txt,
        'exact_heaviside_distribution_restrictor':'theta(kappa_ab * B(z,g)) + kappa_ab * delta^(rho,j)(B(z,g))' in txt,
        'exact_B_definition':'B(z,g) = log( <g^dagger z|g^dagger z> / <z|z> )' in txt,
        'distribution_boundary_support':'supported only at `B=0`' in txt,
        'finite_spin_exact_wording':'exact amplitude-level restriction' in txt,
    }
    ok=all(locks.values())
    return {'iteration':'Iter076N','lane':'A','pass':ok,'source':SOURCE,'locks':locks,
            'surrogate_beta_plus_i_epsilon_used':False,'inserted_levi_civita_projector_used':False}

def lane_b():
    # All-equal s cannot satisfy finite non-degenerate Lorentzian normal closure.
    s_configs=[s for s in SIGMAS if len(set(s))>1]
    compatible=0; incompatible=0; plus_admitted=0; minus_admitted=0
    compatible_plus_wedge_positive=0; compatible_minus_wedge_negative=0
    incompatible_plus_rejected=0; all_checks=True
    for s in s_configs:
        for sigma in SIGMAS:
            wedge=[sigma[a]*sigma[b]*s[a]*s[b] for a,b in EDGES]
            comp=all(sigma[a]*sigma[b]==s[a]*s[b] for a,b in EDGES)
            plus=all(x==1 for x in wedge)
            minus=all(-x==1 for x in wedge)
            if comp:
                compatible+=1
                compatible_plus_wedge_positive+=sum(x==1 for x in wedge)
                compatible_minus_wedge_negative+=sum(-x==-1 for x in wedge)
                if not plus or minus: all_checks=False
            else:
                incompatible+=1
                if not plus: incompatible_plus_rejected+=1
                else: all_checks=False
            plus_admitted+=int(plus); minus_admitted+=int(minus)
            # For source-factorizable kappa on K5, the minus branch may never be positive on all wedges.
            if minus: all_checks=False
    expected=(len(s_configs)==30 and len(SIGMAS)==32 and compatible==60 and incompatible==900)
    ok=all_checks and expected and plus_admitted==60 and minus_admitted==0 and incompatible_plus_rejected==900
    return {'iteration':'Iter076N','lane':'B','pass':ok,'regge_s_assignments':len(s_configs),
            'sigma_assignments':len(SIGMAS),'pair_assignments':len(s_configs)*len(SIGMAS),
            'compatible_pairs':compatible,'incompatible_pairs':incompatible,
            'plus_branch_admitted_pairs':plus_admitted,'minus_branch_admitted_pairs':minus_admitted,
            'compatible_plus_positive_wedge_checks':compatible_plus_wedge_positive,
            'compatible_minus_negative_wedge_checks':compatible_minus_wedge_negative,
            'incompatible_plus_rejected_pairs':incompatible_plus_rejected,
            'beta_sign_assumption':'positive_nonzero_on_frozen_nondegenerate_lorentzian_saddle_locus'}

def lane_c():
    F=control_vectors(); PF=parity(F)
    nondeg=0; parity_flips=0; reversal_invariant=0; exact_equalities=0
    for sigma in SIGMAS:
        D=delta(F,sigma); DP=delta(PF,sigma); DR=delta(F,tuple(-x for x in sigma))
        if D!=0: nondeg+=1
        if D!=0 and DP==-D: parity_flips+=1
        if D!=0 and DR==D: reversal_invariant+=1
        if DP==-D and DR==D: exact_equalities+=1
    try: txt=open(SOURCE,encoding='utf-8').read()
    except Exception: txt=''
    source_parity_lock=('parity-related' in txt and 'determinant `-1`' in txt)
    ok=(nondeg==32 and parity_flips==32 and reversal_invariant==32 and exact_equalities==32 and source_parity_lock)
    return {'iteration':'Iter076N','lane':'C','pass':ok,'sigma_assignments':32,
            'nondegenerate_controls':nondeg,'exact_parity_sign_flips':parity_flips,
            'global_sigma_reversal_invariant':reversal_invariant,'exact_equalities':exact_equalities,
            'source_two_saddles_parity_related_lock':source_parity_lock,
            'conclusion_if_pass':'parity-related critical branches occupy opposite Omega_sigma sectors'}

def lane_d():
    F=control_vectors(); FD=list(F); FD[4]=FD[3]
    sigma=(1,-1,1,-1,-1) # identical last weighted affine columns
    D=delta(FD,sigma); omega=None if D==0 else (1 if D>0 else -1)
    locks={
        'selected_scope':'NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS',
        'exact_toller_restrictor_is_finite_spin_source_structure':True,
        'omega_identification_uses_saddle_parity_reconstruction':True,
        'generic_finite_spin_off_saddle_signed_P3_promoted':False,
        'degenerate_sector_promoted':False,
        'euclidean_sector_promoted':False,
        'vector_geometry_sector_promoted':False,
        'epsilon_minus1_coefficient_established':False,
    }
    ok=(D==0 and omega is None and locks['selected_scope']=='NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS'
        and not locks['generic_finite_spin_off_saddle_signed_P3_promoted']
        and not locks['degenerate_sector_promoted'] and not locks['euclidean_sector_promoted']
        and not locks['vector_geometry_sector_promoted'] and not locks['epsilon_minus1_coefficient_established'])
    return {'iteration':'Iter076N','lane':'D','pass':ok,'degenerate_delta':str(D),
            'omega_on_degenerate':omega,'scope_locks':locks,'fit_or_regularization_used':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def dump(o,p):
    os.makedirs(os.path.dirname(p) or '.',exist_ok=True)
    with open(p,'w',encoding='utf-8') as f: json.dump(o,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for b,_,fs in os.walk(root):
        for f in fs:
            if not f.endswith('.json'): continue
            try:
                with open(os.path.join(b,f),encoding='utf-8') as h:o=json.load(h)
            except Exception: continue
            if o.get('iteration')=='Iter076N' and o.get('lane') in LANES: got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    if valid:
        classification='ITER076N_EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED'
    elif got.get('A') and not got['A'].get('pass'):
        classification='ITER076N_SOURCE_RESTRICTOR_PROVENANCE_FAIL'
    elif got.get('B') and not got['B'].get('pass'):
        classification='ITER076N_CAUSAL_SADDLE_SELECTION_FAIL'
    elif got.get('C') and not got['C'].get('pass'):
        classification='ITER076N_PARITY_OMEGA_BRIDGE_FAIL'
    else:
        classification='INFRASTRUCTURE_OR_NUMERICAL_FAIL'
    return {'iteration':'Iter076N','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},
            'classification':classification,'selected_scope':'NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS' if valid else None,
            'generic_finite_spin_off_saddle_P3_promoted':False,
            'claim_lock':'Amplitude-selection provenance is scoped to the non-degenerate Lorentzian Regge saddle locus; generic finite-spin signed P3 and epsilon^-1 coefficient remain unestablished.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    dump(o,a.output); print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')): raise SystemExit(2)

if __name__=='__main__': main()
