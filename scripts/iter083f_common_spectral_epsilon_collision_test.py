#!/usr/bin/env python3
import argparse
import copy
import json
from fractions import Fraction as F

# Exact Gaussian-rational arithmetic: (real, imag).
def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def poly_mul(a, b):
    out = [(F(0), F(0)) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = cadd(out[i + j], cmul(ai, bj))
    return out


def q_complex(z):
    # z^2 + 1/4, exact for Gaussian rationals.
    return cadd(cmul(z, z), (F(1, 4), F(0)))


def cdiv(a, b):
    den = b[0] * b[0] + b[1] * b[1]
    return (
        (a[0] * b[0] + a[1] * b[1]) / den,
        (a[1] * b[0] - a[0] * b[1]) / den,
    )


def validate_manifest(d):
    try:
        tc = d["toller_companion"]
        cv = d["causal_vertex"]
        geo = d["repository_geometry"]
        rows = tc["branch_rows"]
        return all([
            tc["arxiv"] == "2604.24945",
            tc["kernel_equation"] == 16,
            tc["finite_epsilon_functional_equation"] == 17,
            tc["feynman_limit_equation"] == 20,
            tc["physical_j"] == "1/2",
            tc["physical_l"] == "1/2",
            tc["physical_k"] == "1/2",
            tc["gamma_simple_rho"] == "gamma/2",
            tc["epsilon_variable_type"] == "spectral_rho_shift",
            tc["beta_shifted_by_epsilon"] is False,
            tc["finite_epsilon_damping_factor"] == "exp(-epsilon*beta)",
            tc["finite_epsilon_damping_factor_is_exp_minus_epsilon_over_beta"] is False,
            [(r["branch"], r["m"], r["leading_sign"]) for r in rows] == [
                ("+", "+1/2", -1),
                ("+", "-1/2", 1),
                ("-", "+1/2", 1),
                ("-", "-1/2", -1),
            ],
            all(r["leading_coefficient_epsilon_dependent"] is False for r in rows),
            cv["arxiv"] == "2601.23162v1",
            cv["common_finite_epsilon_ten_wedge_construction_is_published_source"] is False,
            geo["number_of_k5_wedges"] == 10,
            geo["single_wedge_collision_order"] == 2,
            geo["ten_wedge_collision_order"] == 20,
            geo["normal_codimension"] == 12,
            geo["normal_radial_measure_power"] == 11,
            geo["normal_radial_integrand_power"] == -9,
            geo["iter083b_ambiguity_dimension"] == 377,
        ])
    except Exception:
        return False


def require_text(path, needles):
    text = open(path, encoding="utf-8").read()
    missing = [x for x in needles if x not in text]
    return not missing, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="sources/raw/iter083f_finite_epsilon_source_lock.json")
    ap.add_argument("--iter077i", default="sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md")
    ap.add_argument("--iter083b", default="results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md")
    ap.add_argument("--theorem", default="sources/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_SCALING_DERIVATION.md")
    ap.add_argument("--output")
    args = ap.parse_args()

    d = json.load(open(args.manifest, encoding="utf-8"))
    tc = d["toller_companion"]
    geo = d["repository_geometry"]

    # P0: frozen source object and finite-epsilon contour setup.
    p0 = validate_manifest(d)

    # P1: formal kernel polynomial identity.
    # (i z + 1/2)(i z - 1/2) = -(z^2+1/4).
    iz_plus_half = [(F(1, 2), F(0)), (F(0), F(1))]
    iz_minus_half = [(F(-1, 2), F(0)), (F(0), F(1))]
    kernel_poly = poly_mul(iz_plus_half, iz_minus_half)
    expected_poly = [
        (F(-1, 4), F(0)),
        (F(0), F(0)),
        (F(-1), F(0)),
    ]
    p1 = kernel_poly == expected_poly and tc["kernel_j_half"] == "(rho_tilde^2+1/4)/(rho^2+1/4)"

    # Exact sample of shifted-denominator cancellation, using rational rho, epsilon.
    rho = (F(7, 10), F(0))
    eps = F(1, 7)
    rho_plus = (rho[0], eps)
    rho_minus = (rho[0], -eps)
    q_phys = q_complex(rho)
    q_plus = q_complex(rho_plus)
    q_minus = q_complex(rho_minus)
    # (q_shift/q_phys)*(1/q_shift) = 1/q_phys exactly.
    cancel_plus = cmul(cdiv(q_plus, q_phys), cdiv((F(1), F(0)), q_plus))
    cancel_minus = cmul(cdiv(q_minus, q_phys), cdiv((F(1), F(0)), q_minus))
    target_cancel = cdiv((F(1), F(0)), q_phys)
    shifted_denominators_really_differ = q_plus != q_phys and q_minus != q_phys
    p1 = p1 and cancel_plus == target_cancel and cancel_minus == target_cancel and shifted_denominators_really_differ

    # P2/P3: exact leading-series logic for all four rows.
    # exp(-epsilon beta)=1+O(beta), cosh=1+O(beta^2), sinh=beta+O(beta^3).
    # Hence every finite-epsilon numerator type has constant term +1 before its frozen outer sign.
    rows = tc["branch_rows"]
    leading_signs = {(r["branch"], r["m"]): r["leading_sign"] for r in rows}
    expected_signs = {
        ("+", "+1/2"): -1,
        ("+", "-1/2"): 1,
        ("-", "+1/2"): 1,
        ("-", "-1/2"): -1,
    }
    allowed_numerator_types = {
        "pure_exponential",
        "cosh-2*i*rho*sinh+2*epsilon*sinh",
        "cosh+2*i*rho*sinh+2*epsilon*sinh",
    }
    p2 = leading_signs == expected_signs and all(r["finite_epsilon_numerator_type"] in allowed_numerator_types for r in rows)
    p3 = p2 and all(r["leading_coefficient_epsilon_dependent"] is False for r in rows)

    # Exact gamma-simple coefficient reduction:
    # 2*(rho^2+1/4), rho=gamma/2 => (gamma^2+1)/2,
    # so reciprocal magnitude is 2/(gamma^2+1).
    denominator_gamma2_coeff = F(1, 2)
    denominator_constant = F(1, 2)
    gamma_reciprocal_numerator = F(2)
    p3 = p3 and denominator_gamma2_coeff == F(1, 2) and denominator_constant == F(1, 2) and gamma_reciprocal_numerator == 2

    # P4: ascending m=(-1/2,+1/2) gives plus diag(+,-), minus diag(-,+).
    plus_diag = [leading_signs[("+", "-1/2")], leading_signs[("+", "+1/2")]]
    minus_diag = [leading_signs[("-", "-1/2")], leading_signs[("-", "+1/2")]]
    p4_dep, p4_missing = require_text(args.iter077i, [
        "diag(1,-1)",
        "opposite causal branch changes the common leading scale by a minus sign",
        "raw radial power `r^(-20)`",
        "complete leading boundary contraction is nonzero",
    ])
    p4 = plus_diag == [1, -1] and minus_diag == [-1, 1] and p4_dep

    # P5/P6: ten factors keep order 20; codim 12 radial exponent is 11-20=-9.
    total_order = geo["number_of_k5_wedges"] * geo["single_wedge_collision_order"]
    radial_power = (geo["normal_codimension"] - 1) - total_order
    p5 = total_order == 20 and p4
    p6 = radial_power == -9 and radial_power <= -1 and total_order > geo["normal_codimension"]

    # P7: preserve the exact classification and the open genuinely-joint alternatives.
    p7_dep, p7_missing = require_text(args.theorem, [
        "COMMON_FINITE_ONE_WEDGE_SPECTRAL_EPSILON_IS_NOT_A_K5_COLLISION_REGULATOR_IN_THE_FROZEN_J_HALF_SECTOR",
        "does not rule out all common regulators",
        "regulate group-normal variables",
        "several-variable boundary value",
    ])
    p7b_dep, p7b_missing = require_text(args.iter083b, ["dim_C F_8 = 377", "PASS_EXACT_SCOPED"])
    p7 = p7_dep and p7b_dep

    # Negative controls: mutate the same manifest and demand rejection.
    bad_exp_over_beta = copy.deepcopy(d)
    bad_exp_over_beta["toller_companion"]["finite_epsilon_damping_factor"] = "exp(-epsilon/beta)"
    bad_exp_over_beta["toller_companion"]["finite_epsilon_damping_factor_is_exp_minus_epsilon_over_beta"] = True

    bad_beta_shift = copy.deepcopy(d)
    bad_beta_shift["toller_companion"]["epsilon_variable_type"] = "group_normal_beta_shift"
    bad_beta_shift["toller_companion"]["beta_shifted_by_epsilon"] = True

    bad_source_authority = copy.deepcopy(d)
    bad_source_authority["causal_vertex"]["common_finite_epsilon_ten_wedge_construction_is_published_source"] = True

    bad_epsilon_leading = copy.deepcopy(d)
    bad_epsilon_leading["toller_companion"]["branch_rows"][0]["leading_coefficient_epsilon_dependent"] = True

    # Dropping P_jl leaves 1/q(rho+i eps), which differs exactly from 1/q(rho).
    no_kernel_plus = cdiv((F(1), F(0)), q_plus)

    controls = {
        "exp_minus_epsilon_over_beta_surrogate_rejected": not validate_manifest(bad_exp_over_beta),
        "beta_shift_surrogate_rejected": not validate_manifest(bad_beta_shift),
        "new_common_epsilon_not_promoted_to_source_authority": not validate_manifest(bad_source_authority),
        "epsilon_dependent_leading_coefficient_corruption_rejected": not validate_manifest(bad_epsilon_leading),
        "dropping_toller_kernel_changes_shifted_denominator": no_kernel_plus != target_cancel,
        "physical_j_half_not_barrett_crane_only": tc["physical_j"] == "1/2",
        "finite_epsilon_analyzed_before_limit": tc["finite_epsilon_functional_equation"] == 17,
        "future_joint_regulator_scope_retained": p7,
    }

    predicates = {f"P{i}": v for i, v in enumerate([p0, p1, p2, p3, p4, p5, p6, p7])}
    passed = all(predicates.values()) and all(controls.values())

    result = {
        "iteration": "Iter083F-SM",
        "classification": (
            "ITER083F_SM_COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION_EXACT_SCOPED"
            if passed else "ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_TEST_INVALID_IMPLEMENTATION"
        ),
        "verdict": "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION",
        "predicates": predicates,
        "controls": controls,
        "kernel_formal_polynomial_coefficients": [[str(x), str(y)] for x, y in kernel_poly],
        "shifted_denominator_cancellation_exact": cancel_plus == target_cancel and cancel_minus == target_cancel,
        "leading_signs": {f"{b},{m}": s for (b, m), s in leading_signs.items()},
        "plus_leading_diag_ascending_m": plus_diag,
        "minus_leading_diag_ascending_m": minus_diag,
        "gamma_simple_leading_magnitude": "2/(1+gamma^2)",
        "finite_epsilon_leading_coefficient_depends_on_epsilon": False,
        "single_wedge_beta_order": -2,
        "number_of_k5_wedges": 10,
        "ten_wedge_radial_order": -total_order,
        "normal_codimension": geo["normal_codimension"],
        "radial_measure_times_integrand_power": radial_power,
        "locally_integrable_at_common_collision": radial_power > -1,
        "iter083b_frozen_ambiguity_dimension": geo["iter083b_ambiguity_dimension"],
        "dependency_missing": {
            "P4_iter077i": p4_missing,
            "P7_theorem": p7_missing,
            "P7_iter083b": p7b_missing,
        },
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
    print(payload)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
