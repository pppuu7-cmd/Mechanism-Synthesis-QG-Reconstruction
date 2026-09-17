# K5 exact cancellation resolver — geometric/Wick S5 diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE OUTPUT**.

Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Controlling source diagnostics:

- source-vector transport identity confirmed at `dbd03184774a027f6e735138742295dfa211214e`;
- naive post-compression matching transport failed exactly at `d3863af3d3eff5bd8a3511816ecad7b5003d3fc8`;
- full orientation-transpose source-entry transport is exact at `e9a0472da5e55216789f1d6c20118da9f9d59061`.

Frozen vertex cycle: `(1,2,3,4,0)`.
Frozen exact generic alpha witnesses: `W1=(2,3,5,7,11,13,17,19,23,29)` and `W2=(31,37,41,43,47,53,59,61,67,71)` from the parent audit. Their transported values are the already-frozen `perm_weights` outputs.

## Objective

Determine whether the remaining N/B S5 failure lies in the reduced-Laplacian/Wick geometric covariance, rather than in the source coefficient compression.

No physical corner mask, interpolation coefficient, cancellation depth, or scientific local-exponent classifier is used.

## Frozen exact tests

For each frozen witness `W1,W2`:

1. Build the exact reduced K5 Laplacian `L(alpha)` and exact inverse `B0=L^{-1}` in rational arithmetic.
2. Build the full frozen inverse-series matrices `B_n`, `n=0,...,4`, using the same authoritative uniform `Q` as the resolver.
3. At the transported witness `p(alpha)`, rebuild the same series independently.
4. For every oriented edge pair `(i,j)` and every `n=0,...,4`, test the graph-covariance identity

   `C'_{p(i),p(j),n} = s_i s_j C_{i,j,n}`,

   where `C_{ij,n}=r_i^T B_n r_j` and `s_i` is the canonical edge-orientation reversal sign under the frozen vertex cycle.
5. Independently transform the complete weighted source-type dictionary using the already-confirmed orientation-transpose rule, recompress it to a target matching dictionary, and evaluate the full projected Wick channel series at `p(alpha)`.
6. Compare the projected target series coefficient-by-coefficient with the original projected series. The two physical coordinate channels are compared without fitted mixing because the source-vector transport on the frozen Reynolds columns is exactly identity.
7. Repeat the covariance tests with the inverse cycle as round-trip control.

All arithmetic is exact rational/Gaussian-rational. No thresholds or fits.

## Frozen classifier

- `GEOMETRIC_WICK_S5_EXACT`: all reduced-Laplacian covariance identities and both full projected channel series pass exactly for both witnesses and inverse controls.
- `REDUCED_LAPLACIAN_S5_COVARIANCE_FAIL_EXACT`: at least one `C`-series edge-pair identity fails while implementation controls are valid.
- `PROJECTED_WICK_CHANNEL_S5_COVARIANCE_FAIL_EXACT`: all `C`-series identities pass but at least one projected physical channel series fails.
- `INVALID_IMPLEMENTATION`: malformed edge action, failed exact inverse/series construction, failed already-confirmed source recompression control, missing coverage, or broken lineage.

These are implementation/control diagnoses only. They do not establish a physical corner order, local integrability/flux class, global Stokes/IBP statement, period, finite part, regulator independence, or QG result.
