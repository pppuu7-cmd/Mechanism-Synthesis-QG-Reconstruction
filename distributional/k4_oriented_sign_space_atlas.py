#!/usr/bin/env python3
"""Iter057: complete 64-vector K4 oriented pole-sign atlas.

Preregistered at commit 00c92f5f35f21209e4501a4ff8dcbd00e1d3a39b
before implementation/output.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import EDGES, EDGE_NAMES, TREES, incidence
from distributional.k4_denominator_pole_topology_control import SIGMA_CLASSES, edge_signs_from_class
from distributional.k4_global_contour_compatibility import exact_cycle_matrix
from distributional.k4_signed_normal_positive_circuit_atlas import complete_minimal_positive_circuits

EDGE_TO_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
PERMS = tuple(itertools.permutations(range(4)))
ALL_SIGNS = tuple(itertools.product((1, -1), repeat=6))
EXPECTED_LANES = len(ALL_SIGNS) * len(TREES)
EXPECTED_SUPPORT_TESTS = EXPECTED_LANES * 56
EXPECTED_ACTIONS = len(ALL_SIGNS) * len(PERMS)


def sign_text(s):
    return "".join("+" if int(z) > 0 else "-" for z in s)


def independent_edge_action(perm):
    edge_map = [None] * 6
    q_target = [None] * 6
    for old_e, (a, b) in enumerate(EDGES):
        pa, pb = perm[a], perm[b]
        target_edge = EDGE_TO_INDEX[tuple(sorted((pa, pb)))]
        edge_map[old_e] = target_edge
        q_target[target_edge] = 1 if pa < pb else -1
    valid = sorted(edge_map) == list(range(6)) and all(q in (-1, 1) for q in q_target)
    return tuple(edge_map), tuple(q_target), bool(valid)


def transform_signs(s, edge_map, q_target):
    out = [None] * 6
    for old_e, new_e in enumerate(edge_map):
        out[new_e] = int(q_target[new_e] * s[old_e])
    return tuple(out)


def mapped_supports(supports, edge_map):
    return tuple(sorted(
        tuple(sorted(edge_map[i] for i in support))
        for support in supports
    ))


def atlas_one(s, tree):
    _, _, A, _, _, _, det = exact_cycle_matrix(tree)
    B = incidence()
    M = sp.diag(*list(s)) * A
    cycle_valid = all([
        abs(int(det)) == 1,
        int(A.rank()) == 3,
        all(sp.simplify(z) == 0 for z in B * A),
    ])
    circuits, meta = complete_minimal_positive_circuits(M)
    supports = tuple(sorted(tuple(c["support"]) for c in circuits))
    valid = all([
        cycle_valid,
        meta["tested_support_count"] == 56,
        meta["minimality_valid"],
        meta["reconstruction_valid"],
    ])
    hist = {str(k): sum(1 for c in circuits if c["size"] == k) for k in range(1, 5)}
    return {
        "sign_text": sign_text(s),
        "tree": tree,
        "circuit_supports": [list(x) for x in supports],
        "circuit_count": len(supports),
        "circuit_size_histogram": hist,
        "strict_chamber_feasible": len(supports) == 0,
        "support_tests": meta["tested_support_count"],
        "valid": bool(valid),
    }


def connected_orbits(adjacency):
    seen = set()
    out = []
    for node in sorted(adjacency):
        if node in seen:
            continue
        comp = set()
        stack = [node]
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adjacency[x] - comp)
        seen |= comp
        out.append(sorted(comp))
    return sorted(out, key=lambda o: (len(o), o))


def run_audit():
    lanes = []
    canonical = {}
    per_sign = {}
    all_valid = True
    basis_consistent = True

    for s in ALL_SIGNS:
        txt = sign_text(s)
        rows = []
        for tree in sorted(TREES):
            row = atlas_one(s, tree)
            lanes.append(row)
            rows.append(row)
            all_valid = all_valid and row["valid"]
        sigs = {
            r["tree"]: tuple(sorted(tuple(x) for x in r["circuit_supports"]))
            for r in rows
        }
        ref = sigs["P0"]
        same = all(v == ref for v in sigs.values())
        basis_consistent = basis_consistent and same
        canonical[txt] = ref
        p0 = next(r for r in rows if r["tree"] == "P0")
        per_sign[txt] = {
            "basis_invariant": bool(same),
            "strict_chamber_feasible": bool(p0["strict_chamber_feasible"]),
            "circuit_count": int(p0["circuit_count"]),
            "circuit_size_histogram": p0["circuit_size_histogram"],
            "canonical_supports": [list(x) for x in ref],
            "canonical_edge_supports": [[EDGE_NAMES[i] for i in x] for x in ref],
        }

    action_failures = []
    adjacency = {sign_text(s): set() for s in ALL_SIGNS}
    action_count = 0
    all_action_valid = True
    s4_covariant = True
    for s in ALL_SIGNS:
        src = sign_text(s)
        src_supports = canonical[src]
        for perm in PERMS:
            edge_map, q_target, action_valid = independent_edge_action(perm)
            target_tuple = transform_signs(s, edge_map, q_target)
            tgt = sign_text(target_tuple)
            target_exists = tgt in canonical
            transformed_supports = mapped_supports(src_supports, edge_map)
            target_supports = canonical[tgt] if target_exists else tuple()
            atlas_ok = target_exists and transformed_supports == target_supports
            feas_ok = target_exists and (
                per_sign[src]["strict_chamber_feasible"]
                == per_sign[tgt]["strict_chamber_feasible"]
            )
            all_action_valid = all_action_valid and action_valid and target_exists
            s4_covariant = s4_covariant and atlas_ok and feas_ok
            action_count += 1
            adjacency[src].add(tgt)
            adjacency[tgt].add(src)
            if not (action_valid and target_exists and atlas_ok and feas_ok):
                action_failures.append({
                    "source": src,
                    "perm": list(map(int, perm)),
                    "edge_map": list(map(int, edge_map)),
                    "q_target": list(map(int, q_target)),
                    "target": tgt,
                    "action_valid": bool(action_valid),
                    "target_exists": bool(target_exists),
                    "atlas_covariant": bool(atlas_ok),
                    "feasibility_covariant": bool(feas_ok),
                })

    orbits = connected_orbits(adjacency)
    orbit_summaries = []
    orbit_feasibility_consistent = True
    for orbit in orbits:
        feas = {per_sign[s]["strict_chamber_feasible"] for s in orbit}
        consistent = len(feas) == 1
        orbit_feasibility_consistent = orbit_feasibility_consistent and consistent
        orbit_summaries.append({
            "members": orbit,
            "size": len(orbit),
            "feasibility_consistent": bool(consistent),
            "strict_chamber_feasible": next(iter(feas)) if consistent else None,
            "circuit_counts": {s: per_sign[s]["circuit_count"] for s in orbit},
            "circuit_size_histograms": {s: per_sign[s]["circuit_size_histogram"] for s in orbit},
        })

    factorized_signs = sorted({sign_text(edge_signs_from_class(sc)[1]) for sc in SIGMA_CLASSES})
    factorized_set = set(factorized_signs)
    intersecting_orbit_indices = [i for i, o in enumerate(orbits) if factorized_set.intersection(o)]
    closure = sorted({s for i in intersecting_orbit_indices for s in orbits[i]})

    support_total = sum(r["support_tests"] for r in lanes)
    all_valid = all_valid and all_action_valid and support_total == EXPECTED_SUPPORT_TESTS
    all_valid = all_valid and len(lanes) == EXPECTED_LANES and action_count == EXPECTED_ACTIONS

    if not all_valid:
        classification = "ITER057_ORIENTED_SIGN_SPACE_INVALID"
    elif not basis_consistent:
        classification = "K4_ORIENTED_SIGN_SPACE_BASIS_DEPENDENT"
    elif not s4_covariant or not orbit_feasibility_consistent:
        classification = "K4_ORIENTED_SIGN_SPACE_S4_NONCOVARIANT"
    else:
        classification = "K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT"

    feasible_signs = sorted(s for s, v in per_sign.items() if v["strict_chamber_feasible"])
    infeasible_signs = sorted(set(per_sign) - set(feasible_signs))
    return {
        "iteration": "Iter057",
        "classification": classification,
        "sign_vector_count": len(ALL_SIGNS),
        "basis_count": len(TREES),
        "lane_count": len(lanes),
        "support_tests_total": support_total,
        "expected_support_tests_total": EXPECTED_SUPPORT_TESTS,
        "action_count": action_count,
        "expected_action_count": EXPECTED_ACTIONS,
        "all_valid": bool(all_valid),
        "basis_consistent": bool(basis_consistent),
        "orientation_aware_s4_covariant": bool(s4_covariant),
        "orbit_feasibility_consistent": bool(orbit_feasibility_consistent),
        "s4_orbit_count": len(orbits),
        "s4_orbits": orbits,
        "orbit_summaries": orbit_summaries,
        "feasible_sign_count": len(feasible_signs),
        "infeasible_sign_count": len(infeasible_signs),
        "feasible_signs": feasible_signs,
        "factorized_sign_vectors": factorized_signs,
        "factorized_subset_size": len(factorized_signs),
        "factorized_orbit_closure_size": len(closure),
        "factorized_orbit_closure": closure,
        "factorized_intersecting_orbit_indices": intersecting_orbit_indices,
        "per_sign": per_sign,
        "action_failures": action_failures,
        "claim_lock": (
            "Complete exact atlas of the frozen oriented K4 pole-sign surrogate only; no physical causal-sector, "
            "full-Toller permutation, amplitude, K5, G3, F9, G8 or new-physics claim."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    out = run_audit()
    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    summary_keys = [
        "iteration", "classification", "sign_vector_count", "lane_count",
        "support_tests_total", "action_count", "all_valid", "basis_consistent",
        "orientation_aware_s4_covariant", "orbit_feasibility_consistent",
        "s4_orbit_count", "s4_orbits", "feasible_sign_count",
        "factorized_subset_size", "factorized_orbit_closure_size",
        "factorized_orbit_closure", "factorized_intersecting_orbit_indices",
    ]
    print(json.dumps({k: out[k] for k in summary_keys}, indent=2))


if __name__ == "__main__":
    main()
