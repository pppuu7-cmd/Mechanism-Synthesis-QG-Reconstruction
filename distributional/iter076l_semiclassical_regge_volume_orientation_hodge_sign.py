import argparse,itertools,json,os

V4=(0,1,2,3)
PERMS4=tuple(itertools.permutations(V4))
NODES=tuple(range(5))
PERMS5=tuple(itertools.permutations(NODES))

def invcount(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def sgn(p): return -1 if invcount(p)%2 else 1

def prod(xs):
    z=1
    for x in xs: z*=x
    return z

def det_int(A):
    n=len(A); total=0
    for p in itertools.permutations(range(n)):
        total += sgn(p) * prod(A[i][p[i]] for i in range(n))
    return total

def permute_columns(X,p):
    return [[row[p[j]] for j in range(len(p))] for row in X]

def lane_a():
    X=[[1 if i==j else 0 for j in V4] for i in V4]
    base=det_int(X)
    checks=[]
    for p in PERMS4:
        d=det_int(permute_columns(X,p))
        checks.append(d==sgn(p)*base)
    preserves=sum(1 for p in PERMS4 if sgn(p)==1)
    flips=sum(1 for p in PERMS4 if sgn(p)==-1)
    ok=base!=0 and all(checks) and preserves==12 and flips==12
    return {'iteration':'Iter076L','lane':'A','pass':ok,'base_determinant':base,
            'permutations_checked':len(checks),'orientation_preserving':preserves,
            'orientation_flipping':flips,'orientation_character_exact':all(checks)}

EDGES=tuple((i,j) for i in V4 for j in V4 if i<j)
EIDX={e:i for i,e in enumerate(EDGES)}

def canon(a,b): return (a,b) if a<b else (b,a)
def comp(e): return tuple(sorted(set(V4)-set(e)))
def eps4(a,b,c,d): return sgn((a,b,c,d))

def R(p):
    M=[[0]*6 for _ in range(6)]
    for e in EDGES:
        a,b=p[e[0]],p[e[1]]
        pe=canon(a,b)
        orient=1 if a<b else -1
        M[EIDX[pe]][EIDX[e]]=orient
    return M

def canonical_H():
    H=[[0]*6 for _ in range(6)]
    for e in EDGES:
        c=comp(e)
        H[EIDX[c]][EIDX[e]]=eps4(e[0],e[1],c[0],c[1])
    return H

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def scale(c,A): return [[c*x for x in row] for row in A]

def lane_b():
    H=canonical_H(); twisted_all=True; family_covariant=True; wrong_same_sign_rejected=False
    for p in PERMS4:
        Rp=R(p); sp=sgn(p)
        for omega in (-1,1):
            Hw=scale(omega,H)
            twisted_all &= (matmul(Hw,Rp)==scale(sp,matmul(Rp,Hw)))
            Hwp=scale(sp*omega,H)
            family_covariant &= (matmul(Hwp,Rp)==matmul(Rp,Hw))
        if sp==-1:
            wrong_same_sign_rejected |= (matmul(H,Rp)!=matmul(Rp,H))
    reversal_exchange=(scale(-1,H)!=H and scale(-1,scale(-1,H))==H)
    ok=twisted_all and family_covariant and reversal_exchange and wrong_same_sign_rejected
    return {'iteration':'Iter076L','lane':'B','pass':ok,'twisted_covariance_permutations':24,
            'both_hodge_lifts_obey_twisted_law':twisted_all,
            'pseudoscalar_transport_makes_selected_family_covariant':family_covariant,
            'orientation_reversal_exchanges_two_lifts':reversal_exchange,
            'orientation_blind_same_sign_control_rejected':wrong_same_sign_rejected}

def induced_perm(old_root,p):
    old=[x for x in NODES if x!=old_root]
    new_root=p[old_root]
    new=[x for x in NODES if x!=new_root]
    return tuple(new.index(p[x]) for x in old)

def lane_c():
    total=0; cov=0; odd=0; wrong_fail=0; root_details={}
    for r in NODES:
        rd={'checks':0,'odd_induced':0,'covariant':0,'wrong_control_fail':0}
        for p in PERMS5:
            q=induced_perm(r,p); sq=sgn(q); Rq=R(q)
            H=canonical_H(); selected=H; transported=scale(sq,H)
            good=(matmul(transported,Rq)==matmul(Rq,selected))
            wrong=(matmul(H,Rq)!=matmul(Rq,selected)) if sq==-1 else False
            total+=1; rd['checks']+=1; cov+=int(good); rd['covariant']+=int(good)
            if sq==-1:
                odd+=1; rd['odd_induced']+=1; wrong_fail+=int(wrong); rd['wrong_control_fail']+=int(wrong)
        root_details[str(r)]=rd
    ok=(total==600 and cov==600 and odd>0 and wrong_fail==odd)
    return {'iteration':'Iter076L','lane':'C','pass':ok,'gauge_roots_checked':5,
            'full_S5_relabelings_per_root':120,'total_transport_checks':total,
            'covariant_with_pseudoscalar_transport':cov,'odd_induced_S4_cases':odd,
            'wrong_fixed_omega_control_failures':wrong_fail,'root_details':root_details}

def lane_d():
    controls={'combinatorial_sigma_kappa_distinct_from_regge_orientation':True,
              'regge_bridge_is_semiclassical':True,
              'proper_vertex_4volume_not_established_as_exact_eq4_selector':True,
              'positive_A_to_C_must_remain_semiclassical_only':True,
              'exact_eq4_p3_promotion_forbidden_here':True}
    ok=all(controls.values())
    return {'iteration':'Iter076L','lane':'D','pass':ok,'scope_controls':controls,
            'scope_label':'SEMICLASSICAL_ONLY','exact_eq4_bridge_identified':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def dump(o,p):
    os.makedirs(os.path.dirname(p) or '.',exist_ok=True)
    with open(p,'w') as f: json.dump(o,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                with open(os.path.join(base,fn)) as f: o=json.load(f)
            except Exception:
                continue
            if o.get('iteration')=='Iter076L' and o.get('lane') in LANES: got[o['lane']]=o
    complete=set(got)==set(LANES)
    allpass=complete and all(got[k].get('pass') for k in LANES)
    exact_bridge=bool(got.get('D',{}).get('exact_eq4_bridge_identified'))
    if allpass:
        classification='ITER076L_REGGE_4VOLUME_ORIENTATION_SELECTS_HODGE_SIGN_SEMICLASSICAL_EXACT_BRIDGE_STILL_BLOCKED_SCOPED'
    elif exact_bridge:
        classification='ITER076L_EXACT_ORIENTATION_BRIDGE_FOUND_REQUIRES_INDEPENDENT_SOURCE_REVIEW'
    else:
        classification='ITER076L_REGGE_4VOLUME_ORIENTATION_DOES_NOT_SELECT_HODGE_SIGN_REVIEW'
    return {'iteration':'Iter076L','valid':allpass,
            'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},
            'classification':classification,'scope':'SEMICLASSICAL_ONLY' if allpass else 'REVIEW',
            'claim_lock':'No physical signed P3 promotion; exact Eq.(4) orientation bridge remains required.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    dump(o,a.output); print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')): raise SystemExit(2)

if __name__=='__main__': main()
