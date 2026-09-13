# Iter076P preregistration — can exact Toller conjugation act within the source causal K5 sector?

Date: 2026-09-13

## Purpose

Iter076O proves that exact Heaviside bulk support contains both nonzero `Omega_sigma` sectors off saddle for the same fixed source causal data. A generic finite-spin orientation selector, if it exists, must therefore arise from stronger weighting/interference structure.

The newly frozen source snapshot `sources/TOLLER_MATRICES_2026_CONJUGATION_BRANCH_FLIP_SNAPSHOT.md` records an exact candidate symmetry: complex conjugation of a reduced gamma-simple Toller block flips its branch `kappa -> -kappa` (with the corresponding magnetic-index reversal).

This prospective gate tests whether that exact branch flip remains inside the source-defined causal K5 image `kappa_ab=sigma_a sigma_b`. If it does not, the known conjugation identity cannot by itself provide a same-causal full-amplitude pairing, cancellation, or orientation projector.

No Iter076P production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Frozen objects

Five source edge signs:

`sigma=(sigma_0,...,sigma_4) in {+/-1}^5`.

Ten K5 wedge signs:

`kappa_ab=sigma_a sigma_b`, for all `a<b`.

Define the all-wedge conjugation flip

`C(kappa)_ab = -kappa_ab`.

Use the exact source identity in the gamma-simple lowest-spin block:

`conj(t^(kappa,gamma j,j)_{j j m}(beta)) = t^(-kappa,gamma j,j)_{j j,-m}(beta)`.

The gate concerns only branch-pattern closure. It does not assume that magnetic-index reversal leaves a chosen boundary state invariant.

## Frozen lanes

### Lane A — source identity lock

Verify the committed source snapshot contains:
1. the exact companion-paper conjugation relation with branch flip;
2. its gamma-simple `j=l=k` specialization;
3. the source causal factorization `kappa_ab=sigma_a sigma_b`;
4. the explicit scope guard that no full-amplitude cancellation is inferred.

PASS iff all four locks are present and no surrogate identity is inserted.

### Lane B — exhaustive causal-image closure census

Enumerate all `32` edge-sign assignments `sigma` and construct their ten-wedge patterns. Record the `16` distinct patterns modulo global edge reversal.

For every distinct causal pattern `kappa`, test whether the all-wedge flipped pattern `-kappa` equals the causal pattern of any of the `32` possible `sigma'` assignments.

PASS iff:
- the causal image has exactly `16` distinct wedge patterns;
- `0/16` all-wedge flipped patterns lie in that image;
- equivalently, the causal image and its global branch-flipped image are disjoint.

### Lane C — triangle obstruction certificate

For every one of the `16` distinct causal patterns and each of the `10` K5 triangles `(a,b,c)`, compute

`P_abc = kappa_ab kappa_bc kappa_ca`.

PASS iff:
- all `160/160` causal triangle products are `+1`;
- all `160/160` triangle products of the globally branch-flipped patterns are `-1`.

This is the local exact certificate that no all-wedge branch-flipped pattern can be source-factorized.

### Lane D — interpretation firewall

PASS iff the aggregate records all of the following hard locks:
- `known_toller_conjugation_closes_within_causal_K5_image = false`;
- `same_causal_vertex_conjugation_symmetry_established = false`;
- `same_causal_opposite_Omega_cancellation_established = false`;
- `generic_finite_spin_signed_P3_promoted = false`;
- `both_Omega_sectors_survive_full_integration = UNTESTED`;
- `Iter076N_saddle_selection_unchanged = true`;
- `Iter076O_bulk_overlap_unchanged = true`;
- `epsilon_minus1_coefficient_established = false`.

## Frozen interpretation

If A-D pass, classify:

`ITER076P_EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED`

Meaning: the exact known Toller conjugation identity flips every reduced wedge branch, but the resulting K5 branch pattern is not realizable by any source causal edge assignment. Therefore this identity cannot by itself pair or cancel opposite `Omega_sigma` sectors **inside a fixed source causal vertex amplitude**.

This does not prove that no other exact finite-spin orientation selector exists. It rules out the most direct branch-conjugation mechanism and leaves parity/boundary-state/full-integral interference as separate questions.

If the source locks fail, classify:
`ITER076P_TOLLER_CONJUGATION_SOURCE_LOCK_FAIL`.

If any globally flipped causal pattern remains source-factorizable, classify:
`ITER076P_CAUSAL_IMAGE_CLOSED_UNDER_BRANCH_FLIP_REVIEW`.

If the triangle certificate fails, classify:
`ITER076P_TRIANGLE_FACTOR_CERTIFICATE_FAIL`.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no nominal `epsilon^-1` coefficient; no F9/G3/G8/K5 promotion.
