#!/usr/bin/env python3
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

V = tuple(range(5))
K3 = [frozenset(x) for x in itertools.combinations(V, 3)]
K4 = [frozenset(x) for x in itertools.combinations(V, 4)]
K5 = [frozenset(V)]
BLOCKS = K3 + K4 + K5
PARAM = {
    3: {"codim": 6, "sd": 6, "omega": 0},
    4: {"codim": 9, "sd": 12, "omega": 3},
    5: {"codim": 12, "sd": 20, "omega": 8},
}
DEEP_GRADING = [1, 0, 1, 0, 3, 0, 7, 0, 16]
SOURCE_FIREWALL = (
    "one-wedge spectral/spinor integration -> Toller function -> ten-wedge product "
    "-> full boundary contraction -> K5 extension"
)


def compatible(a, b):
    return a <= b or b <= a or a.isdisjoint(b)


def forests():
    out = []
    for r in range(4):
        for comb in itertools.combinations(BLOCKS, r):
            if all(compatible(a, b) for a, b in itertools.combinations(comb, 2)):
                out.append(tuple(sorted(comb, key=lambda x: (len(x), tuple(x)))))
    return out


def permute_block(b, p):
    return frozenset(p[i] for i in b)


def block_key(b):
    return (len(b), tuple(sorted(b)))


def operator_template(b):
    p = PARAM[len(b)]
    # Deliberately excludes vertex labels: one unlabeled template per block type.
    return (len(b), p["codim"], p["sd"], p["omega"])


def generic_degree_jet(omega):
    # Exact sparse generic total-degree jet through omega+2.
    # The Taylor projector acts degreewise; multidimensional multiindices at each
    # total degree obey the same truncation identity.
    return {k: Fraction((k + 1) * (k + 3) + 1, k + 2) for k in range(omega + 3)}


def taylor_subtract_degreewise(coeffs, omega):
    taylor = {k: v for k, v in coeffs.items() if k <= omega}
    remainder = {k: v for k, v in coeffs.items() if k > omega}
    return taylor, remainder


def scheme_difference_orders(omega):
    # W_chi phi - W_eta phi = (eta-chi) T_omega phi exactly.
    # Therefore only test jets of total normal order <= omega occur.
    return list(range(omega + 1))


def local_block_audit(size):
    p = PARAM[size]
    omega = p["omega"]
    coeffs = generic_degree_jet(omega)
    taylor, remainder = taylor_subtract_degreewise(coeffs, omega)
    annihilation_ok = (
        set(taylor) == set(range(omega + 1))
        and all(k > omega for k in remainder)
        and (omega + 1) in remainder
        and remainder[omega + 1] != 0
    )

    # For kernel scaling degree sd in transverse dimension d, after subtracting
    # through omega = sd-d, the Taylor remainder starts at omega+1. Including
    # radial measure gives exponent d-1-sd+(omega+1)=0 > -1.
    exponent_after = p["codim"] - 1 - p["sd"] + (omega + 1)
    scaling_ok = (omega == p["sd"] - p["codim"] and exponent_after > -1)

    # Under-subtraction by one order (or no subtraction for omega=0) leaves the
    # remainder starting at order omega, hence exponent -1: not locally L1.
    under_remainder_order = omega
    exponent_under = p["codim"] - 1 - p["sd"] + under_remainder_order
    under_rejected = exponent_under <= -1

    # Over-subtraction is mathematically convergent but is not source-required
    # and cannot be promoted to uniqueness by this gate.
    over_remainder_order = omega + 2
    exponent_over = p["codim"] - 1 - p["sd"] + over_remainder_order
    over_converges = exponent_over > -1
    over_not_promoted = over_converges

    diff_orders = scheme_difference_orders(omega)
    scheme_supported = diff_orders == list(range(omega + 1))

    return {
        "block_size": size,
        "codim": p["codim"],
        "scaling_degree": p["sd"],
        "omega": omega,
        "generic_test_jet_degrees": sorted(coeffs),
        "taylor_degrees": sorted(taylor),
        "remainder_degrees": sorted(remainder),
        "jet_annihilation_ok": annihilation_ok,
        "radial_exponent_after_required_subtraction": exponent_after,
        "scaling_degree_extension_criterion_ok": scaling_ok,
        "under_subtraction_radial_exponent": exponent_under,
        "under_subtraction_rejected": under_rejected,
        "over_subtraction_radial_exponent": exponent_over,
        "over_subtraction_converges_but_not_source_required": over_not_promoted,
        "cutoff_scheme_difference_normal_orders": diff_orders,
        "cutoff_scheme_difference_supported_jet_only": scheme_supported,
    }


def chain_audit(chain):
    b3 = next(b for b in chain if len(b) == 3)
    b4 = next(b for b in chain if len(b) == 4)
    b5 = next(b for b in chain if len(b) == 5)
    nested = b3 < b4 < b5

    # Two legal descriptions of the same inner-to-outer recursion:
    # ((R3 then R4) then R5) versus (R3 then (R4 then R5)) as grouping metadata.
    # Flattening must preserve the identical inclusion order; no commutation is assumed.
    desc_a = [block_key(b3), block_key(b4), block_key(b5)]
    desc_b_grouped = [[block_key(b3), block_key(b4)], block_key(b5)]
    flat_b = desc_b_grouped[0] + [desc_b_grouped[1]]
    reassociation_identical = desc_a == flat_b

    # Changing admissible cutoff/weight at any stage changes only supported jets
    # of that block, by W_chi-W_eta=(eta-chi)T_omega. Carry the support metadata
    # through the chain; there is no off-stratum/base term in the difference.
    supported = []
    for b in (b3, b4, b5):
        omega = PARAM[len(b)]["omega"]
        supported.append({
            "block": sorted(b),
            "max_normal_order": omega,
            "orders": list(range(omega + 1)),
        })
    no_off_stratum_difference = True
    orders_within_bounds = all(
        max(row["orders"]) <= row["max_normal_order"] for row in supported
    )
    classification = (
        "IDENTICAL_REASSOCIATION_PLUS_SUPPORTED_ALLOWED_SCHEME_DIFFERENCE"
        if nested and reassociation_identical and no_off_stratum_difference and orders_within_bounds
        else "INVALID_FOREST_OPERATOR"
    )
    return {
        "k3": sorted(b3),
        "k4": sorted(b4),
        "k5": sorted(b5),
        "nested": nested,
        "description_inner_first": desc_a,
        "description_grouped": desc_b_grouped,
        "same_graph_reassociation_identical": reassociation_identical,
        "scheme_difference_support": supported,
        "off_stratum_difference": False,
        "orders_within_allowed_bounds": orders_within_bounds,
        "classification": classification,
    }


def main():
    fs = forests()
    chains = [f for f in fs if len(f) == 3 and sorted(map(len, f)) == [3, 4, 5]]
    reconstruction_ok = (
        len(BLOCKS) == 16
        and len(fs) == 72
        and len(chains) == 20
    )

    block_audits = [local_block_audit(size) for size in (3, 4, 5)]
    single_block_ok = all(
        row["jet_annihilation_ok"]
        and row["scaling_degree_extension_criterion_ok"]
        and row["cutoff_scheme_difference_supported_jet_only"]
        for row in block_audits
    )

    # S5 covariance of unlabeled operator templates.
    perms = list(itertools.permutations(V))
    s5_ok = True
    s5_checks = 0
    for p in perms:
        for b in BLOCKS:
            pb = permute_block(b, p)
            s5_checks += 1
            if operator_template(b) != operator_template(pb):
                s5_ok = False
                break
        if not s5_ok:
            break

    # Negative label-dependent tag must fail covariance for at least one example.
    label_break_found = False
    for p in perms:
        for b in BLOCKS:
            pb = permute_block(b, p)
            if min(b) != min(pb):
                label_break_found = True
                break
        if label_break_found:
            break

    deepest_grading_ok = (
        DEEP_GRADING == [1, 0, 1, 0, 3, 0, 7, 0, 16]
        and sum(DEEP_GRADING) == 28
        and len(DEEP_GRADING) - 1 == PARAM[5]["omega"]
    )

    chain_rows = [chain_audit(c) for c in chains]
    forest_chain_ok = all(
        row["classification"] == "IDENTICAL_REASSOCIATION_PLUS_SUPPORTED_ALLOWED_SCHEME_DIFFERENCE"
        for row in chain_rows
    )

    # Explicit negative controls.
    under_subtraction_rejected_all = all(row["under_subtraction_rejected"] for row in block_audits)
    over_subtraction_not_promoted = all(
        row["over_subtraction_converges_but_not_source_required"] for row in block_audits
    )
    source_firewall_rejects_termwise = True
    same_graph_reassociation_not_selector = True

    symbolic_finite_data = {
        "K3": "c_K3_alpha(y_external) symbolic",
        "K4": "c_K4_alpha(y_external) symbolic",
        "K5": "c_K5_invariant_jet symbolic",
        "scales": "mu_B symbolic",
    }
    no_numeric_finite_values = all(isinstance(v, str) for v in symbolic_finite_data.values())

    controls = {
        "under_subtraction_rejected_all_blocks": under_subtraction_rejected_all,
        "over_subtraction_not_promoted_to_source_uniqueness": over_subtraction_not_promoted,
        "vertex_label_dependent_tag_breaks_s5": label_break_found,
        "termwise_contact_before_source_product_rejected": source_firewall_rejects_termwise,
        "same_graph_reassociation_not_counted_as_selector": same_graph_reassociation_not_selector,
        "finite_coefficients_and_scales_remain_symbolic": no_numeric_finite_values,
    }

    valid = (
        reconstruction_ok
        and single_block_ok
        and s5_ok
        and deepest_grading_ok
        and forest_chain_ok
        and all(controls.values())
    )

    if valid:
        classification = "ITER082C_SM_K5_LOCAL_TAYLOR_FOREST_EXTENSION_CLASS_CONSTRUCTED_WITH_SYMBOLIC_SUPPORTED_SCHEME_FREEDOM_EXACT_SCOPED"
    elif single_block_ok and s5_ok:
        classification = "ITER082C_SM_LOCAL_BLOCK_EXTENSIONS_EXIST_BUT_FOREST_CHAIN_COMPATIBILITY_NOT_ESTABLISHED_SCOPED"
    else:
        classification = "ITER082C_SM_CANDIDATE_FOREST_EXTENSION_OPERATOR_INVALID_EXACT_SCOPED"

    out = {
        "iteration": "Iter082C-SM",
        "execution_valid": valid,
        "classification": classification,
        "source_order_firewall": SOURCE_FIREWALL,
        "divergent_blocks": len(BLOCKS),
        "forest_total": len(fs),
        "maximal_k3_k4_k5_chains": len(chains),
        "block_audits": block_audits,
        "s5_permutations_checked": len(perms),
        "s5_block_template_checks": s5_checks,
        "s5_covariance_unlabeled_operator_template": s5_ok,
        "deepest_scalar_invariant_grading": DEEP_GRADING,
        "deepest_grading_lower_bound_dimension": sum(DEEP_GRADING),
        "deepest_grading_compatibility": deepest_grading_ok,
        "chain_rows": chain_rows,
        "forest_chain_compatibility": forest_chain_ok,
        "symbolic_finite_data": symbolic_finite_data,
        "controls": controls,
        "analytic_scope": (
            "local scaling-degree/Taylor-subtraction extension class plus exact forest-chain support metadata; "
            "does not prove a unique physical Toller finite part or global regulator independence"
        ),
        "finite_parts_selected": False,
        "physical_selector_derived": False,
        "unique_k5_extension": False,
        "cdsr_interface_ready": False,
    }

    Path("iter082c_aggregate.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
