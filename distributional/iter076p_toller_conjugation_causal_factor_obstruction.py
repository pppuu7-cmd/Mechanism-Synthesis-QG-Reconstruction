import argparse,itertools,json,os

N=tuple(range(5))
EDGES=tuple((a,b) for a in N for b in N if a<b)
TRIANGLES=tuple(itertools.combinations(N,3))
SIGMAS=tuple(itertools.product((-1,1),repeat=5))
SOURCE='sources/TOLLER_MATRICES_2026_CONJUGATION_BRANCH_FLIP_SNAPSHOT.md'

def pattern(sigma):
    return tuple(sigma[a]*sigma[b] for a,b in EDGES)

def lane_a():
    try: txt=open(SOURCE,encoding='utf-8').read()
    except Exception as exc:
        return {'iteration':'Iter076P','lane':'A','pass':False,'failure':'source_read','detail':str(exc)}
    locks={
        'exact_conjugation_branch_flip':'conj(t^(+/- ,rho,k)_{j l m}(beta)) = (-1)^(j-l) t^(-/+ ,rho,k)_{l j,-m}(beta)' in txt,
        'gamma_simple_specialization':'conj(t^(kappa,gamma j,j)_{j j m}(beta)) = t^(-kappa,gamma j,j)_{j j,-m}(beta)' in txt,
        'causal_factorization':'kappa_ab = sigma_a sigma_b' in txt,
        'no_full_amplitude_cancellation_claim':'does not establish cancellation or non-cancellation' in txt,
    }
    ok=all(locks.values())
    return {'iteration':'Iter076P','lane':'A','pass':ok,'source':SOURCE,'locks':locks,'surrogate_identity_used':False}

def lane_b():
    image=sorted(set(pattern(s) for s in SIGMAS))
    image_set=set(image)
    flipped=[tuple(-x for x in k) for k in image]
    hits=sum(k in image_set for k in flipped)
    inter=len(image_set.intersection(flipped))
    ok=(len(image)==16 and hits==0 and inter==0)
    return {'iteration':'Iter076P','lane':'B','pass':ok,'edge_sign_assignments':32,
            'distinct_causal_wedge_patterns':len(image),'flipped_patterns_tested':len(flipped),
            'flipped_patterns_in_causal_image':hits,'causal_and_flipped_image_intersection':inter}

def tri_product(k,t):
    eidx={e:i for i,e in enumerate(EDGES)}
    a,b,c=t
    return k[eidx[(a,b)]]*k[eidx[(a,c)]]*k[eidx[(b,c)]]

def lane_c():
    image=sorted(set(pattern(s) for s in SIGMAS))
    causal=[]; flipped=[]
    for k in image:
        fk=tuple(-x for x in k)
        for t in TRIANGLES:
            causal.append(tri_product(k,t))
            flipped.append(tri_product(fk,t))
    cp=sum(x==1 for x in causal); fm=sum(x==-1 for x in flipped)
    ok=(len(causal)==160 and cp==160 and len(flipped)==160 and fm==160)
    return {'iteration':'Iter076P','lane':'C','pass':ok,'distinct_patterns':len(image),
            'triangles_per_pattern':len(TRIANGLES),'causal_triangle_checks':len(causal),
            'causal_triangle_plus_one':cp,'flipped_triangle_checks':len(flipped),
            'flipped_triangle_minus_one':fm,'certificate':'triangle_product_obstruction'}

def lane_d():
    locks={
        'known_toller_conjugation_closes_within_causal_K5_image':False,
        'same_causal_vertex_conjugation_symmetry_established':False,
        'same_causal_opposite_Omega_cancellation_established':False,
        'generic_finite_spin_signed_P3_promoted':False,
        'both_Omega_sectors_survive_full_integration':'UNTESTED',
        'Iter076N_saddle_selection_unchanged':True,
        'Iter076O_bulk_overlap_unchanged':True,
        'epsilon_minus1_coefficient_established':False,
    }
    ok=(not locks['known_toller_conjugation_closes_within_causal_K5_image']
        and not locks['same_causal_vertex_conjugation_symmetry_established']
        and not locks['same_causal_opposite_Omega_cancellation_established']
        and not locks['generic_finite_spin_signed_P3_promoted']
        and locks['both_Omega_sectors_survive_full_integration']=='UNTESTED'
        and locks['Iter076N_saddle_selection_unchanged'] and locks['Iter076O_bulk_overlap_unchanged']
        and not locks['epsilon_minus1_coefficient_established'])
    return {'iteration':'Iter076P','lane':'D','pass':ok,'locks':locks}

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
            if o.get('iteration')=='Iter076P' and o.get('lane') in LANES: got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    if valid: cls='ITER076P_EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED'
    elif got.get('A') and not got['A'].get('pass'): cls='ITER076P_TOLLER_CONJUGATION_SOURCE_LOCK_FAIL'
    elif got.get('B') and not got['B'].get('pass'): cls='ITER076P_CAUSAL_IMAGE_CLOSED_UNDER_BRANCH_FLIP_REVIEW'
    elif got.get('C') and not got['C'].get('pass'): cls='ITER076P_TRIANGLE_FACTOR_CERTIFICATE_FAIL'
    else: cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL'
    return {'iteration':'Iter076P','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},
            'classification':cls,'known_toller_conjugation_closes_within_causal_K5_image':False if valid else None,
            'same_causal_opposite_Omega_cancellation_established':False,
            'generic_finite_spin_signed_P3_promoted':False,
            'full_integration_sector_survival':'UNTESTED',
            'claim_lock':'Known exact Toller conjugation flips the all-wedge branch pattern outside the source causal K5 image if valid; no same-causal cancellation or generic finite-spin P3 follows.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir):raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    dump(o,a.output);print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')):raise SystemExit(2)

if __name__=='__main__':main()
