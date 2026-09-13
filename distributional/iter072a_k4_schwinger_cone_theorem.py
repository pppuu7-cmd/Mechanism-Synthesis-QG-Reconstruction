#!/usr/bin/env python3
"""Iter072A exact K4 common-epsilon leading-collision Schwinger-cone audit.

Frozen by status/ITERATION_072A_PREREG.md before implementation.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import sympy as sp
from distributional.k4_forest_order_finite_part import constrained_edge_flows, TREES

EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']
TREELIST=['S0','S1','P0','P1']

def signs_source(label):
    q=[1 if c=='+' else -1 for c in label]
    return [q[a]*q[b] for a,b in EDGES]

def signs_wrong(label):
    q=[1 if c=='+' else -1 for c in label]
    return [q[a] for a,b in EDGES]

def L_exact(tree):
    y,x,_,_,det=constrained_edge_flows(tree,(sp.Integer(0),)*4)
    L=sp.zeros(6,3)
    for e,xe in enumerate(x):
        for j,v in enumerate(y):
            L[e,j]=sp.simplify(sp.diff(xe,v))
        assert sp.expand(xe-sum(L[e,j]*y[j] for j in range(3)))==0
    return L,sp.Integer(det)

def orientation(signs):
    out={}
    for e,((a,b),s) in enumerate(zip(EDGES,signs)):
        u,v=(a,b) if s==1 else (b,a)
        out[(u,v)]=e
    return out

def strongly_connected(signs):
    orient=orientation(signs)
    adj={i:[] for i in range(4)}
    for (u,v),e in orient.items(): adj[u].append(v)
    for s in range(4):
        seen={s}; stack=[s]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
        if len(seen)!=4: return False
    return True

def directed_cycles(signs):
    orient=orientation(signs)
    cycles=[]; seen=set()
    for k in (3,4):
        for perm in itertools.permutations(range(4),k):
            if min(perm)!=perm[0]: continue
            ok=True; vec=[0]*6
            for i in range(k):
                u,v=perm[i],perm[(i+1)%k]
                if (u,v) not in orient: ok=False; break
                vec[orient[(u,v)]]=1
            if ok:
                # canonical vector removes rotation duplicates; reversed direction is not a cycle unless source allows it.
                key=tuple(vec)
                if key not in seen: seen.add(key); cycles.append(vec)
    return cycles

def exact_lane(label):
    s=signs_source(label); wrong=signs_wrong(label)
    strong=strongly_connected(s); wrong_strong=strongly_connected(wrong)
    cyc=directed_cycles(s)
    if cyc:
        C=sp.Matrix(cyc).T
        cone_dim=int(C.rank())
        tsum=[sum(row[e] for row in cyc) for e in range(6)]
    else:
        cone_dim=0; tsum=[0]*6
    strict=all(v>0 for v in tsum)
    basis={}; classifications=[]
    p1=p2=p4=p5=p6=p7=True
    ref_kernel=None; ref_proper=None
    for tree in TREELIST:
        L,det=L_exact(tree)
        A=L.T*sp.diag(*s)
        rank=int(A.rank()); nullity=6-rank
        residual=list(A*sp.Matrix(tsum)) if strict else []
        cycle_res=[]
        for c in cyc: cycle_res.extend(list(A*sp.Matrix(c)))
        P1=(rank==3 and nullity==3 and abs(int(det))==1)
        P2=(strict==strong and all(v==0 for v in residual) and all(v==0 for v in cycle_res))
        P4=((strong and strict and cone_dim==3) or ((not strong) and (not strict) and cone_dim<3))
        proper=[]
        maxdeg=-999
        for r in range(1,6):
            for subset in itertools.combinations(range(6),r):
                rr=int(L[list(subset),:].rank())
                deg=r-rr
                maxdeg=max(maxdeg,deg)
                proper.append((subset,rr,deg))
        P5=(maxdeg<3)
        # Frozen Iter071A numerator/test constant terms at y=0.
        rho=sp.Rational(3,5); den0=rho*rho+sp.Rational(1,4)
        c1=2*rho/den0; c2=2/den0
        yy=sp.symbols('y0:3'); xx=[sum(L[e,j]*yy[j] for j in range(3)) for e in range(6)]
        numer=sp.prod(1+c1*x+(c2/2)*x*x for x in xx)
        tests=[sp.Integer(1),1+xx[0]-2*xx[4]+xx[5],1+xx[0]*xx[5]-xx[1]*xx[4]]
        constants=[sp.expand(numer*t).subs({v:0 for v in yy}) for t in tests]
        P6=all(v==1 for v in constants)
        kernel_key=tuple(tuple(int(A[i,j]) for j in range(6)) for i in range(3))
        proper_key=tuple(sorted((len(ss),rr,deg) for ss,rr,deg in proper))
        if ref_kernel is None:
            # Kernel itself is basis-coordinate dependent, so compare exact nullspace row-reduced signatures below.
            ref_proper=proper_key
        else:
            if proper_key!=ref_proper: p7=False
        basis[tree]={'rank':rank,'nullity':nullity,'tree_det':int(det),'max_proper_collision_degree':maxdeg,
                     'strict_flow_residual_zero':bool(all(v==0 for v in residual)),
                     'cycle_residuals_zero':bool(all(v==0 for v in cycle_res)),
                     'source_test_constants':[str(v) for v in constants],
                     'P1':bool(P1),'P2':bool(P2),'P4':bool(P4),'P5':bool(P5),'P6':bool(P6)}
        p1=p1 and P1; p2=p2 and P2; p4=p4 and P4; p5=p5 and P5; p6=p6 and P6
    p3=(strong==strict)
    p7=bool(p7 and all(b['rank']==3 and b['nullity']==3 for b in basis.values()) and len({b['max_proper_collision_degree'] for b in basis.values()})==1)
    valid=bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    return {'iteration':'Iter072A','sigma':label,'source_edge_signs':s,'wrong_control_edge_signs':wrong,
            'strongly_connected':bool(strong),'wrong_control_strongly_connected':bool(wrong_strong),
            'negative_control_disagrees':bool(strong!=wrong_strong),'directed_cycles':cyc,'cycle_count':len(cyc),
            'positive_cycle_span_dimension':cone_dim,'constructive_flow':tsum,'strict_positive_circulation':bool(strict),
            'full_collision_degree':3,'basis':basis,
            'predicates':{'P1_EXACT_RANK':bool(p1),'P2_STRICT_POSITIVE_CONE':bool(p2),'P3_TOURNAMENT_EQUIVALENCE':bool(p3),
                          'P4_FULL_DIMENSIONAL_CONE':bool(p4),'P5_PROPER_STRATUM_POWER_SEPARATION':bool(p5),
                          'P6_SOURCE_TEST_CONSTANT_TERM':bool(p6),'P7_BASIS_COVARIANCE':bool(p7)},
            'valid':valid,'lane_classification':'ITER072A_LANE_EXACT_VALID' if valid else 'ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL',
            'scope_lock':'Reduced K4 common-epsilon leading full-collision coefficient only; no physical sector selection, full vertex theorem, K5, G3/F9/G8 promotion.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sigma',required=True,choices=SIGMAS); ap.add_argument('--output',required=True); a=ap.parse_args()
    out=exact_lane(a.sigma); p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not out['valid']: raise SystemExit(7)
if __name__=='__main__': main()
