# K5 exact cancellation resolver — orientation-transpose source S5 diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE DIAGNOSTIC OUTPUT**.

Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Prior exact controls:

- source-derived invariant-vector channel transport is identity (`S5_SOURCE_TRANSPORT_IDENTITY_CONFIRMED`, result commit `dbd03184774a027f6e735138742295dfa211214e`);
- naive compressed matching transport fails exactly (`COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT`, production head `b29ad1bcfb99d8565240a15ec921aa37f617fe90`, durable result commit `d3863af3d3eff5bd8a3511816ecad7b5003d3fc8`).

Frozen cycle: `(1,2,3,4,0)` and its inverse.

## Defect hypothesis frozen before outcome

The prior compressed diagnostic transports each perfect-matching edge index and multiplies by the product of orientation signs, but it acts **after** the source-entry types `(row,col)` have been contracted away. Under a vertex permutation that reverses the canonical orientation of an edge, the boundary contraction also exchanges which endpoint supplies the matrix row and which supplies the matrix column. Therefore the source-entry type must transform as

- orientation preserved: `(row,col) -> (row,col)`;
- orientation reversed: `(row,col) -> (col,row)`;

at the permuted edge position.

This transpose/type action is frozen now as the only new transport ingredient. No channel fit, coefficient fit, random witness, corner coefficient, or post-outcome convention change is allowed.

## Exact tests

Using the already-authoritative `TCW`, `ENTRY`, `MATCH_COEFF`, edge order and invariant channel weights from the parent source construction:

1. Transport the complete weighted source-type dictionary `TCW` under the frozen cycle by permuting edge positions and applying the orientation-dependent `(row,col)` transpose above.
2. Compare the transported `TCW` dictionary exactly, key by key and two-channel rational coefficient by coefficient, with the original `TCW`.
3. Recompress the transported `TCW` independently through the exact entry-metric/Wick matching construction and compare the resulting complete `945`-matching two-channel rational dictionary with the authoritative `MATCH_COEFF`.
4. Repeat with the inverse cycle and require exact round trip.
5. Record separately:
   - type-key coverage/collisions;
   - `TCW` coefficient equality;
   - recompressed matching-key coverage;
   - recompressed coefficient equality;
   - orientation-reversal count;
   - mismatch witnesses.

No physical `N/B/U` corner coefficient is used.

## Frozen classifier

- `ORIENTATION_TRANSPOSE_SOURCE_S5_EXACT` iff full transported `TCW` and independently recompressed `MATCH_COEFF` both agree exactly for cycle and inverse/round-trip controls.
- `SOURCE_TYPE_S5_COVARIANCE_FAIL_EXACT` iff the transported `TCW` itself fails exact equality while implementation controls are valid.
- `ENTRY_COMPRESSION_S5_COVARIANCE_FAIL_EXACT` iff transported `TCW` is exact but independently recompressed matching coefficients fail.
- `INVALID_IMPLEMENTATION` for malformed edge action, missing/colliding keys, failed inverse round trip, incomplete 10-edge/type coverage, or broken authoritative lineage.

These are implementation/control diagnoses only. None is a physical K5, local integrability, global Stokes/IBP, period, finite-part, regulator-independence, or QG verdict.

## Consequence lock

If `ORIENTATION_TRANSPOSE_SOURCE_S5_EXACT`, the current resolver S5 lane may be repaired only by this prospectively frozen full source-entry transport and then must be rerun; no old payload is promoted automatically.

If `SOURCE_TYPE_S5_COVARIANCE_FAIL_EXACT`, the next target is the local leg-order / invariant-weight source construction before any corner rerun.

If `ENTRY_COMPRESSION_S5_COVARIANCE_FAIL_EXACT`, the next target is the exact `ENTRY`/Wick compression map before any corner rerun.
