#!/usr/bin/env python3
"""Exact-source backend repair for Iter076U.

The frozen U hypothesis/census is unchanged. For the only sector used by U,
`j=l=k=1/2`, all four diagonal reduced Toller blocks are simplified exactly
from source Eq.(9), avoiding the known generic mpmath 2F1 continuation bug.
Lane A independently compares these closed forms against the source-backed
high-precision general Toller oracle at moderate beta.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import iter076u_jhalf_intertwiner_contracted_onejet as base

mp.mp.dps = 70
_ORIG_PLUS = base.ep.toller_plus
_ORIG_MINUS = base.ep.toller_minus


def _check_sector(tj, tl, tm, tk):
    return tj == tl == tk == 1 and tm in (-1, 1)


def exact_plus(tj, tl, tm, tk, rho, beta):
    if not _check_sector(tj, tl, tm, tk):
        return _ORIG_PLUS(tj, tl, tm, tk, rho, beta)
    rho = mp.mpf(rho); beta = mp.mpf(beta)
    D = rho * rho + mp.mpf("0.25")
    s = mp.sinh(beta); c = mp.cosh(beta)
    phase = mp.e ** (mp.j * rho * beta)
    if tm == 1:
        return -phase / (2 * D * s * s)
    return phase * (c - 2 * mp.j * rho * s) / (2 * D * s * s)


def exact_minus(tj, tl, tm, tk, rho, beta):
    if not _check_sector(tj, tl, tm, tk):
        return _ORIG_MINUS(tj, tl, tm, tk, rho, beta)
    rho = mp.mpf(rho); beta = mp.mpf(beta)
    D = rho * rho + mp.mpf("0.25")
    s = mp.sinh(beta); c = mp.cosh(beta)
    phase = mp.e ** (-mp.j * rho * beta)
    if tm == -1:
        return -phase / (2 * D * s * s)
    return phase * (c + 2 * mp.j * rho * s) / (2 * D * s * s)


# full_branch in the imported repository module resolves these functions through
# the shared endpoint_precontraction_scan module object, so this patches only
# the exact j=1/2 sector used by the frozen U census.
base.ep.toller_plus = exact_plus
base.ep.toller_minus = exact_minus


def load_oracle():
    p = ROOT / "code" / "toller_general_eprl_reference.py"
    spec = importlib.util.spec_from_file_location("u_toller_oracle", p)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def lane_a_with_backend_control():
    ordinary = base.lane_a()
    oracle = load_oracle()
    worst = mp.mpf("0")
    rows = []
    for gamma_s in ("0.4", "1.2"):
        rho = mp.mpf(gamma_s) / 2
        for beta_s in ("0.3", "0.8", "1.7"):
            beta = mp.mpf(beta_s)
            for tm in (-1, 1):
                for branch in (+1, -1):
                    got = exact_plus(1, 1, tm, 1, rho, beta) if branch > 0 else exact_minus(1, 1, tm, 1, rho, beta)
                    m = mp.mpf(tm) / 2
                    ref = oracle.tplus(mp.mpf("0.5"), mp.mpf("0.5"), m, mp.mpf("0.5"), rho, beta) if branch > 0 else oracle.tminus(mp.mpf("0.5"), mp.mpf("0.5"), m, mp.mpf("0.5"), rho, beta)
                    rel = abs(got - ref) / max(abs(ref), mp.mpf("1e-70"))
                    worst = max(worst, rel)
                    rows.append({"gamma": gamma_s, "beta": beta_s, "two_m": tm, "branch": branch, "relative_residual": mp.nstr(rel, 14)})
    ordinary["backend_control_cases"] = len(rows)
    ordinary["backend_control_worst_relative_residual"] = mp.nstr(worst, 20)
    ordinary["backend_control_threshold"] = "1e-35"
    ordinary["backend_control_rows"] = rows
    ordinary["valid"] = bool(ordinary.get("valid") and worst < mp.mpf("1e-35"))
    return ordinary


MODES = {"A": lane_a_with_backend_control, "C": base.lane_c, "D": base.lane_d}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("A", "census", "C", "D"))
    ap.add_argument("--gamma")
    ap.add_argument("--path-id", type=int)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        obj = base.aggregate(args.aggregate_dir)
    elif args.mode == "census":
        if args.gamma is None or args.path_id not in base.PATHS:
            raise SystemExit("census requires --gamma and valid --path-id")
        obj = base.census(args.gamma, args.path_id)
        obj["backend"] = "exact source Eq.(9) j=l=k=1/2 closed forms"
    elif args.mode in MODES:
        obj = MODES[args.mode]()
    else:
        raise SystemExit("choose --mode or --aggregate-dir")
    base.write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
