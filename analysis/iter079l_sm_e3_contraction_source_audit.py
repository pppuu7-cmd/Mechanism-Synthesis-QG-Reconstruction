#!/usr/bin/env python3
import json
from pathlib import Path
m=json.loads(Path('analysis/iter079l_sm_e3_contraction_source_matrix.json').read_text())
f=m['frozen_inputs']; t=m['toy_control']
D=bool(f['D_fixed_pairing_conditional_algebra'] and f['D_rescaled_pairing_changes_composition'] and t['pairing_identity']==11 and t['pairing_scaled_by_2']==22)
if not (f['A_parent_E3_explicit'] and f['B_parent_gluing_identity_explicit'] and D):
    c='ITER079L_SM_INVALID_PROVENANCE_OR_CONTROL'; v='INVALID'
elif f['C_causal_multivertex_E3_inheritance_explicit']:
    c='ITER079L_SM_E3_PARENT_CONTRACTION_EXPLICIT_AND_CAUSAL_INHERITANCE_SOURCE_EXPLICIT_EXACT_SCOPED'; v='PASS_EXACT_SCOPED'
else:
    c='ITER079L_SM_E3_PARENT_CONTRACTION_CONDITIONALLY_INHERITS_ALGEBRAICALLY_BUT_CAUSAL_MULTIVERTEX_SOURCE_BRIDGE_MISSING_BLOCKED_EXACT_SCOPED'; v='BLOCKED_SOURCE_BRIDGE'
out={'gate':m['gate'],'prereg_commit':m['prereg_commit'],'lane_A':f['A_parent_E3_explicit'],'lane_B':f['B_parent_gluing_identity_explicit'],'lane_C':f['C_causal_multivertex_E3_inheritance_explicit'],'lane_D':D,'classification':c,'verdict':v,'claim_locks_preserved':m['claim_locks_preserved']}
Path('iter079l_sm_e3_contraction_source_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
