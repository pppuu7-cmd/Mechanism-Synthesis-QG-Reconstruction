#!/usr/bin/env python3
"""Direct cross-backend validation of native Toller sum against sl2cfoam dsmall.

Both inputs use the same EPRL booster grid and the raw Ruhl convention.  This is
stronger than validating each implementation only against a shared Python oracle:
it directly compares the compiled native causal kernel to the real upstream
sl2cfoam reduced-Wigner backend.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def key(r):
    return (
        int(r["two_j"]), int(r["two_l"]), int(r["two_m"]),
        round(float(r["gamma"]), 12), round(float(r["beta"]), 12),
    )


def z(re, im):
    return complex(float(re), float(im))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sl2c", required=True)
    ap.add_argument("--native", required=True)
    ap.add_argument("--output", default="results/cross_backend_toller_vs_sl2cfoam.json")
    ap.add_argument("--threshold", type=float, default=5e-12)
    args = ap.parse_args()

    with open(args.sl2c, newline="") as f:
        srows = {key(r): r for r in csv.DictReader(f, delimiter="\t")}
    with open(args.native, newline="") as f:
        nrows = {key(r): r for r in csv.DictReader(f, delimiter="\t")}

    missing_native = sorted(set(srows) - set(nrows))
    missing_sl2c = sorted(set(nrows) - set(srows))
    common = sorted(set(srows) & set(nrows))
    cases = []
    worst = -1.0
    worst_case = None

    for k in common:
        sr, nr = srows[k], nrows[k]
        ds = z(sr["re"], sr["im"])
        tp = z(nr["tp_re"], nr["tp_im"])
        tm = z(nr["tm_re"], nr["tm_im"])
        tsum = tp + tm
        err = abs(tsum - ds) / max(abs(ds), 1e-300)
        cond_native = (abs(tp) + abs(tm)) / max(abs(tsum), 1e-300)
        rec = {
            "two_j": k[0], "two_l": k[1], "two_m": k[2],
            "gamma": k[3], "beta": k[4],
            "sl2cfoam_d": [ds.real, ds.imag],
            "native_t_plus": [tp.real, tp.imag],
            "native_t_minus": [tm.real, tm.imag],
            "native_sum": [tsum.real, tsum.imag],
            "relative_error": err,
            "native_cancellation_condition": cond_native,
        }
        cases.append(rec)
        if err > worst:
            worst, worst_case = err, rec

    passed = (
        not missing_native and not missing_sl2c and len(common) > 0
        and worst < args.threshold
    )
    out = {
        "cases": len(common),
        "grid_exactly_matched": not missing_native and not missing_sl2c,
        "missing_native": [list(k) for k in missing_native],
        "missing_sl2cfoam": [list(k) for k in missing_sl2c],
        "threshold": args.threshold,
        "worst_relative_error": worst,
        "worst_case": worst_case,
        "passed": passed,
        "verdict": "NATIVE_TOLLER_SUM_MATCHES_REAL_SL2CFOAM_DSMALL" if passed else "CROSS_BACKEND_TOLLER_MISMATCH",
        "interpretation": "The compiled causal split reconstructs the same raw reduced Wigner matrix used by the upstream sl2cfoam booster path on an identical grid. Existing booster-level Speziale phase remains downstream and must be left unchanged.",
        "scope": "pointwise cross-backend additive identity only; no integrated booster, causal vertex, or F9 credit",
        "cases_detail": cases,
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k != "cases_detail"}, indent=2))
    if not passed:
        raise SystemExit(3)


if __name__ == "__main__":
    main()
