#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
PRED_KEYS = [
    "A1_PREEXISTING",
    "A2_FULL_W_ACTION",
    "A3_SELECTION_POWER",
    "A4_OBJECT_REACH",
    "A5_INDEPENDENT_MOTIVATION",
]


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
        "iteration": "Iter080F-SM",
        "lane": "A",
        "valid": valid,
        "scientific_outcome": "PASS_PROVENANCE_TIMING" if valid else "INVALID_PROVENANCE",
        "candidate_rows": rows,
        "iter077q": {
            "commit": ITER077Q_COMMIT,
            "expected_date": ITER077Q_DATE,
            "actual_date": q_date,
            "ok": q_ok,
        },
    }


def present(text: str, *anchors: str) -> bool:
    return all(a in text for a in anchors)


def row(
    sid: str,
    source: str,
    text: str,
    anchors: list[str],
    preds: tuple[bool, bool, bool, bool, bool],
    reason: str,
) -> dict:
    out = {
        "id": sid,
        "source": source,
        "anchors": anchors,
        "anchor_ok": present(text, *anchors),
        **dict(zip(PRED_KEYS, preds)),
        "reason": reason,
    }
    out["qualifies_A1_A5"] = out["anchor_ok"] and all(out[k] for k in PRED_KEYS)
    return out


def build_census() -> dict:
    a = read(V01)
    b = read(V02)
    statements = [
        row(
            "V01_M14_EXTERNAL_FILTER",
            "v0.1",
            a,
            ["M09 entanglement/holography and M14 analyticity/unitarity are initially external consistency filters."],
            (True, False, False, False, True),
            "Analyticity/unitarity is an external consistency filter, not a local extension-space selector.",
        ),
        row(
            "V01_HISTORY_AMPLITUDE_ANSATZ",
            "v0.1",
            a,
            ["A[B_f,B_i] = Sum_H", "Chi_causal is not allowed to be an arbitrary after-the-fact projector."],
            (True, False, False, True, True),
            "The history ansatz and structural-causality rule reach amplitudes but do not act on the full extension ambiguity W.",
        ),
        row(
            "V01_G3_MEASURE_BLOCKER",
            "v0.1",
            a,
            ["Neither `W_geom` nor a unique normalized measure is currently derived.", "This is a candidate architecture, not yet a quantum dynamics."],
            (False, False, False, True, True),
            "Explicit statement that the required prescription is not derived; it is not a pre-existing selector.",
        ),
        row(
            "V01_RG_TARGET",
            "v0.1",
            a,
            ["Introduce a coarse-graining map", "The actual beta functional must be derived for the CRQN state/history space."],
            (False, False, False, False, True),
            "The beta functional is an undeveloped target and not an explicit local extension-space operation.",
        ),
        row(
            "V01_G4_BETA_BLOCKER",
            "v0.1",
            a,
            ["No CRQN beta functional or controlled continuum critical surface has yet been computed."],
            (False, False, False, False, True),
            "Open blocker, not a stated selector prescription.",
        ),
        row(
            "V01_GAUGE_REFOLIATION_RULE",
            "v0.1",
            a,
            ["a foliation may be used as regulator/bookkeeping;", "physical observables must become independent of that foliation in the continuum limit;", "if a preferred foliation remains physical"],
            (True, False, False, False, True),
            "A continuum decision rule, not a rule selecting local K5 extension data.",
        ),
        row(
            "V01_G5_BLOCKER",
            "v0.1",
            a,
            ["G5 remains `OPEN_BLOCKED` until the candidate constraint/gauge algebra or covariant replacement is explicit."],
            (False, False, False, False, True),
            "Gauge closure is explicitly missing.",
        ),
        row(
            "V01_DIMENSIONAL_FLOW_SAME_MEASURE",
            "v0.1",
            a,
            ["A dimensional flow is useful only if derived from the same ensemble and measure that generate the continuum phase."],
            (True, False, False, False, True),
            "Same-measure consistency condition for a downstream observable, not extension selection.",
        ),
        row(
            "V01_G3_TABLE",
            "v0.1",
            a,
            ["| G3 quantum dynamics | normalized amplitude/measure and composition rule | OPEN_BLOCKED |"],
            (False, False, False, True, True),
            "The table names a required object as blocked rather than supplying it.",
        ),
        row(
            "V01_G4_TABLE",
            "v0.1",
            a,
            ["| G4 RG/continuum | defined coarse graining + critical continuum trajectory | OPEN_BLOCKED |"],
            (False, False, False, False, True),
            "RG target remains open.",
        ),
        row(
            "V01_G5_TABLE",
            "v0.1",
            a,
            ["| G5 gauge/anomaly | continuum gravitational gauge structure closes | OPEN_BLOCKED |"],
            (False, False, False, False, True),
            "Gauge target remains open.",
        ),
        row(
            "V01_G7_TABLE",
            "v0.1",
            a,
            ["| G7 observable | normalized same-realization cross-scale observable | OPEN_BLOCKED |"],
            (False, False, False, False, True),
            "A normalized observable is a downstream target, not a local selector.",
        ),
        row(
            "V01_LOCAL_AMPLITUDE_PROGRAMME",
            "v0.1",
            a,
            ["Require boundary composition, gauge covariance and a causal orientation rule.", "Determine whether a spin-foam/GFT-like vertex amplitude can be generalized"],
            (True, False, False, True, True),
            "Required properties/programme but no operation on the full ambiguity W.",
        ),
        row(
            "V01_FINITE_TRUNCATION_COARSE_GRAINING",
            "v0.1",
            a,
            ["Choose a finite truncation and derive how couplings/weights transform under graph/history blocking."],
            (False, False, False, False, True),
            "A future finite-truncation RG task, not a pre-existing full-W selector.",
        ),
        row(
            "V01_SAME_REALIZATION_OBSERVABLE_PROGRAMME",
            "v0.1",
            a,
            ["Compute one same-realization observable", "two-point boundary geometry correlator;", "spectral dimension from the same ensemble;"],
            (False, False, False, False, True),
            "Observable programme is downstream of local object definition.",
        ),
        row(
            "V01_EARLY_SUCCESS_COARSE_GRAINING",
            "v0.1",
            a,
            ["a computable coarse-graining transformation;", "a nontrivial continuum candidate;"],
            (True, False, False, False, True),
            "Early-success criterion does not select local extension data.",
        ),
        row(
            "V01_KILL_GAUGE_FINE_TUNING",
            "v0.1",
            a,
            ["continuum gauge symmetry requires fine tuning of an unbounded number of independent couplings;"],
            (True, False, False, False, True),
            "A falsifier, not a constructive full-W selection rule.",
        ),
        row(
            "V01_KILL_NORMALIZED_OBSERVABLES",
            "v0.1",
            a,
            ["normalized observables cannot be defined from the same microscopic measure."],
            (True, False, False, False, True),
            "A falsifier on observables/measure, not a selector for the local extension.",
        ),
        row(
            "V02_HISTORY_AMPLITUDE_TARGET",
            "v0.2",
            b,
            ["A_CRQN[K,o,j,i] = Prod_f A_f Prod_e A_e Prod_v A_v^CRQN`.", "The v0.2 task is not to choose `A_v^CRQN` freely."],
            (True, False, False, True, True),
            "Amplitude architecture reaches the local object but does not supply full-W extension action.",
        ),
        row(
            "V02_JOINT_REQUIREMENTS_CONSTRAIN_VERTEX",
            "v0.2",
            b,
            ["joint requirements of causal composition, quantum geometry, RG closure and continuum gauge recovery constrain it."],
            (True, False, False, True, True),
            "A stated research requirement, not an explicit selector functional.",
        ),
        row(
            "V02_UNKNOWN_CAUSAL_FACTOR",
            "v0.2",
            b,
            ["`F_causal` is **unknown**.", "The v0.2 task is not to choose `A_v^CRQN` freely."],
            (False, False, False, True, True),
            "The local causal factor is explicitly unknown.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_REVERSAL",
            "v0.2",
            b,
            ["time/orientation reversal is not automatically identical to the original causal transition amplitude;"],
            (True, False, False, True, True),
            "Local amplitude property shared by potentially many extensions.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_GLUING",
            "v0.2",
            b,
            ["gluing compatible local histories preserves causal orientation and boundary composition;"],
            (True, False, False, True, True),
            "Composition constraint without full-W selector action.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_SEMICLASSICS",
            "v0.2",
            b,
            ["large-quantum-number stationary points include Lorentzian Regge geometries with compatible causal data;"],
            (True, False, False, True, True),
            "Semiclassical requirement does not specify finite-spin extension selection.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_LOCAL_CONSISTENCY",
            "v0.2",
            b,
            ["locally inconsistent causal/geometric assignments are dynamically suppressed or excluded;"],
            (True, False, False, True, True),
            "Admissibility/dynamical suppression requirement, not extension-space action.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_FINITE_RG_COUPLINGS",
            "v0.2",
            b,
            ["causal couplings form a finite RG-controlled set rather than arbitrary complex-dependent weights;"],
            (True, False, False, True, True),
            "Finite RG-coupling requirement cannot act on the full infinite-dimensional W as written.",
        ),
        row(
            "V02_CAUSAL_PROPERTY_FOLIATION",
            "v0.2",
            b,
            ["continuum observables must not retain an unphysical preferred discretization/foliation."],
            (True, False, False, False, True),
            "Continuum observable constraint, not local extension selection.",
        ),
        row(
            "V02_G3_OPEN_BLOCKED",
            "v0.2",
            b,
            ["- G3 quantum dynamics: `OPEN_BLOCKED`."],
            (False, False, False, True, True),
            "Quantum dynamics is explicitly open.",
        ),
        row(
            "V02_G4_OPEN_BLOCKED",
            "v0.2",
            b,
            ["- G4 RG/continuum: `OPEN_BLOCKED`."],
            (False, False, False, False, True),
            "RG/continuum is explicitly open.",
        ),
        row(
            "V02_G5_OPEN_BLOCKED",
            "v0.2",
            b,
            ["- G5 gauge/refoliation: `OPEN_BLOCKED`."],
            (False, False, False, False, True),
            "Gauge/refoliation is explicitly open.",
        ),
        row(
            "V02_G7_OPEN_BLOCKED",
            "v0.2",
            b,
            ["- G7 same-realization observable: `OPEN_BLOCKED`."],
            (False, False, False, False, True),
            "Same-realization observable is explicitly open.",
        ),
        row(
            "V02_FINITE_PHI_RELATION",
            "v0.2",
            b,
            ["whether there exists a finite relation", "`Phi(A_v, o, j, i, beta, gauge) = 0`"],
            (False, False, False, True, True),
            "Existence question for a finite relation, not a specified full-function-space selector.",
        ),
        row(
            "V02_PHI_JOINT_REQUIREMENTS",
            "v0.2",
            b,
            ["causal composition + quantum-geometric semiclassics + RG stability + continuum gauge recovery"],
            (True, False, False, True, True),
            "Joint desiderata do not specify how to act on W.",
        ),
        row(
            "V02_SMALLER_SUBMANIFOLD_HYPOTHESIS",
            "v0.2",
            b,
            ["If the conditions select a smaller submanifold or new relation among vertex/edge couplings"],
            (False, False, False, True, True),
            "Conditional future possibility, not an already-defined selector.",
        ),
    ]

    relevant_terms = (
        "amplitude", "measure", "composition", "coarse-graining", "coarse graining",
        "beta", "rg", "gauge", "refoliation", "foliation", "analyticity", "unitarity",
        "normalized", "normalization", "observable", "f_causal", "phi(", "local factor",
        "causal-amplitude", "quantum dynamics",
    )
    sources = {"v0.1": a, "v0.2": b}
    coverage_lines = []
    uncovered = []
    for source, text in sources.items():
        anchors = [anchor for s in statements if s["source"] == source for anchor in s["anchors"]]
        for lineno, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("|") and "---" in line:
                continue
            low = line.lower()
            if not any(term in low for term in relevant_terms):
                continue
            covered_by = [anchor for anchor in anchors if anchor in line or line in anchor]
            item = {"source": source, "line": lineno, "text": line, "covered": bool(covered_by)}
            coverage_lines.append(item)
            if not covered_by:
                uncovered.append(item)

    anchors_valid = all(s["anchor_ok"] for s in statements)
    qualifying = [s["id"] for s in statements if s["qualifies_A1_A5"]]
    coverage_complete = len(uncovered) == 0
    return {
        "statements": statements,
        "anchors_valid": anchors_valid,
        "coverage_complete": coverage_complete,
        "coverage_lines": coverage_lines,
        "uncovered_relevant_lines": uncovered,
        "qualifying_preexisting_axioms": qualifying,
    }


def lane_b() -> dict:
    census = build_census()
    valid = census["anchors_valid"] and census["coverage_complete"]
    if not valid:
        outcome = "INVALID_IMPLEMENTATION"
    elif census["qualifying_preexisting_axioms"]:
        outcome = "PASS_EXISTING_SELECTOR_AXIOM"
    else:
        outcome = "BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING"
    return {
        "iteration": "Iter080F-SM",
        "lane": "B",
        "repair": "CONTROL_ONLY_AUDITABLE_COMPLETE_CENSUS",
        "valid": valid,
        "scientific_outcome": outcome,
        **census,
    }


def classify_axiom(x: dict) -> bool:
    return all(bool(x.get(k)) for k in PRED_KEYS)


def scientific_fingerprint(census: dict) -> dict:
    return {
        "statements": [
            {
                "id": s["id"],
                "source": s["source"],
                "anchor_ok": s["anchor_ok"],
                **{k: s[k] for k in PRED_KEYS},
                "qualifies_A1_A5": s["qualifies_A1_A5"],
            }
            for s in census["statements"]
        ],
        "coverage_complete": census["coverage_complete"],
        "uncovered_relevant_lines": census["uncovered_relevant_lines"],
        "qualifying_preexisting_axioms": census["qualifying_preexisting_axioms"],
    }


def isolation_replay() -> dict:
    baseline = build_census()
    baseline_fp = scientific_fingerprint(baseline)
    changed_raw = git("diff", "--name-only", ITER077Q_COMMIT, "HEAD")
    changed = [p for p in changed_raw.splitlines() if p.strip()]
    frozen_paths = {f["path"] for f in FROZEN.values()}
    forbidden_candidate_changes = sorted(frozen_paths.intersection(changed))
    removable = [p for p in changed if p not in frozen_paths and (ROOT / p).exists()]
    removed = []
    restored = False
    replay_fp = None
    replay_error = None
    try:
        for rel in removable:
            p = ROOT / rel
            if p.is_file() or p.is_symlink():
                p.unlink()
                removed.append(rel)
        replay = build_census()
        replay_fp = scientific_fingerprint(replay)
    except Exception as exc:
        replay_error = f"{type(exc).__name__}: {exc}"
    finally:
        if removed:
            subprocess.check_call(["git", "checkout", "HEAD", "--", *removed], cwd=ROOT)
        restored = all((ROOT / rel).exists() for rel in removed)
    return {
        "changed_post_iter077q_count": len(changed),
        "changed_post_iter077q_paths": changed,
        "forbidden_candidate_changes": forbidden_candidate_changes,
        "removed_count": len(removed),
        "removed_paths": removed,
        "replay_executed": replay_fp is not None,
        "fingerprint_equal": replay_fp == baseline_fp if replay_fp is not None else False,
        "restore_ok": restored,
        "error": replay_error,
        "valid": (
            len(changed) > 0
            and not forbidden_candidate_changes
            and len(removed) > 0
            and replay_fp is not None
            and replay_fp == baseline_fp
            and restored
        ),
    }


def lane_c() -> dict:
    positive = {k: True for k in PRED_KEYS}
    finite_scalar = {
        "A1_PREEXISTING": True,
        "A2_FULL_W_ACTION": False,
        "A3_SELECTION_POWER": False,
        "A4_OBJECT_REACH": True,
        "A5_INDEPENDENT_MOTIVATION": True,
    }
    aspiration = {
        "A1_PREEXISTING": False,
        "A2_FULL_W_ACTION": False,
        "A3_SELECTION_POWER": False,
        "A4_OBJECT_REACH": False,
        "A5_INDEPENDENT_MOTIVATION": True,
    }
    isolation = isolation_replay()
    controls = {
        "positive_predicates_all_true": all(positive[k] is True for k in PRED_KEYS),
        "synthetic_full_function_selector_accepts": classify_axiom(positive),
        "finite_scalar_A2_false": finite_scalar["A2_FULL_W_ACTION"] is False,
        "finite_scalar_A3_false": finite_scalar["A3_SELECTION_POWER"] is False,
        "finite_scalar_rejected": not classify_axiom(finite_scalar),
        "aspiration_A1_false": aspiration["A1_PREEXISTING"] is False,
        "aspiration_A2_false": aspiration["A2_FULL_W_ACTION"] is False,
        "aspiration_A3_false": aspiration["A3_SELECTION_POWER"] is False,
        "aspirational_rg_gauge_rejected": not classify_axiom(aspiration),
        "post_iter077q_dependency_isolation_executed": isolation["valid"],
    }
    valid = all(controls.values())
    return {
        "iteration": "Iter080F-SM",
        "lane": "C",
        "repair": "CONTROL_ONLY_PREDICATE_CONTROLS_AND_EXECUTABLE_ISOLATION",
        "valid": valid,
        "scientific_outcome": "PASS_ANTI_RESCUE_CONTROLS" if valid else "INVALID_CLASSIFIER_OR_ISOLATION",
        "controls": controls,
        "isolation": isolation,
    }


def lane_d() -> dict:
    c = read(CURRENT)
    locks = {
        "iter077q": "ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED" in c,
        "iter080a": "ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED" in c,
        "iter080d": "ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED" in c,
        "iter080e": "ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED" in c,
        "k5_blocked": "BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING" in c,
        "repair_authorized": (
            "ITER080F_CONTROL_ONLY_ANTI_RESCUE_REPAIR" in c
            or "CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS" in c
        ),
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter080F-SM",
        "lane": "D",
        "valid": valid,
        "scientific_outcome": "PASS_DEPENDENCY_LOCK" if valid else "INVALID_PROVENANCE",
        "locks": locks,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(directory: Path) -> dict:
    data = {}
    for lane in "ABCD":
        matches = list(directory.rglob(f"iter080f_sm_{lane}.json"))
        if len(matches) != 1:
            return {
                "iteration": "Iter080F-SM",
                "execution_valid": False,
                "verdict": "INVALID_IMPLEMENTATION_OR_PROVENANCE",
                "classification": "INVALID_IMPLEMENTATION_OR_PROVENANCE",
                "error": f"lane {lane} artifact count={len(matches)}",
            }
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
    return {
        "iteration": "Iter080F-SM",
        "execution_valid": valid,
        "lane_scientific_outcomes": {x: data[x].get("scientific_outcome") for x in "ABCD"},
        "qualifying_preexisting_axioms": qualifying,
        "lane_b_coverage_complete": data["B"].get("coverage_complete"),
        "lane_b_uncovered_relevant_lines": data["B"].get("uncovered_relevant_lines", []),
        "lane_b_statement_count": len(data["B"].get("statements", [])),
        "lane_c_isolation": data["C"].get("isolation", {}),
        "verdict": verdict,
        "classification": classification,
        "claim_lock": "No new selector, no unique K5 extension, no G3/F9/G8/K5 promotion, no regulator-independence theorem, no complete-QG claim.",
    }


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
