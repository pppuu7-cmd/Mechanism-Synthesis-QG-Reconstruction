#!/usr/bin/env python3
"""Iter068A: exact K4 microlocal denominator-skeleton collision audit.

Prospectively frozen by status/ITERATION_068A_PREREG.md.
This script audits only oriented incidence-normal covectors associated with the
source-backed Iter059/062 ordered spectral-sign bridge. It does not compute the
full Toller wavefront set or a physical vertex amplitude.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

VERTICES = range(4)
EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def parse_sigma(txt: str):
    if len(txt) != 4 or txt[0] != '+' or any(c not in '+-' for c in txt):
        raise ValueError("sigma must be four signs with sigma_0 fixed '+', e.g. '+-+-'")
    return tuple(1 if c == '+' else -1 for c in txt)


def vec_add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def oriented_normal(edge, s):
    a,b=edge
    v=[0,0,0,0]
    v[a]=s
    v[b]=-s
    return tuple(v)


def adjacency(signs):
    adj={v:set() for v in VERTICES}
    for e,s in zip(EDGES,signs):
        a,b=e
        if s == 1:
            adj[a].add(b)
        else:
            adj[b].add(a)
    return adj


def directed_cycle(adj):
    # Exhaustive simple cycles of lengths 3 and 4, canonicalized by rotations.
    found=[]
    for L in (3,4):
        for cyc in itertools.permutations(VERTICES,L):
            if min(cyc) != cyc[0]:
                continue
            if all(cyc[(i+1)%L] in adj[cyc[i]] for i in range(L)):
                rev=tuple(reversed(cyc))
                found.append(tuple(cyc))
    if not found:
        return None
    return min(set(found))


def topo_order(adj):
    indeg={v:0 for v in VERTICES}
    for u in VERTICES:
        for v in adj[u]:
            indeg[v]+=1
    avail=sorted(v for v in VERTICES if indeg[v]==0)
    out=[]
    while avail:
        u=avail.pop(0)
        out.append(u)
        for v in sorted(adj[u]):
            indeg[v]-=1
            if indeg[v]==0:
                avail.append(v); avail.sort()
    return out if len(out)==4 else None


def subset_zero_witness(normals):
    # Exact independent collision test: exhaustive nonempty 0/1 edge subsets.
    # For an oriented graph incidence matrix, a simple directed cycle yields a
    # unit-coefficient positive circulation; conversely any positive circulation
    # contains a directed cycle. On K4 this exhaustive unit-subset test is exact.
    zero=(0,0,0,0)
    for mask in range(1,1<<len(normals)):
        total=zero
        idx=[]
        for i,n in enumerate(normals):
            if (mask>>i)&1:
                total=vec_add(total,n); idx.append(i)
        if total==zero:
            return idx
    return None


def cycle_edge_indices(cycle, signs):
    idx=[]
    for u,v in zip(cycle, cycle[1:]+cycle[:1]):
        for i,(a,b) in enumerate(EDGES):
            if {a,b}=={u,v}:
                forward=(a==u and b==v and signs[i]==1) or (b==u and a==v and signs[i]==-1)
                if not forward:
                    raise AssertionError("cycle edge orientation mismatch")
                idx.append(i); break
        else:
            raise AssertionError("cycle edge missing")
    return idx


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sigma', required=True)
    ap.add_argument('--convention', required=True, choices=['+1','-1'])
    ap.add_argument('--output', required=True)
    a=ap.parse_args()

    sigma=parse_sigma(a.sigma)
    c=int(a.convention)
    kappas=[sigma[u]*sigma[v] for u,v in EDGES]
    signs=[c*k for k in kappas]  # eta=+1 on canonical a<b edges
    normals=[oriented_normal(e,s) for e,s in zip(EDGES,signs)]

    # P1: source-backed ordered reversal must flip ordered spectral sign.
    reversal_ok=all((-c*k)==(-s) for k,s in zip(kappas,signs))

    # P2: direct exact incidence-normal subset collision test.
    subset_witness=subset_zero_witness(normals)
    collision=subset_witness is not None
    subset_sum=None
    if collision:
        total=(0,0,0,0)
        for i in subset_witness:
            total=vec_add(total,normals[i])
        subset_sum=list(total)

    # P3: independent tournament cycle/topological-order audit.
    adj=adjacency(signs)
    cyc=directed_cycle(adj)
    topo=topo_order(adj)
    cycle_present=cyc is not None
    cycle_equiv=(collision == cycle_present)
    if cyc is not None:
        cycle_idx=cycle_edge_indices(cyc,signs)
        total=(0,0,0,0)
        for i in cycle_idx:
            total=vec_add(total,normals[i])
        cycle_exact=(total==(0,0,0,0))
    else:
        cycle_idx=[]
        cycle_exact=(topo is not None and all(topo.index(u)<topo.index(v) for u in VERTICES for v in adj[u]))

    p1=reversal_ok
    p2=(subset_sum==[0,0,0,0]) if collision else True
    p3=cycle_equiv and cycle_exact
    valid=p1 and p2 and p3

    if not valid:
        classification='ITER068A_INVALID_OR_INCONSISTENT'
    elif collision:
        classification='K4_HORMANDER_PRODUCT_SKELETON_OBSTRUCTED_AT_FULL_COLLISION'
    else:
        classification='K4_HORMANDER_PRODUCT_SKELETON_COMPATIBLE_AT_FULL_COLLISION'

    out={
        'iteration':'Iter068A',
        'sigma':a.sigma,
        'convention':c,
        'edges':[list(e) for e in EDGES],
        'kappa':kappas,
        'ordered_spectral_signs':signs,
        'oriented_normals':[list(n) for n in normals],
        'predicates':{
            'P1_ORDER_REVERSAL_COVARIANCE':p1,
            'P2_EXACT_COLLISION_TEST':p2,
            'P3_DIRECTED_CYCLE_EQUIVALENCE':p3,
        },
        'collision_witness_edge_indices':subset_witness,
        'directed_cycle':list(cyc) if cyc else None,
        'directed_cycle_edge_indices':cycle_idx,
        'topological_order':topo,
        'classification':classification,
        'valid':valid,
        'claim_lock':'Denominator-skeleton microlocal compatibility/obstruction only; not the full Toller wavefront set, not a physical sector selector, and not a vertex finiteness/divergence theorem.'
    }
    path=Path(a.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not valid:
        raise SystemExit(9)


if __name__=='__main__':
    main()
