#!/usr/bin/env python3
"""Iter052: canonical six-order triple-residue antisymmetry gate.

Preregistered in status/ITERATION_052.md before this implementation.
This audits only the existing sequential K4 residue algebra.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import TREES, build_kernel, parse_k, parse_signs
from distributional.k4_fp_channel_decomposition import exact_equal, is_zero
from distributional.k4_rr_residue_structure import residue_step

CONDITIONS = {
    "BASE":   ("1.07", "0.085", "++++++", "0.23,-0.34,0.18,-0.07"),
    "G_LO":   ("0.61", "0.085", "++++++", "0.23,-0.34,0.18,-0.07"),
    "G_HI":   ("1.61", "0.085", "++++++", "0.23,-0.34,0.18,-0.07"),
    "E_LO":   ("1.07", "0.035", "++++++", "0.23,-0.34,0.18,-0.07"),
    "E_HI":   ("1.07", "0.16",  "++++++", "0.23,-0.34,0.18,-0.07"),
    "S_ALT1": ("1.07", "0.085", "+-+-+-", "0.23,-0.34,0.18,-0.07"),
    "S_ALT2": ("1.07", "0.085", "--++--", "0.23,-0.34,0.18,-0.07"),
    "K_ALT1": ("1.07", "0.085", "++++++", "-0.17,0.29,-0.33,0.21"),
    "K_ALT2": ("1.07", "0.085", "++++++", "0.31,0.14,-0.26,-0.19"),
}
PERMS = tuple(itertools.permutations((0, 1, 2)))


def parity(perm):
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return 1 if inv % 2 == 0 else -1


def distinct_exact(values):
    reps = []
    for value in values:
        if not any(exact_equal(value, rep) for rep in reps):
            reps.append(value)
    return reps


def triple_orders(expr, y):
    ordered = {}
    all_steps_exact = True
    for perm in PERMS:
        cur = expr
        steps = []
        for idx in perm:
            step = residue_step(cur, y[idx])
            steps.append({
                "coordinate": idx,
                "recombination_exact": bool(step["recombination_exact"]),
                "meta": step["meta"],
            })
            all_steps_exact = all_steps_exact and bool(step["recombination_exact"])
            cur = sp.cancel(step["R"])
        key = "".join(map(str, perm))
        ordered[key] = {
            "parity": parity(perm),
            "value": cur,
            "value_text": str(cur),
            "steps": steps,
        }

    even_sum = sp.cancel(sum((r["value"] for r in ordered.values() if r["parity"] > 0), sp.Integer(0)))
    odd_sum = sp.cancel(sum((r["value"] for r in ordered.values() if r["parity"] < 0), sp.Integer(0)))
    antisym = sp.cancel(even_sum - odd_sum)
    values = [ordered["".join(map(str, p))]["value"] for p in PERMS]
    reps = distinct_exact(values)
    all_equal = len(reps) == 1

    return {
        "valid": bool(all_steps_exact),
        "all_step_recombinations_exact": bool(all_steps_exact),
        "orders": {
            k: {
                "parity": v["parity"],
                "value": v["value_text"],
                "steps": v["steps"],
            }
            for k, v in ordered.items()
        },
        "even_sum": str(even_sum),
        "odd_sum": str(odd_sum),
        "antisymmetrizer": str(antisym),
        "antisymmetrizer_zero": bool(is_zero(antisym)),
        "all_six_orders_equal": bool(all_equal),
        "distinct_order_value_count": len(reps),
        "distinct_order_values": [str(v) for v in reps],
    }


def compute(condition, tree):
    if condition not in CONDITIONS:
        raise ValueError(condition)
    if tree not in TREES:
        raise ValueError(tree)
    g, e, sign_text, k_text = CONDITIONS[condition]
    gamma = sp.Rational(g)
    epsilon = sp.Rational(e)
    signs = parse_signs(sign_text)
    k = parse_k(k_text)

    y, source_expr, source_meta = build_kernel(gamma, epsilon, signs, k, tree, control=False)
    cy, control_expr, control_meta = build_kernel(gamma, epsilon, signs, k, tree, control=True)
    source = triple_orders(source_expr, y)
    control = triple_orders(control_expr, cy)
    valid = source["valid"] and control["valid"] and control["antisymmetrizer_zero"]

    return {
        "iteration": "Iter052",
        "condition": condition,
        "tree": tree,
        "gamma": g,
        "epsilon": e,
        "signs": sign_text,
        "k": list(map(str, k)),
        "valid": bool(valid),
        "source": source,
        "control": control,
        "source_kernel_meta": source_meta,
        "control_kernel_meta": control_meta,
        "claim_lock": (
            "Canonical triple-residue antisymmetry audit of the existing sequential K4 algebra only; "
            "no multivariate physical amplitude, preferred order, counterterm, K5, G3, F9 or G8 claim."
        ),
    }


def aggregate(input_dir: Path):
    rows = []
    for path in sorted(input_dir.rglob("iter052_*.json")):
        try:
            row = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if row.get("iteration") == "Iter052" and "source" in row:
            rows.append(row)

    expected = len(CONDITIONS) * len(TREES)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter052 lanes, found {len(rows)}")
    keys = {(r["condition"], r["tree"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter052 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_controls_zero = all(r["control"]["antisymmetrizer_zero"] for r in rows)
    source_zero = [r["source"]["antisymmetrizer_zero"] for r in rows]
    all_source_zero = all(source_zero)
    nontrivial = any(r["source"]["distinct_order_value_count"] > 1 for r in rows)

    if not (all_valid and all_controls_zero):
        classification = "ITER052_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif all_source_zero and nontrivial:
        classification = "K4_RRR_CANONICAL_ANTISYMMETRY_IDENTITY_EXACT"
    elif not all_source_zero:
        classification = "K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO"
    else:
        classification = "ITER052_CONTROL_OR_RECONSTRUCTION_INVALID"

    nonzero_positions = [
        f"{r['condition']}/{r['tree']}"
        for r in rows if not r["source"]["antisymmetrizer_zero"]
    ]
    distinct_hist = {}
    for r in rows:
        n = str(r["source"]["distinct_order_value_count"])
        distinct_hist[n] = distinct_hist.get(n, 0) + 1
    by_condition = {}
    for condition in CONDITIONS:
        subset = [r for r in rows if r["condition"] == condition]
        by_condition[condition] = {
            "source_antisym_nonzero_count": sum(not r["source"]["antisymmetrizer_zero"] for r in subset),
            "source_all_six_equal_count": sum(r["source"]["all_six_orders_equal"] for r in subset),
            "distinct_order_counts": [r["source"]["distinct_order_value_count"] for r in subset],
        }

    return {
        "iteration": "Iter052",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_antisymmetrizers_zero": bool(all_controls_zero),
        "all_source_antisymmetrizers_zero": bool(all_source_zero),
        "nontriviality_guard": bool(nontrivial),
        "source_nonzero_antisymmetrizer_count": len(nonzero_positions),
        "source_nonzero_positions": nonzero_positions,
        "source_distinct_order_count_histogram": distinct_hist,
        "by_condition": by_condition,
        "claim_lock": (
            "Canonical S3 antisymmetrizer diagnostic only. Any exact identity requires independent held-out "
            "validation before structural promotion; no K5/G3/F9/G8 or physical-amplitude claim."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("compute", "aggregate"), default="compute")
    ap.add_argument("--condition", choices=tuple(CONDITIONS))
    ap.add_argument("--tree", choices=tuple(TREES))
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.mode == "compute":
        if args.condition is None or args.tree is None:
            raise SystemExit("compute requires --condition and --tree")
        out = compute(args.condition, args.tree)
    else:
        out = aggregate(Path(args.input_dir))
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
