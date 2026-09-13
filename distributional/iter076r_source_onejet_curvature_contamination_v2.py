#!/usr/bin/env python3
"""Parser-only repair for Iter076R lane D.

Scientific predicates are unchanged from
prereg/ITER076R_SOURCE_ONEJET_CURVATURE_CONTAMINATION.md.
The only repair is matching the literal Markdown emphasis in Iter076D:
`does **not** establish the source-to-K4 pushforward`.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter076r_source_onejet_curvature_contamination as base


def lane_d_fixed():
    d_checks = base.require(
        "status/ITERATION_076D_RESULT.md",
        [
            "odd terms vanish",
            "does **not** establish the source-to-K4 pushforward",
        ],
    )
    p_checks = base.require(
        "status/CURRENT.md",
        [
            "EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED",
            "known exact Toller complex-conjugation branch flip exits the source causal K5 image",
            "nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`",
        ],
    )
    q_checks = base.require(
        "results/ITER076Q_HODGE_LINE_SYM2_QUADRATIC_DESCENT_RESULT.md",
        [
            "ITER076Q_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED",
            "source numerator/density has a nonzero one-jet",
        ],
    )
    all_evidence = all(d_checks.values()) and all(p_checks.values()) and all(q_checks.values())
    locks = {
        "full_toller_intertwiner_numerator_onejet_established_zero": False,
        "physical_source_to_k4_nonlinear_curvature_established": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "physical_finiteness_or_divergence_theorem": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = all_evidence and not any(locks.values())
    return {
        "iteration": "Iter076R",
        "lane": "D",
        "valid": bool(valid),
        "evidence": {
            "iter076d": d_checks,
            "iter076p_current": p_checks,
            "iter076q": q_checks,
        },
        "scope_locks": locks,
        "repair_scope": "Markdown evidence matcher only",
        "scientific_statement": (
            "Haar one-jet vanishing does not imply vanishing of the full Toller/intertwiner numerator one-jet; "
            "known Toller conjugation is not a same-causal evenness symmetry, and the physical nonlinear pushforward remains unbuilt."
        ),
    }


LANES = {"A": base.lane_a, "B": base.lane_b, "C": base.lane_c, "D": lane_d_fixed}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else base.aggregate(args.aggregate_dir)
    base.write(obj, args.output)
    print(__import__("json").dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
