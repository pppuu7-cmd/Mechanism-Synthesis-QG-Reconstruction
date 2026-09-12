#!/usr/bin/env python3
"""Iter048: decompose the frozen K4 FP commutator into R/A channels.

The one-dimensional finite-part functional is not changed:
    FP_u = R_u + A_u
with R the upper-half-plane residue term of the proper rational remainder and
A = -i*pi*a_-1.  The discarded polynomial quotient is metadata only.
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

PAIRS = ("01", "02", "12")
CHANNELS = ("RR", "RA", "AR", "AA")


def is_zero(expr):
    return sp.cancel(expr) == 0


def exact_equal(a, b):
    return is_zero(sp.cancel(a - b))


def degree_pair(expr, var):
    expr = sp.cancel(expr)
    if is_zero(expr):
        return [-1, 0]
    num, den = sp.fraction(expr)
    return [
        int(sp.Poly(num, var, domain="EX").degree()),
        int(sp.Poly(den, var, domain="EX").degree()),
    ]


def fp_components_1d(expr, var):
    """Exact R/A split of the unchanged finite_part_1d functional."""
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
        raise RuntimeError(
            f"improper remainder after division: deg(num)={dn}, deg(den)={dd}"
        )

    roots = _linear_roots_of_denominator(Prd.as_expr(), var)
    Dprime = sp.diff(Prd.as_expr(), var)
    Nexpr = Prn.as_expr()
    residue_sum = sp.Integer(0)
    upper_count = 0
    for root, imr in roots:
        sign = float(sp.N(imr, 30))
        if abs(sign) < 1e-14:
            raise RuntimeError(f"unexpected real-axis pole: {root}")
        if sign > 0:
            residue_sum += sp.cancel(Nexpr.subs(var, root) / Dprime.subs(var, root))
            upper_count += 1

    Rcomp = sp.cancel(2 * sp.pi * sp.I * residue_sum)
    Acomp = sp.cancel(-sp.pi * sp.I * a_minus1)
    full = sp.cancel(Rcomp + Acomp)
    frozen, frozen_meta = finite_part_1d(expr, var)
    matches_frozen = exact_equal(full, frozen)

    qdeg = -1 if Q.is_zero else int(Q.degree())
    return {
        "R": Rcomp,
        "A": Acomp,
        "full": full,
        "matches_frozen": bool(matches_frozen),
        "meta": {
            "quotient_degree": qdeg,
            "quotient_nonzero": not Q.is_zero,
            "a_minus1_zero": bool(is_zero(a_minus1)),
            "upper_pole_count": upper_count,
            "pole_count": len(roots),
            "frozen_meta": frozen_meta,
        },
    }


def ordered_channels(expr, y, first: int, second: int):
    first_split = fp_components_1d(expr, y[first])
    from_R = fp_components_1d(first_split["R"], y[second])
    from_A = fp_components_1d(first_split["A"], y[second])

    channels = {
        "RR": sp.cancel(from_R["R"]),
        "RA": sp.cancel(from_R["A"]),
        "AR": sp.cancel(from_A["R"]),
        "AA": sp.cancel(from_A["A"]),
    }
    channel_sum = sp.cancel(sum(channels.values(), sp.Integer(0)))

    frozen_first, _ = finite_part_1d(expr, y[first])
    frozen_ordered, _ = finite_part_1d(frozen_first, y[second])
    ordered_reconstruction = exact_equal(channel_sum, frozen_ordered)

    all_component_matches = all([
        first_split["matches_frozen"],
        from_R["matches_frozen"],
        from_A["matches_frozen"],
    ])
    return {
        "channels": channels,
        "sum": channel_sum,
        "frozen_ordered": sp.cancel(frozen_ordered),
        "ordered_reconstruction": bool(ordered_reconstruction),
        "all_component_matches": bool(all_component_matches),
        "first_meta": first_split["meta"],
        "second_from_R_meta": from_R["meta"],
        "second_from_A_meta": from_A["meta"],
    }


def decompose_commutator(gamma, epsilon, signs, k, tree, pair, control=False):
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

    remaining = next(idx for idx in range(3) if idx not in (i, j))
    var = y[remaining]
    channel_rows = {}
    for ch in CHANNELS:
        channel_rows[ch] = {
            "zero": bool(is_zero(deltas[ch])),
            "difference_exact": str(deltas[ch]),
            "degree": degree_pair(deltas[ch], var),
        }

    valid = all([
        ij["ordered_reconstruction"], ji["ordered_reconstruction"],
        ij["all_component_matches"], ji["all_component_matches"],
        total_reconstruction,
    ])
    return {
        "valid": bool(valid),
        "total_zero": bool(is_zero(total)),
        "total_exact": str(total),
        "total_degree": degree_pair(total, var),
        "remaining_coordinate": remaining,
        "channels": channel_rows,
        "channel_reconstruction_exact": bool(total_reconstruction),
        "ordered_ij_reconstruction_exact": ij["ordered_reconstruction"],
        "ordered_ji_reconstruction_exact": ji["ordered_reconstruction"],
        "all_one_step_component_recombinations_exact": bool(
            ij["all_component_matches"] and ji["all_component_matches"]
        ),
        "ij_first_meta": ij["first_meta"],
        "ji_first_meta": ji["first_meta"],
        "kernel_meta": kernel_meta,
    }


def lane_pattern(source):
    if source["total_zero"]:
        return "SOURCE_TOTAL_ZERO"
    rr = not source["channels"]["RR"]["zero"]
    a_nonzero = any(
        not source["channels"][ch]["zero"] for ch in ("RA", "AR", "AA")
    )
    if rr and a_nonzero:
        return "MIXED"
    if rr and not a_nonzero:
        return "RESIDUE_ONLY"
    if (not rr) and a_nonzero:
        return "INFINITY_ONLY"
    return "UNRESOLVED"


def compute(args):
    gamma = sp.Rational(args.gamma)
    epsilon = sp.Rational(args.epsilon)
    signs = parse_signs(args.signs)
    k = parse_k(args.k)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.pair not in PAIRS:
        raise ValueError(args.pair)

    source = decompose_commutator(
        gamma, epsilon, signs, k, args.tree, args.pair, control=False
    )
    control = decompose_commutator(
        gamma, epsilon, signs, k, args.tree, args.pair, control=True
    )
    valid = source["valid"] and control["valid"] and control["total_zero"]
    control_channel_cancellation = (
        control["total_zero"]
        and any(not control["channels"][ch]["zero"] for ch in CHANNELS)
    )
    return {
        "iteration": "Iter048",
        "case": args.case,
        "tree": args.tree,
        "pair": args.pair,
        "gamma": args.gamma,
        "epsilon": args.epsilon,
        "signs": args.signs,
        "k": list(map(str, k)),
        "valid": bool(valid),
        "source_pattern": lane_pattern(source),
        "control_channel_cancellation": bool(control_channel_cancellation),
        "source": source,
        "control": control,
        "claim_lock": (
            "Exact channel localization inside the unchanged sequential FP only; "
            "no new counterterm, preferred order, physical divergence, K5, G3, F9 or G8 claim."
        ),
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter048_*.json")):
        try:
            row = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if row.get("iteration") == "Iter048" and "source" in row:
            rows.append(row)
    if len(rows) != 24:
        raise RuntimeError(f"expected 24 Iter048 lanes, found {len(rows)}")
    keys = {(r["case"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != 24:
        raise RuntimeError("duplicate/missing Iter048 matrix keys")

    all_valid = all(r["valid"] for r in rows)
    source_all_nonzero = all(not r["source"]["total_zero"] for r in rows)
    patterns = [r["source_pattern"] for r in rows]

    if not all_valid:
        classification = "K4_FP_CHANNEL_DECOMPOSITION_INVALID"
    elif not source_all_nonzero:
        classification = "K4_FP_CHANNEL_DIAGNOSTIC_REVIEW"
    elif any(p == "MIXED" for p in patterns):
        classification = "K4_FP_OBSTRUCTION_MIXED_CHANNELS"
    elif all(p == "RESIDUE_ONLY" for p in patterns):
        classification = "K4_FP_OBSTRUCTION_RESIDUE_CHANNEL"
    elif all(p == "INFINITY_ONLY" for p in patterns):
        classification = "K4_FP_OBSTRUCTION_INFINITY_CHANNEL"
    else:
        classification = "K4_FP_CHANNEL_DIAGNOSTIC_REVIEW"

    def summarize(subset):
        counts = {
            ch: sum(not r["source"]["channels"][ch]["zero"] for r in subset)
            for ch in CHANNELS
        }
        return {
            "lane_count": len(subset),
            "valid_lane_count": sum(r["valid"] for r in subset),
            "nonzero_source_total_count": sum(not r["source"]["total_zero"] for r in subset),
            "source_channel_nonzero_counts": counts,
            "source_pattern_counts": {
                p: sum(r["source_pattern"] == p for r in subset)
                for p in ("RESIDUE_ONLY", "INFINITY_ONLY", "MIXED", "SOURCE_TOTAL_ZERO", "UNRESOLVED")
            },
            "control_total_zero_count": sum(r["control"]["total_zero"] for r in subset),
            "control_channel_cancellation_count": sum(r["control_channel_cancellation"] for r in subset),
            "all_channel_reconstructions_exact": all(
                r["source"]["channel_reconstruction_exact"]
                and r["control"]["channel_reconstruction_exact"]
                for r in subset
            ),
        }

    return {
        "iteration": "Iter048",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": all_valid,
        "all_source_totals_nonzero": source_all_nonzero,
        "all_control_totals_zero": all(r["control"]["total_zero"] for r in rows),
        "cases": {
            case: summarize([r for r in rows if r["case"] == case])
            for case in ("A", "B")
        },
        "overall": summarize(rows),
        "claim_lock": (
            "Channel decomposition of the frozen FP obstruction only. It does not define a physical "
            "multivariate amplitude or authorize K5/G3/F9/G8 promotion."
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
