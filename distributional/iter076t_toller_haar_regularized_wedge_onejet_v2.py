#!/usr/bin/env python3
"""Authoritative symbolic-normalization repair for Iter076T.

Only Lane A implementation changes: instead of asking SymPy to discover
1-exp(-2 beta)=2 exp(-beta)sinh(beta), the frozen source identity is applied
explicitly before exact comparison. No scientific prediction or threshold is changed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter076t_toller_haar_regularized_wedge_onejet as base


def lane_a_fixed():
    beta, rho = sp.symbols("beta rho", real=True)
    I = sp.I
    gamma_plus = sp.simplify(sp.Integer(2) / ((I * rho - sp.Rational(1, 2)) * (I * rho + sp.Rational(1, 2))))
    gamma_minus = sp.simplify(sp.Integer(2) / ((-I * rho - sp.Rational(1, 2)) * (-I * rho + sp.Rational(1, 2))))

    # Apply the frozen source/hypergeometric identities explicitly.
    # 2F1(2,b;b,z)=(1-z)^-2 and
    # 1-exp(-2 beta)=2 exp(-beta)sinh(beta).
    hyper_reduced = sp.exp(2 * beta) / (4 * sp.sinh(beta) ** 2)
    tplus_reconstructed = sp.factor(sp.exp(-(2 - I * rho) * beta) * gamma_plus * hyper_reduced)
    tminus_reconstructed = sp.factor(sp.exp(-(2 + I * rho) * beta) * gamma_minus * hyper_reduced)
    tplus_target = -sp.exp(I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)
    tminus_target = -sp.exp(-I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)

    plus_ratio = sp.simplify(tplus_reconstructed / tplus_target)
    minus_ratio = sp.simplify(tminus_reconstructed / tminus_target)
    uplus = sp.simplify(sp.sinh(beta) ** 2 * tplus_target)
    uminus = sp.simplify(sp.sinh(beta) ** 2 * tminus_target)
    duplus = sp.simplify(sp.diff(uplus, beta).subs(beta, 0))
    duminus = sp.simplify(sp.diff(uminus, beta).subs(beta, 0))
    expected_plus = -I * rho / (2 * (rho**2 + sp.Rational(1, 4)))
    expected_minus = I * rho / (2 * (rho**2 + sp.Rational(1, 4)))
    valid = (
        plus_ratio == 1
        and minus_ratio == 1
        and sp.simplify(duplus - expected_plus) == 0
        and sp.simplify(duminus - expected_minus) == 0
    )
    return {
        "iteration": "Iter076T",
        "lane": "A",
        "valid": bool(valid),
        "repair_scope": "symbolic normalization only",
        "gamma_ratio_plus": str(gamma_plus),
        "gamma_ratio_minus": str(gamma_minus),
        "explicit_hypergeometric_reduction": str(hyper_reduced),
        "closed_form_plus": str(tplus_target),
        "closed_form_minus": str(tminus_target),
        "reconstructed_over_target_plus": str(plus_ratio),
        "reconstructed_over_target_minus": str(minus_ratio),
        "uplus_prime_zero": str(duplus),
        "uminus_prime_zero": str(duminus),
        "onejet_nonzero_condition": "rho != 0",
    }


LANES = {"A": lane_a_fixed, "B": base.lane_b, "C": base.lane_c, "D": base.lane_d}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else base.aggregate(args.aggregate_dir)
    base.write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
