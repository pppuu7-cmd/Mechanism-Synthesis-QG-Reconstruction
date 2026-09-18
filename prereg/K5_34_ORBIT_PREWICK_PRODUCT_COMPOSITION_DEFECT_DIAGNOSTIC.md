# K5 34-orbit resolver: pre-Wick product composition defect diagnostic

Status: PROSPECTIVE IMPLEMENTATION-ONLY DIAGNOSTIC. Frozen before implementation.

## Trigger

Terminal run 35301356348 under prereg commit bf520ee5eb2a72d4aad867cb0b97f80299f2c301 returned `INVALID_IMPLEMENTATION_OR_PROVENANCE`, with stage equalities endpoint_map=true, source_component_key=true, boundary_contragredient=true, source_spectral_component=true and prewick_product=false; the mandatory orientation-reversal negative control discriminated. This is not a scientific FAIL. Boundary-S5 independent Critic remains authority and resolver authority remains 0/64.

## Frozen question

On the same frozen lane mask=1, ray=W1, cycle permutation (0 1 2 3 4), and canonical matching `((0,1),(2,4),(3,5),(6,8),(7,9))`, what exact composition operation first makes the independently reconstructed target pre-Wick matching coefficient differ from the repair-1 push-forward coefficient?

## Frozen decomposition

Use exact Fraction arithmetic and reconstruct from source data, not historical N/B outputs. For the frozen matching compare the target route with the pushed canonical route at these nested stages:

1. canonical matching and its unique S5 preimage/image roundtrip;
2. per-edge endpoint permutation and reversal flags;
3. per-source-term transported type tuple before matching projection;
4. matching-eligibility indicator before and after transport;
5. per-boundary-component contribution to the matching coefficient, before summing the 32 components;
6. channel-wise real/imag contribution after boundary contragredient weighting;
7. final sum over all 32 components.

For the first unequal stage record only deterministic hashes, equality booleans, counts, first component/source-term index, and whether the discrepancy is a pure sign, component permutation, multiplicity, or nontrivial rational mismatch. Do not emit N/B leading orders or physical coefficients.

## Mandatory controls

- Independently reconstruct all 32 boundary components and 100000 source terms and retain all 945 matchings before restricting to the frozen matching.
- Verify exact edge/matching permutation roundtrip.
- Verify the frozen matching has exactly one canonical preimage under the edge permutation.
- Verify source-fixed transport is rejected.
- Verify one deliberately flipped reversal flag is rejected.
- Verify one deliberately permuted boundary component is rejected.
- Verify one deliberately changed contribution multiplicity is rejected.
- No fitted phase, character, 2x2 matrix, relabeling, coefficient cancellation choice, q18/q19/q21 value, or historical resolver N/B output may be used.

## Frozen classifications

- `K5_S5_PREWICK_DEFECT_MATCHING_PREIMAGE`
- `K5_S5_PREWICK_DEFECT_TYPE_TRANSPORT`
- `K5_S5_PREWICK_DEFECT_MATCHING_ELIGIBILITY`
- `K5_S5_PREWICK_DEFECT_BOUNDARY_COMPONENT_COMPOSITION`
- `K5_S5_PREWICK_DEFECT_CHANNEL_REIM_COMPOSITION`
- `K5_S5_PREWICK_DEFECT_FINAL_COMPONENT_SUM`
- `K5_S5_PREWICK_NO_DEFECT_ON_FROZEN_MATCHING`
- `INVALID_IMPLEMENTATION_OR_PROVENANCE`

## Interpretation ceiling

Implementation diagnosis only. No Repair-2 and no heavy 34-orbit resolver rerun is authorized until this diagnostic is terminal and consumed. Resolver authority remains 0/64. No Stokes/IBP, K5-period, finite-part selector, F9/G3/G8, regulator-independence, NEW_PHYSICS_FOUND, or complete-QG promotion follows.
