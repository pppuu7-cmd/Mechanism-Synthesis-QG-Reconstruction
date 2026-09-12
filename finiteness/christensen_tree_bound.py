#!/usr/bin/env python3
"""Iteration 027A: exact K5 spanning-tree bound for causal Toller kernels.

Christensen's Lorentzian 10j finiteness proof uses convex combinations of
weighted spanning-tree graphs.  For K5 there are E=10 edges and every spanning
tree contains V-1=4 edges.  If a convex weighted-tree cover represents unit
weight on every K5 edge and no tree-edge exponent exceeds M, summing all edge
constraints gives the exact lower bound

    10 <= 4 M  ->  M >= 5/2.

The symmetric uniform distribution over all 5^(5-2)=125 labelled spanning
trees achieves M=5/2 because each K5 edge occurs in exactly 50 trees.

For a scalar/matrix kernel with local norm |K(beta)| ~ beta^{-p} and H3 radial
measure sinh(beta)^2 d beta ~ beta^2 d beta, the single weighted edge integral

    int beta^2 |K(beta)|^m d beta

is locally finite iff 2-p*m > -1, i.e.

    m < 3/p.

Thus:
- Livine-Oriti-like beta^-1 kernels allow m<3, so m=5/2 is compatible with the
  spanning-tree proof;
- the j=1/2 causal Toller kernel measured in Iteration 020 has p≈2, so only
  m<3/2 is allowed and the same K5 tree proof cannot close.

This is a no-go for this *particular positive absolute-value tree-bound method*,
not a proof that the causal EPRL/Toller vertex diverges.  Matrix cancellations,
distributional i-epsilon terms, or a different global estimate may still work.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path
import argparse

N=5
VERTICES=tuple(range(N))
EDGES=tuple((i,j) for i in range(N) for j in range(i+1,N))


def prufer_tree(seq):
    deg=[1]*N
    for x in seq: deg[x]+=1
    edges=[]
    seq=list(seq)
    for x in seq:
        leaf=min(i for i,d in enumerate(deg) if d==1)
        e=tuple(sorted((leaf,x))); edges.append(e)
        deg[leaf]-=1; deg[x]-=1
    rem=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(sorted(rem)))
    return tuple(sorted(edges))


def all_trees():
    return sorted(set(prufer_tree(seq) for seq in itertools.product(VERTICES,repeat=N-2)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()

    trees=all_trees()
    counts=Counter(e for T in trees for e in T)
    E=len(EDGES); tsize=N-1
    m_min=E/tsize
    # Uniform lambda=1/125 and weight=5/2 on every used tree edge.
    reconstructed={e:(counts[e]/len(trees))*m_min for e in EDGES}
    max_rec_err=max(abs(v-1.0) for v in reconstructed.values())

    p_toller=2.0
    p_lo=1.0
    mcrit_toller=3.0/p_toller
    mcrit_lo=3.0/p_lo

    # Exact scaling exponents of the weighted radial integrand beta^(2-p*m).
    tests=[]
    for label,p in [('Toller_beta^-2',p_toller),('LO_beta^-1',p_lo)]:
        for m in (1.0,1.49,1.5,2.0,2.5,3.0):
            power=2-p*m
            tests.append({
                'kernel':label,'p':p,'m':m,
                'radial_integrand_power':power,
                'locally_integrable':bool(power>-1),
                'log_borderline':bool(abs(power+1)<1e-12),
            })

    out={
        'vertices':N,'edges':E,'spanning_tree_count':len(trees),
        'tree_edge_count':tsize,
        'edge_occurrence_counts':{f'{a}-{b}':counts[(a,b)] for a,b in EDGES},
        'minimum_possible_max_tree_edge_exponent':m_min,
        'lower_bound_derivation':'10 = sum_e 1 <= sum_T lambda_T * 4*M = 4*M, so M >= 5/2',
        'uniform_tree_cover_reconstruction_error':max_rec_err,
        'toller_local_power_p':p_toller,
        'toller_single_edge_integrability_requires_m_lt':mcrit_toller,
        'livine_oriti_local_power_p':p_lo,
        'livine_oriti_single_edge_integrability_requires_m_lt':mcrit_lo,
        'tree_bound_margin_toller_mcrit_minus_Mmin':mcrit_toller-m_min,
        'tree_bound_margin_LO_mcrit_minus_Mmin':mcrit_lo-m_min,
        'weighted_edge_tests':tests,
        'verdict':('CHRISTENSEN_TREE_BOUND_NO_GO_FOR_BETA_MINUS_2_TOLLER'
                   if m_min>=mcrit_toller else 'TREE_BOUND_NOT_EXCLUDED'),
        'control':('LIVINE_ORITI_COMPATIBLE_WITH_TREE_BOUND'
                   if m_min<mcrit_lo else 'LO_CONTROL_FAILED'),
        'guardrail':(
            'Exact no-go only for positive absolute-value convex spanning-tree bounds of the Christensen type '
            'using the local beta^-2 norm power. It is not a divergence proof for the physical distributional causal vertex.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if len(trees)!=125 or any(counts[e]!=50 for e in EDGES) or max_rec_err>1e-12:
        raise SystemExit(9)

if __name__=='__main__': main()
