#!/usr/bin/env python3
"""Iter077I-SM: source-ordered all-j=1/2 Toller-function K5 local L1 audit.

Frozen by prereg/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1.md.
All zero/nonzero decisions use exact Gaussian-integer arithmetic.
Scientific FAIL is valid output; only missing object/source provenance is BLOCKED.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = list(itertools.combinations(range(5), 2))
X = {
    0: (0, 0, 0),
    1: (1, 2, 3),
    2: (2, 3, 5),
    3: (3, 5, 7),
    4: (5, 7, 11),
}
NEIGHBORS = {a: [b for b in range(5) if b != a] for a in range(5)}
LEG_POS = {(a, b): NEIGHBORS[a].index(b) for a in range(5) for b in NEIGHBORS[a]}

# Ascending magnetic basis (-1/2,+1/2), encoded as bits 0,1.
# Every node tensor is stripped only by a common nonzero normalization.
NODE_OPTIONS = {
    0: [
        ((0, 1, 0, 1), +1),
        ((0, 1, 1, 0), -1),
        ((1, 0, 0, 1), -1),
        ((1, 0, 1, 0), +1),
    ],
    1: [
        ((0, 0, 1, 1), +2),
        ((0, 1, 0, 1), -1),
        ((0, 1, 1, 0), -1),
        ((1, 0, 0, 1), -1),
        ((1, 0, 1, 0), -1),
        ((1, 1, 0, 0), +2),
    ],
}


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gscale(s, z):
    return (s * z[0], s * z[1])


def relative_vector(a, b):
    return tuple(X[a][i] - X[b][i] for i in range(3))


def leading_matrix(v):
    """Exact Gaussian-integer zero/nonzero-equivalent C(v) matrix."""
    vx, vy, vz = v
    return [
        [(vz, 0), (-vx, -vy)],
        [(-vx, +vy), (-vz, 0)],
    ]


EDGE_MATRICES = {e: leading_matrix(relative_vector(*e)) for e in EDGES}


def contract_boundary(ks, edge_signs=None):
    """Exact stripped K5 contraction for one five-node boundary basis component."""
    total = (0, 0)
    options = [NODE_OPTIONS[k] for k in ks]
    for choices in itertools.product(*options):
        states = []
        coeff = 1
        for state, c in choices:
            states.append(state)
            coeff *= c
        z = (coeff, 0)
        for a, b in EDGES:
            row = states[b][LEG_POS[(b, a)]]
            col = states[a][LEG_POS[(a, b)]]
            entry = EDGE_MATRICES[(a, b)][row][col]
            if edge_signs is not None:
                entry = gscale(edge_signs[(a, b)], entry)
            z = gmul(z, entry)
            if z == (0, 0):
                break
        total = gadd(total, z)
    return total


def exact_full32():
    out = []
    for ks in itertools.product((0, 1), repeat=5):
        value = contract_boundary(ks)
        out.append({
            "boundary_k": list(ks),
            "scaled_gaussian_integer": [value[0], value[1]],
            "nonzero": value != (0, 0),
        })
    canonical = json.dumps(out, sort_keys=True, separators=(",", ":"))
    checksum = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return out, checksum


def lane_a():
    source = (ROOT / "sources" / "ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1.md").read_text(encoding="utf-8")
    hres = (ROOT / "results" / "ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md").read_text(encoding="utf-8")

    squared_lengths = {f"{a}{b}": sum(x * x for x in relative_vector(a, b)) for a, b in EDGES}
    all_nonzero = all(v > 0 for v in squared_lengths.values())

    gamma = Fraction(6, 5)
    scalar = Fraction(2, 1) / (1 + gamma * gamma)
    expected_scalar = Fraction(50, 61)

    locks = {
        "source_vertex_ten_toller": "product of ten Toller matrices" in source,
        "source_toller_functions": "polynomially bounded **functions**" in source,
        "unique_feynman_projector": "uniquely projects the two Toller branches" in source,
        "source_ordering": "one-wedge source construction -> Toller function -> K5 product -> group integration" in source,
        "jhalf_beta_minus2": "beta^(-2)" in source,
        "leading_diag_shape": "diag(1,-1)" in source,
        "branch_sign_flip": "changes the common leading scale by a minus sign" in source,
        "finite_epsilon_termwise_cure_already_excluded": "FINITE_SPECTRAL_EPSILON" in hres,
        "no_termwise_contact_import": "does **not** multiply the ten spinor-contact distributions termwise" in prereg,
        "frozen_ray_all_edges_nonzero": all_nonzero,
        "gamma_control_scalar_exact": scalar == expected_scalar,
    }
    valid = bool(all(locks.values()))
    return {
        "iteration": "Iter077I-SM",
        "lane": "A",
        "valid": valid,
        "scientific_outcome": "PASS" if valid else "BLOCKED",
        "source_locks": locks,
        "frozen_ray_squared_edge_lengths": squared_lengths,
        "gamma_control": "6/5",
        "leading_common_scalar_2_over_1_plus_gamma2": f"{scalar.numerator}/{scalar.denominator}",
        "wedge_radial_power": -2,
    }


def lane_b():
    rows, checksum = exact_full32()
    nonzero = sum(int(r["nonzero"]) for r in rows)
    passed = nonzero == 32
    return {
        "iteration": "Iter077I-SM",
        "lane": "B",
        "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "boundary_components_checked": 32,
        "nonzero_components": nonzero,
        "zero_components": 32 - nonzero,
        "all_32_nonzero": passed,
        "sha256_exact_rows": checksum,
        "rows": rows,
    }


def causal_signs(sigmas):
    return {(a, b): sigmas[a] * sigmas[b] for a, b in EDGES}


def lane_c():
    base_rows, _ = exact_full32()
    base = {tuple(r["boundary_k"]): tuple(r["scaled_gaussian_integer"]) for r in base_rows}
    rows = []
    all_nonzero = True
    all_equal = True
    for tail in itertools.product((-1, 1), repeat=4):
        sigmas = (1,) + tail
        signs = causal_signs(sigmas)
        product_kappa = 1
        for e in EDGES:
            product_kappa *= signs[e]
        for ks in itertools.product((0, 1), repeat=5):
            value = contract_boundary(ks, signs)
            same = value == base[ks]
            nz = value != (0, 0)
            all_nonzero &= nz
            all_equal &= same
            rows.append({
                "sigma": list(sigmas),
                "boundary_k": list(ks),
                "product_kappa": product_kappa,
                "scaled_gaussian_integer": [value[0], value[1]],
                "nonzero": nz,
                "equals_allplus": same,
            })
    passed = bool(len(rows) == 512 and all_nonzero and all_equal and all(r["product_kappa"] == 1 for r in rows))
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "iteration": "Iter077I-SM",
        "lane": "C",
        "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "factorized_causal_assignments": 16,
        "boundary_components": 32,
        "contractions_checked": len(rows),
        "all_nonzero": bool(all_nonzero),
        "all_equal_to_allplus": bool(all_equal),
        "all_product_kappa_plus_one": all(r["product_kappa"] == 1 for r in rows),
        "sha256_exact_rows": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "rows": rows,
    }


def lane_d():
    full32, _ = exact_full32()
    nonzero = sum(int(r["nonzero"]) for r in full32)
    wedges = 10
    wedge_power = -2
    q = wedges * wedge_power
    d = 12
    margin = q + d
    radial_exponent = d - 1 + q
    passed = bool(nonzero == 32 and q == -20 and d == 12 and margin == -8 and radial_exponent == -9 and radial_exponent <= -1)
    return {
        "iteration": "Iter077I-SM",
        "lane": "D",
        "valid": True,
        "scientific_outcome": "PASS" if passed else "FAIL",
        "nonzero_boundary_components": nonzero,
        "wedge_count": wedges,
        "per_wedge_power": wedge_power,
        "total_integrand_power_q": q,
        "transverse_boost_dimension_d": d,
        "first_moment_margin_q_plus_d": margin,
        "radial_measure_power_d_minus_1": d - 1,
        "absolute_radial_integrand_exponent": radial_exponent,
        "local_absolute_L1": False if passed else None,
        "open_angular_neighborhood_reason": "the exact leading contraction is analytic in nonzero edge-direction data and is nonzero at the frozen witness",
        "distributional_or_conditional_boundary_value_tested": False,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter077I-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj

    present = set(got) == set(LANES)
    if not present or not got.get("A", {}).get("valid", False):
        return {
            "iteration": "Iter077I-SM",
            "execution_valid": False,
            "verdict": "BLOCKED",
            "classification": "ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_BLOCKED_OBJECT_DEFINITION",
            "lanes_found": sorted(got),
        }

    execution_valid = all(bool(got[k].get("valid")) for k in LANES)
    outcomes = {k: got[k].get("scientific_outcome") for k in LANES}
    if execution_valid and all(v == "PASS" for v in outcomes.values()):
        verdict = "PASS"
        classification = "ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED"
    elif execution_valid:
        verdict = "FAIL"
        classification = "ITER077I_SM_SOURCE_ORDERED_JHALF_K5_FULL32_L1_PREDICTION_FAILS_EXACT_SCOPED"
    else:
        verdict = "BLOCKED"
        classification = "ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_BLOCKED_OBJECT_DEFINITION"

    return {
        "iteration": "Iter077I-SM",
        "execution_valid": execution_valid,
        "verdict": verdict,
        "classification": classification,
        "lane_scientific_outcomes": outcomes,
        "full32_nonzero": got.get("B", {}).get("nonzero_components"),
        "causal_contractions_checked": got.get("C", {}).get("contractions_checked"),
        "all_factorized_causal_leading_coefficients_equal": got.get("C", {}).get("all_equal_to_allplus"),
        "total_power_q": got.get("D", {}).get("total_integrand_power_q"),
        "transverse_dimension_d": got.get("D", {}).get("transverse_boost_dimension_d"),
        "first_moment_margin_q_plus_d": got.get("D", {}).get("first_moment_margin_q_plus_d"),
        "radial_absolute_exponent": got.get("D", {}).get("absolute_radial_integrand_exponent"),
        "next_admissible_gate": "Test the source-selected correlated/conditional common-collision group boundary value for the complete 32-component source-ordered Toller-function K5 object, including exact smooth subleading phase/measure/intertwiner data; do not infer full vertex divergence from L1 failure alone.",
        "claim_lock": "No full causal-vertex divergence/nonexistence theorem, conditional boundary-value theorem, regulator-independence theorem, causal-sector-sum theorem, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, G3/F9/G8/K5 promotion, new physics, or complete QG.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")

    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))

    # Scientific FAIL is valid; only source/object BLOCKED fails infrastructure.
    if args.lane:
        if not obj.get("valid", False):
            raise SystemExit(1)
    elif not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
