#!/usr/bin/env python3
"""Iter042A: source-supported S5 jet-span audit for the j=1/2 Appendix-D primitive.

Scientific scope
----------------
For j=1/2 the published Appendix-D boundary distribution on each wedge contains
only delta and delta', so an edge-local derivative source can contribute at
most one derivative from each of the ten K5 wedges.  Iter039/040 showed that
S5 covariance alone leaves many primitive local jets on the six-dimensional
K5 cycle space.

This script asks a *necessary-condition* question only:

  Which S5-invariant homogeneous jet directions can be reached by Reynolds
  averaging square-free products of the ten projected edge derivative
  directions, with every edge used at most once?

It deliberately does NOT multiply singular distributions and therefore does
not define the physical multi-wedge extension.  Non-transversality from
Iter028/029 remains in force.  A missing direction is source-forbidden within
this edge-local j=1/2 derivative budget; a present direction is only
source-compatible, not physically selected.

The rank computation is performed in an evaluation representation at generic
points.  In addition to the source span, we independently reconstruct the full
S5 invariant space and the descendant subspace q2*Inv_{d-2}; this permits a
numerical quotient test against the exact character dimensions used in
Iter039/040.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Tuple

import numpy as np

from distributional.k5_extension_invariant_jet_audit import (
    EDGES,
    cycle_basis,
    cycle_rep,
    inv_dim,
)

N = 5


def compositions(total: int, parts: int) -> Iterable[Tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def normalized_rank(a: np.ndarray, rtol: float = 2e-9) -> int:
    if a.size == 0 or a.shape[1] == 0:
        return 0
    b = np.asarray(a, dtype=float).copy()
    norms = np.linalg.norm(b, axis=0)
    keep = norms > 1e-13
    if not np.any(keep):
        return 0
    b = b[:, keep] / norms[keep]
    s = np.linalg.svd(b, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > rtol * s[0]))


def reynolds_monomial_matrix(tx: np.ndarray, degree: int) -> np.ndarray:
    """Columns are Reynolds averages of all coordinate monomials of degree d.

    tx has shape (|G|, n_samples, 6) and stores R_g x.
    """
    g, m, n = tx.shape
    assert n == 6
    alphas = list(compositions(degree, 6))
    out = np.empty((m, len(alphas)), dtype=float)
    for col, alpha in enumerate(alphas):
        vals = np.ones((g, m), dtype=float)
        for j, p in enumerate(alpha):
            if p:
                vals *= tx[:, :, j] ** p
        out[:, col] = vals.mean(axis=0)
    return out


def source_squarefree_matrix(tx: np.ndarray, q: np.ndarray, degree: int) -> np.ndarray:
    """Reynolds averages of products of distinct projected edge directions."""
    g, m, _ = tx.shape
    if degree < 0 or degree > len(EDGES):
        return np.empty((m, 0), dtype=float)
    # L[g,m,e] = q_e . (R_g x_m)
    lin = np.einsum("ei,gmi->gme", q, tx, optimize=True)
    subsets = list(itertools.combinations(range(len(EDGES)), degree))
    out = np.empty((m, len(subsets)), dtype=float)
    for col, subset in enumerate(subsets):
        out[:, col] = np.prod(lin[:, :, subset], axis=2).mean(axis=0)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--samples", type=int, default=160)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    d = args.degree
    if d < 2 or d > 10:
        raise SystemExit("degree must be in [2,10] for the j=1/2 ten-edge source budget")

    q = cycle_basis()
    s5 = list(itertools.permutations(range(N)))
    reps = {p: cycle_rep(p, q) for p in s5}
    rstack = np.stack([reps[p] for p in s5], axis=0)

    exact_d, res_d = inv_dim(s5, reps, d)
    exact_m, res_m = inv_dim(s5, reps, d - 2)
    primitive_exact = exact_d - exact_m

    rng = np.random.default_rng(args.seed)
    # Generic bounded points with nonconstant radius.  The mild radial spread
    # keeps high-degree evaluation ranks conditioned while preserving q2
    # descendant information.
    x = rng.normal(size=(args.samples, 6))
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    radii = rng.uniform(0.65, 1.35, size=(args.samples, 1))
    x *= radii
    tx = np.einsum("gij,mj->gmi", rstack, x, optimize=True)

    full = reynolds_monomial_matrix(tx, d)
    lower = reynolds_monomial_matrix(tx, d - 2)
    q2 = np.sum(x * x, axis=1)[:, None]
    descendants = q2 * lower
    source = source_squarefree_matrix(tx, q, d)

    rank_full = normalized_rank(full)
    rank_desc = normalized_rank(descendants)
    rank_source = normalized_rank(source)
    rank_full_desc = normalized_rank(np.concatenate([full, descendants], axis=1))
    rank_full_source = normalized_rank(np.concatenate([full, source], axis=1))
    rank_desc_source = normalized_rank(np.concatenate([descendants, source], axis=1))

    source_primitive_rank = rank_desc_source - rank_desc
    primitive_deficit = primitive_exact - source_primitive_rank
    coverage = (1.0 if primitive_exact == 0 else source_primitive_rank / primitive_exact)

    gates = {
        "full_invariant_rank_matches_character": rank_full == exact_d,
        "descendant_rank_matches_character": rank_desc == exact_m,
        "descendants_lie_in_full_invariants": rank_full_desc == rank_full,
        "source_reynolds_span_lies_in_full_invariants": rank_full_source == rank_full,
        "source_primitive_rank_nonnegative": source_primitive_rank >= 0,
        "source_primitive_rank_not_above_exact_quotient": source_primitive_rank <= primitive_exact,
        "character_integrality_residual_ok": max(res_d, res_m) < 2e-8,
    }

    if primitive_exact == 0:
        classification = "NO_PRIMITIVE_QUOTIENT_AT_DEGREE"
    elif source_primitive_rank == primitive_exact:
        classification = "EDGE_LOCAL_APPENDIXD_SOURCE_SPANS_PRIMITIVE_QUOTIENT"
    elif source_primitive_rank == 0:
        classification = "EDGE_LOCAL_APPENDIXD_SOURCE_MISSES_ALL_PRIMITIVES"
    else:
        classification = "EDGE_LOCAL_APPENDIXD_SOURCE_LEAVES_PRIMITIVE_DEFICIT"

    out = {
        "iteration": "Iter042A",
        "degree": d,
        "seed": args.seed,
        "samples": args.samples,
        "exact_s5_invariant_dimension": exact_d,
        "exact_quadratic_descendant_dimension": exact_m,
        "exact_primitive_quotient_dimension": primitive_exact,
        "evaluation_full_rank": rank_full,
        "evaluation_descendant_rank": rank_desc,
        "source_squarefree_subset_count": math.comb(10, d),
        "source_invariant_rank": rank_source,
        "source_primitive_quotient_rank": source_primitive_rank,
        "primitive_deficit": primitive_deficit,
        "primitive_coverage_fraction": coverage,
        "max_character_integrality_residual": max(res_d, res_m),
        "numerical_gates": gates,
        "classification": classification,
        "claim_lock": (
            "Necessary-condition source-support audit only. Square-free edge derivative products encode the "
            "j=1/2 Appendix-D fact that each wedge supplies at most delta-prime order one. The actual "
            "multi-wedge distribution product is non-transverse and is not defined here; source-compatible "
            "does not mean physically selected, and missing higher structures could still arise only from "
            "additional correlated finite-epsilon/analytic information beyond this edge-local budget."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
