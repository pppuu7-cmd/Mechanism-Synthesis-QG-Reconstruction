#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "analysis" / "iter080e_sm_joint_k5_selector_source_matrix.json"
SNAPSHOT = ROOT / "sources" / "ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_SNAPSHOT.md"
PREREG = ROOT / "prereg" / "ITER080E_SM_JOINT_K5_FUNCTION_SPACE_SELECTOR_SOURCE_AUDIT.md"
CURRENT = ROOT / "status" / "CURRENT.md"
Q_DERIVATION = ROOT / "sources" / "ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md"

EXPECTED_SOURCE_IDS = {
    "BCG_CAUSAL_VERTEX": ("2601.23162", "## S1"),
    "BCG_TOLLER_MATRICES": ("2604.24945", "## S2"),
    "BELTRAN_GENERALIZED_CAUSAL": ("2603.22661v2", "## S3"),
}
EXPECTED_Q_BLOB = "1b15464e8f7d5ae9d87932938f76de1ac8f3351f"
REQUIRED_PREREG_HEADINGS = [
    "## HYPOTHESIS", "## OBJECT", "## DEPENDENCY", "## SOURCE AUTHORITY",
    "## FROZEN INPUTS", "## POSITIVE CONTROLS", "## NEGATIVE CONTROLS",
    "## PASS", "## FAIL", "## BLOCKED", "## INVALID", "## INTERPRETATION CEILING",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_matrix() -> dict:
    return json.loads(read_text(MATRIX))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def section(text: str, marker: str) -> str:
    start = text.find(marker)
    if start < 0:
        return ""
    nxt = text.find("\n## S", start + len(marker))
    return text[start:] if nxt < 0 else text[start:nxt]


def selector_eligible(predicates: dict, eligible_status: str = "EXPLICIT") -> bool:
    required = (
        "P1_JOINT_K5",
        "P2_SOURCE_ORDER",
        "P3_FULL_OBJECT_REACH",
        "P4_FUNCTION_SPACE_UNIQUENESS",
        "P5_REGULATOR_BRANCH_AUTHORITY",
    )
    return all(predicates.get(key) == eligible_status for key in required)


def lane_a() -> dict:
    m = load_matrix()
    snap = read_text(SNAPSHOT)
    prereg = read_text(PREREG)

    heading_locks = {h: h in prereg for h in REQUIRED_PREREG_HEADINGS}
    source_ids = [row.get("id") for row in m.get("sources", [])]
    exact_census = set(source_ids) == set(EXPECTED_SOURCE_IDS) and len(source_ids) == 3

    source_checks = {}
    for row in m.get("sources", []):
        sid = row.get("id")
        expected = EXPECTED_SOURCE_IDS.get(sid)
        if expected is None:
            source_checks[sid or "<missing>"] = {"valid": False, "reason": "unexpected source id"}
            continue
        arxiv, marker = expected
        sec = section(snap, marker)
        evidence_hashes = []
        hashes_ok = True
        for ev in row.get("evidence_files", []):
            path = ROOT / ev["path"]
            actual = git_blob_sha(path) if path.exists() else None
            ok = actual == ev.get("blob_sha")
            hashes_ok = hashes_ok and ok
            evidence_hashes.append({"path": ev["path"], "expected": ev.get("blob_sha"), "actual": actual, "ok": ok})
        anchors_ok = True
        anchor_checks = {}
        for pred, item in row.get("predicates", {}).items():
            anchor = item.get("anchor", "")
            ok = bool(anchor) and anchor in sec
            anchors_ok = anchors_ok and ok
            anchor_checks[pred] = ok
        version_ok = row.get("arxiv") == arxiv and arxiv in sec and arxiv in prereg
        primary_ok = row.get("primary") is True
        source_checks[sid] = {
            "valid": bool(version_ok and primary_ok and hashes_ok and anchors_ok),
            "version_ok": version_ok,
            "primary_ok": primary_ok,
            "evidence_hashes": evidence_hashes,
            "anchor_checks": anchor_checks,
        }

    err = m.get("erratum", {})
    err_path = ROOT / err.get("path", "")
    err_actual = git_blob_sha(err_path) if err_path.exists() else None
    err_text = read_text(err_path) if err_path.exists() else ""
    erratum_ok = (
        err_actual == err.get("blob_sha")
        and err.get("required_anchor", "") in err_text
        and "NON_AUTHORITATIVE_SOURCE_LOCK_INVALID" in err_text
    )

    valid = (
        all(heading_locks.values())
        and exact_census
        and all(x.get("valid") for x in source_checks.values())
        and erratum_ok
    )
    return {
        "iteration": "Iter080E-SM",
        "lane": "A",
        "valid": valid,
        "scientific_outcome": "PASS_SOURCE_COVERAGE" if valid else "INVALID_SOURCE_LOCK",
        "exact_primary_source_census": exact_census,
        "prereg_heading_locks": heading_locks,
        "source_checks": source_checks,
        "erratum": {"expected": err.get("blob_sha"), "actual": err_actual, "ok": erratum_ok},
    }


def lane_b() -> dict:
    m = load_matrix()
    snap = read_text(SNAPSHOT)
    required = m.get("required_predicates", [])
    eligible_status = m.get("selector_eligible_status")
    rows = []
    structurally_valid = True

    for row in m.get("sources", []):
        sid = row.get("id")
        expected = EXPECTED_SOURCE_IDS.get(sid)
        if expected is None:
            structurally_valid = False
            continue
        _, marker = expected
        sec = section(snap, marker)
        statuses = {}
        evidence_ok = {}
        for pred in required:
            item = row.get("predicates", {}).get(pred, {})
            status = item.get("status")
            anchor = item.get("anchor", "")
            ok = bool(anchor) and anchor in sec and status in anchor
            statuses[pred] = status
            evidence_ok[pred] = ok
            structurally_valid = structurally_valid and ok
        eligible = selector_eligible(statuses, eligible_status)
        rows.append({"id": sid, "arxiv": row.get("arxiv"), "statuses": statuses, "evidence_ok": evidence_ok, "selector_eligible": eligible})

    eligible_real = [r["id"] for r in rows if r["selector_eligible"]]
    if structurally_valid and len(rows) == 3:
        outcome = "PASS_SOURCE_DEFINED_SELECTOR" if eligible_real else "BLOCKED_OBJECT_DEFINITION"
    else:
        outcome = "INVALID_IMPLEMENTATION"
    return {
        "iteration": "Iter080E-SM",
        "lane": "B",
        "valid": bool(structurally_valid and len(rows) == 3),
        "scientific_outcome": outcome,
        "selector_eligible_status": eligible_status,
        "source_rows": rows,
        "eligible_real_primary_sources": eligible_real,
    }


def lane_c() -> dict:
    m = load_matrix()
    controls = m.get("controls", {})
    eligible_status = m.get("selector_eligible_status")
    pos = selector_eligible(controls.get("positive_synthetic", {}), eligible_status)
    negative_names = [
        "negative_one_wedge",
        "negative_finite_symmetry",
        "negative_finite_scalar",
        "negative_causal_orientation",
    ]
    neg = {name: selector_eligible(controls.get(name, {}), eligible_status) for name in negative_names}
    synthetic_not_real = "positive_synthetic" not in {row.get("id") for row in m.get("sources", [])}
    valid = pos and all(not x for x in neg.values()) and synthetic_not_real
    return {
        "iteration": "Iter080E-SM",
        "lane": "C",
        "valid": valid,
        "scientific_outcome": "PASS_CLASSIFIER_CONTROLS" if valid else "INVALID_IMPLEMENTATION",
        "positive_synthetic_eligible": pos,
        "negative_eligibility": neg,
        "synthetic_excluded_from_real_sources": synthetic_not_real,
    }


def lane_d() -> dict:
    current = read_text(CURRENT)
    q_sha = git_blob_sha(Q_DERIVATION) if Q_DERIVATION.exists() else None
    locks = {
        "iter077k_joint_gap": "one-wedge spectral `i epsilon` does not define a joint K5 finite part" in current,
        "iter077q_function_space": "infinite-dimensional tangential subspace" in current,
        "iter080a_finite_symmetry_insufficient": "finite K5 permutation covariance does not uniquely select" in current,
        "iter080d_finite_scalar_insufficient": "fixed finite scalar-valued complex-linear selector" in current,
        "active_selector_front": "SOURCE_DERIVED_FUNCTION_VALUED_DIFFERENTIAL_SPECTRAL_MICROLOCAL_JOINT_K5_CONDITION" in current,
        "q_derivation_hash": q_sha == EXPECTED_Q_BLOB,
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter080E-SM",
        "lane": "D",
        "valid": valid,
        "scientific_outcome": "PASS_DEPENDENCY_LOCK" if valid else "INVALID_PROVENANCE",
        "locks": locks,
        "iter077q_derivation_blob": q_sha,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root: str) -> dict:
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter080E-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj

    present = set(got) == set(LANES)
    all_valid = present and all(got[k].get("valid") for k in LANES)
    eligible = got.get("B", {}).get("eligible_real_primary_sources", [])
    b_outcome = got.get("B", {}).get("scientific_outcome")

    if not all_valid:
        verdict = "INVALID"
        classification = "ITER080E_SM_INVALID_SOURCE_OR_IMPLEMENTATION"
    elif b_outcome == "PASS_SOURCE_DEFINED_SELECTOR" and eligible:
        verdict = "PASS_SOURCE_DEFINED_SELECTOR"
        classification = "ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_CONTAINS_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_DEFINED_EXACT_AUDIT_SCOPED"
    elif b_outcome == "BLOCKED_OBJECT_DEFINITION" and not eligible:
        verdict = "BLOCKED_OBJECT_DEFINITION"
        classification = "ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED"
    else:
        verdict = "INVALID"
        classification = "ITER080E_SM_INVALID_AGGREGATE_LOGIC"

    return {
        "iteration": "Iter080E-SM",
        "execution_valid": all_valid,
        "lane_scientific_outcomes": {k: got.get(k, {}).get("scientific_outcome") for k in LANES},
        "eligible_real_primary_sources": eligible,
        "verdict": verdict,
        "classification": classification,
        "new_scientific_fact": (
            "Within the complete frozen primary BCG/Beltran causal-Toller corpus represented in-repo, no explicit prescription satisfies all five frozen requirements for a correlated joint-K5 selector acting on the full Iter077Q function-space ambiguity."
            if verdict == "BLOCKED_OBJECT_DEFINITION"
            else "See selector eligibility and frozen source evidence."
        ),
        "interpretation_ceiling": "A BLOCKED result is a source-object-definition statement for the frozen corpus, not a theorem that no selector or causal vertex distribution can exist; no regulator-independence, composition, G3, RG, continuum, spin-2, GR, matter/QFT or prediction claim follows.",
        "next_admissible_gate": "Do not invent a selector post hoc. Require genuinely new/revised primary authority or an independently motivated prospectively testable candidate-version selector; otherwise the current CRQN local-amplitude arrow remains blocked. Orthogonally, the existing causal multivertex E3/E4/E6 source bridge also remains blocked.",
        "claim_lock": "No NEW_PHYSICS_FOUND; no complete-QG claim; no full-amplitude causal divergence/nonexistence theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no G3/F9/G8/K5 promotion; retain published one-wedge spectral i epsilon."
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid"):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
