#!/usr/bin/env python3
"""Iter076Z: scalar radial strip leaves a nonscalar Toller front-face object.

Frozen by prereg/ITER076Z_TOLLER_FRONT_FACE_NONSCALAR_OBSTRUCTION.md.
This is an exact source-object-definition gate; no physical source-to-K4 pushforward
or epsilon^-1 coefficient is promoted.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import wigner_d_small

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
)

ROOT = Path(__file__).resolve().parents[1]
I = sp.I


def exact_zero_matrix(M):
    return all(sp.simplify(x) == 0 for x in M)


def ascending_y_rotation(j, angle):
    """Exact Wigner small-d rotation in the ascending-m basis used in this repo."""
    Udesc = sp.Matrix(wigner_d_small(j, angle))
    d = Udesc.rows
    P = sp.zeros(d, d)
    for r in range(d):
        P[r, d - 1 - r] = 1
    return sp.simplify(P * Udesc * P)


def proportional(A, B):
    """Return whether A=lambda B for one scalar lambda, plus candidate ratios."""
    ratios = []
    for r in range(B.rows):
        for c in range(B.cols):
            a = sp.simplify(A[r, c])
            b = sp.simplify(B[r, c])
            if b == 0:
                if a != 0:
                    return False, ratios
            else:
                ratios.append(sp.simplify(a / b))
    if not ratios:
        return exact_zero_matrix(A), ratios
    return all(sp.simplify(x - ratios[0]) == 0 for x in ratios), ratios


def state_support_sectors(state):
    return sorted({sp.simplify(sum(ms)) for ms, coeff in state.items() if sp.simplify(coeff) != 0}, key=str)


def total_jy_state(state, spins):
    jp = apply_total_ladder(state, spins, "+")
    jm = apply_total_ladder(state, spins, "-")
    out = {}
    for key, val in jp.items():
        out[key] = sp.simplify(out.get(key, 0) + val / (2 * I))
    for key, val in jm.items():
        out[key] = sp.simplify(out.get(key, 0) - val / (2 * I))
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


def lane_a():
    supplement = (ROOT / "sources" / "TOLLER_FRONT_FACE_NONSCALAR_SUPPLEMENT.md").read_text(encoding="utf-8")
    xres = (ROOT / "results" / "ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_RESULT.md").read_text(encoding="utf-8")
    yres = (ROOT / "results" / "ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY_RESULT.md").read_text(encoding="utf-8")
    locks = {
        "radial_front_face_limit": "beta^(2j+1) T(g) -> C_n" in supplement,
        "boundary_tensor_family": "F_n := i [tensor_e C_{j_e,n}]" in supplement,
        "angular_derivative": "dot F = -i F_z [sum_e J_y^(e)]" in supplement,
        "magnetic_sector_obstruction": "M=+1" in supplement and "M=-1" in supplement and "M=0" in supplement,
        "five_of_seven": "exactly `5/7` frozen controls" in supplement,
        "scalar_taylor_not_source_faithful": "scalar ordinary Taylor-jet formulation" in supplement and "not source-faithful" in supplement,
        "full_blowup_firewall": "does not construct the full blow-up calculus" in supplement,
        "epsilon_firewall": "`epsilon^-1` coefficient" in supplement,
        "x_authoritative_pass": "ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED" in xres,
        "y_authoritative_pass": "ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED" in yres,
    }
    return {
        "iteration": "Iter076Z",
        "lane": "A",
        "valid": bool(all(locks.values())),
        "source_locks": locks,
    }


def lane_b():
    rows = []
    all_ok = True
    angle = sp.pi / 2
    for j in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]:
        _, C = leading_shape(j)
        Jz = jz_matrix(j)
        Jp = jplus_matrix(j)
        Jm = jminus_matrix(j)
        Jy = sp.simplify((Jp - Jm) / (2 * I))
        U = ascending_y_rotation(j, angle)
        Uinv = sp.simplify(U.inv())
        Crot = sp.simplify(U * C * Uinv)

        invertible = C.det() != 0
        stabilizer_ok = exact_zero_matrix(Jz * C - C * Jz)
        rotation_nonconstant = not exact_zero_matrix(Crot - C)
        comm = sp.simplify(Jy * C - C * Jy)
        transverse_nonzero = not exact_zero_matrix(comm)
        comm_prop_C, comm_ratios = proportional(comm, C)
        not_prop_C = not comm_prop_C

        Cm = -C
        Cmrot = sp.simplify(U * Cm * Uinv)
        projective_flip_same = exact_zero_matrix(Cmrot + Crot) and (not exact_zero_matrix(Cmrot - Cm))

        # In the frozen scope even j=1/2 is direction dependent; for j>=1 the
        # commutator must additionally be nonzero and nonscalar relative to C.
        generic_ok = transverse_nonzero and not_prop_C if j >= 1 else rotation_nonconstant
        ok = bool(invertible and stabilizer_ok and rotation_nonconstant and projective_flip_same and generic_ok)
        all_ok &= ok
        rows.append({
            "j": str(j),
            "C_diag": [str(x) for x in C.diagonal()],
            "invertible": bool(invertible),
            "Jz_stabilizer_commutes": bool(stabilizer_ok),
            "transverse_finite_rotation_changes_C": bool(rotation_nonconstant),
            "transverse_commutator_nonzero": bool(transverse_nonzero),
            "transverse_commutator_proportional_to_C": bool(comm_prop_C),
            "commutator_proportionality_ratios": [str(x) for x in comm_ratios],
            "C_to_minus_C_projective_nonconstancy_same": bool(projective_flip_same),
        })
    return {
        "iteration": "Iter076Z",
        "lane": "B",
        "valid": bool(all_ok),
        "controls": rows,
    }


def intertwiner_controls():
    spin_controls = [
        (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
        (sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 2), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)),
    ]
    for spins in spin_controls:
        ks = sorted(set(coupled_values(spins[0], spins[1])) & set(coupled_values(spins[2], spins[3])))
        for k in ks:
            yield spins, k, build_intertwiner(*spins, k)


def lane_c():
    rows = []
    total = 0
    m0_ok_count = 0
    transverse_zero = 0
    transverse_survive = 0
    all_ok = True
    for spins, k, state in intertwiner_controls():
        total += 1
        F = apply_leading_tensor(state, spins)
        sectors_F = state_support_sectors(F)
        jp = apply_total_ladder(F, spins, "+")
        jm = apply_total_ladder(F, spins, "-")
        sectors_p = state_support_sectors(jp)
        sectors_m = state_support_sectors(jm)

        m0_only = sectors_F == [sp.Integer(0)]
        p_sector_ok = (not jp) or sectors_p == [sp.Integer(1)]
        m_sector_ok = (not jm) or sectors_m == [sp.Integer(-1)]
        both_zero = (not jp) and (not jm)
        both_nonzero = bool(jp) and bool(jm)
        all_half = all(s == sp.Rational(1, 2) for s in spins)
        predicted_zero = all_half
        prediction_ok = both_zero if predicted_zero else both_nonzero
        disjoint = set(sectors_F).isdisjoint(set(sectors_p)) and set(sectors_F).isdisjoint(set(sectors_m)) and set(sectors_p).isdisjoint(set(sectors_m))
        ok = bool(state and F and m0_only and p_sector_ok and m_sector_ok and prediction_ok and disjoint)
        all_ok &= ok
        m0_ok_count += int(m0_only)
        transverse_zero += int(both_zero)
        transverse_survive += int(both_nonzero)
        rows.append({
            "spins": [str(x) for x in spins],
            "k": str(k),
            "F_support_M": [str(x) for x in sectors_F],
            "Jplus_support_M": [str(x) for x in sectors_p],
            "Jminus_support_M": [str(x) for x in sectors_m],
            "Jplus_zero": bool(not jp),
            "Jminus_zero": bool(not jm),
            "frozen_special_zero": bool(predicted_zero),
            "magnetic_sectors_pairwise_disjoint": bool(disjoint),
            "prediction_match": bool(ok),
        })

    valid = bool(all_ok and total == 7 and m0_ok_count == 7 and transverse_zero == 2 and transverse_survive == 5)
    return {
        "iteration": "Iter076Z",
        "lane": "C",
        "valid": valid,
        "intertwiners_checked": total,
        "F_M0_only_controls": m0_ok_count,
        "transverse_zero_controls": transverse_zero,
        "transverse_survival_controls": transverse_survive,
        "controls": rows,
    }


def lane_d():
    lam = sp.symbols("lambda")
    rows = []
    total = 0
    surviving = 0
    special = 0
    all_ok = True
    for spins, k, state in intertwiner_controls():
        total += 1
        F = apply_leading_tensor(state, spins)
        JyF = total_jy_state(F, spins)
        all_half = all(s == sp.Rational(1, 2) for s in spins)

        # Build lambda*F + JyF exactly. Any M=+/-1 component is independent of
        # lambda because F has only M=0 support, giving an exact scalar no-go.
        combo = {key: sp.simplify(lam * val) for key, val in F.items()}
        for key, val in JyF.items():
            combo[key] = sp.simplify(combo.get(key, 0) + val)
        combo = {k0: v for k0, v in combo.items() if sp.simplify(v) != 0}
        obstruction = [
            (ms, coeff) for ms, coeff in combo.items()
            if sp.simplify(sum(ms)) != 0 and sp.simplify(coeff).has(lam) is False and sp.simplify(coeff) != 0
        ]

        if all_half:
            special += 1
            expected = not JyF and len(obstruction) == 0
            scalar_flattening_possible_at_first_angular_order = True
        else:
            surviving += 1
            expected = bool(JyF) and len(obstruction) > 0
            scalar_flattening_possible_at_first_angular_order = False
        all_ok &= expected
        rows.append({
            "spins": [str(x) for x in spins],
            "k": str(k),
            "JyF_nonzero": bool(JyF),
            "lambda_independent_nonzero_M_obstruction_components": len(obstruction),
            "scalar_flattening_possible_at_first_angular_order": scalar_flattening_possible_at_first_angular_order,
            "special_all_spin_half": bool(all_half),
            "prediction_match": bool(expected),
        })

    locks = {
        "scalar_front_face_flattening_generic": False,
        "matrix_or_bundle_valued_front_face_required": True,
        "ordinary_scalar_source_numerator_jet_source_faithful": False,
        "smooth_Haar_factor_remains_separate": True,
        "full_ten_wedge_blowup_constructed": False,
        "physical_source_to_K4_pushforward_established": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_P3_promoted": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    valid = bool(
        all_ok and total == 7 and special == 2 and surviving == 5
        and not locks["scalar_front_face_flattening_generic"]
        and locks["matrix_or_bundle_valued_front_face_required"]
        and not locks["ordinary_scalar_source_numerator_jet_source_faithful"]
        and locks["smooth_Haar_factor_remains_separate"]
        and not locks["full_ten_wedge_blowup_constructed"]
        and not locks["physical_source_to_K4_pushforward_established"]
        and not locks["epsilon_minus1_coefficient_established"]
        and not locks["generic_finite_spin_signed_P3_promoted"]
        and not locks["G3_promoted"] and not locks["F9_promoted"] and not locks["G8_promoted"] and not locks["K5_promoted"]
    )
    return {
        "iteration": "Iter076Z",
        "lane": "D",
        "valid": valid,
        "controls": rows,
        "special_scalar_flattenable_controls": special,
        "generic_scalar_no_go_controls": surviving,
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
            if obj.get("iteration") == "Iter076Z" and lane in LANES:
                got[lane] = obj
    valid = set(got) == set(LANES) and all(bool(got[k].get("valid")) for k in LANES)
    classification = (
        "ITER076Z_SCALAR_RADIAL_STRIP_LEAVES_NONSCALAR_DIRECTION_DEPENDENT_TOLLER_FRONT_FACE_BUNDLE_OBJECT_REQUIRED_EXACT_SCOPED"
        if valid else "ITER076Z_TOLLER_FRONT_FACE_NONSCALAR_OBSTRUCTION_CONFIRMATION_FAIL"
    )
    return {
        "iteration": "Iter076Z",
        "valid": bool(valid),
        "classification": classification,
        "lanes_found": sorted(got),
        "lane_valid": {k: bool(got.get(k, {}).get("valid")) for k in LANES},
        "scientific_scope": (
            "After scalar radial power stripping, the generic causal Toller source leaves a direction-dependent matrix/bundle-valued "
            "front-face coefficient. Its transverse angular response occupies total-magnetic M=+/-1 sectors and cannot be canceled "
            "by any scalar direction-dependent normalization in 5/7 frozen exact intertwiner controls."
        ),
        "next_admissible_gate": (
            "Construct the minimal covariant K5 front-face data model (radial weights, normal directions, leading matrices and angular "
            "connection) on the source relative-coordinate cut complex before attempting any K4 cut-to-cycle/Hodge transport."
        ),
        "claim_lock": (
            "No full ten-wedge blow-up, physical source-to-K4 map, epsilon^-1 coefficient, causal-vertex finiteness/divergence theorem, "
            "generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion."
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
