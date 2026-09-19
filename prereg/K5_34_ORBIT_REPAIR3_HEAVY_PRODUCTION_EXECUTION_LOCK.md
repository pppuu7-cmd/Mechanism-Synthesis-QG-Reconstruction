# K5 34-orbit repair3 heavy production — execution lock

Date: 2026-09-19
Status: PROSPECTIVE EXECUTION-ONLY LOCK, frozen before the single repair3 heavy production run.

## Activation authority

This lock activates only because the independent repair3 preflight is terminal `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` and the subsequent static/import binding gate is terminal `PASS_REPAIR3_STATIC_IMPORT_BINDING` (run 35433269649, artifact 10581126528). The immutable parent scientific prereg remains `d6b0e805101c8590eafac71398cc2b1466691752` and the Researcher production contract remains `prereg/K5_34_ORBIT_REPAIR3_RESEARCHER_OUTCOME_BLIND_POSTPREFLIGHT_PRODUCTION_CONTRACT.md`.

## Frozen production

Exactly one authoritative heavy production is permitted. It MUST use:

- `scripts/k5_34_orbit_exact_leading_coefficient_shard_repair3.py`;
- the already bound repair3 target-label matching-key core;
- eight deterministic exhaustive non-overlapping shards over the unchanged 32 proper orbit representatives / 64 channel-orbit components;
- both W1/W2 invariant-dual channels;
- complete N[0..27] and B[0..31] coefficient vectors;
- recomputed projective-normal U degree-5 authority;
- exact rational arithmetic;
- all parent route, second-path, S5 full-coefficient covariance, mask511 reproduction and independent Boundary-S5 authority controls.

The aggregate MUST use the unchanged parent classifier meanings. No N/B result may be inspected before all eight shards are terminal and the aggregate is complete. Partial shard output has no scientific authority.

## Sole scientific-path repair

The only allowed scientific-path difference from the invalid parent production is the already frozen matching-key re-framing:

`S5_MATCH_COEFF_CYCLE_TARGET[P(mt)] = S5_MATCH_COEFF_CYCLE_PULLBACK[mt]`

for all 945 retained matchings. Coefficient values/multiset and every other physics/scientific input remain unchanged. No fitting, tuning, tolerance, adaptive support, representative change, counterterm, q18 partial, or post-output convention change is allowed.

## Frozen terminal classifier

Only:

- `INVALID_IMPLEMENTATION` if any mandatory implementation/provenance/coverage/covariance/exactness control fails;
- `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_PARTIAL_BLOCKED_SCOPED` if implementation is valid but any required component is uncertified;
- `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_EXACT_SCOPED` only if all 64 components are exactly resolved with every frozen control passing.

A terminal exact result may authorize only the already-separated local DAG / physical N-action-flux valuation audit. It does not authorize global Stokes/IBP, K5 periods, finite-part selector, regulator independence, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claims.

## Failure semantics

Infrastructure/numerical failure is not scientific FAIL. If a shard fails operationally, preserve completed shards and diagnose/retry only the failed operational work. A valid frozen scientific obstruction is a result and must not be repaired away.
