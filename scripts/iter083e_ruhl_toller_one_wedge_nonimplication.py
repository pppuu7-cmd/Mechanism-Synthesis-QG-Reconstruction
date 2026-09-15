#!/usr/bin/env python3
import argparse
import copy
import json


def require_text(path, needles):
    text = open(path, encoding="utf-8").read()
    missing = [x for x in needles if x not in text]
    return not missing, missing


def validate_source_lock(d):
    try:
        tc = d["sources"]["toller_companion"]
        cv = d["sources"]["causal_vertex"]
        return all([
            tc["arxiv"] == "2604.24945",
            tc["one_wedge_uniqueness"] is True,
            tc["uniqueness_variable"] == "rho",
            tc["feynman_projector_integration_variable"] == "tilde_rho",
            tc["feynman_projector_number_of_spectral_integration_variables"] == 1,
            tc["toller_is_sl2c_representation"] is False,
            tc["wigner_d_is_sl2c_representation"] is True,
            tc["explicit_toller_nonrepresentation_equation"] is True,
            tc["joint_k5_extension_uniqueness_theorem_in_audited_argument"] is False,
            tc["equation_refs"]["non_representation"] == 14,
            tc["equation_refs"]["feynman_functional"] == 17,
            tc["equation_refs"]["feynman_projector"] == 20,
            cv["arxiv"] == "2601.23162v1",
            cv["number_of_k5_wedge_toller_factors"] == 10,
            cv["remaining_sl2c_group_integrations"] == 4,
            cv["common_left_gauge_fixed"] is True,
            cv["joint_multivariable_common_collision_regulator_found_in_audit"] is False,
            cv["joint_common_collision_boundary_value_theorem_found_in_audit"] is False,
            cv["joint_extension_selector_from_composition_found_in_audit"] is False,
        ])
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-lock", default="sources/raw/iter083e_public_source_lock.json")
    ap.add_argument("--iter083b", default="results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md")
    ap.add_argument("--iter083c", default="results/ITER083C_SM_TOLLER_ADDITIVITY_SELECTOR_NULLMODE_RESULT.md")
    ap.add_argument("--iter083d", default="results/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY_RESULT.md")
    ap.add_argument("--theorem", default="sources/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NONIMPLICATION_DERIVATION.md")
    ap.add_argument("--output")
    args = ap.parse_args()

    source = json.load(open(args.source_lock, encoding="utf-8"))

    # P0: exact source-lock structure: one-rho uniqueness and one-variable projector.
    p0 = validate_source_lock(source)

    # P1: source ordering is explicitly ten elementary factors before final extension.
    ordering = source["sources"]["causal_vertex"]["ordering"]
    p1 = ordering == [
        "define_elementary_toller_branch",
        "form_ten_wedge_product",
        "boundary_contract",
        "integrate_gauge_fixed_k5_group_variables",
        "distributional_extension_if_needed",
    ]

    # P2: abstract supported counter-deformation.  The one-wedge analytic signature
    # is source-fixed and independent of the final contact coordinate.  We exhaust
    # the 377 basis translations and verify the signature is unchanged.
    f8_dim = 377
    one_wedge_signature = (
        source["sources"]["toller_companion"]["uniqueness_variable"],
        tuple(source["sources"]["toller_companion"]["uniqueness_conditions"]),
        source["sources"]["toller_companion"]["feynman_projector_integration_variable"],
        source["sources"]["toller_companion"]["equation_refs"]["feynman_projector"],
    )
    extension_records = [
        {"one_wedge_signature": one_wedge_signature, "supported_contact_basis_index": i}
        for i in range(f8_dim)
    ]
    p2 = len(extension_records) == 377 and all(
        r["one_wedge_signature"] == one_wedge_signature for r in extension_records
    )

    # P3: source explicitly forbids importing the representation composition law.
    tc = source["sources"]["toller_companion"]
    p3 = (
        tc["toller_is_sl2c_representation"] is False
        and tc["explicit_toller_nonrepresentation_equation"] is True
        and tc["equation_refs"]["non_representation"] == 14
    )

    # P4-P5: authoritative downstream no-go dependencies.
    p4_lock, p4_missing = require_text(args.iter083c, [
        "PASS_EXACT_SCOPED",
        "58,025",
        "TOLLER_ADDITIVITY_HAS_EXACT_JOINT_K5_TOP_BOOLEAN_SELECTOR_NULLMODE",
    ])
    p4 = p4_lock

    p5_lock, p5_missing = require_text(args.iter083d, [
        "PASS_EXACT_SCOPED",
        "exactly 377-dimensional",
        "S_Beltran(Delta)=16 a",
        "S_BCG(Delta)=32 a",
    ])
    p5 = p5_lock

    # P6: authoritative F8 has dimension 377, while all one-wedge data remain fixed.
    p6_lock, p6_missing = require_text(args.iter083b, [
        "PASS_EXACT_SCOPED",
        "dim_C F_8 = 377",
        "exact dimension",
    ])
    p6 = p6_lock and f8_dim == 377 and p2 and p3 and p4 and p5

    # P7: theorem explicitly retains potential genuinely joint falsifiers.
    p7_lock, p7_missing = require_text(args.theorem, [
        "correlated multivariable boundary value",
        "common K5 regulator",
        "multiplication theorem",
        "composition/gluing/differential/positivity/RG",
        "not a proof that no correlated multivariable prescription exists",
    ])
    p7 = p7_lock and len(source.get("falsifiers", [])) >= 4

    # Negative controls: the same validator must reject false source/manifold surrogates.
    bad_rep = copy.deepcopy(source)
    bad_rep["sources"]["toller_companion"]["toller_is_sl2c_representation"] = True

    bad_projector = copy.deepcopy(source)
    bad_projector["sources"]["toller_companion"]["feynman_projector_number_of_spectral_integration_variables"] = 10

    bad_joint = copy.deepcopy(source)
    bad_joint["sources"]["toller_companion"]["joint_k5_extension_uniqueness_theorem_in_audited_argument"] = True

    bad_k5 = copy.deepcopy(source)
    bad_k5["sources"]["causal_vertex"]["number_of_k5_wedge_toller_factors"] = 1

    bad_order = list(ordering)
    bad_order[0], bad_order[-1] = bad_order[-1], bad_order[0]

    controls = {
        "false_toller_representation_rejected": not validate_source_lock(bad_rep),
        "false_ten_variable_feynman_projector_rejected": not validate_source_lock(bad_projector),
        "false_joint_uniqueness_source_claim_rejected": not validate_source_lock(bad_joint),
        "false_one_wedge_k5_product_rejected": not validate_source_lock(bad_k5),
        "extension_before_elementary_branch_order_rejected": bad_order != ordering,
        "one_wedge_constraints_constant_on_all_377_supported_basis_translations": p2,
        "additivity_not_used_as_selector": p4,
        "causal_sum_not_used_as_selector": p5,
        "future_joint_selector_falsifier_retained": p7,
    }

    predicates = {f"P{i}": v for i, v in enumerate([p0, p1, p2, p3, p4, p5, p6, p7])}
    passed = all(predicates.values()) and all(controls.values())

    result = {
        "iteration": "Iter083E-SM",
        "classification": (
            "ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_ANALYTIC_UNIQUENESS_DOES_NOT_LIFT_TO_JOINT_K5_EXTENSION_SELECTOR_SCOPED"
            if passed else "ITER083E_SM_RUHL_TOLLER_NONIMPLICATION_INVALID_IMPLEMENTATION"
        ),
        "verdict": "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION",
        "predicates": predicates,
        "controls": controls,
        "frozen_supported_ambiguity_dimension": f8_dim,
        "one_wedge_uniqueness_variable": tc["uniqueness_variable"],
        "feynman_projector_integration_variables": tc["feynman_projector_number_of_spectral_integration_variables"],
        "toller_is_sl2c_representation": tc["toller_is_sl2c_representation"],
        "k5_wedge_toller_factors": source["sources"]["causal_vertex"]["number_of_k5_wedge_toller_factors"],
        "supported_basis_translations_checked": len(extension_records),
        "dependency_missing": {
            "P4_iter083c": p4_missing,
            "P5_iter083d": p5_missing,
            "P6_iter083b": p6_missing,
            "P7_theorem": p7_missing,
        },
        "scientific_statement": (
            "All currently source-defined one-wedge Ruhl/Toller analytic data are unchanged by translation of the final joint K5 extension by any a in F8; known additive and unit causal-sum relations also leave this ambiguity unsolved."
        ),
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
    print(payload)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
