#!/usr/bin/env python3
"""Iter056: exact orientation-cocycle covariance of K4 signed normals.

Preregistered in status/ITERATION_056.md at commit
`dfd78f896ec4f0d10b727ff71551aacd32bf637d` before implementation/output.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import EDGES, EDGE_NAMES, TREES, incidence
from distributional.k4_denominator_pole_topology_control import SIGMA_CLASSES, edge_signs_from_class
from distributional.k4_global_contour_compatibility import exact_cycle_matrix

EDGE_TO_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
PERMS = tuple(itertools.permutations(range(4)))
EXPECTED_ACTIONS = len(SIGMA_CLASSES) * len(PERMS)
EXPECTED_COVARIANCE_CHECKS = EXPECTED_ACTIONS * len(TREES) * len(TREES)


def edge_action(perm):
    """Return plain edge map E and orientation cocycle q in target edge order."""
    edge_map = [None] * 6
    q_target = [None] * 6
    E = sp.zeros(6, 6)
    for old_e, (a, b) in enumerate(EDGES):
        pa, pb = perm[a], perm[b]
        mapped = tuple(sorted((pa, pb)))
        new_e = EDGE_TO_INDEX[mapped]
        q = 1 if pa < pb else -1
        edge_map[old_e] = new_e
        q_target[new_e] = q
        E[new_e, old_e] = 1
    valid = (
        sorted(edge_map) == list(range(6))
        and all(q in (-1, 1) for q in q_target)
        and E.det() in (-1, 1)
    )
    Q = sp.diag(*q_target)
    H = Q * E
    return tuple(edge_map), tuple(q_target), E, H, bool(valid)


def naive_target_class(sign_class, perm):
    sigma = list(map(int, edge_signs_from_class(sign_class)[0]))
    new_sigma = [None] * 4
    for old in range(4):
        new_sigma[perm[old]] = sigma[old]
    gauge = new_sigma[0]
    new_sigma = [int(gauge * x) for x in new_sigma]
    target = "".join("+" if x > 0 else "-" for x in new_sigma[1:])
    return target, tuple(new_sigma)


def effective_signs(sign_class, edge_map, q_target):
    s_old = tuple(map(int, edge_signs_from_class(sign_class)[1]))
    s_eff = [None] * 6
    for old_e, new_e in enumerate(edge_map):
        s_eff[new_e] = int(q_target[new_e] * s_old[old_e])
    return s_old, tuple(s_eff)


def factorize_edge_signs(s):
    """Exact test s_ab=tau_a tau_b with tau_0=+1."""
    tau = (1, int(s[0]), int(s[1]), int(s[2]))
    reconstructed = tuple(tau[a] * tau[b] for a, b in EDGES)
    ok = reconstructed == tuple(map(int, s))
    target = None
    if ok:
        target = "".join("+" if x > 0 else "-" for x in tau[1:])
        if target not in SIGMA_CLASSES:
            ok = False
            target = None
    return bool(ok), target, tau, reconstructed


def coordinate_change(A_trans: sp.Matrix, target_tree: str):
    _, _, A_target, _, _, target_chords, det_target = exact_cycle_matrix(target_tree)
    # In constrained_edge_flows, target chord rows are y0,y1,y2 in chord order.
    C = sp.Matrix([[A_trans[e, j] for j in range(3)] for e in target_chords])
    residual = sp.simplify(A_target * C - A_trans)
    exact = all(sp.simplify(z) == 0 for z in residual)
    detC = sp.simplify(C.det())
    unimodular = detC in (-1, 1)
    return A_target, C, detC, bool(exact), bool(unimodular)


def run_audit():
    B = incidence()
    actions = []
    failures = []
    action_factorized = 0
    covariance_checks = 0
    covariance_passes = 0
    all_valid = True

    factorized_by_source = Counter()
    nonfactorized_by_source = Counter()
    effective_sign_counter = Counter()
    reversal_hist = Counter()

    for sign_class in SIGMA_CLASSES:
        s_source = tuple(map(int, edge_signs_from_class(sign_class)[1]))
        for perm in PERMS:
            edge_map, q_target, E, H, edge_valid = edge_action(perm)
            s_old, s_eff = effective_signs(sign_class, edge_map, q_target)
            factorized, eff_class, tau_eff, reconstructed = factorize_edge_signs(s_eff)
            naive_class, naive_sigma = naive_target_class(sign_class, perm)
            naive_signs = tuple(map(int, edge_signs_from_class(naive_class)[1]))

            denominator_identity = True
            eps = sp.symbols("eps", positive=True, real=True)
            x = sp.symbols("x", real=True)
            for old_e, new_e in enumerate(edge_map):
                q = q_target[new_e]
                lhs = q * (x - sp.I * s_eff[new_e] * eps)
                rhs = q * x - sp.I * s_old[old_e] * eps
                denominator_identity = denominator_identity and (sp.simplify(lhs - rhs) == 0)

            if factorized:
                action_factorized += 1
                factorized_by_source[sign_class] += 1
            else:
                nonfactorized_by_source[sign_class] += 1
            effective_sign_counter["".join("+" if z > 0 else "-" for z in s_eff)] += 1
            reversal_count = sum(1 for q in q_target if q < 0)
            reversal_hist[reversal_count] += 1

            action_valid = all([
                edge_valid,
                denominator_identity,
                reconstructed == tuple(map(int, s_eff)) if factorized else True,
                naive_class in SIGMA_CLASSES,
            ])
            all_valid = all_valid and action_valid

            action_cov_ok = True
            action_basis_checks = 0
            for source_tree in sorted(TREES):
                _, _, A_source, _, _, _, det_source = exact_cycle_matrix(source_tree)
                A_trans = sp.simplify(H * A_source)
                cycle_ok = all([
                    abs(int(det_source)) == 1,
                    int(A_source.rank()) == 3,
                    int(A_trans.rank()) == 3,
                    all(sp.simplify(z) == 0 for z in B * A_trans),
                ])
                for target_tree in sorted(TREES):
                    A_target, C, detC, coord_exact, unimodular = coordinate_change(A_trans, target_tree)
                    lhs = sp.simplify(sp.diag(*s_eff) * A_target * C)
                    rhs = sp.simplify(E * sp.diag(*s_source) * A_source)
                    signed_normal_exact = all(sp.simplify(z) == 0 for z in lhs - rhs)
                    covariance_checks += 1
                    action_basis_checks += 1
                    check_ok = all([cycle_ok, coord_exact, unimodular, signed_normal_exact])
                    if check_ok:
                        covariance_passes += 1
                    else:
                        failures.append({
                            "source_class": sign_class,
                            "perm": list(map(int, perm)),
                            "source_tree": source_tree,
                            "target_tree": target_tree,
                            "cycle_ok": bool(cycle_ok),
                            "coordinate_change_exact": bool(coord_exact),
                            "det_C": str(detC),
                            "unimodular": bool(unimodular),
                            "signed_normal_exact": bool(signed_normal_exact),
                        })
                    action_cov_ok = action_cov_ok and check_ok
                    all_valid = all_valid and cycle_ok and coord_exact and unimodular

            actions.append({
                "source_class": sign_class,
                "perm": list(map(int, perm)),
                "edge_map_old_to_new": list(map(int, edge_map)),
                "orientation_q_target": list(map(int, q_target)),
                "orientation_reversal_count": reversal_count,
                "source_edge_signs": list(map(int, s_old)),
                "naive_target_class": naive_class,
                "naive_target_sigma": list(map(int, naive_sigma)),
                "naive_target_edge_signs": list(map(int, naive_signs)),
                "effective_oriented_edge_signs": list(map(int, s_eff)),
                "effective_sign_text": "".join("+" if z > 0 else "-" for z in s_eff),
                "effective_signs_factorized": bool(factorized),
                "effective_factorized_class": eff_class,
                "effective_tau_if_factorized": list(map(int, tau_eff)) if factorized else None,
                "denominator_identity_exact": bool(denominator_identity),
                "basis_pair_checks": action_basis_checks,
                "signed_normal_covariance_all_basis_pairs": bool(action_cov_ok),
                "valid": bool(action_valid),
            })

    primary_covariance = covariance_passes == covariance_checks == EXPECTED_COVARIANCE_CHECKS
    if len(actions) != EXPECTED_ACTIONS:
        all_valid = False
    if covariance_checks != EXPECTED_COVARIANCE_CHECKS:
        all_valid = False

    if not all_valid:
        classification = "ITER056_ORIENTATION_COCYCLE_AUDIT_INVALID"
    elif not primary_covariance:
        classification = "K4_ORIENTATION_COCYCLE_COVARIANCE_FAIL"
    elif action_factorized == EXPECTED_ACTIONS:
        classification = "K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_CLOSED"
    else:
        classification = "K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_NOT_CLOSED"

    nonfactorized_examples = [
        {
            "source_class": a["source_class"],
            "perm": a["perm"],
            "orientation_q_target": a["orientation_q_target"],
            "effective_sign_text": a["effective_sign_text"],
            "naive_target_class": a["naive_target_class"],
        }
        for a in actions if not a["effective_signs_factorized"]
    ][:24]

    return {
        "iteration": "Iter056",
        "classification": classification,
        "source_class_count": len(SIGMA_CLASSES),
        "vertex_permutation_count": len(PERMS),
        "action_count": len(actions),
        "source_target_basis_pairs_per_action": len(TREES) * len(TREES),
        "signed_normal_covariance_check_count": covariance_checks,
        "signed_normal_covariance_pass_count": covariance_passes,
        "all_audit_valid": bool(all_valid),
        "primary_orientation_cocycle_covariance_exact": bool(primary_covariance),
        "factorized_action_count": action_factorized,
        "nonfactorized_action_count": EXPECTED_ACTIONS - action_factorized,
        "factorized_fraction": f"{action_factorized}/{EXPECTED_ACTIONS}",
        "factorized_by_source_class": dict(factorized_by_source),
        "nonfactorized_by_source_class": dict(nonfactorized_by_source),
        "orientation_reversal_histogram": {str(k): v for k, v in sorted(reversal_hist.items())},
        "distinct_effective_oriented_sign_vectors": len(effective_sign_counter),
        "effective_oriented_sign_vector_counts": dict(sorted(effective_sign_counter.items())),
        "covariance_failures": failures,
        "nonfactorized_examples": nonfactorized_examples,
        "actions": actions,
        "claim_lock": (
            "Exact covariance statement for the frozen oriented-flow denominator/signed-normal surrogate only. "
            "No unsourced full-Toller inversion law, physical vertex covariance, K5, G3, F9, G8 or new-physics claim."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = run_audit()
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    summary = {k: out[k] for k in [
        "iteration", "classification", "action_count",
        "signed_normal_covariance_check_count", "signed_normal_covariance_pass_count",
        "all_audit_valid", "primary_orientation_cocycle_covariance_exact",
        "factorized_action_count", "nonfactorized_action_count", "factorized_fraction",
        "orientation_reversal_histogram", "distinct_effective_oriented_sign_vectors",
        "effective_oriented_sign_vector_counts",
    ]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
