#!/usr/bin/env python3
"""Iter051A: exhaustive factorized causal-sign RR census on held-out nuisance points."""
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
    "H1": {
        "gamma": sp.Rational(74, 100),
        "epsilon": sp.Rational(52, 1000),
        "k": (sp.Rational(27,100), sp.Rational(-18,100), sp.Rational(-24,100), sp.Rational(15,100)),
    },
    "H2": {
        "gamma": sp.Rational(132, 100),
        "epsilon": sp.Rational(117, 1000),
        "k": (sp.Rational(-13,100), sp.Rational(26,100), sp.Rational(-38,100), sp.Rational(25,100)),
    },
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
        for idx, (a,b) in enumerate(((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
    )
    valid = all([
        source["valid"],
        control["valid"],
        control["total_zero"],
        control_channels_zero,
        factorized_check,
    ])
    return {
        "iteration": "Iter051A",
        "point": args.point,
        "gamma": str(cfg["gamma"]),
        "epsilon": str(cfg["epsilon"]),
        "k": list(map(str, cfg["k"])),
        "sign_class": args.sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": args.tree,
        "pair": args.pair,
        "valid": bool(valid),
        "factorized_sign_check": bool(factorized_check),
        "source": source,
        "control": control,
        "all_control_channels_zero": bool(control_channels_zero),
        "claim_lock": (
            "Exhaustive factorized causal-sign census of the existing sequential K4 RR diagnostic only; "
            "no physical multivariate amplitude, K5, G3, F9 or G8 claim."
        ),
    }


def mask_for(rows):
    return {
        f"{r['tree']}/{r['pair']}": bool(r["source"]["rr_nonzero"])
        for r in sorted(rows, key=lambda x: (x["tree"], x["pair"]))
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter051a_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter051A" and "source" in r:
            rows.append(r)

    expected = len(POINTS) * len(SIGMA_CLASSES) * len(TREES) * len(PAIRS)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter051A lanes, found {len(rows)}")
    keys = {(r["point"], r["sign_class"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter051A matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_controls_zero = all(r["control"]["total_zero"] and r["all_control_channels_zero"] for r in rows)
    all_factorized = all(r["factorized_sign_check"] for r in rows)

    classes = {}
    stable = True
    total_hamming = 0
    for sc in SIGMA_CLASSES:
        by_point = {}
        for pt in POINTS:
            subset = [r for r in rows if r["sign_class"] == sc and r["point"] == pt]
            if len(subset) != len(TREES) * len(PAIRS):
                raise RuntimeError(f"{pt}/{sc}: expected 12 lanes, found {len(subset)}")
            mask = mask_for(subset)
            by_point[pt] = {
                "rr_mask": mask,
                "rr_nonzero_count": sum(mask.values()),
            }
        changed = [k for k in sorted(by_point["H1"]["rr_mask"])
                   if by_point["H1"]["rr_mask"][k] != by_point["H2"]["rr_mask"][k]]
        hamming = len(changed)
        total_hamming += hamming
        stable = stable and (hamming == 0)
        classes[sc] = {
            "H1": by_point["H1"],
            "H2": by_point["H2"],
            "hamming_distance": hamming,
            "changed_positions": changed,
        }

    if not (all_valid and all_controls_zero and all_factorized):
        classification = "ITER051A_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif stable:
        classification = "K4_RR_SIGN_CLASS_NUISANCE_STABLE"
    else:
        classification = "K4_RR_SIGN_CLASS_NUISANCE_DEPENDENT"

    return {
        "iteration": "Iter051A",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_totals_and_channels_zero": bool(all_controls_zero),
        "all_factorized_sign_checks": bool(all_factorized),
        "all_sign_class_masks_nuisance_stable": bool(stable),
        "total_hamming_distance_H1_H2": int(total_hamming),
        "classes": classes,
        "claim_lock": (
            "Sign-class nuisance stability of the sequential RR diagnostic only. No selector mechanism, "
            "physical amplitude, K5, G3, F9 or G8 promotion."
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
