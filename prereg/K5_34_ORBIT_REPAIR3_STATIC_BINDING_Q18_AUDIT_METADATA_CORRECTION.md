# K5 repair3 static binding — q18 audit-metadata correction preregistration

Prospectively frozen after terminal run 35430614849 and before implementation.

## Observed gate-only defect
All substantive repair3 binding checks passed in run 35430614849 except `q18_not_on_production_path`. The core contains the literal key `q18_values_used` only as audit/provenance metadata explicitly set to `False`; the production shard contains no q18 reference. A raw substring ban therefore confounds an explicit non-use attestation with use of quarantined q18 values.

## Frozen correction
Replace only the raw substring test for q18 with a structural production-path audit:
1. production shard source must contain no `q18` token;
2. repair3 core may contain `q18_values_used` only in audit/provenance checks or output metadata whose value is explicitly `False` / tests an authoritative artifact field `is False`;
3. no q18 value, table, coefficient, order, import, loader, computation, branch condition, or argument may feed `route_a`, `route_b_interpolation`, matching coefficients, N/B construction, or production output;
4. retain the runtime/static assertion `q18_values_used == False` where available.

No scientific criterion, matching coefficient, N/B order, orbit/channel coverage, U=5 authority, W1/W2 definition, classifier, or repair3 production algorithm may change. The correction must not inspect N/B outcomes or q18 values. Heavy resolver remains forbidden until the corrected static/import gate returns `PASS_REPAIR3_STATIC_IMPORT_BINDING`.

Frozen interpretation: failure after this correction is BLOCKED/INVALID implementation or provenance unless an independently preregistered scientific gate says otherwise; it is not a scientific FAIL.