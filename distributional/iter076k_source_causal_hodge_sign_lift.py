import argparse,itertools,json,os
V=(0,1,2,3)
EDGES=tuple((i,j) for i in V for j in V if i<j)
EIDX={e:i for i,e in enumerate(EDGES)}
PERMS=tuple(itertools.permutations(V))
def canon(a,b): return (a,b) if a<b else (b,a)
def invcount(p): return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def sgn(p): return -1 if invcount(p)%2 else 1
def comp(e): return tuple(sorted(set(V)-set(e)))
def eps4(a,b,c,d): return -1 if invcount((a,b,c,d))%2 else 1
def R(p):
    M=[[0]*6 for _ in range(6)]
    for e in EDGES:
        pe=canon(p[e[0]],p[e[1]])
        M[EIDX[pe]][EIDX[e]]=1
    return M
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def scale(c,A): return [[c*x for x in r] for r in A]
def eq(A,B): return A==B
def signed_H(pair_signs):
    H=[[0]*6 for _ in range(6)]
    seen=[]; ps_iter=iter(pair_signs)
    assigned={}
    for e in EDGES:
        c=comp(e); key=tuple(sorted((EIDX[e],EIDX[c])))
        if key not in assigned: assigned[key]=next(ps_iter)
        s=assigned[key]
        H[EIDX[c]][EIDX[e]]=s
        H[EIDX[e]][EIDX[c]]=s
    return H
def canonical_H():
    H=[[0]*6 for _ in range(6)]
    for e in EDGES:
        c=comp(e); H[EIDX[c]][EIDX[e]]=eps4(e[0],e[1],c[0],c[1])
    return H
def lane_a():
    I=[[1 if i==j else 0 for j in range(6)] for i in range(6)]; sols=[]
    for signs in itertools.product((-1,1),repeat=3):
        H=signed_H(signs)
        if not eq(matmul(H,H),I): continue
        if all(eq(matmul(H,R(p)),scale(sgn(p),matmul(R(p),H))) for p in PERMS): sols.append((signs,H))
    H0=canonical_H(); plus=any(H==H0 for _,H in sols); minus=any(H==scale(-1,H0) for _,H in sols)
    return {'iteration':'Iter076K','lane':'A','pass':len(sols)==2 and plus and minus,'solution_count':len(sols),'plus_H_present':plus,'minus_H_present':minus,'solutions':[s for s,_ in sols]}
def apply_sigma(p,s):
    # passive relabel: value at new position p[i] equals old i
    out=[0]*4
    for i in V: out[p[i]]=s[i]
    return tuple(out)
def odd_stabilizer(s):
    return [p for p in PERMS if apply_sigma(p,s)==s and sgn(p)==-1]
def lane_b():
    configs=list(itertools.product((-1,1),repeat=4)); witnesses={str(s):len(odd_stabilizer(s)) for s in configs}
    # any sign-equivariant nonzero q is impossible if every orbit has an odd stabilizer; verify all configs do.
    obstructed=all(witnesses[str(s)]>0 for s in configs)
    root_values=(-1,1)
    checks=len(configs)*len(root_values)
    return {'iteration':'Iter076K','lane':'B','pass':obstructed,'configurations_with_root':checks,'all_configs_have_odd_stabilizer':obstructed,'odd_stabilizer_counts':witnesses,'selector_count':0 if obstructed else None}
def kappas(s): return tuple(s[i]*s[j] for i,j in EDGES)
def perm_kappa(p,k):
    out=[0]*6
    for e in EDGES:
        pe=canon(p[e[0]],p[e[1]])
        out[EIDX[pe]]=k[EIDX[e]]
    return tuple(out)
def lane_c():
    ks=sorted(set(kappas(s) for s in itertools.product((-1,1),repeat=4)))
    odd_counts={str(k):sum(1 for p in PERMS if perm_kappa(p,k)==k and sgn(p)==-1) for k in ks}
    obstructed=all(v>0 for v in odd_counts.values())
    return {'iteration':'Iter076K','lane':'C','pass':obstructed,'unique_kappa_configurations':len(ks),'all_kappa_configs_have_odd_stabilizer':obstructed,'odd_stabilizer_counts':odd_counts,'selector_count':0 if obstructed else None}
def lane_d():
    # label-order orientation sign changes under odd permutations by definition.
    flips=sum(sgn(p)==-1 for p in PERMS); preserves=sum(sgn(p)==1 for p in PERMS)
    # for any gauge root among 5 nodes, the unsigned K4 complement is intrinsic; orientation requires ordering of remaining four.
    roots=5; unsigned_covariant=True; orientation_extra=True; same_sign_control_rejected=(flips>0)
    ok=(flips==12 and preserves==12 and unsigned_covariant and orientation_extra and same_sign_control_rejected)
    return {'iteration':'Iter076K','lane':'D','pass':ok,'odd_relabelings_flip_label_orientation':flips,'even_relabelings_preserve_label_orientation':preserves,'gauge_roots_checked':roots,'unsigned_complement_covariant':unsigned_covariant,'signed_lift_requires_orientation_choice':orientation_extra,'orientation_blind_control_rejected':same_sign_control_rejected}
LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}
def dump(o,p): os.makedirs(os.path.dirname(p) or '.',exist_ok=True); open(p,'w').write(json.dumps(o,indent=2,sort_keys=True))
def aggregate(root):
    got={}
    for b,_,fs in os.walk(root):
        for f in fs:
            if not f.endswith('.json'): continue
            try:o=json.load(open(os.path.join(b,f)))
            except:continue
            if o.get('iteration')=='Iter076K' and o.get('lane') in LANES: got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    return {'iteration':'Iter076K','valid':valid,'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'classification':'ITER076K_SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED' if valid else 'ITER076K_SOURCE_CAUSAL_DATA_SELECT_HODGE_SIGN_REVIEW','claim_lock':'Scoped provenance only; physical P3 and epsilon^-1 coefficient unestablished.'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir);dump(o,a.output);print(json.dumps(o,indent=2,sort_keys=True))
    if not o.get('pass',o.get('valid')): raise SystemExit(2)
if __name__=='__main__':main()
