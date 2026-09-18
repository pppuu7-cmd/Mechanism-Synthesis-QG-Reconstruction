# K5 34-orbit resolver: source-coefficient transport defect diagnostic

Status: PROSPECTIVE IMPLEMENTATION-ONLY DIAGNOSTIC. Frozen before implementation.

## Trigger

Terminal run 35293133302 under prereg commit 37aa29af296a09f05c1a1392d05225416b073106 classified the first mismatch as `K5_34_ORBIT_S5_DEFECT_LOCALIZED_SOURCE_COEFFICIENT_TRANSPORT`. Edge permutation/roundtrip and all 945 matching supports agree exactly; the first mismatch occurs in the per-matching transported source coefficient dictionary for canonical matching `((0,1),(2,4),(3,5),(6,8),(7,9))`. Boundary-S5 independent Critic remains authority. This diagnostic must not alter physics inputs or infer N/B orders.

## Frozen question

On the same frozen lane mask=1, ray=W1, cycle permutation (0 1 2 3 4), which pre-Wick factor first causes the exact per-matching source coefficient transport mismatch?

## Frozen decomposition

For the first mismatching matching only, reconstruct both the independent Boundary-S5 target route and repair-1 pushed route using exact Fraction arithmetic. Compare, in order:

1. source endpoint map for each of the ten source factors;
2. orientation-reversal flags/signs for each source factor;
3. transported source multi-index / component key before boundary contraction;
4. boundary contragredient component coefficient;
5. source spectral/component coefficient before matching restriction;
6. product coefficient attached to the frozen matching immediately before Wick contraction.

Record equality booleans and deterministic hashes at every stage, plus the first mismatching source-factor index/key. Do not emit numerical/scientific N/B leading orders or coefficients.

## Mandatory controls

- Reconstruct conventions solely from the independently confirmed Boundary-S5 authority; no fitted phase, character, 2x2 matrix, relabeling, or post-output convention choice.
- Verify all 32 boundary components and 100000 source terms before restricting to the frozen matching.
- Verify the canonical matching remains present on both routes and matching support itself is unchanged.
- Source-fixed negative control must be rejected.
- Deliberately flip one orientation-reversal flag and require rejection.
- Deliberately alter one boundary contragredient coefficient and require rejection.
- No q18/q19/q21 values and no historical resolver N/B outputs may be consumed.

## Frozen classifications

- `K5_S5_SOURCE_COEFF_DEFECT_ENDPOINT_MAP`
- `K5_S5_SOURCE_COEFF_DEFECT_ORIENTATION_REVERSAL`
- `K5_S5_SOURCE_COEFF_DEFECT_SOURCE_COMPONENT_KEY`
- `K5_S5_SOURCE_COEFF_DEFECT_BOUNDARY_CONTRAGREDIENT`
- `K5_S5_SOURCE_COEFF_DEFECT_SOURCE_SPECTRAL_COMPONENT`
- `K5_S5_SOURCE_COEFF_DEFECT_PREWICK_PRODUCT`
- `K5_S5_SOURCE_COEFF_NO_DEFECT_ON_FROZEN_MATCHING`
- `INVALID_IMPLEMENTATION_OR_PROVENANCE`

## Interpretation ceiling

Implementation diagnosis only. No Repair-2 and no heavy 34-orbit rerun is authorized until this diagnostic is terminal and consumed. Resolver authority remains 0/64. No Stokes/IBP, K5-period, finite-part selector, F9/G3/G8, regulator-independence, NEW_PHYSICS_FOUND, or complete-QG promotion follows.
