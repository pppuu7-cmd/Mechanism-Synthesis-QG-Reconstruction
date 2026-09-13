#!/usr/bin/env python3
import argparse, itertools, json, math, os
import sympy as sp

VERTS=range(4)
EDGES=[(i,j) for i in VERTS for j in VERTS if i<j]
EINDEX={e:k for k,e in enumerate(EDGES)}
PERMS=list(itertools.permutations(VERTS))

def parity_seq(seq):
    inv=sum(1 for i in range(len(seq)) for j in range(i+1,len(seq)) if seq[i]>seq[j])
    return -1 if inv%2 else 1

def parity(p): return parity_seq(p)

def incidence():
    B=sp.zeros(4,6)
    for k,(i,j) in enumerate(EDGES):
        B[i,k]=-1; B[j,k]=1
    return B

B=incidence()
CUT=sp.Matrix.hstack(*B.T.columnspace())
CYCLE=sp.Matrix.hstack(*B.nullspace())

def edge_action(p, signed=True):
    R=sp.zeros(6,6)
    for k,(i,j) in enumerate(EDGES):
        a,b=p[i],p[j]
        if a<b: e=(a,b); s=1
        else: e=(b,a); s=-1
        if not signed: s=1
        R[EINDEX[e],k]=s
    return R

def hodge(signless=False, flip_edge=None):
    H=sp.zeros(6,6)
    for k,(i,j) in enumerate(EDGES):
        comp=sorted(set(VERTS)-{i,j}); a,b=comp
        s=1 if signless else parity_seq((i,j,a,b))
        if flip_edge==(i,j): s=-s
        H[EINDEX[(a,b)],k]=s
    return H

H=hodge()

def coords(V,y):
    sol=V.gauss_jordan_solve(y)[0]
    if V*sol != y: raise ValueError('coordinate reconstruction failed')
    return sp.Matrix(sol)

def restricted(V,R):
    return sp.Matrix.hstack(*[coords(V,R*V[:,j]) for j in range(V.cols)])

def primitive(v):
    vals=[sp.Rational(x) for x in list(v)]
    den=sp.ilcm(*[x.q for x in vals]) if vals else 1
    ints=[int(x*den) for x in vals]
    g=0
    for x in ints: g=math.gcd(g,abs(x))
    if g: ints=[x//g for x in ints]
    first=next((x for x in ints if x),1)
    if first<0: ints=[-x for x in ints]
    return sp.Matrix(3,3,ints)

def intertwiner_generator():
    xs=sp.symbols('x0:9'); X=sp.Matrix(3,3,xs); eqs=[]
    for p in PERMS:
        R=edge_action(p,True); C=restricted(CUT,R); Z=restricted(CYCLE,R)
        eqs.extend(list(Z*X-parity(p)*(X*C)))
    A,_=sp.linear_eq_to_matrix(eqs,xs); ns=A.nullspace()
    return A,ns,(primitive(ns[0]) if len(ns)==1 else None)

def lane_a():
    nonzero_rows=[sum(1 for x in H.row(i) if x!=0) for i in range(6)]
    nonzero_cols=[sum(1 for x in H.col(i) if x!=0) for i in range(6)]
    hcut=H*CUT; hcycle=H*CYCLE
    cut_to_cycle=(B*hcut==sp.zeros(4,3)) and hcut.rank()==3
    cycle_to_cut=all((CUT*coords(CUT,hcycle[:,j])==hcycle[:,j]) for j in range(3)) and hcycle.rank()==3
    ok=(nonzero_rows==[1]*6 and nonzero_cols==[1]*6 and H.T*H==sp.eye(6) and H*H==sp.eye(6) and cut_to_cycle and cycle_to_cut)
    return {'iteration':'Iter076H','lane':'A','valid':bool(ok),'H':[list(map(int,H.row(i))) for i in range(6)],'predicates':{'signed_permutation_matrix':nonzero_rows==[1]*6 and nonzero_cols==[1]*6,'orthogonal_exact':H.T*H==sp.eye(6),'involution_exact':H*H==sp.eye(6),'cut_to_cycle_rank3':bool(cut_to_cycle),'cycle_to_cut_rank3':bool(cycle_to_cut)}}

def lane_b():
    XH=sp.Matrix.hstack(*[coords(CYCLE,H*CUT[:,j]) for j in range(3)])
    A,ns,XF=intertwiner_generator()
    eq=(XF is not None and (XH==XF or XH==-XF))
    ok=(len(ns)==1 and XH.det()!=0 and eq)
    return {'iteration':'Iter076H','lane':'B','valid':bool(ok),'twisted_system_rank':int(A.rank()),'twisted_hom_dimension':len(ns),'X_H':[list(map(int,XH.row(i))) for i in range(3)],'X_F':([list(map(int,XF.row(i))) for i in range(3)] if XF is not None else None),'match_up_to_global_sign':bool(eq),'det_X_H':int(XH.det())}

def lane_c():
    failures=[]
    for p in PERMS:
        R=edge_action(p,True)
        if H*R != parity(p)*(R*H): failures.append(list(p))
    comp_fail=[]
    for p in PERMS:
        Rp=edge_action(p,True)
        for q in PERMS:
            Rq=edge_action(q,True)
            r=tuple(p[q[i]] for i in VERTS); Rr=edge_action(r,True)
            if Rr != Rp*Rq: comp_fail.append([list(p),list(q)])
    ok=not failures and not comp_fail
    return {'iteration':'Iter076H','lane':'C','valid':bool(ok),'permutations':24,'ordered_pairs':576,'twisted_covariance_failures':len(failures),'representation_composition_failures':len(comp_fail)}

def twisted_cov_ok(M):
    return all(M*edge_action(p,True)==parity(p)*(edge_action(p,True)*M) for p in PERMS)

def transports_cut_cycle(M):
    try:
        return all(B*(M*CUT[:,j])==sp.zeros(4,1) for j in range(3)) and all(CUT*coords(CUT,M*CYCLE[:,j])==M*CYCLE[:,j] for j in range(3))
    except Exception:
        return False

def lane_d():
    Hblind=hodge(signless=True)
    blind_cov=twisted_cov_ok(Hblind)
    bad=[]
    for e in EDGES:
        M=hodge(False,e)
        bad.append({'edge':e,'involution':bool(M*M==sp.eye(6)),'cut_cycle_transport':bool(transports_cut_cycle(M)),'twisted_covariance':bool(twisted_cov_ok(M))})
    all_rejected=all(not (x['involution'] and x['cut_cycle_transport'] and x['twisted_covariance']) for x in bad)
    ok=(not blind_cov and all_rejected)
    return {'iteration':'Iter076H','lane':'D','valid':bool(ok),'orientation_blind_twisted_covariance':bool(blind_cov),'single_sign_flip_controls':bad,'all_single_flip_controls_rejected':bool(all_rejected),'fitted_entries_used':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def write(obj,path):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w',encoding='utf-8') as f: json.dump(obj,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                with open(os.path.join(base,fn),encoding='utf-8') as f: obj=json.load(f)
            except Exception: continue
            if obj.get('lane') in LANES: got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(bool(got[k].get('valid')) for k in LANES)
    cls='ITER076H_CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED' if valid else 'ITER076H_CANONICAL_HODGE_IDENTIFICATION_FAILS_FROZEN_GATE'
    return {'iteration':'Iter076H','valid':bool(valid),'classification':cls,'lanes_found':sorted(got),'lane_valid':{k:bool(got.get(k,{}).get('valid')) for k in LANES},'claim_lock':'Canonical algebraic Hodge realization only; source selection of Hodge/P3 is not established.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=sorted(LANES)); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    write(obj,a.output); print(json.dumps(obj,indent=2,sort_keys=True))
    if a.lane and not obj['valid']: raise SystemExit(2)
    if a.aggregate_dir and not obj['valid']: raise SystemExit(2)

if __name__=='__main__': main()
