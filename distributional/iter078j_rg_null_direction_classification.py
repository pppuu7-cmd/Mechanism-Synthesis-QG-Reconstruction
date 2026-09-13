#!/usr/bin/env python3
"""Iter078J-RG: classify the unique linearized null direction of Iter078H."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H_PATH = ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py"
spec = importlib.util.spec_from_file_location("iter078h", H_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(h)


def primitive_null(mode):
    L = h.compact_tensor()
    J = h.jacobian_at(L, mode)
    rank, pivots, null = h.rref_rank_null(J)
    if null is None:
        return rank, pivots, None, False
    return rank, pivots, null, bool(h.verify_null(J, null))


def proportional_int(a, b):
    """Exact proportionality of integer vectors; returns (bool, Fraction|None)."""
    if a is None or b is None or len(a) != len(b):
        return False, None
    ratio = None
    for x, y in zip(a, b):
        if y == 0:
            if x != 0:
                return False, None
            continue
        r = Fraction(x, y)
        if ratio is None:
            ratio = r
        elif r != ratio:
            return False, None
    if ratio is None:
        return all(x == 0 for x in a), Fraction(0)
    if any(y != 0 and Fraction(x, y) != ratio for x, y in zip(a, b)):
        return False, None
    return True, ratio


def compare_nulls(a, b):
    if a == b:
        return "IDENTICAL", Fraction(1)
    ok, r = proportional_int(a, b)
    if ok:
        return "PROPORTIONAL", r
    return "DIFFERENT", None


def signum(x):
    return 0 if x == 0 else (1 if x > 0 else -1)


def candidate_catalogue(L):
    out = {
        "compact_tensor_L": list(L),
        "constant": [1] * 32,
        "support_nonzero": [1 if x != 0 else 0 for x in L],
        "support_zero": [1 if x == 0 else 0 for x in L],
        "signed_compact_support": [signum(x) for x in L],
    }
    for smask in range(32):
        vec = []
        s = tuple((smask >> i) & 1 for i in range(5))
        for k in h.TUPLES:
            dot = sum(si * ki for si, ki in zip(s, k))
            vec.append(-1 if dot % 2 else 1)
        out[f"walsh_{smask:02d}"] = vec
    return out


def catalogue_match(null, L):
    matches = []
    for name, v in candidate_catalogue(L).items():
        ok, r = proportional_int(null, v)
        if ok:
            matches.append({"name": name, "ratio_null_over_candidate": str(r)})
    return matches


def solve_vandermonde(values):
    """Given six integer values P(0)..P(5), return monomial coeffs c0..c5 over Q."""
    m = []
    for t in range(6):
        row = [Fraction(t ** p) for p in range(6)] + [Fraction(values[t])]
        m.append(row)
    for c in range(6):
        p = next(r for r in range(c, 6) if m[r][c] != 0)
        m[c], m[p] = m[p], m[c]
        q = m[c][c]
        m[c] = [x / q for x in m[c]]
        for r in range(6):
            if r == c:
                continue
            q = m[r][c]
            if q != 0:
                m[r] = [x - q * y for x, y in zip(m[r], m[c])]
    return [m[p][6] for p in range(6)]


def line_coefficients(mode, null):
    L = h.compact_tensor()
    evals = []
    for t in range(6):
        C = [x + t * n for x, n in zip(L, null)]
        evals.append(h.rg_map(C, mode))
    coeff_by_component = [solve_vandermonde([evals[t][j] for t in range(6)]) for j in range(32)]
    vectors = []
    for p in range(6):
        vectors.append([coeff_by_component[j][p] for j in range(32)])
    # subtract R(L): constant is retained only for reconstruction control; perturbation starts at p=1
    reconstructed = []
    for t in range(6):
        row = []
        for j in range(32):
            row.append(sum(vectors[p][j] * (t ** p) for p in range(6)))
        reconstructed.append(row)
    reconstruction_ok = reconstructed == [[Fraction(x) for x in row] for row in evals]
    return L, evals, vectors, reconstruction_ok


def vec_nonzero_count(v):
    return sum(x != 0 for x in v)


def vec_proportional_fraction(v, base):
    # v fractions, base ints/fractions
    ratio = None
    for x, y0 in zip(v, base):
        y = Fraction(y0)
        if y == 0:
            if x != 0:
                return False, None
            continue
        r = x / y
        if ratio is None:
            ratio = r
        elif r != ratio:
            return False, None
    if ratio is None:
        return all(x == 0 for x in v), Fraction(0)
    return True, ratio


def serialize_fraction_vectors(vectors):
    return [[[x.numerator, x.denominator] for x in v] for v in vectors]


def lane_a():
    re, pe, ne, ve = primitive_null("eprl")
    ru, pu, nu, vu = primitive_null("unit")
    relation, factor = compare_nulls(ne, nu)
    valid = re == 31 and ru == 31 and len(ne or []) == 32 and len(nu or []) == 32 and ve and vu
    return {
        "iteration": "Iter078J-RG",
        "lane": "A",
        "valid": valid,
        "eprl_rank": re,
        "eprl_nullity": 32 - re,
        "eprl_null": ne,
        "eprl_verified": ve,
        "unit_rank": ru,
        "unit_nullity": 32 - ru,
        "unit_null": nu,
        "unit_verified": vu,
        "cross_measure_relation": relation,
        "cross_measure_factor": str(factor) if factor is not None else None,
    }


def lane_b():
    L = h.compact_tensor()
    re, _, ne, ve = primitive_null("eprl")
    ru, _, nu, vu = primitive_null("unit")
    me = catalogue_match(ne, L)
    mu = catalogue_match(nu, L)
    valid = re == ru == 31 and ve and vu
    return {
        "iteration": "Iter078J-RG",
        "lane": "B",
        "valid": valid,
        "catalogue_size": len(candidate_catalogue(L)),
        "eprl_matches": me,
        "eprl_match_status": "MATCH" if me else "NO_MATCH",
        "unit_matches": mu,
        "unit_match_status": "MATCH" if mu else "NO_MATCH",
    }


def nonlinear_lane(mode, lane_name):
    rank, _, null, verified = primitive_null(mode)
    L, evals, vectors, reconstruction_ok = line_coefficients(mode, null)
    # Euler/Jacobian null means coefficient of t^1 in R(L+t n) is zero.
    linear_zero = all(x == 0 for x in vectors[1])
    first = next((p for p in range(2, 6) if any(x != 0 for x in vectors[p])), None)
    ncounts = {str(p): vec_nonzero_count(vectors[p]) for p in range(1, 6)}
    props = {}
    for p in range(2, 6):
        ok_n, rn = vec_proportional_fraction(vectors[p], null)
        ok_l, rl = vec_proportional_fraction(vectors[p], L)
        props[str(p)] = {
            "proportional_to_null": ok_n,
            "factor_to_null": str(rn) if rn is not None else None,
            "proportional_to_L": ok_l,
            "factor_to_L": str(rl) if rl is not None else None,
        }
    serialized = serialize_fraction_vectors(vectors)
    digest = hashlib.sha256(json.dumps(serialized, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    valid = rank == 31 and verified and reconstruction_ok and linear_zero
    return {
        "iteration": "Iter078J-RG",
        "lane": lane_name,
        "valid": valid,
        "measure": mode,
        "null": null,
        "polynomial_reconstruction_ok": reconstruction_ok,
        "linear_coefficient_exactly_zero": linear_zero,
        "first_nonzero_nonlinear_order": first if first is not None else "EXACT_FLAT",
        "nonzero_component_counts_by_order": ncounts,
        "proportionality_by_order": props,
        "sha256_fraction_coefficient_vectors": digest,
        "coefficient_vectors": serialized,
    }


def lane_c():
    return nonlinear_lane("eprl", "C")


def lane_d():
    return nonlinear_lane("unit", "D")

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
            if obj.get("iteration") == "Iter078J-RG" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    complete = set(got) == set(LANES)
    valid = complete and all(bool(got[k].get("valid")) for k in LANES)
    if not valid:
        return {"iteration": "Iter078J-RG", "execution_valid": False, "verdict": "INVALID_IMPLEMENTATION", "lanes_found": sorted(got)}
    ec = got["C"]["first_nonzero_nonlinear_order"]
    ud = got["D"]["first_nonzero_nonlinear_order"]
    eflat = ec == "EXACT_FLAT"
    uflat = ud == "EXACT_FLAT"
    classification = (
        "ITER078J_RG_LINEARIZED_NULL_IS_EXACT_FLAT_DIRECTION_OF_FIXED_JHALF_1TO5_CONTROL_MAP_EXACT_SCOPED"
        if eflat else
        f"ITER078J_RG_UNIQUE_LINEARIZED_NULL_IS_NONLINEARLY_LIFTED_AT_ORDER_{ec}_EXACT_CONTROL_SCOPED"
    )
    return {
        "iteration": "Iter078J-RG",
        "execution_valid": True,
        "verdict": "CONTROL_RESULT",
        "classification": classification,
        "cross_measure_null_relation": got["A"]["cross_measure_relation"],
        "eprl_null": got["A"]["eprl_null"],
        "unit_null": got["A"]["unit_null"],
        "eprl_catalogue_matches": got["B"]["eprl_matches"],
        "unit_catalogue_matches": got["B"]["unit_matches"],
        "eprl_first_nonlinear_order": ec,
        "unit_first_nonlinear_order": ud,
        "eprl_counts_by_order": got["C"]["nonzero_component_counts_by_order"],
        "unit_counts_by_order": got["D"]["nonzero_component_counts_by_order"],
        "eprl_coeff_digest": got["C"]["sha256_fraction_coefficient_vectors"],
        "unit_coeff_digest": got["D"]["sha256_fraction_coefficient_vectors"],
        "interpretation_ceiling": "Fixed-j=1/2 pure order-zero tensor-network control only; no physical causal-Toller gauge-mode or RG-fixed-point claim.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose one lane or aggregate")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
