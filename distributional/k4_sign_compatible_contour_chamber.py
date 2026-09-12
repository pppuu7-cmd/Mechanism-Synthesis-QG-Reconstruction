#!/usr/bin/env python3
"""Iter054: exact sign-compatible affine contour chamber audit for K4.

The causal signs are realizable by one affine cycle-contour direction v with
edge-dependent positive magnitudes iff diag(s) A v > 0.  Feasibility is decided
exactly using strict separation: zero must not lie in the convex hull of the
six signed row normals.  By Caratheodory in R^3 an obstruction has support <=4.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import TREES, incidence
from distributional.k4_denominator_pole_topology_control import SIGMA_CLASSES, edge_signs_from_class
from distributional.k4_global_contour_compatibility import exact_cycle_matrix

WITNESS_MAX_ABS = 12


def _nonnegative_exact(z):
    z = sp.simplify(z)
    return z.is_nonnegative is True


def convex_zero_certificate(M: sp.Matrix):
    """Return exact minimal-support convex certificate for 0 in conv(rows(M)).

    A minimal convex representation has affinely independent support, hence at
    most four rows in R^3.  Enumerating support size upward gives a deterministic
    exact certificate when one exists.
    """
    n = M.rows
    rhs = sp.Matrix([0, 0, 0, 1])
    for k in range(1, min(4, n) + 1):
        for inds in itertools.combinations(range(n), k):
            C = sp.Matrix([
                [M[j, 0] for j in inds],
                [M[j, 1] for j in inds],
                [M[j, 2] for j in inds],
                [sp.Integer(1) for _ in inds],
            ])
            # Minimal-support convex representations are affinely independent.
            if int(C.rank()) != k:
                continue
            if int(C.row_join(rhs).rank()) != k:
                continue
            solset = sp.linsolve((C, rhs))
            if solset == sp.EmptySet:
                continue
            weights = tuple(sp.simplify(z) for z in next(iter(solset)))
            if not all(_nonnegative_exact(z) for z in weights):
                continue
            weighted = sp.zeros(3, 1)
            for idx, w in zip(inds, weights):
                weighted += w * M[idx, :].T
            valid = (
                sp.simplify(sum(weights) - 1) == 0
                and all(sp.simplify(z) == 0 for z in weighted)
            )
            if valid:
                return {
                    "indices": list(inds),
                    "weights": list(weights),
                }
    return None


def integer_witness(M: sp.Matrix, max_abs: int = WITNESS_MAX_ABS):
    """Deterministic exact witness search, increasing L-infinity radius."""
    for r in range(1, max_abs + 1):
        for vals in itertools.product(range(-r, r + 1), repeat=3):
            if max(abs(x) for x in vals) != r:
                continue
            if vals == (0, 0, 0):
                continue
            v = sp.Matrix(vals)
            margins = [sp.simplify(z) for z in M * v]
            if all(z.is_positive is True for z in margins):
                return v, margins
    return None, None


def compute(sign_class: str, tree: str):
    sigma, edge_signs, edge_text = edge_signs_from_class(sign_class)
    y, x, A, b, tree_edges, chords, det = exact_cycle_matrix(tree)
    s = sp.Matrix(edge_signs)
    D = sp.diag(*list(s))
    M = sp.simplify(D * A)
    B = incidence()

    BA = sp.simplify(B * A)
    cycle_basis_valid = (
        abs(int(det)) == 1
        and int(A.rank()) == 3
        and all(sp.simplify(z) == 0 for z in BA)
    )

    row_checks = []
    for e, xe in enumerate(x):
        reconstructed = b[e] + sum(A[e, j] * y[j] for j in range(3))
        row_checks.append(sp.simplify(xe - reconstructed) == 0)

    cert = convex_zero_certificate(M)
    feasible = cert is None

    obstruction = None
    cert_valid = True
    if cert is not None:
        inds = cert["indices"]
        weights = cert["weights"]
        weighted = sp.zeros(3, 1)
        for idx, w in zip(inds, weights):
            weighted += w * M[idx, :].T
        cert_valid = all([
            1 <= len(inds) <= 4,
            all(_nonnegative_exact(w) for w in weights),
            sp.simplify(sum(weights) - 1) == 0,
            all(sp.simplify(z) == 0 for z in weighted),
        ])
        obstruction = {
            "edge_indices": inds,
            "weights": list(map(str, weights)),
            "weighted_row_sum": list(map(str, weighted)),
        }

    witness = None
    margins = None
    witness_valid = True
    if feasible:
        v, ms = integer_witness(M)
        if v is None:
            witness_valid = False
        else:
            witness = list(map(int, v))
            margins = list(map(str, ms))
            witness_valid = all(sp.simplify(z).is_positive is True for z in ms)

    valid = all([
        cycle_basis_valid,
        all(row_checks),
        cert_valid,
        witness_valid,
        (obstruction is None) == feasible,
    ])

    return {
        "iteration": "Iter054",
        "sign_class": sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": tree,
        "tree_edges": list(map(int, tree_edges)),
        "chord_edges": list(map(int, chords)),
        "A": [[str(A[i,j]) for j in range(3)] for i in range(6)],
        "signed_normal_matrix_M": [[str(M[i,j]) for j in range(3)] for i in range(6)],
        "strict_sign_chamber_feasible": bool(feasible),
        "integer_witness_v": witness,
        "witness_signed_margins": margins,
        "witness_max_abs_bound": WITNESS_MAX_ABS,
        "obstruction_certificate": obstruction,
        "cycle_basis_valid": bool(cycle_basis_valid),
        "edge_row_reconstruction_all_exact": bool(all(row_checks)),
        "certificate_valid": bool(cert_valid),
        "witness_valid": bool(witness_valid),
        "valid": bool(valid),
        "claim_lock": (
            "One-vector affine contour sign-chamber feasibility only. Unequal positive edge magnitudes are allowed; "
            "no equal-epsilon reconstruction, correlated/nonlinear contour, physical amplitude, K5, G3, F9 or G8 claim."
        ),
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter054_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter054" and "strict_sign_chamber_feasible" in r:
            rows.append(r)

    expected = len(SIGMA_CLASSES) * len(TREES)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter054 lanes, found {len(rows)}")
    keys = {(r["sign_class"], r["tree"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter054 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    basis_consistent = True
    feasible_classes = []
    per_class = {}
    for sc in SIGMA_CLASSES:
        sr = sorted([r for r in rows if r["sign_class"] == sc], key=lambda r: r["tree"])
        vals = [r["strict_sign_chamber_feasible"] for r in sr]
        same = all(v == vals[0] for v in vals[1:])
        basis_consistent = basis_consistent and same
        if same and vals[0]:
            feasible_classes.append(sc)
        per_class[sc] = {
            "feasible_in_all_tree_bases": bool(same and vals[0]),
            "feasibility_by_tree": {r["tree"]: bool(r["strict_sign_chamber_feasible"]) for r in sr},
            "witnesses": {r["tree"]: r["integer_witness_v"] for r in sr if r["integer_witness_v"] is not None},
            "obstruction_supports": {
                r["tree"]: (r["obstruction_certificate"] or {}).get("edge_indices")
                for r in sr if r["obstruction_certificate"] is not None
            },
        }

    n = len(feasible_classes)
    if not all_valid or not basis_consistent:
        classification = "ITER054_RECONSTRUCTION_OR_CERTIFICATE_INVALID"
    elif n == len(SIGMA_CLASSES):
        classification = "K4_CAUSAL_SIGN_CHAMBER_ALL_CLASSES_FEASIBLE"
    elif n == 0:
        classification = "K4_CAUSAL_SIGN_CHAMBER_NO_CLASS_FEASIBLE"
    else:
        classification = "K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT"

    return {
        "iteration": "Iter054",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "basis_consistent": bool(basis_consistent),
        "feasible_class_count": n,
        "feasible_classes": feasible_classes,
        "per_class": per_class,
        "claim_lock": (
            "Exact affine sign-chamber taxonomy only; no statement about equal-magnitude i-epsilon shifts, "
            "general correlated/nonlinear contours or physical causal amplitudes."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["compute", "aggregate"], default="compute")
    ap.add_argument("--sign-class", choices=SIGMA_CLASSES)
    ap.add_argument("--tree", choices=sorted(TREES))
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    if args.mode == "compute":
        if args.sign_class is None or args.tree is None:
            raise SystemExit("compute requires --sign-class and --tree")
        out = compute(args.sign_class, args.tree)
    else:
        out = aggregate(Path(args.input_dir))

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
