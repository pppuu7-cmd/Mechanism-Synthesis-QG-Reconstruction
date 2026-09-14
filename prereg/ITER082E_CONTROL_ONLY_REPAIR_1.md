# Iter082E control-only repair 1

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION**
Date: 2026-09-14

Parent scientific preregistration: `prereg/ITER082E_SM_K5_NONLINEAR_TUBULAR_CHART_OVERLAP_EXTENSION_CLASS_INDEPENDENCE.md`, commit `15105f6326f652db44809336579060a46403ca8d`.
Quarantined production: run `34895924300`, artifact `10368810908`.
Controlling review: `results/ITER082E_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`.

## Repair scope

This is a **control-only implementation repair**. No scientific criterion, chart formula, divergence order, classification label, or claim ceiling from the parent preregistration may change.

The repaired implementation must replace asserted bookkeeping with explicit polynomial computation.

### R1 — actual polynomial normal transport

For the frozen node-wise radial chart maps, construct truncated exact polynomial maps through total degree 9 and explicitly substitute block-normal perturbations. For every K3/K4/K5 block type, verify from computed coefficients:

- transformed barycentric normal has zero constant term;
- its degree-one normal part is the identity on the barycentric normal subspace;
- neither direction X→V nor V→X lowers the normal-ideal vanishing order.

### R2 — actual nested-chain transport

For all 20 maximal K3⊂K4⊂K5 chains, compute the induced formal transport on the three nested projector increments and verify mechanically that the cumulative ideal orders `(a, a+b, a+b+c)` never decrease through degree 9, in both directions.

A mathematically equivalent exact divisibility/order computation is allowed; merely preassigning `filtration_violations=0` is forbidden.

### R3 — quotient finite-jet check

Use the computed transport matrices/order maps together with the exact frozen inverse series to verify that the induced map on the degree≤9 finite-jet quotient is invertible and preserves the allowed supported-jet class `(omega_3,omega_4,omega_5)=(0,3,8)`.

### R4 — same-machinery negative controls

Frozen malformed variants must be fed into the same validators/calculators. Metadata-only rejection is forbidden. At minimum mechanically realize:

1. nonzero constant shift;
2. label-dependent cubic coefficient;
3. singular linear normal map;
4. explicit degree-lowering malformed map taking a K5 order-9 control to order 8;
5. numeric finite-part injection detected from the representative data structure;
6. reassociation-as-selector injection detected from the operator/provenance data structure.

## Outcome discipline

- If repaired implementation itself is invalid: `INVALID_IMPLEMENTATION_OR_PROVENANCE` and no scientific classification.
- If valid implementation yields any parent P0–P5 failure: parent frozen scientific FAIL label.
- Only if every parent predicate and repaired control passes may the parent frozen PASS label be assigned.

No outcome-driven changes are allowed after production output inspection.
