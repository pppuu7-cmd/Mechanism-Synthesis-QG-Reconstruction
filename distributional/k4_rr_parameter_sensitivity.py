#!/usr/bin/env python3
"""Iter050: K4 RR parameter sensitivity and coarse Feynman pole-topology audit.

Uses the unchanged Iter048 FP=R+A algebra.  This is a diagnostic of the
sequential K4 finite-part construction only; it does not define a physical
multivariate amplitude.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import (
    TREES,
    build_kernel,
    parse_k,
    parse_signs,
)
from distributional.k4_fp_channel_decomposition import (
    CHANNELS,
    degree_pair,
    exact_equal,
    is_zero,
    ordered_channels,
)

PAIRS = ("01", "02", "12")
CONDITIONS = (
    "BASE", "G_LO", "G_HI", "E_LO", "E_HI",
    "S_ALT1", "S_ALT2", "K_ALT1", "K_ALT2",
)
FACTOR_FAMILIES = {
    "gamma": ("G_LO", "G_HI"),
    "epsilon": ("E_LO", "E_HI"),
    "signs": ("S_ALT1", "S_ALT2"),
    "k": ("K_ALT1", "K_ALT2"),
}


def ordered_signature(row):
    return [
        int(row["first_meta"]["upper_pole_count"]),
        int(row["second_from_R_meta"]["upper_pole_count"]),
    ]


def decompose_with_pole_meta(gamma, epsilon, signs, k, tree, pair, control=False):
    y, expr, kernel_meta = build_kernel(
        gamma, epsilon, signs, k, tree, control=control
    )
    i, j = map(int, pair)
    ij = ordered_channels(expr, y, i, j)
    ji = ordered_channels(expr, y, j, i)

    deltas = {
        ch: sp.cancel(ij["channels"][ch] - ji["channels"][ch])
        for ch in CHANNELS
    }
    reconstructed = sp.cancel(sum(deltas.values(), sp.Integer(0)))
    total = sp.cancel(ij["frozen_ordered"] - ji["frozen_ordered"])
    total_reconstruction = exact_equal(reconstructed, total)

    remaining_idx = next(idx for idx in range(3) if idx not in (i, j))
    remaining = y[remaining_idx]
    channels = {
        ch: {
            "zero": bool(is_zero(deltas[ch])),
            "degree": degree_pair(deltas[ch], remaining),
        }
        for ch in CHANNELS
    }

    sig_ij = ordered_signature(ij)
    sig_ji = ordered_signature(ji)
    valid = all([
        ij["ordered_reconstruction"],
        ji["ordered_reconstruction"],
        ij["all_component_matches"],
        ji["all_component_matches"],
        total_reconstruction,
    ])

    return {
        "valid": bool(valid),
        "total_zero": bool(is_zero(total)),
        "total_degree": degree_pair(total, remaining),
        "remaining_coordinate": remaining_idx,
        "channels": channels,
        "rr_nonzero": bool(not channels["RR"]["zero"]),
        "channel_reconstruction_exact": bool(total_reconstruction),
        "ordered_ij_reconstruction_exact": bool(ij["ordered_reconstruction"]),
        "ordered_ji_reconstruction_exact": bool(ji["ordered_reconstruction"]),
        "all_one_step_component_recombinations_exact": bool(
            ij["all_component_matches"] and ji["all_component_matches"]
        ),
        "sig_ij": sig_ij,
        "sig_ji": sig_ji,
        "pole_count_asymmetry": bool(sig_ij != sig_ji),
        "ij_first_meta": ij["first_meta"],
        "ij_second_from_R_meta": ij["second_from_R_meta"],
        "ij_second_from_A_meta": ij["second_from_A_meta"],
        "ji_first_meta": ji["first_meta"],
        "ji_second_from_R_meta": ji["second_from_R_meta"],
        "ji_second_from_A_meta": ji["second_from_A_meta"],
        "kernel_meta": kernel_meta,
    }


def compute(args):
    if args.condition not in CONDITIONS:
        raise ValueError(args.condition)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.pair not in PAIRS:
        raise ValueError(args.pair)

    gamma = sp.Rational(args.gamma)
    epsilon = sp.Rational(args.epsilon)
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    signs = parse_signs(args.signs)
    k = parse_k(args.k)

    source = decompose_with_pole_meta(
        gamma, epsilon, signs, k, args.tree, args.pair, control=False
    )
    control = decompose_with_pole_meta(
        gamma, epsilon, signs, k, args.tree, args.pair, control=True
    )
    control_channels_zero = all(control["channels"][ch]["zero"] for ch in CHANNELS)
    valid = source["valid"] and control["valid"] and control["total_zero"]

    return {
        "iteration": "Iter050",
        "condition": args.condition,
        "tree": args.tree,
        "pair": args.pair,
        "gamma": args.gamma,
        "epsilon": args.epsilon,
        "signs": args.signs,
        "k": list(map(str, k)),
        "valid": bool(valid),
        "source": source,
        "control": control,
        "all_control_channels_zero": bool(control_channels_zero),
        "claim_lock": (
            "OAT source-parameter and coarse pole-count audit of the existing K4 RR diagnostic only; "
            "no selector fitting, counterterm, K5, physical vertex, G3, F9 or G8 claim."
        ),
    }


def mask_for(rows):
    return {
        f"{r['tree']}/{r['pair']}": bool(r["source"]["rr_nonzero"])
        for r in sorted(rows, key=lambda x: (x["tree"], x["pair"]))
    }


def aggregate(input_dir: Path):
    rows = []
    for path in sorted(input_dir.rglob("iter050_*.json")):
        try:
            row = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if row.get("iteration") == "Iter050" and "source" in row:
            rows.append(row)

    expected = len(CONDITIONS) * len(TREES) * len(PAIRS)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter050 lanes, found {len(rows)}")
    keys = {(r["condition"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter050 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_control_totals_zero = all(r["control"]["total_zero"] for r in rows)
    all_control_channels_zero = all(r["all_control_channels_zero"] for r in rows)

    by_condition = {
        c: [r for r in rows if r["condition"] == c]
        for c in CONDITIONS
    }
    for c, subset in by_condition.items():
        if len(subset) != len(TREES) * len(PAIRS):
            raise RuntimeError(f"condition {c}: expected 12 lanes, found {len(subset)}")

    base_mask = mask_for(by_condition["BASE"])
    condition_masks = {c: mask_for(by_condition[c]) for c in CONDITIONS}
    transition_counts = {}
    transition_positions = {}
    for c in CONDITIONS:
        if c == "BASE":
            transition_counts[c] = 0
            transition_positions[c] = []
            continue
        changed = [k for k in sorted(base_mask) if condition_masks[c][k] != base_mask[k]]
        transition_counts[c] = len(changed)
        transition_positions[c] = changed

    factor_transition_counts = {
        fam: sum(transition_counts[c] for c in conds)
        for fam, conds in FACTOR_FAMILIES.items()
    }
    factor_any_transition = {
        fam: any(transition_counts[c] > 0 for c in conds)
        for fam, conds in FACTOR_FAMILIES.items()
    }

    contingency = {
        "rr1_asym1": 0,
        "rr1_asym0": 0,
        "rr0_asym1": 0,
        "rr0_asym0": 0,
    }
    selector_exact = True
    for r in rows:
        rr = bool(r["source"]["rr_nonzero"])
        asym = bool(r["source"]["pole_count_asymmetry"])
        contingency[f"rr{int(rr)}_asym{int(asym)}"] += 1
        selector_exact = selector_exact and (rr == asym)

    any_transition = any(transition_counts[c] > 0 for c in CONDITIONS if c != "BASE")

    if not (all_valid and all_control_totals_zero):
        classification = "ITER050_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif not any_transition:
        classification = "K4_RR_PARAMETER_STABLE_ON_FROZEN_GRID"
    elif selector_exact:
        classification = "K4_RR_FACTOR_DEPENDENT_WITH_POLE_COUNT_SELECTOR"
    else:
        classification = "K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT"

    condition_summary = {}
    for c in CONDITIONS:
        subset = by_condition[c]
        condition_summary[c] = {
            "lane_count": len(subset),
            "rr_nonzero_count": sum(r["source"]["rr_nonzero"] for r in subset),
            "pole_count_asymmetry_count": sum(r["source"]["pole_count_asymmetry"] for r in subset),
            "rr_mask": condition_masks[c],
            "transition_count_vs_BASE": transition_counts[c],
            "transition_positions_vs_BASE": transition_positions[c],
        }

    return {
        "iteration": "Iter050",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_totals_zero": bool(all_control_totals_zero),
        "all_control_channels_zero": bool(all_control_channels_zero),
        "any_rr_transition_vs_BASE": bool(any_transition),
        "pole_count_selector_exact": bool(selector_exact),
        "rr_vs_pole_count_asymmetry": contingency,
        "condition_summary": condition_summary,
        "factor_transition_counts": factor_transition_counts,
        "factor_any_transition": factor_any_transition,
        "claim_lock": (
            "Parameter sensitivity and coarse pole-count topology only. No post-hoc selector, "
            "physical multivariate amplitude, K5, G3, F9 or G8 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["compute", "aggregate"], default="compute")
    ap.add_argument("--condition")
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
        required = [
            args.condition, args.gamma, args.epsilon, args.signs,
            args.k, args.tree, args.pair,
        ]
        if any(v is None for v in required):
            raise SystemExit("compute mode requires condition,gamma,epsilon,signs,k,tree,pair")
        out = compute(args)
    else:
        out = aggregate(Path(args.input_dir))

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
