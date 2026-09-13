#!/usr/bin/env python3
"""Iter076R — source one-jet versus nonlinear-map curvature contamination.

Prospectively frozen by prereg/ITER076R_SOURCE_ONEJET_CURVATURE_CONTAMINATION.md.
This exact algebra gate does not construct a physical source-to-K4 pushforward.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
VERTS = range(4)
EDGES = [(i, j) for i in VERTS for j in VERTS if i < j]
EINDEX = {e: k for k, e in enumerate(EDGES)}
PERMS = list(itertools.permutations(VERTS))
XVAR = sp.symbols("x0:3")
MONS = [
    XVAR[0] ** 2,
    XVAR[1] ** 2,
    XVAR[2] ** 2,
    XVAR[0] * XVAR[1],
    XVAR[0] * XVAR[2],
    XVAR[1] * XVAR[2],
]


def parity_seq(seq):
    inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
    return -1 if inv % 2 else 1


def parity(p):
    return parity_seq(p)


def incidence():
    B = sp.zeros(4, 6)
    for k, (i, j) in enumerate(EDGES):
        B[i, k] = -1
        B[j, k] = 1
    return B


B = incidence()
CUT = sp.Matrix.hstack(*B.T.columnspace())
CYCLE = sp.Matrix.hstack(*B.nullspace())


def edge_action(p):
    R = sp.zeros(6, 6)
    for k, (i, j) in enumerate(EDGES):
        a, b = p[i], p[j]
        if a < b:
            e, s = (a, b), 1
        else:
            e, s = (b, a), -1
        R[EINDEX[e], k] = s
    return R


def coords(V, y):
    sol = V.gauss_jordan_solve(y)[0]
    if V * sol != y:
        raise ValueError("coordinate reconstruction failed")
    return sp.Matrix(sol)


def restricted(V, R):
    return sp.Matrix.hstack(*[coords(V, R * V[:, j]) for j in range(V.cols)])


def sym2(A):
    y = A * sp.Matrix(XVAR)
    images = [
        y[0] ** 2,
        y[1] ** 2,
        y[2] ** 2,
        y[0] * y[1],
        y[0] * y[2],
        y[1] * y[2],
    ]
    rows = []
    for f in images:
        poly = sp.Poly(sp.expand(f), *XVAR)
        rows.append([poly.coeff_monomial(m) for m in MONS])
    return sp.Matrix(rows)


def int_matrix(M):
    return [[int(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def curvature_nullspace():
    variables = sp.symbols("k0:18")
    K = sp.Matrix(3, 6, variables)
    equations = []
    for p in PERMS:
        R = edge_action(p)
        C = restricted(CUT, R)
        Z = restricted(CYCLE, R)
        equations.extend(list(Z * K - parity(p) * K * sym2(C)))
    A, _ = sp.linear_eq_to_matrix(equations, variables)
    return A, A.nullspace()


def lane_a():
    beta = sp.symbols("beta")
    haar = (sp.sinh(beta) / beta) ** 2
    series = sp.series(haar, beta, 0, 6).removeO().expand()
    derivative_zero = sp.limit(sp.diff(haar, beta), beta, 0) == 0
    expected = 1 + beta**2 / 3 + 2 * beta**4 / 45
    valid = derivative_zero and sp.expand(series - expected) == 0
    return {
        "iteration": "Iter076R",
        "lane": "A",
        "valid": bool(valid),
        "haar_series_through_beta4": str(series),
        "haar_onejet_at_zero": 0 if derivative_zero else "NONZERO_OR_UNRESOLVED",
        "scope": "radial Haar/KAK density only",
    }


def lane_b():
    A, null = curvature_nullspace()
    dim = len(null)
    K0 = sp.Matrix(3, 6, null[0]) if dim else sp.zeros(3, 6)
    covariance_failures = []
    if dim:
        for p in PERMS:
            R = edge_action(p)
            C = restricted(CUT, R)
            Z = restricted(CYCLE, R)
            if Z * K0 != parity(p) * K0 * sym2(C):
                covariance_failures.append(list(p))
    valid = A.rank() == 17 and dim == 1 and not covariance_failures and K0 != sp.zeros(3, 6)
    return {
        "iteration": "Iter076R",
        "lane": "B",
        "valid": bool(valid),
        "unknowns": 18,
        "constraint_rank": int(A.rank()),
        "twisted_quadratic_curvature_dimension": dim,
        "basis_K0": int_matrix(K0) if dim else [],
        "permutations_checked": 24,
        "covariance_failures": covariance_failures,
    }


def lane_c():
    _, null = curvature_nullspace()
    if not null:
        return {
            "iteration": "Iter076R",
            "lane": "C",
            "valid": True,
            "curvature_space_zero": True,
            "contamination_witness": None,
        }
    K0 = sp.Matrix(3, 6, null[0])
    l0, l1, l2 = sp.symbols("l0 l1 l2")
    ell = sp.Matrix([[l0, l1, l2]])
    coeff = ell * K0
    poly = sp.expand(sum(coeff[0, i] * MONS[i] for i in range(6)))
    special = sp.expand(poly.subs({l0: 1, l1: 2, l2: 3}))
    valid = poly != 0 and special != 0 and K0.rank() == 3
    return {
        "iteration": "Iter076R",
        "lane": "C",
        "valid": bool(valid),
        "curvature_space_zero": False,
        "rank_K0": int(K0.rank()),
        "generic_contracted_coefficients": [str(x) for x in list(coeff)],
        "generic_contamination_polynomial": str(poly),
        "integer_covector_1_2_3_witness": str(special),
    }


def require(path, needles):
    s = (ROOT / path).read_text(encoding="utf-8")
    return {needle: needle in s for needle in needles}


def lane_d():
    d_checks = require(
        "status/ITERATION_076D_RESULT.md",
        [
            "odd terms vanish",
            "does **not** establish the source-to-K4 pushforward",
        ],
    )
    p_checks = require(
        "status/CURRENT.md",
        [
            "EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED",
            "known exact Toller complex-conjugation branch flip exits the source causal K5 image",
            "nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`",
        ],
    )
    q_checks = require(
        "results/ITER076Q_HODGE_LINE_SYM2_QUADRATIC_DESCENT_RESULT.md",
        [
            "ITER076Q_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED",
            "source numerator/density has a nonzero one-jet",
        ],
    )
    all_evidence = all(d_checks.values()) and all(p_checks.values()) and all(q_checks.values())
    locks = {
        "full_toller_intertwiner_numerator_onejet_established_zero": False,
        "physical_source_to_k4_nonlinear_curvature_established": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "physical_finiteness_or_divergence_theorem": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = all_evidence and not any(locks.values())
    return {
        "iteration": "Iter076R",
        "lane": "D",
        "valid": bool(valid),
        "evidence": {
            "iter076d": d_checks,
            "iter076p_current": p_checks,
            "iter076q": q_checks,
        },
        "scope_locks": locks,
        "scientific_statement": (
            "Haar one-jet vanishing does not imply vanishing of the full Toller/intertwiner numerator one-jet; "
            "known Toller conjugation is not a same-causal evenness symmetry, and the physical nonlinear pushforward remains unbuilt."
        ),
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def write(obj, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                with open(os.path.join(base, fn), encoding="utf-8") as f:
                    obj = json.load(f)
            except Exception:
                continue
            lane = obj.get("lane")
            if lane in LANES:
                got[lane] = obj
    all_valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    dim = got.get("B", {}).get("twisted_quadratic_curvature_dimension")
    witness = got.get("C", {}).get("curvature_space_zero") is False
    if all_valid and dim == 1 and witness:
        classification = "ITER076R_HAAR_ONEJET_ZERO_BUT_SYMMETRY_ALLOWS_NONLINEAR_QUADRATIC_CURVATURE_SOURCE_NUMERATOR_ONEJET_STILL_REQUIRED_EXACT_SCOPED"
    elif all_valid and dim == 0:
        classification = "ITER076R_SYMMETRY_FORBIDS_QUADRATIC_CURVATURE_CONTAMINATION_EXACT_SCOPED"
    else:
        classification = "ITER076R_SOURCE_ONEJET_CURVATURE_GATE_FAIL"
    valid = all_valid and classification != "ITER076R_SOURCE_ONEJET_CURVATURE_GATE_FAIL"
    return {
        "iteration": "Iter076R",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "curvature_channel_dimension": dim,
        "source_haar_onejet_zero": got.get("A", {}).get("haar_onejet_at_zero") == 0,
        "full_source_numerator_onejet_zero_established": False,
        "epsilon_minus1_coefficient_established": False,
        "next_admissible_gate": (
            "Derive or source-audit the full Toller/intertwiner numerator one-jet and, if nonzero, the actual nonlinear source-to-K4 curvature before forming the physical degree-two coefficient."
        ),
        "claim_lock": (
            "No new physics, complete-QG claim, generic finite-spin signed P3, physical causal-vertex finiteness/divergence theorem, epsilon^-1 coefficient, or G3/F9/G8/K5 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
