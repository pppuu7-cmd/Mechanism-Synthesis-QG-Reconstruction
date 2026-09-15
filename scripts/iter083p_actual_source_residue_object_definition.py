#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

FILES = {
    'source_lock_e': 'sources/ITER083E_PUBLIC_SOURCE_LOCK.md',
    'result_e': 'results/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NONIMPLICATION_RESULT.md',
    'result_f': 'results/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_RESULT.md',
    'result_l': 'results/ITER083L_SM_K5_LOCALITY_SELECTOR_SOURCE_AUTHORITY_RESULT.md',
    'result_n': 'results/ITER083N_PROVENANCE_CORRECT_RETRY_1_RESULT.md',
    'critic_n': 'status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md',
    'current': 'status/CURRENT.md',
}

def read(rel):
    p = ROOT / rel
    return p.read_text(encoding='utf-8')

def has(text, *needles):
    return all(n in text for n in needles)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    texts = {k: read(v) for k, v in FILES.items()}
    hashes = {k: hashlib.sha256(texts[k].encode('utf-8')).hexdigest() for k in FILES}

    anchors = {
        'source_order_locked': has(
            texts['source_lock_e'],
            'one-wedge Feynman/Toller prescription',
            'ten-factor vertex formula',
            'No source statement in this manifest identifies `rho` with a common-collision normal coordinate'
        ),
        'no_joint_source_prescription_in_audited_vertex': has(
            texts['source_lock_e'],
            'No source-locked joint prescription recorded here',
            'single correlated multivariable boundary value/common regulator',
            'nor a composition/gluing condition that selects supported common-collision extension coefficients'
        ),
        'one_wedge_uniqueness_is_not_joint_selector': has(
            texts['result_e'],
            'single complex spectral variable `rho`',
            'different mathematical stages',
            'cannot select one member of that family'
        ),
        'finite_common_spectral_epsilon_not_collision_regulator': has(
            texts['result_f'],
            'finite spectral epsilon does not even regularize the K5 common collision',
            'An extension/renormalized multiplication is still required'
        ),
        'source_audit_has_no_joint_subtraction_or_common_regulator': has(
            texts['result_l'],
            'a joint K3/K4/K5 finite-part/subtraction map',
            'a common K5 collision regulator/limit',
            'No unique physical extension, no full K5 meromorphic continuation'
        ),
        'iter083n_family_is_formal_not_physical_residue': has(
            texts['result_n'],
            'No physical Toller residue, finite-part prescription, subtraction constant, scale choice or new regulator is inserted.',
            'does **not** prove that the actual full source-ordered Toller residue is nonzero'
        ),
        'critic_requires_actual_source_residue_next': has(
            texts['critic_n'],
            'actual source-ordered residue normal-jet annihilator ?',
            'If the actual residue object cannot be defined without exchanging limits or substituting a surrogate, return `BLOCKED_OBJECT_DEFINITION`.'
        ),
        'current_authorizes_actual_residue_gate': has(
            texts['current'],
            '`ACTUAL_SOURCE_ORDERED_RESIDUE_NORMAL_JET_ANNIHILATOR_GATE`',
            'If the actual residue cannot be defined without exchanging source order, termwise multiplying distributions or substituting a scalar/Hodge/Q surrogate, classify `BLOCKED_OBJECT_DEFINITION`.'
        ),
    }

    execution_valid = all(anchors.values())

    # Object-definition requirements from frozen Iter083P preregistration.
    # These are evaluated for the *actual full source-ordered meromorphic residue object*,
    # not for the off-collision vertex or one-wedge spectral functions separately.
    requirements = {
        'R1_full_source_meromorphic_deformation_parameter_and_object': False,
        'R2_exact_source_to_joint_deformation_map': False,
        'R3_full_boundary_contracted_residue_map_all_32_or_exact_reduction': False,
        'R4_deformed_full_object_measure_and_normalization': False,
        'R5_joint_deformation_branch_and_published_spectral_compatibility_theorem': False,
        'R6_full_k5_laurent_expansion_theorem_near_collision': False,
        'R7_unique_source_identification_of_A_minus_1': False,
    }

    # Already-defined ingredients are recorded separately to prevent a false claim that the source has no vertex.
    available_inputs = {
        'one_wedge_toller_analytic_object': True,
        'published_one_wedge_feynman_i_epsilon': True,
        'ten_factor_off_collision_k5_vertex_formula': True,
        'four_gauge_fixed_sl2c_group_integrations': True,
        'formal_iter083n_local_meromorphic_family_as_mathematical_control_only': True,
    }

    negative_controls = {
        'one_wedge_spectral_epsilon_not_relabelled_joint_residue_parameter': anchors['one_wedge_uniqueness_is_not_joint_selector'] and anchors['finite_common_spectral_epsilon_not_collision_regulator'],
        'iter083n_formal_rho_power_not_promoted_to_source_authority': anchors['iter083n_family_is_formal_not_physical_residue'],
        'representative_component_not_used_for_full_residue': True,
        'auxiliary_Q_hodge_scalar_surrogates_not_used': anchors['source_audit_has_no_joint_subtraction_or_common_regulator'],
        'termwise_contact_product_not_substituted_for_source_order': anchors['current_authorizes_actual_residue_gate'],
        'no_posthoc_finite_part_scale_state_or_regulator': anchors['iter083n_family_is_formal_not_physical_residue'],
        'generic_extension_existence_not_promoted_to_physical_selector': anchors['source_audit_has_no_joint_subtraction_or_common_regulator'],
    }

    if not execution_valid or not all(negative_controls.values()):
        verdict = 'INVALID_IMPLEMENTATION'
        classification = 'ITER083P_SM_SOURCE_RESIDUE_OBJECT_DEFINITION_AUDIT_INVALID_IMPLEMENTATION'
    elif all(requirements.values()):
        verdict = 'PASS_OBJECT_DEFINED_SCOPED'
        classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_OBJECT_DEFINED_SCOPED'
    else:
        verdict = 'BLOCKED_OBJECT_DEFINITION'
        classification = 'ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED'

    out = {
        'iteration': 'Iter083P-SM',
        'gate': 'ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION',
        'execution_valid': execution_valid,
        'verdict': verdict,
        'classification': classification,
        'requirements': requirements,
        'missing_requirements': [k for k,v in requirements.items() if not v],
        'available_inputs': available_inputs,
        'anchors': anchors,
        'negative_controls': negative_controls,
        'source_file_sha256': hashes,
        'interpretation_ceiling': 'Missing bridge/object definition only; not a no-go theorem for future source-faithful meromorphic constructions and not a physical residue or finite-part verdict.',
    }

    p = ROOT / args.output
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
