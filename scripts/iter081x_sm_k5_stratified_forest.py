#!/usr/bin/env python3
"""Iter081X-SM exact K5 collision-partition and divergent-forest object definition."""
from __future__ import annotations

import itertools, json, math, os, subprocess
from collections import Counter, defaultdict
from pathlib import Path

VERTICES=tuple(range(5))
PREREG='3c306fdc4581bc5d1fdd2cb6c3500a4e49a2e676'


def partitions(seq):
    if not seq:
        yield []
        return
    first=seq[0]
    for p in partitions(seq[1:]):
        yield [frozenset([first])] + list(p)
        for i in range(len(p)):
            q=list(p)
            q[i]=frozenset(set(q[i])|{first})
            yield q


def canon_partition(p):
    return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b:(-len(b),b)))


def partition_type(p):
    return tuple(sorted((len(b) for b in p),reverse=True))


def pstats(typ):
    r=len(typ)
    codim=3*(5-r)
    internal=sum(k*(k-1)//2 for k in typ)
    q=-2*internal
    margin=q+codim
    return dict(block_sizes=list(typ),blocks=r,codim=codim,internal_edges=internal,
                q=q,l1_margin=margin,omega=-margin)


def compatible(a,b):
    return a<=b or b<=a or a.isdisjoint(b)


def transform_forest(fs,perm):
    mp=dict(zip(VERTICES,perm))
    transformed=[]
    for b in fs:
        transformed.append(tuple(sorted(mp[x] for x in b)))
    return tuple(sorted(transformed,key=lambda b:(len(b),b)))


def canonical_forest(fs):
    return min(transform_forest(fs,p) for p in itertools.permutations(VERTICES))


def main():
    raw=[canon_partition(p) for p in partitions(list(VERTICES))]
    # recursive generator is unique, but lock exact uniqueness explicitly
    parts=sorted(set(raw),key=lambda p:(tuple(-len(b) for b in p),p))
    type_counts=Counter(partition_type(p) for p in parts)
    type_rows=[]
    for typ in sorted(type_counts,key=lambda t:(-t[0],t)):
        row=pstats(typ); row['count']=type_counts[typ]
        type_rows.append(row)

    blocks=[frozenset(c) for k in (3,4,5) for c in itertools.combinations(VERTICES,k)]
    block_rows=[]
    for b in blocks:
        k=len(b); codim=3*(k-1); edges=k*(k-1)//2; q=-2*edges
        block_rows.append({'block':sorted(b),'k':k,'codim':codim,'internal_edges':edges,
                           'q':q,'margin':q+codim,'omega':-(q+codim)})

    forests=[]
    for mask in range(1<<len(blocks)):
        fs=tuple(blocks[i] for i in range(len(blocks)) if (mask>>i)&1)
        if all(compatible(a,b) for a,b in itertools.combinations(fs,2)):
            forests.append(tuple(sorted(fs,key=lambda b:(len(b),tuple(sorted(b))))))
    by_size=Counter(len(f) for f in forests)
    maximal_size=max(map(len,forests))
    maximal=[f for f in forests if len(f)==maximal_size]

    orbits=defaultdict(list)
    for f in forests:
        orbits[canonical_forest(f)].append(f)
    orbit_rows=[]
    for rep,members in sorted(orbits.items(),key=lambda kv:(len(kv[0]),kv[0])):
        orbit_rows.append({'forest_size':len(rep),'orbit_size':len(members),
                           'representative':[list(b) for b in rep]})

    expected_types={
      (1,1,1,1,1):1,(2,1,1,1):10,(2,2,1):15,
      (3,1,1):10,(3,2):10,(4,1):5,(5,):1,
    }
    controls={
      'bell_B5_52':len(parts)==52,
      'partition_type_counts':dict(type_counts)==expected_types,
      'pair_diagonals_10':math.comb(5,2)==10,
      'divergent_blocks_16':len(blocks)==16,
      'divergent_block_size_counts':Counter(map(len,blocks))==Counter({3:10,4:5,5:1}),
      'single_block_margins':all(next(r for r in block_rows if r['k']==k)['margin']==m for k,m in [(3,0),(4,-3),(5,-8)]),
      'k2_margin_plus1':pstats((2,1,1,1))['l1_margin']==1,
      'deepest_excess_8':pstats((5,))['omega']==8,
      'forest_count_72':len(forests)==72,
      'forest_size_counts':dict(by_size)=={0:1,1:16,2:35,3:20},
      'maximal_forests_20':len(maximal)==20 and maximal_size==3,
      'all_maximal_K3_K4_K5_chains':all([len(b) for b in f]==[3,4,5] and f[0]<f[1]<f[2] for f in maximal),
      's5_forest_orbits_8':len(orbits)==8,
      'historical_iter022_sign_agreement':pstats((3,1,1))['l1_margin']==0 and pstats((4,1))['l1_margin']<0 and pstats((5,))['l1_margin']<0,
    }
    prereg_ancestor=subprocess.call(['git','merge-base','--is-ancestor',PREREG,'HEAD'])==0
    valid=all(controls.values()) and prereg_ancestor
    out={
      'iteration':'Iter081X-SM',
      'classification':'ITER081X_SM_K5_STRATIFIED_DIAGONAL_FOREST_OBJECT_DEFINED_EXACT_SCOPED' if valid else 'INVALID_OBJECT_DEFINITION',
      'verdict':'PASS_EXACT_SCOPED' if valid else 'INVALID_OBJECT_DEFINITION',
      'normal_configuration_space':'(R^3)^5 / R^3_diag, dimension 12',
      'edge_leading_degree':-2,
      'partition_count':len(parts),
      'partition_type_rows':type_rows,
      'connected_divergent_blocks':block_rows,
      'forest_definition':'collections of divergent vertex blocks pairwise nested or disjoint',
      'forest_count':len(forests),
      'forest_size_counts':{str(k):v for k,v in sorted(by_size.items())},
      'maximal_forest_size':maximal_size,
      'maximal_forest_count':len(maximal),
      's5_forest_orbit_count':len(orbits),
      's5_forest_orbits':orbit_rows,
      'controls':controls,
      'scope':'exact incidence/power-counting/forest object only; k3/k4 full-boundary physical divergence not proven',
      'provenance':{'git_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                    'prereg_commit_expected':PREREG,'prereg_ancestor':prereg_ancestor},
    }
    p=Path(os.environ.get('ITER081X_OUT','results/raw/iter081x_sm_k5_stratified_forest.json'))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
