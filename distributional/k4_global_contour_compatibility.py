#!/usr/bin/env python3
"""Iter053: exact common-translation contour compatibility for K4 causal shifts.

For a K4 tree/cycle basis, x_e(y,k)=b_e(k)+a_e.y and the frozen causal
kernel contains x_e-i*s_e*epsilon.  A single cycle-contour translation
    y -> y - i*epsilon*v
reproduces all six shifts iff A v = s, where A has rows a_e.

This is a narrow analyticity/geometry audit only.  It does not test general
correlated/nonlinear contours or define a physical multivariate amplitude.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import TREES, incidence, constrained_edge_flows
from distributional.k4_denominator_pole_topology_control import SIGMA_CLASSES, edge_signs_from_class


def exact_cycle_matrix(tree: str):
    if tree not in TREES:
        raise ValueError(tree)
    y, x, tree_edges, chords, det = constrained_edge_flows(
        tree, (sp.Integer(0),) * 4
    )
    A = sp.Matrix([[sp.diff(xe, yy) for yy in y] for xe in x])
    b = sp.Matrix([sp.simplify(xe.subs({yy: 0 for yy in y})) for xe in x])
    return y, x, A, b, tree_edges, chords, det


def compute(sign_class: str, tree: str):
    sigma, edge_signs, edge_text = edge_signs_from_class(sign_class)
    y, x, A, b, tree_edges, chords, det = exact_cycle_matrix(tree)
    B = incidence()
    s = sp.Matrix(edge_signs)

    rank_A = int(A.rank())
    rank_aug = int(A.row_join(s).rank())
    compatible = rank_A == rank_aug

    # Exact graph identity: columns of A must span the K4 cycle space ker(B).
    BA = sp.simplify(B * A)
    Bs = sp.simplify(B * s)
    BA_zero = all(sp.simplify(z) == 0 for z in BA)
    Bs_zero = all(sp.simplify(z) == 0 for z in Bs)
    cycle_space_dimension = 6 - int(B.rank())
    cycle_basis_complete = BA_zero and rank_A == cycle_space_dimension == 3
    criterion_equivalent = compatible == Bs_zero

    # Chord variables are the coordinate variables themselves, so fixing v by
    # the three chord rows gives a deterministic exact candidate even when the
    # six-equation system is inconsistent.  Its residual localizes the failure.
    v_candidate = sp.Matrix([s[e] for e in chords])
    residual = sp.simplify(A * v_candidate - s)
    residual_zero = all(sp.simplify(z) == 0 for z in residual)

    solution = None
    if compatible:
        solset = sp.linsolve((A, s))
        soltuple = next(iter(solset))
        solution = [str(sp.simplify(z)) for z in soltuple]
        exact_reconstruction = all(
            sp.simplify(z) == 0 for z in (A * sp.Matrix(soltuple) - s)
        )
    else:
        exact_reconstruction = not residual_zero

    # Reconstruct each edge coefficient row directly from x_e.
    row_checks = []
    for e, xe in enumerate(x):
        reconstructed = b[e] + sum(A[e, j] * y[j] for j in range(3))
        row_checks.append(sp.simplify(xe - reconstructed) == 0)

    valid = all([
        abs(int(det)) == 1,
        cycle_basis_complete,
        criterion_equivalent,
        all(row_checks),
        exact_reconstruction,
        residual_zero == compatible,
    ])

    return {
        "iteration": "Iter053",
        "sign_class": sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": tree,
        "tree_edges": list(map(int, tree_edges)),
        "chord_edges": list(map(int, chords)),
        "tree_incidence_det": str(det),
        "A": [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)],
        "rank_A": rank_A,
        "rank_augmented": rank_aug,
        "compatible_uniform_translation": bool(compatible),
        "solution_v": solution,
        "deterministic_chord_candidate_v": list(map(str, v_candidate)),
        "candidate_residual": list(map(str, residual)),
        "B_times_s": list(map(str, Bs)),
        "B_times_A_zero": bool(BA_zero),
        "s_in_cycle_space": bool(Bs_zero),
        "rank_cycle_space": int(cycle_space_dimension),
        "rank_and_graph_criteria_equivalent": bool(criterion_equivalent),
        "edge_row_reconstruction_all_exact": bool(all(row_checks)),
        "valid": bool(valid),
        "claim_lock": (
            "Uniform affine cycle-contour translation compatibility only; no claim about "
            "general correlated/nonlinear contours, multivariate amplitude finiteness, K5, G3, F9 or G8."
        ),
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter053_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter053" and "compatible_uniform_translation" in r:
            rows.append(r)

    expected = len(SIGMA_CLASSES) * len(TREES)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter053 lanes, found {len(rows)}")
    keys = {(r["sign_class"], r["tree"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter053 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    per_class = {}
    basis_consistent = True
    compatible_classes = []
    for sc in SIGMA_CLASSES:
        sr = [r for r in rows if r["sign_class"] == sc]
        vals = [r["compatible_uniform_translation"] for r in sr]
        graph_vals = [r["s_in_cycle_space"] for r in sr]
        same = all(v == vals[0] for v in vals[1:]) and all(v == graph_vals[0] for v in graph_vals[1:])
        basis_consistent = basis_consistent and same and (vals[0] == graph_vals[0])
        if vals[0] and same:
            compatible_classes.append(sc)
        per_class[sc] = {
            "compatible_in_all_tree_bases": bool(vals[0] and same),
            "compatibility_by_tree": {r["tree"]: bool(r["compatible_uniform_translation"]) for r in sr},
            "B_times_s": sr[0]["B_times_s"],
        }

    ncomp = len(compatible_classes)
    if not all_valid or not basis_consistent:
        classification = "ITER053_RECONSTRUCTION_OR_BASIS_INVALID"
    elif ncomp == len(SIGMA_CLASSES):
        classification = "K4_CAUSAL_SHIFTS_GLOBAL_UNIFORM_CONTOUR_COMPATIBLE"
    elif ncomp == 0:
        classification = "K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION"
    else:
        classification = "K4_CAUSAL_SHIFTS_GLOBAL_UNIFORM_CONTOUR_CLASS_DEPENDENT"

    return {
        "iteration": "Iter053",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "basis_consistent": bool(basis_consistent),
        "compatible_class_count": ncomp,
        "compatible_classes": compatible_classes,
        "per_class": per_class,
        "claim_lock": (
            "Exact no/yes statement only for one uniform affine translation of the three K4 cycle variables. "
            "No no-go theorem for general correlated contours or physical causal amplitudes."
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
