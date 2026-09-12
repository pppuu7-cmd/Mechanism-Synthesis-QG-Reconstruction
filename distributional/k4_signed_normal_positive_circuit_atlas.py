#!/usr/bin/env python3
"""Iter055: exact minimal positive-circuit atlas of K4 signed normals.

For each causal sign class s and K4 cycle basis A, form M=diag(s)A and
exhaustively enumerate all support-minimal positive dependences among the six
row normals.  Then verify exact tree-basis invariance and full S4 covariance.

Preregistration: status/ITERATION_055.md at commit
5ef00a72f034d2dbf943ccd5e0c7ab5662bb8d21.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import EDGES, EDGE_NAMES, TREES, incidence
from distributional.k4_denominator_pole_topology_control import SIGMA_CLASSES, edge_signs_from_class
from distributional.k4_global_contour_compatibility import exact_cycle_matrix

ALL_PERMS = tuple(itertools.permutations(range(4)))
MAX_SUPPORT = 4
EXPECTED_SUPPORT_TESTS = sum(math.comb(6, k) for k in range(1, MAX_SUPPORT + 1))
EDGE_TO_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}


def _strict_positive(z):
    return sp.simplify(z).is_positive is True


def positive_dependence_on_support(M: sp.Matrix, support):
    """Return unique normalized exact positive weights or None.

    For a support-minimal positive dependence in R^3 with support <=4, the
    normalized system [M_S^T; 1...1] w = [0,0,0,1] is unique.  We test rank
    exactly and accept only strictly positive rational/algebraic-exact weights.
    """
    support = tuple(support)
    k = len(support)
    C = sp.Matrix([
        [M[j, 0] for j in support],
        [M[j, 1] for j in support],
        [M[j, 2] for j in support],
        [sp.Integer(1) for _ in support],
    ])
    rhs = sp.Matrix([0, 0, 0, 1])
    if int(C.rank()) != k or int(C.row_join(rhs).rank()) != k:
        return None
    solset = sp.linsolve((C, rhs))
    if solset == sp.EmptySet:
        return None
    vals = tuple(sp.simplify(z) for z in next(iter(solset)))
    if len(vals) != k or not all(_strict_positive(z) for z in vals):
        return None
    weighted = sp.zeros(3, 1)
    for idx, w in zip(support, vals):
        weighted += w * M[idx, :].T
    if sp.simplify(sum(vals) - 1) != 0:
        return None
    if any(sp.simplify(z) != 0 for z in weighted):
        return None
    return vals


def complete_minimal_positive_circuits(M: sp.Matrix):
    raw = {}
    tested = 0
    for k in range(1, MAX_SUPPORT + 1):
        for support in itertools.combinations(range(M.rows), k):
            tested += 1
            w = positive_dependence_on_support(M, support)
            if w is not None:
                raw[tuple(support)] = w

    minimal = {}
    for support, weights in sorted(raw.items(), key=lambda kv: (len(kv[0]), kv[0])):
        sset = set(support)
        if any(set(prev).issubset(sset) for prev in minimal):
            continue
        minimal[support] = weights

    # Independent minimality validation against every proper subset, not just
    # previously retained supports.
    minimality_valid = True
    for support in minimal:
        for r in range(1, len(support)):
            for sub in itertools.combinations(support, r):
                if positive_dependence_on_support(M, sub) is not None:
                    minimality_valid = False

    reconstruction_valid = True
    for support, weights in minimal.items():
        weighted = sp.zeros(3, 1)
        for idx, w in zip(support, weights):
            weighted += w * M[idx, :].T
        reconstruction_valid = reconstruction_valid and all([
            all(_strict_positive(w) for w in weights),
            sp.simplify(sum(weights) - 1) == 0,
            all(sp.simplify(z) == 0 for z in weighted),
        ])

    rows = []
    for support, weights in minimal.items():
        rows.append({
            "support": list(support),
            "edge_names": [EDGE_NAMES[i] for i in support],
            "size": len(support),
            "weights": [str(w) for w in weights],
        })
    return rows, {
        "tested_support_count": tested,
        "expected_support_count": EXPECTED_SUPPORT_TESTS,
        "raw_positive_support_count": len(raw),
        "minimal_circuit_count": len(minimal),
        "minimality_valid": bool(minimality_valid),
        "reconstruction_valid": bool(reconstruction_valid),
    }


def compute_atlas_one(sign_class: str, tree: str):
    sigma, edge_signs, edge_text = edge_signs_from_class(sign_class)
    y, x, A, b, tree_edges, chords, det = exact_cycle_matrix(tree)
    B = incidence()
    M = sp.diag(*list(sp.Matrix(edge_signs))) * A
    BA = sp.simplify(B * A)

    cycle_basis_valid = all([
        abs(int(det)) == 1,
        int(A.rank()) == 3,
        all(sp.simplify(z) == 0 for z in BA),
    ])
    row_reconstruction = []
    for e, xe in enumerate(x):
        rec = b[e] + sum(A[e, j] * y[j] for j in range(3))
        row_reconstruction.append(sp.simplify(xe - rec) == 0)

    circuits, meta = complete_minimal_positive_circuits(M)
    valid = all([
        cycle_basis_valid,
        all(row_reconstruction),
        meta["tested_support_count"] == EXPECTED_SUPPORT_TESTS,
        meta["minimality_valid"],
        meta["reconstruction_valid"],
    ])

    return {
        "sign_class": sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": tree,
        "tree_edges": list(map(int, tree_edges)),
        "chord_edges": list(map(int, chords)),
        "A": [[str(A[i, j]) for j in range(3)] for i in range(6)],
        "M": [[str(M[i, j]) for j in range(3)] for i in range(6)],
        "circuits": circuits,
        "circuit_supports": [c["support"] for c in circuits],
        "circuit_size_histogram": {
            str(k): sum(1 for c in circuits if c["size"] == k)
            for k in range(1, MAX_SUPPORT + 1)
        },
        "circuit_meta": meta,
        "cycle_basis_valid": bool(cycle_basis_valid),
        "row_reconstruction_all_exact": bool(all(row_reconstruction)),
        "valid": bool(valid),
    }


def vertex_permutation_action(sign_class: str, perm):
    sigma, edge_signs, _ = edge_signs_from_class(sign_class)
    new_sigma = [None] * 4
    for old_v in range(4):
        new_sigma[perm[old_v]] = int(sigma[old_v])
    gauge = new_sigma[0]
    new_sigma = [int(gauge * x) for x in new_sigma]
    if new_sigma[0] != 1:
        raise RuntimeError("sigma_0 regauging failed")
    target_class = "".join("+" if x > 0 else "-" for x in new_sigma[1:])
    if target_class not in SIGMA_CLASSES:
        raise RuntimeError(f"invalid target class {target_class}")

    edge_map = []
    for a, b in EDGES:
        mapped = tuple(sorted((perm[a], perm[b])))
        if mapped not in EDGE_TO_INDEX:
            raise RuntimeError(f"invalid mapped edge {mapped}")
        edge_map.append(EDGE_TO_INDEX[mapped])
    if sorted(edge_map) != list(range(6)):
        raise RuntimeError("edge map is not a bijection")

    # Independent sign-vector covariance check.
    target_edge_signs = edge_signs_from_class(target_class)[1]
    mapped_signs = [None] * 6
    for old_e, new_e in enumerate(edge_map):
        mapped_signs[new_e] = int(edge_signs[old_e])
    sign_covariant = tuple(mapped_signs) == tuple(map(int, target_edge_signs))

    return target_class, tuple(edge_map), bool(sign_covariant)


def mapped_supports(supports, edge_map):
    return tuple(sorted(
        tuple(sorted(edge_map[i] for i in support))
        for support in supports
    ))


def atlas_signature(row):
    return tuple(sorted(tuple(map(int, s)) for s in row["circuit_supports"]))


def build_orbits(class_map_edges):
    adjacency = {sc: set() for sc in SIGMA_CLASSES}
    for rec in class_map_edges:
        adjacency[rec["source_class"]].add(rec["target_class"])
        adjacency[rec["target_class"]].add(rec["source_class"])
    seen = set()
    orbits = []
    for sc in SIGMA_CLASSES:
        if sc in seen:
            continue
        stack = [sc]
        comp = set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adjacency[x] - comp)
        seen |= comp
        orbits.append(sorted(comp))
    return sorted(orbits, key=lambda c: (len(c), c))


def run_full_audit():
    rows = []
    for sc in SIGMA_CLASSES:
        for tree in sorted(TREES):
            rows.append(compute_atlas_one(sc, tree))

    all_valid = all(r["valid"] for r in rows)

    by_class_tree = {(r["sign_class"], r["tree"]): r for r in rows}
    basis_consistent = True
    per_class = {}
    canonical_tree = "P0"
    canonical_atlas = {}
    for sc in SIGMA_CLASSES:
        signatures = {tree: atlas_signature(by_class_tree[(sc, tree)]) for tree in sorted(TREES)}
        ref = signatures[canonical_tree]
        same = all(sig == ref for sig in signatures.values())
        basis_consistent = basis_consistent and same
        canonical_atlas[sc] = ref
        ref_row = by_class_tree[(sc, canonical_tree)]
        per_class[sc] = {
            "basis_invariant": bool(same),
            "circuit_count": len(ref),
            "circuit_size_histogram": ref_row["circuit_size_histogram"],
            "canonical_supports": [list(s) for s in ref],
            "canonical_edge_supports": [[EDGE_NAMES[i] for i in s] for s in ref],
        }

    permutation_records = []
    s4_covariant = True
    all_edge_maps_valid = True
    all_sign_maps_valid = True
    for sc in SIGMA_CLASSES:
        source_supports = canonical_atlas[sc]
        for perm in ALL_PERMS:
            target, edge_map, sign_ok = vertex_permutation_action(sc, perm)
            transformed = mapped_supports(source_supports, edge_map)
            target_supports = canonical_atlas[target]
            atlas_ok = transformed == target_supports
            edge_ok = sorted(edge_map) == list(range(6))
            all_edge_maps_valid = all_edge_maps_valid and edge_ok
            all_sign_maps_valid = all_sign_maps_valid and sign_ok
            s4_covariant = s4_covariant and edge_ok and sign_ok and atlas_ok
            permutation_records.append({
                "source_class": sc,
                "perm": list(map(int, perm)),
                "target_class": target,
                "edge_map": list(map(int, edge_map)),
                "edge_map_valid": bool(edge_ok),
                "sign_vector_covariant": bool(sign_ok),
                "atlas_covariant": bool(atlas_ok),
            })

    orbits = build_orbits(permutation_records)
    orbit_summaries = []
    for orbit in orbits:
        orbit_summaries.append({
            "classes": orbit,
            "size": len(orbit),
            "circuit_counts": {sc: per_class[sc]["circuit_count"] for sc in orbit},
            "circuit_size_histograms": {sc: per_class[sc]["circuit_size_histogram"] for sc in orbit},
        })

    structural_valid = all([
        all_valid,
        all_edge_maps_valid,
        all_sign_maps_valid,
        len(permutation_records) == len(SIGMA_CLASSES) * len(ALL_PERMS),
        sum(len(o) for o in orbits) == len(SIGMA_CLASSES),
        len({sc for o in orbits for sc in o}) == len(SIGMA_CLASSES),
    ])

    if not structural_valid:
        classification = "ITER055_CIRCUIT_ATLAS_INVALID"
    elif not basis_consistent:
        classification = "K4_SIGNED_NORMAL_CIRCUIT_ATLAS_BASIS_DEPENDENT"
    elif not s4_covariant:
        classification = "K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT"
    else:
        classification = "K4_SIGNED_NORMAL_CIRCUIT_ATLAS_BASIS_AND_S4_COVARIANT"

    return {
        "iteration": "Iter055",
        "classification": classification,
        "lane_count": len(rows),
        "support_tests_per_lane": EXPECTED_SUPPORT_TESTS,
        "total_support_tests": len(rows) * EXPECTED_SUPPORT_TESTS,
        "all_lanes_valid": bool(all_valid),
        "basis_consistent": bool(basis_consistent),
        "s4_covariant": bool(s4_covariant),
        "all_edge_maps_valid": bool(all_edge_maps_valid),
        "all_sign_maps_valid": bool(all_sign_maps_valid),
        "permutation_check_count": len(permutation_records),
        "causal_class_orbits_under_S4": orbits,
        "orbit_summaries": orbit_summaries,
        "per_class": per_class,
        "lanes": rows,
        "permutation_records": permutation_records,
        "claim_lock": (
            "Exact signed-normal minimal-positive-circuit and covariance atlas only; no contour prescription, "
            "physical amplitude, K5, G3, F9, G8, new-physics or general no-go claim."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = run_full_audit()
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "iteration": out["iteration"],
        "classification": out["classification"],
        "lane_count": out["lane_count"],
        "total_support_tests": out["total_support_tests"],
        "basis_consistent": out["basis_consistent"],
        "s4_covariant": out["s4_covariant"],
        "causal_class_orbits_under_S4": out["causal_class_orbits_under_S4"],
        "per_class": out["per_class"],
    }, indent=2))


if __name__ == "__main__":
    main()
