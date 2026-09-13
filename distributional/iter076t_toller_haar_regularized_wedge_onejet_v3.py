#!/usr/bin/env python3
"""Authoritative evidence-path repair for Iter076T.

Frozen mathematics from the preregistration is unchanged. Lane D now reads the
administratively renumbered authoritative Iter076S face-contamination result.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter076t_toller_haar_regularized_wedge_onejet as base
import iter076t_toller_haar_regularized_wedge_onejet_v2 as v2

ROOT = Path(__file__).resolve().parents[1]


def lane_d_fixed():
    snapshot = (ROOT / "sources/CAUSAL_VERTEX_TOLLER_ONEJET_SOURCE_SNAPSHOT.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg/ITER076T_TOLLER_HAAR_REGULARIZED_WEDGE_ONEJET.md").read_text(encoding="utf-8")
    sres = (ROOT / "results/ITER076S_QUADRATIC_CURVATURE_ONEJET_FACE_CONTAMINATION_RESULT.md").read_text(encoding="utf-8")
    evidence = {
        "source_full_vertex_scope_guard": "fully contracted/integrated causal vertex" in snapshot,
        "source_contact_vs_bulk_split": "theta(sigma B) + sigma delta^(rho,j)(B)" in snapshot,
        "curvature_contamination_prior": "one-jet cannot be bypassed by symmetry" in sres,
        "authoritative_iter076s_classification": "ITER076S_UNIQUE_TWISTED_QUADRATIC_CURVATURE_ALLOWS_ONEJET_CONTAMINATION_ON_TRANSITIVE_FACES_EXACT_SCOPED" in sres,
        "full_vertex_nonzero_not_claimed": "does not prove that the fully contracted or integrated vertex one-jet is nonzero" in prereg,
        "epsilon_minus1_not_emitted": "no nominal `epsilon^-1` coefficient" in prereg,
    }
    locks = {
        "full_contracted_vertex_onejet_established_nonzero": False,
        "full_contracted_vertex_onejet_established_zero": False,
        "physical_nonlinear_pushforward_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_p3_promoted": False,
        "physical_finiteness_or_divergence_theorem": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = all(evidence.values()) and not any(locks.values())
    return {
        "iteration": "Iter076T",
        "lane": "D",
        "valid": bool(valid),
        "evidence": evidence,
        "scope_locks": locks,
        "repair_scope": "authoritative Iter076S evidence path only",
        "next_missing_object": "FULL_TOLLER_INTERTWINER_CONTRACTED_NUMERATOR_ONEJET",
        "interpretation": "A nonzero local magnetic-component Toller/Haar one-jet witness defeats universal local-zero claims but does not decide cancellations in the full contracted/integrated vertex.",
    }


LANES = {"A": v2.lane_a_fixed, "B": base.lane_b, "C": base.lane_c, "D": lane_d_fixed}


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
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
