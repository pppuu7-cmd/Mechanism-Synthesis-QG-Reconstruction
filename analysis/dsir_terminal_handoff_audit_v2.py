#!/usr/bin/env python3
"""Parser-only repair for DSIR terminal handoff lane T.

Scientific predicates are unchanged from prereg/DSIR_TERMINAL_HANDOFF_RST.md.
The only repair is matching the literal Markdown emphasis in
`docs/LITERATURE_GAP_F9.md`: `**not** a proof of global novelty`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import dsir_terminal_handoff_audit as base


def lane_t_fixed():
    checks = {
        "carc_physical_open": base.contains(
            "bridges/M02_M04_M05_M07_CAUSAL_ANALYTIC_RG.md",
            "SYNTHESIS_DERIVED_CONSTRAINT / PHYSICAL_REALIZATION_OPEN",
            "Causal Analyticity–RG Commutator",
            "repeat over more than one blocking/refinement step",
        ),
        "cci_physical_target": base.contains(
            "bridges/M02_M04_M05_M07_CAUSAL_CYLINDRICAL_INTERTWINING.md",
            "SYNTHESIS_DERIVED_FINITE_SCALE_CONSTRAINT / PHYSICAL_REALIZATION_OPEN",
            "P_b'^± iota_b'b = iota_b'b P_b^±",
            "closure of the Toller analytic/pole class",
        ),
        "f9_current_blocked": base.contains(
            "status/CURRENT.md",
            "Physical F9: `BLOCKED`",
        ),
        "literature_gap_not_novelty": base.contains(
            "docs/LITERATURE_GAP_F9.md",
            "**not** a proof of global novelty",
            "did not surface a paper explicitly proving",
        ),
    }
    missing = {k: v[1] for k, v in checks.items() if not v[0]}
    passed = not missing
    return {
        "lane": "T",
        "pass": passed,
        "terminal_status": "BLOCKED_TRANSFER_TO_POLYGON" if passed else None,
        "missing_object": "PHYSICAL_MULTISCALE_CCI_REALIZATION" if passed else None,
        "scientific_gate_promoted": False,
        "checks": {k: v[0] for k, v in checks.items()},
        "missing_evidence_strings": missing,
        "polygon_test": [
            "define physical H_b and P_b^+-",
            "derive rather than fit embedding/coarse-graining maps iota_b'b",
            "test cylindrical consistency over multiple refinements",
            "test P_b'^+- iota_b'b - iota_b'b P_b^+- = 0",
            "test closure of Toller analytic/pole class without new cross-branch data",
        ],
        "repair_scope": "markdown evidence matcher only",
    }


LANES = {
    "R": base.lane_r,
    "S": base.lane_s,
    "T": lane_t_fixed,
    "U": base.lane_u,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    args = ap.parse_args()
    if args.aggregate_dir:
        raise SystemExit(base.aggregate(args.aggregate_dir))
    if not args.lane:
        ap.error("provide --lane or --aggregate-dir")
    result = LANES[args.lane]()
    base.write_lane(args.lane, result)
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
