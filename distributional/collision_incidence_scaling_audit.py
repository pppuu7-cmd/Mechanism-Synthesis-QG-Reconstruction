#!/usr/bin/env python3
"""Iteration 028A: exact K2..K5 collision-incidence and scaling-degree audit.

This is an exact local tangent-space/combinatorial diagnostic motivated by the
multi-collision powers observed in Iterations 022--024 and by the need to know
when boundary-supported distributions can be multiplied without an extension.

For a collision graph G=(V,E), local boost differences are linearized as
x_a-x_b in R^3.  The lifted incidence matrix is B_G \otimes I_3.  Its rank is
3(|V|-c), while it contains 3|E| scalar constraints, hence

  excess = 3 ( |E|-|V|+c ) = 3 * cycle_rank.

Forests have zero excess; cycles have linearly dependent collision normals.
In the corresponding delta^3 collision surrogate this is exactly where the
naive product ceases to be transverse and an extension/renormalization question
appears.

Separately, using the empirically validated ordinary Toller local power
|T|~beta^-2, the uniform-scaling degree of a graph is 2|E| in local dimension
3(|V|-c), so

  omega = 2|E| - 3(|V|-c).

omega>=0 flags a local ordinary-function absolute-integrability obstruction.
This is NOT the exact wavefront set of the published Toller Feynman distribution:
the Appendix-D spectral boundary variable must still be pulled back to the full
group amplitude.  The incidence calculation is a prospective conormal model and
a guard for the next exact distributional construction.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def components(vertices, edges):
    parent={v:v for v in vertices}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for a,b in edges: union(a,b)
    return len({find(v) for v in vertices})


def row_for_subset(k, subset):
    all_edges=list(itertools.combinations(range(k),2))
    edges=[all_edges[i] for i in subset]
    active=sorted({v for e in edges for v in e})
    if not active:
        return None
    c=components(active,edges)
    V=len(active); E=len(edges)
    cycle=E-V+c
    rank3=3*(V-c)
    constraints3=3*E
    excess=constraints3-rank3
    omega=2*E-rank3
    return {
        'k_parent':k,'active_vertices':active,'V':V,'E':E,'components':c,
        'edges':[list(e) for e in edges],
        'cycle_rank':cycle,'lifted_incidence_rank':rank3,
        'scalar_collision_constraints':constraints3,'normal_excess':excess,
        'is_forest':cycle==0,'ordinary_toller_omega':omega,
        'ordinary_absolute_flag':'OBSTRUCTION' if omega>=0 else 'LOCALLY_INTEGRABLE_BY_POWER',
        'delta3_transversality_surrogate':'TRANSVERSE' if excess==0 else 'NONTRANSVERSE_EXTENSION_REQUIRED',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    summaries={}; full=[]
    for k in range(2,6):
        all_edges=list(itertools.combinations(range(k),2)); rows=[]
        for mask in range(1,1<<len(all_edges)):
            subset=[i for i in range(len(all_edges)) if (mask>>i)&1]
            r=row_for_subset(k,subset); rows.append(r)
        # keep only rows whose active set is all k vertices for parent-cluster summaries
        spanning=[r for r in rows if r['V']==k]
        connected=[r for r in spanning if r['components']==1]
        divergent=[r for r in connected if r['ordinary_toller_omega']>=0]
        nontrans=[r for r in connected if r['normal_excess']>0]
        forests=[r for r in connected if r['is_forest']]
        complete=next(r for r in connected if r['E']==len(all_edges))
        summaries[str(k)]={
            'edge_count_complete':len(all_edges),
            'connected_spanning_subgraphs':len(connected),
            'connected_forests':len(forests),
            'connected_nontransverse_cycle_graphs':len(nontrans),
            'connected_ordinary_power_obstructions':len(divergent),
            'complete_graph':complete,
        }
        full.extend(rows)

    # inclusion-minimal connected ordinary-power obstructions across K5 subsets
    candidates=[r for r in full if r['components']==1 and r['ordinary_toller_omega']>=0]
    def edge_set(r): return {tuple(e) for e in r['edges']}
    minimal=[]
    for r in candidates:
        er=edge_set(r)
        has_proper=False
        for q in candidates:
            eq=edge_set(q)
            if q['V']<=r['V'] and eq < er:
                # only count a proper divergent subgraph on vertices actually present in r
                if set(q['active_vertices']).issubset(set(r['active_vertices'])):
                    has_proper=True; break
        if not has_proper: minimal.append(r)
    # de-duplicate isomorphic/minimal entries by (V,E,cycle,omega)
    types=sorted({(r['V'],r['E'],r['cycle_rank'],r['ordinary_toller_omega']) for r in minimal})

    out={
        'model':'linearized_collision_incidence_B_kron_I3',
        'ordinary_toller_edge_power':2,
        'summary_by_parent_k':summaries,
        'minimal_divergent_types':[{'V':v,'E':e,'cycle_rank':c,'omega':o} for v,e,c,o in types],
        'expected_complete_cluster_omegas':{'K2':-1,'K3':0,'K4':3,'K5':8},
        'verdict':'COLLISION_INCIDENCE_AND_SCALING_AUDIT_COMPLETE',
        'guardrail':('Exact for the stated linearized collision-incidence surrogate and ordinary beta^-2 power counting. '
                     'It is not by itself the Hörmander wavefront set or pullback theorem for the full Toller Feynman distribution.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
