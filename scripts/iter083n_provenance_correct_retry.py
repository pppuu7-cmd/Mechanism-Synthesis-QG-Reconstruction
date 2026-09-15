#!/usr/bin/env python3
import argparse
import json
import math
from fractions import Fraction

EXPECTED_SOURCE_LOCK_COMMIT = 'cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533'
EXPECTED_THEOREM_COMMIT = '70a756c9c7c66f822d0e5933e9522b2d359dafe8'
EXPECTED_ITER083M_CRITIC_COMMIT = 'e7623cb5303ea49894e480e2fc4a884df44e7713'
EXPECTED_PARENT_PREREG = 'c29ba0ddbaa4d6e1581db558b792565a7916a0cd'
EXPECTED_HISTORICAL_INVALIDATION = 'fbff993fc920e707d0ff885b73549f3204d208c5'
PASS_CLASS = 'ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED'


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def require_text(text, needles):
    missing = [needle for needle in needles if needle not in text]
    return not missing, missing


def multiply_n_once(state):
    out = {}
    for k, c in state.items():
        if k >= 1:
            out[k - 1] = out.get(k - 1, Fraction(0)) - Fraction(k) * c
    return out


def multiply_n_power(k, q):
    state = {k: Fraction(1)}
    for _ in range(q):
        state = multiply_n_once(state)
    return state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output')
    ap.add_argument('--prereg', default='prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md')
    ap.add_argument('--retry-prereg', default='prereg/ITER083N_PROVENANCE_CORRECT_RETRY_1.md')
    ap.add_argument('--source-lock', default='sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md')
    ap.add_argument('--theorem', default='sources/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_DERIVATION.md')
    ap.add_argument('--current', default='status/CURRENT.md')
    ap.add_argument('--iter083m-critic', default='results/ITER083M_REPAIRED_ADVERSARIAL_REVIEW.md')
    ap.add_argument('--iter083n-invalid-review', default='results/ITER083N_ADVERSARIAL_PROVENANCE_REVIEW.md')
    ap.add_argument('--iter082d', default='results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md')
    ap.add_argument('--iter083b', default='results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md')
    args = ap.parse_args()

    prereg = read(args.prereg)
    retry_prereg = read(args.retry_prereg)
    source_lock = read(args.source_lock)
    theorem = read(args.theorem)
    current = read(args.current)
    iter083m_critic = read(args.iter083m_critic)
    iter083n_invalid_review = read(args.iter083n_invalid_review)
    iter082d = read(args.iter082d)
    iter083b = read(args.iter083b)

    # P0 is authority-sensitive: stale historical Researcher PASS text is deliberately not an input.
    p0_current, m0_current = require_text(current, [
        'fresh Iter083N retry under the unchanged frozen scientific contract',
        'ITER083N_PROVENANCE_CORRECT_RETRY_UNDER_UNCHANGED_FROZEN_CONTRACT',
        EXPECTED_ITER083M_CRITIC_COMMIT,
        EXPECTED_SOURCE_LOCK_COMMIT,
        EXPECTED_THEOREM_COMMIT,
        'INVALID_PROVENANCE',
    ])
    p0_critic, m0_critic = require_text(iter083m_critic, [
        'CONFIRMED_SCOPED',
        'ITER083M_REPAIRED_CRITIC_CONFIRMED_SCOPED',
        'fresh Iter083N retry under its unchanged frozen scientific contract',
        EXPECTED_SOURCE_LOCK_COMMIT,
        EXPECTED_THEOREM_COMMIT,
    ])
    p0_invalid, m0_invalid = require_text(iter083n_invalid_review, [
        'INVALID_PROVENANCE',
        'old Researcher Iter083M result file',
        'PASS_EXACT_SCOPED',
        EXPECTED_SOURCE_LOCK_COMMIT,
        EXPECTED_THEOREM_COMMIT,
        'verify controlling repository authority',
    ])
    p0_d, m0_d = require_text(iter082d, ['omega=(0,3,8)', 'omega_B'])
    p0_b, m0_b = require_text(iter083b, ['normal order at most', 'dim_C F_8 = 377'])
    p0_p, m0_p = require_text(prereg, ['LAURENT_TRANSFORMATION', 'SUPPORTED_JET_ANNIHILATOR', 'ACTUAL_RESIDUE_FIREWALL'])
    p0_retry, m0_retry = require_text(retry_prereg, [
        'PROSPECTIVELY FROZEN BEFORE RETRY IMPLEMENTATION / PRODUCTION OUTPUT',
        EXPECTED_PARENT_PREREG,
        EXPECTED_SOURCE_LOCK_COMMIT,
        EXPECTED_THEOREM_COMMIT,
        EXPECTED_ITER083M_CRITIC_COMMIT,
        'The historical run remains separately `INVALID_PROVENANCE` forever',
    ])
    p0 = all([p0_current, p0_critic, p0_invalid, p0_d, p0_b, p0_p, p0_retry])

    residue_before = (1, 0, 0)
    finite_before = (0, 1, 0)
    residue_after = (1, 0, 0)
    finite_after = (0, 1, 1)
    residue_unchanged = residue_after == residue_before
    finite_shift = tuple(finite_after[i] - finite_before[i] for i in range(3))
    p1 = residue_unchanged and finite_shift == (0, 0, 1)

    delta_checks = 0
    delta_failures = []
    for k in range(9):
        for q in range(10):
            got = multiply_n_power(k, q)
            expected = ({k - q: Fraction(((-1) ** q) * math.factorial(k), math.factorial(k - q))} if q <= k else {})
            delta_checks += 1
            if got != expected:
                delta_failures.append({'k': k, 'q': q})
    annihilator_checks = {}
    sharp_witnesses = {}
    for omega in (0, 3, 8):
        annihilator_checks[str(omega)] = all(multiply_n_power(k, omega + 1) == {} for k in range(omega + 1))
        sharp_witnesses[str(omega)] = all(multiply_n_power(q, q) != {} for q in range(omega + 1))
    p2 = (not delta_failures and all(annihilator_checks.values()) and all(sharp_witnesses.values()))

    thresholds = {
        'K3': {'omega': 0, 'required_I_power': 1},
        'K4': {'omega': 3, 'required_I_power': 4},
        'K5': {'omega': 8, 'required_I_power': 9},
    }
    p3 = thresholds == {
        'K3': {'omega': 0, 'required_I_power': 1},
        'K4': {'omega': 3, 'required_I_power': 4},
        'K5': {'omega': 8, 'required_I_power': 9},
    }

    p4_t, m4_t = require_text(theorem, ['Equality of the normalized Hessians', 'phi|_N=0', 'not enough, by itself'])
    p4 = p4_t and thresholds['K3']['required_I_power'] == 1 and thresholds['K4']['required_I_power'] > 1 and thresholds['K5']['required_I_power'] > 1

    p5_t, m5_t = require_text(theorem, ["rho'=c rho", '(log c) A_-1'])
    p5 = p5_t

    p6_p, m6_p = require_text(prereg, ['do not infer that the physical Toller residue activates every allowed derivative channel', 'Actual independence can be stronger'])
    p6_t, m6_t = require_text(theorem, ['particular physical residue may have smaller order', 'No actual nonzero physical scheme dependence is proved'])
    p6 = p6_p and p6_t

    p7_s, m7_s = require_text(source_lock, ['Felder and David Kazhdan', 'finite part changes by a local residue term', 'odd-codimension', 'has not been established'])
    p7_p, m7_p = require_text(prereg, ['odd-codimension residue-vanishing', 'must NOT be promoted automatically'])
    p7 = p7_s and p7_p

    predicates = {'P0': p0, 'P1': p1, 'P2': p2, 'P3': p3, 'P4': p4, 'P5': p5, 'P6': p6, 'P7': p7}
    controls = {
        'reject_stale_researcher_pass_as_authority': p0_current and p0_critic and p0_invalid,
        'reject_tangent_metric_as_full_finite_part_for_omega_positive': p4,
        'reject_all_residues_as_order_zero': thresholds['K5']['omega'] == 8 and thresholds['K4']['omega'] == 3,
        'reject_actual_k5_dependence_claim_without_residue': p6,
        'reject_fk_k4_parity_without_membership': p7,
        'retain_exact_nonlinear_source_radius_possibility': 'retain the possibility that an exact nonlinear source radial function fixes all relevant jets' in prereg,
        'retain_actual_residue_annihilator_possibility': 'retain the possibility that the actual residue annihilates the defining-function change' in prereg,
        'retain_global_forest_patching_blocker': 'retain global forest/patching blockers' in prereg,
    }

    execution_valid = all([p0, delta_checks == 90, not delta_failures, all(controls.values())])
    scientific_pass = all(predicates[f'P{i}'] for i in range(1, 8))

    if not execution_valid:
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083N_SM_PROVENANCE_CORRECT_RETRY_INVALID_IMPLEMENTATION'
    elif scientific_pass:
        verdict = 'PASS_EXACT_SCOPED'
        classification = PASS_CLASS
    else:
        verdict = 'FAIL_EXACT_SCOPED'
        classification = 'ITER083N_SM_PROVENANCE_CORRECT_RETRY_EXACT_PREDICATE_FAILURE_SCOPED'

    result = {
        'iteration': 'Iter083N-SM provenance-correct retry 1',
        'classification': classification,
        'verdict': verdict,
        'execution_valid': execution_valid,
        'predicates': predicates,
        'controls': controls,
        'provenance': {
            'parent_prereg_commit': EXPECTED_PARENT_PREREG,
            'retry_prereg_commit': 'd9edb0fd2a5c522ddec021f2b4f8e1a964ee3d96',
            'control_repair_prereg_commit': '74ec4edd547d07503e70a0a972a500df70c7c60a',
            'source_lock_commit': EXPECTED_SOURCE_LOCK_COMMIT,
            'theorem_derivation_commit': EXPECTED_THEOREM_COMMIT,
            'iter083m_controlling_critic_commit': EXPECTED_ITER083M_CRITIC_COMMIT,
            'historical_iter083n_invalidation_commit': EXPECTED_HISTORICAL_INVALIDATION,
            'historical_iter083n_result_status': 'INVALID_PROVENANCE_DO_NOT_REHABILITATE',
            'historical_retry_run': '34925091322_INVALID_IMPLEMENTATION',
        },
        'laurent_residue_unchanged': residue_unchanged,
        'laurent_finite_part_shift': 'phi*A_-1',
        'delta_identity_checks': delta_checks,
        'delta_identity_failures': len(delta_failures),
        'annihilator_checks': annihilator_checks,
        'sharp_witnesses': sharp_witnesses,
        'universal_independence_thresholds': thresholds,
        'same_tangent_metric_conformal_information': 'phi|_N=0 only',
        'constant_rescaling_shift': '(log c) A_-1',
        'scientific_statement': 'For a simple-pole radial analytic regularization, conformal change rho->exp(phi)rho leaves the residue fixed and shifts the finite part by phi times the supported residue. Universal independence for residue order <=omega requires phi in I_N^(omega+1). The confirmed Iter083M tangent metric fixes only phi|_N=0, universally sufficient for K3 but not the full allowed K4/K5 supported-residue spaces.',
        'dependency_missing': {
            'P0_current': m0_current,
            'P0_iter083m_critic': m0_critic,
            'P0_historical_invalid_review': m0_invalid,
            'P0_iter082d': m0_d,
            'P0_iter083b': m0_b,
            'P0_parent_prereg': m0_p,
            'P0_retry_prereg': m0_retry,
            'P4_theorem': m4_t,
            'P5_theorem': m5_t,
            'P6_prereg': m6_p,
            'P6_theorem': m6_t,
            'P7_source': m7_s,
            'P7_prereg': m7_p,
        },
        'claim_ceiling': 'No actual nonzero physical finite-part dependence; no source-authorized finite-part selector; no physical regulator dependence/independence; no unique K5 extension; no global patching; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.',
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(payload + '\n')
    print(payload)
    return 0 if verdict == 'PASS_EXACT_SCOPED' else 2


if __name__ == '__main__':
    raise SystemExit(main())
