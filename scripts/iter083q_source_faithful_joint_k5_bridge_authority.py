#!/usr/bin/env python3
import argparse
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE_CRITIC_COMMIT = 'f3e8d7134be751ce74557691b2aae34019b15cab'
PREREG_COMMIT = '4151c02452edd3e5e2c49952686e42e64c6dc180'

EXPECTED_ORDER = [
    'one-wedge spectral/spinor integration',
    'Toller function',
    'product of ten Toller matrices',
    'full 32-component boundary contraction',
    'K5 group integration / distributional extension',
]

FILES = {
    'prereg': 'prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md',
    'derivation': 'sources/ITER083Q_SM_SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_DERIVATION.md',
    'critic_p': 'results/ITER083P_CONTROL_REPAIR_3_ADVERSARIAL_REVIEW.md',
    'iter077i': 'sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md',
    'iter083g': 'sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md',
    'iter083h': 'sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md',
    'iter083j': 'sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md',
    'iter083l': 'sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md',
    'current': 'status/CURRENT.md',
    'critic_handoff': 'status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md',
    'erratum': 'status/ITER077_CONTACT_FORMULA_ERRATUM.md',
}

ANCHORS = {
    'prereg': [
        'B1. Explicit simultaneous ten-wedge analytic/meromorphic or several-variable boundary-value family',
        'B9. The construction defines enough of the actual full boundary-contracted local object',
        'BLOCKED_OBJECT_DEFINITION',
    ],
    'critic_p': [
        'do not supply a source-defined **joint full-K5 meromorphic deformation** or exact source-to-joint-deformation map',
        'boundary completeness of the underlying source object is **not itself missing**',
        'the undeformed source object does have its Haar/group measure',
        'R5: no theorem that a joint deformation preserves the source branch/sign structure and published one-wedge spectral prescription',
        'R6: no full source-ordered K5 Laurent/meromorphic-continuation theorem at the common collision',
        'No actual full-K5 Laurent family, residue distribution, joint boundary value, renormalized product or microlocal multiplication theorem is defined by current authority.',
    ],
    'iter077i': [
        'the causal vertex Eq. (4) is a product of ten Toller matrices followed by four gauge-fixed `SL(2,C)` integrations',
        '`2^5=32`',
        'not the termwise product of ten spinor-contact distributions',
    ],
    'iter083g': [
        'Status: SOURCE/FRAMEWORK LOCK, NOT MSQGR PHYSICAL AUTHORITY',
        'a 10-variable complex-power analytic regularization of the K5 product',
        'a minimal-subtraction/finite-part normalization selecting the 377 supported coefficients',
        'Do not infer that the actual K5 regularized meromorphic germ satisfies all hypotheses',
    ],
    'iter083h': [
        'No full K5 meromorphic continuation theorem',
        'nested K3/K4 subcollisions supply additional pole forms',
    ],
    'iter083j': [
        'Status: FRAMEWORK SOURCE LOCK, NOT LORENTZIAN K5 PHYSICAL AUTHORITY',
        'the connected Lorentzian K5 source automatically requires every regulator coordinate split to factorize',
        'Do not infer a unique physical extension solely from uniqueness of Q inside this framework.',
    ],
    'iter083l': [
        'the published epsilon is a one-wedge spectral prescription in one integration variable `rho_tilde`',
        'It does not introduce a ten-variable analytic collision regulator for the K5 product.',
        'a joint K3/K4/K5 finite-part/subtraction map',
        'a K5 gluing/composition normalization selecting supported extension coefficients',
    ],
    'derivation': [
        'Status: **MISSING_BRIDGE_INGREDIENT**.',
        'Status: **SOURCE_INGREDIENT_PRESENT_BRIDGE_APPLICATION_UNDEFINED**.',
        'Status: **MISSING_APPLICABILITY_BRIDGE**.',
        '`BLOCKED_OBJECT_DEFINITION`.',
    ],
}

B_STATUS = {
    'B1_simultaneous_true_k5_family': 'MISSING_BRIDGE_INGREDIENT',
    'B2_exact_source_to_joint_map': 'MISSING_BRIDGE_INGREDIENT',
    'B3_full_32_boundary_contraction': 'SOURCE_INGREDIENT_PRESENT_BRIDGE_APPLICATION_UNDEFINED',
    'B4_haar_measure_normalization_ordering': 'SOURCE_INGREDIENT_PRESENT_BRIDGE_APPLICATION_UNDEFINED',
    'B5_branch_sign_spectral_compatibility': 'MISSING_BRIDGE_INGREDIENT',
    'B6_applicable_authoritative_continuation_theorem': 'MISSING_APPLICABILITY_BRIDGE',
    'B7_independent_normalization_authority': 'MISSING_BRIDGE_INGREDIENT',
    'B8_bridge_covariance': 'DOWNSTREAM_UNDEFINED_WITHOUT_BRIDGE',
    'B9_actual_local_object_sufficient_for_residue_gate': 'MISSING_BRIDGE_INGREDIENT',
}

ROBUST_MISSING = [
    'B1_simultaneous_true_k5_family',
    'B2_exact_source_to_joint_map',
    'B5_branch_sign_spectral_compatibility',
    'B6_applicable_authoritative_continuation_theorem',
    'B7_independent_normalization_authority',
    'B9_actual_local_object_sufficient_for_residue_gate',
]


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def validate_candidate(c):
    reasons = []
    required = [
        'all_ten_wedges', 'true_k5_incidence', 'exact_source_map', 'full_32_boundary_or_exact_reduction',
        'source_measure_and_order', 'source_branch_spectral_compatibility', 'applicable_joint_theorem',
        'independent_normalization_authority', 'required_covariance', 'actual_local_object_defined',
    ]
    for key in required:
        if c.get(key) is not True:
            reasons.append('missing_' + key)
    forbidden = [
        'representative_component', 'scalar_hodge_cycle_surrogate', 'auxiliary_q_as_physical',
        'termwise_contact_substitution', 'beta_i_epsilon_substitution', 'posthoc_finite_part',
        'preferred_sequential_continuation', 'omits_source_measure', 'omits_true_k5_incidence',
    ]
    for key in forbidden:
        if c.get(key) is True:
            reasons.append('forbidden_' + key)
    if c.get('source_order') != EXPECTED_ORDER:
        reasons.append('wrong_source_order')
    return {'accepted': not reasons, 'reasons': reasons}


def positive_fixture():
    c = {
        'all_ten_wedges': True, 'true_k5_incidence': True, 'exact_source_map': True,
        'full_32_boundary_or_exact_reduction': True, 'source_measure_and_order': True,
        'source_branch_spectral_compatibility': True, 'applicable_joint_theorem': True,
        'independent_normalization_authority': True, 'required_covariance': True,
        'actual_local_object_defined': True, 'source_order': EXPECTED_ORDER,
    }
    return validate_candidate(c)


def negative_controls():
    base = {
        'all_ten_wedges': True, 'true_k5_incidence': True, 'exact_source_map': True,
        'full_32_boundary_or_exact_reduction': True, 'source_measure_and_order': True,
        'source_branch_spectral_compatibility': True, 'applicable_joint_theorem': True,
        'independent_normalization_authority': True, 'required_covariance': True,
        'actual_local_object_defined': True, 'source_order': EXPECTED_ORDER,
    }
    cases = {
        'representative_boundary_component': {'representative_component': True, 'full_32_boundary_or_exact_reduction': False},
        'scalar_k4_k5_hodge_cycle_surrogate': {'scalar_hodge_cycle_surrogate': True, 'true_k5_incidence': False},
        'auxiliary_q_promoted_physical': {'auxiliary_q_as_physical': True, 'independent_normalization_authority': False},
        'termwise_contact_product_pullback': {'termwise_contact_substitution': True, 'source_order': ['termwise contact expansion', 'product', 'pullback']},
        'beta_plus_i_epsilon': {'beta_i_epsilon_substitution': True, 'exact_source_map': False},
        'fitted_posthoc_finite_part': {'posthoc_finite_part': True, 'independent_normalization_authority': False},
        'preferred_sequential_continuation': {'preferred_sequential_continuation': True, 'required_covariance': False},
        'omit_source_haar_measure': {'omits_source_measure': True, 'source_measure_and_order': False},
        'omit_true_k5_incidence': {'omits_true_k5_incidence': True, 'true_k5_incidence': False},
    }
    out = {}
    for name, changes in cases.items():
        c = dict(base)
        c.update(changes)
        v = validate_candidate(c)
        out[name] = {'rejected': not v['accepted'], 'reasons': v['reasons']}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    missing_files = [p for p in FILES.values() if not (ROOT / p).is_file()]
    texts = {k: read(p) for k, p in FILES.items() if (ROOT / p).is_file()}
    anchor_failures = []
    for key, anchors in ANCHORS.items():
        text = texts.get(key, '')
        for anchor in anchors:
            if anchor not in text:
                anchor_failures.append({'file': FILES[key], 'anchor': anchor})

    # Supersession discipline: any newer source/result authority after the qualified
    # Iter083P Critic must be explicitly audited. Current Iter083Q derivation is a
    # derived audit, not independent positive authority.
    delta = [x for x in git('diff', '--name-only', BASE_CRITIC_COMMIT, 'HEAD').splitlines() if x]
    allowed_new_source_result = {FILES['derivation']}
    new_authority_candidates = [
        p for p in delta
        if (p.startswith('sources/') or p.startswith('results/')) and p not in allowed_new_source_result
    ]

    ancestry = {
        'critic_is_ancestor': subprocess.run(['git','merge-base','--is-ancestor',BASE_CRITIC_COMMIT,'HEAD'], cwd=ROOT).returncode == 0,
        'prereg_is_ancestor': subprocess.run(['git','merge-base','--is-ancestor',PREREG_COMMIT,'HEAD'], cwd=ROOT).returncode == 0,
    }

    pos = positive_fixture()
    neg = negative_controls()
    controls_ok = pos['accepted'] and all(v['rejected'] for v in neg.values())
    execution_valid = not missing_files and not anchor_failures and not new_authority_candidates and all(ancestry.values()) and controls_ok

    if not execution_valid:
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083Q_SM_JOINT_K5_BRIDGE_AUTHORITY_AUDIT_INVALID_IMPLEMENTATION'
    elif all(B_STATUS[k] == 'ESTABLISHED' for k in B_STATUS):
        verdict = 'BRIDGE_AUTHORITY_CONFIRMED_SCOPED'
        classification = 'ITER083Q_SM_SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_CONFIRMED_SCOPED'
    elif any(B_STATUS[k].startswith('MISSING') for k in ROBUST_MISSING):
        verdict = 'BLOCKED_OBJECT_DEFINITION'
        classification = 'ITER083Q_SM_SOURCE_FAITHFUL_JOINT_K5_ANALYTIC_MEROMORPHIC_BRIDGE_NOT_CURRENTLY_DEFINED_SCOPED'
    else:
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083Q_SM_JOINT_K5_BRIDGE_AUTHORITY_AUDIT_UNRESOLVED'

    data = {
        'iteration': 'Iter083Q-SM',
        'gate': 'SOURCE_FAITHFUL_JOINT_K5_MEROMORPHIC_OR_MULTIVARIABLE_BOUNDARY_VALUE_BRIDGE_AUTHORITY_GATE',
        'head': git('rev-parse', 'HEAD'),
        'base_critic_commit': BASE_CRITIC_COMMIT,
        'prereg_commit': PREREG_COMMIT,
        'source_order': EXPECTED_ORDER,
        'authority_manifest': [{'path': p, 'sha256': sha(p)} for p in FILES.values() if (ROOT / p).is_file()],
        'missing_files': missing_files,
        'anchor_failures': anchor_failures,
        'delta_since_qualified_critic': delta,
        'new_authority_candidates_requiring_supersession_audit': new_authority_candidates,
        'ancestry': ancestry,
        'predicates': B_STATUS,
        'robust_missing_predicates': ROBUST_MISSING,
        'positive_fixture': {'accepted': pos['accepted'], 'reasons': pos['reasons']},
        'negative_controls': neg,
        'controls_ok': controls_ok,
        'execution_valid': execution_valid,
        'verdict': verdict,
        'classification': classification,
        'claim_locks_preserved': True,
        'next_gate_authorized': verdict == 'BRIDGE_AUTHORITY_CONFIRMED_SCOPED',
    }
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
