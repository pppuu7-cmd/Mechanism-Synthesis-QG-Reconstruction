# K5 full-source Boundary-S5 independent Critic — classifier/execution repair

Status: **PROSPECTIVELY FROZEN BEFORE REPAIRED EXECUTION OR OUTPUT**.
Date: 2026-09-17

## Parent scientific contract

The scientific contract remains exactly `prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md`, commit `cf8576acb7237b751c26d5b5942aa60874bcd00e`.

Independent reconstruction implementation authority is `scripts/critic_k5_full_source_boundary_s5_symbolic_independent_reconstruction.py`, implementation commit `64a4f4935d0238d67e2d60e0b202f81f1195330a`, blob `948f32653872e0920b4450d60d56d48a2a0cc24d`.

Outcome-blind pre-execution audit `status/K5_BOUNDARY_S5_CRITIC_PREEXECUTION_CLASSIFIER_AUDIT_20260917.md`, commit `d89971fb9f6df2d7659f7fa8a523e457bdb44ede`, found only a classifier separation defect. No substantive Boundary-S5 output from the implementation was consumed before this repair freeze.

## Repair scope

No hypothesis, object, source identity, S5 conventions, endpoint transpose, source-reversal sign, covariance-orientation sign, boundary representation, 32-component set, 100000-term source expansion, 945 matching set, exact arithmetic, negative controls, PASS/REFUTED/BLOCKED/INVALID criteria, or interpretation ceiling changes.

The repair is only:

1. Execute the frozen independent Critic reconstruction unchanged to a raw JSON file.
2. Reclassify that raw payload under the already-frozen four scientific outcomes, separating implementation/provenance validity from substantive theorem conditions.
3. Preserve the raw JSON byte-for-byte and hash it before producing the repaired classification.
4. Do not read q18 partial values or any Researcher symbolic intermediate/result as expected output.

## Frozen implementation/provenance-validity set A

A requires:

- every `source_checks` entry true;
- static reconstruction controls true: canonical ten-edge ordering, node norms/cross term, exact 24 local actions, C^5=1, T^2=1, generated group size 120, Reynolds rank/pivots/idempotence;
- independent Kirchhoff reconstruction controls true: 125 unit spanning-tree monomials, determinant equals independent tree enumeration, degree 4;
- boundary/source coverage controls true: 32 components, exactly 100000 original source terms, source module total, exact source-matrix reversal;
- all mandatory malformed controls true;
- all forbidden-method controls true.

The substantive identities listed below are deliberately excluded from A.

Failure of A is `INVALID_IMPLEMENTATION`, except an explicit missing required primitive emitted by the base reconstruction is `BLOCKED` with the missing dependency.

## Frozen substantive theorem set B

With A valid, B is the conjunction of:

- exact C source/boundary contragredient dictionary identity;
- exact T source/boundary contragredient dictionary identity;
- exact C inverse source-dictionary roundtrip;
- exact T inverse source-dictionary roundtrip;
- exact C boundary inverse;
- exact T boundary inverse;
- exact all-120 boundary-representation composition;
- exact all-120 edge-orientation-map composition;
- exact C `Psi` and covariance-numerator transport;
- exact T `Psi` and covariance-numerator transport;
- exact complete-Wick/matching orientation factor for all 945 matchings under C;
- exact complete-Wick/matching orientation factor for all 945 matchings under T.

If A and every B condition pass, repaired classification is `CONFIRMED_EXACT_SCOPED`.

If A passes but any B condition fails, repaired classification is `REFUTED_EXACT_SCOPED` only when the raw payload contains a machine-readable exact counterexample sufficient for the failed branch (source-dictionary mismatch with exact rational coefficients, covariance/matching witness identifying the exact failed pair/matching/factor, or exact composition/inverse failure witness). If a substantive condition fails but the current raw payload is insufficient to support the frozen refutation witness requirement, the repaired classifier must output `INVALID_IMPLEMENTATION` with `refutation_witness_missing=true`; a further prospective diagnostic-only repair would then be required before any scientific refutation may be terminalized.

## Frozen BLOCKED rule

If the independent reconstruction reports missing required source/prereg/erratum/derivation objects, output `BLOCKED` and preserve the exact missing list. Do not guess a surrogate.

## Exact result/provenance controls

The repaired runner must record:

- parent Critic prereg commit;
- frozen independent reconstruction implementation commit/blob;
- raw base-result SHA256;
- repaired-runner Git blob SHA1 if available at execution;
- raw base return code;
- complete A and B boolean maps;
- mandatory malformed-control map;
- exact counterexample payload if any;
- `q18_values_used=false`;
- interpretation ceiling unchanged.

## Workflow rule

GitHub Actions may execute only the frozen independent Critic reconstruction plus this classifier wrapper. Green CI alone is not science; the artifact JSON is authority only after all provenance/contract checks are validated.

## Interpretation ceiling

Even `CONFIRMED_EXACT_SCOPED` establishes only independent coefficient-level S5 transport authority for the frozen complete unprojected order-zero all-j=1/2 source/boundary object on `Psi_K5 != 0`. It does not establish any q18 result, all-orbit cancellation, local/full K5 integrability, global Stokes/IBP, invariant-dual periods, physical finite-part selector, reduction of `dim_C F_8=377`, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
