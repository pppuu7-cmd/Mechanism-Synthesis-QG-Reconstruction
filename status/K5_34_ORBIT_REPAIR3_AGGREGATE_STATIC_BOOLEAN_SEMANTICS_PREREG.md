# K5 repair3 aggregate static boolean-semantics correction — prospective preregistration

## Trigger
Heavy repair3 production run 35444233673 completed all 8 shards and aggregate successfully at the infrastructure level. The frozen parent aggregate returned `INVALID_IMPLEMENTATION` solely because `static_source_authority_all_shards=false`.

Inspection after terminal classification localizes the defect to aggregate validation semantics: the aggregate currently evaluates `all(d['static_checks'].values())`. The shard payload intentionally contains negative-use attestations such as `q18_values_used=false` and `N_B_orders_or_coefficients_used=false`; those values mean the prohibited inputs were *not* used, but the generic `all(values)` interprets them as failed controls.

## Frozen correction before implementation
The correction is implementation/provenance-only. It MUST NOT alter any scientific coefficient, matching map, orbit/channel coverage, N/B/U degree ceiling, W1/W2 path, S5 transport, second path, mask511 control, or scientific classifier thresholds.

For each shard, static authority is valid iff:
1. every positive assertion in `static_checks` is `true`; and
2. the two negative-use attestations `q18_values_used` and `N_B_orders_or_coefficients_used` are exactly `false`.

No other false static check is permitted. Missing keys are invalid. The correction must be applied only to aggregate validation; the already-successful heavy shard computations are not to be recomputed merely to repair this validator bug.

## Frozen outcomes
After correction and re-aggregation of the exact existing terminal shard payloads, retain the unchanged parent classifier and its existing scientific outcomes. If any non-attestation static check is false, or either negative-use attestation is not exactly false, classification remains `INVALID_IMPLEMENTATION`.

No result from run 35444233673 is promoted by this preregistration itself. Claim locks remain unchanged: no global Stokes/IBP theorem, no physical finiteness/divergence theorem, no F9/G3/G8 promotion, no `NEW_PHYSICS_FOUND`, no complete-QG claim.
