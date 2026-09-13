# Iter076P terminal result — exact Toller conjugation exits the source causal K5 image

Date: 2026-09-13

## Authority

- exact Toller conjugation source snapshot: `eb40c0a321dbaa7bd8a838bc7206a29eb22686f7`
- frozen preregistration: `a0730079deede85153deebd4380b80c6a04bdf95`
- implementation: `1a8e88c332027067166bba9b1a50261bdaa93b05`
- production/workflow head: `1c4a3c1d1c9365a2100f9956503e857aafec490f`
- authoritative run: `34781943529` (`success`)
- aggregate job: `103790458790`
- aggregate artifact: `10325062495`
- aggregate artifact ZIP digest: `sha256:198adaca04cb54ff7b004cd758cdc74518979dd0a25074f85928454ecb0f2b0e`

Raw lane artifacts consumed by the aggregate job:
- A: job `103790433864`, artifact `10325268646`, digest `sha256:2fb1b3c18cdfc55760e357c40bd5ef3c19fec00d2c47adeccdce8c91fed59528`
- B: job `103790433553`, artifact `10324948944`, digest `sha256:d94dbcfc9e1c996619a8cbf4e07bb6c518768dac93c6c763f3d5dab98850efff`
- C: job `103790433746`, artifact `10325556712`, digest `sha256:8de854eb8166410cb56728af8d4ddf8165813ac4f89ae9e457262dd723be9b62`
- D: job `103790433716`, artifact `10325042517`, digest `sha256:196b563436c81883c7bfcc8ad9d62824f66b212f1f9df93d98ec59419b2e6c90`

## Frozen scientific classification

`ITER076P_EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED`

All four prospectively frozen lanes pass and the aggregate output is `valid=true`.

## Terminal facts

### Lane A — exact source identity

The source locks pass. The companion Toller paper gives the exact reduced-matrix relation

`conj(t^(+/- ,rho,k)_{j l m}) = (-1)^(j-l) t^(-/+ ,rho,k)_{l j,-m}`.

For the gamma-simple lowest-spin block `j=l=k`, this becomes a direct branch flip

`conj(t^(kappa,gamma j,j)_{j j m}) = t^(-kappa,gamma j,j)_{j j,-m}`.

No surrogate conjugation law was inserted.

### Lane B — exhaustive causal-image closure census

The `32` source edge-sign assignments generate exactly `16` distinct ten-wedge causal patterns because global `sigma -> -sigma` is redundant.

For every one of those `16` patterns, the all-wedge flipped pattern `-kappa` was compared against the complete source causal image.

Exact counts:
- distinct causal wedge patterns: `16`;
- flipped patterns tested: `16`;
- flipped patterns found in causal image: `0`;
- intersection of causal image and globally branch-flipped image: `0`.

Thus exact Toller conjugation does not close inside the source causal K5 branch set.

### Lane C — local triangle obstruction

For every source-factorizable causal pattern and every one of the `10` K5 triangles,

`kappa_ab kappa_bc kappa_ca = +1`.

The exhaustive certificate gives `160/160` causal triangle products equal to `+1`.

After flipping every wedge branch, every triangle product changes to `-1`; the exhaustive certificate gives `160/160` flipped triangle products equal to `-1`.

This is an exact local obstruction: no globally branch-flipped pattern can be written as `sigma'_a sigma'_b` for any edge-sign assignment.

### Lane D — interpretation firewall

The terminal locks remain:
- known exact Toller conjugation does not close within the causal K5 image;
- no same-causal vertex conjugation symmetry is established;
- no same-causal opposite-`Omega` cancellation is established;
- generic finite-spin signed P3 is not promoted;
- survival of both `Omega` sectors after full integration remains `UNTESTED`;
- Iter076N saddle selection remains unchanged;
- Iter076O exact bulk-overlap result remains unchanged;
- the nominal `epsilon^-1` coefficient remains unestablished.

## Interpretation lock

Iter076O showed that both orientation sectors occur in exact off-saddle bulk support. Iter076P rules out the most direct exact conjugation mechanism as a way to turn that support overlap into a same-causal orientation pairing or cancellation.

The reason is structural rather than numerical. Complex conjugation of a gamma-simple reduced Toller block flips its branch. Doing this on all ten wedges sends a source-factorizable causal K5 pattern to a sign pattern that violates the causal triangle constraints and therefore lies outside the causal vertex sector.

Consequently, the known Toller conjugation identity cannot by itself establish a finite-spin orientation projector or cancellation **within one fixed causal vertex amplitude**.

This is not a no-go theorem for every possible exact finite-spin selector. A different spacetime-parity transformation, a correlated transformation of boundary data, or a genuinely integrated phase/intertwiner interference mechanism could in principle behave differently and would require separate source provenance and prospective testing.

## Current P3 scope

The source-backed signed Hodge/P3 orientation is established on the non-degenerate Lorentzian Regge saddle locus through Iter076N. Generic finite-spin off-saddle signed P3 remains blocked by Iter076O and is not rescued by the known Toller conjugation identity after Iter076P.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation or non-cancellation theorem; no nominal `epsilon^-1` coefficient; no F9/G3/G8/K5 promotion.
