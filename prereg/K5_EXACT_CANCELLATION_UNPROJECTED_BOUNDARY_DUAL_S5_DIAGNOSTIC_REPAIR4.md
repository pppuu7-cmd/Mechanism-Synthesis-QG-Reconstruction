# K5 exact cancellation unprojected boundary-dual S5 diagnostic — execution repair 4

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR-4 OUTPUT**.

Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`, `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`.

Parent diagnostic preregistration: `41f26f8e314f4ab1213fe6a681b69d2c87e00d68`.

Execution repairs 1–3: `fa0eb9027a7df8138a6cef734ef75fbf43200815`, `a7d0057bcbde959df84bd5da3fb96447ced01175`, `a03481f8020cd0eaf9426b9a569913a459f55b19`.

Repair-3 terminal recovery authority: `status/K5_EXACT_CANCELLATION_S5_RECOVERY_20260917.md`, reconciliation commit `438a97c455b6b3fbfb5f70c9cbe370142c166e6d`.

Historical diagnostic runs `35175131496`, `35177472120`, `35177549375`, and `35185801499` terminated `cancelled` before a complete classifier. No partial substantive values from those runs are authority.

## HYPOTHESIS

The already-frozen complete unprojected boundary-dual S5 diagnostic can terminalize exactly if its six unique frozen alpha evaluations are executed as six independent GitHub Actions shards and recombined only after every shard has produced the complete 32-component, 100000-source-term exact parent `unprojected(alpha)` vector.

This is an execution/parallelization hypothesis only. It does not alter the diagnostic object, the frozen witnesses, the S5 action, the coordinate extraction, the four candidate representation laws, or the classifier.

## exact OBJECT

Exactly the parent diagnostic object from `41f26f8e314f4ab1213fe6a681b69d2c87e00d68`: the complete unprojected 32-component order-zero boundary Wick amplitude `a(alpha) in C^32`, built from the authoritative all-`j=1/2`, all-32, 100000-source-term K5 source object, at the two frozen witnesses and their frozen cycle/inverse images, before Reynolds/dual-channel projection.

The six unique alpha objects are frozen as:

- `W1_base = W1`;
- `W1_cycle = perm_weights(W1, cycle)`;
- `W1_inverse = perm_weights(W1, cycle^{-1})`;
- `W2_base = W2`;
- `W2_cycle = perm_weights(W2, cycle)`;
- `W2_inverse = perm_weights(W2, cycle^{-1})`.

The logical parent call graph still contains eight uses: each base vector is reused for both its cycle and inverse lane, so exactly six unique exact vectors are computed and two logical base evaluations are reuse-only.

No physical-corner mask, interpolation coefficient, leading cancellation order, local exponent, fitted 2x2 channel matrix, finite part, regulator choice, or post-hoc boundary state is introduced.

## DEPENDENCY

`full source-ordered all-32 K5 boundary object + exact order-zero Wick geometry + authoritative 32-dimensional S5 action + Reynolds projector -> source-derived representation law of unprojected boundary amplitude -> authoritative invariant-dual coordinate transport -> execution authorization for parent exact-cancellation resolver`.

The parent exact-cancellation scientific gate remains blocked until this diagnostic terminalizes validly.

## SOURCE AUTHORITY

- source ordering: `one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`;
- corrected Iter077I authority: run `34786586785`, alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; historical run `34786550378` remains failure/non-authority;
- invariant-dual K5 projective object: result commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`;
- canonical physical numerator DAG: commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`;
- parent exact-cancellation gate: `d6b0e805101c8590eafac71398cc2b1466691752`;
- exact source-vector S5 transport: `dbd03184774a027f6e735138742295dfa211214e`;
- exact orientation-transpose source-entry transport/recompression: `e9a0472da5e55216789f1d6c20118da9f9d59061`;
- projected-Wick diagnostic localizing the remaining issue to dual-coordinate interpretation: `6b545c6e3195fe32221370fa76791b89bf7a5ee8`;
- parent diagnostic implementation `scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py`, whose exact direct recursive `unprojected(alpha)` function is the shard evaluator;
- published one-wedge spectral `i epsilon` retained unchanged.

## FROZEN INPUTS

- all source spins `j=1/2`;
- all 32 boundary basis states;
- all original `100000` source node-choice terms for every shard;
- exact `Fraction` / Gaussian-rational arithmetic only;
- cycle `(1,2,3,4,0)` and its exact inverse;
- `W1=(2,3,5,7,11,13,17,19,23,29)`;
- `W2=(31,37,41,43,47,53,59,61,67,71)`;
- the six unique alpha labels above, with no adaptive shard creation;
- order-zero Wick contraction only;
- exact reduced-Laplacian `B0=L(alpha)^-1` as in the parent diagnostic;
- exact 32x32 S5 action matrices reconstructed from source local tensor action;
- Reynolds rank two and pivots `[1,4]`;
- authoritative dual coordinates `P^T a` and current compressed weighted coordinates;
- exactly four candidate representation laws: `A`, `A^-1`, `A^T`, `A^-T`;
- parent classification taxonomy unchanged;
- each shard may use a 45-minute infrastructure timeout; aggregation may use 15 minutes;
- no scientific tolerance, approximation, floating-point conversion, truncated source support, or post-output retry with altered scientific inputs.

## POSITIVE CONTROLS

P1. Every shard must verify the parent diagnostic prereg SHA and exact frozen alpha tuple for its label before evaluation.

P2. Every shard must call the unchanged parent direct-recursive `unprojected(alpha)` evaluator, return exactly 32 complex-rational components, and report exactly `100000` traversed source terms.

P3. Each component must serialize numerator/denominator exactly; no float or tolerance is permitted.

P4. Aggregation requires exactly the six predetermined labels and rejects missing, duplicate, or extra shard labels.

P5. Aggregation independently recomputes the six expected alpha tuples from `W1`, `W2`, the frozen cycle and inverse and requires exact equality with shard manifests.

P6. Aggregation reconstructs exactly 24 local S5 actions, exact `A*A^-1=I=A^-1*A`, Reynolds rank two and pivots `[1,4]`.

P7. The four parent logical lanes are reconstructed exactly from the six shards: W1-cycle, W1-inverse, W2-cycle, W2-inverse; the same base shard is reused in the two directions for each witness.

P8. For every lane, authoritative dual coordinates are computed as the pivot entries of `P^T a`, and current weighted compressed coordinates are recomputed exactly from the frozen weights; no fitted channel transform is permitted.

P9. For every lane, all four predetermined representation laws are evaluated exactly and the parent classifier is copied verbatim:
`BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT`, `BOUNDARY_S5_OTHER_REPRESENTATION_EXACT`, `DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT`, or `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT`.

P10. A deterministic aggregate manifest records all six shard labels, alpha tuples, exact source-term counts, vector lengths, and per-shard SHA256 digests before classification.

## NEGATIVE CONTROLS

N1. A synthetic manifest with `W1_cycle` assigned the `W1_inverse` alpha tuple must be rejected before reading its vector as a valid shard.

N2. A synthetic shard with one of the 32 boundary components removed must be rejected by the exact vector-length contract.

N3. A synthetic aggregate with the first entry of `A` perturbed by exact `+1` must fail the exact inverse/action control.

N4. Any missing/extra label, altered witness, altered cycle, changed source-term count, changed Reynolds pivots, altered representation-law list, float conversion, thresholded equality, physical-corner coefficient use, or post-hoc channel fit is `INVALID_IMPLEMENTATION`.

## PASS

Repair-4 execution is valid only if P1-P10 and N1-N4 pass and the aggregate emits exactly one pre-existing non-invalid parent diagnostic classification:

- `BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT`;
- `BOUNDARY_S5_OTHER_REPRESENTATION_EXACT`;
- `DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT`;
- `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT`.

Green CI alone is not PASS; all six complete shard payloads, aggregate controls, exact classifier, hashes, and artifact are required.

## FAIL

There is no new repair-specific scientific FAIL. A valid non-invalid parent diagnostic classification is recorded exactly as emitted. A coordinate/representation mismatch is a valid diagnostic result, not automatically a physical K5 failure.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` only if controlling source authority required by the parent diagnostic becomes unavailable or inconsistent. Runtime/runner cost is not an object-definition blocker.

## INVALID

`INVALID_IMPLEMENTATION` if any frozen shard/aggregate/negative/lineage control fails, if any finite sum is truncated or altered, if the parent classifier changes, or if forbidden physical-corner values are consumed.

`INFRASTRUCTURE_FAILURE` if one or more shards or the aggregate fail to terminalize for runner/time/resource reasons. No partial shard or aggregate substantive value becomes authority.

## INTERPRETATION CEILING

This diagnostic may establish only the exact S5 representation law of the unprojected order-zero boundary Wick object and whether the current weighted two-channel extraction equals the authoritative `P^T` invariant-dual coordinates. It may authorize an execution-only repair of the already-frozen parent exact-cancellation resolver.

It does **not** classify any physical Schwinger corner, prove local finiteness/divergence, establish global Stokes/IBP, determine an invariant-dual K5 period, reduce `dim_C F_8=377`, select a physical finite part, prove regulator independence, establish F9/G3/G8/K5, imply `NEW_PHYSICS_FOUND`, or complete quantum gravity.