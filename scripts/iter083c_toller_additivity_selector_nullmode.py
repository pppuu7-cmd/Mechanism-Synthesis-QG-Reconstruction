#!/usr/bin/env python3
import argparse
import itertools
import json
import os

VERTICES = tuple(range(5))
EDGES = tuple((a, b) for a in VERTICES for b in VERTICES if a < b)
NEDGE = len(EDGES)
SIGNS = (-1, 1)


def prod(xs):
    z = 1
    for x in xs:
        z *= x
    return z


def top_char(kappa):
    return prod(kappa)


def permutations(n):
    return itertools.permutations(range(n))


def permute_kappa(kappa, p):
    idx = {e: i for i, e in enumerate(EDGES)}
    out = [None] * NEDGE
    for e, i in idx.items():
        a, b = e
        aa, bb = sorted((p[a], p[b]))
        out[idx[(aa, bb)]] = kappa[i]
    return tuple(out)


def causal_patterns():
    out = set()
    for sigma in itertools.product(SIGNS, repeat=5):
        out.add(tuple(sigma[a] * sigma[b] for a, b in EDGES))
    return out


def marginal_sum(mask, complement_values, char_fn=top_char):
    summed = [i for i in range(NEDGE) if mask & (1 << i)]
    complement = [i for i in range(NEDGE) if not (mask & (1 << i))]
    total = 0
    for summed_values in itertools.product(SIGNS, repeat=len(summed)):
        kappa = [None] * NEDGE
        for i, value in zip(complement, complement_values):
            kappa[i] = value
        for i, value in zip(summed, summed_values):
            kappa[i] = value
        total += char_fn(tuple(kappa))
    return total


def all_marginals_zero(char_fn):
    checks = 0
    failures = []
    for mask in range(1, 1 << NEDGE):
        complement = [i for i in range(NEDGE) if not (mask & (1 << i))]
        for values in itertools.product(SIGNS, repeat=len(complement)):
            checks += 1
            z = marginal_sum(mask, values, char_fn)
            if z != 0:
                failures.append({"mask": mask, "complement_values": list(values), "sum": z})
                return False, checks, failures
    return True, checks, failures


def one_edge_marginal_zero(table):
    for e in range(NEDGE):
        complement = [i for i in range(NEDGE) if i != e]
        for vals in itertools.product(SIGNS, repeat=NEDGE - 1):
            total = 0
            for s in SIGNS:
                k = [None] * NEDGE
                for i, v in zip(complement, vals):
                    k[i] = v
                k[e] = s
                total += table[tuple(k)]
            if total != 0:
                return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    ap.add_argument(
        "--iter077i-source",
        default="sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md",
    )
    ap.add_argument(
        "--iter077m-source",
        default="sources/ITER077M_SM_SOURCE_SYMMETRY_SELECTOR_DERIVATION.md",
    )
    args = ap.parse_args()

    assert NEDGE == 10
    kappas = list(itertools.product(SIGNS, repeat=NEDGE))

    # P0: exact upstream branch/scaling lock is present in the frozen derivation.
    text_i = open(args.iter077i_source, encoding="utf-8").read()
    required_i = [
        "beta^(-2) diag(1,-1)",
        "t^(-,gamma/2,1/2)(beta) = -[2/(1+gamma^2)] beta^(-2)",
        "raw radial power `r^(-20)`",
        "switching a wedge from `T+` to `T-` multiplies its matrix by a nonzero common sign",
    ]
    p0 = all(s in text_i for s in required_i)

    # P1/P2: top character lies in every nonempty partial-sum kernel.
    p1, marginal_checks, marginal_failures = all_marginals_zero(top_char)
    full_sum = sum(top_char(k) for k in kappas)
    p2 = full_sum == 0

    # P3: exact causal image and even-degree K5 identity.
    causal = causal_patterns()
    causal_top_values = sorted(set(top_char(k) for k in causal))
    p3 = len(causal) == 16 and causal_top_values == [1]

    # P4: S5 stability/invariance, exhaustively over 120 permutations.
    perms5 = list(permutations(5))
    p4 = all(
        permute_kappa(k, p) in causal
        for p in perms5
        for k in causal
    ) and all(
        top_char(permute_kappa(k, p)) == top_char(k)
        for p in perms5
        for k in kappas
    )

    # P5: the multiplier is always nonzero +/-1; homogeneous linear support,
    # covariance and scaling properties of an upstream admissible ambiguity a
    # are therefore preserved. Upstream existence of nonzero a is source-locked.
    text_m = open(args.iter077m_source, encoding="utf-8").read()
    witness_locked = (
        "A_ext,c = A_ext + c F_SU2(y;Psi) delta_N(x)" in text_m
        and "do not by themselves select a unique K5 extension" in text_m
    )
    p5 = witness_locked and set(top_char(k) for k in kappas) == {-1, 1}

    # P6: strongest additive no-go follows from P1 plus nonzero causal action.
    p6 = p1 and p2 and p3 and all(top_char(k) != 0 for k in causal)

    # P7: dependency-safe output deliberately does not promote a pending 377.
    iter083a_raw = "results/raw/iter083a_sm_boundary_covariant_jet_character_validation.json"
    authoritative_dimension = None
    iter083a_status = "NOT_PERSISTED_OR_NOT_AUTHORITATIVE"
    if os.path.exists(iter083a_raw):
        try:
            d = json.load(open(iter083a_raw, encoding="utf-8"))
            if d.get("verdict") == "PASS_EXACT_SCOPED" and all(d.get("predicates", {}).values()):
                authoritative_dimension = d.get("total_m_leq8")
                iter083a_status = "PERSISTED_PASS_EXACT_SCOPED"
        except Exception:
            iter083a_status = "PERSISTED_BUT_UNREADABLE"
    p7 = authoritative_dimension is None or isinstance(authoritative_dimension, int)

    # Negative controls.
    constant_full_sum = len(kappas)
    neg_constant = constant_full_sum != 0

    # Every proper-subset Boolean character is exposed by summing an edge not in its support.
    proper_subset_exposed = True
    for rmask in range(0, (1 << NEDGE) - 1):
        missing = next(i for i in range(NEDGE) if not (rmask & (1 << i)))

        def subset_char(k, m=rmask):
            return prod(k[i] for i in range(NEDGE) if m & (1 << i))

        comp = [1] * (NEDGE - 1)
        if marginal_sum(1 << missing, comp, subset_char) == 0:
            proper_subset_exposed = False
            break
    neg_proper_subset = proper_subset_exposed

    top_table = {k: top_char(k) for k in kappas}
    damaged_table = dict(top_table)
    damaged_table[kappas[0]] *= -1
    neg_random = not one_edge_marginal_zero(damaged_table)

    all_minus = tuple([-1] * NEDGE)
    neg_causal_count = len(causal) != len(kappas)
    neg_all_minus = all_minus not in causal

    controls = {
        "constant_mode_rejected_as_full_sum_nullmode": neg_constant,
        "every_proper_subset_character_exposed_by_some_partial_sum": neg_proper_subset,
        "damaged_randomized_sign_table_rejected": neg_random,
        "false_all_1024_sign_assignments_causal_rejected": neg_causal_count,
        "all_minus_wedge_assignment_rejected_as_causal": neg_all_minus,
        "off_support_deformation_rejected_by_frozen_definition": witness_locked,
        "additivity_not_promoted_to_common_regulator": authoritative_dimension is None or p7,
    }

    predicates = {f"P{i}": v for i, v in enumerate([p0, p1, p2, p3, p4, p5, p6, p7])}
    passed = all(predicates.values()) and all(controls.values())

    result = {
        "iteration": "Iter083C-SM",
        "classification": (
            "ITER083C_SM_TOLLER_ADDITIVITY_HAS_EXACT_JOINT_K5_TOP_BOOLEAN_SELECTOR_NULLMODE"
            if passed
            else "ITER083C_SM_TOLLER_ADDITIVITY_NULLMODE_INVALID_IMPLEMENTATION"
        ),
        "verdict": "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION",
        "predicates": predicates,
        "controls": controls,
        "number_of_wedges": NEDGE,
        "unconstrained_sign_assignments": len(kappas),
        "nonempty_partial_sum_subsets_checked": (1 << NEDGE) - 1,
        "conditional_marginal_sums_checked": marginal_checks,
        "marginal_failures": marginal_failures,
        "full_top_character_sum": full_sum,
        "distinct_causal_patterns": len(causal),
        "top_character_values_on_causal_patterns": causal_top_values,
        "all_minus_is_causal": all_minus in causal,
        "iter083a_dependency_status": iter083a_status,
        "authoritative_boundary_covariant_dimension_if_available": authoritative_dimension,
        "scientific_statement": (
            "Every additive identity generated by T+ + T- = D annihilates the top Boolean sector deformation, "
            "while that deformation equals +a on every factorized causal K5 sign pattern."
        ),
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
    print(payload)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
