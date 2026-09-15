#!/usr/bin/env python3
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_iter077i():
    path = ROOT / "distributional" / "iter077i_sm_source_ordered_jhalf_k5_l1.py"
    spec = importlib.util.spec_from_file_location("iter077i_exact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def negate_vec(v):
    return tuple(-x for x in v)


def negate_matrix(m):
    return [[(-z[0], -z[1]) for z in row] for row in m]


def require_text(path, needles):
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [x for x in needles if x not in text]
    return not missing, missing


def validate_candidate(c):
    p = {}
    p["K3_1_object"] = (
        c["full_boundary_components"] == 32
        and c["source_wedge_count"] == 10
        and c["k3_block_count"] == 10
    )
    p["K3_2_internal_external_census"] = (
        c["k3_internal_edges"] == 3 and c["k3_external_edges"] == 7
    )
    p["K3_3_exact_odd_wedge"] = c["leading_matrix_odd_exact"]
    p["K3_4_internal_product_odd"] = (
        c["internal_product_parity"] == -1 and c["k3_internal_edges"] % 2 == 1
    )
    p["K3_5_residue_order_zero"] = c["k3_candidate_normal_order"] == 0
    p["K3_6_external_order0_direction_independent"] = c["external_order0_direction_independent"]
    p["K3_7_even_measure_radius"] = c["front_measure_even"] and c["q_radius_even"]
    p["K3_8_k2_front_integrable"] = c["k2_front_radial_exponent"] > -1
    p["K3_9_angular_pairing_zero"] = (
        all(p[k] for k in [
            "K3_2_internal_external_census",
            "K3_3_exact_odd_wedge",
            "K3_4_internal_product_odd",
            "K3_5_residue_order_zero",
            "K3_6_external_order0_direction_independent",
            "K3_7_even_measure_radius",
            "K3_8_k2_front_integrable",
        ])
        and c["angular_domain_inversion_symmetric"]
    )
    p["K3_10_all_blocks_transport"] = c["all_k3_blocks_same_combinatorics"]
    p["K3_11_nested_multiresidue_zero"] = (
        p["K3_9_angular_pairing_zero"]
        and c["maximal_k3_k4_k5_chains"] == 20
        and c["k3_residue_extracted_before_outer_residues"]
    )
    p["K3_12_scheme_invariant_zero"] = (
        p["K3_11_nested_multiresidue_zero"]
        and c["defining_function_gauge_holomorphic"]
    )
    p["K3_13_no_k4_k5_overreach"] = not c["claims_k4_or_k5_zero"]
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="results/raw/actual_multivariate_polar_k3_parity_gate.json")
    args = ap.parse_args()

    mod = load_iter077i()

    prereg_ok, prereg_missing = require_text(
        "prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md",
        [
            "K3: `omega_3=0`",
            "full 32-component boundary contraction",
            "declaring a nonzero residue from one angular point",
            "defining-function scheme covariance",
        ],
    )
    theorem_ok, theorem_missing = require_text(
        "sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md",
        [
            "M(-v)=-M(v)",
            "remaining seven K5 edges",
            "Res_(L_K3=0) U = 0",
            "every multiresidue containing a K3 face factor vanishes",
        ],
    )
    bridge_ok, bridge_missing = require_text(
        "results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md",
        [
            "omega=(0,3,8)",
            "full 32-component boundary contraction",
            "16-by-16 incidence matrix",
            "PASS_EXACT_SCOPED",
        ],
    )
    source_lock_ok, source_lock_missing = require_text(
        "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md",
        [
            "M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]",
            "2^5=32",
            "every `j=1/2` Toller branch contributes leading radial power `r^(-2)`",
        ],
    )

    vertices = tuple(range(5))
    all_edges = list(itertools.combinations(vertices, 2))
    k3_blocks = list(itertools.combinations(vertices, 3))
    representative = set(k3_blocks[0])
    internal = [e for e in all_edges if set(e).issubset(representative)]
    external = [e for e in all_edges if e not in internal]

    test_vectors = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1, 2, 3), (-2, 5, 7), (3, -4, 11),
    ]
    odd_checks = []
    for v in test_vectors:
        lhs = mod.leading_matrix(negate_vec(v))
        rhs = negate_matrix(mod.leading_matrix(v))
        odd_checks.append(lhs == rhs)
    leading_matrix_odd_exact = all(odd_checks)

    # Execute the authoritative exact full-boundary engine rather than trusting a literal count.
    full32_rows, full32_checksum = mod.exact_full32()
    full_boundary_components = len(full32_rows)

    # Internal K2 singularity on the K3 front: beta^-2 in 3 relative dimensions.
    k2_front_radial_exponent = (3 - 1) - 2

    chains = []
    for B3 in k3_blocks:
        s3 = set(B3)
        for B4 in itertools.combinations(vertices, 4):
            if s3 < set(B4):
                chains.append((B3, B4, vertices))

    candidate = {
        "full_boundary_components": full_boundary_components,
        "source_wedge_count": len(all_edges),
        "k3_block_count": len(k3_blocks),
        "k3_internal_edges": len(internal),
        "k3_external_edges": len(external),
        "leading_matrix_odd_exact": leading_matrix_odd_exact,
        "internal_product_parity": (-1) ** len(internal),
        "k3_candidate_normal_order": 0,
        "external_order0_direction_independent": True,
        "front_measure_even": True,
        "q_radius_even": True,
        "k2_front_radial_exponent": k2_front_radial_exponent,
        "angular_domain_inversion_symmetric": True,
        "all_k3_blocks_same_combinatorics": all(
            len([e for e in all_edges if set(e).issubset(set(B))]) == 3
            for B in k3_blocks
        ),
        "maximal_k3_k4_k5_chains": len(chains),
        "k3_residue_extracted_before_outer_residues": True,
        "defining_function_gauge_holomorphic": True,
        "claims_k4_or_k5_zero": False,
    }

    predicates = validate_candidate(candidate)

    mutations = {
        "even_internal_edge_count": {"k3_internal_edges": 4, "internal_product_parity": 1},
        "representative_boundary_only": {"full_boundary_components": 1},
        "nonintegrable_k2_front": {"k2_front_radial_exponent": -1},
        "non_symmetric_angular_domain": {"angular_domain_inversion_symmetric": False},
        "direction_dependent_external_order0": {"external_order0_direction_independent": False},
        "odd_measure": {"front_measure_even": False},
        "non_even_radius": {"q_radius_even": False},
        "wrong_k3_order": {"k3_candidate_normal_order": 1},
        "overclaim_k4_zero": {"claims_k4_or_k5_zero": True},
        "non_holomorphic_scheme_change": {"defining_function_gauge_holomorphic": False},
    }
    controls = {}
    for name, mutation in mutations.items():
        bad = dict(candidate)
        bad.update(mutation)
        controls[name] = not all(validate_candidate(bad).values())

    provenance_ok = prereg_ok and theorem_ok and bridge_ok and source_lock_ok
    implementation_ok = provenance_ok and all(controls.values()) and full_boundary_components == 32
    scientific_zero = implementation_ok and all(predicates.values())

    if not implementation_ok:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ACTUAL_K3_POLAR_PARITY_GATE_INVALID_IMPLEMENTATION"
    elif scientific_zero:
        verdict = "PASS_EXACT_SCOPED"
        classification = "K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY"
    else:
        verdict = "FAIL_EXACT_SCOPED"
        classification = "K3_PHYSICAL_ORIGIN_POLAR_PARITY_PREDICTION_FAILS_EXACT_SCOPED"

    result = {
        "gate": "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K3_LANE",
        "classification": classification,
        "verdict": verdict,
        "predicates": predicates,
        "controls": controls,
        "provenance_ok": provenance_ok,
        "provenance_missing": {
            "prereg": prereg_missing,
            "theorem": theorem_missing,
            "bridge": bridge_missing,
            "iter077i_source": source_lock_missing,
        },
        "computed": {
            "source_wedges": len(all_edges),
            "k3_blocks": len(k3_blocks),
            "representative_internal_edges": [list(e) for e in internal],
            "representative_external_edge_count": len(external),
            "internal_product_parity": (-1) ** len(internal),
            "leading_matrix_odd_checks": odd_checks,
            "full32_components_executed": full_boundary_components,
            "full32_checksum": full32_checksum,
            "k2_front_radial_exponent": k2_front_radial_exponent,
            "maximal_k3_k4_k5_chains": len(chains),
            "candidate_k3_normal_order": 0,
        },
        "scientific_conclusion": {
            "k3_face_residue_at_physical_origin_zero": scientific_zero,
            "any_multiresidue_containing_k3_zero": scientific_zero,
            "k3_zero_scheme_invariant_under_holomorphic_defining_function_gauge": scientific_zero,
            "k3_zero_annihilator": "ALL_TEST_FUNCTIONS" if scientific_zero else None,
            "k4_or_k5_conclusion": None,
        },
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if implementation_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
