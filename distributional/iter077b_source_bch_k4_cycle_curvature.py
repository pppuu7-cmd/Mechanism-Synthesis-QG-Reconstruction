#!/usr/bin/env python3
"""Iter077B: exact BCH quadratic cycle curvature on gauge-fixed K5 -> K4 controls.

Frozen by prereg/ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md.
This is a source relative-coordinate result, not a physical Toller/front-face pushforward.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def incidence(n: int):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    B = sp.zeros(n, len(edges))
    for k, (a, b) in enumerate(edges):
        B[a, k] = -1
        B[b, k] = 1
    return edges, B


def same_colspace(A: sp.Matrix, B: sp.Matrix) -> bool:
    return A.rank() == B.rank() == A.row_join(B).rank()


def signed_permutation(n: int, p):
    edges, B = incidence(n)
    idx = {e: k for k, e in enumerate(edges)}
    P = sp.zeros(n, n)
    E = sp.zeros(len(edges), len(edges))
    for a in range(n):
        P[p[a], a] = 1
    for k, (a, b) in enumerate(edges):
        pa, pb = p[a], p[b]
        if pa < pb:
            e, s = (pa, pb), 1
        else:
            e, s = (pb, pa), -1
        E[idx[e], k] = s
    return P, E


def parity(p) -> int:
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def k4_objects():
    edges, B = incidence(4)
    Br = B.copy(); Br.row_del(3)
    Pcut = sp.simplify(Br.T * (Br * Br.T).inv() * Br)
    Pcyc = sp.simplify(sp.eye(6) - Pcut)
    H = sp.zeros(6, 6)
    # Edges: 01,02,03,12,13,23. H e_ij = eps_ijkl e_kl.
    mapping = {0: (5, 1), 1: (4, -1), 2: (3, 1), 3: (2, 1), 4: (1, -1), 5: (0, 1)}
    for c, (r, s) in mapping.items(): H[r, c] = s
    return edges, B, Br, Pcut, Pcyc, H


def cross(a, b):
    return sp.Matrix(a).cross(sp.Matrix(b))


def edge_linear(X):
    edges, *_ = k4_objects()
    return sp.Matrix.hstack(*[sp.Matrix(X[a] - X[b]) for a, b in edges]).T


def edge_quadratic(X, coeff=sp.Rational(1, 2)):
    edges, *_ = k4_objects()
    return sp.Matrix.hstack(*[sp.simplify(coeff * cross(X[a], X[b])) for a, b in edges]).T


def q_cycle(X, coeff=sp.Rational(1, 2)):
    *_, Pcyc, _H = k4_objects()
    return sp.simplify(Pcyc * edge_quadratic(X, coeff))


def generic_controls():
    raw = [
        [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)],
        [(1, 2, 0), (0, 1, 1), (2, 0, 1), (1, -1, 2), (2, 1, -1)],
        [(2, -1, 1), (1, 1, 0), (0, 2, 1), (-1, 1, 2), (1, 0, -2)],
    ]
    return [[sp.Matrix(v) for v in control] for control in raw]


def commuting_control():
    axis = sp.Matrix([1, 2, -1])
    return [k * axis for k in [1, 2, -1, 3, -2]]


def local_for_root(X5, root):
    nodes = [a for a in range(5) if a != root]
    return nodes, [X5[a] for a in nodes]


def matrix_zero(M):
    return M == sp.zeros(*M.shape)


def lane_a():
    edges, B, Br, _Pcut, _Pcyc, H = k4_objects()
    cut = Br.T
    cycle = sp.Matrix.hstack(*[sp.Matrix(v) for v in B.nullspace()])
    h2 = H * H == sp.eye(6)
    h_cut_cycle = B * H * cut == sp.zeros(4, 3)
    h_cycle_cut = same_colspace(cut, H * cycle)
    relabel = True
    h_twist = True
    for p in itertools.permutations(range(4)):
        P, E = signed_permutation(4, p)
        relabel &= (P * B == B * E)
        h_twist &= (E * H * E.T == parity(p) * H)
    valid = bool(B.rank() == 3 and cut.rank() == 3 and len(B.nullspace()) == 3 and h2 and h_cut_cycle and h_cycle_cut and relabel and h_twist)
    return {
        "iteration": "Iter077B", "lane": "A", "valid": valid,
        "edge_order": [f"{a}{b}" for a, b in edges], "incidence_rank": B.rank(),
        "cut_dim": cut.rank(), "cycle_dim": len(B.nullspace()), "H_squared_identity": bool(h2),
        "H_cut_to_cycle": bool(h_cut_cycle), "H_cycle_to_cut": bool(h_cycle_cut),
        "S4_incidence_covariance": bool(relabel), "S4_Hodge_orientation_character": bool(h_twist),
    }


def lane_b():
    _edges, B, Br, Pcut, Pcyc, _H = k4_objects()
    rows = []
    all_ok = True
    s = sp.Rational(3, 2)
    c = sp.symbols("c")
    for ci, X5 in enumerate(generic_controls()):
        for root in range(5):
            nodes, X = local_for_root(X5, root)
            L = edge_linear(X)
            Q = edge_quadratic(X)
            Qc = sp.simplify(Pcyc * Q)
            cut_linear = matrix_zero(sp.simplify((sp.eye(6) - Pcut) * L))
            nonzero = not matrix_zero(Qc)
            scaled_L = edge_linear([s * x for x in X])
            scaled_Qc = q_cycle([s * x for x in X])
            scale_ok = matrix_zero(sp.simplify(scaled_L - s * L)) and matrix_zero(sp.simplify(scaled_Qc - s**2 * Qc))
            symbolic_Qc = q_cycle(X, c)
            coeff_linear = matrix_zero(sp.simplify(symbolic_Qc - 2 * c * Qc))
            ok = cut_linear and nonzero and scale_ok and coeff_linear
            all_ok &= ok
            rows.append({
                "control": ci, "root": root, "nodes": nodes,
                "linear_in_cut": bool(cut_linear), "quadratic_cycle_nonzero": bool(nonzero),
                "homogeneous_scaling": bool(scale_ok), "BCH_coefficient_linear": bool(coeff_linear),
            })
    comm_rows = []
    comm_ok = True
    X5 = commuting_control()
    for root in range(5):
        _nodes, X = local_for_root(X5, root)
        Qc = q_cycle(X)
        zero = matrix_zero(Qc)
        comm_ok &= zero
        comm_rows.append({"root": root, "quadratic_cycle_zero": bool(zero)})
    valid = bool(all_ok and comm_ok)
    return {
        "iteration": "Iter077B", "lane": "B", "valid": valid,
        "generic_controls": rows, "commuting_control": comm_rows,
        "source_BCH_coefficient": "1/2",
    }


def lane_c():
    _edges, B, Br, _Pcut, Pcyc, H = k4_objects()
    all_ok = True
    rows = []
    for ci, X5 in enumerate(generic_controls()):
        for root in range(5):
            _nodes, X = local_for_root(X5, root)
            Qc = q_cycle(X)
            root_nonzero = not matrix_zero(Qc)
            cov = True
            twist = True
            cycle_ok = (B * Qc == sp.zeros(4, 3))
            for p in itertools.permutations(range(4)):
                _P, E = signed_permutation(4, p)
                Xp = [None] * 4
                for old in range(4): Xp[p[old]] = X[old]
                Qp = q_cycle(Xp)
                cov &= matrix_zero(sp.simplify(Qp - E * Qc))
                twist &= matrix_zero(sp.simplify(H * Qp - parity(p) * E * H * Qc))
                cycle_ok &= (B * Qp == sp.zeros(4, 3))
            Hcut = same_colspace(Br.T, H * Qc) if Qc.rank() else True
            ok = root_nonzero and cov and twist and cycle_ok and Hcut
            all_ok &= ok
            rows.append({
                "control": ci, "root": root, "generic_cycle_nonzero": bool(root_nonzero),
                "S4_cycle_covariance": bool(cov), "S4_Hodge_twisted_covariance": bool(twist),
                "cycle_membership_preserved": bool(cycle_ok), "H_Qcycle_in_cut_space": bool(Hcut),
            })
    return {"iteration": "Iter077B", "lane": "C", "valid": bool(all_ok), "controls": rows, "all_five_roots_same_classification": bool(all_ok)}


def lane_d():
    note = (ROOT / "sources" / "ITER077_PARALLEL_FRONTIER_SOURCE_DERIVATION.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md").read_text(encoding="utf-8")
    locks = {
        "source_BCH_quadratic_cycle_curvature_selected": True,
        "source_BCH_coefficient": "1/2",
        "commuting_control_curvature_zero": True,
        "canonical_Hodge_twisted_representative_available": True,
        "front_face_Toller_pushforward_established": False,
        "physical_reduced_K4_numerator_coefficient_established": False,
        "epsilon_minus1_coefficient_established": False,
        "correlated_K5_boundary_value_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False, "F9_promoted": False, "G8_promoted": False, "K5_promoted": False,
    }
    textual = all(x in note + prereg for x in ["(1/2)[X_a,X_b]", "physical", "epsilon_minus1_coefficient_established=false"])
    return {"iteration": "Iter077B", "lane": "D", "valid": bool(textual), "scope_locks": locks}


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def write(obj, path):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"): continue
            try: obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception: continue
            lane = obj.get("lane")
            if obj.get("iteration") == "Iter077B" and lane in LANES: got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    return {
        "iteration": "Iter077B", "valid": bool(valid),
        "classification": "ITER077B_SOURCE_BCH_SECOND_ORDER_SELECTS_NONZERO_K4_CYCLE_CURVATURE_EXACT_COORDINATE_SCOPED" if valid else "ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE_SELECTION_FAIL",
        "lanes_found": sorted(got), "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "source_BCH_coefficient": "1/2",
        "next_admissible_gate": "Compose the Iter077A front-face bundle data with the source BCH quadratic relative-coordinate map before any reduced K4 numerator or epsilon^-1 analysis.",
        "claim_lock": "No physical Toller/front-face pushforward, reduced K4 numerator coefficient, epsilon^-1 coefficient, correlated K5 boundary value, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion.",
    }


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lane", choices=LANES); ap.add_argument("--aggregate-dir"); ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir): raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj, indent=2, sort_keys=True)); write(obj, args.output)
    if not obj.get("valid"): raise SystemExit(1)


if __name__ == "__main__": main()
