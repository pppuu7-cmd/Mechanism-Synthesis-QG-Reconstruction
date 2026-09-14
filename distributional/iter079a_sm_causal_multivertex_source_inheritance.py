#!/usr/bin/env python3
"""Iter079A-SM source-faithful causal multi-vertex inheritance audit.

Frozen by prereg/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE.md
before implementation.  This is a source/provenance gate, not a numerical physics
surrogate: lanes independently validate the frozen authority matrix and its
compatibility with existing distributional results.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "sources" / "ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md"
PREREG = ROOT / "prereg" / "ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def lane_a():
    s = read(SNAP)
    locks = {
        "bcg_single_vertex_scope_frozen": "single vertex dual to a 4-simplex" in s,
        "bcg_one_wedge_iepsilon_frozen": "Eq. (3) gives the one-wedge Toller matrix" in s,
        "bcg_fixed_causal_vertex_eq4_frozen": "Eq. (4) defines the fixed-causal single-vertex amplitude" in s,
        "causal_sum_not_eprl_frozen": "does **not** reproduce EPRL" in s,
        "toller_companion_local_scope_frozen": "not multi-vertex composition" in s,
    }
    return {
        "iteration": "Iter079A-SM", "lane": "A", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "INVALID_SOURCE_LOCK",
        "locks": locks,
        "scope": "BCG/Toller local source scope",
    }


def lane_b():
    s = read(SNAP)
    locks = {
        "beltran_v2_date_frozen": "3 Aug 2026" in s,
        "arbitrary_2complex_causality": "arbitrary oriented 2-complex" in s,
        "generalized_bcg_vertex": "generalized Bianchi–Chen–Gamonal causal vertex" in s,
        "E1_resolved": "E1 | arbitrary-2-complex causal orientation" in s and "`SOURCE_EXPLICIT`" in s,
        "E2_resolved": "E2 | generalized causal Toller vertex" in s,
        "finiteness_open": "finiteness of the generalized causal vertex amplitude as an open question" in s,
        "no_extension_transport_claim": "does not provide a law transporting supported extension coefficient functions" in s,
    }
    return {
        "iteration": "Iter079A-SM", "lane": "B", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "INVALID_SOURCE_LOCK",
        "locks": locks,
        "resolved_elements": ["E1", "E2"] if all(locks.values()) else [],
    }


def lane_c():
    s = read(SNAP)
    missing = []
    for eid in ("E3", "E4", "E5", "E6"):
        needle = f"| {eid} |"
        row = next((ln for ln in s.splitlines() if needle in ln), "")
        if "MISSING_REQUIRED_OBJECT" in row:
            missing.append(eid)
    neg = {
        "parent_eprl_not_silent_bridge": "do not by themselves prove" in s,
        "bf_eprl_import_forbidden": "additional bridge choice" in s,
        "all_E3_E6_marked_missing": missing == ["E3", "E4", "E5", "E6"],
    }
    return {
        "iteration": "Iter079A-SM", "lane": "C", "valid": all(neg.values()),
        "scientific_outcome": "BLOCKED" if all(neg.values()) else "INVALID",
        "locks": neg,
        "missing_required_elements": missing,
        "scope": "composition inheritance E3-E6",
    }


def lane_d():
    s = read(SNAP)
    q = read(ROOT / "results" / "ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md")
    k = read(ROOT / "results" / "ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION_RESULT.md")
    missing = []
    for eid in ("E7", "E8"):
        needle = f"| {eid} |"
        row = next((ln for ln in s.splitlines() if needle in ln), "")
        if "MISSING_REQUIRED_OBJECT" in row:
            missing.append(eid)
    locks = {
        "iter077q_infinite_family_authority": "countably infinite-dimensional" in q,
        "iter077q_Qn_family": "Q^n" in q,
        "iter077k_joint_prescription_missing": "joint K5" in k and "BLOCKED" in k,
        "E7_E8_missing": missing == ["E7", "E8"],
        "no_hidden_transport_in_snapshot": "none of S1-S4 acts on Iter077Q" in s,
    }
    return {
        "iteration": "Iter079A-SM", "lane": "D", "valid": all(locks.values()),
        "scientific_outcome": "BLOCKED" if all(locks.values()) else "INVALID",
        "locks": locks,
        "missing_required_elements": missing,
        "scope": "distributional/regulator and extension transport E7-E8",
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root: str):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter079A-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    present = set(got) == set(LANES)
    valid = present and all(bool(got[x].get("valid")) for x in LANES)
    outcomes = {x: got.get(x, {}).get("scientific_outcome") for x in LANES}
    resolved = sorted(set(got.get("B", {}).get("resolved_elements", [])))
    missing = sorted(set(got.get("C", {}).get("missing_required_elements", []) + got.get("D", {}).get("missing_required_elements", [])))
    if valid and resolved == ["E1", "E2"] and missing == ["E3", "E4", "E5", "E6", "E7", "E8"]:
        verdict = "BLOCKED"
        classification = "ITER079A_SM_CAUSAL_MULTIVERTEX_PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_OBJECT_DEFINITION_BLOCKED_EXACT_SOURCE_AUDIT"
    elif valid and not missing:
        verdict = "PASS"
        classification = "ITER079A_SM_CAUSAL_MULTIVERTEX_OBJECT_SOURCE_DEFINED"
    else:
        verdict = "INVALID"
        classification = "ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_AUDIT_INVALID_OR_INCOMPLETE"
    return {
        "iteration": "Iter079A-SM",
        "execution_valid": valid,
        "lane_scientific_outcomes": outcomes,
        "resolved_elements": resolved,
        "missing_required_elements": missing,
        "E9_fixed_multivertex": "NOT_REQUIRED_AT_THIS_LAYER",
        "E9_refinement_RG": "MISSING_REQUIRED_OBJECT",
        "verdict": verdict,
        "classification": classification,
        "new_scientific_fact": "Beltran v2 closes arbitrary-2-complex causal orientation and generalized local Toller-vertex authority (E1/E2), but a complete source-faithful multi-vertex distributional functional still lacks E3-E8, especially regulator/extension transport.",
        "next_admissible_gate": "Do not repeat orientation/valence work. Acquire or derive one explicit causal composition bridge for E3-E6 together with a distributional extension-transport rule for E7-E8; otherwise retain the multi-vertex object-definition blocker. E9 remains separately required for RG/refinement.",
        "claim_lock": "No unique K5 extension, no full causal multivertex amplitude theorem, no regulator independence, no RG fixed point, no G3/F9/G8/K5 promotion, no new physics or complete QG.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
