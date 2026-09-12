#!/usr/bin/env python3
"""Iter047: exact pairwise commutators of the unchanged Iter045/046 FP operator."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# When executed as `python distributional/...py`, Python places the script
# directory rather than the repository root on sys.path.  Add only the repo
# root; this is an infrastructure fix and changes no frozen science.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import (
    TREES, build_kernel, finite_part_1d, parse_k, parse_signs
)

PAIRS = ("01", "02", "12")


def two_step(expr, y, first: int, second: int):
    a, ma = finite_part_1d(expr, y[first])
    b, mb = finite_part_1d(a, y[second])
    return sp.cancel(b), [ma, mb]


def commutator(gamma, epsilon, signs, k, tree, pair, control=False):
    y, expr, meta = build_kernel(gamma, epsilon, signs, k, tree, control=control)
    i, j = map(int, pair)
    ij, mij = two_step(expr, y, i, j)
    ji, mji = two_step(expr, y, j, i)
    diff = sp.cancel(ij - ji)
    remaining = next(idx for idx in range(3) if idx not in (i, j))
    var = y[remaining]
    num, den = sp.fraction(diff)
    zero = sp.simplify(diff) == 0
    if zero:
        num_degree = -1
        den_degree = 0
    else:
        num_degree = int(sp.Poly(num, var, domain="EX").degree())
        den_degree = int(sp.Poly(den, var, domain="EX").degree())
    return {
        "zero": bool(zero),
        "difference_exact": str(diff),
        "remaining_coordinate": remaining,
        "numerator_degree": num_degree,
        "denominator_degree": den_degree,
        "ij_stages": mij,
        "ji_stages": mji,
        "kernel_meta": meta,
    }


def compute(args):
    gamma = sp.Rational(args.gamma)
    epsilon = sp.Rational(args.epsilon)
    signs = parse_signs(args.signs)
    k = parse_k(args.k)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.pair not in PAIRS:
        raise ValueError(args.pair)
    src = commutator(gamma, epsilon, signs, k, args.tree, args.pair, False)
    ctl = commutator(gamma, epsilon, signs, k, args.tree, args.pair, True)
    return {
        "iteration": "Iter047",
        "case": args.case,
        "tree": args.tree,
        "pair": args.pair,
        "gamma": args.gamma,
        "epsilon": args.epsilon,
        "signs": args.signs,
        "k": list(map(str, k)),
        "source": src,
        "control": ctl,
        "lane_classification": (
            "K4_FP_COMMUTATOR_CONTROL_INVALID" if not ctl["zero"] else
            "SOURCE_COMMUTATOR_ZERO" if src["zero"] else
            "SOURCE_COMMUTATOR_NONZERO_CONTROL_ZERO"
        ),
        "claim_lock": "Pairwise sequential-FP algebra only; no physical divergence, counterterm, K5, G3, F9 or G8 claim.",
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter047_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter047" and "source" in r:
            rows.append(r)
    if len(rows) != 24:
        raise RuntimeError(f"expected 24 Iter047 lanes, found {len(rows)}")
    keys = {(r["case"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != 24:
        raise RuntimeError("duplicate/missing Iter047 matrix keys")
    control_valid = all(r["control"]["zero"] for r in rows)
    source_all_zero = all(r["source"]["zero"] for r in rows)
    if not control_valid:
        classification = "K4_FP_COMMUTATOR_CONTROL_INVALID"
    elif source_all_zero:
        classification = "K4_PAIRWISE_FP_COMMUTATORS_ZERO"
    else:
        classification = "K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED"
    per_case = {}
    for case in ("A", "B"):
        cr = [r for r in rows if r["case"] == case]
        nz = [
            {"tree": r["tree"], "pair": r["pair"],
             "num_degree": r["source"]["numerator_degree"],
             "den_degree": r["source"]["denominator_degree"]}
            for r in cr if not r["source"]["zero"]
        ]
        per_case[case] = {
            "lane_count": len(cr),
            "nonzero_source_commutator_count": len(nz),
            "nonzero_source_lanes": nz,
            "all_control_commutators_zero": all(r["control"]["zero"] for r in cr),
        }
    return {
        "iteration": "Iter047",
        "lane_count": len(rows),
        "classification": classification,
        "all_control_commutators_zero": control_valid,
        "all_source_commutators_zero": source_all_zero,
        "cases": per_case,
        "claim_lock": "Exact localization of the sequential 1D FP obstruction only; no physical vertex/divergence or novelty promotion.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["compute", "aggregate"], default="compute")
    ap.add_argument("--case")
    ap.add_argument("--gamma")
    ap.add_argument("--epsilon")
    ap.add_argument("--signs")
    ap.add_argument("--k")
    ap.add_argument("--tree", choices=sorted(TREES))
    ap.add_argument("--pair", choices=PAIRS)
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.mode == "compute":
        required = [args.case, args.gamma, args.epsilon, args.signs, args.k, args.tree, args.pair]
        if any(v is None for v in required):
            raise SystemExit("compute mode requires case,gamma,epsilon,signs,k,tree,pair")
        out = compute(args)
    else:
        out = aggregate(Path(args.input_dir))
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
