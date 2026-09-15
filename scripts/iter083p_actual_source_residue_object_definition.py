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

PARENT = 'prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md'
REPAIR1 = 'prereg/ITER083P_CONTROL_ONLY_REPAIR_1.md'
REPAIR2 = 'prereg/ITER083P_CONTROL_ONLY_REPAIR_2.md'
REPAIR3 = 'prereg/ITER083P_CONTROL_ONLY_REPAIR_3.md'
CRITIC1 = 'results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md'
CRITIC2 = 'results/ITER083P_CONTROL_REPAIR_2_ADVERSARIAL_REVIEW.md'
CRITIC2_PREREG = 'prereg/ITER083P_CONTROL_REPAIR_2_INDEPENDENT_CRITIC_REVIEW.md'

ITER077I = 'sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md'
ITER080K = 'sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md'
ITER083E = 'sources/ITER083E_PUBLIC_SOURCE_LOCK.md'
ITER083F = 'sources/ITER083F_PUBLIC_SOURCE_LOCK.md'
ITER083G = 'sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md'
ITER083H = 'sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md'
ITER083J = 'sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md'
ITER083K = 'sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md'
ITER083L = 'sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md'
ITER083M = 'sources/ITER083M_SM_SOURCE_NORMAL_RADIAL_GEOMETRY_DERIVATION.md'
ITER083N = 'sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md'
ITER083N_DER = 'sources/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_DERIVATION.md'

REQUIRED_PATHS = [
    'status/CURRENT.md',
    'status/MSQGR_RESEARCHER_HANDOFF.md',
    'status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md',
    'status/ITER077_CONTACT_FORMULA_ERRATUM.md',
    'status/ITER083P_CONTROL_REPAIR_2_CRITIC_PROVENANCE_LEDGER.md',
    PARENT, REPAIR1, REPAIR2, REPAIR3, CRITIC2_PREREG, CRITIC1, CRITIC2,
    ITER077I, ITER080K, ITER083E, ITER083F, ITER083G, ITER083H,
    ITER083J, ITER083K, ITER083L, ITER083M, ITER083N, ITER083N_DER,
]

PHYSICAL_AUTHORITY_PATHS = {
    ITER077I, ITER080K, ITER083E, ITER083F, ITER083L,
}

NEGATION_MARKERS = (
    ' no ', 'not ', ' does not ', 'cannot ', 'without ', 'missing ',
    'absent ', 'conditional ', 'not yet ', 'do not ',
)

REQUIREMENT_SPECS = {
    'R1_full_source_meromorphic_deformation_parameter_and_object': {
        'positive_groups': [('full k5', 'meromorphic', 'family'), ('full source', 'analytic family', 'k5')],
        'negative_sets': [[
            (ITER083L, '## Objects absent from the published K5 definition', 'edgewise collision-analytic parameters'),
            (ITER083H, '## 8. Scope locks', 'No full K5 meromorphic continuation theorem'),
        ]],
    },
    'R2_exact_source_to_joint_deformation_map': {
        'positive_groups': [('exact map', 'joint deformation', 'k5'), ('source', 'map', 'joint', 'deformation')],
        'negative_sets': [[
            (ITER083L, '## Objects absent from the published K5 definition', 'a joint K3/K4/K5 finite-part/subtraction map'),
            (ITER083G, '## MSQGR source scope', 'a 10-variable complex-power analytic regularization of the K5 product'),
        ]],
    },
    'R3_full_boundary_contracted_residue_map_all_32_or_exact_reduction': {
        'positive_groups': [('residue map', 'full boundary contraction', '32'), ('residue', 'boundary', '32', 'exact reduction')],
        'negative_sets': [[
            (ITER077I, '## Complete all-j=1/2 boundary basis', '`2^5=32`'),
            ('status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md', '## BOUNDARY_COMPLETENESS_CHECK', 'No physical all-32 residue map, vanishing theorem or exact reduction is established by this review.'),
            (ITER083L, '## Direct formula facts', 'There are ten Toller factors.'),
        ]],
    },
    'R4_deformed_full_object_measure_and_normalization': {
        'positive_groups': [('deformed full', 'measure', 'normalization'), ('meromorphic', 'haar', 'normalization', 'k5')],
        'negative_sets': [[
            (ITER083G, '## MSQGR source scope', 'a minimal-subtraction/finite-part normalization selecting the 377 supported coefficients'),
            (ITER083L, '## Objects absent from the published K5 definition', 'a K5 gluing/composition normalization selecting supported extension coefficients'),
        ]],
    },
    'R5_joint_deformation_branch_and_published_spectral_compatibility_theorem': {
        'positive_groups': [('joint k5', 'branch', 'published i epsilon', 'compatibility theorem'), ('joint', 'branch', 'spectral', 'compatibility')],
        'negative_sets': [[
            (ITER083L, '## Direct formula facts', 'the published epsilon is a one-wedge spectral prescription'),
            (ITER080K, '## Systematic audit for a joint-K5 collision-extension selector', 'No explicit theorem/equation/prescription was identified'),
        ]],
    },
    'R6_full_k5_laurent_expansion_theorem_near_collision': {
        'positive_groups': [('full k5', 'laurent', 'collision'), ('full k5', 'meromorphic continuation theorem')],
        'negative_sets': [[
            (ITER083H, '## 8. Scope locks', 'No full K5 meromorphic continuation theorem'),
            (ITER083G, '## Forbidden implications', 'actual K5 regularized meromorphic germ satisfies all hypotheses'),
        ]],
    },
    'R7_unique_source_identification_of_A_minus_1': {
        'positive_groups': [('a_-1', 'source', 'unique'), ('residue coefficient', 'source', 'full k5', 'unique')],
        'negative_sets': [[
            (ITER083N, '## Forbidden implications', 'Do not claim the physical Toller residue is nonzero in every supported-jet channel.'),
            (ITER083N, '## Forbidden implications', 'Do not promote the formal Laurent transformation law to a complete global K5 renormalization theorem.'),
        ]],
    },
}


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def sha256_text(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def relevant_tagged_name(name):
    return bool(re.match(r'^(ITER077I_|ITER080K_|ITER083[EFGHIJKLMNP]_)', name))


def enumerate_corpus():
    paths = set(REQUIRED_PATHS)
    for dirname in ('sources', 'results', 'status', 'prereg'):
        base = ROOT / dirname
        if not base.is_dir():
            continue
        for p in base.iterdir():
            if p.is_file() and relevant_tagged_name(p.name):
                paths.add(str(p.relative_to(ROOT)))
    return sorted(paths)


def default_role(path):
    if path in PHYSICAL_AUTHORITY_PATHS:
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


def section(text, heading):
    pos = text.find(heading)
    if pos < 0:
        return ''
    tail = text[pos + len(heading):]
    m = re.search(r'\n##\s+', tail)
    return tail[:m.start()] if m else tail


def paragraph_matches(text, terms):
    out = []
    for para in re.split(r'\n\s*\n', text):
        low = ' ' + para.lower().replace('\n', ' ') + ' '
        if all(term.lower() in low for term in terms) and not any(marker in low for marker in NEGATION_MARKERS):
            out.append(' '.join(para.split())[:700])
    return out


def negative_set_evidence(texts, evidence_set):
    hits = []
    for path, heading, needle in evidence_set:
        text = texts.get(path)
        if text is None:
            return None
        scoped = section(text, heading) if heading else text
        if needle not in scoped:
            return None
        hits.append({'path': path, 'section': heading, 'anchor': needle})
    return hits


def derive_requirements(texts, corpus_paths, role_map):
    evidence = {}
    statuses = {}
    physical_paths = [p for p in corpus_paths if role_map.get(p) == 'physical_source_authority' and p in texts]
    for req, spec in REQUIREMENT_SPECS.items():
        positive = []
        for path in physical_paths:
            for terms in spec['positive_groups']:
                for excerpt in paragraph_matches(texts[path], terms):
                    positive.append({'path': path, 'terms': list(terms), 'excerpt': excerpt})
        negative_sets = []
        for eset in spec['negative_sets']:
            hit = negative_set_evidence(texts, eset)
            if hit is not None:
                negative_sets.append(hit)
        if positive and negative_sets:
            status = 'CONTRADICTORY'
        elif positive:
            status = 'DEFINED'
        elif negative_sets:
            status = 'ABSENT_OR_ONLY_CONDITIONAL'
        else:
            status = 'UNRESOLVED_EVIDENCE'
        statuses[req] = status
        evidence[req] = {
            'status': status,
            'positive_matches': positive,
            'negative_or_conditional_evidence_sets': negative_sets,
            'searched_physical_authority_paths': physical_paths,
            'searched_complete_corpus_paths': list(corpus_paths),
        }
    return statuses, evidence


def validate_candidate(statuses, candidate):
    reasons = []
    if any(statuses.get(k) != 'DEFINED' for k in REQUIREMENT_SPECS): reasons.append('not_all_R1_R7_defined')
    if candidate.get('source_order') != EXPECTED_SOURCE_ORDER: reasons.append('wrong_source_order')
    if candidate.get('wedge_count') != 10: reasons.append('not_all_ten_wedges')
    if candidate.get('true_k5_incidence') is not True: reasons.append('not_true_k5_incidence')
    if candidate.get('boundary_components') != 32 and candidate.get('exact_boundary_reduction_theorem') is not True: reasons.append('boundary_incomplete_without_exact_reduction')
    if candidate.get('family_kind') != 'actual_source_ordered_k5_meromorphic_family': reasons.append('wrong_or_surrogate_family_kind')
    if candidate.get('source_authorized_measure_normalization') is not True: reasons.append('measure_normalization_not_source_authorized')
    if candidate.get('source_authorized_branch_spectral_compatibility') is not True: reasons.append('branch_spectral_compatibility_not_source_authorized')
    if candidate.get('posthoc_choice') is True: reasons.append('posthoc_choice_forbidden')
    if candidate.get('generic_extension_only') is True: reasons.append('generic_extension_not_source_bridge')
    return {'accepted': not reasons, 'rejection_reasons': reasons}


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


def evaluate(texts, paths, roles, require_complete_manifest):
    statuses, evidence = derive_requirements(texts, paths, roles)
    candidate = make_candidate(statuses)
    validation = validate_candidate(statuses, candidate)
    unresolved = [k for k, v in statuses.items() if v == 'UNRESOLVED_EVIDENCE']
    contradictory = [k for k, v in statuses.items() if v == 'CONTRADICTORY']
    if require_complete_manifest and unresolved:
        verdict = 'INVALID_IMPLEMENTATION'
    elif all(v == 'DEFINED' for v in statuses.values()) and validation['accepted']:
        verdict = 'PASS_OBJECT_DEFINED_SCOPED'
    elif contradictory:
        verdict = 'FAIL_EXACT_SCOPED'
    elif any(v == 'ABSENT_OR_ONLY_CONDITIONAL' for v in statuses.values()):
        verdict = 'BLOCKED_OBJECT_DEFINITION'
    else:
        verdict = 'INVALID_IMPLEMENTATION'
    return statuses, evidence, candidate, validation, verdict


def positive_fixture():
    path = 'sources/SYNTHETIC_ITER083P_POSITIVE_AUTHORITY.md'
    text = '''
Full K5 meromorphic family: the full source object is a full K5 meromorphic family.

Exact map joint deformation K5: the source supplies the exact map to the joint deformation.

Residue map full boundary contraction 32: the residue map uses the full boundary contraction on all 32 components.

Deformed full measure normalization: the deformed full object uses the source Haar measure and normalization.

Joint K5 branch published i epsilon compatibility theorem: the joint K5 branch is compatible with the published i epsilon prescription by theorem.

Full K5 Laurent collision: the full K5 object has a Laurent expansion at the collision.

A_-1 source unique: A_-1 is uniquely identified by the source.
'''
    texts = {path: text}
    paths = [path]
    roles = {path: 'physical_source_authority'}
    statuses, evidence, candidate, validation, verdict = evaluate(texts, paths, roles, False)
    return {'statuses': statuses, 'evidence': evidence, 'candidate_validation': validation, 'verdict': verdict, 'passed': verdict == 'PASS_OBJECT_DEFINED_SCOPED'}


def missing_evidence_control():
    path = 'sources/SYNTHETIC_ITER083P_MISSING_EVIDENCE.md'
    text = '''
Full K5 meromorphic family: the full source object is a full K5 meromorphic family.
Exact map joint deformation K5: the source supplies the exact map to the joint deformation.
Residue map full boundary contraction 32: the residue map uses the full boundary contraction on all 32 components.
Deformed full measure normalization: the deformed full object uses the source Haar measure and normalization.
Joint K5 branch published i epsilon compatibility theorem: compatibility is a theorem.
Full K5 Laurent collision: the full K5 object has a Laurent expansion at the collision.
'''
    texts = {path: text}
    paths = [path]
    roles = {path: 'physical_source_authority'}
    statuses, evidence = derive_requirements(texts, paths, roles)
    passed = statuses['R7_unique_source_identification_of_A_minus_1'] == 'UNRESOLVED_EVIDENCE'
    return {'statuses': statuses, 'evidence': evidence, 'passed': passed}


def malformed_negative_controls():
    statuses = {k: 'DEFINED' for k in REQUIREMENT_SPECS}
    base = make_candidate(statuses)
    cases = {}
    def run(name, changes):
        c = json.loads(json.dumps(base)); c.update(changes)
        v = validate_candidate(statuses, c)
        cases[name] = {'rejected': not v['accepted'], 'rejection_reasons': v['rejection_reasons']}
    run('representative_component_rejected', {'boundary_components': 1, 'exact_boundary_reduction_theorem': False})
    run('auxiliary_Q_hodge_scalar_surrogate_rejected', {'family_kind': 'auxiliary_Q_hodge_scalar_surrogate'})
    run('termwise_contact_product_rejected', {'source_order': ['theta/delta/delta-prime termwise product', 'pullback']})
    run('posthoc_finite_part_regulator_rejected', {'posthoc_choice': True})
    run('generic_extension_theorem_rejected', {'generic_extension_only': True})
    run('one_wedge_spectral_epsilon_as_joint_parameter_rejected', {'family_kind': 'one_wedge_spectral_epsilon_relabelled_joint'})
    run('iter083n_formal_rho_power_as_source_family_rejected', {'family_kind': 'iter083n_formal_rho_power_family'})
    return cases


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', required=True); args = ap.parse_args()
    paths = enumerate_corpus()
    missing = [p for p in REQUIRED_PATHS if not (ROOT / p).is_file()]
    texts = {p: read(p) for p in paths if (ROOT / p).is_file()}
    roles = {p: default_role(p) for p in paths}
    manifest = [{'path': p, 'sha256': sha256_text(texts[p]), 'role': roles[p]} for p in paths if p in texts]
    manifest_complete = not missing and all(p in texts for p in REQUIRED_PATHS)
    manifest_paths = {m['path'] for m in manifest}

    provenance = {
        'parent_contract_present': 'BLOCKED_OBJECT_DEFINITION' in texts.get(PARENT, '') and 'INVALID_IMPLEMENTATION' in texts.get(PARENT, ''),
        'repair3_prospective_lock_present': 'PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / PRODUCTION OUTPUT' in texts.get(REPAIR3, ''),
        'critic_authorizes_only_control_repair': 'Only a further **control-only Iter083P repair/retry under the unchanged scientific preregistration** is authorized.' in texts.get('status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md', ''),
        'iter077i_in_manifest': ITER077I in manifest_paths,
        'iter077_erratum_in_manifest': 'status/ITER077_CONTACT_FORMULA_ERRATUM.md' in manifest_paths,
        'critic2_contract_in_manifest': CRITIC2 in manifest_paths and CRITIC2_PREREG in manifest_paths,
    }

    statuses, evidence, candidate, candidate_validation, scientific_verdict = evaluate(texts, paths, roles, True)
    positive = positive_fixture()
    missing_control = missing_evidence_control()
    negatives = malformed_negative_controls()
    negatives_ok = all(v['rejected'] for v in negatives.values())
    unresolved = [k for k, v in statuses.items() if v == 'UNRESOLVED_EVIDENCE']

    execution_valid = manifest_complete and all(provenance.values()) and positive['passed'] and missing_control['passed'] and negatives_ok and not unresolved
    if not execution_valid:
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083P_SM_SOURCE_RESIDUE_OBJECT_DEFINITION_AUDIT_INVALID_IMPLEMENTATION'
    else:
        verdict = scientific_verdict
        if verdict == 'PASS_OBJECT_DEFINED_SCOPED':
            classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_OBJECT_DEFINED_SCOPED'
        elif verdict == 'FAIL_EXACT_SCOPED':
            classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_AUTHORITY_CONTRADICTION_SCOPED'
        elif verdict == 'BLOCKED_OBJECT_DEFINITION':
            classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED'
        else:
            classification = 'ITER083P_SM_SOURCE_RESIDUE_OBJECT_DEFINITION_AUDIT_INVALID_IMPLEMENTATION'

    out = {
        'iteration': 'Iter083P-SM-control-repair-3',
        'gate': 'ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION',
        'repair_scope': 'control-only; parent scientific contract unchanged',
        'execution_valid': execution_valid,
        'manifest_complete': manifest_complete,
        'missing_required_manifest_paths': missing,
        'authority_manifest': manifest,
        'authority_manifest_count': len(manifest),
        'provenance_anchors': provenance,
        'requirement_statuses': statuses,
        'requirement_evidence': evidence,
        'unresolved_requirements': unresolved,
        'missing_requirements': [k for k, v in statuses.items() if v != 'DEFINED'],
        'main_candidate': candidate,
        'main_candidate_validation': candidate_validation,
        'positive_fixture': positive,
        'missing_evidence_control': missing_control,
        'negative_controls': negatives,
        'negative_controls_ok': negatives_ok,
        'verdict': verdict,
        'classification': classification,
        'interpretation_ceiling': 'Object-definition audit only. No physical residue value/order/sign/cancellation, finite-part selector, regulator dependence/independence, unique K5 extension, F9/G3 promotion or downstream QG claim.',
    }
    p = ROOT / args.output; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
