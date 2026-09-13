#!/usr/bin/env python3
"""Iter076B: exact quadratic overlap-jet restriction complex.

Frozen prospectively in status/ITERATION_076B_PREREG.md.
This is algebraic bookkeeping only; it does not assign an epsilon^-1 coefficient.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

import sympy as sp

from distributional.iter073a_k4_signed_cutspace_face_atlas import Lmat
from distributional.iter073d_transitive_face_cones import records_for, TRANS, TREES
from distributional.iter076a_transitive_overlap_mobius import support_closure, mobius, TOP

NEG = "++-+"


def q_pairs(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


def restriction_matrix(N: sp.Matrix) -> sp.Matrix:
    """Map coefficients of Sym^2(Q^3) to Sym^2(Q^d) under z=N*y."""
    d = N.cols
    src = q_pairs(3)
    dst = q_pairs(d)
    R = sp.zeros(len(dst), len(src))
    for c, (a, b) in enumerate(src):
        for r, (i, j) in enumerate(dst):
            if i == j:
                coeff = N[a, i] * N[b, i]
            else:
                coeff = N[a, i] * N[b, j] + N[a, j] * N[b, i]
            R[r, c] = sp.simplify(coeff)
    return R


def sym2_pullback(C: sp.Matrix) -> sp.Matrix:
    """Map Sym^2(u)-coefficients to Sym^2(v) for u=C*v."""
    da, db = C.rows, C.cols
    src = q_pairs(da)
    dst = q_pairs(db)
    T = sp.zeros(len(dst), len(src))
    for c, (a, b) in enumerate(src):
        for r, (i, j) in enumerate(dst):
            if i == j:
                coeff = C[a, i] * C[b, i]
            else:
                coeff = C[a, i] * C[b, j] + C[a, j] * C[b, i]
            T[r, c] = sp.simplify(coeff)
    return T


def canonical_nullspace(L: sp.Matrix, S: frozenset[int]) -> sp.Matrix:
    A = L[list(sorted(S)), :] if S else sp.zeros(0, 3)
    ns = A.nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(3, 0)


def inclusion_coordinates(NA: sp.Matrix, NB: sp.Matrix):
    """Return C with NB=NA*C, or None if inclusion fails."""
    if NB.cols == 0:
        return sp.zeros(NA.cols, 0)
    if NA.cols == 0:
        return None
    cols = []
    for j in range(NB.cols):
        sol = sp.linsolve((NA, NB[:, j]))
        vals = list(sol)
        if len(vals) != 1:
            return None
        v = vals[0]
        # NA has full column rank, so solution must be unique/no parameters.
        if any(getattr(x, 'free_symbols', set()) for x in v):
            return None
        cols.append(sp.Matrix(v))
    C = sp.Matrix.hstack(*cols)
    return C if NA * C == NB else None


def audit(label: str, tree: str):
    L, _ = Lmat(tree)
    faces = [frozenset(r['S']) for r in records_for(label, tree)]
    nodes = support_closure(faces)
    mu = mobius(nodes)

    rows = {}
    for S in nodes:
        N = canonical_nullspace(L, S)
        R = restriction_matrix(N)
        rows[S] = {
            'nullity': N.cols,
            'quadratic_rank': int(R.rank()),
            'N': N,
            'R': R,
        }

    compatible = True
    monotone = True
    pair_count = 0
    for A in nodes:
        for B in nodes:
            if not A < B:
                continue
            pair_count += 1
            NA, NB = rows[A]['N'], rows[B]['N']
            C = inclusion_coordinates(NA, NB)
            if C is None:
                compatible = False
                continue
            T = sym2_pullback(C)
            if T * rows[A]['R'] != rows[B]['R']:
                compatible = False
            if rows[B]['quadratic_rank'] > rows[A]['quadratic_rank']:
                monotone = False

    recs = sorted(
        (len(S), rows[S]['nullity'], rows[S]['quadratic_rank'], mu[(S, TOP)])
        for S in nodes
    )
    return {
        'face_count': len(faces),
        'closure_size': len(nodes),
        'mobius_identity_ok': all(
            sum(mu[(a, z)] for z in nodes if a <= z <= b) == (1 if a == b else 0)
            for a in nodes for b in nodes if a <= b
        ),
        'top_mu_histogram': sorted(Counter(mu[(S, TOP)] for S in nodes).items()),
        'restriction_records': [list(x) for x in recs],
        'comparable_pairs_checked': pair_count,
        'restriction_compatibility_exact': compatible,
        'rank_monotonicity_exact': monotone,
        'nonzero_proper_quadratic_rank': any(
            S != TOP and rows[S]['quadratic_rank'] > 0 for S in nodes
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    source = {}
    p1 = p2 = p3 = p4 = p5 = p6 = True
    class_signatures = []

    expected_mu = [(-1, 4), (0, 5), (1, 4)]
    expected_closure = 13

    for label in TRANS:
        basis = {}
        ref = None
        for tree in TREES:
            rec = audit(label, tree)
            basis[tree] = rec
            p1 &= (rec['face_count'] == 6 and rec['closure_size'] == expected_closure
                   and rec['mobius_identity_ok'] and rec['top_mu_histogram'] == expected_mu)
            p2 &= rec['rank_monotonicity_exact']
            p3 &= rec['restriction_compatibility_exact']
            sig = tuple(tuple(x) for x in rec['restriction_records'])
            if ref is None:
                ref = sig
            else:
                p4 &= (sig == ref)
            p6 &= rec['nonzero_proper_quadratic_rank']
        class_signatures.append(ref)
        source[label] = basis

    p5 &= all(sig == class_signatures[0] for sig in class_signatures)
    neg_counts = {tree: len(records_for(NEG, tree)) for tree in TREES}
    p7 = all(v == 0 for v in neg_counts.values())

    ok = bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out = {
        'iteration': 'Iter076B',
        'predicates': {
            'P1_ITER076A_POSET_MOBIUS_REPRODUCED': bool(p1),
            'P2_QUADRATIC_RESTRICTION_RANK_MONOTONE': bool(p2),
            'P3_COMPARABLE_RESTRICTIONS_COMMUTE_EXACTLY': bool(p3),
            'P4_CYCLE_BASIS_SIGNATURE_INVARIANT': bool(p4),
            'P5_TRANSITIVE_S4_ORBIT_SIGNATURE_EQUAL': bool(p5),
            'P6_DEGREE2_DATA_NONTRIVIAL_NEGATIVE_CONTROL': bool(p6),
            'P7_NONTRANSITIVE_CONTROL_EMPTY': bool(p7),
        },
        'negative_control_face_counts': neg_counts,
        'classification': (
            'ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_EXACT_COVARIANT_SCOPED'
            if ok else
            'ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_OBSTRUCTED_SCOPED'
        ),
        'source': source,
        'claim_lock': (
            'Exact quadratic overlap-jet bookkeeping only; no epsilon^-1 coefficient, '
            'finite-part/counterterm prescription, physical causal-vertex theorem, '
            'K5/G3/F9/G8 promotion, complete QG or new physics.'
        ),
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True), encoding='utf-8')
    print(json.dumps({k: v for k, v in out.items() if k != 'source'}, indent=2, sort_keys=True))
    if not ok:
        raise SystemExit(9)


if __name__ == '__main__':
    main()
