# K5 exact cancellation resolver — unprojected boundary dual S5 diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE OUTPUT**.

Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Authoritative invariant-dual object: `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, which requires dual projection `P^T` because the stripped 32-state boundary basis is non-orthonormal.
Controlling diagnostics: source-vector columns are fixed by the S5 cycle; reduced-Laplacian covariance is exact; projected channel scalar invariance nevertheless fails.

Frozen vertex cycle: `(1,2,3,4,0)` and inverse.
Frozen generic exact witnesses: parent `W1`, `W2` at no corner scaling.
Frozen Wick-series diagnostic order: **series order zero only**, because the preceding exact geometric/Wick diagnostic already shows the channel mismatch at order zero. No higher-order outcome is needed to identify the representation law.

## Objective

Compute the complete **unprojected 32-component boundary Wick object** before any Reynolds/dual-channel projection and determine its exact S5 representation law directly.

No physical corner mask, interpolation coefficient, cancellation order, or fitted 2x2 matrix is used.

## Frozen reconstruction

For each generic alpha witness:

1. Build exact rational `B0=L(alpha)^{-1}` using the same K5 reduced-Laplacian authority.
2. For each of all 32 boundary basis states, contract its complete authoritative source node-choice sum (all terms collectively covering the parent 100000 source terms) through the exact order-zero Wick pairing, retaining the full complex rational amplitude. This produces `a(alpha) in C^32`.
3. Repeat at `p(alpha)` and `p^{-1}(alpha)`.
4. Independently reconstruct the exact 32x32 S5 action matrices `A_p`, `A_{p^{-1}}` from the local tensor action, as in the original invariant-dual authority.
5. Test, with no fitting, all four predetermined representation laws:
   - vector: `a(p alpha)=A_p a(alpha)`;
   - inverse-vector: `a(p alpha)=A_p^{-1} a(alpha)`;
   - transpose: `a(p alpha)=A_p^T a(alpha)`;
   - dual/contragredient: `a(p alpha)=A_p^{-T} a(alpha)`.
6. Require the same unique law for W1 and W2 and consistent inverse-cycle round trip.
7. Compute invariant-dual coordinates exactly as frozen by the parent authority: `P^T a`, represented by its RREF pivot coordinates `[1,4]`, and record whether those coordinates are invariant under the law actually satisfied by `a`.
8. Independently compare the weighted two-channel contraction currently used by the compressed implementation with these authoritative `P^T a` pivot coordinates at the same generic witnesses.

## Frozen classifier

- `BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT` iff the unique exact law is `A^{-T}` for both witnesses and inverse controls, the `P^T` pivot coordinates are invariant, and the weighted compressed coordinates equal the authoritative coordinates.
- `BOUNDARY_S5_OTHER_REPRESENTATION_EXACT` iff exactly one of the other three predetermined laws is exact consistently; record which law, without post-hoc redefinition.
- `DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT` iff `A^{-T}` is exact but the current compressed weighted coordinates differ from authoritative `P^T a` coordinates.
- `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT` iff none or multiple predetermined laws fit exactly while implementation controls pass.
- `INVALID_IMPLEMENTATION` for incomplete 32-state/source coverage, failed A/inverse reconstruction, failed exact B0 construction, or broken lineage.

No classifier here is a physical corner, local integrability, global Stokes/IBP, period, finite-part, regulator-independence, or QG result.
