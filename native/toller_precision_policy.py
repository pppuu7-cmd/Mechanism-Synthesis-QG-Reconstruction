#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from toller_general_eprl_reference import tplus, tminus, d_ruhl  # noqa: E402

mp.mp.dps = 90

TARGET_DECIMAL_DIGITS = 12
GUARD_DIGITS = 5


def required_digits(cond: mp.mpf) -> int:
    if cond <= 1:
        return TARGET_DECIMAL_DIGITS + GUARD_DIGITS
    return math.ceil(TARGET_DECIMAL_DIGITS + GUARD_DIGITS + float(mp.log10(cond)))


def main() -> None:
    cases = []
    maxima = {"condition": 0.0, "digits": 0, "bits": 0}
    for tj in (1, 2, 3, 4):
        j = mp.mpf(tj) / 2
        k = j
        for dl in range(0, 5):
            l = j + dl
            for tm in range(-tj, tj + 1, 2):
                m = mp.mpf(tm) / 2
                for gamma in (mp.mpf("0.1"), mp.mpf("0.4"), mp.mpf("1.0"), mp.mpf("1.2")):
                    rho = gamma * j
                    for beta in (mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.4"), mp.mpf("0.8"), mp.mpf("1.7")):
                        tp = tplus(j, l, m, k, rho, beta)
                        tmn = tminus(j, l, m, k, rho, beta)
                        d = d_ruhl(j, l, m, k, rho, beta)
                        cond = (abs(tp) + abs(tmn)) / max(abs(d), mp.mpf("1e-80"))
                        digits = required_digits(cond)
                        bits = math.ceil(digits * math.log2(10))
                        rec = {
                            "j": float(j), "l": float(l), "m": float(m),
                            "gamma": float(gamma), "beta": float(beta),
                            "condition": float(cond),
                            "recommended_decimal_digits": digits,
                            "recommended_binary_bits": bits,
                        }
                        cases.append(rec)
                        if cond > maxima["condition"]:
                            maxima = {"condition": float(cond), "digits": digits, "bits": bits, "case": rec}

    conds = sorted(c["condition"] for c in cases)
    digs = sorted(c["recommended_decimal_digits"] for c in cases)
    def pct(xs, p):
        idx = min(len(xs) - 1, max(0, math.ceil(p * len(xs)) - 1))
        return xs[idx]

    out = {
        "cases": len(cases),
        "target_decimal_digits_after_cancellation": TARGET_DECIMAL_DIGITS,
        "guard_digits": GUARD_DIGITS,
        "condition_percentiles": {
            "p50": pct(conds, 0.50), "p90": pct(conds, 0.90),
            "p99": pct(conds, 0.99), "max": conds[-1],
        },
        "recommended_decimal_digit_percentiles": {
            "p50": pct(digs, 0.50), "p90": pct(digs, 0.90),
            "p99": pct(digs, 0.99), "max": digs[-1],
        },
        "worst_case": maxima,
        "policy": {
            "long_double": "allowed only when recommended_decimal_digits <= 18 and branch reconstruction is not used as a subtraction-sensitive reference",
            "mpfr_128bit": "default causal booster tier when recommended_binary_bits <= 128",
            "mpfr_dynamic": "use recommended_binary_bits plus implementation margin when >128 bits",
        },
        "verdict": "ADAPTIVE_PRECISION_REQUIRED_FOR_CAUSAL_BOOSTER",
        "scope": "precision budgeting from analytic branch cancellation; does not itself compute a booster or F9",
    }
    Path("results").mkdir(exist_ok=True)
    Path("results/toller_precision_policy.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
