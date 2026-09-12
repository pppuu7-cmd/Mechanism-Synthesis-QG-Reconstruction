#!/usr/bin/env python3
"""Iter029B: enumerate maximal transverse edge subsets of K_n.

A subset is transverse iff the reduced incidence rows are independent.  For a
connected graph this is exactly a forest; maximal connected transverse subsets
are spanning trees.  We enumerate all subsets for n<=5 to obtain an exact,
independent combinatorial control on how many redundant boundary constraints
must be removed from the complete graph before the naive product criterion can
hold.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import sympy as sp


def edges_complete(n): return [(i,j) for i in range(n) for j in range(i+1,n)]

def Bred(n,edges):
    rows=[]
    for i,j in edges:
        r=[0]*n; r[i]=1; r[j]=-1; rows.append(r[:-1])
    return sp.Matrix(rows) if rows else sp.zeros(0,n-1)

def connected(n,edges):
    adj=[set() for _ in range(n)]
    for i,j in edges: adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); stack.append(v)
    return len(seen)==n

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--n',type=int,required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); n=a.n; E=edges_complete(n); m=len(E)
    transverse_by_size={}; connected_transverse_by_size={}
    for r in range(m+1):
        t=ct=0
        for idx in itertools.combinations(range(m),r):
            es=[E[i] for i in idx]
            independent=(Bred(n,es).rank()==r)
            if independent:
                t+=1
                if r and connected(n,es): ct+=1
        transverse_by_size[str(r)]=t
        connected_transverse_by_size[str(r)]=ct
    max_trans=max(int(k) for k,v in transverse_by_size.items() if v)
    spanning_trees=connected_transverse_by_size.get(str(n-1),0)
    out={
      'iteration':'029B','n':n,'complete_edges':m,'complete_cycle_nullity':m-(n-1),
      'max_transverse_edges':max_trans,'minimum_edges_to_remove_for_transversality':m-max_trans,
      'spanning_tree_count_enumerated':spanning_trees,'cayley_expected':n**(n-2),
      'transverse_subsets_by_size':transverse_by_size,
      'connected_transverse_subsets_by_size':connected_transverse_by_size,
      'matches_iter028_redundancy_exponent':(m-max_trans)==(m-(n-1)),
      'guardrail':'Choosing a spanning-tree subset only diagnoses redundancy. It is not a physical prescription for deleting wedges and does not define the full causal amplitude.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
