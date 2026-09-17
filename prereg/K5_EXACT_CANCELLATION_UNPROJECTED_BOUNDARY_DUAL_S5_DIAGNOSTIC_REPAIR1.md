# K5 exact cancellation unprojected boundary-dual S5 diagnostic — execution repair 1

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR-1 OUTPUT**.

Parent diagnostic preregistration: `41f26f8e314f4ab1213fe6a681b69d2c87e00d68`.
Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Failed/cancelled production: run `35175131496`, job `105055061459`.

## Concrete defect

The frozen diagnostic has a 20-minute workflow timeout. Its first production completed checkout and lineage verification but was cancelled during the exact unprojected 32-state / 100000-source Wick contraction at the timeout boundary, before producing a scientific classifier.

Inspection of the frozen implementation shows deterministic duplicate work: for each witness, `lane(..., cycle, ...)` and `lane(..., inverse, ...)` each recompute the identical base `unprojected(alpha)`. Across W1/W2 this executes the expensive exact contraction 8 times although there are only 6 distinct alpha tuples (base, cycle image, inverse-cycle image for each witness).

## Frozen repair

Repair 1 changes execution only:

1. Keep the original diagnostic implementation and all mathematical definitions unchanged.
2. Memoize `unprojected(alpha)` by the exact alpha tuple for the lifetime of the process.
3. Require exactly 6 unique unprojected evaluations for the two frozen witnesses and cycle/inverse lanes; repeated base evaluations must be cache hits.
4. Do not change W1/W2, cycle, inverse cycle, 32-state boundary basis, 100000-source coverage, Wick order, Reynolds projector, pivot coordinates, action matrices, representation laws, classifier, or any scientific threshold.
5. Do not use physical-corner coefficients.
6. Keep full-history lineage verification against this repair preregistration, the parent diagnostic preregistration, the geometric/Wick terminal result, and the parent exact-cancellation gate.

## Terminal interpretation

A successful repair-1 workflow is not by itself scientific PASS. The terminal classifier remains exactly one of the parent frozen diagnostic outcomes:

- `BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT`
- `BOUNDARY_S5_OTHER_REPRESENTATION_EXACT`
- `DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT`
- `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT`
- `INVALID_IMPLEMENTATION`

No local corner, Stokes/IBP, integrated-period, finite-part, regulator-independence, or downstream-QG conclusion is authorized by this execution repair.
