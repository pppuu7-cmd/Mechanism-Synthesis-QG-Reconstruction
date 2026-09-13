#!/usr/bin/env python3
"""Iter076V: matrix relative boost one-jet and SU(2)-intertwiner closure.

Frozen by prereg/ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE.md.
Boost-normal source control only; compact tangential one-jets remain open.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
gamma = sp.symbols("gamma", nonzero=True, real=True)


def m_values(j):
    j2 = int(2 * j)
    return [sp.Rational(m2, 2) for m2 in range(-j2, j2 + 1, 2)]


def coupled_values(j1, j2):
    lo2 = int(2 * abs(j1 - j2))
    hi2 = int(2 * (j1 + j2))
    return [sp.Rational(k2, 2) for k2 in range(lo2, hi2 + 1, 2)]


def leading_shape(j):
    """Primitive rational C_m shape up to an overall nonzero branch scale."""
    ms = m_values(j)
    vals = [sp.Integer(1)]
    for mv in ms[1:]:
        ratio = -sp.Rational(1, 1) * (j - mv + 1) / (j + mv)
        vals.append(sp.simplify(vals[-1] * ratio))
    return ms, sp.diag(*vals)


def Jz_matrix(j):
    return sp.diag(*m_values(j))


def Ry_pi(j):
    ms = m_values(j)
    idx = {mv: k for k, mv in enumerate(ms)}
    U = sp.zeros(len(ms), len(ms))
    for r, mv in enumerate(ms):
        p = -mv
        exponent = int(j - mv)
        U[r, idx[p]] = -1 if exponent % 2 else 1
    return U


def exact_zero_matrix(M):
    return all(sp.simplify(x) == 0 for x in M)


def lane_a():
    text = (ROOT / "sources" / "GAMMA_SIMPLE_TOLLER_MATRIX_ONEJET_INTERTWINER_SUPPLEMENT.md").read_text(encoding="utf-8")
    locks = {
        "five_su2_intertwiners": "five SU(2) intertwiners" in text,
        "eq4_relative_group": "g_b^(-1) g_a" in text,
        "eq4_magnetic_slots": "T_{j_ab m_ba, j_ab m_ab}" in text,
        "eq7_compact_covariance": "Eq. (7) gives compact covariance" in text,
        "boost_normal_scope": "boost-normal" in text,
        "compact_tangent_firewall": "compact/rotation tangential derivatives" in text,
        "epsilon_firewall": "nominal `epsilon^-1` coefficient" in text,
    }
    return {
        "iteration": "Iter076V",
        "lane": "A",
        "valid": bool(all(locks.values())),
        "source_locks": locks,
    }


def lane_b():
    j, m, g = sp.symbols("j m g", real=True)
    z = I * g * j - m
    plus_reflection = sp.pi / sp.sin(sp.pi * z)
    minus_reflection = sp.pi / sp.sin(-sp.pi * z)
    branch_ratio = sp.simplify(minus_reflection / plus_reflection)

    cshape = 1 / (
        sp.sin(sp.pi * (I * g * j - m))
        * sp.gamma(j - m + 1)
        * sp.gamma(j + m + 1)
    )
    step_ratio = sp.simplify(sp.trigsimp(sp.expand_func(cshape / cshape.subs(m, m - 1))))
    expected_step = -(j - m + 1) / (j + m)
    symbolic_ok = sp.simplify(branch_ratio + 1) == 0 and sp.simplify(step_ratio - expected_step) == 0

    controls = []
    matrix_ok = True
    all_nonzero = True
    for jv in [sp.Rational(1,2), sp.Integer(1), sp.Rational(3,2), sp.Integer(2), sp.Rational(5,2), sp.Integer(3)]:
        ms, C = leading_shape(jv)
        Jz = Jz_matrix(jv)
        D = C * (I * gamma * Jz)
        left = sp.simplify(C.inv() * D)
        right = sp.simplify(D * C.inv())
        target = I * gamma * Jz
        ok = exact_zero_matrix(left - target) and exact_zero_matrix(right - target)
        nz = all(x != 0 for x in C.diagonal())
        matrix_ok &= ok
        all_nonzero &= nz
        controls.append({
            "j": str(jv),
            "m": [str(x) for x in ms],
            "C_shape_diag": [str(x) for x in C.diagonal()],
            "invertible_shape": bool(nz and C.det() != 0),
            "relative_operator_ok": bool(ok),
        })

    valid = bool(symbolic_ok and matrix_ok and all_nonzero)
    return {
        "iteration": "Iter076V",
        "lane": "B",
        "valid": valid,
        "branch_leading_scale_ratio_minus_over_plus": str(branch_ratio),
        "symbolic_m_step_ratio": str(step_ratio),
        "expected_m_step_ratio": str(sp.factor(expected_step)),
        "symbolic_relations_ok": bool(symbolic_ok),
        "relative_operator": "i*gamma*J_z",
        "controls": controls,
    }


def lane_c():
    rows = []
    all_ok = True
    for jv in [sp.Rational(1,2), sp.Integer(1), sp.Rational(3,2), sp.Integer(2)]:
        _, C = leading_shape(jv)
        Jz = Jz_matrix(jv)
        D = C * (I * gamma * Jz)

        # Identity-axis control.
        rel_z_l = C.inv() * D
        rel_z_r = D * C.inv()
        z_ok = exact_zero_matrix(rel_z_l - I * gamma * Jz) and exact_zero_matrix(rel_z_r - I * gamma * Jz)

        # Opposite-axis exact SU(2) rotation by pi around y.
        U = Ry_pi(jv)
        Uinv = U.inv()
        Cminus = sp.simplify(U * C * Uinv)
        Dminus = sp.simplify(U * D * Uinv)
        Jminus = sp.simplify(U * Jz * Uinv)
        axis_ok = exact_zero_matrix(Jminus + Jz)
        rel_minus_l = sp.simplify(Cminus.inv() * Dminus)
        rel_minus_r = sp.simplify(Dminus * Cminus.inv())
        opposite_ok = (
            axis_ok
            and exact_zero_matrix(rel_minus_l + I * gamma * Jz)
            and exact_zero_matrix(rel_minus_r + I * gamma * Jz)
        )

        # Generic conjugation identity control with an exact invertible matrix.
        d = C.rows
        Uc = sp.eye(d)
        if d >= 2:
            Uc[0, 1] = 1
        Cc = Uc * C * Uc.inv()
        Dc = Uc * D * Uc.inv()
        Jc = Uc * Jz * Uc.inv()
        generic_conjugation_ok = (
            exact_zero_matrix(Cc.inv() * Dc - I * gamma * Jc)
            and exact_zero_matrix(Dc * Cc.inv() - I * gamma * Jc)
        )
        ok = z_ok and opposite_ok and generic_conjugation_ok
        all_ok &= ok
        rows.append({
            "j": str(jv),
            "z_axis_ok": bool(z_ok),
            "opposite_axis_J_is_minus_Jz": bool(axis_ok),
            "opposite_axis_relative_operator_is_minus_i_gamma_Jz": bool(opposite_ok),
            "generic_conjugation_identity_ok": bool(generic_conjugation_ok),
        })

    return {
        "iteration": "Iter076V",
        "lane": "C",
        "valid": bool(all_ok),
        "controls": rows,
        "arbitrary_axis_rule": "C_n^-1 D_n = D_n C_n^-1 = i*gamma*J_n",
        "compact_tangential_derivative_inferred": False,
    }


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


def lane_d():
    spin_controls = [
        (sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2)),
        (sp.Rational(1,2), sp.Integer(1), sp.Rational(1,2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    rows = []
    all_ok = True
    total_intertwiners = 0
    for spins in spin_controls:
        common_k = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in common_k:
            state = build_intertwiner(*spins, k)
            total_intertwiners += 1
            nonzero = bool(state)
            support_ok = nonzero and all(sp.simplify(sum(ms)) == 0 for ms in state)
            jz_ok = nonzero and all(sp.simplify(sum(ms) * c) == 0 for ms, c in state.items())
            jp = apply_total_ladder(state, spins, "+") if nonzero else {"bad": 1}
            jm = apply_total_ladder(state, spins, "-") if nonzero else {"bad": 1}
            jp_ok = len(jp) == 0
            jm_ok = len(jm) == 0
            boost_z_ok = jz_ok
            arbitrary_axis_ok = jz_ok and jp_ok and jm_ok
            ok = nonzero and support_ok and jz_ok and jp_ok and jm_ok and boost_z_ok and arbitrary_axis_ok
            all_ok &= ok
            rows.append({
                "spins": [str(x) for x in spins],
                "k": str(k),
                "nonzero_components": len(state),
                "magnetic_support_sum_zero": bool(support_ok),
                "total_Jz_annihilates": bool(jz_ok),
                "total_Jplus_annihilates": bool(jp_ok),
                "total_Jminus_annihilates": bool(jm_ok),
                "node5_common_boost_onejet_zero": bool(arbitrary_axis_ok),
            })

    locks = {
        "node_common_boost_onejet_killed_by_intertwiner": bool(all_ok),
        "causal_branch_independent": True,
        "compact_tangential_onejet_established": False,
        "full_source_onejet_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = bool(all_ok and total_intertwiners == 7 and not any(v for k, v in locks.items() if k not in {"node_common_boost_onejet_killed_by_intertwiner", "causal_branch_independent"}) and locks["node_common_boost_onejet_killed_by_intertwiner"] and locks["causal_branch_independent"])
    return {
        "iteration": "Iter076V",
        "lane": "D",
        "valid": valid,
        "intertwiners_checked": total_intertwiners,
        "controls": rows,
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
            if obj.get("iteration") == "Iter076V" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076V_RELATIVE_TOLLER_BOOST_ONEJET_IS_I_GAMMA_J_AND_SU2_INTERTWINER_KILLS_NODE_COMMON_BOOST_EXACT_SCOPED"
        if valid
        else "ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076V",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "After leading singular matrix extraction, the gamma-simple Toller boost-normal relative one-jet is "
            "i*gamma*J_n on either causal branch. A common boost of source node 5 inserts total J_n and is "
            "annihilated by every SU(2)-invariant boundary intertwiner. Compact tangential one-jets remain open."
        ),
        "next_admissible_gate": (
            "Audit compact/rotation tangential variations of the extracted leading singular matrix on the SU(2) "
            "locus and determine whether they are pure intertwiner gauge directions or independent source one-jet data."
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
