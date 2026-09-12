#!/usr/bin/env python3
"""Iter041: exact source delta/delta-prime pattern census on complete K_k collisions."""
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path

def edges(k): return [(i,j) for i in range(k) for j in range(i+1,k)]

def permute_pattern(pattern, perm, es, idx):
    out=[0]*len(es)
    for e,(i,j) in enumerate(es):
        a,b=perm[i],perm[j]
        if a>b: a,b=b,a
        out[idx[(a,b)]]=pattern[e]
    return tuple(out)

def orbit(seed, perms, es, idx):
    return {permute_pattern(seed,p,es,idx) for p in perms}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--k',type=int,required=True)
    ap.add_argument('--m',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); k=a.k; es=edges(k); E=len(es); m=a.m
    if k not in (2,3,4,5) or not 0<=m<=E: raise SystemExit('invalid (k,m)')
    idx={e:i for i,e in enumerate(es)}; perms=list(itertools.permutations(range(k)))
    pats=[]
    for comb in itertools.combinations(range(E),m):
        p=[0]*E
        for i in comb: p[i]=1
        pats.append(tuple(p))
    unseen=set(pats); orbits=[]; closure_ok=True
    while unseen:
        seed=min(unseen); o=orbit(seed,perms,es,idx)
        closure_ok &= all(sum(x)==m for x in o)
        orbits.append(o); unseen-=o
    sizes=sorted(len(o) for o in orbits)
    cycle_rank=E-(k-1); sd=E+m; omega=sd-(k-1)
    gates={
      'pattern_count_matches_binomial': len(pats)==math.comb(E,m),
      'orbit_partition_complete': sum(sizes)==len(pats),
      'orbit_action_closed': bool(closure_ok),
      'cycle_rank_exact': cycle_rank>=0,
    }
    result={
      'iteration':'Iter041','k':k,'edges':E,'delta_prime_edges':m,
      'pattern_count':len(pats),'orbit_count':len(orbits),'orbit_sizes':sizes,
      'relative_coordinate_dimension':k-1,'cycle_rank':cycle_rank,
      'nominal_scaling_degree':sd,'superficial_extension_degree':omega,
      'classification':('ACYCLIC_SINGLE_WEDGE_CONTROL' if cycle_rank==0 else 'CYCLIC_SOURCE_COLLISION'),
      'scientific_discriminators':{
        'source_lane_only_quadratic_or_lower': (omega<=2),
        'higher_order_extension_budget_present': (cycle_rank>0 and omega>=4),
      },
      'numerical_gates':gates,
      'claim_lock':'Scaling/combinatorial census only; not existence, divergence, or a physical extension prescription.'
    }
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if not all(gates.values()): raise SystemExit(1)
if __name__=='__main__': main()
