#!/usr/bin/env python3
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources/raw/k4_order3_source_object_authority_audit.json"
REQS = [
    "R1_K4_NORMAL_CHART", "R2_BCH_ORDER3", "R3_TOLLER_ORDER3",
    "R4_EXTERNAL_TOLLER_JETS", "R5_HAAR_JACOBIAN_ORDER3",
    "R6_Q_DEFINING_FUNCTION_ORDER3", "R7_FULL32_CONTRACTION_MAP",
    "R8_FRONT_PAIRING", "R9_BRANCH_NORMALIZATION", "R10_S5_TRANSPORT",
]
SUFFICIENT = "SOURCE_DEFINED_SUFFICIENT"
CONDITIONAL = "ABSENT_OR_ONLY_CONDITIONAL"
UNRESOLVED = "UNRESOLVED_EVIDENCE"


def verify_evidence(manifest):
    failures = []
    checked = 0
    for r in REQS:
        item = manifest["requirements"].get(r)
        if not item:
            failures.append(f"missing_manifest_requirement:{r}")
            continue
        if item.get("status") not in manifest["allowed_statuses"]:
            failures.append(f"bad_status:{r}:{item.get('status')}")
        if not item.get("reason"):
            failures.append(f"missing_reason:{r}")
        evidence = item.get("evidence", [])
        if not evidence:
            failures.append(f"missing_evidence:{r}")
            continue
        for ev in evidence:
            checked += 1
            p = ROOT / ev["path"]
            if not p.exists():
                failures.append(f"missing_path:{r}:{ev['path']}")
                continue
            text = p.read_text(encoding="utf-8")
            for needle in ev.get("must_contain", []):
                if needle not in text:
                    failures.append(f"missing_anchor:{r}:{ev['path']}:{needle}")
            if len(ev.get("commit", "")) != 40:
                failures.append(f"bad_commit_anchor:{r}:{ev.get('commit')}")
    return checked, failures


def validate_candidate(c):
    reasons = []
    statuses = c.get("requirement_status", {})
    if set(statuses) != set(REQS):
        reasons.append("requirement_set_mismatch")
    unresolved = [r for r in REQS if statuses.get(r) == UNRESOLVED]
    missing = [r for r in REQS if statuses.get(r) == CONDITIONAL]
    bad = [r for r in REQS if statuses.get(r) not in {SUFFICIENT, CONDITIONAL, UNRESOLVED}]
    if bad:
        reasons.append("invalid_requirement_status")
    if c.get("regulator_parameters") != 16:
        reasons.append("not_16_parameter_multivariate_family")
    if c.get("k4_blocks") != 5:
        reasons.append("not_five_k4_blocks")
    if c.get("source_wedges") != 10:
        reasons.append("not_ten_source_wedges")
    if c.get("full_boundary_components") != 32:
        reasons.append("not_full32_boundary")
    if c.get("nested_density_powers") != [5, 8, 11]:
        reasons.append("wrong_nested_density_powers")
    if c.get("k4_normal_order") != 3:
        reasons.append("wrong_k4_normal_order")
    if not c.get("noncommutative_bch_required", False):
        reasons.append("bch_omitted")
    if not c.get("external_toller_jets_required", False):
        reasons.append("external_toller_jets_omitted")
    if not c.get("haar_jets_required", False):
        reasons.append("haar_jets_omitted")
    if c.get("uses_one_parameter_specialization", False):
        reasons.append("one_parameter_specialization")
    if c.get("uses_scalar_surrogate", False):
        reasons.append("scalar_surrogate")
    if c.get("representative_boundary_only", False):
        reasons.append("representative_boundary_only")
    if c.get("frozen_angular_ray", False):
        reasons.append("frozen_angular_ray")
    if c.get("infers_k4_zero_from_k3", False):
        reasons.append("k3_to_k4_zero_inference")
    if c.get("termwise_contact_product", False):
        reasons.append("termwise_contact_product")
    if c.get("posthoc_finite_part", False):
        reasons.append("posthoc_finite_part")
    execution_valid = not reasons and not unresolved
    object_defined = execution_valid and not missing and all(statuses.get(r) == SUFFICIENT for r in REQS)
    return {
        "execution_valid": execution_valid,
        "object_defined": object_defined,
        "missing_requirements": missing,
        "unresolved_requirements": unresolved,
        "reasons": reasons,
    }


def base_candidate(statuses):
    return {
        "requirement_status": dict(statuses),
        "regulator_parameters": 16,
        "k4_blocks": 5,
        "source_wedges": 10,
        "full_boundary_components": 32,
        "nested_density_powers": [5, 8, 11],
        "k4_normal_order": 3,
        "noncommutative_bch_required": True,
        "external_toller_jets_required": True,
        "haar_jets_required": True,
        "uses_one_parameter_specialization": False,
        "uses_scalar_surrogate": False,
        "representative_boundary_only": False,
        "frozen_angular_ray": False,
        "infers_k4_zero_from_k3": False,
        "termwise_contact_product": False,
        "posthoc_finite_part": False,
    }


def run_controls():
    full = {r: SUFFICIENT for r in REQS}
    positive = validate_candidate(base_candidate(full))
    cases = {}

    def reject(name, mutator):
        c = base_candidate(full)
        mutator(c)
        v = validate_candidate(c)
        cases[name] = {"rejected": not v["object_defined"], "reasons": v["reasons"]}

    reject("one_parameter_rho_z_u", lambda c: c.__setitem__("uses_one_parameter_specialization", True))
    reject("scalar_k4_hodge_surrogate", lambda c: c.__setitem__("uses_scalar_surrogate", True))
    reject("representative_boundary_component", lambda c: c.__setitem__("representative_boundary_only", True))
    reject("frozen_angular_ray", lambda c: c.__setitem__("frozen_angular_ray", True))
    reject("historical_density_5_2_2", lambda c: c.__setitem__("nested_density_powers", [5, 2, 2]))
    reject("commuting_cubic_without_bch", lambda c: c.__setitem__("noncommutative_bch_required", False))
    reject("leading_toller_only", lambda c: c["requirement_status"].__setitem__("R3_TOLLER_ORDER3", CONDITIONAL))
    reject("omit_external_toller_jets", lambda c: c.__setitem__("external_toller_jets_required", False))
    reject("omit_haar_jets", lambda c: c.__setitem__("haar_jets_required", False))
    reject("infer_k4_zero_from_k3", lambda c: c.__setitem__("infers_k4_zero_from_k3", True))
    reject("termwise_contact_product", lambda c: c.__setitem__("termwise_contact_product", True))
    reject("posthoc_finite_part", lambda c: c.__setitem__("posthoc_finite_part", True))
    return positive, cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    evidence_checked, evidence_failures = verify_evidence(manifest)
    statuses = {r: manifest["requirements"][r]["status"] for r in REQS}
    real = validate_candidate(base_candidate(statuses))
    positive, controls = run_controls()
    controls_ok = len(controls) == 12 and all(v["rejected"] for v in controls.values())
    provenance_ok = manifest.get("prereg_commit") == "a6983a4d7379bf73f48752a4de357450996d8572" and not evidence_failures

    if not provenance_ok or not controls_ok or not positive["object_defined"] or not real["execution_valid"]:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_INVALID_IMPLEMENTATION"
    elif real["object_defined"]:
        verdict = "PASS_EXACT_SCOPED"
        classification = "ACTUAL_K4_ORDER3_SOURCE_COEFFICIENT_OBJECT_DEFINED_AND_REACHABLE_SCOPED"
    else:
        verdict = "BLOCKED_OBJECT_DEFINITION"
        classification = "ACTUAL_K4_ORDER3_SOURCE_COEFFICIENT_OBJECT_DEFINITION_BLOCKED_SCOPED"

    out = {
        "gate": manifest["gate"],
        "authority_cut": manifest["authority_cut"],
        "prereg_commit": manifest["prereg_commit"],
        "verdict": verdict,
        "classification": classification,
        "provenance_ok": provenance_ok,
        "evidence_records_checked": evidence_checked,
        "evidence_failures": evidence_failures,
        "execution_valid": verdict != "INVALID_IMPLEMENTATION",
        "requirement_status": statuses,
        "missing_requirements": real["missing_requirements"],
        "unresolved_requirements": real["unresolved_requirements"],
        "positive_control": positive,
        "negative_controls": controls,
        "negative_controls_all_rejected": controls_ok,
        "object_defined_for_k4_order3": real["object_defined"],
        "partial_k4_coefficient_values_emitted": False,
        "scientific_conclusion": {
            "abstract_multivariate_germ_remains_authoritative": True,
            "k3_zero_remains_authoritative": True,
            "k4_order3_explicit_source_coefficient_reachable_now": real["object_defined"],
            "k4_zero_or_nonzero_classification": None,
            "k5_conclusion": None,
            "physical_finite_part_conclusion": None
        }
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
