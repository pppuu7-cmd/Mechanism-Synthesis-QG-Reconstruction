#!/usr/bin/env python3
"""Iter077G-SM: corrected j=1/2 source contact, microlocal collision, scaling threshold.

Frozen by prereg/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING.md.
Scientific FAIL is a valid result; only missing/invalid object provenance is BLOCKED.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from fractions import Fraction
from pathlib import Path

import sympy as sp

from distributional.iter077a_true_source_b_map_transversality import (
    AXES,
    EDGES,
    nullspace,
    rank_q,
    transpose,
    true_jacobian,
    witness_directions,
)

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
RANK9_COLORS = "xxxxxyyyzz"
LAM = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(1),
       Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]


def rank9_directions():
    return {e: AXES[RANK9_COLORS[i]] for i, e in enumerate(EDGES)}


def jt_vec(J, v):
    return [sum(J[r][c] * v[r] for r in range(len(J))) for c in range(len(J[0]))]


def provenance_lock():
    src = (ROOT / "sources" / "CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_EQ37_39_CORRECTED_SNAPSHOT.md").read_text(encoding="utf-8")
    err = (ROOT / "status" / "ITER077_CONTACT_FORMULA_ERRATUM.md").read_text(encoding="utf-8")
    ares = (ROOT / "results" / "ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md").read_text(encoding="utf-8")
    cres = (ROOT / "results" / "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md").read_text(encoding="utf-8")
    dres = (ROOT / "results" / "ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md").read_text(encoding="utf-8")
    checks = {
        "eq37_c_nplus1": "c_{n+1}" in src,
        "eq37_minus_i_power": "(-i)^(n+1)" in src,
        "jhalf_correct_local_form": "-(2 i rho/D) delta(x) - (1/D) delta'(x)" in src,
        "erratum_quarantines_old": "NON_AUTHORITATIVE_SOURCE_LOCK_INVALID" in err,
        "iter077a_authority": "ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED" in ares,
        "iter077c_authority": "ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED" in cres,
        "iter077d_authority": "ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED" in dres,
        "bf_scaling_input": "math-ph/9903028" in src,
        "epsilon_firewall": "spectral `i epsilon`" in src,
    }
    return checks


def lane_a():
    locks = provenance_lock()
    if not all(locks.values()):
        return {
            "iteration": "Iter077G-SM", "lane": "A", "valid": False,
            "scientific_outcome": "BLOCKED", "provenance_locks": locks,
            "classification": "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_BLOCKED_OBJECT_DEFINITION",
        }

    rho, gamma, q = sp.symbols("rho gamma q", real=True)
    D = rho**2 + sp.Rational(1, 4)
    F = sp.expand(((rho + q)**2 + sp.Rational(1, 4)) / D)
    c1 = sp.simplify(sp.diff(F, q).subs(q, 0))
    c2 = sp.simplify(sp.diff(F, q, 2).subs(q, 0))
    A_rho = sp.simplify(c1 * (-I))
    C_rho = sp.simplify((c2 / 2) * (-I)**2)
    A_gamma = sp.simplify(A_rho.subs(rho, gamma / 2))
    C_gamma = sp.simplify(C_rho.subs(rho, gamma / 2))

    expected_c1 = sp.simplify(2 * rho / D)
    expected_c2 = sp.simplify(2 / D)
    expected_A = sp.simplify(-4 * I * gamma / (1 + gamma**2))
    expected_C = sp.simplify(-4 / (1 + gamma**2))
    control_A = sp.simplify(A_gamma.subs(gamma, sp.Rational(6, 5)))
    control_C = sp.simplify(C_gamma.subs(gamma, sp.Rational(6, 5)))

    A_num, A_den = sp.fraction(sp.factor(A_gamma))
    C_num, C_den = sp.fraction(sp.factor(C_gamma))
    A_zeros = sp.solve(sp.Eq(A_num, 0), gamma)
    C_zeros = sp.solve(sp.Eq(C_num, 0), gamma)

    predictions = {
        "c1": sp.simplify(c1 - expected_c1) == 0,
        "c2": sp.simplify(c2 - expected_c2) == 0,
        "A_gamma": sp.simplify(A_gamma - expected_A) == 0,
        "C_gamma": sp.simplify(C_gamma - expected_C) == 0,
        "control_A": sp.simplify(control_A + sp.Rational(120, 61) * I) == 0,
        "control_C": sp.simplify(control_C + sp.Rational(100, 61)) == 0,
        "A_zero_set": A_zeros == [sp.Integer(0)],
        "C_no_finite_real_zero": C_zeros == [],
        "denominators_nonzero_polynomials": A_den != 0 and C_den != 0,
    }
    passed = bool(all(predictions.values()))
    return {
        "iteration": "Iter077G-SM", "lane": "A", "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "classification": "ITER077G_SM_CORRECTED_JHALF_CONTACT_COEFFICIENTS_EXACT_SCOPED" if passed else "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED",
        "provenance_locks": locks,
        "F_jhalf": str(F),
        "c1": str(c1), "c2": str(c2),
        "A_rho_delta_coefficient": str(A_rho),
        "C_rho_delta_prime_coefficient": str(C_rho),
        "A_gamma": str(A_gamma), "C_gamma": str(C_gamma),
        "gamma_6_over_5_A": str(control_A),
        "gamma_6_over_5_C": str(control_C),
        "A_finite_real_zero_set": [str(x) for x in A_zeros],
        "C_finite_real_zero_set": [str(x) for x in C_zeros],
        "frozen_prediction_checks": predictions,
    }


def corrected_fourier_objects():
    gamma, t = sp.symbols("gamma t", real=True)
    K = sp.simplify((-4 * I / (1 + gamma**2))**10)
    P = K
    for lam in LAM:
        P *= gamma + t * sp.Rational(lam.numerator, lam.denominator)
    P = sp.factor(P)
    expected = sp.factor(K * gamma**7 * (gamma + t)**2 * (gamma - t))
    return gamma, t, K, P, expected


def lane_b():
    J10 = true_jacobian(witness_directions())
    rank10 = rank_q(J10)
    left10 = nullspace(transpose(J10))

    J9 = true_jacobian(rank9_directions())
    rank9 = rank_q(J9)
    left9 = nullspace(transpose(J9))
    jtl = jt_vec(J9, LAM)

    gamma, t, K, P, expected = corrected_fourier_objects()
    restriction_ok = sp.simplify(P - expected) == 0
    ppoly = sp.Poly(sp.cancel(P / K), t)
    degree = int(ppoly.degree())
    leading = sp.factor(ppoly.LC() * K)
    expected_leading = sp.factor(-K * gamma**7)
    leading_ok = sp.simplify(leading - expected_leading) == 0
    nonzero_for_gamma_ne_0 = sp.factor(expected_leading) != 0 and gamma in expected_leading.free_symbols

    passed = bool(
        rank10 == 10 and len(left10) == 0
        and rank9 == 9 and len(left9) == 1
        and any(x != 0 for x in LAM) and all(x == 0 for x in jtl)
        and restriction_ok and degree == 3 and leading_ok and nonzero_for_gamma_ne_0
    )
    return {
        "iteration": "Iter077G-SM", "lane": "B", "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "classification": "ITER077G_SM_CORRECTED_CONTACT_GENERIC_SUBMERSION_ALLOWED_RANK9_SELFSTRESS_WAVEFRONT_COLLISION_EXACT_SCOPED" if passed else "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED",
        "generic_rank": rank10,
        "generic_left_nullity": len(left10),
        "rank9_rank": rank9,
        "rank9_left_nullity": len(left9),
        "lambda": [str(x) for x in LAM],
        "J9_transpose_lambda": [str(x) for x in jtl],
        "P10_on_t_lambda": str(P),
        "P10_expected": str(expected),
        "restriction_exact": bool(restriction_ok),
        "degree_in_t": degree,
        "leading_coefficient": str(leading),
        "leading_expected": str(expected_leading),
        "leading_exact": bool(leading_ok),
        "generic_submersion_pullback_authorized": rank10 == 10 and len(left10) == 0,
        "rank9_standard_Hormander_contact_criterion_fails": bool(rank9 == 9 and all(x == 0 for x in jtl) and degree == 3 and leading_ok),
        "full_source_selected_boundary_value_nonexistent": False,
    }


def lane_c():
    gamma, t, K, P, _ = corrected_fourier_objects()
    reduced = sp.factor(sp.cancel(P / K))
    poly = sp.Poly(reduced, t)
    degree = int(poly.degree())
    support = [i for i, x in enumerate(LAM) if x != 0]
    support_edges = [f"{EDGES[i][0]}{EDGES[i][1]}" for i in support]
    leading_full = sp.factor(poly.LC() * K)
    expected_leading = sp.factor(-K * gamma**7)
    leading_control = sp.simplify(leading_full.subs(gamma, sp.Rational(6, 5)))
    passed = bool(
        degree == 3 and len(support) == 3
        and support_edges == ["01", "02", "12"]
        and sp.simplify(leading_full - expected_leading) == 0
        and leading_control != 0
    )
    return {
        "iteration": "Iter077G-SM", "lane": "C", "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "classification": "ITER077G_SM_CORRECTED_CONTACT_SELFSTRESS_EXCESS_ORDER_N3_NONZERO_EXACT_SCOPED" if passed else "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED",
        "self_stress_support_edges": support_edges,
        "support_size": len(support),
        "Fourier_restriction_reduced": str(reduced),
        "degree_t": degree,
        "n_eff": degree,
        "leading_coefficient": str(leading_full),
        "expected_leading_coefficient": str(expected_leading),
        "gamma_6_over_5_leading_coefficient": str(leading_control),
        "full_smooth_spinor_intertwiner_contraction_tested": False,
    }


def lane_d():
    dres = (ROOT / "results" / "ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md").read_text(encoding="utf-8")
    second_jet_lock = (
        "determinant `-1`" in dres
        and "inertia `(3 positive, 3 negative)`" in dres
    )
    rows = []
    for n in range(4):
        sd = 2 * (n + 1)
        unique = sd < 6
        ambiguity_order = None if unique else sd - 6
        rows.append({
            "n": n,
            "scaling_degree": sd,
            "transverse_dimension": 6,
            "unique_extension_preserving_scaling_degree": unique,
            "max_local_delta_derivative_order": ambiguity_order,
        })
    ambiguity_dim_n3 = sum(math.comb(6 + k - 1, k) for k in range(3))
    predictions = bool(
        second_jet_lock
        and rows[0]["scaling_degree"] == 2 and rows[0]["unique_extension_preserving_scaling_degree"]
        and rows[1]["scaling_degree"] == 4 and rows[1]["unique_extension_preserving_scaling_degree"]
        and rows[2]["scaling_degree"] == 6 and not rows[2]["unique_extension_preserving_scaling_degree"] and rows[2]["max_local_delta_derivative_order"] == 0
        and rows[3]["scaling_degree"] == 8 and not rows[3]["unique_extension_preserving_scaling_degree"] and rows[3]["max_local_delta_derivative_order"] == 2
        and ambiguity_dim_n3 == 28
    )
    return {
        "iteration": "Iter077G-SM", "lane": "D", "valid": True,
        "scientific_outcome": "PASS" if predictions else "FAIL",
        "classification": "ITER077G_SM_SIX_DIMENSIONAL_QUADRATIC_CONTACT_SCALING_THRESHOLD_N2_MARGINAL_N3_SD8_EXACT_SCOPED" if predictions else "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED",
        "iter077d_mixed_second_jet_lock": bool(second_jet_lock),
        "scaling_table": rows,
        "n3_unconstrained_local_ambiguity_dimension_before_symmetry_or_source_selection": ambiguity_dim_n3,
        "unique_distributional_extension_is_absolute_integrability_claim": False,
        "source_selected_i_epsilon_extension_established": False,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter077G-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj

    all_present = set(got) == set(LANES)
    all_valid = all_present and all(bool(got[k].get("valid")) for k in LANES)
    if not all_valid:
        verdict = "BLOCKED"
        classification = "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_BLOCKED_OBJECT_DEFINITION"
        execution_valid = False
    else:
        outcomes = [got[k].get("scientific_outcome") for k in LANES]
        verdict = "PASS" if all(x == "PASS" for x in outcomes) else "FAIL"
        classification = (
            "ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED"
            if verdict == "PASS"
            else "ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED"
        )
        execution_valid = True

    return {
        "iteration": "Iter077G-SM",
        "execution_valid": execution_valid,
        "verdict": verdict,
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "lane_scientific_outcomes": {k: got.get(k, {}).get("scientific_outcome") for k in LANES},
        "corrected_jhalf_A_gamma": got.get("A", {}).get("A_gamma"),
        "corrected_jhalf_C_gamma": got.get("A", {}).get("C_gamma"),
        "generic_submersion_pullback_authorized": got.get("B", {}).get("generic_submersion_pullback_authorized"),
        "rank9_standard_Hormander_contact_criterion_fails": got.get("B", {}).get("rank9_standard_Hormander_contact_criterion_fails"),
        "rank9_n_eff": got.get("C", {}).get("n_eff"),
        "n3_scaling_degree": 8 if got.get("D", {}).get("scientific_outcome") == "PASS" else None,
        "n3_unconstrained_local_ambiguity_dimension": got.get("D", {}).get("n3_unconstrained_local_ambiguity_dimension_before_symmetry_or_source_selection"),
        "missing_object": "SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL" if verdict == "PASS" else None,
        "next_admissible_gate": "Derive the correlated rank-9 n_eff=3 extension from the published spectral i-epsilon prescription and then test it with the exact smooth Toller/spinor/intertwiner factors; arbitrary finite parts are forbidden.",
        "claim_lock": "No full source-vertex nonexistence/finiteness/divergence theorem, regulator-independence theorem, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete-QG, or G3/F9/G8/K5 promotion.",
    }


def main():
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
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))

    # Scientific FAIL is valid. Only object/provenance BLOCKED is infrastructure-invalid.
    if args.lane:
        if not obj.get("valid", False):
            raise SystemExit(1)
    else:
        if not obj.get("execution_valid", False):
            raise SystemExit(1)


if __name__ == "__main__":
    main()
