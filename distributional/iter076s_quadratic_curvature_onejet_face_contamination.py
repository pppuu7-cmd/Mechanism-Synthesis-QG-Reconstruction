#!/usr/bin/env python3
"""Iter076S: confirm symmetry-allowed quadratic curvature one-jet contamination.

Frozen scientifically by the colliding prereg commit 62bdff74931814d2fbf598b6d0898bcb0140b271
and administratively renumbered without criterion changes in
prereg/ITER076S_QUADRATIC_CURVATURE_ONEJET_FACE_CONTAMINATION.md.
This is a structural exact-algebra gate. It does not select a physical nonlinear
source-to-K4 map and does not establish a physical source one-jet.
"""
from __future__ import annotations

import argparse
import json
import os

import sympy as sp

from distributional.iter073a_k4_signed_cutspace_face_atlas import TREES, Lmat
from distributional.iter073d_transitive_face_cones import TRANS, records_for
from distributional.iter076b_degree2_overlap_jet_complex import restriction_matrix
from distributional.iter076q_hodge_line_sym2_quadratic_descent import (
    PERMS,
    CUT,
    CYCLE,
    edge_action,
    hodge_coords,
    parity,
    restricted,
    sym2,
)

B_EXPECTED = sp.Matrix([
    [1, 0, 0, -1, -1, 0],
    [-1, 0, 1, 1, 0, -1],
    [1, -1, 0, 0, -1, 1],
])

T_EXPECTED = sp.Matrix([
    [-1, -1, -1],
    [-1, -1, 0],
    [1, 0, 1],
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
])


def int_matrix(M: sp.Matrix):
    return [[int(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def primitive_matrix(v: sp.Matrix, rows: int, cols: int) -> sp.Matrix:
    vals = [sp.Rational(x) for x in list(v)]
    den = sp.ilcm(*[x.q for x in vals]) if vals else 1
    ints = [int(x * den) for x in vals]
    g = 0
    for x in ints:
        g = sp.igcd(g, abs(x))
    if g:
        ints = [x // g for x in ints]
    first = next((x for x in ints if x), 1)
    if first < 0:
        ints = [-x for x in ints]
    return sp.Matrix(rows, cols, ints)


def curvature_system():
    xs = sp.symbols("b0:18")
    K = sp.Matrix(3, 6, xs)
    eqs = []
    for p in PERMS:
        R = edge_action(p)
        C = restricted(CUT, R)
        Z = restricted(CYCLE, R)
        eqs.extend(list(K * sym2(C) - parity(p) * Z * K))
    A, _ = sp.linear_eq_to_matrix(eqs, xs)
    ns = A.nullspace()
    generator = primitive_matrix(ns[0], 3, 6) if len(ns) == 1 else None
    return A, ns, generator


def curvature_covariant(K: sp.Matrix) -> bool:
    for p in PERMS:
        R = edge_action(p)
        C = restricted(CUT, R)
        Z = restricted(CYCLE, R)
        if K * sym2(C) != parity(p) * Z * K:
            return False
    return True


def contamination_map(K: sp.Matrix) -> sp.Matrix:
    """Map a source one-jet ell to degree-two coefficients in S0 cycle coords."""
    X = hodge_coords()
    Xi = X.inv()
    z0, z1, z2 = sp.symbols("z0 z1 z2")
    z = sp.Matrix([z0, z1, z2])
    c = Xi * z
    m = sp.Matrix([
        c[0] ** 2,
        c[1] ** 2,
        c[2] ** 2,
        c[0] * c[1],
        c[0] * c[2],
        c[1] * c[2],
    ])
    D = -Xi * (K * m)
    l0, l1, l2 = sp.symbols("l0 l1 l2")
    ell = sp.Matrix([[l0, l1, l2]])
    expr = sp.expand((ell * D)[0])
    poly = sp.Poly(expr, z0, z1, z2)
    mons = [z0 ** 2, z0 * z1, z0 * z2, z1 ** 2, z1 * z2, z2 ** 2]
    ls = [l0, l1, l2]
    return sp.Matrix([
        [sp.expand(poly.coeff_monomial(mon)).coeff(l) for l in ls]
        for mon in mons
    ])


def basis_transform_from_s0(L: sp.Matrix) -> sp.Matrix:
    L0, _ = Lmat("S0")
    cols = [L0.gauss_jordan_solve(L[:, j])[0] for j in range(3)]
    M = sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])
    if L0 * M != L:
        raise AssertionError("cycle-basis coordinate transport failed")
    return M


def collision_nullspace(L: sp.Matrix, S) -> sp.Matrix:
    A = L[list(sorted(S)), :] if S else sp.zeros(0, 3)
    ns = A.nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(3, 0)


def lane_a():
    A, ns, generator = curvature_system()
    expected_covariant = curvature_covariant(B_EXPECTED)
    generator_matches = generator is not None and generator == B_EXPECTED
    valid = A.rank() == 17 and len(ns) == 1 and expected_covariant and generator_matches
    return {
        "iteration": "Iter076S",
        "lane": "A",
        "valid": bool(valid),
        "covariance_system_rank": int(A.rank()),
        "twisted_quadratic_hom_dimension": len(ns),
        "primitive_generator": int_matrix(generator) if generator is not None else None,
        "expected_generator_matches": bool(generator_matches),
        "expected_generator_covariant": bool(expected_covariant),
        "physical_nonzero_curvature_selected": False,
    }


def lane_b():
    T = contamination_map(B_EXPECTED)
    T0 = contamination_map(sp.zeros(3, 6))
    valid = T.rank() == 3 and T == T_EXPECTED and T0 == sp.zeros(6, 3)
    return {
        "iteration": "Iter076S",
        "lane": "B",
        "valid": bool(valid),
        "contamination_map": int_matrix(T),
        "contamination_rank": int(T.rank()),
        "matches_frozen_prediction": bool(T == T_EXPECTED),
        "zero_curvature_contamination_zero": bool(T0 == sp.zeros(6, 3)),
        "physical_source_one_jet_assumed": False,
    }


def lane_c():
    T = contamination_map(B_EXPECTED)
    L0, _ = Lmat("S0")
    if L0 != CYCLE:
        raise AssertionError("Iter076Q cycle basis is not Iter073/076B S0 basis")

    lane_rows = {}
    global_blocks = []
    nonzero = 0
    zero = 0
    all_lane_multisets_ok = True
    all_lane_stacked_rank2 = True
    basis_unimodular = True

    for label in TRANS:
        lane_rows[label] = {}
        for tree in TREES:
            L, _ = Lmat(tree)
            M = basis_transform_from_s0(L)
            basis_unimodular &= abs(int(M.det())) == 1
            coeff_transport = restriction_matrix(M)
            ranks = []
            blocks = []
            face_rows = []
            for rec in records_for(label, tree):
                S = frozenset(rec["S"])
                N = collision_nullspace(L, S)
                Rface = restriction_matrix(N)
                F = Rface * coeff_transport * T
                r = int(F.rank())
                ranks.append(r)
                blocks.append(F)
                global_blocks.append(F)
                if r:
                    nonzero += 1
                else:
                    zero += 1
                face_rows.append({
                    "S": sorted(S),
                    "collision_dimension": int(N.cols),
                    "contamination_restriction_rank": r,
                })
            stack = sp.Matrix.vstack(*blocks) if blocks else sp.zeros(0, 3)
            lane_rank = int(stack.rank())
            multiset_ok = sorted(ranks) == [0, 0, 0, 0, 1, 1]
            all_lane_multisets_ok &= multiset_ok
            all_lane_stacked_rank2 &= lane_rank == 2
            lane_rows[label][tree] = {
                "basis_det": int(M.det()),
                "face_rank_multiset": sorted(ranks),
                "stacked_face_contamination_rank": lane_rank,
                "onejet_invisible_dimension_for_fixed_class_tree": 3 - lane_rank,
                "faces": face_rows,
            }

    global_stack = sp.Matrix.vstack(*global_blocks) if global_blocks else sp.zeros(0, 3)
    global_rank = int(global_stack.rank())
    valid = bool(
        basis_unimodular
        and nonzero == 32
        and zero == 64
        and all_lane_multisets_ok
        and all_lane_stacked_rank2
        and global_rank == 3
    )
    return {
        "iteration": "Iter076S",
        "lane": "C",
        "valid": valid,
        "face_restrictions_total": nonzero + zero,
        "nonzero_rank1_face_restrictions": nonzero,
        "zero_face_restrictions": zero,
        "every_class_tree_rank_multiset_000011": bool(all_lane_multisets_ok),
        "every_class_tree_stacked_rank_two": bool(all_lane_stacked_rank2),
        "all_cycle_basis_transforms_unimodular": bool(basis_unimodular),
        "global_transitive_family_contamination_rank": global_rank,
        "global_nonzero_onejet_invisible": bool(global_rank < 3),
        "lanes": lane_rows,
    }


def lane_d():
    bad = B_EXPECTED.copy()
    bad[0, 0] += 1
    bad_rejected = not curvature_covariant(bad)

    Tzero = sp.zeros(6, 3)
    zero_face_ok = True
    checked = 0
    for label in TRANS:
        for tree in TREES:
            L, _ = Lmat(tree)
            M = basis_transform_from_s0(L)
            coeff_transport = restriction_matrix(M)
            for rec in records_for(label, tree):
                N = collision_nullspace(L, frozenset(rec["S"]))
                F = restriction_matrix(N) * coeff_transport * Tzero
                zero_face_ok &= F == sp.zeros(F.rows, F.cols)
                checked += 1

    locks = {
        "physical_quadratic_curvature_selected": False,
        "physical_source_one_jet_established": False,
        "one_jet_can_be_bypassed_by_symmetry": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = bool(
        bad_rejected
        and zero_face_ok
        and checked == 96
        and not locks["physical_quadratic_curvature_selected"]
        and not locks["physical_source_one_jet_established"]
        and not locks["one_jet_can_be_bypassed_by_symmetry"]
        and not locks["epsilon_minus1_coefficient_established"]
        and not locks["generic_finite_spin_signed_P3_promoted"]
        and not locks["G3_promoted"]
        and not locks["F9_promoted"]
        and not locks["G8_promoted"]
        and not locks["K5_promoted"]
    )
    return {
        "iteration": "Iter076S",
        "lane": "D",
        "valid": valid,
        "altered_curvature_outside_line_rejected": bool(bad_rejected),
        "zero_curvature_face_contamination_zero": bool(zero_face_ok),
        "zero_control_faces_checked": checked,
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
            if lane in LANES and obj.get("iteration") == "Iter076S":
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076S_UNIQUE_TWISTED_QUADRATIC_CURVATURE_ALLOWS_ONEJET_CONTAMINATION_ON_TRANSITIVE_FACES_EXACT_SCOPED"
        if valid
        else "ITER076S_QUADRATIC_CURVATURE_ONEJET_CONTAMINATION_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076S",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "A unique symmetry-allowed quadratic curvature line exists and generic one-jet contamination survives "
            "the transitive proper-face restriction complex. This does not select a physical curvature or prove a "
            "physical source one-jet is nonzero."
        ),
        "next_admissible_gate": (
            "Audit the source-faithful numerator/Haar-Jacobian one-jet. Separate the exact even Haar contribution "
            "from wedge/numerator and coordinate-Jacobian contributions; do not infer vanishing from denominator-only symmetry."
        ),
        "claim_lock": (
            "No new physics, complete-QG claim, physical nonlinear P3, physical source one-jet, epsilon^-1 coefficient, "
            "causal-vertex finiteness/divergence theorem, or G3/F9/G8/K5 promotion."
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
