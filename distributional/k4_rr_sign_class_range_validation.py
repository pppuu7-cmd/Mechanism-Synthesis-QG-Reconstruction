#!/usr/bin/env python3
"""Iter051C: held-out range validation of frozen Iter051A causal-sign RR masks."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import TREES
from distributional.k4_fp_channel_decomposition import CHANNELS
from distributional.k4_denominator_pole_topology_control import (
    SIGMA_CLASSES,
    edge_signs_from_class,
)
from distributional.k4_rr_parameter_sensitivity import (
    PAIRS,
    decompose_with_pole_meta,
)

POINTS = {
    "H4": {
        "gamma": sp.Rational(31, 100),
        "epsilon": sp.Rational(31, 1000),
        "k": (
            sp.Rational(41, 100),
            sp.Rational(-37, 100),
            sp.Rational(12, 100),
            sp.Rational(-16, 100),
        ),
    },
    "H5": {
        "gamma": sp.Rational(245, 100),
        "epsilon": sp.Rational(163, 1000),
        "k": (
            sp.Rational(-22, 100),
            sp.Rational(47, 100),
            sp.Rational(-31, 100),
            sp.Rational(6, 100),
        ),
    },
}

REFERENCE_ACTIVE = {
    "+++": {"P1/01", "P1/02", "P1/12", "S0/01"},
    "++-": {"P0/12", "P1/01", "P1/02", "P1/12", "S0/01", "S0/12", "S1/12"},
    "+-+": {"P0/01", "P0/02", "P0/12", "P1/01", "S0/01"},
    "+--": {"P0/01", "P0/02", "P0/12", "P1/01", "P1/12", "S0/01", "S0/12", "S1/12"},
    "-++": {"P0/01", "P0/02", "P0/12", "P1/12", "S1/01", "S1/12"},
    "-+-": {"P0/01", "P0/02", "P0/12", "S0/12", "S1/01"},
    "--+": {"P0/01", "P0/12", "P1/01", "P1/02", "P1/12", "S1/01", "S1/12"},
    "---": {"P0/01", "P1/01", "P1/02", "P1/12", "S0/12", "S1/01"},
}

POSITIONS = tuple(f"{tree}/{pair}" for tree in ("S0", "S1", "P0", "P1") for pair in PAIRS)
REFERENCE_MASKS = {
    sc: {pos: (pos in active) for pos in POSITIONS}
    for sc, active in REFERENCE_ACTIVE.items()
}


def compute(args):
    if args.point not in POINTS:
        raise ValueError(args.point)
    if args.sign_class not in SIGMA_CLASSES:
        raise ValueError(args.sign_class)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.pair not in PAIRS:
        raise ValueError(args.pair)

    cfg = POINTS[args.point]
    if sum(cfg["k"], sp.Integer(0)) != 0:
        raise RuntimeError("frozen external flow must sum exactly to zero")

    sigma, edge_signs, edge_text = edge_signs_from_class(args.sign_class)
    source = decompose_with_pole_meta(
        cfg["gamma"], cfg["epsilon"], edge_signs, cfg["k"], args.tree, args.pair, control=False
    )
    control = decompose_with_pole_meta(
        cfg["gamma"], cfg["epsilon"], edge_signs, cfg["k"], args.tree, args.pair, control=True
    )

    control_channels_zero = all(control["channels"][ch]["zero"] for ch in CHANNELS)
    factorized_check = all(
        edge_signs[idx] == sigma[a] * sigma[b]
        for idx, (a, b) in enumerate(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
    )
    valid = all([
        source["valid"],
        control["valid"],
        control["total_zero"],
        control_channels_zero,
        factorized_check,
    ])

    pos = f"{args.tree}/{args.pair}"
    observed = bool(source["rr_nonzero"])
    expected = bool(REFERENCE_MASKS[args.sign_class][pos])

    return {
        "iteration": "Iter051C",
        "point": args.point,
        "gamma": str(cfg["gamma"]),
        "epsilon": str(cfg["epsilon"]),
        "k": list(map(str, cfg["k"])),
        "sign_class": args.sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": args.tree,
        "pair": args.pair,
        "position": pos,
        "valid": bool(valid),
        "factorized_sign_check": bool(factorized_check),
        "source": source,
        "control": control,
        "all_control_channels_zero": bool(control_channels_zero),
        "reference_rr_nonzero": expected,
        "reference_match": bool(observed == expected),
        "claim_lock": (
            "Held-out range validation of frozen Iter051A sequential RR masks only; "
            "no global sign-universality, physical multivariate K4, K5, G3, F9 or G8 claim."
        ),
    }


def mask_for(rows):
    return {
        f"{r['tree']}/{r['pair']}": bool(r["source"]["rr_nonzero"])
        for r in sorted(rows, key=lambda x: (x["tree"], x["pair"]))
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter051c_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter051C" and "source" in r:
            rows.append(r)

    expected_n = len(POINTS) * len(SIGMA_CLASSES) * len(TREES) * len(PAIRS)
    if len(rows) != expected_n:
        raise RuntimeError(f"expected {expected_n} Iter051C lanes, found {len(rows)}")
    keys = {(r["point"], r["sign_class"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != expected_n:
        raise RuntimeError("duplicate/missing Iter051C matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_controls_zero = all(
        r["control"]["total_zero"] and r["all_control_channels_zero"] for r in rows
    )
    all_factorized = all(r["factorized_sign_check"] for r in rows)
    all_lane_reference_matches = all(r["reference_match"] for r in rows)

    classes = {}
    total_reference_hamming = 0
    total_cross_point_hamming = 0
    for sc in SIGMA_CLASSES:
        ref = REFERENCE_MASKS[sc]
        by_point = {}
        point_masks = {}
        for pt in POINTS:
            subset = [r for r in rows if r["sign_class"] == sc and r["point"] == pt]
            if len(subset) != len(TREES) * len(PAIRS):
                raise RuntimeError(f"{pt}/{sc}: expected 12 lanes, found {len(subset)}")
            mask = mask_for(subset)
            point_masks[pt] = mask
            changed = [pos for pos in POSITIONS if mask[pos] != ref[pos]]
            total_reference_hamming += len(changed)
            by_point[pt] = {
                "rr_mask": mask,
                "rr_nonzero_count": int(sum(mask.values())),
                "reference_hamming_distance": len(changed),
                "changed_positions_vs_reference": changed,
            }

        cross_changed = [pos for pos in POSITIONS if point_masks["H4"][pos] != point_masks["H5"][pos]]
        total_cross_point_hamming += len(cross_changed)
        classes[sc] = {
            "reference_mask": ref,
            "reference_rr_nonzero_count": int(sum(ref.values())),
            "H4": by_point["H4"],
            "H5": by_point["H5"],
            "H4_H5_hamming_distance": len(cross_changed),
            "H4_H5_changed_positions": cross_changed,
        }

    if not (all_valid and all_controls_zero and all_factorized):
        classification = "ITER051C_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif all_lane_reference_matches and total_reference_hamming == 0:
        classification = "K4_RR_SIGN_CLASS_RANGE_STABLE"
    else:
        classification = "K4_RR_SIGN_CLASS_RANGE_DEPENDENT"

    return {
        "iteration": "Iter051C",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_totals_and_channels_zero": bool(all_controls_zero),
        "all_factorized_sign_checks": bool(all_factorized),
        "all_lane_reference_matches": bool(all_lane_reference_matches),
        "total_reference_hamming_distance": int(total_reference_hamming),
        "total_H4_H5_hamming_distance": int(total_cross_point_hamming),
        "classes": classes,
        "claim_lock": (
            "Exact wider-range held-out validation of the frozen Iter051A sequential RR masks only. "
            "No fitted selector, global sign theorem, physical amplitude, K5, G3, F9 or G8 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["compute", "aggregate"], default="compute")
    ap.add_argument("--point", choices=sorted(POINTS))
    ap.add_argument("--sign-class", choices=SIGMA_CLASSES)
    ap.add_argument("--tree", choices=sorted(TREES))
    ap.add_argument("--pair", choices=PAIRS)
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    a = ap.parse_args()

    if a.mode == "compute":
        if any(v is None for v in (a.point, a.sign_class, a.tree, a.pair)):
            raise SystemExit("compute requires --point --sign-class --tree --pair")
        out = compute(a)
    else:
        out = aggregate(Path(a.input_dir))

    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
