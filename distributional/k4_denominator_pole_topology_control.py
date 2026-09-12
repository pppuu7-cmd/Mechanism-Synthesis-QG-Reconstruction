#!/usr/bin/env python3
"""Independent denominator-only pole-topology control for Iter050."""
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

from distributional.k4_forest_order_finite_part import TREES, build_kernel
from distributional.k4_fp_channel_decomposition import ordered_channels

EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
PAIRS = ("01","02","12")
SIGMA_CLASSES = tuple("".join("+" if s > 0 else "-" for s in bits)
                      for bits in itertools.product((1,-1), repeat=3))

VARIANTS = (
    ("E04_K0", sp.Rational(4,100), (sp.Rational(23,100),sp.Rational(-34,100),sp.Rational(18,100),sp.Rational(-7,100))),
    ("E14_K0", sp.Rational(14,100), (sp.Rational(23,100),sp.Rational(-34,100),sp.Rational(18,100),sp.Rational(-7,100))),
    ("E04_K1", sp.Rational(4,100), (sp.Rational(-17,100),sp.Rational(29,100),sp.Rational(-33,100),sp.Rational(21,100))),
    ("E14_K1", sp.Rational(14,100), (sp.Rational(-17,100),sp.Rational(29,100),sp.Rational(-33,100),sp.Rational(21,100))),
)


def edge_signs_from_class(txt: str):
    if txt not in SIGMA_CLASSES:
        raise ValueError(txt)
    sigma = (1,) + tuple(1 if c == "+" else -1 for c in txt)
    edge = tuple(sigma[a] * sigma[b] for a,b in EDGES)
    return sigma, edge, "".join("+" if x > 0 else "-" for x in edge)


def sig(row):
    return {
        "upper": [
            int(row["first_meta"]["upper_pole_count"]),
            int(row["second_from_R_meta"]["upper_pole_count"]),
        ],
        "total": [
            int(row["first_meta"]["pole_count"]),
            int(row["second_from_R_meta"]["pole_count"]),
        ],
    }


def compute_one(sign_class, tree):
    sigma, edge_signs, edge_text = edge_signs_from_class(sign_class)
    rows = []
    valid = True
    for pair in PAIRS:
        i,j = map(int,pair)
        for name, epsilon, k in VARIANTS:
            y, expr, meta = build_kernel(
                sp.Integer(1), epsilon, edge_signs, k, tree, control=True
            )
            ij = ordered_channels(expr, y, i, j)
            ji = ordered_channels(expr, y, j, i)
            lane_valid = all([
                ij["ordered_reconstruction"], ji["ordered_reconstruction"],
                ij["all_component_matches"], ji["all_component_matches"],
            ])
            valid = valid and lane_valid
            rows.append({
                "pair": pair,
                "variant": name,
                "epsilon": str(epsilon),
                "k": list(map(str,k)),
                "valid": bool(lane_valid),
                "sig_ij": sig(ij),
                "sig_ji": sig(ji),
                "kernel_meta": meta,
            })

    pair_summary = {}
    stable = True
    for pair in PAIRS:
        pr = [r for r in rows if r["pair"] == pair]
        keys = [
            (tuple(r["sig_ij"]["upper"]), tuple(r["sig_ij"]["total"]),
             tuple(r["sig_ji"]["upper"]), tuple(r["sig_ji"]["total"]))
            for r in pr
        ]
        pair_stable = all(k == keys[0] for k in keys[1:])
        stable = stable and pair_stable
        pair_summary[pair] = {
            "stable_across_eps_k": bool(pair_stable),
            "reference_signature": {
                "sig_ij": pr[0]["sig_ij"],
                "sig_ji": pr[0]["sig_ji"],
            },
        }

    return {
        "iteration": "Iter050DenominatorControl",
        "sign_class": sign_class,
        "sigma": list(map(int,sigma)),
        "edge_signs": edge_text,
        "tree": tree,
        "valid": bool(valid),
        "stable_across_eps_k": bool(stable),
        "pairs": pair_summary,
        "rows": rows,
        "claim_lock": "Denominator-only F=1 topology control; no source RR inference or physical amplitude claim.",
    }


def aggregate(input_dir: Path):
    rows=[]
    for p in sorted(input_dir.rglob("iter050_denctrl_*.json")):
        try:
            r=json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter050DenominatorControl" and "rows" in r:
            rows.append(r)
    if len(rows) != 32:
        raise RuntimeError(f"expected 32 denominator-control jobs, found {len(rows)}")
    keys={(r["sign_class"],r["tree"]) for r in rows}
    if len(keys) != 32:
        raise RuntimeError("duplicate/missing denominator-control matrix keys")
    all_valid=all(r["valid"] for r in rows)
    all_stable=all(r["stable_across_eps_k"] for r in rows)
    if not all_valid:
        cls="DENOMINATOR_POLE_TOPOLOGY_CONTROL_INVALID"
    elif not all_stable:
        cls="DENOMINATOR_POLE_TOPOLOGY_EPS_OR_K_DEPENDENT"
    else:
        cls="DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE"
    unstable=[
        {"sign_class":r["sign_class"],"tree":r["tree"],
         "pairs":[p for p,v in r["pairs"].items() if not v["stable_across_eps_k"]]}
        for r in rows if not r["stable_across_eps_k"]
    ]
    return {
        "iteration":"Iter050DenominatorControl",
        "job_count":len(rows),
        "classification":cls,
        "all_valid":bool(all_valid),
        "all_stable_across_eps_k":bool(all_stable),
        "unstable_groups":unstable,
        "claim_lock":"Independent F=1 denominator topology baseline only; no source RR selector fit, K5, G3, F9 or G8 claim.",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["compute","aggregate"],default="compute")
    ap.add_argument("--sign-class",choices=SIGMA_CLASSES)
    ap.add_argument("--tree",choices=sorted(TREES))
    ap.add_argument("--input-dir",default="results")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    if a.mode=="compute":
        if a.sign_class is None or a.tree is None:
            raise SystemExit("compute requires --sign-class and --tree")
        out=compute_one(a.sign_class,a.tree)
    else:
        out=aggregate(Path(a.input_dir))
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__ == "__main__":
    main()
