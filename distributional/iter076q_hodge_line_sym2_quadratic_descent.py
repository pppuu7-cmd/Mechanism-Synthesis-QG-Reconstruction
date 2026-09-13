#!/usr/bin/env python3
"""Iter076Q: exact descent of the K4 Hodge line to homogeneous degree two.

Prospectively frozen by prereg/ITER076Q_HODGE_LINE_SYM2_QUADRATIC_DESCENT.md.
This gate is algebraic and scoped: it does not define a physical source-to-K4 P3.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os

import sympy as sp

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


def hodge():
    H = sp.zeros(6, 6)
    for k, (i, j) in enumerate(EDGES):
        comp = sorted(set(VERTS) - {i, j})
        a, b = comp
        H[EINDEX[(a, b)], k] = parity_seq((i, j, a, b))
    return H


H = hodge()


def coords(V, y):
    sol = V.gauss_jordan_solve(y)[0]
    if V * sol != y:
        raise ValueError("coordinate reconstruction failed")
    return sp.Matrix(sol)


def restricted(V, R):
    return sp.Matrix.hstack(*[coords(V, R * V[:, j]) for j in range(V.cols)])


def hodge_coords():
    return sp.Matrix.hstack(*[coords(CYCLE, H * CUT[:, j]) for j in range(CUT.cols)])


def sym2(A):
    """Matrix on the frozen degree-two monomial basis under y=A x."""
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


def lane_a():
    X = hodge_coords()
    failures = []
    for p in PERMS:
        R = edge_action(p)
        C = restricted(CUT, R)
        Z = restricted(CYCLE, R)
        if Z * X != parity(p) * (X * C):
            failures.append(list(p))
    valid = X.det() != 0 and not failures
    return {
        "iteration": "Iter076Q",
        "lane": "A",
        "valid": bool(valid),
        "X": int_matrix(X),
        "det_X": int(X.det()),
        "permutations_checked": len(PERMS),
        "twisted_covariance_failures": failures,
        "representatives_retained": ["+X", "-X"],
        "physical_representative_selected": False,
    }


def lane_b():
    X = hodge_coords()
    SX = sym2(X)
    SmX = sym2(-X)
    q00, q11, q22, q01, q02, q12 = sp.symbols("q00 q11 q22 q01 q02 q12")
    Q = sp.Matrix([[q00, q01, q02], [q01, q11, q12], [q02, q12, q22]])
    generic_form_equal = sp.simplify(X.T * Q * X - (-X).T * Q * (-X)) == sp.zeros(3, 3)
    valid = SX == SmX and SX.rank() == 6 and abs(int(SX.det())) == 1 and generic_form_equal
    return {
        "iteration": "Iter076Q",
        "lane": "B",
        "valid": bool(valid),
        "sym2_X": int_matrix(SX),
        "sym2_plus_minus_equal": bool(SX == SmX),
        "rank_sym2_X": int(SX.rank()),
        "det_sym2_X": int(SX.det()),
        "abs_det_sym2_X_unimodular": bool(abs(int(SX.det())) == 1),
        "generic_symmetric_quadratic_form_equal": bool(generic_form_equal),
    }


def lane_c():
    X = hodge_coords()
    SX = sym2(X)
    quadratic_failures = []
    linear_control_failures = []
    odd_twist_witnesses = 0
    for p in PERMS:
        R = edge_action(p)
        C = restricted(CUT, R)
        Z = restricted(CYCLE, R)
        if sym2(Z) * SX != SX * sym2(C):
            quadratic_failures.append(list(p))
        linear_twisted = Z * X == parity(p) * (X * C)
        if not linear_twisted:
            linear_control_failures.append(list(p))
        if parity(p) == -1 and Z * X == -(X * C) and Z * X != X * C:
            odd_twist_witnesses += 1
    valid = not quadratic_failures and not linear_control_failures and odd_twist_witnesses == 12
    return {
        "iteration": "Iter076Q",
        "lane": "C",
        "valid": bool(valid),
        "permutations_checked": len(PERMS),
        "quadratic_untwisted_covariance_failures": quadratic_failures,
        "linear_twisted_control_failures": linear_control_failures,
        "odd_permutations_retaining_linear_twist": odd_twist_witnesses,
        "expected_odd_permutations": 12,
    }


def lane_d():
    X = hodge_coords()
    l0, l1, l2 = sp.symbols("l0 l1 l2")
    ell = sp.Matrix([[l0, l1, l2]])
    plus = ell * X
    minus = ell * (-X)
    odd_negative_control = sp.simplify(plus + minus) == sp.zeros(1, 3) and plus != minus
    abs_jac_equal = abs(int(X.det())) == abs(int((-X).det()))
    locks = {
        "nonlinear_map_can_mix_nonzero_source_one_jet_into_degree_two": True,
        "physical_source_numerator_jacobian_coefficient_established": False,
        "epsilon_minus1_value_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = odd_negative_control and abs_jac_equal and all([
        locks["nonlinear_map_can_mix_nonzero_source_one_jet_into_degree_two"],
        not locks["physical_source_numerator_jacobian_coefficient_established"],
        not locks["epsilon_minus1_value_established"],
        not locks["generic_finite_spin_signed_P3_promoted"],
        not locks["G3_promoted"],
        not locks["F9_promoted"],
        not locks["G8_promoted"],
        not locks["K5_promoted"],
    ])
    return {
        "iteration": "Iter076Q",
        "lane": "D",
        "valid": bool(valid),
        "generic_linear_covector_plus_minus_opposite": bool(odd_negative_control),
        "abs_linear_jacobian_sign_independent": bool(abs_jac_equal),
        "det_plus_X": int(X.det()),
        "det_minus_X": int((-X).det()),
        "scope_locks": locks,
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
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076Q_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED"
        if valid
        else "ITER076Q_ORIENTATION_LINE_QUADRATIC_DESCENT_FAIL"
    )
    return {
        "iteration": "Iter076Q",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "Global sign of the exact linear Hodge line is irrelevant for homogeneous quadratic transport only. "
            "Physical source-to-K4 provenance and possible source-one-jet/nonlinear-map contamination remain open."
        ),
        "next_admissible_gate": (
            "Prospectively audit whether the relevant source numerator/Haar-Jacobian one-jet vanishes or is "
            "annihilated in the physical alternating/transitive channel before assigning any epsilon^-1 coefficient."
        ),
        "claim_lock": (
            "No new physics, complete-QG claim, generic finite-spin signed P3, physical causal-vertex "
            "finiteness/divergence theorem, epsilon^-1 coefficient, or G3/F9/G8/K5 promotion."
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
