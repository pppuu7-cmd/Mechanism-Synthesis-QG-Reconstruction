#!/usr/bin/env python3
"""Adversarial exact control for Iter078J-RG null directions.

Checks whether the exact primitive null vectors reported by Iter078J lie in
the invariant subspace of the fixed-causal label stabilizer S_p x S_(5-p),
using the exact 32x32 boundary action independently constructed for the
Iter078E critic audit.

Retrospective reviewer control only; no competing scientific gate.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "distributional" / "iter078e_critic_boundary_stabilizer.py"
spec = importlib.util.spec_from_file_location("stab", BASE)
stab = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(stab)

N_EPRL = (
    3,-3,-3,-9,0,2,-10,0,-6,0,-12,2,-1,1,1,3,
    -6,6,6,2,-3,1,1,-11,-3,1,1,-11,0,-8,-8,0,
)
N_UNIT = (
    1,-1,-1,-3,0,0,-4,0,-2,0,-4,2,-1,1,1,3,
    -2,2,2,2,-1,1,1,-5,-1,1,1,-5,0,-2,-2,0,
)


def matvec(m, v):
    return [sum(m[i][j] * Fraction(v[j]) for j in range(32)) for i in range(32)]


def analyze(vec, p_count):
    gens = stab.stabilizer_generators(p_count)
    residuals = []
    invariant = True
    for perm in gens:
        pv = matvec(stab.global_action(perm), vec)
        res = [pv[i] - vec[i] for i in range(32)]
        nz = [i for i, x in enumerate(res) if x]
        residuals.append({
            "permutation_old_to_new": list(perm),
            "nonzero_residual_count": len(nz),
            "first_nonzero_residual_index": nz[0] if nz else None,
            "first_nonzero_residual": str(res[nz[0]]) if nz else None,
        })
        invariant = invariant and not nz
    return {
        "p_count": p_count,
        "stabilizer": f"S_{p_count} x S_{5-p_count}",
        "generator_count": len(gens),
        "is_invariant": invariant,
        "generator_residuals": residuals,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, choices=range(6), required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = {
        "iteration": "Iter078J-RG critic null-stabilizer audit",
        "p_count": args.p,
        "eprl_null": analyze(N_EPRL, args.p),
        "unit_null": analyze(N_UNIT, args.p),
        "status": "RETROSPECTIVE_ADVERSARIAL_EXACT_CONTROL",
        "interpretation": "CI success certifies execution only; scientific scope is assigned by the critic review.",
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
