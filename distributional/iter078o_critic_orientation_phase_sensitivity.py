#!/usr/bin/env python3
"""Adversarial phase-character sensitivity control for Iter078O-RG.

Frozen by prereg/ITER078O_CRITIC_ORIENTATION_PHASE_SENSITIVITY.md before execution.
Uses only exact character data of the already-frozen Iter078O representation.
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "distributional" / "iter078o_rg_causal_stabilizer_symmetry.py"
spec = importlib.util.spec_from_file_location("iter078o_base", BASE)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)


def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            inv += int(p[i] > p[j])
    return -1 if inv % 2 else 1


def integer_character_average(sig):
    G = base.stabilizer(sig)
    triv = base.Z
    sign = base.Z
    odd = 0
    even = 0
    for p in G:
        tr = base.trace(base.global_matrix(p))
        triv = base.fadd(triv, tr)
        s = parity(p)
        sign = base.fadd(sign, base.fscale(Fraction(s), tr))
        if s == 1:
            even += 1
        else:
            odd += 1
    triv = base.fscale(Fraction(1, len(G)), triv)
    sign = base.fscale(Fraction(1, len(G)), sign)
    valid = (
        triv[1] == 0 and sign[1] == 0 and
        triv[0].denominator == 1 and sign[0].denominator == 1
    )
    return {
        "stabilizer_size": len(G),
        "even_elements": even,
        "odd_elements": odd,
        "original_fixed_dimension": int(triv[0]) if valid else None,
        "parity_twisted_fixed_dimension": int(sign[0]) if valid else None,
        "different": bool(valid and triv != sign),
        "valid": valid,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    classes = {
        "0<->5": (-1,-1,-1,-1,-1),
        "1<->4": (-1,1,1,1,1),
        "2<->3": (-1,-1,1,1,1),
    }
    results = {k: integer_character_average(v) for k,v in classes.items()}
    valid = all(r["valid"] for r in results.values())
    changed = [k for k,r in results.items() if r["different"]]
    expected_original = {"0<->5":2,"1<->4":3,"2<->3":5}
    originals_match = all(results[k]["original_fixed_dimension"] == expected_original[k] for k in classes)
    valid = valid and originals_match

    if valid and changed:
        verdict = "PASS"
        classification = "ITER078O_CRITIC_FIXED_SUBSPACE_COUNTS_PHASE_CHARACTER_SENSITIVE_CONTROL_SCOPED"
    elif valid:
        verdict = "FAIL"
        classification = "ITER078O_CRITIC_PARITY_PHASE_TWIST_DOES_NOT_CHANGE_FROZEN_FIXED_COUNTS"
    else:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ITER078O_CRITIC_PHASE_SENSITIVITY_INVALID_IMPLEMENTATION"

    obj = {
        "reviewed_iteration": "Iter078O-RG",
        "execution_valid": valid,
        "verdict": verdict,
        "classification": classification,
        "classes": results,
        "classes_with_changed_fixed_dimension": changed,
        "original_dimensions_match_terminal_result": originals_match,
        "interpretation": "The parity twist is an adversarial representation-level phase-character control, not asserted to be the physical causal action. A changed count proves convention sensitivity of absolute fixed-space dimensions absent an independently fixed physical orientation/duality phase convention.",
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not valid:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
