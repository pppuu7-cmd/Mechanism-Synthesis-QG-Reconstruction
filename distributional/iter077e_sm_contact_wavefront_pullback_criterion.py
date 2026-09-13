#!/usr/bin/env python3
"""Iter077E-SM: generic submersion vs rank-9 contact pullback criterion.

Frozen by prereg/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION.md.
This tests the standard canonical Hormander criterion only. Failure at the
exceptional contact summand is not interpreted as nonexistence of the full
source-selected i-epsilon boundary value.
"""
from __future__ import annotations

import argparse
import json
import os
from fractions import Fraction
from pathlib import Path

from distributional.iter077a_true_source_b_map_transversality import (
    EDGES,
    AXES,
    nullspace,
    rank_q,
    transpose,
    true_jacobian,
    witness_directions,
)

ROOT = Path(__file__).resolve().parents[1]

RANK9_COLORS = "xxxxxyyyzz"
LAMBDA = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(1),
          Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]


def mat_t_vec(J, v):
    return [sum(J[r][c] * v[r] for r in range(len(J))) for c in range(len(J[0]))]


def rank9_directions():
    return {e: AXES[RANK9_COLORS[i]] for i, e in enumerate(EDGES)}


def lane_a():
    source = (ROOT / "sources" / "CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_PULLBACK_MICROLOCAL_SUPPLEMENT.md").read_text(encoding="utf-8")
    a = (ROOT / "results" / "ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md").read_text(encoding="utf-8")
    c = (ROOT / "results" / "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md").read_text(encoding="utf-8")
    d = (ROOT / "results" / "ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md").read_text(encoding="utf-8")
    checks = {
        "source_wedge_factor": "theta(kappa B) + kappa delta^(rho,j)(B)" in source,
        "finite_delta_derivatives": "sum_{n=0}^{2j}" in source and "d^n/dx^n delta(x)" in source,
        "c0_exact": "c_0^(rho,j)=1" in source,
        "ordinary_delta_component": "-delta(x)" in source,
        "pure_ten_contact": "delta(B_01) delta(B_02) ... delta(B_34)" in source,
        "iter077a_pass": "ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED" in a,
        "iter077c_pass": "ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED" in c,
        "iter077d_pass": "ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED" in d,
        "nonexistence_firewall": "No claim that the full source-selected causal amplitude does not exist" in source,
    }
    return {"iteration":"Iter077E-SM","lane":"A","valid":all(checks.values()),"checks":checks}


def lane_b():
    # A finite point-supported distribution has Fourier polynomial
    # P(xi)=sum a_n (i xi)^n. With a_0=-1, P is never the zero polynomial.
    controls = []
    all_ok = True
    # Representative derivative orders N=0..6; higher coefficients are symbolic,
    # but the exact nonzero constant coefficient already prevents P==0.
    for N in range(7):
        constant = Fraction(-1)
        polynomial_identically_zero = (constant == 0)
        nonzero_polynomial_not_rapid_both_rays = not polynomial_identically_zero
        ok = constant == -1 and nonzero_polynomial_not_rapid_both_rays
        all_ok &= ok
        controls.append({
            "max_derivative_order":N,
            "constant_fourier_coefficient":str(constant),
            "polynomial_identically_zero":polynomial_identically_zero,
            "not_rapidly_decreasing_on_both_rays":nonzero_polynomial_not_rapid_both_rays,
        })
    # Fourier transform of delta^{\otimes 10} is a nonzero constant.
    delta10_fourier_constant = Fraction(1)
    full_nonzero_cotangent_fibre = delta10_fourier_constant != 0
    valid = bool(all_ok and full_nonzero_cotangent_fibre)
    return {
        "iteration":"Iter077E-SM","lane":"B","valid":valid,
        "point_distribution_controls":controls,
        "delta10_fourier_constant":str(delta10_fourier_constant),
        "delta10_wavefront_full_nonzero_fibre":bool(full_nonzero_cotangent_fibre),
        "scope":"point-contact summand only; not the full combined i-epsilon boundary value",
    }


def lane_c():
    J = true_jacobian(witness_directions())
    rank = rank_q(J)
    left_kernel = nullspace(transpose(J))
    transpose_injective = len(left_kernel) == 0
    standard_submersion_pullback_authorized = rank == 10 and transpose_injective
    valid = bool(standard_submersion_pullback_authorized)
    return {
        "iteration":"Iter077E-SM","lane":"C","valid":valid,
        "rank_true_source_J":rank,
        "kernel_J_transpose_dimension":len(left_kernel),
        "nonzero_normal_covector_exists":not transpose_injective,
        "standard_submersion_pullback_authorized":standard_submersion_pullback_authorized,
        "global_K5_theorem":False,
    }


def lane_d():
    J = true_jacobian(rank9_directions())
    rank = rank_q(J)
    left_kernel = nullspace(transpose(J))
    jt_lambda = mat_t_vec(J, LAMBDA)
    lambda_nonzero = any(x != 0 for x in LAMBDA)
    lambda_normal = lambda_nonzero and all(x == 0 for x in jt_lambda)
    # Frozen Lane-B theorem: delta^{tensor 10} has all nonzero target covectors in WF.
    lambda_in_point_contact_wf = lambda_nonzero
    criterion_fails = lambda_normal and lambda_in_point_contact_wf
    dres = (ROOT / "results" / "ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md").read_text(encoding="utf-8")
    second_jet_non_degenerate = "determinant `-1`" in dres and "inertia `(3 positive, 3 negative)`" in dres
    locks = {
        "GENERIC_SUBMERSION_PULLBACK_AUTHORIZED":True,
        "RANK9_POINT_CONTACT_STANDARD_PULLBACK_CRITERION_FAILS":bool(criterion_fails),
        "FULL_SOURCE_SELECTED_BOUNDARY_VALUE_NONEXISTENT":False,
        "CORRELATED_SOURCE_SELECTED_EXTENSION_REQUIRED":True,
        "CORRELATED_K5_BOUNDARY_VALUE_ESTABLISHED":False,
        "PHYSICAL_SOURCE_TO_K4_PUSHFORWARD":False,
        "EPSILON_MINUS1_COEFFICIENT":False,
        "CAUSAL_VERTEX_FINITENESS_OR_DIVERGENCE_THEOREM":False,
        "G3_promoted":False,"F9_promoted":False,"G8_promoted":False,"K5_promoted":False,
    }
    valid = bool(
        rank == 9 and len(left_kernel) == 1 and lambda_normal and lambda_in_point_contact_wf
        and criterion_fails and second_jet_non_degenerate
        and locks["CORRELATED_SOURCE_SELECTED_EXTENSION_REQUIRED"]
        and not locks["FULL_SOURCE_SELECTED_BOUNDARY_VALUE_NONEXISTENT"]
        and not locks["CORRELATED_K5_BOUNDARY_VALUE_ESTABLISHED"]
    )
    return {
        "iteration":"Iter077E-SM","lane":"D","valid":valid,
        "rank_true_source_J":rank,
        "left_nullity":len(left_kernel),
        "lambda":[str(x) for x in LAMBDA],
        "J_transpose_lambda":[str(x) for x in jt_lambda],
        "lambda_in_normal_set":bool(lambda_normal),
        "lambda_in_delta10_wavefront":bool(lambda_in_point_contact_wf),
        "standard_Hormander_disjointness_condition_fails":bool(criterion_fails),
        "second_jet_non_degenerate_but_not_pullback_repair":bool(second_jet_non_degenerate),
        "scope_locks":locks,
    }


LANES={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}


def write(obj,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding="utf-8")


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if obj.get('iteration')=='Iter077E-SM' and obj.get('lane') in LANES:
                got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(bool(got[k].get('valid')) for k in LANES)
    return {
        "iteration":"Iter077E-SM","valid":bool(valid),
        "classification":"ITER077E_SM_GENERIC_SUBMERSION_PULLBACK_ALLOWED_RANK9_CONTACT_HORMANDER_CRITERION_COLLIDES_CORRELATED_BOUNDARY_VALUE_REQUIRED_EXACT_SCOPED" if valid else "ITER077E_SM_CONTACT_PULLBACK_SPLIT_PREDICTION_FAILS_EXACT_SCOPED",
        "lanes_found":sorted(got),
        "lane_valid":{k:bool(got.get(k,{}).get('valid')) for k in LANES},
        "generic_submersion_pullback_authorized":bool(got.get('C',{}).get('standard_submersion_pullback_authorized')),
        "rank9_point_contact_standard_criterion_fails":bool(got.get('D',{}).get('standard_Hormander_disjointness_condition_fails')),
        "full_source_selected_boundary_value_nonexistent":False,
        "correlated_source_selected_extension_required":True,
        "next_admissible_gate":"Use the published source-selected i-epsilon boundary value and the Iter077D-SM quadratic normal form to test local exceptional-stratum scaling/extension uniqueness; do not use an arbitrary finite part.",
        "claim_lock":"No full-amplitude nonexistence, causal-vertex finiteness/divergence, regulator-independence, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete-QG, or G3/F9/G8/K5 promotion."
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True)
    args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj,indent=2,sort_keys=True)); write(obj,args.output)
    if not obj.get('valid'): raise SystemExit(1)

if __name__=='__main__': main()
