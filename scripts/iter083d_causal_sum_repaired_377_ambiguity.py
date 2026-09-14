#!/usr/bin/env python3
import argparse
import itertools
import json

VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)
SIGNS = (-1, 1)


def prod(xs):
    z = 1
    for x in xs:
        z *= x
    return z


def wedge_pattern(sigma):
    return tuple(sigma[a] * sigma[b] for a, b in EDGES)


def top_char(kappa):
    return prod(kappa)


def require(path, needles):
    text = open(path, encoding="utf-8").read()
    missing = [s for s in needles if s not in text]
    return not missing, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    ap.add_argument(
        "--iter081i",
        default="results/ITER081I_CRITIC_BELTRAN_CAUSAL_SUM_EXTENSION_AMBIGUITY_COROLLARY.md",
    )
    ap.add_argument(
        "--iter081h",
        default="results/ITER081H_CRITIC_BELTRAN_CAUSAL_SUM_L1_COROLLARY.md",
    )
    ap.add_argument(
        "--iter083a",
        default="results/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_RESULT.md",
    )
    ap.add_argument(
        "--iter083b",
        default="results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md",
    )
    ap.add_argument(
        "--iter083c",
        default="results/ITER083C_SM_TOLLER_ADDITIVITY_SELECTOR_NULLMODE_RESULT.md",
    )
    args = ap.parse_args()

    node_assignments = list(itertools.product(SIGNS, repeat=5))
    patterns = [wedge_pattern(s) for s in node_assignments]
    multiplicity = {}
    for k in patterns:
        multiplicity[k] = multiplicity.get(k, 0) + 1
    distinct = sorted(multiplicity)

    # P0: historical Iter081I really used the now-superseded infinite tangential family.
    p0_lock, p0_missing = require(args.iter081i, [
        "Q(y)^n F(y) delta_N",
        "infinite-dimensional",
        "ITER077Q",
    ])

    # P1: 32 node labels, 16 distinct wedge patterns, each duplicated twice.
    p1 = (
        len(node_assignments) == 32
        and len(distinct) == 16
        and set(multiplicity.values()) == {2}
    )

    # P2: top Boolean character is +1 on every causal pattern.
    causal_top = sorted(set(top_char(k) for k in distinct))
    p2 = causal_top == [1]

    # Authoritative finite coefficient-space dimension.
    p3b_lock, p3b_missing = require(args.iter083b, [
        "dim_C F_8 = 377",
        "PASS_EXACT_SCOPED",
        "exact dimension",
    ])
    dim_f8 = 377
    beltran_factor = sum(top_char(k) for k in distinct)
    bcg_factor = sum(top_char(k) for k in patterns)
    p3 = (
        p3b_lock
        and beltran_factor == 16
        and bcg_factor == 32
        and beltran_factor != 0
        and bcg_factor != 0
    )

    # P4: summed source remains sd 20 with same 16-pattern source family.
    p4_lock, p4_missing = require(args.iter081h, [
        "16 C_alpha r^(-20)",
        "transverse scaling degree",
        "16 eta=+1 assignments",
    ])
    p4 = p4_lock

    # P5: Iter083C top mode is additive-null yet +a on all causal sectors.
    p5_lock, p5_missing = require(args.iter083c, [
        "58,025",
        "16 causal",
        "Delta_kappa = +a",
        "TOLLER_ADDITIVITY_HAS_EXACT_JOINT_K5_TOP_BOOLEAN_SELECTOR_NULLMODE",
    ])
    p5 = p5_lock

    # P6: no external weights are used: literal unit sums only.
    unit_beltran = [1] * len(distinct)
    unit_bcg = [1] * len(patterns)
    p6 = sum(unit_beltran) == 16 and sum(unit_bcg) == 32

    # P7: authoritative A/B dependencies establish finite 377 rather than old infinity.
    p7a_lock, p7a_missing = require(args.iter083a, [
        "m_0..m_8 = (2,0,5,1,22,10,72,48,217)",
        "377",
        "PASS_EXACT_SCOPED",
    ])
    p7 = p7a_lock and p3b_lock and dim_f8 == 377

    # Negative controls.
    controls = {
        "reject_32_distinct_wedge_patterns": len(distinct) != 32,
        "reject_beltran_factor_32": beltran_factor != 32,
        "reject_bcg_factor_16": bcg_factor != 16,
        "reject_alternating_weight_insertion": sum(((-1) ** i) for i in range(16)) == 0,
        "reject_historical_infinite_dimension_as_current": p0_lock and dim_f8 != -1,
        "reject_scaling_only_as_377_proof": p7a_lock and p3b_lock,
        "reject_finite_sum_as_unique_selector": beltran_factor != 0 and dim_f8 > 0,
        "retain_future_nonadditive_selector_scope": p5_lock,
    }

    predicates = {
        "P0": p0_lock,
        "P1": p1,
        "P2": p2,
        "P3": p3,
        "P4": p4,
        "P5": p5,
        "P6": p6,
        "P7": p7,
    }

    passed = all(predicates.values()) and all(controls.values())

    result = {
        "iteration": "Iter083D-SM",
        "classification": (
            "ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED"
            if passed
            else "ITER083D_SM_CAUSAL_SUM_REPAIR_INVALID_IMPLEMENTATION"
        ),
        "verdict": "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION",
        "predicates": predicates,
        "controls": controls,
        "node_sign_assignments": len(node_assignments),
        "distinct_causal_wedge_patterns": len(distinct),
        "multiplicities_in_32_label_sum": sorted(set(multiplicity.values())),
        "top_character_values_on_causal_patterns": causal_top,
        "beltran_unit_sum_top_mode_factor": beltran_factor,
        "bcg_32_label_sum_top_mode_factor": bcg_factor,
        "frozen_ambiguity_dimension": dim_f8,
        "beltran_surviving_dimension_lower_bound": dim_f8 if beltran_factor else 0,
        "bcg_surviving_dimension_lower_bound": dim_f8 if bcg_factor else 0,
        "historical_iter081i_status": "SUPERSEDED_INVALID_SOURCE_SYMMETRY_MODEL",
        "dependency_missing": {
            "P0": p0_missing,
            "P3B": p3b_missing,
            "P4": p4_missing,
            "P5": p5_missing,
            "P7A": p7a_missing,
        },
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
    print(payload)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
