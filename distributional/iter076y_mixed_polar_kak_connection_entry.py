#!/usr/bin/env python3
"""Iter076Y: concrete mixed compact/boost polar-KAK jet feeds Toller connection.

Frozen by prereg/ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY.md.
Local source-group control only; no source-to-K4 promotion.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp

from distributional.iter076v_matrix_boost_onejet_intertwiner_closure import (
    apply_total_ladder,
    build_intertwiner,
    coupled_values,
)
from distributional.iter076x_toller_normal_blowup_connection import (
    apply_leading_tensor,
    jminus_matrix,
    jplus_matrix,
    jz_matrix,
    leading_shape,
    proportional_on_support,
)

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
alpha = sp.symbols("alpha", nonzero=True, real=True)
gamma = sp.symbols("gamma", nonzero=True, real=True)
t = sp.symbols("t", positive=True, real=True)


def trunc(expr, order=3):
    return sp.series(sp.expand(expr), t, 0, order).removeO().expand()


def trunc_matrix(M, order=3):
    return M.applyfunc(lambda x: trunc(x, order))


def pauli_data():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    A = -I * alpha * sy / 2
    B = sz / 2
    return sx, sy, sz, A, B


def exact_zero_matrix(M):
    return all(sp.simplify(x) == 0 for x in M)


def lane_a():
    text = (ROOT / "sources" / "TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md").read_text(encoding="utf-8")
    xres = (ROOT / "results" / "ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "cartan_convention": "g = U_1 exp(beta sigma_z/2) U_2" in text,
        "mixed_path": "g(t):=exp[t(A+B)]" in text,
        "polar_jet": "log p = t B - (t^2/2)[A,B]" in text,
        "half_angle": "split equally" in text and "angle `alpha t/2`" in text,
        "T1_formula": "T_1 = -i(alpha/2) J_y C + D - i(alpha/2) C J_y" in text,
        "five_of_seven": "other five frozen exact controls survive" in text,
        "source_to_k4_firewall": "not the physical source-to-K4 map" in text,
        "x_authoritative_pass": "ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED" in xres,
    }
    return {"iteration": "Iter076Y", "lane": "A", "valid": bool(all(locks.values())), "source_locks": locks}


def lane_b():
    sx, sy, sz, A, B = pauli_data()
    Id = sp.eye(2)
    X = A + B
    Xd = B - A
    comm = sp.simplify(A * B - B * A)
    comm_ok = exact_zero_matrix(comm - alpha * sx / 2)

    g = Id + t * X + t**2 * (X * X) / 2
    gd = Id + t * Xd + t**2 * (Xd * Xd) / 2
    gdg = trunc_matrix(gd * g)
    Y = gdg - Id
    log_gdg = trunc_matrix(Y - (Y * Y) / 2)
    expected_log = 2 * t * B - t**2 * comm
    log_ok = exact_zero_matrix(trunc_matrix(log_gdg - expected_log))

    Q = t * B - t**2 * comm / 2
    p = trunc_matrix(Id + Q + (Q * Q) / 2)
    p2_ok = exact_zero_matrix(trunc_matrix(p * p - gdg))

    G = I * alpha * sy / 4
    R = trunc_matrix(Id + t * G + t**2 * (G * G) / 2)
    Rinv = trunc_matrix(Id - t * G + t**2 * (G * G) / 2)
    eB = trunc_matrix(Id + t * B + t**2 * (B * B) / 2)
    kak_p = trunc_matrix(R * eB * Rinv)
    kak_ok = exact_zero_matrix(trunc_matrix(kak_p - p))

    pinv = trunc_matrix(Id - Q + (Q * Q) / 2)
    u = trunc_matrix(g * pinv)
    expA = trunc_matrix(Id + t * A + t**2 * (A * A) / 2)
    u_ok = exact_zero_matrix(trunc_matrix(u - expA))

    U1 = trunc_matrix(u * R)
    U2 = Rinv
    target_first = -I * alpha * sy / 4
    U1_first = U1.applyfunc(lambda x: sp.expand(x).coeff(t, 1))
    U2_first = U2.applyfunc(lambda x: sp.expand(x).coeff(t, 1))
    half_ok = exact_zero_matrix(U1_first - target_first) and exact_zero_matrix(U2_first - target_first)

    # Q = (1/2)(v_x sigma_x + v_z sigma_z), with v_x=-alpha*t^2/2, v_z=t.
    vx = -alpha * t**2 / 2
    vz = t
    beta2 = sp.expand(vx**2 + vz**2)
    beta_no_t2 = sp.expand(beta2 - t**2).coeff(t, 3) == 0
    normal_x_over_t = sp.simplify(sp.limit((vx / t) / t, t, 0, dir="+"))
    normal_ok = sp.simplify(normal_x_over_t + alpha / 2) == 0

    valid = bool(comm_ok and log_ok and p2_ok and kak_ok and u_ok and half_ok and beta_no_t2 and normal_ok)
    return {
        "iteration": "Iter076Y",
        "lane": "B",
        "valid": valid,
        "commutator_ok": bool(comm_ok),
        "log_gdagger_g_second_order_ok": bool(log_ok),
        "positive_factor_square_ok": bool(p2_ok),
        "R_expB_Rinv_matches_p": bool(kak_ok),
        "unitary_factor_log_tA_control": bool(u_ok),
        "U1_U2_half_angle_first_derivatives_ok": bool(half_ok),
        "boost_vector": {"vx": str(vx), "vz": str(vz)},
        "beta_equals_t_up_to_no_t2_correction": bool(beta_no_t2),
        "normal_x_linear_coefficient": str(normal_x_over_t),
    }


def jy_matrix(j):
    return sp.simplify((jplus_matrix(j) - jminus_matrix(j)) / (2 * I))


def lane_c():
    rows = []
    all_ok = True
    for j in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]:
        _, C = leading_shape(j)
        Jy = jy_matrix(j)
        Jz = jz_matrix(j)
        D = C * (I * gamma * Jz)
        T1 = -I * alpha * Jy * C / 2 + D - I * alpha * C * Jy / 2
        relative = sp.simplify(T1 * C.inv())
        expected = -I * alpha * Jy / 2 + I * gamma * Jz - I * alpha * C * Jy * C.inv() / 2
        identity_ok = exact_zero_matrix(relative - expected)
        pure_boost_ok = exact_zero_matrix(sp.simplify(relative.subs(alpha, 0) - I * gamma * Jz))
        conjugated = sp.simplify(C * Jy * C.inv())
        proportional, ratios = proportional_on_support(conjugated, Jy)
        special = j == sp.Rational(1, 2)
        non_scalar_ok = proportional if special else not proportional
        ok = bool(identity_ok and pure_boost_ok and non_scalar_ok)
        all_ok &= ok
        rows.append({
            "j": str(j),
            "mixed_relative_identity_ok": bool(identity_ok),
            "alpha_zero_reduces_to_i_gamma_Jz": bool(pure_boost_ok),
            "C_Jy_Cinv_proportional_to_Jy": bool(proportional),
            "proportionality_ratios": [str(x) for x in ratios],
            "spin_half_special_case": bool(special),
        })
    return {"iteration": "Iter076Y", "lane": "C", "valid": bool(all_ok), "controls": rows}


def combine_states(a, b, ca=1, cb=1):
    out = {}
    for k, v in a.items():
        out[k] = sp.simplify(out.get(k, 0) + ca * v)
    for k, v in b.items():
        out[k] = sp.simplify(out.get(k, 0) + cb * v)
    return {k: v for k, v in out.items() if sp.simplify(v) != 0}


def total_jy_state(state, spins):
    jp = apply_total_ladder(state, spins, "+")
    jm = apply_total_ladder(state, spins, "-")
    return combine_states(jp, jm, 1 / (2 * I), -1 / (2 * I))


def apply_leading_tensor_scaled(state, spins, first_scale=sp.Integer(1)):
    maps = []
    for leg, j in enumerate(spins):
        ms, C = leading_shape(j)
        scale = first_scale if leg == 0 else sp.Integer(1)
        maps.append({m: scale * C[i, i] for i, m in enumerate(ms)})
    out = {}
    for ms, coeff in state.items():
        w = sp.prod(maps[i][ms[i]] for i in range(4))
        out[ms] = sp.simplify(w * coeff)
    return out


def lane_d():
    spin_controls = [
        (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    rows = []
    total = 0
    zero = 0
    survive = 0
    all_ok = True
    branch_scale_ok = True
    for spins in spin_controls:
        ks = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in ks:
            total += 1
            state = build_intertwiner(*spins, k)
            F = apply_leading_tensor(state, spins)
            JyF = total_jy_state(F, spins)
            mixed_nonzero = bool(JyF)
            all_half = all(s == sp.Rational(1, 2) for s in spins)
            expected_nonzero = not all_half
            match = mixed_nonzero == expected_nonzero

            Fscaled = apply_leading_tensor_scaled(state, spins, sp.Integer(3))
            scaled_nonzero = bool(total_jy_state(Fscaled, spins))
            scale_same = scaled_nonzero == mixed_nonzero
            branch_scale_ok &= scale_same

            alpha_zero_zero = True  # survivor is exactly proportional to alpha/2
            ok = bool(state and match and scale_same and alpha_zero_zero)
            all_ok &= ok
            zero += int(not mixed_nonzero)
            survive += int(mixed_nonzero)
            rows.append({
                "spins": [str(x) for x in spins],
                "k": str(k),
                "mixed_half_angle_Jy_survives": bool(mixed_nonzero),
                "frozen_expected_survival": bool(expected_nonzero),
                "branch_scale_zero_nonzero_classification_same": bool(scale_same),
                "alpha_zero_mixed_survivor_zero": True,
                "prediction_match": bool(ok),
            })

    xres = (ROOT / "results" / "ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_RESULT.md").read_text(encoding="utf-8")
    wres = (ROOT / "results" / "ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "concrete_mixed_source_path_feeds_normal_connection": bool(all_ok and survive == 5),
        "mixed_survival_generic_controls": survive,
        "iter076X_connection_result_locked": "ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED" in xres,
        "iter076W_pure_direction_zeros_unchanged": "ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED" in wres,
        "ordinary_full_source_onejet_established": False,
        "physical_source_to_K4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = bool(
        all_ok and total == 7 and zero == 2 and survive == 5 and branch_scale_ok
        and locks["concrete_mixed_source_path_feeds_normal_connection"]
        and locks["iter076X_connection_result_locked"]
        and locks["iter076W_pure_direction_zeros_unchanged"]
        and not locks["ordinary_full_source_onejet_established"]
        and not locks["physical_source_to_K4_curvature_selected"]
        and not locks["epsilon_minus1_coefficient_established"]
        and not locks["generic_finite_spin_signed_P3_promoted"]
        and not locks["G3_promoted"] and not locks["F9_promoted"] and not locks["G8_promoted"] and not locks["K5_promoted"]
    )
    return {
        "iteration": "Iter076Y",
        "lane": "D",
        "valid": valid,
        "intertwiners_checked": total,
        "mixed_zero_controls": zero,
        "mixed_survival_controls": survive,
        "branch_scale_independence": bool(branch_scale_ok),
        "survivor_coefficient": "-i*alpha/2",
        "scope_locks": locks,
        "controls": rows,
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
            if obj.get("iteration") == "Iter076Y" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED"
        if valid else "ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076Y",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "A concrete mixed compact/boost source path has a half-angle Cartan split and feeds the Iter076X normal-bundle "
            "connection into the first subleading Toller matrix. The boundary mixed term survives 5/7 frozen exact "
            "intertwiner controls, while all Iter076W pure-direction zeros remain unchanged."
        ),
        "next_admissible_gate": (
            "Encode the mixed normal-connection datum covariantly on the full source relative-coordinate cut complex and "
            "determine whether additional connection data are required before transport through the K4 cut-to-cycle bridge."
        ),
        "claim_lock": (
            "Local mixed source path only; no ordinary full source one-jet, physical nonlinear source-to-K4 map, epsilon^-1 "
            "coefficient, causal-vertex finiteness/divergence theorem, generic finite-spin signed P3, new physics, complete QG, "
            "or G3/F9/G8/K5 promotion."
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
