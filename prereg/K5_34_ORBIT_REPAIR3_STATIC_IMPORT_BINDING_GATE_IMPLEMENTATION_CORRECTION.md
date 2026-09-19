# K5 repair3 static/import binding gate — implementation correction preregistration

Status: PROSPECTIVE, frozen before corrective implementation.

The first production run of the already-preregistered static/import binding gate (run 35427903794) terminated `INVALID_REPAIR3_STATIC_IMPORT_BINDING` before any N/B production. Inspection of its raw log localizes two gate-implementation defects, not scientific failures and not repair3-core failures:

1. `two_invariant_dual_channels` was implemented as `len(W1)==2 and len(W2)==2`. The frozen contract requires the two invariant-dual channels W1 and W2 to remain present; it does not require each channel object itself to have Python length two. The corrected check is presence/non-nullness of both W1 and W2, while the existing production constants check continues to bind frozen U=5 and the other constants.
2. `no_q18_partial` was implemented as the substring test `'q18' not in source.lower()`. This falsely rejects the repair3 core's explicit audit metadata `q18_values_used=False`. The frozen contract forbids importing/referencing quarantined q18 partial-output paths, not the presence of negative audit metadata. The corrected static check ignores the literal metadata identifier `q18_values_used` and rejects any remaining q18 token/reference.

Frozen scientific criteria are unchanged. No N/B outcomes or q18 values may be computed or inspected by this correction. All other checks and deliberate negative controls from `prereg/K5_34_ORBIT_REPAIR3_STATIC_IMPORT_BINDING_GATE.md` remain unchanged. The corrected gate may classify only `PASS_REPAIR3_STATIC_IMPORT_BINDING`, `FAIL_REPAIR3_STATIC_IMPORT_BINDING`, or `INVALID_REPAIR3_STATIC_IMPORT_BINDING` under the original contract.

Only after a terminal PASS may repair3 heavy production be authorized.
