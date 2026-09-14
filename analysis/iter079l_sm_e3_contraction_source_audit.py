#!/usr/bin/env python3
import json
from pathlib import Path
m=json.loads(Path('analysis/iter079l_sm_e3_contraction_source_matrix.json').read_text())
f=m['frozen_inputs']; t=m['toy_control']
sources={s['id']:s for s in m['primary_sources']}
required=m['lane_C_predicate']['required_causal_sources']
C_sources={sid: bool(sources[sid].get('explicit_many_vertex_parent_E3_inheritance', False)) for sid in required}
C=any(C_sources.values())
provenance=all(sid in sources and sources[sid].get('evidence') for sid in required) and 'KKL2010' in sources
D=bool(f['D_fixed_pairing_conditional_algebra'] and f['D_rescaled_pairing_changes_composition'] and t['pairing_identity']==11 and t['pairing_scaled_by_2']==22)
if not provenance or not (f['A_parent_E3_explicit'] and f['B_parent_gluing_identity_explicit'] and D):
    c='ITER079L_SM_INVALID_PROVENANCE_OR_CONTROL'; v='INVALID'
elif C:
    c='ITER079L_SM_E3_PARENT_CONTRACTION_EXPLICIT_AND_CAUSAL_INHERITANCE_SOURCE_EXPLICIT_EXACT_SCOPED'; v='PASS_EXACT_SCOPED'
else:
    c='ITER079L_SM_E3_PARENT_CONTRACTION_CONDITIONALLY_INHERITS_ALGEBRAICALLY_BUT_CAUSAL_MULTIVERTEX_SOURCE_BRIDGE_MISSING_BLOCKED_EXACT_SCOPED'; v='BLOCKED_SOURCE_BRIDGE'
out={
 'gate':m['gate'],
 'original_prereg_commit':m['original_prereg_commit'],
 'repair_prereg_commit':m['repair_prereg_commit'],
 'lane_A':f['A_parent_E3_explicit'],
 'lane_B':f['B_parent_gluing_identity_explicit'],
 'lane_C':C,
 'lane_C_source_specific':C_sources,
 'lane_C_source_evidence':{sid:sources[sid]['evidence'] for sid in required},
 'lane_D':D,
 'provenance_valid':provenance,
 'classification':c,'verdict':v,
 'claim_locks_preserved':m['claim_locks_preserved']
}
Path('iter079l_sm_e3_contraction_source_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
