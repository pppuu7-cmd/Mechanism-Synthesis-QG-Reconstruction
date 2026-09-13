#!/usr/bin/env python3
"""Iter077N-SM: exact compact supported-ambiguity survival + gluing audit.

Frozen by prereg/ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING.md.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "distributional" / "iter077i_sm_source_ordered_jhalf_k5_l1.py"
spec = importlib.util.spec_from_file_location("iter077i_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

KS = list(itertools.product((0, 1), repeat=5))
IDENTITY = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]


def compact_eval(ks):
    old = base.EDGE_MATRICES
    try:
        base.EDGE_MATRICES = {e: IDENTITY for e in base.EDGES}
        return base.contract_boundary(ks)
    finally:
        base.EDGE_MATRICES = old


def lane_a():
    rows = []
    for ks in KS:
        z = compact_eval(ks)
        rows.append({
            "boundary_k": list(ks),
            "exact_stripped_compact_K5": [z[0], z[1]],
            "nonzero": z != (0, 0),
        })
    nonzero = sum(int(r["nonzero"]) for r in rows)
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "iteration": "Iter077N-SM",
        "lane": "A",
        "valid": True,
        "boundary_components_checked": 32,
        "nonzero_compact_functionals": nonzero,
        "zero_compact_functionals": 32 - nonzero,
        "supported_ambiguity_survives_integrated_vertex": nonzero > 0,
        "scientific_outcome": "SURVIVES" if nonzero > 0 else "KERNEL",
        "sha256_exact_rows": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "rows": rows,
    }


def lane_b():
    source = (ROOT / "sources" / "ITER077N_SM_GLUING_SOURCE_LOCK.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING.md").read_text(encoding="utf-8")
    locks = {
        "state_sum_product_vertices": "prod_v A_v" in source,
        "resolution_identity_intertwiners": "resolutions of the identity" in source,
        "gluing_bilinear_expansion": "G_c = G_00 + c(G_L0+G_0L) + c^2 G_LL" in source,
        "same_universal_c": "same universal" in prereg,
        "positive_control_c_independent_target": "c-independent target" in prereg,
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter077N-SM",
        "lane": "B",
        "valid": valid,
        "scientific_outcome": "PASS" if valid else "BLOCKED",
        "source_locks": locks,
        "structural_identity": "G_c=G_00+c(G_L0+G_0L)+c^2 G_LL",
        "standard_gluing_is_operation_not_selector": valid,
    }


def lane_c():
    source = (ROOT / "sources" / "ITER077N_SM_GLUING_SOURCE_LOCK.md").read_text(encoding="utf-8")
    locks = {
        "causal_single_vertex_scope": "paper focused on a single vertex" in source,
        "many_vertex_future_step": "many vertices" in source and "important next step" in source,
        "finiteness_open": "finiteness of the causal vertex must be investigated again" in source,
        "no_existing_c_independent_selector": "does not supply such an equation" in source,
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter077N-SM",
        "lane": "C",
        "valid": valid,
        "scientific_outcome": "PASS" if valid else "BLOCKED",
        "source_locks": locks,
        "published_multi_vertex_selector_found": False if valid else None,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c}


def aggregate(root):
    got = {}
    for base_dir, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base_dir, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter077N-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    present = set(got) == set(LANES)
    valid = present and all(bool(got[k].get("valid")) for k in LANES)
    if not valid:
        verdict = "BLOCKED"
        classification = "ITER077N_SM_AMBIGUITY_SURVIVAL_OR_GLUING_BLOCKED_OBJECT_DEFINITION"
    elif not got["A"].get("supported_ambiguity_survives_integrated_vertex"):
        verdict = "FAIL"
        classification = "ITER077N_SM_FROZEN_DELTA_N_FSU2_AMBIGUITY_INTEGRATES_TO_ZERO_ALL32_EXACT_SCOPED"
    elif got["B"].get("standard_gluing_is_operation_not_selector") and not got["C"].get("published_multi_vertex_selector_found"):
        verdict = "PASS"
        classification = "ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED"
    else:
        verdict = "BLOCKED"
        classification = "ITER077N_SM_AMBIGUITY_SURVIVAL_OR_GLUING_BLOCKED_OBJECT_DEFINITION"
    return {
        "iteration": "Iter077N-SM",
        "execution_valid": valid,
        "verdict": verdict,
        "classification": classification,
        "lane_scientific_outcomes": {k: got.get(k, {}).get("scientific_outcome") for k in LANES},
        "nonzero_compact_boundary_functionals": got.get("A", {}).get("nonzero_compact_functionals"),
        "compact_rows_checksum": got.get("A", {}).get("sha256_exact_rows"),
        "standard_gluing_is_operation_not_selector": got.get("B", {}).get("standard_gluing_is_operation_not_selector"),
        "published_multi_vertex_selector_found": got.get("C", {}).get("published_multi_vertex_selector_found"),
        "next_admissible_gate": "If PASS, test a genuinely stronger independently motivated selector such as cylindrical/refinement consistency or an RG fixed-point condition; ordinary state-sum contraction alone is exhausted.",
        "claim_lock": "No G3 PASS, regulator independence, generic-spin theorem, full causal-vertex nonexistence/divergence theorem, new physics or complete QG.",
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
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
