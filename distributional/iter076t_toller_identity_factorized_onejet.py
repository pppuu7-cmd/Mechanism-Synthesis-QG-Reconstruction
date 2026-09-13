#!/usr/bin/env python3
"""Iter076T: exact Toller identity singularity and factorized branch one-jet gate.

Frozen by prereg/ITER076T_TOLLER_IDENTITY_FACTORIZED_ONEJET.md.
This gate distinguishes the singular individual Toller branch from a regular
pole-stripped Barrett-Crane control. It does not define the physical EPRL
boundary-contracted numerator one-jet.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
beta = sp.symbols("beta", positive=True, real=True)
rho = sp.symbols("rho", nonzero=True, real=True)


def tplus_expr():
    return sp.exp(I * rho * beta) / (2 * I * rho * sp.sinh(beta))


def tminus_expr():
    return -sp.exp(-I * rho * beta) / (2 * I * rho * sp.sinh(beta))


def d_expr():
    return sp.sin(rho * beta) / (rho * sp.sinh(beta))


def exact_zero(expr) -> bool:
    return sp.simplify(sp.trigsimp(expr)) == 0


def lane_a():
    supplement = (ROOT / "sources" / "TOLLER_IDENTITY_FACTORIZATION_SOURCE_SUPPLEMENT.md").read_text(encoding="utf-8")
    jhalf = (ROOT / "distributional" / "jhalf_iepsilon_validation.py").read_text(encoding="utf-8")

    locks = {
        "additive_relation": "T^(+) + T^(-) = D" in supplement,
        "second_kind": "functions of the second kind" in supplement,
        "frequency_character": "positive- and negative-frequency components" in supplement,
        "bc_tplus": "t^(+)(beta) = +(1/(2 i rho)) exp(+i rho beta)/sinh(beta)" in supplement,
        "bc_tminus": "t^(-)(beta) = -(1/(2 i rho)) exp(-i rho beta)/sinh(beta)" in supplement,
        "bc_wigner": "d(beta) = sin(rho beta)/(rho sinh(beta))" in supplement,
        "scope_physical_onejet_not_defined": "does **not** define the physical EPRL/Toller wedge numerator one-jet" in supplement,
        "jhalf_c1": "c1 = 2 rho/(rho^2+1/4)" in jhalf,
        "jhalf_c2": "c2 = 2/(rho^2+1/4)" in jhalf,
        "jhalf_contact": "delta^(rho,1/2) = -i c1 delta - (c2/2) delta'" in jhalf,
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter076T",
        "lane": "A",
        "valid": bool(valid),
        "source_locks": locks,
        "physical_EPRL_Toller_intertwiner_onejet_established": False,
    }


def lane_b():
    tp = tplus_expr()
    tm = tminus_expr()
    d = d_expr()

    rp = sp.simplify(sp.limit(beta * tp, beta, 0, dir="+"))
    rm = sp.simplify(sp.limit(beta * tm, beta, 0, dir="+"))
    expected_rp = 1 / (2 * I * rho)
    expected_rm = -1 / (2 * I * rho)

    additive = exact_zero(tp + tm - d)
    d0 = sp.simplify(sp.limit(d, beta, 0, dir="+"))
    d1 = sp.simplify(sp.limit(sp.diff(d, beta), beta, 0, dir="+"))
    series_d = sp.series(d, beta, 0, 4)
    expected_trunc = 1 - (rho**2 + 1) * beta**2 / 6
    series_ok = exact_zero(series_d.removeO() - expected_trunc)

    valid = bool(
        exact_zero(rp - expected_rp)
        and exact_zero(rm - expected_rm)
        and rp != 0
        and rm != 0
        and additive
        and d0 == 1
        and d1 == 0
        and series_ok
    )
    return {
        "iteration": "Iter076T",
        "lane": "B",
        "valid": valid,
        "beta_tplus_limit": str(rp),
        "beta_tminus_limit": str(rm),
        "individual_branches_regular_taylor_germs_at_identity": False,
        "additive_identity_exact": bool(additive),
        "wigner_sum_identity_value": str(d0),
        "wigner_sum_identity_first_derivative": str(d1),
        "wigner_sum_series": str(series_d),
        "wigner_even_through_linear_order": bool(d1 == 0),
    }


def lane_c():
    tp = tplus_expr()
    tm = tminus_expr()
    np = sp.simplify((2 * I * rho * beta) * tp)
    nm = sp.simplify((-2 * I * rho * beta) * tm)

    np0 = sp.simplify(sp.limit(np, beta, 0, dir="+"))
    nm0 = sp.simplify(sp.limit(nm, beta, 0, dir="+"))
    np1 = sp.simplify(sp.limit(sp.diff(np, beta), beta, 0, dir="+"))
    nm1 = sp.simplify(sp.limit(sp.diff(nm, beta), beta, 0, dir="+"))
    np2 = sp.simplify(sp.limit(sp.diff(np, beta, 2), beta, 0, dir="+") / 2)
    nm2 = sp.simplify(sp.limit(sp.diff(nm, beta, 2), beta, 0, dir="+") / 2)
    expected_q = -(rho**2 / 2 + sp.Rational(1, 6))

    sp_np = sp.series(np, beta, 0, 3)
    sp_nm = sp.series(nm, beta, 0, 3)

    valid = bool(
        np0 == 1
        and nm0 == 1
        and exact_zero(np1 - I * rho)
        and exact_zero(nm1 + I * rho)
        and exact_zero(np2 - expected_q)
        and exact_zero(nm2 - expected_q)
        and np1 != 0
        and nm1 != 0
    )
    return {
        "iteration": "Iter076T",
        "lane": "C",
        "valid": valid,
        "Nplus": str(np),
        "Nminus": str(nm),
        "Nplus_at_zero": str(np0),
        "Nminus_at_zero": str(nm0),
        "Nplus_onejet": str(np1),
        "Nminus_onejet": str(nm1),
        "shared_quadratic_coefficient": str(np2),
        "Nplus_series": str(sp_np),
        "Nminus_series": str(sp_nm),
        "generic_nonzero_regular_branch_onejet": True,
        "unique_physical_EPRL_factorization_claimed": False,
    }


def lane_d():
    q = sp.symbols("q", real=True)
    r = sp.symbols("r", real=True)
    c1 = 2 * r / (r**2 + sp.Rational(1, 4))
    c2 = 2 / (r**2 + sp.Rational(1, 4))

    identities = []
    for sigma in (-1, 1):
        x = I * r
        prod = ((x + I * sigma * q + sp.Rational(1, 2)) * (x + I * sigma * q - sp.Rational(1, 2))) / (
            (x + sp.Rational(1, 2)) * (x - sp.Rational(1, 2))
        )
        expanded = 1 + c1 * sigma * q + (c2 / 2) * (sigma * q) ** 2
        identities.append(exact_zero(prod - expanded))

    roots = sp.solve(sp.Eq(sp.together(c1).as_numer_denom()[0], 0), r)
    c1_only_zero_at_r0 = roots == [0]

    locks = {
        "spectral_contact_not_group_coordinate_onejet": True,
        "naive_branch_derivative_at_identity_is_valid_onejet": False,
        "universal_individual_branch_evenness_established": False,
        "physical_EPRL_Toller_intertwiner_onejet_established": False,
        "physical_nonlinear_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }

    valid = bool(
        all(identities)
        and c1_only_zero_at_r0
        and locks["spectral_contact_not_group_coordinate_onejet"]
        and not locks["naive_branch_derivative_at_identity_is_valid_onejet"]
        and not locks["universal_individual_branch_evenness_established"]
        and not locks["physical_EPRL_Toller_intertwiner_onejet_established"]
        and not locks["physical_nonlinear_source_to_K4_curvature_selected"]
        and not locks["epsilon_minus1_coefficient_established"]
        and not locks["generic_finite_spin_signed_P3_promoted"]
        and not locks["G3_promoted"]
        and not locks["F9_promoted"]
        and not locks["G8_promoted"]
        and not locks["K5_promoted"]
    )
    return {
        "iteration": "Iter076T",
        "lane": "D",
        "valid": valid,
        "appendix_d_polynomial_identity_both_signs": bool(all(identities)),
        "c1": str(c1),
        "c1_real_zeros": [str(x) for x in roots],
        "c1_generically_nonzero": bool(c1_only_zero_at_r0),
        "scope_locks": locks,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


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
            lane = obj.get("lane")
            if obj.get("iteration") == "Iter076T" and lane in LANES:
                got[lane] = obj

    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076T_NAIVE_TOLLER_IDENTITY_ONEJET_SINGULAR_POLE_STRIPPED_BC_BRANCH_HAS_GENERIC_NONZERO_ONEJET_EXACT_SCOPED"
        if valid
        else "ITER076T_TOLLER_IDENTITY_FACTORIZED_ONEJET_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076T",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "Individual Toller branches need not define smooth identity Taylor germs. In the exact Barrett-Crane control, "
            "a pole-stripped regular branch factor has a generic nonzero one-jet. This does not define the physical "
            "gamma-simple EPRL/intertwiner numerator one-jet."
        ),
        "next_admissible_gate": (
            "Derive the identity singular order and a source-defined regular factor for the gamma-simple EPRL reduced "
            "Toller branch of Eq.(9), then test its finite one-jet before boundary-intertwiner contraction."
        ),
        "claim_lock": (
            "No new physics, complete-QG claim, physical full numerator one-jet, physical nonlinear source-to-K4 map, "
            "epsilon^-1 coefficient, causal-vertex finiteness/divergence theorem, generic finite-spin signed P3, or "
            "G3/F9/G8/K5 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
