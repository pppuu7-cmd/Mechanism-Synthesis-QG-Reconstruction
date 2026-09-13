#!/usr/bin/env python3
import argparse, itertools, json, math
import sympy as sp

VERTS = range(4)
EDGES = [(i,j) for i in VERTS for j in VERTS if i<j]
EINDEX = {e:k for k,e in enumerate(EDGES)}


def incidence():
    B = sp.zeros(4,6)
    for k,(i,j) in enumerate(EDGES):
        B[i,k] = -1
        B[j,k] = 1
    return B

B = incidence()
CUT = sp.Matrix.hstack(*[v for v in B.T.columnspace()])
CYCLE = sp.Matrix.hstack(*B.nullspace())


def parity(p):
    inv = sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j])
    return -1 if inv % 2 else 1


def edge_action(p, canonical_sign=True):
    R = sp.zeros(6,6)
    for k,(i,j) in enumerate(EDGES):
        a,b = p[i], p[j]
        if a < b:
            e=(a,b); s=1
        else:
            e=(b,a); s=-1
        if not canonical_sign:
            s=1
        R[EINDEX[e],k] = s
    return R


def coordinates(V, y):
    sol = V.gauss_jordan_solve(y)[0]
    assert V*sol == y
    return sp.Matrix(sol)


def restricted_rep(V, R):
    cols=[]
    for j in range(V.cols):
        cols.append(coordinates(V, R*V[:,j]))
    return sp.Matrix.hstack(*cols)

PERMS = list(itertools.permutations(VERTS))
REPS=[]
for p in PERMS:
    R=edge_action(p, True)
    C=restricted_rep(CUT,R)
    Z=restricted_rep(CYCLE,R)
    REPS.append((p,parity(p),R,C,Z))


def cycle_type(p):
    seen=set(); lens=[]
    for i in VERTS:
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=p[j]
        lens.append(n)
    return tuple(sorted(lens, reverse=True))


def intertwiner_nullspace(twisted=False, reps=REPS):
    xs = sp.symbols('x0:9')
    X = sp.Matrix(3,3,xs)
    eqs=[]
    for p,sgn,R,C,Z in reps:
        M = Z*X - (sgn if twisted else 1)*(X*C)
        eqs.extend(list(M))
    A,_ = sp.linear_eq_to_matrix(eqs, xs)
    ns=A.nullspace()
    return A, ns


def primitive_matrix(v):
    vals=[sp.Rational(x) for x in list(v)]
    den=sp.ilcm(*[x.q for x in vals]) if vals else 1
    ints=[int(x*den) for x in vals]
    g=0
    for x in ints: g=math.gcd(g,abs(x))
    if g: ints=[x//g for x in ints]
    first=next((x for x in ints if x),1)
    if first<0: ints=[-x for x in ints]
    return sp.Matrix(3,3,ints)


def lane_a():
    inter = CUT.row_join(-CYCLE).nullspace()
    chars={}
    inv_ok=True
    for p,sgn,R,C,Z in REPS:
        typ=str(cycle_type(p))
        chars.setdefault(typ, {'cut':set(),'cycle':set(),'sign':set(),'count':0})
        chars[typ]['cut'].add(int(sp.trace(C)))
        chars[typ]['cycle'].add(int(sp.trace(Z)))
        chars[typ]['sign'].add(sgn)
        chars[typ]['count'] += 1
        inv_ok &= all((R*CUT[:,j]) in sp.Matrix.hstack(*CUT.columnspace()).columnspace() for j in range(CUT.cols))
        inv_ok &= all((R*CYCLE[:,j]) in sp.Matrix.hstack(*CYCLE.columnspace()).columnspace() for j in range(CYCLE.cols))
    # sympy membership above is brittle conceptually; exact coordinate construction already certified invariance.
    inv_ok = all(CUT*restricted_rep(CUT,R) == R*CUT and CYCLE*restricted_rep(CYCLE,R) == R*CYCLE for _,_,R,_,_ in REPS)
    simple={k:{'cut':sorted(v['cut']),'cycle':sorted(v['cycle']),'sign':sorted(v['sign']),'count':v['count']} for k,v in chars.items()}
    expected_cut={'(1, 1, 1, 1)':3,'(2, 1, 1)':1,'(2, 2)':-1,'(3, 1)':0,'(4,)':-1}
    expected_cycle={'(1, 1, 1, 1)':3,'(2, 1, 1)':-1,'(2, 2)':-1,'(3, 1)':0,'(4,)':1}
    char_ok=True
    for k,val in expected_cut.items(): char_ok &= simple[k]['cut']==[val]
    for k,val in expected_cycle.items(): char_ok &= simple[k]['cycle']==[val]
    return {'iteration':'Iter076F','lane':'A','valid':bool(inv_ok and char_ok),'dimensions':{'cut':CUT.rank(),'cycle':CYCLE.rank(),'intersection':len(inter)},'characters':simple,'predicates':{'dimensions_exact':CUT.rank()==3 and CYCLE.rank()==3 and len(inter)==0,'spaces_invariant':bool(inv_ok),'characters_standard_vs_sign_twist_exact':bool(char_ok)},'claim_lock':'Representation-theory structure only; no physical P3 map.'}


def lane_b():
    A0,n0=intertwiner_nullspace(False)
    A1,n1=intertwiner_nullspace(True)
    return {'iteration':'Iter076F','lane':'B','valid':len(n0)==0 and len(n1)==1,'ranks':{'untwisted_system':A0.rank(),'twisted_system':A1.rank()},'dimensions':{'untwisted_hom':len(n0),'sign_twisted_hom':len(n1)},'predicates':{'untwisted_hom_zero':len(n0)==0,'sign_twisted_hom_one':len(n1)==1},'claim_lock':'Representation-theory structure only; no physical P3 map.'}


def generator():
    _,ns=intertwiner_nullspace(True)
    if len(ns)!=1: return None
    return primitive_matrix(ns[0])


def lane_c():
    X=generator()
    if X is None:
        return {'iteration':'Iter076F','lane':'C','valid':False,'reason':'twisted_generator_not_unique'}
    twisted_ok=all(Z*X == sgn*(X*C) for p,sgn,R,C,Z in REPS)
    untwisted_fails_odd=any(sgn==-1 and Z*X != X*C for p,sgn,R,C,Z in REPS)
    return {'iteration':'Iter076F','lane':'C','valid':bool(X.det()!=0 and twisted_ok and untwisted_fails_odd),'generator':[list(map(int,X.row(i))) for i in range(3)],'determinant':int(X.det()),'predicates':{'generator_invertible':X.det()!=0,'twisted_covariance_all_24':bool(twisted_ok),'ordinary_covariance_rejected_on_odd':bool(untwisted_fails_odd)},'claim_lock':'Algebraic twisted isomorphism only; not source-derived physical P3.'}


def transform_reps(U,V):
    Ui=U.inv(); Vi=V.inv(); out=[]
    for p,sgn,R,C,Z in REPS:
        out.append((p,sgn,R,Ui*C*U,Vi*Z*V))
    return out


def lane_d():
    basis_pairs=[
        (sp.eye(3),sp.eye(3)),
        (sp.Matrix([[1,1,0],[0,1,0],[0,0,1]]),sp.Matrix([[1,0,1],[0,1,0],[0,0,1]])),
        (sp.Matrix([[0,1,0],[1,0,0],[0,0,-1]]),sp.Matrix([[1,0,0],[0,0,1],[0,-1,0]])),
    ]
    dims=[]
    basis_ok=True
    for U,V in basis_pairs:
        reps=transform_reps(U,V)
        d0=len(intertwiner_nullspace(False,reps)[1]); d1=len(intertwiner_nullspace(True,reps)[1])
        dims.append([d0,d1]); basis_ok &= (d0,d1)==(0,1)
    X=generator()
    ordinary_control_rejected = X is not None and any(sgn==-1 and Z*X != X*C for p,sgn,R,C,Z in REPS)
    # Wrong edge action without orientation signs should not preserve the signed incidence/cycle decomposition consistently.
    wrong_preserves=True
    for p in PERMS:
        Rw=edge_action(p,False)
        try:
            restricted_rep(CUT,Rw); restricted_rep(CYCLE,Rw)
        except Exception:
            wrong_preserves=False; break
    return {'iteration':'Iter076F','lane':'D','valid':bool(basis_ok and ordinary_control_rejected and not wrong_preserves),'basis_hom_dimensions':dims,'predicates':{'basis_covariant_dimensions':bool(basis_ok),'ordinary_intertwiner_control_rejected':bool(ordinary_control_rejected),'drop_reorientation_sign_control_rejected':bool(not wrong_preserves)},'claim_lock':'Basis/negative-control audit only; no physical P3 map.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD'),required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    data={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[args.lane]()
    with open(args.output,'w') as f: json.dump(data,f,indent=2,sort_keys=True)
    print(json.dumps(data,indent=2,sort_keys=True))
    if not data.get('valid',False): raise SystemExit(2)

if __name__=='__main__': main()
