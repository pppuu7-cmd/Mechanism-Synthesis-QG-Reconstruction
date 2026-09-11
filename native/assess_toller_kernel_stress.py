#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from toller_general_eprl_reference import tplus, tminus, d_ruhl  # noqa: E402

mp.mp.dps = 90


def zpair(r, i):
    return mp.mpc(mp.mpf(r), mp.mpf(i))


def rel(a, b):
    return abs(a - b) / max(abs(b), mp.mpf("1e-60"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("probe")
    ap.add_argument("--output", default="results/native_toller_stress.json")
    args = ap.parse_args()

    records = []
    with Path(args.probe).open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            tj, tl, tm = int(row["two_j"]), int(row["two_l"]), int(row["two_m"])
            j, l, m = mp.mpf(tj)/2, mp.mpf(tl)/2, mp.mpf(tm)/2
            k = j
            gamma, beta = mp.mpf(row["gamma"]), mp.mpf(row["beta"])
            rho = gamma*j
            tp, tmn, d = tplus(j,l,m,k,rho,beta), tminus(j,l,m,k,rho,beta), d_ruhl(j,l,m,k,rho,beta)
            ctp, ctm = zpair(row["tp_re"], row["tp_im"]), zpair(row["tm_re"], row["tm_im"])
            cond = (abs(tp)+abs(tmn))/max(abs(d),mp.mpf("1e-80"))
            ep, em, es = rel(ctp,tp), rel(ctm,tmn), rel(ctp+ctm,d)
            records.append({
                "condition": float(cond), "branch_error": float(max(ep,em)), "sum_error": float(es),
                "j": float(j), "l": float(l), "m": float(m), "gamma": float(gamma), "beta": float(beta)
            })

    records.sort(key=lambda r: r["condition"])
    bins = [(1e2,"<=1e2"),(1e4,"<=1e4"),(1e6,"<=1e6"),(1e8,"<=1e8"),(1e10,"<=1e10"),(1e12,"<=1e12"),(1e16,"<=1e16")]
    stats=[]
    low=0.0
    for hi,label in bins:
        xs=[r for r in records if low < r["condition"] <= hi]
        if xs:
            stats.append({"condition_bin":label,"count":len(xs),"max_branch_error":max(x["branch_error"] for x in xs),"max_sum_error":max(x["sum_error"] for x in xs)})
        low=hi

    safe12=[r["condition"] for r in records if r["branch_error"] < 1e-12 and r["sum_error"] < 1e-12]
    unsafe12=[r["condition"] for r in records if r["branch_error"] >= 1e-12 or r["sum_error"] >= 1e-12]
    safe8=[r["condition"] for r in records if r["branch_error"] < 1e-8 and r["sum_error"] < 1e-8]
    unsafe8=[r["condition"] for r in records if r["branch_error"] >= 1e-8 or r["sum_error"] >= 1e-8]
    worst=max(records,key=lambda r:max(r["branch_error"],r["sum_error"]))

    out={
        "cases":len(records),
        "condition_range":[records[0]["condition"],records[-1]["condition"]],
        "bins":stats,
        "largest_condition_still_below_1e-12":max(safe12) if safe12 else None,
        "smallest_condition_exceeding_1e-12":min(unsafe12) if unsafe12 else None,
        "largest_condition_still_below_1e-8":max(safe8) if safe8 else None,
        "smallest_condition_exceeding_1e-8":min(unsafe8) if unsafe8 else None,
        "worst_case":worst,
        "verdict":"MEASURED_LONG_DOUBLE_STABILITY_ENVELOPE",
        "implication":"Use this measured envelope together with analytic condition-number budgeting to choose the switch to MPFR/guarded precision; do not assume long double is safe in high-cancellation sectors.",
        "scope":"standalone pointwise stress test only; no booster/F9 credit"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__ == "__main__":
    main()
