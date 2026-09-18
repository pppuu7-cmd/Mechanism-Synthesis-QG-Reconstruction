# Prospective preregistration — K5 34-orbit component-1 support-mixing defect diagnostic

Status: FROZEN BEFORE IMPLEMENTATION.

## Motivation
The terminal boundary-component contragredient composition diagnostic (run 35341951171) classified `K5_S5_BOUNDARY_DEFECT_COMPONENT_SUPPORT_MIXING`. Matching preimage, transported type support and Wick eligibility passed; the first mismatch was component 1. This is implementation diagnosis only. Resolver authority remains 0/64.

## Frozen lane
Use exactly the same mask=1, W1, 5-cycle and deterministic frozen matching as the parent diagnostic. Retain canonical ten-edge ordering, all 32 boundary components, 100000 source terms, 945 retained matchings, exact rational arithmetic and the independently confirmed Boundary-S5 transport authority.

## Frozen question
For boundary component 1 only, compare two independently constructed target supports and coefficients:
1. canonical nonzero source-support propagated through the exact boundary contragredient `A^{-T}` component mixing law;
2. target source-support obtained by direct endpoint/orientation transport of the underlying source terms followed by target component projection.

Decompose the first disagreement in this immutable order:
`canonical_nonzero_support -> AinvT_target_component_support -> direct_transported_target_support -> support_index_equality -> coefficient_equality`.
Record the lexicographically first missing/spurious support index and, if support agrees, the first coefficient mismatch.

## Mandatory controls
- exact Fraction/rational arithmetic only;
- component index is exactly 1 and cannot be selected after result inspection;
- all 32/100000/945 provenance cardinalities must be revalidated;
- independent endpoint/orientation roundtrip must pass;
- deliberate wrong transpose (`A^{-1}` in place of `A^{-T}`) must be distinguishable on a predeclared nontrivial control component;
- deliberate mutation of one nonzero source coefficient must be detected;
- no N/B leading coefficients/orders, q18 values, fitted cancellations, or historical resolver coefficient payload may be consumed.

## Frozen classifications
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` if any mandatory validity/control condition fails;
- `K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS` if support indices differ;
- `K5_S5_COMPONENT1_DEFECT_SUPPORT_COEFFICIENT` if support indices agree but an exact coefficient differs;
- `K5_S5_COMPONENT1_SUPPORT_MIXING_EXACT` only if both independently constructed support dictionaries agree exactly.

No Repair-2 or heavy 34-orbit resolver rerun is authorized before this diagnostic is terminal and its artifact is consumed. No scientific/physics promotion follows from any outcome.