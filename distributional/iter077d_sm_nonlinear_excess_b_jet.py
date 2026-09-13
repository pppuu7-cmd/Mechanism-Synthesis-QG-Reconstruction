#!/usr/bin/env python3
"""Iter077D-SM: exact nonlinear excess B-jet on the frozen rank-9 source stratum.

Frozen by prereg/ITER077D_SM_NONLINEAR_EXCESS_B_JET.md.
Scientific FAIL is preserved as valid output; only object/provenance invalidity exits nonzero.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
T = sp.symbols("t", real=True)
SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Y = sp.Matrix([[0, -I], [I, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
IDENTITY = sp.eye(2)
ZX = sp.Matrix([1, 1])


def trunc(expr, order):
    return sp.series(sp.expand(expr), T, 0, order + 1).removeO().expand()


def matrix_trunc(M, order):
    return M.applyfunc(lambda x: trunc(x, order))


def exp_series(M, coefficient, order):
    out = sp.zeros(2)
    for k in range(order + 1):
        out += (coefficient * T) ** k * (M ** k) / sp.factorial(k)
    return matrix_trunc(out, order)


def relative_H(A, B, order):
    """H=(g_b^-1 g_a)(g_b^-1 g_a)^dagger for Hermitian A,B."""
    left = exp_series(B, -sp.Rational(1, 2), order)
    middle = exp_series(A, 1, order)
    return matrix_trunc(left * middle * left, order)


def source_B_series(A, B, spinor, order):
    H = relative_H(A, B, order)
    norm = sp.simplify((spinor.conjugate().T * spinor)[0])
    q = trunc((spinor.conjugate().T * H * spinor)[0] / norm, order)
    return sp.series(sp.log(q), T, 0, order + 1).removeO().expand()


def pauli_vec(x, y, z):
    return x * SIGMA_X + y * SIGMA_Y + z * SIGMA_Z


def lane_a():
    prereg = (ROOT / "prereg" / "ITER077D_SM_NONLINEAR_EXCESS_B_JET.md").read_text(encoding="utf-8")
    source = (ROOT / "sources" / "ITER077D_SM_NONLINEAR_EXCESS_B_JET_DERIVATION.md").read_text(encoding="utf-8")
    c_result = (ROOT / "results" / "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md").read_text(encoding="utf-8")
    current = (ROOT / "status" / "CURRENT.md").read_text(encoding="utf-8")
    locks = {
        "source_eq32": "B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)" in source,
        "rank9_witness": "xxxxxyyyzz" in prereg and "xxxxxyyyzz" in c_result,
        "self_stress": "lambda=(1,-1,0,0,1,0,0,0,0,0)" in prereg and "lambda=(1,-1,0,0,1,0,0,0,0,0)" in c_result,
        "right_kernel_coordinates": "x_1=b e_y+a e_z" in prereg and "x_2=x_3=x_4=b e_y+c e_z" in prereg,
        "no_scalar_surrogate": "no scalar incidence surrogate" in prereg,
        "no_symmetry_higher_zero": "no symmetry-only argument" in prereg,
        "epsilon_lock": "published spectral `i epsilon`" in prereg,
        "current_source_front": "TRUE_SOURCE_B_MAP_EXCEPTIONAL_CONTACT_PULLBACK" in current,
    }
    valid = bool(all(locks.values()))
    return {"iteration": "Iter077D-SM", "lane": "A", "valid": valid, "scientific_outcome": "VALID" if valid else "BLOCKED", "locks": locks}


def lane_b():
    ax, ay, az, bx, by, bz = sp.symbols("ax ay az bx by bz", real=True)
    nx, ny, nz = sp.symbols("nx ny nz", real=True)
    A = pauli_vec(ax, ay, az)
    B = pauli_vec(bx, by, bz)
    D = sp.simplify(A - B)
    H = relative_H(A, B, 2)
    target_H = matrix_trunc(IDENTITY + T * D + T**2 * (D * D) / 2, 2)
    h_ok = all(sp.simplify(H[r, c] - target_H[r, c]) == 0 for r in range(2) for c in range(2))

    # Bloch-state expectation via rho=(I+n.sigma)/2.
    rho = (IDENTITY + pauli_vec(nx, ny, nz)) / 2
    q = trunc(sp.trace(rho * H), 2)
    dvec = sp.Matrix([ax - bx, ay - by, az - bz])
    nvec = sp.Matrix([nx, ny, nz])
    nd = sp.expand((nvec.T * dvec)[0])
    d2 = sp.expand((dvec.T * dvec)[0])
    target_q = 1 + T * nd + T**2 * d2 / 2
    q_ok = sp.simplify(q - target_q) == 0
    blog = sp.series(sp.log(q), T, 0, 3).removeO().expand()
    target_blog = sp.expand(T * nd + T**2 * (d2 - nd**2) / 2)
    b_ok = sp.simplify(blog - target_blog) == 0
    valid = bool(h_ok and q_ok and b_ok)
    return {
        "iteration": "Iter077D-SM",
        "lane": "B",
        "valid": valid,
        "scientific_outcome": "VALID" if valid else "BLOCKED",
        "relative_H_second_order_exact": bool(h_ok),
        "bloch_expectation_second_order_exact": bool(q_ok),
        "source_B_second_order_exact": bool(b_ok),
        "B_series": str(sp.collect(blog, T)),
        "target_B_series": str(sp.collect(target_blog, T)),
    }


def frozen_phi(order=4):
    a, b, c = sp.symbols("a b c", real=True)
    X0 = sp.zeros(2)
    X1 = pauli_vec(0, b, a)
    X2 = pauli_vec(0, b, c)
    # X3=X4=X2 on the frozen right-kernel family, but lambda has support only 01,02,12.
    B01 = source_B_series(X0, X1, ZX, order)  # source orientation g_1^-1 g_0
    B02 = source_B_series(X0, X2, ZX, order)
    B12 = source_B_series(X1, X2, ZX, order)
    phi = sp.expand(B01 - B02 + B12)
    return a, b, c, sp.collect(phi, T), B01, B02, B12


def hessian_of_quadratic(q, variables):
    return sp.Matrix([[sp.diff(q, x, y) for y in variables] for x in variables])


def lane_c():
    a, b, c, phi, _, _, _ = frozen_phi(4)
    coeffs = {k: sp.factor(sp.expand(phi).coeff(T, k)) for k in range(1, 5)}
    expected = {
        1: sp.Integer(0),
        2: a * (a - c),
        3: sp.Integer(0),
        4: -(a - c) * (a**3 - a**2 * c + 2 * a * c**2 + 2 * b**2 * c) / 6,
    }
    coefficient_checks = {str(k): sp.simplify(coeffs[k] - expected[k]) == 0 for k in range(1, 5)}
    q2 = sp.expand(coeffs[2])
    H = hessian_of_quadratic(q2, (a, b, c))
    expected_H = sp.Matrix([[2, 0, -1], [0, 0, 0], [-1, 0, 0]])
    hessian_ok = H == expected_H
    rank = H.rank()
    eig = H.eigenvals()
    expected_eigs = {sp.Integer(0): 1, 1 - sp.sqrt(2): 1, 1 + sp.sqrt(2): 1}
    eig_ok = eig == expected_eigs
    inertia = {"positive": 1, "negative": 1, "zero": 1} if eig_ok else None
    prediction_pass = bool(all(coefficient_checks.values()) and hessian_ok and rank == 2 and eig_ok)
    return {
        "iteration": "Iter077D-SM",
        "lane": "C",
        "valid": True,
        "scientific_outcome": "PASS" if prediction_pass else "FAIL",
        "classification": "ITER077D_SM_RANK9_EXCESS_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_SCOPED" if prediction_pass else "ITER077D_SM_FROZEN_NONLINEAR_EXCESS_JET_PREDICTION_FAILS_EXACT_SCOPED",
        "phi_through_t4": str(phi),
        "coefficients": {str(k): str(coeffs[k]) for k in coeffs},
        "frozen_coefficient_checks": coefficient_checks,
        "quadratic_hessian": [[str(H[r, col]) for col in range(3)] for r in range(3)],
        "hessian_matches_frozen": bool(hessian_ok),
        "hessian_rank_Q": int(rank),
        "hessian_eigenvalues": {str(k): int(v) for k, v in eig.items()},
        "eigenvalue_set_matches_frozen": bool(eig_ok),
        "inertia": inertia,
    }


def lane_d():
    a, b, c, phi, B01, B02, B12 = frozen_phi(4)
    # D1 is an exact group identity, not a finite-order inference.
    diagonal_group_equality = True  # a=c implies X1=X2 by frozen definitions.
    diagonal_B12_identity = diagonal_group_equality  # then g_2^-1 g_1=I -> B12=0 exactly.
    diagonal_root_equality = diagonal_group_equality  # same group and same z_x -> B01=B02 exactly.
    diagonal_phi_identity = diagonal_B12_identity and diagonal_root_equality

    phi_a0 = sp.collect(sp.expand(phi.subs(a, 0)), T)
    coeffs_a0 = {k: sp.factor(sp.expand(phi_a0).coeff(T, k)) for k in range(1, 5)}
    quartic_expected = b**2 * c**2 / 3
    a0_lower_zero = all(sp.simplify(coeffs_a0[k]) == 0 for k in (1, 2, 3))
    a0_quartic_ok = sp.simplify(coeffs_a0[4] - quartic_expected) == 0
    quartic_generic_nonzero = sp.simplify(quartic_expected) != 0
    quartic_square_form = sp.factor(quartic_expected) == b**2 * c**2 / 3

    # D3 is contained in the exact a=c diagonal plane.
    pure_b_exact_flat = diagonal_phi_identity
    finite_series_diagonal_check = sp.simplify(phi.subs(c, a)) == 0
    finite_series_pure_b_check = sp.simplify(phi.subs({a: 0, c: 0})) == 0

    prediction_pass = bool(
        diagonal_phi_identity
        and finite_series_diagonal_check
        and a0_lower_zero
        and a0_quartic_ok
        and quartic_generic_nonzero
        and quartic_square_form
        and pure_b_exact_flat
        and finite_series_pure_b_check
    )
    return {
        "iteration": "Iter077D-SM",
        "lane": "D",
        "valid": True,
        "scientific_outcome": "PASS" if prediction_pass else "FAIL",
        "classification": "ITER077D_SM_EXACT_DIAGONAL_FLAT_PLANE_AND_QUARTIC_LIFTED_SECOND_ISOTROPIC_BRANCH_EXACT_SCOPED" if prediction_pass else "ITER077D_SM_FROZEN_NONLINEAR_EXCESS_JET_PREDICTION_FAILS_EXACT_SCOPED",
        "D1_exact_group_equality_a_eq_c": bool(diagonal_group_equality),
        "D1_B12_zero_exact": bool(diagonal_B12_identity),
        "D1_B01_equals_B02_exact": bool(diagonal_root_equality),
        "D1_phi_zero_exact": bool(diagonal_phi_identity),
        "D1_series_crosscheck_through_t4": bool(finite_series_diagonal_check),
        "D2_phi_a0_through_t4": str(phi_a0),
        "D2_coefficients": {str(k): str(coeffs_a0[k]) for k in coeffs_a0},
        "D2_lower_orders_zero": bool(a0_lower_zero),
        "D2_quartic_coefficient": str(coeffs_a0[4]),
        "D2_quartic_expected": str(quartic_expected),
        "D2_quartic_match": bool(a0_quartic_ok),
        "D2_quartic_generically_nonzero_for_nonzero_b_c": bool(quartic_generic_nonzero),
        "D3_pure_b_axis_exact_flat": bool(pure_b_exact_flat),
        "D3_series_crosscheck_through_t4": bool(finite_series_pure_b_check),
    }


def aggregate(aggregate_dir: Path):
    lanes = {}
    for p in aggregate_dir.glob("**/iter077d_sm_*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        lane = data.get("lane")
        if lane in {"A", "B", "C", "D"}:
            lanes[lane] = data
    present = set(lanes) == {"A", "B", "C", "D"}
    ab_valid = present and lanes["A"].get("valid") and lanes["B"].get("valid")
    cd_valid = present and lanes["C"].get("valid") and lanes["D"].get("valid")
    if ab_valid and cd_valid:
        if lanes["C"].get("scientific_outcome") == "PASS" and lanes["D"].get("scientific_outcome") == "PASS":
            verdict = "PASS"
            classification = "ITER077D_SM_RANK9_EXCESS_CONSTRAINT_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_DIAGONAL_FLAT_PLANE_AND_QUARTIC_LIFTED_SECOND_ISOTROPIC_BRANCH_EXACT_SCOPED"
        else:
            verdict = "FAIL"
            classification = "ITER077D_SM_FROZEN_NONLINEAR_EXCESS_JET_PREDICTION_FAILS_EXACT_SCOPED"
        execution_valid = True
    else:
        verdict = "BLOCKED"
        classification = "ITER077D_SM_NONLINEAR_EXCESS_B_JET_BLOCKED_OBJECT_DEFINITION"
        execution_valid = False
    return {
        "iteration": "Iter077D-SM",
        "execution_valid": bool(execution_valid),
        "verdict": verdict,
        "classification": classification,
        "lanes_found": sorted(lanes),
        "lane_valid": {k: bool(lanes[k].get("valid")) for k in sorted(lanes)},
        "lane_scientific_outcomes": {k: lanes[k].get("scientific_outcome") for k in sorted(lanes)},
        "quadratic_hessian_rank_Q": lanes.get("C", {}).get("hessian_rank_Q"),
        "quadratic_inertia": lanes.get("C", {}).get("inertia"),
        "exact_diagonal_flat_plane": lanes.get("D", {}).get("D1_phi_zero_exact"),
        "second_isotropic_branch_quartic_coefficient": lanes.get("D", {}).get("D2_quartic_coefficient"),
        "next_admissible_gate": "Use the frozen non-Morse excess germ to formulate a local source-contact pullback/scaling test that treats the exact flat diagonal plane and the quartically lifted isotropic branch explicitly; do not jump to a full-vertex finiteness or epsilon^-1 claim.",
        "claim_lock": "No full causal-vertex finiteness/divergence theorem, regulator-independence theorem, physical source-to-K4 pushforward, nominal epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=["A", "B", "C", "D"])
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    if args.aggregate_dir:
        out = aggregate(Path(args.aggregate_dir))
    else:
        if not args.lane:
            raise SystemExit("--lane required unless --aggregate-dir is used")
        out = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}[args.lane]()

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))

    # Scientific FAIL is a valid result; only BLOCKED/object-invalid exits nonzero.
    if args.aggregate_dir:
        if not out.get("execution_valid", False):
            raise SystemExit(1)
    elif not out.get("valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
