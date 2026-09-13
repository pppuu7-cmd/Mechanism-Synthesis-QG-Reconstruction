import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def require(text, needles):
    return {n: (n in text) for n in needles}


def lane_r():
    f65 = read("status/ITERATION_065A_RESULT.md")
    f66 = read("status/ITERATION_066A_RESULT.md")
    f67 = read("status/ITERATION_067A_RESULT.md")
    f68b = read("status/ITERATION_068B_RESULT.md")
    f68c = read("status/ITERATION_068C_RESULT.md")
    checks = {}
    checks.update({"iter065a_missing_correlated_object": "ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING" in f65})
    checks.update({"iter066a_framework_but_selector_missing": "ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING" in f66})
    checks.update({"iter067a_conditional_theorem_routes": "ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN" in f67})
    checks.update({"iter068b_separate_contact_route_obstructed": "ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES" in f68b})
    checks.update({"iter068c_prepullback_not_correlated_pullback": "does **not** establish that Eq.(5)/(6) survives" in f68c})
    ok = all(checks.values())
    return {
        "lane": "R", "pass": ok,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if ok else "EVIDENCE_INTEGRITY_FAIL",
        "missing_object": "JOINT_SOURCE_FAITHFUL_TOLLER_K5_BOUNDARY_VALUE",
        "checks": checks,
        "polygon_tests": [
            "keep common finite-spectral-i-epsilon family correlated through the joint limit",
            "verify tempered/distributional boundary-value existence via holomorphy-growth or wavefront hypotheses",
            "verify root-tree-cycle-order-regulator independence",
            "verify exact independent-wedge Eq.(5)/(6) control survives correlated pullback/integration",
            "reject arbitrary counterterm or fitted finite part"
        ]
    }


def lane_s():
    cand = read("candidates/CANDIDATE_A_CRQN_V0_2.md")
    cur = read("status/CURRENT.md")
    checks = {
        "carrier_selected": "CARRIER_SELECTED" in cand and "Q = (K,o,j,i,x)" in cand,
        "source_causal_vertex_is_comparator_not_crqn_derivation": "F_causal` is **unknown**" in cand,
        "g3_open": "G3 quantum dynamics: `OPEN`" in cur,
        "no_normalized_same_realization_package": "G3 quantum dynamics: `OPEN`" in cur,
    }
    ok = all(checks.values())
    return {
        "lane": "S", "pass": ok,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if ok else "EVIDENCE_INTEGRITY_FAIL",
        "missing_object": "CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION",
        "checks": checks,
        "polygon_tests": [
            "instantiate one same-realization amplitude-measure-composition package",
            "verify normalization and gluing/composition",
            "verify causal compatibility on the selected carrier",
            "ablate source-comparator ingredients and forbid silent copying as novelty"
        ]
    }


def lane_t():
    bridge = read("bridges/M02_M04_M05_M07_CAUSAL_CYLINDRICAL_INTERTWINING.md")
    cur = read("status/CURRENT.md")
    checks = {
        "cci_synthesis_derived": "Causal Cylindrical Intertwining" in bridge and "P_b'^± iota_b'b = iota_b'b P_b^±" in bridge,
        "physical_realization_open": "PHYSICAL_REALIZATION_OPEN" in bridge,
        "f9_blocked": "Physical F9: `BLOCKED`" in cur,
        "multistep_requirement": "multiple refinement steps" in bridge,
        "analytic_class_closure_requirement": "closure of the Toller analytic/pole class" in bridge,
    }
    ok = all(checks.values())
    return {
        "lane": "T", "pass": ok,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if ok else "EVIDENCE_INTEGRITY_FAIL",
        "missing_object": "PHYSICAL_MULTISCALE_CCI_REALIZATION",
        "checks": checks,
        "polygon_tests": [
            "define physical H_b and causal projectors P_b^+-",
            "derive dynamically justified embedding maps iota_b'b",
            "verify cylindrical consistency over more than one refinement step",
            "verify CCI residual P'_+- iota - iota P_+- = 0",
            "verify Toller analytic/pole-class closure without new cross-branch data"
        ]
    }


def lane_u():
    cur = read("status/CURRENT.md")
    road = read("docs/DSIR_100_PERCENT_ROADMAP.md")
    prereg = read("prereg/DSIR_TERMINAL_HANDOFF_RST.md")
    allowed = [
        "PASS_SOURCE_NATIVE", "PASS_DERIVED_MSQGR", "NO_GO_SOURCE_NATIVE",
        "CONVERGENCE_ONLY", "BLOCKED_TRANSFER_TO_POLYGON", "NOT_APPLICABLE",
        "SADDLE_EFFECTIVE_ONLY", "OPEN_EXACT_OBJECT_LOCALIZED"
    ]
    ledger = {
        "carrier": {"status": "PASS_DERIVED_MSQGR", "object": "oriented causal labelled 2-complex Q=(K,o,j,i,x)"},
        "source_amplitude_and_iepsilon": {"status": "PASS_SOURCE_NATIVE", "object": "causal/Toller source vertex with published spectral i-epsilon"},
        "signed_P3_generic_finite_spin": {"status": "SADDLE_EFFECTIVE_ONLY", "missing_object": "EXACT_FINITE_SPIN_PARITY_OR_FULL_INTEGRAL_SELECTOR", "test": "establish source-backed exact selector beyond the nondegenerate Lorentzian Regge saddle locus"},
        "epsilon_minus1_coefficient": {"status": "OPEN_EXACT_OBJECT_LOCALIZED", "missing_object": "REGULAR_TOLLER_INTERTWINER_NUMERATOR_ONEJET_PLUS_NONLINEAR_PUSHFORWARD_CURVATURE", "test": "factor singular/contact structure from regular source numerator, derive one-jet and nonlinear pushforward, then combine with frozen quadratic face data"},
        "K5": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "JOINT_SOURCE_FAITHFUL_TOLLER_K5_BOUNDARY_VALUE", "test": "execute lane-R predicates"},
        "G3": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION", "test": "execute lane-S predicates"},
        "F9": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "PHYSICAL_MULTISCALE_CCI_REALIZATION", "test": "execute lane-T predicates"},
        "G8": {"status": "CONVERGENCE_ONLY", "missing_object": "BEYOND_COMPARATOR_DYNAMICAL_RELATION", "test": "demonstrate a non-reparameterization relation or prediction after dynamics is instantiated"},
        "G4": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "CONTROLLED_RG_CONTINUUM_TRAJECTORY", "test": "derive coarse graining and continuum critical surface in same realization"},
        "G5": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "GAUGE_REFOLIATION_ANOMALY_CLOSURE", "test": "verify continuum gauge/refoliation closure without uncontrolled anomaly"},
        "G6": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "IR_EINSTEIN_QFT_RECOVERY", "test": "derive EH plus matter sector with controlled corrections"},
        "G7": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "NORMALIZED_SAME_REALIZATION_OBSERVABLE", "test": "derive at least one normalized cross-scale observable"},
        "G1_G2_residual": {"status": "BLOCKED_TRANSFER_TO_POLYGON", "missing_object": "FINAL_EQUIVALENCE_GAUGE_NO_PREFERRED_FRAME_CLOSURE", "test": "close final equivalence/gauge relations and demonstrate no physical preferred frame in continuum"},
    }
    status_ok = all(v["status"] in allowed for v in ledger.values())
    blocked_ok = all((v["status"] not in ("BLOCKED_TRANSFER_TO_POLYGON", "OPEN_EXACT_OBJECT_LOCALIZED") or (v.get("missing_object") and v.get("test"))) for v in ledger.values())
    claim_lock_ok = all(x in cur for x in ["no generic finite-spin signed P3", "no nominal `epsilon^-1` coefficient", "no G3 PASS or F9/G8/K5 promotion"])
    scope_ok = "100% handoff-contract completeness" in prereg and "does **not** mean" in road
    ok = status_ok and blocked_ok and claim_lock_ok and scope_ok
    return {"lane": "U", "pass": ok, "terminal_status": "LEDGER_FROZEN" if ok else "EVIDENCE_INTEGRITY_FAIL", "checks": {"allowed_statuses": status_ok, "blocked_fields_have_missing_object_and_test": blocked_ok, "claim_locks_preserved": claim_lock_ok, "100_percent_scope_guard": scope_ok}, "ledger": ledger}

LANES = {"R": lane_r, "S": lane_s, "T": lane_t, "U": lane_u}


def aggregate(root):
    got = {}
    for p in Path(root).rglob("*.json"):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("campaign") == "DSIR_TERMINAL_HANDOFF" and obj.get("lane") in LANES:
            got[obj["lane"]] = obj
    complete = set(got) == set(LANES) and all(got[k].get("pass") for k in LANES)
    return {
        "campaign": "DSIR_TERMINAL_HANDOFF",
        "valid": complete,
        "lane_pass": {k: bool(got.get(k, {}).get("pass")) for k in LANES},
        "DSIR_FUNNEL_CONTRACT_COMPLETE": 100 if complete else 0,
        "classification": "DSIR_FUNNEL_HANDOFF_CONTRACT_100_PERCENT_COMPLETE_PHYSICS_BLOCKERS_EXPLICIT_SCOPED" if complete else "DSIR_FUNNEL_HANDOFF_CONTRACT_INCOMPLETE_REVIEW_REQUIRED",
        "scope_guard": "100 means handoff-contract completeness, not solution of quantum gravity or PASS of all physical gates",
        "claim_lock": "No G3/F9/G8/K5 promotion; no generic finite-spin signed P3; no epsilon^-1 value; no physical finiteness/divergence theorem."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    if args.lane:
        obj = LANES[args.lane]()
        obj["campaign"] = "DSIR_TERMINAL_HANDOFF"
    else:
        obj = aggregate(args.aggregate_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("pass", obj.get("valid", False)):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
