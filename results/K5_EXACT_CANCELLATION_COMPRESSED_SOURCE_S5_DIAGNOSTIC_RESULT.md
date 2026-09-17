# K5 exact cancellation compressed-source S5 diagnostic — terminal result

Date: 2026-09-17

Classification: **`COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT`**.

This is an exact implementation/control diagnosis for the current cancellation resolver S5 lane. It is not a physical K5 corner, Stokes/IBP, period, finite-part, or downstream-QG verdict.

## Prospective authority

- Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
- Diagnostic preregistration: `3e5303665ecd423b84745e9b74c7a5682116685e`.
- Corrected implementation/head: `b29ad1bcfb99d8565240a15ec921aa37f617fe90`.
- Production run: `35160096950`.
- Job: `105008624008`.
- Artifact: `10473110363`.
- Artifact ZIP SHA256: `16f40f0b0ce51e6a5a05ffca1fa92dde92f20dea8b4b3a4df88dcd2df2cb3f89`.
- Production JSON SHA256: `4f9a1b67905b144f8dd7076cd53d077bb92ce328575166f9481266774ecf6f3f`.

The prior first diagnostic execution had only a runtime-name defect in result serialization; commit `b29ad1bcfb99d8565240a15ec921aa37f617fe90` repaired that execution defect without changing the frozen transport rule or classifier.

## Exact result

All implementation validity controls pass:

- frozen K5 cycle is a permutation;
- all ten edges are present;
- all `945` matching keys are transported bijectively;
- no forward or inverse key collisions occur;
- inverse-cycle round trip is exact;
- orientation global sign is `+1` for the frozen cycle and inverse.

Nevertheless the complete two-channel rational coefficient dictionary is **not** invariant under the frozen compressed matching transport:

- `keys_exact = true`;
- `coefficients_exact = false`;
- classification `COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT`.

The artifact contains explicit exact rational mismatch witnesses; for example the matching `((0, 1), (2, 4), (3, 5), (6, 8), (7, 9))` has base first-channel real coefficient `8/5` while the frozen transported dictionary gives `-88/5` (with additional second-channel mismatch as recorded in the payload).

## Scientific consequence

Together with the earlier source-transport result `S5_SOURCE_TRANSPORT_IDENTITY_CONFIRMED`, this excludes a post-hoc nontrivial constant `2x2` channel-mixing repair: the physical invariant-vector transport is exactly identity, while the compressed matching coefficients fail exact covariance.

Therefore the current exact-cancellation resolver production remains **implementation-invalid for S5 certification** even though its primary interpolation and independent denominator-cleared coefficient routes agree and the purely geometric `U_Z` covariance lane passes. No physical corner order or local integrability/flux label may be promoted from that production yet.

The next highest-information diagnostic is the missing orientation-sensitive source-entry transport inside the compression: under a vertex permutation that reverses a canonical edge orientation, the contraction swaps the source row/column roles in addition to the `C(-v)=-C(v)` sign. The prior compressed diagnostic transported only matching edge indices plus the global sign and did not test this transpose/type action.
