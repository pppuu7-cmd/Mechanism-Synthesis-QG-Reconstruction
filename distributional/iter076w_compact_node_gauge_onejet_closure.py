#!/usr/bin/env python3
"""Iter076W: exact compact source-node gauge one-jet closure audit.

Frozen by prereg/ITER076W_COMPACT_NODE_GAUGE_ONEJET_CLOSURE.md.
No mixed compact/boost differentiability or physical source->K4 curvature is inferred.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from collections import Counter
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

ROOT = Path(__file__).resolve().parents[1]


def m_values(j):
    j2 = int(2 * j)
    return [sp.Rational(m2, 2) for m2 in range(-j2, j2 + 1, 2)]


def coupled_values(j1, j2):
    lo2 = int(2 * abs(j1 - j2))
    hi2 = int(2 * (j1 + j2))
    return [sp.Rational(k2, 2) for k2 in range(lo2, hi2 + 1, 2)]


def build_intertwiner(j1, j2, j3, j4, k):
    state = {}
    for ms in itertools.product(m_values(j1), m_values(j2), m_values(j3), m_values(j4)):
        m1, m2, m3, m4 = ms
        coeff = sp.Integer(0)
        for q in m_values(k):
            coeff += (
                clebsch_gordan(j1, j2, k, m1, m2, q)
                * clebsch_gordan(j3, j4, k, m3, m4, -q)
                * clebsch_gordan(k, k, 0, q, -q, 0)
            )
        coeff = sp.simplify(coeff)
        if coeff != 0:
            state[ms] = coeff
    return state


def apply_total_ladder(state, spins, direction):
    out = {}
    step = 1 if direction == "+" else -1
    for ms, coeff in state.items():
        for leg, (jv, mv) in enumerate(zip(spins, ms)):
            target_m = mv + step
            if target_m not in m_values(jv):
                continue
            if direction == "+":
                fac = sp.sqrt((jv - mv) * (jv + mv + 1))
            else:
                fac = sp.sqrt((jv + mv) * (jv - mv + 1))
            target = list(ms)
            target[leg] = target_m
            target = tuple(target)
            out[target] = sp.simplify(out.get(target, 0) + fac * coeff)
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


def apply_total_jz(state):
    out = {}
    for ms, coeff in state.items():
        v = sp.simplify(sum(ms) * coeff)
        if v != 0:
            out[ms] = v
    return out


def apply_single_leg_jz(state, leg):
    out = {}
    for ms, coeff in state.items():
        v = sp.simplify(ms[leg] * coeff)
        if v != 0:
            out[ms] = v
    return out


def frozen_intertwiners():
    spin_controls = [
        (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    rows = []
    for spins in spin_controls:
        common_k = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in common_k:
            rows.append((spins, k, build_intertwiner(*spins, k)))
    return rows


def lane_a():
    p = ROOT / "sources" / "TOLLER_COMPACT_NODE_GAUGE_ONEJET_SUPPLEMENT.md"
    text = p.read_text(encoding="utf-8")
    compact = " ".join(text.split())
    locks = {
        "five_su2_intertwiners": "five SU(2) intertwiners" in compact,
        "eq4_relative_argument": "g_b^{-1}g_a" in compact,
        "root_g1_fixed": "g_1=1" in compact,
        "integrated_g2_to_g5": "g_2,...,g_5" in compact,
        "eq7_compact_covariance": "Eq. (7) gives the exact compact covariance" in compact,
        "common_generator_four_slots": "same SU(2) generator acts on all four node-5 slots" in compact,
        "mixed_direction_firewall": "mixed compact-boost directions" in compact,
        "epsilon_firewall": "nominal `epsilon^-1` coefficient" in compact,
    }
    valid = all(locks.values())
    return {"iteration": "Iter076W", "lane": "A", "valid": bool(valid), "source_locks": locks}


def lane_b():
    controls = []
    all_ok = True
    rows = frozen_intertwiners()
    for spins, k, state in rows:
        nonzero = bool(state)
        support = nonzero and all(sp.simplify(sum(ms)) == 0 for ms in state)
        jz_zero = nonzero and not apply_total_jz(state)
        jp_zero = nonzero and not apply_total_ladder(state, spins, "+")
        jm_zero = nonzero and not apply_total_ladder(state, spins, "-")
        arbitrary_direction = jz_zero and jp_zero and jm_zero
        ok = nonzero and support and arbitrary_direction
        all_ok &= ok
        controls.append({
            "spins": [str(x) for x in spins],
            "k": str(k),
            "nonzero_components": len(state),
            "magnetic_support_sum_zero": bool(support),
            "total_Jz_zero": bool(jz_zero),
            "total_Jplus_zero": bool(jp_zero),
            "total_Jminus_zero": bool(jm_zero),
            "common_compact_arbitrary_direction_zero": bool(arbitrary_direction),
        })
    valid = bool(all_ok and len(rows) == 7)
    return {
        "iteration": "Iter076W",
        "lane": "B",
        "valid": valid,
        "intertwiners_checked": len(rows),
        "source_compact_operator": "-i * sum_a J_n^(5a) (normalization-sign irrelevant to zero)",
        "controls": controls,
    }


def all_edges(labels):
    return {tuple(sorted(e)) for e in itertools.combinations(labels, 2)}


def star(node, edges):
    return {e for e in edges if node in e}


def lane_c():
    labels = (1, 2, 3, 4, 5)
    integrated = (2, 3, 4, 5)
    edges = all_edges(labels)
    star5 = star(5, edges)
    target_counts = Counter()
    rows = []
    all_ok = True
    for perm in itertools.permutations(integrated):
        p = {1: 1, **dict(zip(integrated, perm))}
        mapped_edges = {tuple(sorted((p[a], p[b]))) for a, b in edges}
        mapped_star5 = {tuple(sorted((p[a], p[b]))) for a, b in star5}
        target = p[5]
        target_counts[target] += 1
        target_star = star(target, edges)
        root_ok = p[1] == 1
        wedge_bijection = mapped_edges == edges
        star_transport = mapped_star5 == target_star
        ok = root_ok and wedge_bijection and star_transport
        all_ok &= ok
        rows.append({
            "permutation": [p[i] for i in labels],
            "target_of_node5": target,
            "root_fixed": root_ok,
            "wedge_bijection": wedge_bijection,
            "incident_star_transport": star_transport,
        })
    counts_ok = target_counts == Counter({2: 6, 3: 6, 4: 6, 5: 6})
    valid = bool(all_ok and counts_ok and len(rows) == 24)
    return {
        "iteration": "Iter076W",
        "lane": "C",
        "valid": valid,
        "permutations_checked": len(rows),
        "target_counts": {str(k): v for k, v in sorted(target_counts.items())},
        "simultaneous_data_relabel_required": True,
        "creates_scalar_parity_selector": False,
        "controls": rows,
    }


def lane_d():
    rows = frozen_intertwiners()
    controls = []
    total_zero_all = True
    single_leg_nonzero_any = False
    for spins, k, state in rows:
        total_zero = not apply_total_jz(state)
        single = apply_single_leg_jz(state, 0)
        single_nonzero = bool(single)
        total_zero_all &= total_zero
        single_leg_nonzero_any |= single_nonzero
        controls.append({
            "spins": [str(x) for x in spins],
            "k": str(k),
            "total_Jz_zero": bool(total_zero),
            "single_leg0_Jz_nonzero": bool(single_nonzero),
            "single_leg0_nonzero_components": len(single),
        })
    scope = {
        "common_compact_node_onejet_killed": bool(total_zero_all),
        "all_integrated_nodes_transport": True,
        "independent_wedge_compact_onejet_killed": False,
        "mixed_compact_boost_differentiability_established": False,
        "full_source_onejet_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    forbidden_true = [
        "independent_wedge_compact_onejet_killed",
        "mixed_compact_boost_differentiability_established",
        "full_source_onejet_established",
        "physical_source_to_K4_curvature_selected",
        "epsilon_minus1_coefficient_established",
        "generic_finite_spin_signed_P3_promoted",
        "G3_promoted", "F9_promoted", "G8_promoted", "K5_promoted",
    ]
    valid = bool(
        total_zero_all
        and single_leg_nonzero_any
        and scope["common_compact_node_onejet_killed"]
        and scope["all_integrated_nodes_transport"]
        and not any(scope[k] for k in forbidden_true)
    )
    return {
        "iteration": "Iter076W",
        "lane": "D",
        "valid": valid,
        "single_leg_negative_control_nonzero": bool(single_leg_nonzero_any),
        "controls": controls,
        "scope_locks": scope,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


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
            lane = obj.get("lane")
            if obj.get("iteration") == "Iter076W" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076W_COMMON_COMPACT_SOURCE_NODE_ONEJET_KILLED_BY_SU2_INTERTWINER_AND_S4_TRANSPORT_EXACT_SCOPED"
        if valid
        else "ITER076W_COMPACT_NODE_GAUGE_ONEJET_CLOSURE_FAIL"
    )
    return {
        "iteration": "Iter076W",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "Exact Eq.(7) compact covariance plus SU(2)-intertwiner invariance kills a common compact "
            "source-node one-jet. Root-stabilizer S4 transports the structural cancellation from node 5 to "
            "all four integrated source nodes. An independent single-wedge compact perturbation is a nonzero "
            "negative control. Mixed compact/boost differentiability remains open."
        ),
        "next_admissible_gate": (
            "Audit the normal blow-up / mixed compact-boost compatibility of the extracted leading singular "
            "matrix and determine whether the separate pure-direction cancellations assemble into one "
            "direction-independent differentiable regular germ."
        ),
        "claim_lock": (
            "No full source one-jet, physical nonlinear source-to-K4 map, epsilon^-1 coefficient, causal-vertex "
            "finiteness/divergence theorem, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=sorted(LANES))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    out = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    write(out, args.output)
    print(json.dumps(out, indent=2, sort_keys=True))
    if not out.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
