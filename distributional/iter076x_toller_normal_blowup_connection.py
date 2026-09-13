#!/usr/bin/env python3
"""Iter076X: Toller normal-blow-up angular connection.

Frozen by prereg/ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION.md.
This is a bundle/blow-up compatibility gate, not an ordinary Frechet one-jet claim.
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
    m_values,
)

ROOT = Path(__file__).resolve().parents[1]


def leading_shape(j):
    ms = m_values(j)
    vals = [sp.Integer(1)]
    for mv in ms[1:]:
        vals.append(sp.simplify(vals[-1] * (-(j - mv + 1) / (j + mv))))
    return ms, sp.diag(*vals)


def jplus_matrix(j):
    ms = m_values(j)
    idx = {m: i for i, m in enumerate(ms)}
    M = sp.zeros(len(ms), len(ms))
    for m in ms:
        mp = m + 1
        if mp in idx:
            M[idx[mp], idx[m]] = sp.sqrt((j - m) * (j + m + 1))
    return M


def jminus_matrix(j):
    return jplus_matrix(j).T


def jz_matrix(j):
    return sp.diag(*m_values(j))


def exact_zero_matrix(M):
    return all(sp.simplify(x) == 0 for x in M)


def proportional_on_support(A, B):
    ratios = []
    for i in range(B.rows):
        for k in range(B.cols):
            if B[i, k] != 0:
                ratios.append(sp.simplify(A[i, k] / B[i, k]))
            elif A[i, k] != 0:
                return False, []
    if not ratios:
        return True, []
    return all(sp.simplify(r - ratios[0]) == 0 for r in ratios), ratios


def lane_a():
    text = (ROOT / "sources" / "TOLLER_NORMAL_BLOWUP_CONNECTION_SUPPLEMENT.md").read_text(encoding="utf-8")
    w = (ROOT / "results" / "ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "closed_shape": "(-1)^(j+m) binom(2j,j+m)" in text,
        "recurrence": "C_m/C_(m-1)=-(j-m+1)/(j+m)" in text,
        "equivariant_family": "C_n = D^j(U_n) C_z D^j(U_n)^(-1)" in text,
        "section_independence": "well-defined independently of the section choice" in text,
        "relative_connection": "C_z^(-1) A C_z - A" in text,
        "five_of_seven": "`5/7` surviving transverse angular-connection controls" in text,
        "frechet_firewall": "must not be mislabeled as an ordinary linear Frechet one-jet" in text,
        "w_authoritative_pass": "ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED" in w,
    }
    return {"iteration": "Iter076X", "lane": "A", "valid": bool(all(locks.values())), "source_locks": locks}


def lane_b():
    rows = []
    all_ok = True
    for j in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2), sp.Rational(5, 2), sp.Integer(3)]:
        ms, C = leading_shape(j)
        Cp = C.inv()
        Jz = jz_matrix(j)
        Jp = jplus_matrix(j)
        Jm = jminus_matrix(j)
        comm_z = Jz * C - C * Jz
        z_ok = exact_zero_matrix(comm_z)
        invertible = C.det() != 0

        conj_p = sp.simplify(Cp * Jp * C)
        conj_m = sp.simplify(Cp * Jm * C)
        step_p_ok = True
        step_m_ok = True
        idx = {mv: i for i, mv in enumerate(ms)}
        for mv in ms:
            if mv + 1 in idx:
                r = idx[mv + 1]; c = idx[mv]
                expected = -((j + mv + 1) / (j - mv)) * Jp[r, c]
                step_p_ok &= sp.simplify(conj_p[r, c] - expected) == 0
            if mv - 1 in idx:
                r = idx[mv - 1]; c = idx[mv]
                expected = -((j - mv + 1) / (j + mv)) * Jm[r, c]
                step_m_ok &= sp.simplify(conj_m[r, c] - expected) == 0

        conn_p = sp.simplify(conj_p - Jp)
        proportional, ratios = proportional_on_support(conn_p, Jp)
        special_expected = j == sp.Rational(1, 2)
        prop_ok = proportional if special_expected else not proportional

        # C -> -C leaves the relative connection invariant.
        Cm = -C
        branch_flip_ok = exact_zero_matrix(Cm.inv() * (Jp * Cm - Cm * Jp) - C.inv() * (Jp * C - C * Jp))
        ok = bool(invertible and z_ok and step_p_ok and step_m_ok and prop_ok and branch_flip_ok)
        all_ok &= ok
        rows.append({
            "j": str(j),
            "C_diag": [str(x) for x in C.diagonal()],
            "invertible": bool(invertible),
            "Jz_commutes": bool(z_ok),
            "Jplus_weight_formula": bool(step_p_ok),
            "Jminus_weight_formula": bool(step_m_ok),
            "transverse_connection_proportional_to_Jplus": bool(proportional),
            "proportionality_ratios": [str(x) for x in ratios],
            "proportionality_special_case_expected": bool(special_expected),
            "branch_scale_flip_invariant": bool(branch_flip_ok),
        })
    return {"iteration": "Iter076X", "lane": "B", "valid": bool(all_ok), "controls": rows}


def apply_leading_tensor(state, spins):
    maps = []
    for j in spins:
        ms, C = leading_shape(j)
        maps.append({m: C[i, i] for i, m in enumerate(ms)})
    out = {}
    for ms, coeff in state.items():
        weight = sp.prod(maps[i][ms[i]] for i in range(4))
        out[ms] = sp.simplify(weight * coeff)
    return out


def support_weights(original, transformed):
    vals = []
    for ms, coeff in original.items():
        if coeff != 0:
            vals.append(sp.simplify(transformed[ms] / coeff))
    return sorted(set(vals), key=str)


def lane_c():
    spin_controls = [
        (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    rows = []
    total = 0
    jz_zero = 0
    transverse_zero = 0
    transverse_survive = 0
    all_ok = True
    for spins in spin_controls:
        ks = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in ks:
            total += 1
            state = build_intertwiner(*spins, k)
            F = apply_leading_tensor(state, spins)
            weights = support_weights(state, F)
            z_ok = bool(F) and all(sp.simplify(sum(ms) * coeff) == 0 for ms, coeff in F.items())
            jp = apply_total_ladder(F, spins, "+")
            jm = apply_total_ladder(F, spins, "-")
            jp_zero = len(jp) == 0
            jm_zero = len(jm) == 0
            both_zero = jp_zero and jm_zero
            all_half = all(s == sp.Rational(1, 2) for s in spins)
            frozen_expected_zero = all_half
            weight_expected = (len(weights) == 1) if all_half else (len(weights) >= 2)
            exact_prediction = both_zero == frozen_expected_zero
            ok = bool(state and z_ok and jp_zero == jm_zero and exact_prediction and weight_expected)
            all_ok &= ok
            jz_zero += int(z_ok)
            transverse_zero += int(both_zero)
            transverse_survive += int(not both_zero)
            rows.append({
                "spins": [str(x) for x in spins],
                "k": str(k),
                "leading_tensor_support_weights": [str(x) for x in weights],
                "total_Jz_annihilates_after_C": bool(z_ok),
                "total_Jplus_annihilates_after_C": bool(jp_zero),
                "total_Jminus_annihilates_after_C": bool(jm_zero),
                "transverse_angular_connection_survives": bool(not both_zero),
                "frozen_zero_special_case": bool(frozen_expected_zero),
                "prediction_match": bool(ok),
            })
    valid = bool(all_ok and total == 7 and jz_zero == 7 and transverse_zero == 2 and transverse_survive == 5)
    return {
        "iteration": "Iter076X",
        "lane": "C",
        "valid": valid,
        "intertwiners_checked": total,
        "Jz_stabilizer_zero": jz_zero,
        "transverse_connection_zero": transverse_zero,
        "transverse_connection_survives": transverse_survive,
        "frozen_survival_fraction": "5/7",
        "controls": rows,
    }


def lane_d():
    phi = sp.symbols("phi", real=True)
    section_ok = True
    branch_ok = True
    controls = []
    for j in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]:
        ms, C = leading_shape(j)
        H = sp.diag(*[sp.exp(phi * m) for m in ms])
        commute = exact_zero_matrix(H * C - C * H)
        Jp = jplus_matrix(j)
        conn = C.inv() * (Jp * C - C * Jp)
        Cm = -C
        connm = Cm.inv() * (Jp * Cm - Cm * Jp)
        flip = exact_zero_matrix(conn - connm)
        section_ok &= commute
        branch_ok &= flip
        controls.append({"j": str(j), "stabilizer_commutes": bool(commute), "branch_flip_connection_same": bool(flip)})

    c = lane_c()
    w = (ROOT / "results" / "ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "normal_blowup_connection_nontrivial_generic": bool(c["valid"] and c["transverse_connection_survives"] == 5),
        "iter076W_pure_direction_zeros_unchanged": "ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED" in w,
        "ordinary_Frechet_source_onejet_established": False,
        "direction_independent_factorized_germ_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    false_keys = [k for k in locks if k not in {"normal_blowup_connection_nontrivial_generic", "iter076W_pure_direction_zeros_unchanged"}]
    valid = bool(section_ok and branch_ok and locks["normal_blowup_connection_nontrivial_generic"] and locks["iter076W_pure_direction_zeros_unchanged"] and all(not locks[k] for k in false_keys))
    return {
        "iteration": "Iter076X",
        "lane": "D",
        "valid": valid,
        "section_independence_controls": bool(section_ok),
        "causal_branch_scale_independence": bool(branch_ok),
        "controls": controls,
        "scope_locks": locks,
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
            if obj.get("iteration") == "Iter076X" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED"
        if valid else "ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076X",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "The leading singular Toller matrix defines a nontrivial equivariant family over boost-normal directions. "
            "Its transverse angular connection survives exact boundary-intertwiner controls generically (5/7 frozen controls), "
            "so Iter076W pure-direction zeros do not define a direction-independent zero factorized germ."
        ),
        "next_admissible_gate": (
            "Derive the second-order polar/KAK jet for a concrete mixed compact/boost source group path and determine the "
            "coefficient with which the normal-bundle angular connection enters the subleading collision term."
        ),
        "claim_lock": (
            "Normal-blow-up connection only; no ordinary full source one-jet, physical nonlinear source-to-K4 map, "
            "epsilon^-1 coefficient, causal-vertex finiteness/divergence theorem, generic finite-spin signed P3, new physics, "
            "complete QG, or G3/F9/G8/K5 promotion."
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
