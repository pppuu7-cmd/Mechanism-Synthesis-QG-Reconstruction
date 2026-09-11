#!/usr/bin/env python3
"""Robust phase-convention audit between upstream sl2cfoam dsmall and Ruhl d.

This is intentionally separate from the main research matrix so convention work
can be rerun without repeating unrelated physics streams.
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from toller_general_eprl_reference import d_ruhl  # noqa: E402

mp.mp.dps = 80


def phase_phi(rho, j, l):
    a = mp.gamma(j + 1 + 1j * rho)
    b = mp.gamma(l + 1 - 1j * rho)
    return mp.e ** (-1j * mp.pi * (j - l) / 2) * (a / abs(a)) * (b / abs(b))


def rel(a, b):
    return float(abs(a - b) / max(abs(b), mp.mpf("1e-60")))


def cp(z):
    return [float(mp.re(z)), float(mp.im(z))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", default="results/sl2cfoam_dsmall_probe.tsv")
    ap.add_argument("--output", default="results/sl2cfoam_phase_convention_audit.json")
    args = ap.parse_args()

    rows = []
    with open(args.probe, newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            tj, tl, tm = int(r["two_j"]), int(r["two_l"]), int(r["two_m"])
            j, l, m = mp.mpf(tj) / 2, mp.mpf(tl) / 2, mp.mpf(tm) / 2
            g, beta = mp.mpf(r["gamma"]), mp.mpf(r["beta"])
            rho = g * j
            ds = mp.mpc(mp.mpf(r["re"]), mp.mpf(r["im"]))
            dr = d_ruhl(j, l, m, j, rho, beta)
            ph = phase_phi(rho, j, l)
            ratio = ds / dr if abs(dr) > mp.mpf("1e-70") else mp.mpc("nan")
            candidates = {
                "ruhl_identity": dr,
                "phi_times_ruhl": ph * dr,
                "conj_phi_times_ruhl": mp.conj(ph) * dr,
                "minus_phi_times_ruhl": -ph * dr,
                "minus_conj_phi_times_ruhl": -mp.conj(ph) * dr,
                "i_phi_times_ruhl": 1j * ph * dr,
                "minus_i_phi_times_ruhl": -1j * ph * dr,
            }
            errs = {k: rel(v, ds) for k, v in candidates.items()}
            rows.append({
                "two_j": tj, "two_l": tl, "two_m": tm,
                "gamma": float(g), "beta": float(beta),
                "sl2cfoam": cp(ds), "ruhl": cp(dr), "phi": cp(ph),
                "ratio_sl2c_over_ruhl": cp(ratio),
                "ratio_modulus_error_from_one": float(abs(abs(ratio) - 1)),
                "ratio_phase": float(mp.arg(ratio)),
                "errors": errs,
            })

    names = list(rows[0]["errors"])
    scores = {}
    for n in names:
        vals = [r["errors"][n] for r in rows]
        scores[n] = {"max": max(vals), "median": statistics.median(vals)}

    winner = min(names, key=lambda n: scores[n]["max"])
    max_modulus_error = max(r["ratio_modulus_error_from_one"] for r in rows)
    max_abs_ratio_phase = max(abs(r["ratio_phase"]) for r in rows)
    passed = scores[winner]["max"] < 1e-8
    identity_passed = winner == "ruhl_identity" and scores[winner]["max"] < 1e-8

    out = {
        "cases": len(rows),
        "phase_formula_candidate": "Phi=exp[-i*pi*(j-l)/2] Gamma(j+i rho+1)/|Gamma| Gamma(l-i rho+1)/|Gamma|",
        "candidate_scores": scores,
        "winner": winner,
        "winner_max_relative_error": scores[winner]["max"],
        "max_ratio_modulus_error_from_one": max_modulus_error,
        "max_abs_ratio_phase_radians": max_abs_ratio_phase,
        "identity_map_verified": identity_passed,
        "passed": passed,
        "rows": rows,
        "verdict": "SL2CFOAM_EQUALS_RUHL_ON_PROBED_GRID" if identity_passed else ("SL2CFOAM_PHASE_MAP_IDENTIFIED" if passed else "PHASE_MAP_UNRESOLVED"),
        "next_action": "If identity is verified, compare native Toller t+ + t- directly to sl2cfoam dsmall before wiring branch values into booster quadrature.",
        "scope": "pointwise ordinary dsmall convention audit; no causal booster/F9 credit",
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    if not passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
