#!/usr/bin/env python3
"""Iter072B exact signed-cut-space Schwinger leading-coefficient audit."""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp
from distributional.k4_forest_order_finite_part import constrained_edge_flows,incidence
EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
TREES=['S0','S1','P0','P1']
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']

def q(label): return [1 if c=='+' else -1 for c in label]
def source_signs(label):
    z=q(label); return [z[a]*z[b] for a,b in EDGES]
def wrong_signs(label):
    z=q(label); return [z[a] for a,b in EDGES]
def directed(signs): return [(a,b) if s>0 else (b,a) for (a,b),s in zip(EDGES,signs)]
def topo(signs):
    ds=directed(signs); indeg=[0]*4; adj=[[] for _ in range(4)]
    for u,v in ds: adj[u].append(v); indeg[v]+=1
    avail=sorted(i for i in range(4) if indeg[i]==0); out=[]
    while avail:
        u=avail.pop(0); out.append(u)
        for v in sorted(adj[u]):
            indeg[v]-=1
            if indeg[v]==0: avail.append(v); avail.sort()
    return out if len(out)==4 else None

def score(signs):
    d=[0]*4
    for u,v in directed(signs): d[u]+=1
    return sorted(d,reverse=True)
def Lmat(tree):
    y,x,_,_,det=constrained_edge_flows(tree,(sp.Integer(0),)*4)
    L=sp.zeros(6,3)
    for e,xe in enumerate(x):
        for j,v in enumerate(y): L[e,j]=sp.diff(xe,v)
    return L,int(det)
def witness_from_order(order,signs):
    # earlier in topological order gets higher potential so canonical x=u_a-u_b has sign s.
    u=[0]*4
    for rank,v in enumerate(order): u[v]=3-rank
    B=incidence(); # B column has - at a,+ at b, so B^T u = u_b-u_a; use -B^T u = u_a-u_b.
    x=list(-B.T*sp.Matrix(u))
    t=[sp.Integer(signs[e])*x[e] for e in range(6)]
    return u,x,t

def any_order_realizes(signs):
    for order in itertools.permutations(range(4)):
        u,x,t=witness_from_order(order,signs)
        if all(v>0 for v in t): return list(order)
    return None

def lane(label):
    s=source_signs(label); ws=wrong_signs(label)
    order=topo(s); acyclic=order is not None; scores=score(s); transitive=(scores==[3,2,1,0])
    allorder=any_order_realizes(s); wrong_acyclic=topo(ws) is not None
    P2=(acyclic==transitive)
    P4=((allorder is not None)==acyclic)
    binfo={}; p1=p3=p5=p6=p7=p8=True; proper_ref=None
    for tr in TREES:
        L,det=Lmat(tr); A=L.T*sp.diag(*s); rankL=int(L.rank()); rankA=int(A.rank()); nullity=6-rankA
        P1=(rankL==3 and rankA==3 and nullity==3 and abs(det)==1)
        if acyclic:
            u,x,t=witness_from_order(order,s); res=list(A*sp.Matrix(t)); strict=all(v>0 for v in t)
            P3=(strict and all(v==0 for v in res))
        else:
            u=x=t=None; res=[]; P3=True
        P5=((acyclic and allorder is not None and nullity==3) or ((not acyclic) and allorder is None))
        maxdeg=-999; sig=[]
        for r in range(1,6):
            for ss in itertools.combinations(range(6),r):
                rr=int(L[list(ss),:].rank()); deg=r-rr; maxdeg=max(maxdeg,deg); sig.append((len(ss),rr,deg))
        P6=(maxdeg<3)
        yy=sp.symbols('y0:3'); xx=[sum(L[e,j]*yy[j] for j in range(3)) for e in range(6)]
        rho=sp.Rational(3,5); den0=rho*rho+sp.Rational(1,4); c1=2*rho/den0; c2=2/den0
        num=sp.prod(1+c1*z+(c2/2)*z*z for z in xx)
        tests=[1,1+xx[0]-2*xx[4]+xx[5],1+xx[0]*xx[5]-xx[1]*xx[4]]
        const=[sp.expand(num*g).subs({v:0 for v in yy}) for g in tests]; P7=all(v==1 for v in const)
        ps=tuple(sorted(sig))
        if proper_ref is None: proper_ref=ps
        elif ps!=proper_ref: p8=False
        binfo[tr]={'rank_L':rankL,'rank_A':rankA,'kernel_dim':nullity,'tree_det':det,'max_proper_degree':maxdeg,
                   'strict_witness_residual_zero':bool(all(v==0 for v in res)) if acyclic else None,'constants':[str(v) for v in const],
                   'P1':bool(P1),'P3':bool(P3),'P5':bool(P5),'P6':bool(P6),'P7':bool(P7)}
        p1&=P1; p3&=P3; p5&=P5; p6&=P6; p7&=P7
    p8=bool(p8 and len({(v['rank_A'],v['kernel_dim'],v['max_proper_degree']) for v in binfo.values()})==1)
    neg=(acyclic!=wrong_acyclic)
    valid=bool(p1 and P2 and p3 and P4 and p5 and p6 and p7 and p8)
    return {'iteration':'Iter072B','sigma':label,'source_signs':s,'acyclic':acyclic,'transitive':transitive,'score_sequence':scores,
            'topological_order':order,'independent_realizing_order':allorder,'wrong_control_acyclic':wrong_acyclic,'negative_control_disagrees':neg,
            'basis':binfo,'predicates':{'P1_EXACT_RANK':p1,'P2_ACYCLIC_IFF_TRANSITIVE':P2,'P3_CONSTRUCTIVE_CUT_WITNESS':p3,
            'P4_EXHAUSTIVE_ORDER_OBSTRUCTION':P4,'P5_RELATIVE_INTERIOR':p5,'P6_PROPER_STRATUM':p6,'P7_CONSTANT_TERMS':p7,'P8_BASIS_COVARIANCE':p8},
            'valid':valid,'classification':'ITER072B_LANE_VALID' if valid else 'ITER072B_SIGNED_CUTSPACE_THEOREM_FAIL'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sigma',choices=SIGMAS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    out=lane(a.sigma); p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not out['valid']: raise SystemExit(9)
if __name__=='__main__': main()
