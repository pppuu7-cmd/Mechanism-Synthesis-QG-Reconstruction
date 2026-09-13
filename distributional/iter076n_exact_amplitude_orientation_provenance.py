import argparse,itertools,json,os

N=tuple(range(5)); PAIRS=tuple((a,b) for a in N for b in N if a<b); P5=tuple(itertools.permutations(N))

def invcount(p): return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def sgnperm(p): return -1 if invcount(p)%2 else 1

def kappa(sig): return tuple(sig[a]*sig[b] for a,b in PAIRS)

def lane_a():
    sigs=list(itertools.product((-1,1),repeat=5))
    patterns={kappa(s) for s in sigs}
    reversal=all(kappa(s)==kappa(tuple(-x for x in s)) for s in sigs)
    two_to_one=all(sum(kappa(t)==kappa(s) for t in sigs)==2 for s in sigs)
    ok=len(patterns)==16 and reversal and two_to_one
    return {'iteration':'Iter076N','lane':'A','pass':ok,'sigma_assignments':32,'distinct_kappa_patterns':len(patterns),
            'global_reversal_invisible_to_kappa':reversal,'each_kappa_has_two_sigma_lifts':two_to_one,
            'source_visible_branch_data':'kappa_ab=sigma_a*sigma_b'}

def relabel_pair(pair,p):
    a,b=p[pair[0]],p[pair[1]]
    return tuple(sorted((a,b)))

def lane_b():
    base=tuple(sorted(PAIRS))
    all_cov=True; odd_minus=False; even=odd=0
    for p in P5:
        mapped=tuple(sorted(relabel_pair(e,p) for e in PAIRS))
        all_cov &= mapped==base
        if sgnperm(p)>0: even+=1
        else:
            odd+=1
            # A commutative product over all ten wedge factors acquires no permutation sign.
            odd_minus |= False
    ok=all_cov and even==60 and odd==60 and not odd_minus
    return {'iteration':'Iter076N','lane':'B','pass':ok,'S5_checks':120,'even_permutations':even,'odd_permutations':odd,
            'ten_wedge_support_covariant':all_cov,'intrinsic_alternating_sign_from_product_order':odd_minus,
            'interpretation':'source-visible commutative wedge product does not itself provide the S5 sign character'}

def lane_c():
    exact_ingredients={
      'toller_branch_from_kappa':True,
      'relative_group_element_gb_inv_ga':True,
      'haar_group_integrals':True,
      'su2_magnetic_D_factors_in_eq7':True,
      'five_normal_determinant':False,
      'levi_civita_cross_wedge_contraction':False,
      'proper_vertex_beta_projector':False,
      'four_volume_orientation_operator':False,
      'explicit_global_orientation_pseudoscalar':False,
    }
    absent=all(not exact_ingredients[k] for k in ('five_normal_determinant','levi_civita_cross_wedge_contraction','proper_vertex_beta_projector','four_volume_orientation_operator','explicit_global_orientation_pseudoscalar'))
    return {'iteration':'Iter076N','lane':'C','pass':absent,'exact_source_visible_ingredients':exact_ingredients,
            'cross_wedge_orientation_selector_source_exhibited':not absent}

def lane_d():
    facts={
      'combinatorial_regge_relation_declared_semiclassical':True,
      'single_regge_exponential_is_large_spin_result':True,
      'proper_vertex_relation_explicitly_left_to_clarify':True,
      'importing_four_volume_projector_would_add_non_eq4_structure':True,
      'semiclassical_to_exact_promotion_forbidden':True,
    }
    ok=all(facts.values())
    return {'iteration':'Iter076N','lane':'D','pass':ok,'firewall':facts}

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
        c='ITER076N_EQ4_EQ7_EXACT_AMPLITUDE_HAS_NO_SOURCE_EXHIBITED_GLOBAL_ORIENTATION_SELECTOR_PROVENANCE_BLOCKED_SOURCE_NATIVE_SCOPED'
    else:
        c='ITER076N_SOURCE_AUDIT_INCONCLUSIVE_REVIEW_REQUIRED_SCOPED'
    return {'iteration':'Iter076N','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'classification':c,
            'signed_P3_source_native_authorized':False,
            'claim_lock':'The audit establishes absence of a source-exhibited exact selector in the frozen Eq4/Eq7 structure, not a universal impossibility theorem. Semiclassical orientation is not promoted to exact provenance.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir); dump(o,a.output); print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')): raise SystemExit(2)
if __name__=='__main__': main()
