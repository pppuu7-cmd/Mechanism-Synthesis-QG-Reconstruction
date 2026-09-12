#!/usr/bin/env python3
"""Iter029: exact microlocal/Hormander audit for multi-wedge boundary constraints.

Model the simultaneous boundary hypersurfaces by linear forms
    ell_e(x)=x_i-x_j
on a reduced vertex-coordinate space (one global translation removed).
For delta-like boundary factors, the standard product criterion fails if there
is a nontrivial combination of conormals summing to zero.  Algebraically this
is the left-nullspace of the reduced oriented incidence matrix B.

This script computes that obstruction exactly with SymPy, compares complete
K_n graphs to spanning-tree controls, and checks all source-induced K5 causal
sign sectors kappa_ij=sigma_i sigma_j.  Row sign flips cannot change rank, but
we verify that statement explicitly rather than assume it.

Scope guardrail: failure of the sufficient Hormander product criterion for the
naive product is NOT a theorem that no correlated i-epsilon, renormalized
extension, boundary/intertwiner cancellation, or source-specific distribution
exists.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import sympy as sp


def edges_complete(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def edges_tree(n):
    return [(i,i+1) for i in range(n-1)]


def reduced_incidence(n, edges, signs=None):
    signs = signs or [1]*len(edges)
    rows=[]
    for s,(i,j) in zip(signs,edges):
        row=[0]*n
        row[i]=s; row[j]=-s
        rows.append(row[:-1])  # quotient global translation
    return sp.Matrix(rows)


def audit_matrix(n, edges, signs=None):
    B=reduced_incidence(n,edges,signs)
    rank=B.rank()
    left_null=B.T.nullspace()
    return {
        'n_vertices': n,
        'n_edges': len(edges),
        'reduced_coordinate_dim': n-1,
        'rank': rank,
        'cycle_nullity': len(edges)-rank,
        'left_nullity': len(left_null),
        'hormander_naive_delta_product_transverse': len(left_null)==0,
        'left_null_basis': [[int(x) for x in v] for v in left_null],
    }


def source_sector_signs(n, edges, sigma):
    return [sigma[i]*sigma[j] for i,j in edges]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--n', type=int, required=True)
    ap.add_argument('--mode', choices=['complete','tree','source-sectors'], required=True)
    ap.add_argument('--output', required=True)
    args=ap.parse_args()
    n=args.n
    out={'iteration':'029','mode':args.mode,'n':n}

    if args.mode=='complete':
        edges=edges_complete(n)
        out['edges']=edges
        out['audit']=audit_matrix(n,edges)
    elif args.mode=='tree':
        edges=edges_tree(n)
        out['edges']=edges
        out['audit']=audit_matrix(n,edges)
    else:
        edges=edges_complete(n)
        # Fix sigma_0=+1 to quotient the global flip: 2^(n-1) sectors.
        rows=[]
        nullities=[]
        for tail in itertools.product([-1,1], repeat=n-1):
            sigma=(1,)+tail
            signs=source_sector_signs(n,edges,sigma)
            a=audit_matrix(n,edges,signs)
            nullities.append(a['left_nullity'])
            rows.append({'sigma':sigma,'edge_signs':signs,'rank':a['rank'],
                         'left_nullity':a['left_nullity'],
                         'transverse':a['hormander_naive_delta_product_transverse']})
        out['n_source_sectors']=len(rows)
        out['sector_rows']=rows
        out['unique_left_nullities']=sorted(set(nullities))
        out['all_sectors_obstructed']=all(r['left_nullity']>0 for r in rows)
        out['reference_unsigned']=audit_matrix(n,edges)

    out['interpretation_guardrail']=(
        'A nonzero left-nullspace is an exact conormal dependence and therefore '
        'blocks the standard transverse/Hormander definition of the naive delta-product. '
        'It does not exclude a correlated source-backed i-epsilon prescription, '
        'renormalized extension, or matrix/intertwiner cancellation.'
    )
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
