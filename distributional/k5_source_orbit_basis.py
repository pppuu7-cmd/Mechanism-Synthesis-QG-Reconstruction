#!/usr/bin/env python3
"""Iter043B: resolve the j=1/2 square-free source span into S5 edge-subset orbits.

Iter042 found source-supported primitive ranks 3/3 at d=4 and 3/5 at d=6.
This script identifies which unlabeled K5 edge-subgraph orbit polynomials carry
that source span.  It is an algebraic compression for the next Feynman
coefficient-selection stage, not a physical extension prescription.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

from distributional.k5_extension_invariant_jet_audit import EDGES, cycle_basis, cycle_rep, inv_dim
from distributional.k5_appendixd_source_jet_span import compositions, normalized_rank, reynolds_monomial_matrix

N=5
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}


def permute_subset(subset,p):
    out=[]
    for ei in subset:
        a,b=EDGES[ei]; x,y=sorted((p[a],p[b])); out.append(EDGE_INDEX[(x,y)])
    return tuple(sorted(out))


def canonical_subset(subset,perms):
    return min(permute_subset(subset,p) for p in perms)


def orbit_partition(degree,perms):
    buckets={}
    for s in itertools.combinations(range(len(EDGES)),degree):
        c=canonical_subset(s,perms); buckets.setdefault(c,[]).append(s)
    return buckets


def graph_descriptor(rep):
    adj=[set() for _ in range(N)]
    for ei in rep:
        a,b=EDGES[ei]; adj[a].add(b); adj[b].add(a)
    deg=sorted((len(x) for x in adj),reverse=True)
    seen=set(); comps=[]
    for v in range(N):
        if v in seen: continue
        stack=[v]; seen.add(v); n=0
        while stack:
            u=stack.pop(); n+=1
            for w in adj[u]:
                if w not in seen: seen.add(w); stack.append(w)
        comps.append(n)
    triangles=0
    for a,b,c in itertools.combinations(range(N),3):
        if b in adj[a] and c in adj[a] and c in adj[b]: triangles+=1
    return {'degree_sequence':deg,'component_sizes':sorted(comps,reverse=True),'triangles':triangles}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--degree',type=int,required=True)
    ap.add_argument('--seed',type=int,required=True); ap.add_argument('--samples',type=int,default=192)
    ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); d=a.degree
    if d not in (4,6): raise SystemExit('Iter043B is frozen to degrees 4 and 6')
    q=cycle_basis(); perms=list(itertools.permutations(range(N)))
    reps={p:cycle_rep(p,q) for p in perms}; rstack=np.stack([reps[p] for p in perms])
    exact_d,_=inv_dim(perms,reps,d); exact_m,_=inv_dim(perms,reps,d-2)
    primitive_exact=exact_d-exact_m
    rng=np.random.default_rng(a.seed); x=rng.normal(size=(a.samples,6)); x/=np.linalg.norm(x,axis=1,keepdims=True)
    x*=rng.uniform(.65,1.35,size=(a.samples,1)); tx=np.einsum('gij,mj->gmi',rstack,x,optimize=True)
    lower=reynolds_monomial_matrix(tx,d-2); descendants=np.sum(x*x,axis=1)[:,None]*lower
    rank_desc=normalized_rank(descendants)
    lin=np.einsum('ei,gmi->gme',q,tx,optimize=True)
    buckets=orbit_partition(d,perms)
    rows=[]; cols=[]
    for rep,members in sorted(buckets.items()):
        vals=np.prod(lin[:,:,rep],axis=2).mean(axis=0)
        cols.append(vals)
        rows.append({'representative_edge_indices':list(rep),'representative_edges':[list(EDGES[i]) for i in rep],
                     'labeled_subset_count':len(members),**graph_descriptor(rep)})
    O=np.stack(cols,axis=1)
    rank_source=normalized_rank(O); rank_primitive=normalized_rank(np.concatenate([descendants,O],axis=1))-rank_desc
    # essential orbit: removing it lowers source primitive rank
    for j,row in enumerate(rows):
        keep=[k for k in range(O.shape[1]) if k!=j]
        r=(normalized_rank(np.concatenate([descendants,O[:,keep]],axis=1))-rank_desc) if keep else 0
        row['primitive_rank_without_orbit']=r; row['essential_for_full_source_rank']=(r<rank_primitive)
    # Minimal orbit subsets spanning the observed source primitive quotient.
    minimal=[]
    for r in range(1,min(rank_primitive+2,O.shape[1]+1)):
        for comb in itertools.combinations(range(O.shape[1]),r):
            rr=normalized_rank(np.concatenate([descendants,O[:,comb]],axis=1))-rank_desc
            if rr==rank_primitive: minimal.append(list(comb))
        if minimal: break
    out={'iteration':'Iter043B','degree':d,'seed':a.seed,'samples':a.samples,
         'orbit_count':len(rows),'exact_full_invariant_dimension':exact_d,
         'exact_descendant_dimension':exact_m,'exact_primitive_dimension':primitive_exact,
         'source_orbit_invariant_rank':rank_source,'source_primitive_rank':rank_primitive,
         'minimal_spanning_orbit_count':(len(minimal[0]) if minimal else None),
         'minimal_spanning_orbit_index_sets':minimal[:50],'orbits':rows,
         'classification':'SOURCE_ORBIT_BASIS_RESOLVED',
         'claim_lock':'Unlabeled-edge source-basis compression only; no distribution product, finite-part coefficient, counterterm, G3/F9/G8 claim.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('orbits','minimal_spanning_orbit_index_sets')},indent=2))
    if rank_primitive<=0 or rank_primitive>primitive_exact: raise SystemExit(7)

if __name__=='__main__': main()
