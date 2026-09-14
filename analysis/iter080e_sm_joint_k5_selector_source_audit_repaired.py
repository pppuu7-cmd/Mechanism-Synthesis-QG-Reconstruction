#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "analysis" / "iter080e_sm_joint_k5_selector_source_audit.py"

spec = importlib.util.spec_from_file_location("iter080e_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(base)

REQUIRED = (
    "P1_JOINT_K5",
    "P2_SOURCE_ORDER",
    "P3_FULL_OBJECT_REACH",
    "P4_FUNCTION_SPACE_UNIQUENESS",
    "P5_REGULATOR_BRANCH_AUTHORITY",
)


def _load_pinned_evidence(row: dict) -> tuple[str, list[dict], bool]:
    texts = []
    provenance = []
    ok_all = True
    for ev in row.get("evidence_files", []):
        path = ROOT / ev["path"]
        actual = base.git_blob_sha(path) if path.exists() else None
        ok = actual == ev.get("blob_sha")
        ok_all = ok_all and ok
        provenance.append({
            "path": ev["path"],
            "expected_blob_sha": ev.get("blob_sha"),
            "actual_blob_sha": actual,
            "ok": ok,
        })
        if ok:
            texts.append(base.read_text(path))
    return "\n\n".join(texts), provenance, ok_all


def _all(text: str, anchors: list[str]) -> bool:
    return all(a in text for a in anchors)


def _derive_source_predicates(sid: str, text: str) -> tuple[dict, dict]:
    """Derive frozen P1-P5 from source-specific pinned evidence only.

    No Iter080E matrix predicate status/anchor and no Iter080E-authored source
    snapshot is read here. Missing positive source evidence fails closed to a
    non-eligible status rather than manufacturing EXPLICIT authority.
    """
    facts = {}

    if sid == "BCG_CAUSAL_VERTEX":
        facts["vertex_formula"] = _all(text, [
            "fixed-causal single-vertex amplitude",
            "four-`SL(2,C)` group integral with a ten-wedge product",
        ])
        facts["one_wedge_regulator"] = _all(text, [
            "Feynman `i epsilon` spectral integral",
            "This fixes the physical spectral branch convention",
        ])
        facts["scope_only"] = _all(text, [
            "This snapshot establishes a source-defined object and its EPRL control relation.",
            "It does **not** establish finiteness",
        ])
        valid = all(facts.values())
        statuses = {
            "P1_JOINT_K5": "NOT_EXPLICIT",
            "P2_SOURCE_ORDER": "EXPLICIT_FOR_VERTEX_FORMULA",
            "P3_FULL_OBJECT_REACH": "EXPLICIT_FOR_FORMAL_VERTEX_FORMULA_ONLY",
            "P4_FUNCTION_SPACE_UNIQUENESS": "NOT_EXPLICIT",
            "P5_REGULATOR_BRANCH_AUTHORITY": "ONE_WEDGE_ONLY",
        } if valid else {}
        return statuses, facts

    if sid == "BCG_TOLLER_MATRICES":
        facts["individual_toller_scope"] = _all(text, [
            "analytic properties of individual Toller matrices",
            "elementary building block of the causal spinfoam **vertex**",
        ])
        facts["explicit_joint_gap"] = (
            "does not provide a 2-complex composition rule, face/edge causal measure, joint K5 extension prescription, or transport law for supported extension data" in text
        )
        facts["one_wedge_regulator"] = _all(text, [
            "Feynman `i epsilon`",
            "one-wedge Toller",
        ])
        valid = all(facts.values())
        statuses = {
            "P1_JOINT_K5": "NOT_EXPLICIT",
            "P2_SOURCE_ORDER": "LOCAL_WEDGE_ONLY",
            "P3_FULL_OBJECT_REACH": "NOT_EXPLICIT_FOR_EXTENSION",
            "P4_FUNCTION_SPACE_UNIQUENESS": "NOT_EXPLICIT",
            "P5_REGULATOR_BRANCH_AUTHORITY": "ONE_WEDGE_ONLY",
        } if valid else {}
        return statuses, facts

    if sid == "BELTRAN_GENERALIZED_CAUSAL":
        facts["arbitrary_complex"] = "arbitrary oriented 2-complex" in text
        facts["generalized_vertex"] = _all(text, [
            "generalized Bianchi–Chen–Gamonal causal vertex",
            "arbitrary vertex boundary graph",
        ])
        facts["vertex_not_completed_state_sum"] = _all(text, [
            "generalized **vertex amplitude**",
            "possible mechanism/proposal, not as a completed theorem establishing the full distributional state sum",
        ])
        facts["explicit_extension_gap"] = _all(text, [
            "does not address the MSQGR Iter077K/L/M/Q common-collision extension problem",
            "does not select a joint K5 finite part",
            "does not provide a law transporting supported extension coefficient functions through gluing",
        ])
        valid = all(facts.values())
        statuses = {
            "P1_JOINT_K5": "NOT_EXPLICIT",
            "P2_SOURCE_ORDER": "GENERALIZED_LOCAL_VERTEX_ONLY",
            "P3_FULL_OBJECT_REACH": "NOT_EXPLICIT_FOR_COLLISION_EXTENSION",
            "P4_FUNCTION_SPACE_UNIQUENESS": "NOT_EXPLICIT",
            "P5_REGULATOR_BRANCH_AUTHORITY": "NOT_EXPLICIT_FOR_JOINT_EXTENSION",
        } if valid else {}
        return statuses, facts

    return {}, {"unexpected_source_id": False}


def _derive_rows(matrix: dict) -> tuple[list[dict], bool]:
    rows = []
    structurally_valid = True
    for row in matrix.get("sources", []):
        sid = row.get("id")
        if sid not in base.EXPECTED_SOURCE_IDS:
            structurally_valid = False
            continue
        text, provenance, hashes_ok = _load_pinned_evidence(row)
        statuses, evidence_facts = _derive_source_predicates(sid, text)
        predicates_complete = set(statuses) == set(REQUIRED)
        source_valid = bool(hashes_ok and predicates_complete and all(evidence_facts.values()))
        structurally_valid = structurally_valid and source_valid
        eligible = base.selector_eligible(statuses, matrix.get("selector_eligible_status")) if source_valid else False
        rows.append({
            "id": sid,
            "arxiv": row.get("arxiv"),
            "statuses": statuses,
            "evidence_facts": evidence_facts,
            "evidence_provenance": provenance,
            "source_valid": source_valid,
            "selector_eligible": eligible,
        })
    return rows, bool(structurally_valid and len(rows) == 3)


def lane_b_repaired() -> dict:
    matrix = base.load_matrix()
    rows, structurally_valid = _derive_rows(matrix)

    # Adversarial non-circularity control: poison every prefilled status in a
    # deep copy. Derived source predicates and eligibility MUST be unchanged.
    poisoned = copy.deepcopy(matrix)
    for row in poisoned.get("sources", []):
        for item in row.get("predicates", {}).values():
            item["status"] = "POISONED_PREFILLED_STATUS_MUST_NOT_BE_READ"
            item["anchor"] = "POISONED_ITER080E_SELF_AUTHORED_ANCHOR"
    poisoned_rows, poisoned_valid = _derive_rows(poisoned)

    canonical_projection = [
        (r["id"], r["statuses"], r["selector_eligible"]) for r in rows
    ]
    poisoned_projection = [
        (r["id"], r["statuses"], r["selector_eligible"]) for r in poisoned_rows
    ]
    noncircularity_ok = structurally_valid and poisoned_valid and canonical_projection == poisoned_projection

    eligible_real = [r["id"] for r in rows if r["selector_eligible"]]
    valid = structurally_valid and noncircularity_ok
    if valid:
        outcome = "PASS_SOURCE_DEFINED_SELECTOR" if eligible_real else "BLOCKED_OBJECT_DEFINITION"
    else:
        outcome = "INVALID_IMPLEMENTATION"

    return {
        "iteration": "Iter080E-SM",
        "lane": "B",
        "repair": "CONTROL_ONLY_SOURCE_PREDICATE_BINDING",
        "valid": valid,
        "scientific_outcome": outcome,
        "selector_eligible_status": matrix.get("selector_eligible_status"),
        "source_rows": rows,
        "eligible_real_primary_sources": eligible_real,
        "noncircularity_adversarial_control": {
            "prefilled_status_and_anchor_poisoned": True,
            "derived_projection_unchanged": noncircularity_ok,
        },
    }


base.lane_b = lane_b_repaired
base.LANES["B"] = lane_b_repaired

if __name__ == "__main__":
    base.main()
