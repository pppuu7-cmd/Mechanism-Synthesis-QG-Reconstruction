#!/usr/bin/env python3
"""Prospectively frozen DSIR terminal handoff audit.

This is an evidence-integrity/dependency audit.  It does not turn a blocked
physical gate into a scientific PASS.  A PASS means that the DSIR handoff field
is terminally and reproducibly classified with a named downstream test.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

ALLOWED = {
    "PASS_SOURCE_NATIVE",
    "PASS_DERIVED_MSQGR",
    "NO_GO_SOURCE_NATIVE",
    "CONVERGENCE_ONLY",
    "BLOCKED_TRANSFER_TO_POLYGON",
    "NOT_APPLICABLE",
}


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def contains(path: str, *needles: str) -> tuple[bool, list[str]]:
    s = text(path)
    missing = [x for x in needles if x not in s]
    return not missing, missing


def lane_r():
    checks = {
        "iter065a_k5_missing": contains(
            "status/ITERATION_065A_RESULT.md",
            "ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING",
            "distributional K5 level",
        ),
        "iter066a_generic_framework_not_selector": contains(
            "status/ITERATION_066A_RESULT.md",
            "ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING",
            "complete_bridges=[]",
        ),
        "iter067a_conditional_theorem_route": contains(
            "status/ITERATION_067A_RESULT.md",
            "ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN",
            "Q1_JOINT_PHYSICAL_FAMILY",
            "Q4_DISTRIBUTIONAL_EPRL_BRIDGE",
        ),
        "iter068b_separate_contact_route_closed": contains(
            "status/ITERATION_068B_RESULT.md",
            "ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES",
            "joint finite-spectral-`i epsilon` multivariate boundary value",
        ),
        "iter068c_prepullback_control_only": contains(
            "status/ITERATION_068C_RESULT.md",
            "ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3",
            "does **not** establish that Eq.(5)/(6) survives a non-transverse correlated K4/K5 collision pullback",
        ),
    }
    missing = {k: v[1] for k, v in checks.items() if not v[0]}
    passed = not missing
    result = {
        "lane": "R",
        "pass": passed,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if passed else None,
        "missing_object": "JOINT_SOURCE_FAITHFUL_TOLLER_K5_BOUNDARY_VALUE" if passed else None,
        "scientific_gate_promoted": False,
        "checks": {k: v[0] for k, v in checks.items()},
        "missing_evidence_strings": missing,
        "polygon_test": [
            "keep the common finite-spectral-i-epsilon family correlated through the joint limit",
            "verify a tempered/distributional boundary value from explicit holomorphy-growth or wavefront hypotheses",
            "verify root/tree/cycle/order/regulator independence",
            "verify exact independent-wedge Eq.(5)/(6) control after correlated pullback/integration",
            "exclude arbitrary counterterms and fitted finite parts",
        ],
    }
    return result


def lane_s():
    checks = {
        "carrier_selected": contains(
            "candidates/CANDIDATE_A_CRQN_V0_2.md",
            "HYPOTHESIS_ONLY / CARRIER_SELECTED",
            "oriented causal labelled 2-complex",
        ),
        "source_vertex_exact": contains(
            "sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md",
            "Fixed-causal vertex — Eq. (4)",
            "integral prod_{a=2}^5 dg_a",
        ),
        "crqn_factor_unknown": contains(
            "candidates/CANDIDATE_A_CRQN_V0_2.md",
            "`F_causal` is **unknown**",
            "G3 quantum dynamics: `OPEN_BLOCKED`",
        ),
        "same_realization_requirement": contains(
            "docs/METHODOLOGY.md",
            "microstate -> dynamics/measure -> coarse graining -> continuum effective action -> normalized observables -> IR gravity/matter",
            "G3 — quantum-dynamics closure",
        ),
    }
    missing = {k: v[1] for k, v in checks.items() if not v[0]}
    passed = not missing
    result = {
        "lane": "S",
        "pass": passed,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if passed else None,
        "missing_object": "CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION" if passed else None,
        "scientific_gate_promoted": False,
        "checks": {k: v[0] for k, v in checks.items()},
        "missing_evidence_strings": missing,
        "polygon_test": [
            "instantiate one CRQN-specific local amplitude/measure rather than copy a comparator as novelty",
            "define normalization and physical boundary state space",
            "define and test gluing/composition",
            "verify causal compatibility and gauge covariance",
            "run mandatory mechanism ablations in the same realization",
        ],
    }
    return result


def lane_t():
    checks = {
        "carc_physical_open": contains(
            "bridges/M02_M04_M05_M07_CAUSAL_ANALYTIC_RG.md",
            "SYNTHESIS_DERIVED_CONSTRAINT / PHYSICAL_REALIZATION_OPEN",
            "Causal Analyticity–RG Commutator",
            "repeat over more than one blocking/refinement step",
        ),
        "cci_physical_target": contains(
            "bridges/M02_M04_M05_M07_CAUSAL_CYLINDRICAL_INTERTWINING.md",
            "SYNTHESIS_DERIVED_FINITE_SCALE_CONSTRAINT / PHYSICAL_REALIZATION_OPEN",
            "P_b'^± iota_b'b = iota_b'b P_b^±",
            "closure of the Toller analytic/pole class",
        ),
        "f9_current_blocked": contains(
            "status/CURRENT.md",
            "Physical F9: `BLOCKED`",
        ),
        "literature_gap_not_novelty": contains(
            "docs/LITERATURE_GAP_F9.md",
            "not a proof of global novelty",
            "did not surface a paper explicitly proving",
        ),
    }
    missing = {k: v[1] for k, v in checks.items() if not v[0]}
    passed = not missing
    result = {
        "lane": "T",
        "pass": passed,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if passed else None,
        "missing_object": "PHYSICAL_MULTISCALE_CCI_REALIZATION" if passed else None,
        "scientific_gate_promoted": False,
        "checks": {k: v[0] for k, v in checks.items()},
        "missing_evidence_strings": missing,
        "polygon_test": [
            "define physical H_b and P_b^+-",
            "derive rather than fit embedding/coarse-graining maps iota_b'b",
            "test cylindrical consistency over multiple refinements",
            "test P_b'^+- iota_b'b - iota_b'b P_b^+- = 0",
            "test closure of Toller analytic/pole class without new cross-branch data",
        ],
    }
    return result


def has_cycle(graph):
    state = {k: 0 for k in graph}

    def visit(v):
        if state[v] == 1:
            return True
        if state[v] == 2:
            return False
        state[v] = 1
        for w in graph[v]:
            if w not in graph or visit(w):
                return True
        state[v] = 2
        return False

    return any(visit(v) for v in graph if state[v] == 0)


def lane_u():
    evidence_checks = {
        "iter076n_native_p3_no_go": contains(
            "results/ITER076N_EXACT_AMPLITUDE_ORIENTATION_SELECTOR_PROVENANCE_RESULT.md",
            "ITER076N_EQ4_EQ7_HAVE_NO_CANONICAL_S5_ODD_SELECTOR_EXACT_SIGNED_P3_BLOCKED_SEMICLASSICAL_ONLY_SCOPED",
            "source-native exact signed-P3 lane terminates here",
        ),
        "carrier_and_gate_scope": contains(
            "candidates/CANDIDATE_A_CRQN_V0_2.md",
            "G1 ontology: `PARTIAL_PASS`",
            "G2 causal/Lorentz compatibility: `PARTIAL_PASS_EXTERNAL`",
            "G8 nontriviality: `HIGH_RISK_OPEN`",
        ),
        "methodology_g4_g7": contains(
            "docs/METHODOLOGY.md",
            "G4 — RG/continuum closure",
            "G5 — symmetry/anomaly closure",
            "G6 — IR Einstein/QFT closure",
            "G7 — observable closure",
        ),
    }

    fields = {
        "source_evidence": {
            "status": "PASS_SOURCE_NATIVE",
            "scope": "causal vertex Eq.(3)-(7) and spectral i-epsilon",
            "missing_object": None,
            "dependencies": [],
            "polygon_test": "retain source equations as immutable comparator",
        },
        "carrier_selection": {
            "status": "PASS_DERIVED_MSQGR",
            "scope": "oriented causal labelled 2-complex provisional carrier",
            "missing_object": None,
            "dependencies": [],
            "polygon_test": "instantiate carrier without changing its declared ontology",
        },
        "g1_final_equivalence_gauge": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "final ontology closure",
            "missing_object": "FINAL_REPRESENTATION_CATEGORY_EQUIVALENCE_GAUGE_RELATIONS",
            "dependencies": ["carrier_selection"],
            "polygon_test": "fix exact group/representation/equivalence data and verify no hidden redundant states",
        },
        "g2_no_preferred_structure": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "continuum Lorentz/causal closure",
            "missing_object": "NO_PREFERRED_FRAME_FOLIATION_CONTINUUM_CERTIFICATE",
            "dependencies": ["carrier_selection", "source_evidence"],
            "polygon_test": "show regulator/bookkeeping foliation leaves physical observables or classify a different symmetry theory",
        },
        "signed_p3_source_native": {
            "status": "NO_GO_SOURCE_NATIVE",
            "scope": "exact Eq.(4)/(7) amplitude selector",
            "missing_object": None,
            "dependencies": ["source_evidence"],
            "polygon_test": "P0 keeps unsigned Hodge line; any orientation selector requires explicit P1 extension branch",
        },
        "epsilon_minus1_signed_p3_native": {
            "status": "NOT_APPLICABLE",
            "scope": "signed-P3-dependent source coefficient",
            "missing_object": None,
            "dependencies": ["signed_p3_source_native"],
            "polygon_test": "do not assign zero/nonzero/divergent value in P0; define anew only in an explicit extension branch",
        },
        "k5_correlated_boundary_value": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "physical correlated distributional object",
            "missing_object": "JOINT_SOURCE_FAITHFUL_TOLLER_K5_BOUNDARY_VALUE",
            "dependencies": ["source_evidence"],
            "polygon_test": "execute lane-R theorem contract",
        },
        "g3_quantum_dynamics": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "CRQN normalized finite-scale dynamics",
            "missing_object": "CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION",
            "dependencies": ["carrier_selection", "source_evidence"],
            "polygon_test": "execute lane-S same-realization dynamics contract",
        },
        "f9_causal_analytic_rg": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "physical CCI/CARC realization",
            "missing_object": "PHYSICAL_MULTISCALE_CCI_REALIZATION",
            "dependencies": ["g3_quantum_dynamics"],
            "polygon_test": "execute lane-T multiscale CCI contract",
        },
        "g4_rg_continuum": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "continuum critical surface",
            "missing_object": "CRQN_COARSE_GRAINING_FLOW_AND_CRITICAL_SURFACE",
            "dependencies": ["g3_quantum_dynamics"],
            "polygon_test": "derive coarse-graining flow and test a controlled continuum trajectory",
        },
        "g5_symmetry_anomaly": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "gauge/diffeomorphism/refoliation closure",
            "missing_object": "CONTINUUM_GAUGE_ANOMALY_CLOSURE",
            "dependencies": ["g4_rg_continuum"],
            "polygon_test": "verify emergent gauge/refoliation structure without uncontrolled anomaly",
        },
        "g6_ir_einstein_qft": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "IR recovery",
            "missing_object": "SAME_REALIZATION_EINSTEIN_QFT_IR_LIMIT",
            "dependencies": ["g4_rg_continuum", "g5_symmetry_anomaly"],
            "polygon_test": "recover EH plus matter with controlled corrections and causal propagation",
        },
        "g7_observable": {
            "status": "BLOCKED_TRANSFER_TO_POLYGON",
            "scope": "normalized cross-scale observable",
            "missing_object": "SAME_REALIZATION_NORMALIZED_OBSERVABLE",
            "dependencies": ["g3_quantum_dynamics", "g4_rg_continuum"],
            "polygon_test": "derive at least one normalized observable from the same measure/flow",
        },
        "g8_nontriviality": {
            "status": "CONVERGENCE_ONLY",
            "scope": "DSIR exit; no established beyond-comparator dynamical relation",
            "missing_object": None,
            "dependencies": ["g3_quantum_dynamics", "f9_causal_analytic_rg"],
            "polygon_test": "promote only if a same-realization relation/prediction is not equivalent to a registered source framework",
        },
    }

    statuses_ok = all(v["status"] in ALLOWED for v in fields.values())
    blocked_have_objects = all(
        v["status"] != "BLOCKED_TRANSFER_TO_POLYGON" or bool(v["missing_object"])
        for v in fields.values()
    )
    every_test = all(bool(v["polygon_test"]) for v in fields.values())
    graph = {k: v["dependencies"] for k, v in fields.items()}
    acyclic = not has_cycle(graph)
    evidence_ok = all(v[0] for v in evidence_checks.values())
    passed = statuses_ok and blocked_have_objects and every_test and acyclic and evidence_ok

    return {
        "lane": "U",
        "pass": passed,
        "checks": {
            "allowed_statuses_only": statuses_ok,
            "all_blockers_name_missing_object": blocked_have_objects,
            "every_field_has_polygon_test": every_test,
            "dependency_graph_acyclic": acyclic,
            "authoritative_evidence_present": evidence_ok,
        },
        "fields": fields,
        "evidence_checks": {k: v[0] for k, v in evidence_checks.items()},
    }


LANES = {"R": lane_r, "S": lane_s, "T": lane_t, "U": lane_u}


def write_lane(lane, result):
    p = OUT / f"dsir_terminal_lane_{lane}.json"
    p.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


def aggregate(input_dir: str):
    records = {}
    base = Path(input_dir)
    for lane in "RSTU":
        matches = list(base.rglob(f"dsir_terminal_lane_{lane}.json"))
        if len(matches) != 1:
            raise RuntimeError(f"expected exactly one lane {lane} artifact, found {len(matches)}")
        records[lane] = json.loads(matches[0].read_text(encoding="utf-8"))

    all_pass = all(records[x].get("pass") is True for x in "RSTU")
    u_fields = records["U"].get("fields", {})
    terminal_count = sum(1 for v in u_fields.values() if v.get("status") in ALLOWED)
    total_count = len(u_fields)
    completeness = 100 if all_pass and terminal_count == total_count and total_count else round(100 * terminal_count / max(total_count, 1))

    result = {
        "classification": "DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V1" if completeness == 100 else "DSIR_FUNNEL_CONTRACT_INCOMPLETE_REVIEW",
        "lane_pass": {x: records[x]["pass"] for x in "RSTU"},
        "contract_completeness_percent": completeness,
        "contract_complete": completeness == 100,
        "scientific_solution_percent_claimed": None,
        "meaning_of_100": "handoff-contract completeness only; blocked/no-go/convergence terminal statuses remain scientifically unresolved or negative",
        "physical_gate_promotions": [],
        "terminal_statuses": {
            "R_K5": records["R"].get("terminal_status"),
            "S_G3": records["S"].get("terminal_status"),
            "T_F9": records["T"].get("terminal_status"),
            "signed_P3_P0": u_fields.get("signed_p3_source_native", {}).get("status"),
            "G8": u_fields.get("g8_nontriviality", {}).get("status"),
        },
        "exit_fields": u_fields,
        "claim_lock": "No complete-QG/new-physics/finiteness-divergence/G3/F9/G8/K5 promotion follows from contract completeness.",
    }
    (OUT / "dsir_terminal_handoff_aggregate.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if completeness == 100 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    args = ap.parse_args()
    if args.aggregate_dir:
        raise SystemExit(aggregate(args.aggregate_dir))
    if not args.lane:
        ap.error("provide --lane or --aggregate-dir")
    result = LANES[args.lane]()
    write_lane(args.lane, result)
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
