#!/usr/bin/env python3
"""Iter073A exact K4 signed-cut-space proper-face atlas."""
from __future__ import annotations
import argparse,itertools,json
from collections import Counter
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
def Lmat(tree):
    y,x,_,_,det=constrained_edge_flows(tree,(sp.Integer(0),)*4)
    L=sp.zeros(6,3)
    for e,xe in enumerate(x):
        for j,v in enumerate(y): L[e,j]=sp.diff(xe,v)
    return L,int(det)

def weak_order_feasible(S,signs):
    S=set(S)
    for vals in itertools.product(range(4), repeat=4):
        if min(vals)!=0: continue
        ok=True
        for e,(a,b) in enumerate(EDGES):
            d=vals[a]-vals[b]
            if e in S:
                if signs[e]*d<=0: ok=False; break
            else:
                if d!=0: ok=False; break
        if ok: return True,list(vals)
    return False,None

def dag_feasible(S,signs):
    S=set(S); parent=list(range(4))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for e,(a,b) in enumerate(EDGES):
        if e not in S: union(a,b)
    for v in range(4): parent[v]=find(v)
    for e,(a,b) in enumerate(EDGES):
        if e in S and parent[a]==parent[b]: return False
    comps=sorted(set(parent)); idx={c:i for i,c in enumerate(comps)}
    adj=[set() for _ in comps]; indeg=[0]*len(comps)
    for e,(a,b) in enumerate(EDGES):
        if e not in S: continue
        u,v=(a,b) if signs[e]>0 else (b,a)
        cu,cv=idx[parent[u]],idx[parent[v]]
        if cv not in adj[cu]: adj[cu].add(cv); indeg[cv]+=1
    avail=[i for i,d in enumerate(indeg) if d==0]; seen=0
    while avail:
        u=avail.pop(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: avail.append(v)
    return seen==len(comps)

def topo_full(signs):
    return dag_feasible(range(6),signs)

def permuted(signs,perm):
    edge_index={tuple(sorted(e)):i for i,e in enumerate(EDGES)}
    out=[0]*6
    for e,(a,b) in enumerate(EDGES):
        aa,bb=perm[a],perm[b]
        ee=edge_index[tuple(sorted((aa,bb)))]
        orient=1 if aa<bb else -1
        out[ee]=signs[e]*orient
    return out

def atlas(signs,L):
    faces=[]
    for m in range(1,6):
        for S in itertools.combinations(range(6),m):
            A=L[list(S),:].T*sp.diag(*[signs[e] for e in S])
            rank=int(A.rank()); nu=m-rank
            fa,vals=weak_order_feasible(S,signs); fb=dag_feasible(S,signs)
            faces.append({'S':list(S),'m':m,'rank':rank,'nu':nu,'A':fa,'B':fb,'witness':vals})
    return faces

def hist(faces):
    c=Counter((f['m'],f['nu']) for f in faces if f['A'])
    return {f'{m}:{nu}':n for (m,nu),n in sorted(c.items())}

def graph_hist(signs):
    c=Counter(); mx=-1
    for m in range(1,6):
        for S in itertools.combinations(range(6),m):
            if dag_feasible(S,signs):
                # rank/nullity is matroidal; use canonical S0 only for the independent S4 count audit.
                L,_=Lmat('S0'); A=L[list(S),:].T*sp.diag(*[signs[e] for e in S]); nu=m-int(A.rank())
                c[(m,nu)]+=1; mx=max(mx,nu)
    return {f'{m}:{nu}':n for (m,nu),n in sorted(c.items())},mx

def lane(label):
    signs=source_signs(label); wrong=wrong_signs(label)
    basis={}; ref=None; p1=p2=p3=p4=True
    for tr in TREES:
        L,det=Lmat(tr); faces=atlas(signs,L)
        P2=all(f['A']==f['B'] for f in faces)
        P3=all((not f['A']) or f['nu']>=1 for f in faces)
        h=hist(faces); mx=max([f['nu'] for f in faces if f['A']], default=-1)
        sig=tuple((tuple(f['S']),f['rank'],f['nu']) for f in faces)
        if ref is None: ref=(sig,h,mx)
        else: p1 &= (sig==ref[0]); p4 &= (h==ref[1] and mx==ref[2])
        basis[tr]={'tree_det':det,'feasible_faces':sum(1 for f in faces if f['A']),'max_feasible_proper_nullity':mx,'histogram':h,
                   'P2_routes_agree':P2,'P3_feasible_has_positive_nullity':P3}
        p2 &= P2; p3 &= P3
    # Full-set Iter072B cross-check.
    L0,_=Lmat('S0'); Afull=L0.T*sp.diag(*signs); full_nu=6-int(Afull.rank()); full_feasible=dag_feasible(range(6),signs)
    scores=[0]*4
    for (a,b),s in zip(EDGES,signs): scores[a if s>0 else b]+=1
    transitive=(sorted(scores,reverse=True)==[3,2,1,0])
    p6=(full_nu==3 and full_feasible==transitive)
    yy=sp.symbols('y0:3'); xx=[sum(L0[e,j]*yy[j] for j in range(3)) for e in range(6)]
    rho=sp.Rational(3,5); den0=rho*rho+sp.Rational(1,4); c1=2*rho/den0; c2=2/den0
    num=sp.prod(1+c1*z+(c2/2)*z*z for z in xx); tests=[1,1+xx[0]-2*xx[4]+xx[5],1+xx[0]*xx[5]-xx[1]*xx[4]]
    const=[sp.expand(num*g).subs({v:0 for v in yy}) for g in tests]; p7=all(v==1 for v in const)
    # S4 histogram invariance under relabelling.
    h0,m0=graph_hist(signs); p5=True
    for perm in itertools.permutations(range(4)):
        hp,mp=graph_hist(permuted(signs,perm))
        if hp!=h0 or mp!=m0: p5=False; break
    hw,mw=graph_hist(wrong); neg=(hw!=h0 or mw!=m0 or dag_feasible(range(6),wrong)!=full_feasible)
    valid=bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    return {'iteration':'Iter073A','sigma':label,'source_signs':signs,'basis':basis,
            'max_feasible_proper_nullity':ref[2],'proper_histogram':ref[1],
            'full_set':{'nullity':full_nu,'positive_feasible':full_feasible,'transitive':transitive},
            'constants':[str(v) for v in const],'negative_control_disagrees':neg,
            'predicates':{'P1_BASIS_EXACT_RANK_NULLITY':p1,'P2_TWO_ROUTES_AGREE':p2,'P3_FEASIBLE_POSITIVE_NULLITY':p3,
                          'P4_ATLAS_BASIS_COVARIANT':p4,'P5_S4_HISTOGRAM_INVARIANT':p5,'P6_ITER072B_FULLSET_CROSSCHECK':p6,'P7_CONSTANT_TERMS':p7},
            'valid':valid,'classification':'ITER073A_LANE_VALID' if valid else 'ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_FAIL'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sigma',choices=SIGMAS,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    out=lane(a.sigma); p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not out['valid']: raise SystemExit(9)
if __name__=='__main__': main()
