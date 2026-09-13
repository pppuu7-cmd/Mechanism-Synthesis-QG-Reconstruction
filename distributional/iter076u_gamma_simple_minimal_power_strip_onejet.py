#!/usr/bin/env python3
"""Iter076U: gamma-simple Toller minimal power-strip identity one-jet.

Frozen by prereg/ITER076U_GAMMA_SIMPLE_MINIMAL_POWER_STRIP_ONEJET.md.
Exact symbolic gate only; no boundary-intertwiner or source-to-K4 promotion.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
j, m, gamma = sp.symbols("j m gamma", real=True)


def params(sign: int):
    if sign == 1:
        E = j - I * gamma * j + m + 1
        a = j + m + 1
        b = j + 1 - I * gamma * j
        c = 1 + m - I * gamma * j
    elif sign == -1:
        E = j + I * gamma * j - m + 1
        a = j - m + 1
        b = j + 1 + I * gamma * j
        c = 1 - m + I * gamma * j
    else:
        raise ValueError("sign must be +/-1")
    return E, a, b, c


def exact_zero(expr) -> bool:
    return sp.simplify(sp.expand(expr)) == 0


def recurrence_r(sign: int):
    _, a, b, c = params(sign)
    n = 2 * j + 1
    return sp.factor(sp.simplify((n * c - a * b) / (n - 1)))


def expected_r(sign: int):
    if sign == 1:
        return -(1 + I * gamma) * (j - m) / 2
    return -(1 - I * gamma) * (j + m) / 2


def minimal_onejet(sign: int):
    E, _, _, _ = params(sign)
    n = 2 * j + 1
    return sp.factor(sp.simplify(n - E + 2 * recurrence_r(sign)))


def lane_a():
    text = (ROOT / "sources" / "GAMMA_SIMPLE_TOLLER_IDENTITY_ASYMPTOTIC_SUPPLEMENT.md").read_text(encoding="utf-8")
    locks = {
        "eq9_branch_form": "t_±(beta) = exp[-E_± beta] P_± * 2F1(a_±,b_±;c_±; exp(-2 beta))" in text,
        "E_plus": "E_+ = j - i gamma j + m + 1" in text,
        "E_minus": "E_- = j + i gamma j - m + 1" in text,
        "a_plus": "a_+ = j + m + 1" in text,
        "a_minus": "a_- = j - m + 1" in text,
        "scope_j_positive": "`j` is a positive half-integer" in text,
        "scope_gamma_nonzero": "real `gamma != 0`" in text,
        "physical_factorization_firewall": "not asserted to be the unique physical singular/contact factorization" in text,
        "kak_tangent_firewall": "KAK coordinates are singular at the identity" in text,
    }
    valid = all(locks.values())
    return {
        "iteration": "Iter076U",
        "lane": "A",
        "valid": bool(valid),
        "source_locks": locks,
    }


def lane_b():
    n = 2 * j + 1
    rows = {}
    all_ok = True
    for sign in (1, -1):
        _, a, b, c = params(sign)
        gap = sp.factor(sp.simplify(c - a - b))
        r = recurrence_r(sign)
        rex = expected_r(sign)
        recurrence_residual = sp.factor(sp.simplify(-(n - 1) * r + (n * c - a * b)))
        ok = exact_zero(gap + n) and exact_zero(r - rex) and exact_zero(recurrence_residual)
        all_ok &= ok
        rows[str(sign)] = {
            "c_minus_a_minus_b": str(gap),
            "n": str(n),
            "recurrence_r": str(r),
            "expected_r": str(sp.factor(rex)),
            "recurrence_residual": str(recurrence_residual),
            "valid": bool(ok),
        }
    return {
        "iteration": "Iter076U",
        "lane": "B",
        "valid": bool(all_ok),
        "branches": rows,
        "frozen_scope_min_j": "1/2",
        "frozen_scope_min_n": 2,
        "first_recurrence_nonresonant_in_scope": True,
        "later_log_terms_excluded_from_claim": True,
    }


def lane_c():
    gp = minimal_onejet(1)
    gm = minimal_onejet(-1)
    target = I * gamma * m
    plus_ok = exact_zero(gp - target)
    minus_ok = exact_zero(gm - target)
    branch_equal = exact_zero(gp - gm)
    valid = plus_ok and minus_ok and branch_equal
    return {
        "iteration": "Iter076U",
        "lane": "C",
        "valid": bool(valid),
        "Gplus_onejet": str(gp),
        "Gminus_onejet": str(gm),
        "target": str(target),
        "both_branches_equal": bool(branch_equal),
        "m_zero_onejet_zero": bool(sp.simplify(target.subs(m, 0)) == 0),
        "m_nonzero_gamma_nonzero_generically_nonzero": True,
        "physical_full_numerator_promoted": False,
    }


def wigner_identity_derivative():
    E = j - I * gamma * j + m + 1
    a = j + m + 1
    b = j + 1 - I * gamma * j
    c = 2 * j + 2
    # z=1-exp(-2 beta) has z'(0)=2 and 2F1(a,b;c;z)=1+(ab/c)z+...
    return sp.factor(sp.simplify(-E + 2 * a * b / c))


def lane_d():
    rows = []
    all_formula_ok = True
    zero_cases = 0
    nonzero_cases = 0
    branch_checks = 0
    for j2 in range(1, 7):
        jv = sp.Rational(j2, 2)
        for m2 in range(-j2, j2 + 1, 2):
            mv = sp.Rational(m2, 2)
            target = I * gamma * mv
            vals = []
            for sign in (1, -1):
                val = sp.simplify(minimal_onejet(sign).subs({j: jv, m: mv}))
                ok = exact_zero(val - target)
                all_formula_ok &= ok
                branch_checks += 1
                vals.append(str(val))
            is_zero = mv == 0
            if is_zero:
                zero_cases += 1
                all_formula_ok &= sp.simplify(target) == 0
            else:
                nonzero_cases += 1
                all_formula_ok &= sp.simplify(target / (I * gamma * mv)) == 1
            rows.append({
                "j": str(jv),
                "m": str(mv),
                "branch_values": vals,
                "expected_zero": bool(is_zero),
            })

    wd = wigner_identity_derivative()
    wd_target = -I * gamma * j * m / (j + 1)
    wigner_ok = exact_zero(wd - wd_target)
    distinction = sp.factor(sp.simplify(I * gamma * m - wd))

    locks = {
        "unique_physical_Toller_factorization_established": False,
        "full_boundary_intertwiner_onejet_established": False,
        "arbitrary_group_tangent_onejet_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }

    valid = bool(
        all_formula_ok
        and len(rows) == 27
        and zero_cases == 3
        and nonzero_cases == 24
        and branch_checks == 54
        and wigner_ok
        and distinction != 0
        and not any(locks.values())
    )
    return {
        "iteration": "Iter076U",
        "lane": "D",
        "valid": valid,
        "admissible_pairs_checked": len(rows),
        "branch_formula_checks": branch_checks,
        "m_zero_pairs": zero_cases,
        "m_nonzero_pairs": nonzero_cases,
        "wigner_identity_derivative": str(wd),
        "wigner_target": str(sp.factor(wd_target)),
        "wigner_control_exact": bool(wigner_ok),
        "toller_minus_wigner_onejet_difference": str(distinction),
        "scope_locks": locks,
        "rows": rows,
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
            if obj.get("iteration") == "Iter076U" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076U_GAMMA_SIMPLE_TOLLER_MINIMAL_POWER_STRIP_ONEJET_EQUALS_I_GAMMA_M_BOTH_BRANCHES_EXACT_SCOPED"
        if valid
        else "ITER076U_GAMMA_SIMPLE_MINIMAL_POWER_STRIP_ONEJET_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076U",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "For the source Eq.(9) gamma-simple reduced Toller branch and j>0, minimal leading-power stripping "
            "produces a finite right one-jet i*gamma*m for both causal branches. This is wedge-level only and "
            "does not establish the full boundary/intertwiner or arbitrary-tangent source one-jet."
        ),
        "next_admissible_gate": (
            "Audit whether the i*gamma*m wedge-level coefficient is annihilated or survives under exact SU(2) "
            "boundary-intertwiner contraction and gauge-fixed node-wise relative-group tangent insertions."
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
