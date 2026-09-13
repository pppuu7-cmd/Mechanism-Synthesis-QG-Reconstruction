#!/usr/bin/env python3
"""Iter077A: exact algebraic K5 closure of the minimal Toller front-face data type.

Frozen by prereg/ITER077A_K5_TOLLER_FRONT_FACE_DATA_MODEL.md.
No analytic K5 boundary value or physical source-to-K4 pushforward is promoted.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import wigner_d_small

from distributional.iter076v_matrix_boost_onejet_intertwiner_closure import apply_total_ladder
from distributional.iter076x_toller_normal_blowup_connection import (
    apply_leading_tensor,
    jminus_matrix,
    jplus_matrix,
    jz_matrix,
    leading_shape,
)
from distributional.iter076z_toller_front_face_nonscalar_obstruction import intertwiner_controls, total_jy_state

ROOT = Path(__file__).resolve().parents[1]
I = sp.I


def incidence(n: int):
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    B = sp.zeros(n, len(edges))
    for k, (a, b) in enumerate(edges):
        B[a, k] = -1
        B[b, k] = 1
    return edges, B


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
    return P, E, B


def same_colspace(A: sp.Matrix, B: sp.Matrix) -> bool:
    return A.rank() == B.rank() == A.row_join(B).rank()


def exact_zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def proportional(A: sp.Matrix, B: sp.Matrix) -> bool:
    ratio = None
    for r in range(B.rows):
        for c in range(B.cols):
            a, b = sp.simplify(A[r, c]), sp.simplify(B[r, c])
            if b == 0:
                if a != 0:
                    return False
            else:
                q = sp.simplify(a / b)
                if ratio is None:
                    ratio = q
                elif sp.simplify(q - ratio) != 0:
                    return False
    return exact_zero_matrix(A) if ratio is None else True


def ascending_y_rotation(j, angle):
    Udesc = sp.Matrix(wigner_d_small(j, angle))
    d = Udesc.rows
    P = sp.zeros(d, d)
    for r in range(d):
        P[r, d - 1 - r] = 1
    return sp.simplify(P * Udesc * P)


def lane_a():
    note = (ROOT / "sources" / "ITER077_PARALLEL_FRONTIER_SOURCE_DERIVATION.md").read_text(encoding="utf-8")
    paths = {
        "W": ROOT / "results" / "ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_RESULT.md",
        "X": ROOT / "results" / "ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_RESULT.md",
        "Y": ROOT / "results" / "ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY_RESULT.md",
        "Z": ROOT / "results" / "ITER076Z_TOLLER_FRONT_FACE_NONSCALAR_OBSTRUCTION_RESULT.md",
    }
    texts = {k: p.read_text(encoding="utf-8") for k, p in paths.items()}
    locks = {
        "W_compact_gauge": "ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO" in texts["W"],
        "X_connection": "ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED" in texts["X"],
        "Y_mixed_path": "ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED" in texts["Y"],
        "Z_scalar_no_go": "ITER076Z_SCALAR_RADIAL_STRIP_LEAVES_NONSCALAR_DIRECTION_DEPENDENT_TOLLER_FRONT_FACE_BUNDLE_OBJECT_REQUIRED_EXACT_SCOPED" in texts["Z"],
        "typed_tuple": "FF_e = (w_e, n_e, C_e, A_e)" in note,
        "correlated_boundary_firewall": "correlated_Toller_group_boundary_value_established=false" in note,
        "pushforward_firewall": "physical_source_to_K4_pushforward_established=false" in note,
        "epsilon_firewall": "epsilon_minus1_coefficient_established=false" in note,
    }
    return {"iteration": "Iter077A", "lane": "A", "valid": all(locks.values()), "locks": locks}


def lane_b():
    edges, B = incidence(5)
    base_cut = B.T.columnspace()
    Cbase = sp.Matrix.hstack(*base_cut)
    roots = []
    roots_ok = True
    for root in range(5):
        Br = B.copy()
        Br.row_del(root)
        Cr = Br.T
        ok = Br.rank() == 4 and same_colspace(Cbase, Cr)
        roots_ok &= ok
        roots.append({"root": root, "rank": Br.rank(), "same_cut_space": bool(same_colspace(Cbase, Cr))})

    relabel_ok = True
    cut_ok = True
    cycle_ok = True
    cycle_basis = sp.Matrix.hstack(*[sp.Matrix(v) for v in B.nullspace()])
    for p in itertools.permutations(range(5)):
        P, E, _ = signed_permutation(5, p)
        relabel_ok &= (P * B == B * E)
        cut_ok &= same_colspace(Cbase, E * Cbase)
        cycle_ok &= same_colspace(cycle_basis, E * cycle_basis)

    valid = bool(
        B.rank() == 4 and len(edges) == 10 and len(B.nullspace()) == 6
        and roots_ok and relabel_ok and cut_ok and cycle_ok
    )
    return {
        "iteration": "Iter077A", "lane": "B", "valid": valid,
        "B5_rank": B.rank(), "edge_count": len(edges), "cycle_dim": len(B.nullspace()),
        "roots": roots, "S5_incidence_covariance": bool(relabel_ok),
        "S5_cut_space_invariant": bool(cut_ok), "S5_cycle_space_invariant": bool(cycle_ok),
    }


def lane_c():
    controls = []
    all_ok = True
    angle = sp.pi / 2
    for j in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]:
        _, C = leading_shape(j)
        Jz = jz_matrix(j)
        Jp, Jm = jplus_matrix(j), jminus_matrix(j)
        Jy = sp.simplify((Jp - Jm) / (2 * I))
        comm = sp.simplify(Jy * C - C * Jy)
        A = sp.simplify(C.inv() * comm)
        U = ascending_y_rotation(j, angle)
        Cp = sp.simplify(U * C * U.inv())
        Jyp = sp.simplify(U * Jy * U.inv())
        Ap = sp.simplify(Cp.inv() * (Jyp * Cp - Cp * Jyp))
        covariance = exact_zero_matrix(sp.simplify(Ap - U * A * U.inv()))
        scale_invariant = exact_zero_matrix(sp.simplify((-C).inv() * (Jy * (-C) - (-C) * Jy) - A))
        invertible = sp.simplify(C.det()) != 0
        stabilizer = exact_zero_matrix(Jz * C - C * Jz)
        transverse = not exact_zero_matrix(comm)
        nonscalar_generator = (not proportional(A, Jy)) if j >= 1 else True
        ok = bool(invertible and stabilizer and transverse and nonscalar_generator and covariance and scale_invariant)
        all_ok &= ok
        controls.append({
            "j": str(j), "invertible": bool(invertible), "Jz_commutes": bool(stabilizer),
            "transverse_commutator_nonzero": bool(transverse),
            "relative_connection_not_scalar_Jy_for_j_ge_1": bool(nonscalar_generator),
            "adjoint_covariance": bool(covariance), "branch_scale_invariant": bool(scale_invariant),
        })
    return {"iteration": "Iter077A", "lane": "C", "valid": bool(all_ok), "controls": controls}


def lane_d():
    rows = []
    total = gauge_zero = transverse_zero = transverse_nonzero = 0
    all_ok = True
    for spins, k, state in intertwiner_controls():
        total += 1
        gauge_jy = total_jy_state(state, spins)
        F = apply_leading_tensor(state, spins)
        front_jy = total_jy_state(F, spins)
        all_half = all(s == sp.Rational(1, 2) for s in spins)
        gz = not gauge_jy
        expected_front_zero = all_half
        fz = not front_jy
        ok = gz and (fz == expected_front_zero)
        all_ok &= ok
        gauge_zero += int(gz)
        transverse_zero += int(fz)
        transverse_nonzero += int(not fz)
        rows.append({
            "spins": [str(s) for s in spins], "k": str(k),
            "common_compact_generator_killed": bool(gz),
            "front_face_transverse_connection_zero": bool(fz),
            "special_all_spin_half": bool(all_half), "prediction_match": bool(ok),
        })
    locks = {
        "front_face_data_schema_complete": True,
        "K5_incidence_covariance_exact": True,
        "compact_gauge_action_closed": True,
        "generic_transverse_connection_independent": True,
        "correlated_analytic_boundary_value_established": False,
        "physical_source_to_K4_pushforward_established": False,
        "epsilon_minus1_coefficient_established": False,
        "G3_promoted": False, "F9_promoted": False, "G8_promoted": False, "K5_promoted": False,
    }
    valid = bool(all_ok and total == 7 and gauge_zero == 7 and transverse_zero == 2 and transverse_nonzero == 5)
    return {
        "iteration": "Iter077A", "lane": "D", "valid": valid,
        "intertwiners_checked": total, "gauge_zero": gauge_zero,
        "front_transverse_zero": transverse_zero, "front_transverse_nonzero": transverse_nonzero,
        "controls": rows, "scope_locks": locks,
    }


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
            if obj.get("iteration") == "Iter077A" and lane in LANES: got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    return {
        "iteration": "Iter077A", "valid": bool(valid),
        "classification": "ITER077A_MINIMAL_TOLLER_FRONT_FACE_DATA_TYPE_CLOSES_COVARIANTLY_ON_K5_INCIDENCE_EXACT_SCOPED" if valid else "ITER077A_K5_FRONT_FACE_DATA_TYPE_CLOSURE_FAIL",
        "lanes_found": sorted(got), "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "next_admissible_gate": "Use this exact schema in a correlated blown-up/polyhomogeneous K5 boundary object; analytic boundary-value hypotheses remain separate.",
        "claim_lock": "No analytic K5 boundary value, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion.",
    }


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lane", choices=LANES); ap.add_argument("--aggregate-dir"); ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir): raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj, indent=2, sort_keys=True)); write(obj, args.output)
    if not obj.get("valid"): raise SystemExit(1)


if __name__ == "__main__": main()
