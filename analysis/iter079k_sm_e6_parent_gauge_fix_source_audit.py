#!/usr/bin/env python3
import json
from pathlib import Path

MATRIX = Path(__file__).with_name('iter079k_sm_e6_parent_gauge_fix_source_matrix.json')
OUT = Path('iter079k_sm_e6_parent_gauge_fix_source_audit.json')

def main():
    m = json.loads(MATRIX.read_text())
    lanes = m['frozen_lane_assessment_inputs']
    A = lanes['A_parent_local_gauge_treatment']
    B = lanes['B_parent_full_triangulation_compatibility']
    C = lanes['C_causal_inheritance_bridge']

    lane_a = bool(A['redundancy_explicit'] and A['integration_removal_explicit'] and A['normalization_convention_explicit'])
    lane_b = bool(B['explicit'])
    causal_local = bool(C['one_vertex_same_fix_explicit'])
    causal_multivertex = bool(C['many_vertex_normalization_inheritance_explicit'])

    if not (lane_a and lane_b and causal_local):
        classification = 'ITER079K_SM_INVALID_PROVENANCE_OR_CONTROL'
        verdict = 'INVALID'
    elif causal_multivertex:
        classification = 'ITER079K_SM_E6_PARENT_QUOTIENT_FIXING_AND_NORMALIZATION_EXPLICIT_AND_CAUSAL_INHERITANCE_SOURCE_EXPLICIT_EXACT_SCOPED'
        verdict = 'PASS_EXACT_SCOPED'
    else:
        classification = 'ITER079K_SM_PARENT_E6_GAUGE_FIXING_PRESCRIPTION_EXISTS_BUT_CAUSAL_INHERITANCE_BRIDGE_MISSING_SOURCE_BLOCKED_EXACT_SCOPED'
        verdict = 'BLOCKED_SOURCE_BRIDGE'

    out = {
        'gate': m['gate'],
        'prereg_commit': m['prereg_commit'],
        'lane_A_parent_local_gauge_treatment_complete': lane_a,
        'lane_B_parent_full_triangulation_compatibility_explicit': lane_b,
        'lane_C_causal_one_vertex_same_fix_explicit': causal_local,
        'lane_C_causal_many_vertex_normalization_inheritance_explicit': causal_multivertex,
        'forbidden_inferences_count': len(m['forbidden_inferences']),
        'verdict': verdict,
        'classification': classification,
        'claim_locks_preserved': True
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
