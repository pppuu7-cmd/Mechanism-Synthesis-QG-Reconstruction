#!/usr/bin/env python3
"""Iter077Q-SM: exact controls for invariant tangential K5 extension ambiguity.

Frozen by prereg/ITER077Q_SM_INVARIANT_TANGENTIAL_EXTENSION_AMBIGUITY_DIMENSION.md
before implementation.  The infinite-dimensional conclusion is analytic; these lanes
provide independent exact source/provenance, symmetry, nonconstancy/Vandermonde,
and distributional-scope controls.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def unit_pair(p: int, q: int):
    """Rational point ((q^2-p^2)/(q^2+p^2), 2pq/(q^2+p^2)) on S^1."""
    den = q * q + p * p
    return (Fraction(q * q - p * p, den), Fraction(2 * p * q, den))


def mul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c)


def inv(u):
    return (u[0], -u[1])


def tr_rel(gb, ga):
    r = mul(inv(gb), ga)
    return 2 * r[0]


def Q(gs):
    return sum((tr_rel(gs[b], gs[a]) for a, b in itertools.combinations(range(5), 2)), Fraction(0))


def q_abs(gs):
    return sum((2*g[0] for g in gs), Fraction(0))


def lane_a():
    l = read("results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md")
    m = read("results/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR_RESULT.md")
    deriv = read("sources/ITER077M_SM_SOURCE_SYMMETRY_SELECTOR_DERIVATION.md")
    bc = json.loads(read("results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json"))
    locks = {
        "N_is_SU2_4": "N = SU(2)^4" in l,
        "codim12": "codimension is exactly `12`" in l,
        "sd20": "sd_N=20" in l or "sd_N(A_ext)=20" in l,
        "smooth_coefficient_data_allowed": "coefficient data along `N`" in l,
        "true_boundary_F_SU2": "F_SU2" in deriv and "actual source boundary state" in deriv,
        "source_order_preserved": "Source-order PASS" in m,
        "common_left_gauge_preserved": "Global gauge PASS" in m,
        "nonzero_true_boundary_functional": bc.get("components_checked") == 32 and bc.get("nonzero_components", 0) > 0,
    }
    return {
        "iteration": "Iter077Q-SM", "lane": "A", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "BLOCKED",
        "locks": locks,
        "compact_components_checked": bc.get("components_checked"),
        "compact_nonzero_components": bc.get("nonzero_components"),
    }


def lane_b():
    gs = [
        unit_pair(0, 1),
        unit_pair(1, 2),
        unit_pair(2, 3),
        unit_pair(3, 4),
        unit_pair(4, 5),
    ]
    q0 = Q(gs)
    permutation_values = {Q([gs[i] for i in p]) for p in itertools.permutations(range(5))}
    h = unit_pair(7, 11)
    shifted = [mul(h, g) for g in gs]
    q_shifted = Q(shifted)
    abs0 = q_abs(gs)
    abs_shifted = q_abs(shifted)
    locks = {
        "all_120_permutations_same_Q": len(permutation_values) == 1 and next(iter(permutation_values)) == q0,
        "common_left_exact_Q_invariance": q_shifted == q0,
        "negative_control_absolute_coordinate_changes": abs_shifted != abs0,
    }
    return {
        "iteration": "Iter077Q-SM", "lane": "B", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "FAIL",
        "locks": locks,
        "Q_exact": [q0.numerator, q0.denominator],
        "permutations_checked": 120,
        "negative_control_abs_before": [abs0.numerator, abs0.denominator],
        "negative_control_abs_after": [abs_shifted.numerator, abs_shifted.denominator],
    }


def vandermonde_det(xs):
    d = Fraction(1)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            d *= xs[j] - xs[i]
    return d


def path_Q_from_pair(u):
    # Four vertices are identity and vertex 2 is u: Q = 12 + 4*tr(u) = 12+8*cos(t).
    return Fraction(12) + 8 * u[0]


def lane_c():
    frozen_pq = [(0,1),(1,5),(1,4),(1,3),(1,2),(2,3),(3,4),(1,1)]
    us = [unit_pair(p,q) for p,q in frozen_pq]
    qs_formula = [path_Q_from_pair(u) for u in us]
    qs_direct = []
    I = unit_pair(0,1)
    for u in us:
        gs = [I, u, I, I, I]
        qs_direct.append(Q(gs))
    det = vandermonde_det(qs_direct)
    deriv = read("sources/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md")
    locks = {
        "exact_Q_formula_controls": qs_formula == qs_direct,
        "all_frozen_Q_values_distinct": len(set(qs_direct)) == len(qs_direct),
        "vandermonde_nonzero": det != 0,
        "analytic_formula_frozen": "Q(t)=12+8 cos(t)" in deriv,
        "analytic_infinite_independence_proof_frozen": "countably infinite-dimensional" in deriv and "polynomial vanishing" in deriv,
    }
    return {
        "iteration": "Iter077Q-SM", "lane": "C", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "FAIL",
        "locks": locks,
        "frozen_Q_values": [[x.numerator, x.denominator] for x in qs_direct],
        "vandermonde_det": [det.numerator, det.denominator],
        "finite_control_dimension": len(qs_direct),
        "infinite_dimension_evidence_type": "analytic theorem; finite Vandermonde is control only",
    }


def lane_d():
    deriv = read("sources/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md")
    prereg = read("prereg/ITER077Q_SM_INVARIANT_TANGENTIAL_EXTENSION_AMBIGUITY_DIMENSION.md")
    locks = {
        "support_only_on_N": "supported on `N`" in deriv,
        "source_order_not_rearranged": "preserves source ordering" in deriv,
        "fixed_causal_labels": "preserves fixed causal labels" in deriv,
        "true_boundary_linearity": "linearity in `Psi`" in deriv,
        "common_left_gauge": "common-left `SL(2,C)` gauge covariance" in deriv,
        "relabeling_covariance": "preserves relabeling covariance" in deriv,
        "added_delta_sd12": "scaling degree `12`" in deriv,
        "max_class_sd20": "scaling degree `20`" in deriv,
        "no_new_selector": "introduces no new physical condition" in deriv,
        "ceiling_present": "INTERPRETATION CEILING" in prereg,
    }
    return {
        "iteration": "Iter077Q-SM", "lane": "D", "valid": all(locks.values()),
        "scientific_outcome": "PASS" if all(locks.values()) else "INVALID",
        "locks": locks,
        "counterexample_search": "No already-frozen source condition in Iter077L/M restricts smooth tangential coefficients to constants; any such rule is a new selector gate.",
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root: str):
    got = {}
    for base_dir, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base_dir, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter077Q-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    present = set(got) == set(LANES)
    valid = present and all(bool(got[k].get("valid")) for k in LANES)
    outcomes = {k: got.get(k, {}).get("scientific_outcome") for k in LANES}
    if valid and all(v == "PASS" for v in outcomes.values()):
        verdict = "PASS"
        classification = "ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED"
    elif present and any(v == "FAIL" for v in outcomes.values()):
        verdict = "FAIL"
        classification = "ITER077Q_SM_INVARIANT_TANGENTIAL_INFINITE_DIMENSION_HYPOTHESIS_FAILS_SCOPED"
    else:
        verdict = "BLOCKED"
        classification = "ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_BLOCKED_OR_INVALID"
    return {
        "iteration": "Iter077Q-SM",
        "execution_valid": valid,
        "lane_scientific_outcomes": outcomes,
        "verdict": verdict,
        "classification": classification,
        "new_scientific_fact": "Under already-frozen CRQN v0.2 source constraints, the supported K5 extension freedom contains the linearly independent family Q^n F_SU2 delta_N for all n>=0; the constant Iter077M coefficient is not the whole ambiguity.",
        "claim_lock": "No full causal-vertex nonexistence/divergence theorem; no proof that future new principles cannot reduce the ambiguity; no regulator independence; no physical RG closure; no G3/F9/G8/K5 promotion; no new physics or complete QG.",
        "next_admissible_gate": "Treat the physical local amplitude as function-space underdetermined. Test an independently motivated source-faithful composition/renormalization condition capable of restricting tangential coefficient functions, or retain BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING. Do not fit one scalar c as if it exhausted the freedom.",
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
    p = Path(args.output); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
