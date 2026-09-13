#!/usr/bin/env python3
import argparse, itertools, json
from sympy import Matrix, zeros


def edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def incidence(n):
    es=edges(n); B=zeros(n,len(es))
    for k,(i,j) in enumerate(es):
        B[i,k]=1; B[j,k]=-1
    return Matrix(B), es


def reduced_incidence(n,root):
    B,es=incidence(n)
    rows=[i for i in range(n) if i!=root]
    return B[rows,:],es


def colspace_matrix(M):
    cols=M.columnspace()
    return Matrix.hstack(*cols) if cols else zeros(M.rows,0)


def nullspace_matrix(M):
    cols=M.nullspace()
    return Matrix.hstack(*cols) if cols else zeros(M.cols,0)


def intersection_dim(U,V):
    # dim(U cap V)=dim U + dim V - rank[U V]
    if U.cols==0 or V.cols==0: return 0
    return U.cols+V.cols-Matrix.hstack(U,V).rank()


def lane_a():
    roots=[]
    Bfull,es=incidence(5)
    cycle=nullspace_matrix(Bfull)
    for r in range(5):
        Br,_=reduced_incidence(5,r)
        cut=colspace_matrix(Br.T)
        # cycle constraints annihilate every source difference vector
        closure=(cycle.T*cut)==zeros(cycle.cols,cut.cols)
        roots.append({"root":r,"rank":Br.rank(),"cut_dim":cut.cols,"cycle_dim":cycle.cols,"cycle_closure_exact":bool(closure)})
    pred=all(x["rank"]==4 and x["cut_dim"]==4 and x["cycle_dim"]==6 and x["cycle_closure_exact"] for x in roots)
    return {"lane":"A","roots":roots,"predicates":{"all_roots_exact":pred},"valid":pred}


def k4_cycle_basis_maps():
    B,es=incidence(4)
    cyc=nullspace_matrix(B)
    return B,es,cyc


def lane_b():
    B,es,cyc=k4_cycle_basis_maps()
    roots=[]
    for r in range(4):
        Br,_=reduced_incidence(4,r)
        cut=colspace_matrix(Br.T)
        inter=intersection_dim(cut,cyc)
        cycle_constraint=(B*cyc)==zeros(4,cyc.cols)
        roots.append({"root":r,"rank":Br.rank(),"cut_dim":cut.cols,"cycle_dim":cyc.cols,"intersection_dim":inter,"cycle_constraint":bool(cycle_constraint)})
    pred=all(x["rank"]==3 and x["cut_dim"]==3 and x["cycle_dim"]==3 and x["intersection_dim"]==0 and x["cycle_constraint"] for x in roots)
    return {"lane":"B","roots":roots,"predicates":{"k4_cut_cycle_split_exact":pred},"valid":pred}


def lane_c():
    B5,_=incidence(5); B4,_=incidence(4)
    B5r,_=reduced_incidence(5,0); B4r,_=reduced_incidence(4,0)
    cut4=colspace_matrix(B4r.T); cyc4=nullspace_matrix(B4)
    dims={"k5_edges":10,"k5_source_rank":B5r.rank(),"k5_cycle_nullity":len(B5.nullspace()),"k4_edges":6,"k4_cut_dim":cut4.cols,"k4_cycle_dim":cyc4.cols,"k4_cut_cycle_intersection":intersection_dim(cut4,cyc4)}
    pred=(dims=={"k5_edges":10,"k5_source_rank":4,"k5_cycle_nullity":6,"k4_edges":6,"k4_cut_dim":3,"k4_cycle_dim":3,"k4_cut_cycle_intersection":0})
    return {"lane":"C","dimensions":dims,"classification_if_valid":"extra_map_required_not_defined","predicates":{"rank_and_subspace_mismatch_exact":pred},"valid":pred}


def permuted_incidence_rank(n,p):
    B,_=incidence(n)
    P=zeros(n,n)
    for i,j in enumerate(p): P[j,i]=1
    return (P*B).rank(), len((P*B).nullspace())


def lane_d():
    k5_ok=True
    for p in itertools.permutations(range(5)):
        rk,nu=permuted_incidence_rank(5,p)
        if rk!=4 or nu!=6: k5_ok=False; break
    k4_ok=True
    for p in itertools.permutations(range(4)):
        rk,nu=permuted_incidence_rank(4,p)
        if rk!=3 or nu!=3: k4_ok=False; break
    # negative control 1: source edge vector violating triangle closure
    B5,es5=incidence(5); cyc5=nullspace_matrix(B5)
    v=zeros(10,1); v[0,0]=1
    free_edge_rejected=(cyc5.T*v)!=zeros(cyc5.cols,1)
    # negative control 2: a cut vector is not a cycle vector
    B4,_=incidence(4); B4r,_=reduced_incidence(4,0)
    cutv=B4r.T[:,0]
    cut_as_cycle_rejected=(B4*cutv)!=zeros(4,1)
    pred=bool(k5_ok and k4_ok and free_edge_rejected and cut_as_cycle_rejected)
    return {"lane":"D","counts":{"k5_permutations":120,"k4_permutations":24},"predicates":{"k5_permutation_invariant":k5_ok,"k4_permutation_invariant":k4_ok,"free_edge_control_rejected":bool(free_edge_rejected),"cut_as_cycle_control_rejected":bool(cut_as_cycle_rejected)},"valid":pred}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD'),required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    out={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    out.update({"iteration":"Iter076E","claim_lock":"Structural tangent-space audit only; no physical pushforward/coefficient/finiteness theorem."})
    with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not out['valid']: raise SystemExit(2)
if __name__=='__main__': main()
