#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from toller_general_eprl_reference import tplus, tminus, d_ruhl  # noqa: E402

mp.mp.dps = 80


def cpair(re: str, im: str) -> mp.mpc:
    return mp.mpc(mp.mpf(re), mp.mpf(im))


def relerr(a: mp.mpc, b: mp.mpc) -> mp.mpf:
    return abs(a - b) / max(abs(b), mp.mpf("1e-40"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("probe")
    ap.add_argument("--output", default="results/native_toller_kernel_validation.json")
    args = ap.parse_args()

    rows = list(csv.DictReader(Path(args.probe).open(), delimiter="\t"))
    worst_plus = mp.mpf("0")
    worst_minus = mp.mpf("0")
    worst_sum = mp.mpf("0")
    worst_case = None
    offdiag_worst = mp.mpf("0")

    for row in rows:
        tj = int(row["two_j"])
        tl = int(row["two_l"])
        tm = int(row["two_m"])
        j = mp.mpf(tj) / 2
        l = mp.mpf(tl) / 2
        m = mp.mpf(tm) / 2
        k = j
        gamma = mp.mpf(row["gamma"])
        beta = mp.mpf(row["beta"])
        rho = gamma * j

        ctp = cpair(row["tp_re"], row["tp_im"])
        ctm = cpair(row["tm_re"], row["tm_im"])
        ptp = tplus(j, l, m, k, rho, beta)
        ptm = tminus(j, l, m, k, rho, beta)
        pd = d_ruhl(j, l, m, k, rho, beta)

        ep = relerr(ctp, ptp)
        em = relerr(ctm, ptm)
        es = relerr(ctp + ctm, pd)
        worst_plus = max(worst_plus, ep)
        worst_minus = max(worst_minus, em)
        worst_sum = max(worst_sum, es)
        if tl > tj:
            offdiag_worst = max(offdiag_worst, es)
        score = max(ep, em, es)
        if worst_case is None or score > worst_case[0]:
            worst_case = (score, {
                "two_j": tj, "two_l": tl, "two_m": tm,
                "gamma": float(gamma), "beta": float(beta),
                "plus_relative_error": float(ep),
                "minus_relative_error": float(em),
                "sum_vs_d_relative_error": float(es),
            })

    threshold = mp.mpf("5e-12")
    passed = max(worst_plus, worst_minus, worst_sum) < threshold
    out = {
        "cases": len(rows),
        "arithmetic": "C long double complex with direct unit-disk 2F1 series; integer-shift gamma ratios by recurrence",
        "reference": "Python/mpmath 80 dps implementation of general Toller Eqs. 43/44 and Ruhl d Eq. 71",
        "worst_plus_relative_error": float(worst_plus),
        "worst_minus_relative_error": float(worst_minus),
        "worst_additive_sum_vs_ruhl_d_relative_error": float(worst_sum),
        "worst_offdiagonal_l_gt_j_sum_error": float(offdiag_worst),
        "threshold": float(threshold),
        "passed": bool(passed),
        "worst_case": worst_case[1] if worst_case else None,
        "verdict": "NATIVE_TOLLER_KERNEL_POINTWISE_VALIDATED" if passed else "NATIVE_TOLLER_KERNEL_NEEDS_STABILIZATION",
        "scope": "standalone Ruhl-convention pointwise kernel only; not yet wired into sl2cfoam booster and no F9 credit",
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
