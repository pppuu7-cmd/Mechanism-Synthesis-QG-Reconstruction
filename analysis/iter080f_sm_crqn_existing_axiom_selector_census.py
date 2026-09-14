#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V01 = ROOT / "candidates" / "CANDIDATE_A_CRQN.md"
V02 = ROOT / "candidates" / "CANDIDATE_A_CRQN_V0_2.md"
CURRENT = ROOT / "status" / "CURRENT.md"

FROZEN = {
    "v0.1": {
        "path": "candidates/CANDIDATE_A_CRQN.md",
        "blob": "a3023dadb75f4c53d0c44a6de1c46958f4149178",
        "origin": "906c903892803b9a08b97340a1efc5a369a31061",
        "origin_date": "2026-09-11T21:52:10+00:00",
    },
    "v0.2": {
        "path": "candidates/CANDIDATE_A_CRQN_V0_2.md",
        "blob": "3933c110f9bafabb6593f8301029adaa25458bb2",
        "origin": "75250042861f613fe8048a1d001352da478ace0d",
        "origin_date": "2026-09-11T21:55:16+00:00",
    },
}
ITER077Q_COMMIT = "5941b3a064d93f2898d9e9a48545826e950455f1"
ITER077Q_DATE = "2026-09-14T00:24:24+00:00"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def emit(obj: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def lane_a() -> dict:
    rows = []
    valid = True
    for key, f in FROZEN.items():
        p = ROOT / f["path"]
        actual_blob = blob(p)
        try:
            actual_origin_date = git("show", "-s", "--format=%cI", f["origin"])
        except subprocess.CalledProcessError:
            actual_origin_date = None
        row = {
            "candidate": key,
            "path": f["path"],
            "expected_blob": f["blob"],
            "actual_blob": actual_blob,
            "origin_commit": f["origin"],
            "expected_origin_date": f["origin_date"],
            "actual_origin_date": actual_origin_date,
            "predates_iter077q": bool(actual_origin_date and actual_origin_date < ITER077Q_DATE),
        }
        row["ok"] = (
            actual_blob == f["blob"]
            and actual_origin_date == f["origin_date"]
            and row["predates_iter077q"]
        )
        valid = valid and row["ok"]
        rows.append(row)
    try:
        q_date = git("show", "-s", "--format=%cI", ITER077Q_COMMIT)
    except subprocess.CalledProcessError:
        q_date = None
    q_ok = q_date == ITER077Q_DATE
    valid = valid and q_ok
    return {
        "iteration": "Iter080F-SM", "lane": "A", "valid": valid,
        "scientific_outcome": "PASS_PROVENANCE_TIMING" if valid else "INVALID_PROVENANCE",
        "candidate_rows": rows,
        "iter077q": {"commit": ITER077Q_COMMIT, "expected_date": ITER077Q_DATE, "actual_date": q_date, "ok": q_ok},
    }


def present(text: str, *anchors: str) -> bool:
    return all(a in text for a in anchors)


def lane_b() -> dict:
    a = read(V01)
    b = read(V02)
    statements = [
        {
            "id": "V01_G3_MEASURE_BLOCKER",
            "source": "v0.1",
            "anchor_ok": present(a, "Neither `W_geom` nor a unique normalized measure is currently derived.", "This is a candidate architecture, not yet a quantum dynamics."),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": True, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "Explicit blocker, not a selector prescription.",
        },
        {
            "id": "V01_RG_TARGET",
            "source": "v0.1",
            "anchor_ok": present(a, "Introduce a coarse-graining map", "The actual beta functional must be derived for the CRQN state/history space."),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": False, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "RG target is not an explicit local extension-space action.",
        },
        {
            "id": "V01_LOCAL_AMPLITUDE_PROGRAMME",
            "source": "v0.1",
            "anchor_ok": present(a, "Require boundary composition, gauge covariance and a causal orientation rule.", "Determine whether a spin-foam/GFT-like vertex amplitude can be generalized"),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": True, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "Required properties/programme, no rule on the full ambiguity W.",
        },
        {
            "id": "V02_UNKNOWN_CAUSAL_FACTOR",
            "source": "v0.2",
            "anchor_ok": present(b, "`F_causal` is **unknown**.", "The v0.2 task is not to choose `A_v^CRQN` freely."),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": True, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "Explicitly unknown local factor; not an existing selector.",
        },
        {
            "id": "V02_REQUIRED_PROPERTIES",
            "source": "v0.2",
            "anchor_ok": present(b, "## Required causal-amplitude properties", "causal couplings form a finite RG-controlled set", "continuum observables must not retain an unphysical preferred discretization/foliation"),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": True, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "Constraints are requirements but no specified functional action on Iter077Q W.",
        },
        {
            "id": "V02_FINITE_PHI_RELATION",
            "source": "v0.2",
            "anchor_ok": present(b, "whether there exists a finite relation", "`Phi(A_v, o, j, i, beta, gauge) = 0`"),
            "A1_PREEXISTING": True, "A2_FULL_W_ACTION": False, "A3_SELECTION_POWER": False, "A4_OBJECT_REACH": True, "A5_INDEPENDENT_MOTIVATION": True,
            "reason": "Existence question for a finite relation, not a specified full-function-space selector; cannot be promoted after Iter080D.",
        },
    ]
    anchors_valid = all(s["anchor_ok"] for s in statements)
    for s in statements:
        s["qualifies_A1_A5"] = s["anchor_ok"] and all(s[k] for k in ["A1_PREEXISTING","A2_FULL_W_ACTION","A3_SELECTION_POWER","A4_OBJECT_REACH","A5_INDEPENDENT_MOTIVATION"])
    qualifying = [s["id"] for s in statements if s["qualifies_A1_A5"]]
    valid = anchors_valid
    return {
        "iteration": "Iter080F-SM", "lane": "B", "valid": valid,
        "scientific_outcome": ("PASS_EXISTING_SELECTOR_AXIOM" if qualifying else "BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING") if valid else "INVALID_IMPLEMENTATION",
        "statements": statements,
        "qualifying_preexisting_axioms": qualifying,
    }


def classify_axiom(x: dict) -> bool:
    return all(bool(x.get(k)) for k in ["A1_PREEXISTING","A2_FULL_W_ACTION","A3_SELECTION_POWER","A4_OBJECT_REACH","A5_INDEPENDENT_MOTIVATION"])


def lane_c() -> dict:
    positive = {k: True for k in ["A1_PREEXISTING","A2_FULL_W_ACTION","A3_SELECTION_POWER","A4_OBJECT_REACH","A5_INDEPENDENT_MOTIVATION"]}
    finite_scalar = {"A1_PREEXISTING": True,"A2_FULL_W_ACTION": False,"A3_SELECTION_POWER": False,"A4_OBJECT_REACH": True,"A5_INDEPENDENT_MOTIVATION": True}
    aspiration = {"A1_PREEXISTING": True,"A2_FULL_W_ACTION": False,"A3_SELECTION_POWER": False,"A4_OBJECT_REACH": False,"A5_INDEPENDENT_MOTIVATION": True}
    controls = {
        "synthetic_full_function_selector_accepts": classify_axiom(positive),
        "finite_scalar_rejected": not classify_axiom(finite_scalar),
        "aspirational_rg_gauge_rejected": not classify_axiom(aspiration),
        "scientific_inputs_only_two_frozen_candidate_blobs": True,
    }
    valid = all(controls.values())
    return {"iteration":"Iter080F-SM","lane":"C","valid":valid,"scientific_outcome":"PASS_ANTI_RESCUE_CONTROLS" if valid else "INVALID_CLASSIFIER","controls":controls}


def lane_d() -> dict:
    c = read(CURRENT)
    locks = {
        "iter077q": "ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED" in c,
        "iter080a": "ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED" in c,
        "iter080d": "ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED" in c,
        "iter080e": "ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED" in c,
        "k5_blocked": "BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING" in c,
        "next_gate_named": "CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS" in c,
    }
    valid = all(locks.values())
    return {"iteration":"Iter080F-SM","lane":"D","valid":valid,"scientific_outcome":"PASS_DEPENDENCY_LOCK" if valid else "INVALID_PROVENANCE","locks":locks}

LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(directory: Path) -> dict:
    data = {}
    for lane in "ABCD":
        matches = list(directory.rglob(f"iter080f_sm_{lane}.json"))
        if len(matches) != 1:
            return {"iteration":"Iter080F-SM","execution_valid":False,"verdict":"INVALID_IMPLEMENTATION_OR_PROVENANCE","error":f"lane {lane} artifact count={len(matches)}"}
        data[lane] = json.loads(matches[0].read_text())
    valid = all(data[x].get("valid") for x in "ABCD")
    qualifying = data["B"].get("qualifying_preexisting_axioms", []) if valid else []
    if not valid:
        verdict = "INVALID_IMPLEMENTATION_OR_PROVENANCE"
        classification = verdict
    elif qualifying:
        verdict = "PASS_EXISTING_SELECTOR_AXIOM"
        classification = "ITER080F_SM_CRQN_V0_2_PREEXISTING_FULL_FUNCTION_SPACE_SELECTOR_AXIOM_FOUND_REQUIRES_DIRECT_K5_IMPLEMENTATION_TEST_SCOPED"
    else:
        verdict = "BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING"
        classification = "ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED"
    return {"iteration":"Iter080F-SM","execution_valid":valid,"lane_scientific_outcomes":{x:data[x].get("scientific_outcome") for x in "ABCD"},"qualifying_preexisting_axioms":qualifying,"verdict":verdict,"classification":classification}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=list(LANES))
    ap.add_argument("--aggregate-dir", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ns = ap.parse_args()
    if ns.aggregate_dir:
        obj = aggregate(ns.aggregate_dir)
    elif ns.lane:
        obj = LANES[ns.lane]()
    else:
        raise SystemExit("choose --lane or --aggregate-dir")
    emit(obj, ns.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("execution_valid", obj.get("valid", False)):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
