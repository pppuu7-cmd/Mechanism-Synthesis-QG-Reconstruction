#!/usr/bin/env python3
"""Iter051: exact K4 RR pole/residue geometry and cancellation audit.

Preregistered in status/ITERATION_051.md before this implementation.
The underlying K4 kernel and FP=R+A algebra are unchanged from Iter050.
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
    _linear_roots_of_denominator,
    build_kernel,
    finite_part_1d,
    parse_k,
    parse_signs,
)
from distributional.k4_fp_channel_decomposition import CHANNELS, exact_equal, is_zero
from distributional.k4_rr_parameter_sensitivity import decompose_with_pole_meta

PAIRS = ("01", "02", "12")
CONDITIONS = (
    "BASE", "G_LO", "G_HI", "E_LO", "E_HI",
    "S_ALT1", "S_ALT2", "K_ALT1", "K_ALT2",
)


def exact_multiset_equal(xs, ys):
    if len(xs) != len(ys):
        return False
    remaining = list(ys)
    for x in xs:
        hit = None
        for idx, y in enumerate(remaining):
            if exact_equal(sp.cancel(x), sp.cancel(y)):
                hit = idx
                break
        if hit is None:
            return False
        remaining.pop(hit)
    return not remaining


def fp_detail(expr, var):
    """Exact unchanged R/A split plus upper-pole roots and individual residues."""
    expr = sp.cancel(expr)
    num, den = sp.fraction(expr)
    Pn = sp.Poly(num, var, domain="EX")
    Pd = sp.Poly(den, var, domain="EX")
    Q, R = sp.div(Pn, Pd)
    rem = sp.cancel(R.as_expr() / Pd.as_expr())

    rn, rd = sp.fraction(rem)
    Prn = sp.Poly(rn, var, domain="EX")
    Prd = sp.Poly(rd, var, domain="EX")
    dn, dd = Prn.degree(), Prd.degree()
    if Prn.is_zero:
        a_minus1 = sp.Integer(0)
    elif dn == dd - 1:
        a_minus1 = sp.cancel(Prn.LC() / Prd.LC())
    elif dn < dd - 1:
        a_minus1 = sp.Integer(0)
    else:
        raise RuntimeError(f"improper remainder after division: {dn}/{dd}")

    roots = _linear_roots_of_denominator(Prd.as_expr(), var)
    Dprime = sp.diff(Prd.as_expr(), var)
    Nexpr = Prn.as_expr()
    upper = []
    for root, imr in roots:
        sign = float(sp.N(imr, 30))
        if abs(sign) < 1e-14:
            raise RuntimeError(f"unexpected real-axis pole: {root}")
        residue = sp.cancel(Nexpr.subs(var, root) / Dprime.subs(var, root))
        if sign > 0:
            upper.append((sp.cancel(root), residue, sp.cancel(imr)))

    residue_sum = sp.cancel(sum((r for _, r, _ in upper), sp.Integer(0)))
    Rcomp = sp.cancel(2 * sp.pi * sp.I * residue_sum)
    Acomp = sp.cancel(-sp.pi * sp.I * a_minus1)
    frozen, _ = finite_part_1d(expr, var)
    full = sp.cancel(Rcomp + Acomp)
    return {
        "R": Rcomp,
        "A": Acomp,
        "matches_frozen": bool(exact_equal(full, frozen)),
        "upper": upper,
        "upper_residue_sum": residue_sum,
        "upper_count": len(upper),
        "quotient_degree": -1 if Q.is_zero else int(Q.degree()),
    }


def serial_detail(d):
    return {
        "upper_count": d["upper_count"],
        "upper_roots_exact": [str(x) for x, _, _ in d["upper"]],
        "upper_residues_exact": [str(r) for _, r, _ in d["upper"]],
        "upper_imag_parts_exact": [str(im) for _, _, im in d["upper"]],
        "upper_residue_sum_exact": str(d["upper_residue_sum"]),
        "R_exact": str(d["R"]),
        "matches_frozen": d["matches_frozen"],
        "quotient_degree": d["quotient_degree"],
    }


def geometry_for_order(expr, y, first, second):
    d1 = fp_detail(expr, y[first])
    d2 = fp_detail(d1["R"], y[second])
    return d1, d2


def compute(args):
    gamma = sp.Rational(args.gamma)
    epsilon = sp.Rational(args.epsilon)
    signs = parse_signs(args.signs)
    k = parse_k(args.k)
    if args.condition not in CONDITIONS or args.tree not in TREES or args.pair not in PAIRS:
        raise ValueError("invalid matrix coordinate")

    y, expr, _ = build_kernel(gamma, epsilon, signs, k, args.tree, control=False)
    i, j = map(int, args.pair)
    _, ij2 = geometry_for_order(expr, y, i, j)
    _, ji2 = geometry_for_order(expr, y, j, i)

    ij_roots = [x for x, _, _ in ij2["upper"]]
    ji_roots = [x for x, _, _ in ji2["upper"]]
    ij_residues = [r for _, r, _ in ij2["upper"]]
    ji_residues = [r for _, r, _ in ji2["upper"]]

    root_equal = exact_multiset_equal(ij_roots, ji_roots)
    residue_equal = exact_multiset_equal(ij_residues, ji_residues)
    sum_equal = exact_equal(ij2["upper_residue_sum"], ji2["upper_residue_sum"])
    rr = sp.cancel(ij2["R"] - ji2["R"])
    rr_zero = is_zero(rr)

    source = decompose_with_pole_meta(gamma, epsilon, signs, k, args.tree, args.pair, control=False)
    control = decompose_with_pole_meta(gamma, epsilon, signs, k, args.tree, args.pair, control=True)
    control_channels_zero = all(control["channels"][ch]["zero"] for ch in CHANNELS)

    logical_consistency = (rr_zero == sum_equal) and (rr_zero == (not source["rr_nonzero"]))
    valid = all([
        source["valid"], control["valid"], control["total_zero"], control_channels_zero,
        ij2["matches_frozen"], ji2["matches_frozen"], logical_consistency,
    ])

    if not logical_consistency:
        lane_class = "ITER051_INTERNAL_INCONSISTENCY"
    elif root_equal and residue_equal:
        lane_class = "ORDERED_RESIDUE_DATA_IDENTICAL"
    elif sum_equal:
        lane_class = "GEOMETRY_DIFFERS_BUT_SUM_CANCELS"
    else:
        lane_class = "GEOMETRY_DIFFERS_AND_SUM_DIFFERS"

    return {
        "iteration": "Iter051",
        "condition": args.condition,
        "tree": args.tree,
        "pair": args.pair,
        "valid": bool(valid),
        "lane_class": lane_class,
        "rr_zero": bool(rr_zero),
        "rr_exact": str(rr),
        "upper_count_equal": bool(ij2["upper_count"] == ji2["upper_count"]),
        "upper_root_multiset_equal": bool(root_equal),
        "upper_residue_multiset_equal": bool(residue_equal),
        "upper_residue_sum_equal": bool(sum_equal),
        "ij_second_R": serial_detail(ij2),
        "ji_second_R": serial_detail(ji2),
        "source_reconstruction_valid": bool(source["valid"]),
        "control_total_zero": bool(control["total_zero"]),
        "control_channels_zero": bool(control_channels_zero),
        "claim_lock": "Exact residue-geometry diagnostic of unchanged sequential K4 RR only; no fitted selector, counterterm, K5, physical vertex, G3, F9 or G8 claim.",
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter051_*.json")):
        try:
            row = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if row.get("iteration") == "Iter051" and "lane_class" in row:
            rows.append(row)
    expected = len(CONDITIONS) * len(TREES) * len(PAIRS)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} lanes, found {len(rows)}")
    if len({(r['condition'], r['tree'], r['pair']) for r in rows}) != expected:
        raise RuntimeError("duplicate/missing matrix keys")

    all_valid = all(r["valid"] for r in rows)
    exact_sep = all(
        (r["rr_zero"] and r["lane_class"] in ("ORDERED_RESIDUE_DATA_IDENTICAL", "GEOMETRY_DIFFERS_BUT_SUM_CANCELS"))
        or ((not r["rr_zero"]) and r["lane_class"] == "GEOMETRY_DIFFERS_AND_SUM_DIFFERS")
        for r in rows
    )
    cancellation_subset = any(r["lane_class"] == "GEOMETRY_DIFFERS_BUT_SUM_CANCELS" for r in rows)

    if not all_valid:
        classification = "ITER051_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif exact_sep:
        classification = "K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION"
    else:
        classification = "ITER051_CONTROL_OR_RECONSTRUCTION_INVALID"

    classes = (
        "ORDERED_RESIDUE_DATA_IDENTICAL",
        "GEOMETRY_DIFFERS_BUT_SUM_CANCELS",
        "GEOMETRY_DIFFERS_AND_SUM_DIFFERS",
        "ITER051_INTERNAL_INCONSISTENCY",
    )
    return {
        "iteration": "Iter051",
        "lane_count": len(rows),
        "classification": classification,
        "cancellation_dominated_subset": bool(cancellation_subset),
        "additional_structural_flag": "K4_RR_CANCELLATION_DOMINATED_SUBSET" if cancellation_subset else None,
        "all_valid": bool(all_valid),
        "rr_nonzero_count": sum(not r["rr_zero"] for r in rows),
        "class_counts": {c: sum(r["lane_class"] == c for r in rows) for c in classes},
        "by_condition": {
            c: {
                "rr_nonzero": sum((not r["rr_zero"]) for r in rows if r["condition"] == c),
                "class_counts": {cl: sum(r["condition"] == c and r["lane_class"] == cl for r in rows) for cl in classes},
            }
            for c in CONDITIONS
        },
        "claim_lock": "Localization only inside unchanged sequential K4 FP algebra; no physical multivariate extension, K5, G3, F9 or G8 promotion.",
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
        vals = (args.condition,args.gamma,args.epsilon,args.signs,args.k,args.tree,args.pair)
        if any(v is None for v in vals):
            raise SystemExit("compute mode requires full lane parameters")
        out = compute(args)
    else:
        out = aggregate(Path(args.input_dir))
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
