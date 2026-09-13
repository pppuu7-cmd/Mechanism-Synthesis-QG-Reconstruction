#!/usr/bin/env python3
"""Iter076W: compact-node gauge one-jet and pure-direction closure.

Frozen by prereg/ITER076W_COMPACT_NODE_GAUGE_AND_PURE_DIRECTION_CLOSURE.md.
Separate pure-generator directions only; mixed compact/boost differentiability stays open.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp

from distributional.iter076v_matrix_boost_onejet_intertwiner_closure import (
    apply_total_ladder,
    build_intertwiner,
    coupled_values,
)

ROOT = Path(__file__).resolve().parents[1]
VERTS = tuple(range(5))
ROOT_NODE = 0
INTEGRATED = (1, 2, 3, 4)
TARGET_NODE = 4
EDGES = tuple((a, b) for a in VERTS for b in VERTS if a < b)


def root_stabilizer_perms():
    out = []
    for q in itertools.permutations(INTEGRATED):
        p = [0] * 5
        p[ROOT_NODE] = ROOT_NODE
        for src, dst in zip(INTEGRATED, q):
            p[src] = dst
        out.append(tuple(p))
    return out


def edge_image(p, edge):
    a, b = edge
    aa, bb = p[a], p[b]
    return tuple(sorted((aa, bb)))


def lane_a():
    supplement = (ROOT / "sources" / "TOLLER_COMPACT_NODE_GAUGE_ONEJET_SUPPLEMENT.md").read_text(encoding="utf-8")
    v_result = (ROOT / "results" / "ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE_RESULT.md").read_text(encoding="utf-8")
    n_result = (ROOT / "results" / "ITER076N_EXACT_AMPLITUDE_ORIENTATION_SELECTOR_PROVENANCE_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "five_intertwiners": "five SU(2) intertwiners" in supplement,
        "relative_argument": "g_b^{-1}g_a" in supplement,
        "magnetic_slots": "m_ba, j_ab m_ab" in supplement,
        "gauge_root": "g_1=1" in supplement and "g_2,...,g_5" in supplement,
        "compact_covariance": "T(h_b^{-1} g h_a)" in supplement,
        "node5_common_compact": "Node-5 common compact perturbation" in supplement,
        "root_stabilizer_s4": "root-stabilizer `S4`" in supplement,
        "mixed_direction_firewall": "does not by itself prove mixed-direction differentiability" in supplement,
        "curvature_firewall": "physical nonlinear source-to-K4 curvature" in supplement,
        "v_authoritative_pass": "ITER076V_RELATIVE_TOLLER_BOOST_ONEJET_IS_I_GAMMA_J_AND_SU2_INTERTWINER_KILLS_NODE_COMMON_BOOST_EXACT_SCOPED" in v_result,
        "n_120_permutations": "All `120` permutations" in n_result,
        "n_scalar_plus_one": "explicit scalar coefficient `+1`" in n_result,
    }
    return {
        "iteration": "Iter076W",
        "lane": "A",
        "valid": bool(all(locks.values())),
        "source_locks": locks,
    }


def apply_single_jz(state, leg=0):
    return {
        ms: sp.simplify(ms[leg] * coeff)
        for ms, coeff in state.items()
        if sp.simplify(ms[leg] * coeff) != 0
    }


def lane_b():
    spin_controls = [
        (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    rows = []
    all_ok = True
    total = 0
    any_single_leg_nonzero = False
    for spins in spin_controls:
        ks = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in ks:
            total += 1
            state = build_intertwiner(*spins, k)
            nonzero = bool(state)
            jz_ok = nonzero and all(sp.simplify(sum(ms) * coeff) == 0 for ms, coeff in state.items())
            jp_ok = nonzero and not apply_total_ladder(state, spins, "+")
            jm_ok = nonzero and not apply_total_ladder(state, spins, "-")
            arbitrary_axis_ok = bool(jz_ok and jp_ok and jm_ok)
            single_leg = apply_single_jz(state, 0) if nonzero else {}
            single_nonzero = bool(single_leg)
            any_single_leg_nonzero |= single_nonzero
            ok = bool(nonzero and arbitrary_axis_ok)
            all_ok &= ok
            rows.append({
                "spins": [str(x) for x in spins],
                "k": str(k),
                "nonzero_components": len(state),
                "total_Jz_annihilates": bool(jz_ok),
                "total_Jplus_annihilates": bool(jp_ok),
                "total_Jminus_annihilates": bool(jm_ok),
                "common_compact_any_axis_annihilates": arbitrary_axis_ok,
                "single_leg_Jz_negative_control_nonzero": single_nonzero,
            })
    valid = bool(all_ok and total == 7 and any_single_leg_nonzero)
    return {
        "iteration": "Iter076W",
        "lane": "B",
        "valid": valid,
        "intertwiners_checked": total,
        "all_common_compact_generators_annihilated": bool(all_ok),
        "single_leg_generator_negative_control_seen": bool(any_single_leg_nonzero),
        "toller_pole_strip_used": False,
        "controls": rows,
    }


def lane_c():
    perms = root_stabilizer_perms()
    counts_to_target = {v: 0 for v in INTEGRATED}
    all_edge_bijections = True
    all_root_fixed = True
    rows = []
    for p in perms:
        all_root_fixed &= p[ROOT_NODE] == ROOT_NODE and set(p[1:]) == set(INTEGRATED)
        for v in INTEGRATED:
            if p[v] == TARGET_NODE:
                counts_to_target[v] += 1
        mapped = [edge_image(p, e) for e in EDGES]
        bijective = len(set(mapped)) == len(EDGES) and set(mapped) == set(EDGES)
        all_edge_bijections &= bijective
        rows.append({"perm": list(p), "edge_bijection": bool(bijective)})

    n_result = (ROOT / "results" / "ITER076N_EXACT_AMPLITUDE_ORIENTATION_SELECTOR_PROVENANCE_RESULT.md").read_text(encoding="utf-8")
    scalar_plus_one = "explicit scalar coefficient `+1`" in n_result
    counts_ok = all(counts_to_target[v] == 6 for v in INTEGRATED)
    valid = bool(
        len(perms) == 24
        and counts_ok
        and all_edge_bijections
        and all_root_fixed
        and scalar_plus_one
    )
    return {
        "iteration": "Iter076W",
        "lane": "C",
        "valid": valid,
        "root_stabilizer_size": len(perms),
        "maps_each_integrated_node_to_node5_count": {str(k): v for k, v in counts_to_target.items()},
        "all_counts_equal_six": bool(counts_ok),
        "all_ten_wedge_maps_bijective": bool(all_edge_bijections),
        "root_and_integrated_decomposition_preserved": bool(all_root_fixed),
        "eq4_product_measure_scalar_character_plus_one_locked": bool(scalar_plus_one),
        "simultaneous_relabeling_required": True,
        "permutations": rows,
    }


def lane_d():
    b = lane_b()
    c = lane_c()
    v_result = (ROOT / "results" / "ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE_RESULT.md").read_text(encoding="utf-8")
    boost_locked = (
        "ITER076V_RELATIVE_TOLLER_BOOST_ONEJET_IS_I_GAMMA_J_AND_SU2_INTERTWINER_KILLS_NODE_COMMON_BOOST_EXACT_SCOPED"
        in v_result
    )
    cancellations = []
    for node in INTEGRATED:
        for family in ("compact", "boost"):
            for axis in ("x", "y", "z"):
                cancellations.append({
                    "node": node,
                    "family": family,
                    "axis": axis,
                    "structural_zero": bool(b["valid"] and c["valid"] and (family != "boost" or boost_locked)),
                })
    all_zero = len(cancellations) == 24 and all(x["structural_zero"] for x in cancellations)
    locks = {
        "compact_node_common_onejet_killed_by_intertwiner": bool(b["valid"]),
        "boost_node_common_onejet_killed_by_intertwiner": bool(boost_locked),
        "pure_generator_direction_cancellation_all_integrated_nodes": bool(all_zero and c["valid"]),
        "mixed_compact_boost_C1_germ_established": False,
        "direction_independent_leading_factorization_established": False,
        "full_source_onejet_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    false_required = [
        "mixed_compact_boost_C1_germ_established",
        "direction_independent_leading_factorization_established",
        "full_source_onejet_established",
        "physical_source_to_K4_curvature_selected",
        "epsilon_minus1_coefficient_established",
        "generic_finite_spin_signed_P3_promoted",
        "G3_promoted",
        "F9_promoted",
        "G8_promoted",
        "K5_promoted",
    ]
    valid = bool(
        b["valid"]
        and c["valid"]
        and boost_locked
        and all_zero
        and locks["compact_node_common_onejet_killed_by_intertwiner"]
        and locks["boost_node_common_onejet_killed_by_intertwiner"]
        and locks["pure_generator_direction_cancellation_all_integrated_nodes"]
        and all(not locks[k] for k in false_required)
    )
    return {
        "iteration": "Iter076W",
        "lane": "D",
        "valid": valid,
        "pure_direction_cancellations": len(cancellations),
        "all_24_structural_zeros": bool(all_zero),
        "scope_locks": locks,
        "ledger": cancellations,
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
        "ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED"
        if valid
        else "ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076W",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "All six pure Lie-generator directions at every integrated source node are structurally annihilated after "
            "boundary-intertwiner contraction: compact directions by exact SU(2) gauge invariance, boost-normal directions "
            "by Iter076V plus the same closure. Mixed-direction differentiability remains open."
        ),
        "next_admissible_gate": (
            "Audit normal-blow-up and mixed compact/boost compatibility of the leading singular Toller matrix family; "
            "test whether its connection term is pure SU(2) gauge or supplies independent source one-jet data."
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
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
