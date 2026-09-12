#!/usr/bin/env python3
"""Iter049: covariance of the Iter048 RR selector under cycle-coordinate permutations."""
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
from distributional.k4_fp_channel_decomposition import (
    CHANNELS,
    degree_pair,
    exact_equal,
    is_zero,
    ordered_channels,
)

PERMS = tuple("".join(map(str, p)) for p in itertools.permutations(range(3)))


def permuted_decomposition(gamma, epsilon, signs, k, tree, perm_text, control=False):
    p = tuple(map(int, perm_text))
    if sorted(p) != [0, 1, 2]:
        raise ValueError(f"invalid permutation {perm_text}")

    y, expr, kernel_meta = build_kernel(gamma, epsilon, signs, k, tree, control=control)
    # Infrastructure-only repair: cycle variables are real integration coordinates,
    # matching the assumptions carried by the original build_kernel symbols.
    z = sp.symbols("z0 z1 z2", real=True)
    forward = {y[p[a]]: z[a] for a in range(3)}
    backward = {z[a]: y[p[a]] for a in range(3)}
    expr_p = sp.cancel(expr.xreplace(forward))
    roundtrip = sp.cancel(expr_p.xreplace(backward))
    roundtrip_exact = exact_equal(roundtrip, expr)

    ij = ordered_channels(expr_p, z, 0, 1)
    ji = ordered_channels(expr_p, z, 1, 0)
    deltas = {
        ch: sp.cancel(ij["channels"][ch] - ji["channels"][ch])
        for ch in CHANNELS
    }
    reconstructed = sp.cancel(sum(deltas.values(), sp.Integer(0)))
    total = sp.cancel(ij["frozen_ordered"] - ji["frozen_ordered"])
    total_reconstruction = exact_equal(reconstructed, total)

    remaining = z[2]
    channel_rows = {
        ch: {
            "zero": bool(is_zero(deltas[ch])),
            "degree": degree_pair(deltas[ch], remaining),
        }
        for ch in CHANNELS
    }
    valid = all([
        roundtrip_exact,
        ij["ordered_reconstruction"],
        ji["ordered_reconstruction"],
        ij["all_component_matches"],
        ji["all_component_matches"],
        total_reconstruction,
    ])

    original_ordered_pair = [p[0], p[1]]
    original_unordered_pair = "".join(map(str, sorted(original_ordered_pair)))
    return {
        "valid": bool(valid),
        "roundtrip_exact": bool(roundtrip_exact),
        "total_zero": bool(is_zero(total)),
        "total_degree": degree_pair(total, remaining),
        "channels": channel_rows,
        "channel_reconstruction_exact": bool(total_reconstruction),
        "ordered_01_reconstruction_exact": bool(ij["ordered_reconstruction"]),
        "ordered_10_reconstruction_exact": bool(ji["ordered_reconstruction"]),
        "all_one_step_component_recombinations_exact": bool(
            ij["all_component_matches"] and ji["all_component_matches"]
        ),
        "permutation": perm_text,
        "original_ordered_pair": original_ordered_pair,
        "original_unordered_pair": original_unordered_pair,
        "original_remaining_coordinate": p[2],
        "rr_nonzero": bool(not channel_rows["RR"]["zero"]),
        "kernel_meta": kernel_meta,
    }


def compute(args):
    gamma = sp.Rational(args.gamma)
    epsilon = sp.Rational(args.epsilon)
    signs = parse_signs(args.signs)
    k = parse_k(args.k)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.permutation not in PERMS:
        raise ValueError(args.permutation)

    source = permuted_decomposition(
        gamma, epsilon, signs, k, args.tree, args.permutation, control=False
    )
    control = permuted_decomposition(
        gamma, epsilon, signs, k, args.tree, args.permutation, control=True
    )
    control_channels_zero = all(control["channels"][ch]["zero"] for ch in CHANNELS)
    valid = source["valid"] and control["valid"] and control["total_zero"]
    return {
        "iteration": "Iter049",
        "case": args.case,
        "tree": args.tree,
        "permutation": args.permutation,
        "gamma": args.gamma,
        "epsilon": args.epsilon,
        "signs": args.signs,
        "k": list(map(str, k)),
        "valid": bool(valid),
        "source": source,
        "control": control,
        "all_control_channels_zero": bool(control_channels_zero),
        "claim_lock": (
            "Permutation covariance audit of the existing Iter048 diagnostic split only; "
            "no physical multivariate amplitude, K5, G3, F9 or G8 claim."
        ),
    }


def summarize_group(rows):
    pair_groups = {}
    for pair in ("01", "02", "12"):
        pr = [r for r in rows if r["source"]["original_unordered_pair"] == pair]
        if len(pr) != 2:
            raise RuntimeError(f"expected two orientations for pair {pair}, found {len(pr)}")
        statuses = [r["source"]["rr_nonzero"] for r in pr]
        pair_groups[pair] = {
            "lane_count": 2,
            "rr_statuses": statuses,
            "orientation_invariant": statuses[0] == statuses[1],
            "rr_nonzero": statuses[0] if statuses[0] == statuses[1] else None,
            "permutations": [r["permutation"] for r in pr],
        }

    mapped_pair_covariant = all(v["orientation_invariant"] for v in pair_groups.values())
    pair_values = [v["rr_nonzero"] for v in pair_groups.values() if v["rr_nonzero"] is not None]
    pair_selective = (
        mapped_pair_covariant
        and any(pair_values)
        and not all(pair_values)
    )
    all_lane_statuses = [r["source"]["rr_nonzero"] for r in rows]
    position_locked = all(x == all_lane_statuses[0] for x in all_lane_statuses)
    selected_pairs = [p for p, v in pair_groups.items() if v["rr_nonzero"] is True]
    return {
        "mapped_pair_covariant": bool(mapped_pair_covariant),
        "pair_selective": bool(pair_selective),
        "position_locked": bool(position_locked),
        "selected_rr_pairs": selected_pairs,
        "pairs": pair_groups,
    }


def aggregate(input_dir: Path):
    rows = []
    for path in sorted(input_dir.rglob("iter049_*.json")):
        try:
            row = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if row.get("iteration") == "Iter049" and "source" in row:
            rows.append(row)
    if len(rows) != 48:
        raise RuntimeError(f"expected 48 Iter049 lanes, found {len(rows)}")
    keys = {(r["case"], r["tree"], r["permutation"]) for r in rows}
    if len(keys) != 48:
        raise RuntimeError("duplicate/missing Iter049 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_control_totals_zero = all(r["control"]["total_zero"] for r in rows)
    all_control_channels_zero = all(r["all_control_channels_zero"] for r in rows)

    groups = {}
    for case in ("A", "B"):
        groups[case] = {}
        for tree in ("S0", "S1", "P0", "P1"):
            subset = [r for r in rows if r["case"] == case and r["tree"] == tree]
            if len(subset) != 6:
                raise RuntimeError(f"expected six permutations for {case}/{tree}")
            groups[case][tree] = summarize_group(subset)

    every_covariant = all(
        groups[c][t]["mapped_pair_covariant"]
        for c in groups for t in groups[c]
    )
    every_selective = all(
        groups[c][t]["pair_selective"]
        for c in groups for t in groups[c]
    )
    every_position_locked = all(
        groups[c][t]["position_locked"]
        for c in groups for t in groups[c]
    )
    cases_consistent = all(
        groups["A"][t]["selected_rr_pairs"] == groups["B"][t]["selected_rr_pairs"]
        for t in ("S0", "S1", "P0", "P1")
    )

    if not (all_valid and all_control_totals_zero):
        classification = "ITER049_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif every_covariant and every_selective and cases_consistent:
        classification = "K4_RR_SELECTOR_PAIR_COVARIANT"
    elif every_position_locked:
        classification = "K4_RR_SELECTOR_POSITION_LOCKED"
    else:
        classification = "K4_RR_SELECTOR_NONCOVARIANT"

    return {
        "iteration": "Iter049",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_totals_zero": bool(all_control_totals_zero),
        "all_control_channels_zero": bool(all_control_channels_zero),
        "every_group_mapped_pair_covariant": bool(every_covariant),
        "every_group_pair_selective": bool(every_selective),
        "every_group_position_locked": bool(every_position_locked),
        "held_out_cases_consistent_per_tree": bool(cases_consistent),
        "groups": groups,
        "claim_lock": (
            "Selector covariance only. No physical vertex divergence, multivariate extension, "
            "K5 readiness, G3, F9 or G8 promotion."
        ),
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
    ap.add_argument("--permutation", choices=PERMS)
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    if args.mode == "compute":
        required = [args.case, args.gamma, args.epsilon, args.signs, args.k, args.tree, args.permutation]
        if any(v is None for v in required):
            raise SystemExit("compute mode requires case,gamma,epsilon,signs,k,tree,permutation")
        out = compute(args)
    else:
        out = aggregate(Path(args.input_dir))

    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
