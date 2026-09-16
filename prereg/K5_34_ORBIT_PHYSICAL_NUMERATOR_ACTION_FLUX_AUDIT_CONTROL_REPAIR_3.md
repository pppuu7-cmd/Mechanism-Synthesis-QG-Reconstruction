# K5 34-orbit physical numerator/action-flux audit — control repair 3 preregistration

Status: **PROSPECTIVELY FROZEN AFTER REPAIR-2 IMPLEMENTATION FAILURE AND BEFORE ANY REPAIR-3 PRODUCTION OUTCOME**.

Parent scientific gate and all scientific inputs/classifiers remain unchanged.

Repair-2 production run `35151178918`, job `104979592873`, failed before any proper-orbit numerator/action classification at the assertion `certified(Psi) && rPsi==tree_order(Z)`. This is `INVALID_IMPLEMENTATION`, not scientific FAIL.

Frozen defect: the repair-2 wrapper interpreted each `PSI_POLY` monomial key as an iterable of edge indices. In the authoritative parent object, each key is instead a 10-component exponent vector, as independently evidenced by the existing frozen `tree_order(Z)=min(sum(m[e] for e in Z) for m in PSI_POLY)` implementation.

Repair-3 changes exactly one execution detail:

`prod_{e in mon} alpha[e]` is replaced by `prod_{e=0..9} alpha[e]**mon[e]` for direct Kirchhoff-polynomial evaluation.

No orbit, channel, prime, weight, tangent field, numerator/action formula, local exponent, S5 control, PASS/BLOCKED criterion, or interpretation ceiling changes. The direct-tree/cofactor denominator strategy from repair-2 remains frozen. If any later numerator/action/projective-normal leading cancellation is unresolved, it remains `BLOCKED_CANCELLATION_RESOLUTION` rather than being retuned.

Terminal classifications remain `INVALID_IMPLEMENTATION`, `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED`, or `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_EXACT_SCOPED` under the already frozen rules.