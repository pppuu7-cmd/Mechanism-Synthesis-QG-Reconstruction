#!/usr/bin/env python3
"""Iter076T exact Toller/Haar regularized wedge one-jet audit.

Prospectively frozen in prereg/ITER076T_TOLLER_HAAR_REGULARIZED_WEDGE_ONEJET.md.
This establishes only a local/source wedge witness, never the fully contracted
or integrated causal-vertex one-jet.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)


def write(obj, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_oracle():
    path = ROOT / "code" / "toller_general_eprl_reference.py"
    spec = importlib.util.spec_from_file_location("toller_oracle", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def lane_a():
    beta, rho = sp.symbols("beta rho", real=True)
    I = sp.I
    # Source Eq.(9), j=1/2 extremal branch: Gamma recurrence and
    # 2F1(2,b;b,z)=(1-z)^-2 have already reduced the factors to these
    # exact rational/exponential pieces; we recombine them symbolically.
    gamma_plus = sp.simplify(sp.Integer(2) / ((I * rho - sp.Rational(1, 2)) * (I * rho + sp.Rational(1, 2))))
    gamma_minus = sp.simplify(sp.Integer(2) / ((-I * rho - sp.Rational(1, 2)) * (-I * rho + sp.Rational(1, 2))))
    z = sp.exp(-2 * beta)
    hyper = 1 / (1 - z) ** 2
    tplus_reconstructed = sp.simplify(sp.exp(-(2 - I * rho) * beta) * gamma_plus * hyper)
    tminus_reconstructed = sp.simplify(sp.exp(-(2 + I * rho) * beta) * gamma_minus * hyper)
    tplus_target = -sp.exp(I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)
    tminus_target = -sp.exp(-I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)
    plus_res = sp.simplify(sp.trigsimp(tplus_reconstructed - tplus_target))
    minus_res = sp.simplify(sp.trigsimp(tminus_reconstructed - tminus_target))

    uplus = sp.simplify(sp.sinh(beta) ** 2 * tplus_target)
    uminus = sp.simplify(sp.sinh(beta) ** 2 * tminus_target)
    duplus = sp.simplify(sp.diff(uplus, beta).subs(beta, 0))
    duminus = sp.simplify(sp.diff(uminus, beta).subs(beta, 0))
    expected_plus = -I * rho / (2 * (rho**2 + sp.Rational(1, 4)))
    expected_minus = I * rho / (2 * (rho**2 + sp.Rational(1, 4)))
    valid = (
        plus_res == 0
        and minus_res == 0
        and sp.simplify(duplus - expected_plus) == 0
        and sp.simplify(duminus - expected_minus) == 0
    )
    return {
        "iteration": "Iter076T",
        "lane": "A",
        "valid": bool(valid),
        "gamma_ratio_plus": str(gamma_plus),
        "gamma_ratio_minus": str(gamma_minus),
        "closed_form_plus": str(tplus_target),
        "closed_form_minus": str(tminus_target),
        "uplus_prime_zero": str(duplus),
        "uminus_prime_zero": str(duminus),
        "onejet_nonzero_condition": "rho != 0",
    }


def cform(branch, rho, beta):
    den = 2 * (rho * rho + mp.mpf("0.25")) * mp.sinh(beta) ** 2
    return -mp.e ** ((mp.j if branch > 0 else -mp.j) * rho * beta) / den


def relerr(a, b):
    return abs(a - b) / max(abs(b), mp.mpf("1e-70"))


def lane_b():
    oracle = load_oracle()
    mp.mp.dps = 80
    rows = []
    worst = mp.mpf(0)
    derivative_checks = []
    for gamma_s in ("0.4", "1.2"):
        gamma = mp.mpf(gamma_s)
        rho = gamma / 2
        for beta_s in ("0.3", "0.8", "1.7"):
            beta = mp.mpf(beta_s)
            tp = oracle.tplus(mp.mpf("0.5"), mp.mpf("0.5"), mp.mpf("0.5"), mp.mpf("0.5"), rho, beta)
            tm = oracle.tminus(mp.mpf("0.5"), mp.mpf("0.5"), mp.mpf("-0.5"), mp.mpf("0.5"), rho, beta)
            ep = cform(+1, rho, beta)
            em = cform(-1, rho, beta)
            rp = relerr(tp, ep)
            rm = relerr(tm, em)
            worst = max(worst, rp, rm)
            rows.append({
                "gamma": gamma_s,
                "beta": beta_s,
                "plus_relative_residual": mp.nstr(rp, 12),
                "minus_relative_residual": mp.nstr(rm, 12),
            })
        c0 = -1 / (2 * (rho * rho + mp.mpf("0.25")))
        dup = mp.j * rho * c0
        dum = -mp.j * rho * c0
        derivative_checks.append({
            "gamma": gamma_s,
            "rho": mp.nstr(rho, 20),
            "uplus_prime": [mp.nstr(mp.re(dup), 20), mp.nstr(mp.im(dup), 20)],
            "uminus_prime": [mp.nstr(mp.re(dum), 20), mp.nstr(mp.im(dum), 20)],
            "both_nonzero": bool(abs(dup) > 0 and abs(dum) > 0),
        })
    valid = worst < mp.mpf("1e-35") and all(x["both_nonzero"] for x in derivative_checks)
    return {
        "iteration": "Iter076T",
        "lane": "B",
        "valid": bool(valid),
        "oracle": "code/toller_general_eprl_reference.py",
        "cases": len(rows) * 2,
        "worst_relative_residual": mp.nstr(worst, 20),
        "threshold": "1e-35",
        "rows": rows,
        "derivative_checks": derivative_checks,
    }


def lane_c():
    beta, rho = sp.symbols("beta rho", real=True)
    haar_norm = (sp.sinh(beta) / beta) ** 2
    haar_series = sp.series(haar_norm, beta, 0, 6).removeO().expand()
    haar_onejet = sp.limit(sp.diff(haar_norm, beta), beta, 0)
    tp = -sp.exp(sp.I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)
    tm = -sp.exp(-sp.I * rho * beta) / (2 * (rho**2 + sp.Rational(1, 4)) * sp.sinh(beta) ** 2)
    raw_plus = sp.simplify(sp.sinh(beta) ** 2 * tp)
    raw_minus = sp.simplify(sp.sinh(beta) ** 2 * tm)
    dp = sp.simplify(sp.diff(raw_plus, beta).subs(beta, 0))
    dm = sp.simplify(sp.diff(raw_minus, beta).subs(beta, 0))
    expected_series = 1 + beta**2 / 3 + 2 * beta**4 / 45
    valid = (
        sp.simplify(haar_series - expected_series) == 0
        and haar_onejet == 0
        and sp.simplify(dp + sp.I * rho / (2 * (rho**2 + sp.Rational(1, 4)))) == 0
        and sp.simplify(dm - sp.I * rho / (2 * (rho**2 + sp.Rational(1, 4)))) == 0
    )
    return {
        "iteration": "Iter076T",
        "lane": "C",
        "valid": bool(valid),
        "normalized_haar_series": str(haar_series),
        "normalized_haar_onejet": str(haar_onejet),
        "haar_times_plus_regular_factor": str(raw_plus),
        "haar_times_minus_regular_factor": str(raw_minus),
        "plus_surviving_onejet": str(dp),
        "minus_surviving_onejet": str(dm),
        "interpretation": "The even Haar radial density cancels the extremal collision pole but does not erase the Toller boost phase one-jet for rho!=0.",
    }


def lane_d():
    snapshot = (ROOT / "sources/CAUSAL_VERTEX_TOLLER_ONEJET_SOURCE_SNAPSHOT.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg/ITER076T_TOLLER_HAAR_REGULARIZED_WEDGE_ONEJET.md").read_text(encoding="utf-8")
    rres = (ROOT / "results/ITER076R_QUADRATIC_CURVATURE_ONEJET_FACE_CONTAMINATION_RESULT.md").read_text(encoding="utf-8")
    evidence = {
        "source_full_vertex_scope_guard": "fully contracted/integrated causal vertex" in snapshot,
        "source_contact_vs_bulk_split": "theta(sigma B) + sigma delta^(rho,j)(B)" in snapshot,
        "curvature_contamination_prior": "one-jet cannot be bypassed by symmetry" in rres,
        "full_vertex_nonzero_not_claimed": "does not prove that the fully contracted or integrated vertex one-jet is nonzero" in prereg,
        "epsilon_minus1_not_emitted": "no nominal `epsilon^-1` coefficient" in prereg,
    }
    locks = {
        "full_contracted_vertex_onejet_established_nonzero": False,
        "full_contracted_vertex_onejet_established_zero": False,
        "physical_nonlinear_pushforward_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_p3_promoted": False,
        "physical_finiteness_or_divergence_theorem": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = all(evidence.values()) and not any(locks.values())
    return {
        "iteration": "Iter076T",
        "lane": "D",
        "valid": bool(valid),
        "evidence": evidence,
        "scope_locks": locks,
        "next_missing_object": "FULL_TOLLER_INTERTWINER_CONTRACTED_NUMERATOR_ONEJET",
        "interpretation": "A nonzero local magnetic-component Toller/Haar one-jet witness defeats universal local-zero claims but does not decide cancellations in the full contracted/integrated vertex.",
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
            if obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    all_valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076T_EXACT_TOLLER_HAAR_REGULARIZED_WEDGE_HAS_NONZERO_ONEJET_WITNESS_FULL_VERTEX_CONTRACTED_ONEJET_STILL_REQUIRED_SCOPED"
        if all_valid
        else "ITER076T_TOLLER_HAAR_ONEJET_SOURCE_SPECIALIZATION_FAIL"
    )
    return {
        "iteration": "Iter076T",
        "valid": bool(all_valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "local_source_onejet_witness_nonzero": bool(all_valid),
        "full_toller_intertwiner_contracted_onejet_established": False,
        "physical_nonlinear_pushforward_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "next_admissible_gate": "Audit magnetic/intertwiner contraction of the source numerator one-jet before any physical degree-two or epsilon^-1 coefficient is formed.",
        "claim_lock": "No complete-QG/new-physics/generic-finite-spin-P3/finiteness-divergence/G3/F9/G8/K5 promotion.",
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
