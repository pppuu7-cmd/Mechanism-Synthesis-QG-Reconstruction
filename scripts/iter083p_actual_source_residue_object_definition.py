#!/usr/bin/env python3
import argparse
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

EXPECTED_SOURCE_ORDER = [
    'one-wedge spectral/spinor integration',
    'Toller function',
    'product of ten Toller matrices',
    'full boundary contraction',
    'K5 group integration / distributional extension',
]

PARENT_PREREG = 'prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md'
REPAIR_PREREG = 'prereg/ITER083P_CONTROL_ONLY_REPAIR_1.md'
CRITIC_REVIEW = 'results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md'

MINIMUM_DIRECT_LOCKS = [
    'sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md',
    'sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md',
    'sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md',
    'sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md',
    'sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md',
    'sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md',
    'sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md',
]

FIXED_CORPUS = [
    'status/CURRENT.md',
    'status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md',
    'status/ITER077_CONTACT_FORMULA_ERRATUM.md',
    PARENT_PREREG,
    REPAIR_PREREG,
    CRITIC_REVIEW,
]

PHYSICAL_SOURCE_PREFIXES = (
    'sources/ITER080K_',
    'sources/ITER083E_',
    'sources/ITER083F_',
    'sources/ITER083L_',
    'sources/ITER083M_',
)

NEGATION_MARKERS = (
    ' no ',
    'not ',
    ' does not ',
    'cannot ',
    'without ',
    'missing ',
    'absent ',
    'conditional ',
    'not yet ',
)

REQUIREMENT_SPECS = {
    'R1_full_source_meromorphic_deformation_parameter_and_object': {
        'positive_groups': [
            ('full k5', 'meromorphic', 'family'),
            ('full source', 'analytic family', 'k5'),
        ],
        'negative_anchors': [
            ('sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md', 'a 10-variable complex-power analytic regularization of the K5 product'),
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'edgewise collision-analytic parameters `s_e=1+x_e`'),
            ('sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md', 'No full K5 meromorphic continuation theorem'),
        ],
    },
    'R2_exact_source_to_joint_deformation_map': {
        'positive_groups': [
            ('source', 'map', 'joint', 'deformation'),
            ('toller', 'deformation parameter', 'k5'),
        ],
        'negative_anchors': [
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'a joint K3/K4/K5 finite-part/subtraction map'),
            ('sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md', 'a 10-variable complex-power analytic regularization of the K5 product'),
        ],
    },
    'R3_full_boundary_contracted_residue_map_all_32_or_exact_reduction': {
        'positive_groups': [
            ('residue', 'boundary', '32'),
            ('residue map', 'full boundary contraction', 'exact reduction'),
        ],
        'negative_anchors': [
            ('results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md', 'The frozen object requires all 32 all-spin-half boundary components or an exact authoritative reduction.'),
        ],
    },
    'R4_deformed_full_object_measure_and_normalization': {
        'positive_groups': [
            ('deformed full', 'measure', 'normalization'),
            ('meromorphic', 'haar', 'normalization', 'k5'),
        ],
        'negative_anchors': [
            ('sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md', 'a minimal-subtraction/finite-part normalization selecting the 377 supported coefficients'),
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'a K5 gluing/composition normalization selecting supported extension coefficients'),
        ],
    },
    'R5_joint_deformation_branch_and_published_spectral_compatibility_theorem': {
        'positive_groups': [
            ('joint', 'branch', 'spectral', 'compatibility'),
            ('k5', 'published', 'i epsilon', 'compatibility theorem'),
        ],
        'negative_anchors': [
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'the published epsilon is a one-wedge spectral prescription in one integration variable `rho_tilde`'),
            ('sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md', 'no explicit simultaneous ten-wedge K5 collision extension or correlated joint extension rule is supplied there'),
        ],
    },
    'R6_full_k5_laurent_expansion_theorem_near_collision': {
        'positive_groups': [
            ('full k5', 'laurent', 'collision'),
            ('full k5', 'meromorphic continuation theorem'),
        ],
        'negative_anchors': [
            ('sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md', 'No full K5 meromorphic continuation theorem'),
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'No unique physical extension, no full K5 meromorphic continuation'),
        ],
    },
    'R7_unique_source_identification_of_A_minus_1': {
        'positive_groups': [
            ('a_-1', 'source', 'unique'),
            ('residue coefficient', 'source', 'full k5', 'unique'),
        ],
        'negative_anchors': [
            ('sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md', 'Do not claim the physical Toller residue is nonzero in every supported-jet channel.'),
            ('sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md', 'Do not promote the formal Laurent transformation law to a complete global K5 renormalization theorem.'),
            ('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', 'a K5 gluing/composition normalization selecting supported extension coefficients'),
        ],
    },
}


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def sha256_text(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def relevant_tagged_name(name):
    return bool(re.match(r'^ITER080K_', name) or re.match(r'^ITER083[EFGHIJKLMN]_', name))


def enumerate_corpus():
    paths = set(FIXED_CORPUS)
    for dirname in ('sources', 'results'):
        base = ROOT / dirname
        for p in base.iterdir():
            if p.is_file() and relevant_tagged_name(p.name):
                paths.add(str(p.relative_to(ROOT)))
    status_dir = ROOT / 'status'
    for p in status_dir.iterdir():
        if p.is_file() and re.match(r'^ITER083[MNP]_', p.name):
            paths.add(str(p.relative_to(ROOT)))
    return sorted(paths)


def paragraph_matches(text, terms):
    matches = []
    for para in re.split(r'\n\s*\n', text):
        low = ' ' + para.lower().replace('\n', ' ') + ' '
        if all(term.lower() in low for term in terms):
            if not any(marker in low for marker in NEGATION_MARKERS):
                compact = ' '.join(para.split())
                matches.append(compact[:600])
    return matches


def source_role(path):
    if path.startswith(PHYSICAL_SOURCE_PREFIXES):
        return 'physical_source_authority'
    if path.startswith('sources/'):
        return 'conditional_or_framework_source_control'
    if path.startswith('results/'):
        return 'repository_result_or_review'
    if path.startswith('status/'):
        return 'repository_status_or_handoff'
    if path.startswith('prereg/'):
        return 'prospective_contract'
    return 'other'


def derive_requirements(texts, corpus_paths):
    evidence = {}
    statuses = {}
    physical_paths = [p for p in corpus_paths if source_role(p) == 'physical_source_authority']
    for req, spec in REQUIREMENT_SPECS.items():
        positive_matches = []
        for path in physical_paths:
            text = texts[path]
            for terms in spec['positive_groups']:
                for excerpt in paragraph_matches(text, terms):
                    positive_matches.append({'path': path, 'terms': list(terms), 'excerpt': excerpt})
        negative_matches = []
        for path, anchor in spec['negative_anchors']:
            text = texts.get(path, '')
            if anchor in text:
                negative_matches.append({'path': path, 'anchor': anchor})
        if positive_matches and negative_matches:
            status = 'CONTRADICTORY'
        elif positive_matches:
            status = 'DEFINED'
        else:
            status = 'ABSENT_OR_ONLY_CONDITIONAL'
        evidence[req] = {
            'status': status,
            'positive_matches': positive_matches,
            'negative_or_absence_matches': negative_matches,
            'searched_physical_authority_paths': physical_paths,
            'searched_complete_corpus_paths': corpus_paths,
        }
        statuses[req] = status
    return statuses, evidence


def validate_candidate(requirement_statuses, candidate):
    reasons = []
    if any(requirement_statuses.get(k) != 'DEFINED' for k in REQUIREMENT_SPECS):
        reasons.append('not_all_R1_R7_defined')
    if candidate.get('source_order') != EXPECTED_SOURCE_ORDER:
        reasons.append('wrong_source_order')
    if candidate.get('wedge_count') != 10:
        reasons.append('not_all_ten_wedges')
    if candidate.get('true_k5_incidence') is not True:
        reasons.append('not_true_k5_incidence')
    if candidate.get('boundary_components') != 32 and candidate.get('exact_boundary_reduction_theorem') is not True:
        reasons.append('boundary_incomplete_without_exact_reduction')
    if candidate.get('family_kind') != 'actual_source_ordered_k5_meromorphic_family':
        reasons.append('wrong_or_surrogate_family_kind')
    if candidate.get('source_authorized_measure_normalization') is not True:
        reasons.append('measure_normalization_not_source_authorized')
    if candidate.get('source_authorized_branch_spectral_compatibility') is not True:
        reasons.append('branch_spectral_compatibility_not_source_authorized')
    if candidate.get('posthoc_choice') is True:
        reasons.append('posthoc_choice_forbidden')
    if candidate.get('generic_extension_only') is True:
        reasons.append('generic_extension_not_source_bridge')
    return {'accepted': len(reasons) == 0, 'rejection_reasons': reasons}


def make_candidate(statuses):
    return {
        'source_order': EXPECTED_SOURCE_ORDER,
        'wedge_count': 10,
        'true_k5_incidence': True,
        'boundary_components': 32,
        'exact_boundary_reduction_theorem': False,
        'family_kind': 'actual_source_ordered_k5_meromorphic_family',
        'source_authorized_measure_normalization': statuses.get('R4_deformed_full_object_measure_and_normalization') == 'DEFINED',
        'source_authorized_branch_spectral_compatibility': statuses.get('R5_joint_deformation_branch_and_published_spectral_compatibility_theorem') == 'DEFINED',
        'posthoc_choice': False,
        'generic_extension_only': False,
    }


def synthetic_positive_fixture():
    synthetic_text = '''
FULL K5 meromorphic family. This physical source defines a full K5 meromorphic family constructed from the full source object.

Source map joint deformation. The source defines the exact map from Toller variables to the joint deformation parameter for K5.

Residue boundary 32. The residue map uses the full boundary contraction on all 32 components with no representative-component reduction.

Deformed full measure normalization. The deformed full K5 object uses the source Haar measure and normalization.

Joint branch spectral compatibility. A joint K5 branch and published i epsilon compatibility theorem is part of the definition.

Full K5 Laurent collision. The full K5 object admits a Laurent expansion at the collision.

A_-1 source unique. The full K5 residue coefficient A_-1 is uniquely identified by the source.
'''
    fixture_path = 'sources/SYNTHETIC_ITER083P_POSITIVE_AUTHORITY.md'
    fixture_texts = {fixture_path: synthetic_text}
    fixture_paths = [fixture_path]

    # Use the same evidence machinery, with the synthetic document temporarily treated as physical authority.
    original_prefixes = PHYSICAL_SOURCE_PREFIXES
    statuses = {}
    evidence = {}
    for req, spec in REQUIREMENT_SPECS.items():
        positive_matches = []
        for terms in spec['positive_groups']:
            for excerpt in paragraph_matches(synthetic_text, terms):
                positive_matches.append({'path': fixture_path, 'terms': list(terms), 'excerpt': excerpt})
        status = 'DEFINED' if positive_matches else 'ABSENT_OR_ONLY_CONDITIONAL'
        statuses[req] = status
        evidence[req] = {
            'status': status,
            'positive_matches': positive_matches,
            'negative_or_absence_matches': [],
            'searched_physical_authority_paths': fixture_paths,
            'searched_complete_corpus_paths': fixture_paths,
        }
    candidate = make_candidate(statuses)
    validation = validate_candidate(statuses, candidate)
    verdict = 'PASS_OBJECT_DEFINED_SCOPED' if validation['accepted'] else 'INVALID_IMPLEMENTATION'
    return {
        'requirement_statuses': statuses,
        'evidence': evidence,
        'candidate_validation': validation,
        'verdict': verdict,
        'passed': verdict == 'PASS_OBJECT_DEFINED_SCOPED',
    }


def malformed_negative_controls():
    statuses = {k: 'DEFINED' for k in REQUIREMENT_SPECS}
    base = make_candidate(statuses)
    cases = {}

    def run_case(name, mutate):
        c = json.loads(json.dumps(base))
        mutate(c)
        v = validate_candidate(statuses, c)
        cases[name] = {
            'rejected': not v['accepted'],
            'rejection_reasons': v['rejection_reasons'],
            'candidate': c,
        }

    run_case('representative_component_rejected', lambda c: c.update({'boundary_components': 1, 'exact_boundary_reduction_theorem': False}))
    run_case('auxiliary_Q_hodge_scalar_surrogate_rejected', lambda c: c.update({'family_kind': 'auxiliary_Q_hodge_scalar_surrogate'}))
    run_case('termwise_contact_product_rejected', lambda c: c.update({'source_order': ['theta/delta/delta-prime termwise product', 'pullback']}))
    run_case('posthoc_finite_part_regulator_rejected', lambda c: c.update({'posthoc_choice': True}))
    run_case('generic_extension_theorem_rejected', lambda c: c.update({'generic_extension_only': True}))
    run_case('one_wedge_spectral_epsilon_as_joint_parameter_rejected', lambda c: c.update({'family_kind': 'one_wedge_spectral_epsilon_relabelled_joint'}))
    run_case('iter083n_formal_rho_power_as_source_family_rejected', lambda c: c.update({'family_kind': 'iter083n_formal_rho_power_family'}))
    return cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    corpus_paths = enumerate_corpus()
    missing_paths = [p for p in FIXED_CORPUS + MINIMUM_DIRECT_LOCKS if not (ROOT / p).is_file()]
    texts = {p: read(p) for p in corpus_paths if (ROOT / p).is_file()}
    manifest = [
        {
            'path': p,
            'sha256': sha256_text(texts[p]),
            'role': source_role(p),
        }
        for p in corpus_paths if p in texts
    ]
    manifest_complete = not missing_paths and all(p in texts for p in FIXED_CORPUS + MINIMUM_DIRECT_LOCKS)

    provenance_anchors = {
        'parent_prereg_unchanged_contract': 'BLOCKED_OBJECT_DEFINITION' in texts.get(PARENT_PREREG, '') and 'INVALID_IMPLEMENTATION' in texts.get(PARENT_PREREG, ''),
        'critic_requires_control_only_repair': 'Only a control-only Iter083P repair/retry under the unchanged scientific preregistration is authorized.' in texts.get('status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md', ''),
        'current_quarantines_historical_iter083p': 'Iter083P Researcher result may not be used downstream.' in texts.get('status/CURRENT.md', ''),
        'erratum_present': 'ITER077' in texts.get('status/ITER077_CONTACT_FORMULA_ERRATUM.md', ''),
    }

    statuses, evidence = derive_requirements(texts, corpus_paths)
    main_candidate = make_candidate(statuses)
    main_candidate_validation = validate_candidate(statuses, main_candidate)

    positive_fixture = synthetic_positive_fixture()
    negative_controls = malformed_negative_controls()
    negative_controls_ok = all(v['rejected'] for v in negative_controls.values())

    available_inputs = {
        'one_wedge_toller_source_formula': 'Eq. (3) defines one Toller matrix' in texts.get('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', ''),
        'ten_factor_off_collision_k5_vertex_formula': 'There are ten Toller factors.' in texts.get('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', ''),
        'four_gauge_fixed_group_integrations_present_in_repository_authority': 'four gauge-fixed' in texts.get('status/CURRENT.md', '').lower() or 'prod_(a=2)^5 dg_a' in texts.get('sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md', ''),
        'formal_iter083n_laurent_control_only': 'formal Laurent transformation law' in texts.get('sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md', ''),
        'conditional_iter083h_not_full_k5_theorem': 'No full K5 meromorphic continuation theorem' in texts.get('sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md', ''),
    }

    execution_valid = (
        manifest_complete
        and all(provenance_anchors.values())
        and positive_fixture['passed']
        and negative_controls_ok
    )

    if not execution_valid:
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083P_SM_SOURCE_RESIDUE_OBJECT_DEFINITION_AUDIT_INVALID_IMPLEMENTATION'
    elif all(status == 'DEFINED' for status in statuses.values()) and main_candidate_validation['accepted']:
        verdict = 'PASS_OBJECT_DEFINED_SCOPED'
        classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_OBJECT_DEFINED_SCOPED'
    elif any(status == 'CONTRADICTORY' for status in statuses.values()):
        verdict = 'FAIL_EXACT_SCOPED'
        classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_AUTHORITY_CONTRADICTION_SCOPED'
    else:
        verdict = 'BLOCKED_OBJECT_DEFINITION'
        classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED'

    out = {
        'iteration': 'Iter083P-SM-control-repair-1',
        'gate': 'ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION',
        'repair_scope': 'control-only; parent scientific contract unchanged',
        'execution_valid': execution_valid,
        'manifest_complete': manifest_complete,
        'missing_required_manifest_paths': missing_paths,
        'authority_manifest': manifest,
        'authority_manifest_count': len(manifest),
        'provenance_anchors': provenance_anchors,
        'requirement_statuses': statuses,
        'requirements': {k: statuses[k] == 'DEFINED' for k in statuses},
        'requirement_evidence': evidence,
        'missing_requirements': [k for k, v in statuses.items() if v != 'DEFINED'],
        'main_candidate': main_candidate,
        'main_candidate_validation': main_candidate_validation,
        'positive_fixture': positive_fixture,
        'negative_controls': negative_controls,
        'negative_controls_ok': negative_controls_ok,
        'available_inputs': available_inputs,
        'verdict': verdict,
        'classification': classification,
        'interpretation_ceiling': 'Object-definition audit only. No physical residue value/order/sign/cancellation, finite-part selector, regulator dependence/independence, unique K5 extension, F9/G3 promotion or downstream QG claim.',
    }

    p = ROOT / args.output
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
