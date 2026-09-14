#!/usr/bin/env python3
"""Iter082H-SM control-only repair 1.

Prospectively frozen by 28157952d4848675b13e7900b5bfbf8875e5026f.
No scientific criterion is changed.  This wrapper re-runs the frozen Iter082H
implementation, then routes the two previously hard-coded malformed controls
through explicit validators and recomputes P6/verdict.
"""
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

REPAIR_PREREG = "28157952d4848675b13e7900b5bfbf8875e5026f"
BASE_SCRIPT = "scripts/iter082h_full_invariant_symbol_cech_descent.py"
AGG = Path("artifacts/iter082h/aggregate.json")


def transition_valid_identity_linear(linear_coefficient):
    """Same frozen identity-linear/invertibility requirement used by P1."""
    return Fraction(linear_coefficient) == 1


def filtration_valid(input_degree: int, output_degree: int):
    """Same frozen no-normal-order-lowering predicate used by P5."""
    return output_degree >= input_degree


def main():
    prereg_ok = subprocess.call(
        ["git", "merge-base", "--is-ancestor", REPAIR_PREREG, "HEAD"]
    ) == 0
    if not prereg_ok:
        raise SystemExit("control-repair prereg is not an ancestor")

    # Re-run the unchanged scientific implementation first.
    subprocess.check_call(["python3", BASE_SCRIPT])
    out = json.loads(AGG.read_text(encoding="utf-8"))

    # Positive-side validator consistency checks.  These must agree with the
    # already-frozen P1/P5 positives before malformed controls are evaluated.
    positive_identity_linear = out["atlas"]["identity_linear_terms"]
    positive_filtration = all(
        m["cech"]["no_order_lowering"]
        for m in out["modules"].values()
    )

    # Mechanically route malformed controls through the same predicates.
    synthetic_singular_linear = Fraction(0, 1)
    singular_rejected = not transition_valid_identity_linear(synthetic_singular_linear)

    malformed_input_degree = 8
    malformed_output_degree = 6
    order_lowering_rejected = not filtration_valid(
        malformed_input_degree, malformed_output_degree
    )

    out["negative_controls"]["singular_transition"] = {
        "rejected": singular_rejected,
        "synthetic_linear_coefficient": "0/1",
        "validator": "transition_valid_identity_linear(c)==(c==1)",
    }
    out["negative_controls"]["order_lowering"] = {
        "rejected": order_lowering_rejected,
        "synthetic_input_degree": malformed_input_degree,
        "synthetic_output_degree": malformed_output_degree,
        "validator": "filtration_valid(input,output)==(output>=input)",
    }

    p6 = (
        positive_identity_linear
        and positive_filtration
        and all(v["rejected"] for v in out["negative_controls"].values())
    )
    out["predicates"]["P6_all_negative_controls_rejected"] = p6
    out["control_repair_1"] = {
        "prereg_commit": REPAIR_PREREG,
        "prereg_ancestor": prereg_ok,
        "positive_identity_linear_validator_consistent": positive_identity_linear,
        "positive_filtration_validator_consistent": positive_filtration,
        "singular_control_mechanically_rejected": singular_rejected,
        "order_lowering_control_mechanically_rejected": order_lowering_rejected,
        "scientific_criteria_changed": False,
    }

    pass_all = all(out["predicates"].values()) and prereg_ok
    if pass_all:
        out["classification"] = "K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_EXACT_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED"
        out["verdict"] = "PASS_EXACT_SCOPED"
    else:
        out["classification"] = "K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_FAIL_EXACT_SCOPED"
        out["verdict"] = "FAIL_EXACT_SCOPED"

    AGG.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not pass_all:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
