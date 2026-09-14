#!/usr/bin/env python3
"""Iter081R-SM exact Molien/character count for corrected K5 invariant normal jets.

No floating eigenvalues or numerical group integration are used.  The normal
fiber is V = spin-1(SU2) tensor Std_5(S5), dimension 12.  We count
SO(3) x S5 singlets in Sym^k(V), k<=8, using exact truncated Laurent-series
arithmetic.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

KMAX = 8
S5_ORDER = math.factorial(5)
PREREG = "18945b681978cf22a8253a6489034e68a1cae372"

# Seven conjugacy cycle types of S5.
CYCLE_TYPES = [
    (1, 1, 1, 1, 1),
    (2, 1, 1, 1),
    (2, 2, 1),
    (3, 1, 1),
    (3, 2),
    (4, 1),
    (5,),
]


def class_size(cycles: tuple[int, ...]) -> int:
    counts = Counter(cycles)
    denom = 1
    for ell, mult in counts.items():
        denom *= (ell ** mult) * math.factorial(mult)
    return S5_ORDER // denom


# A truncated polynomial is dict[(t_degree, x_exponent)] = integer coefficient.
def mul_poly(a, b):
    out = defaultdict(int)
    for (ta, xa), ca in a.items():
        for (tb, xb), cb in b.items():
            if ta + tb <= KMAX:
                out[(ta + tb, xa + xb)] += ca * cb
    return {k: v for k, v in out.items() if v}


def numerator_factor(weight: int):
    # (1 - t x^weight)
    return {(0, 0): 1, (1, weight): -1}


def geometric_factor(cycle_len: int, weight: int):
    # 1 / (1 - (t x^weight)^cycle_len), truncated at t^KMAX.
    return {
        (cycle_len * n, weight * cycle_len * n): 1
        for n in range(KMAX // cycle_len + 1)
    }


def class_generating_polynomial(cycles: tuple[int, ...]):
    # For Std_5, det(1-s Std)=prod_cycles(1-s^ell)/(1-s), hence
    # 1/det(1-t x^w Std)=(1-t x^w)/prod_cycles(1-(t x^w)^ell).
    poly = {(0, 0): 1}
    for weight in (2, 0, -2):  # spin-1 SU2 torus weights
        poly = mul_poly(poly, numerator_factor(weight))
        for ell in cycles:
            poly = mul_poly(poly, geometric_factor(ell, weight))
    return poly


def su2_singlet_multiplicity(poly, degree: int) -> int:
    # All SU2 irreps here have integer spin.  Each spin J>=1 character contains
    # x^0 and x^2 once, whereas spin 0 contains x^0 but no x^2.  Therefore
    # mult(spin0) = coeff(x^0)-coeff(x^2).
    return poly.get((degree, 0), 0) - poly.get((degree, 2), 0)


def git(args):
    return subprocess.check_output(["git"] + args, text=True).strip()


def main():
    class_rows = []
    weighted = [0] * (KMAX + 1)
    sizes = []

    for cycles in CYCLE_TYPES:
        size = class_size(cycles)
        sizes.append(size)
        poly = class_generating_polynomial(cycles)
        multiplicities = [su2_singlet_multiplicity(poly, k) for k in range(KMAX + 1)]
        for k, m0 in enumerate(multiplicities):
            weighted[k] += size * m0
        class_rows.append({
            "cycle_type": list(cycles),
            "class_size": size,
            "su2_singlet_multiplicity_by_degree": multiplicities,
        })

    dims_fraction = [Fraction(v, S5_ORDER) for v in weighted]
    dims_integral = all(q.denominator == 1 for q in dims_fraction)
    dims = [q.numerator if q.denominator == 1 else f"{q.numerator}/{q.denominator}" for q in dims_fraction]

    # SO(3)-only negative control = identity S5 class before averaging.
    identity_row = next(r for r in class_rows if r["cycle_type"] == [1, 1, 1, 1, 1])
    so3_only = identity_row["su2_singlet_multiplicity_by_degree"]

    controls = {
        "seven_cycle_types": len(CYCLE_TYPES) == 7,
        "class_sizes_sum_120": sum(sizes) == S5_ORDER,
        "dimensions_integral": dims_integral,
        "dimensions_nonnegative": dims_integral and all(int(d) >= 0 for d in dims),
        "d0_eq_1": dims_integral and dims[0] == 1,
        "d1_eq_0": dims_integral and dims[1] == 0,
        "quadratic_invariant_exists": dims_integral and dims[2] >= 1,
        "laplacian_power_orders_exist": dims_integral and all(dims[k] >= 1 for k in (0, 2, 4, 6, 8)),
        "s5_projection_active": dims_integral and any(so3_only[k] != dims[k] for k in range(4, KMAX + 1)),
    }

    # Geometry lock: dimension spin1 * dimension Std_5 = 3*4=12 and allowed
    # derivative order is 20-12=8 from Iter077L.
    geometry = {
        "normal_fiber": "spin1_SU2 tensor Std5_S5",
        "normal_dimension": 3 * 4,
        "codimension_N": 12,
        "source_scaling_degree": 20,
        "max_normal_derivative_order": 20 - 12,
        "node_gauge_orbit": "SU2^5 / SU2_diag ~= SU2^4 = N",
    }
    geometry_valid = (
        geometry["normal_dimension"] == geometry["codimension_N"] == 12
        and geometry["max_normal_derivative_order"] == KMAX
    )

    prereg_ancestor = subprocess.call(["git", "merge-base", "--is-ancestor", PREREG, "HEAD"]) == 0
    all_controls = all(controls.values()) and geometry_valid and prereg_ancestor
    total_dim = sum(int(d) for d in dims) if dims_integral else None

    if all_controls and total_dim is not None and total_dim > 1:
        classification = "ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_NONTRIVIAL_EXACT_SCOPED"
        verdict = "PASS_EXACT_SCOPED"
    elif all_controls and total_dim == 1:
        classification = "ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_SCALAR_ONLY_EXACT_SCOPED"
        verdict = "PASS_EXACT_SCOPED"
    else:
        classification = "INVALID_IMPLEMENTATION_OR_GEOMETRIC_REPRESENTATION"
        verdict = "INVALID_IMPLEMENTATION_OR_GEOMETRIC_REPRESENTATION"

    out = {
        "iteration": "Iter081R-SM",
        "classification": classification,
        "verdict": verdict,
        "geometry": geometry,
        "degree_dimensions_d0_to_d8": dims,
        "total_scalar_invariant_jet_dimension_leq8": total_dim,
        "so3_only_negative_control_dimensions": so3_only,
        "s5_class_rows": class_rows,
        "controls": controls,
        "provenance": {
            "git_head": git(["rev-parse", "HEAD"]),
            "prereg_commit_expected": PREREG,
            "prereg_ancestor": prereg_ancestor,
        },
        "claim_locks": [
            "scalar invariant-jet lower bound only",
            "not full boundary-covariant extension-space dimension",
            "no unique selector",
            "no causal-vertex divergence/nonexistence",
            "no regulator independence",
            "no G3/F9/G8/K5 promotion",
            "no NEW_PHYSICS_FOUND",
        ],
    }

    outpath = Path(os.environ.get("ITER081R_OUT", "results/raw/iter081r_sm_invariant_jets.json"))
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))

    if verdict.startswith("INVALID"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
