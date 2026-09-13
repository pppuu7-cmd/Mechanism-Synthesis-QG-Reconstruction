# Iteration 068C result — distributional pre-pullback EPRL control

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `19255005545d5c4cd505f8ebc9d3afa2ee3f3aae`
- Implementation: `0a13fbfd438e7698348881a48715dcdeb403cd03`
- Initial workflow commit: `05240b0ae88bb0d1f5d5a1a5ac2ab5019b1b622d`
- Initial run `34740836541`: infrastructure-only Python import-path failure before scientific predicates.
- Minimal launcher-only repair: `97b0189313dd7d689378a3601266e558ad26b0ec`
- Authoritative repaired run: `34740924423`
- Aggregate job: `103680419357`
- Aggregate artifact: `10312555350`
- Aggregate digest: `sha256:69786e4ecd550ba25f2329cae9b904d0dab8fba18326115db606f972f3014b2f`

## Frozen result

Aggregate classification:

`ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`

Lane classifications:

- gamma `0.2`: `ITER068C_PREPULLBACK_CONTROL_REVIEW`
- gamma `1.2`: `ITER068C_PREPULLBACK_DISTRIBUTIONAL_EPRL_CONTROL_PASS`
- gamma `2.0`: `ITER068C_PREPULLBACK_DISTRIBUTIONAL_EPRL_CONTROL_PASS`

All three lanes were valid. Exact algebraic predicates passed:

- the `delta'` branch coefficients cancel exactly under the independent one-wedge `+/-` sum;
- the residual `delta` coefficient is exactly `epsilon*c2`;
- the six-edge independent `2^6` branch sum equals the product of the six one-edge branch sums before any collision pullback.

The frozen convergence threshold was not met at gamma `0.2`. The error nevertheless decreased monotonically on all three held-out tests. At epsilon `0.025`, relative errors were approximately:

- `even`: `0.0528646`
- `oddmix`: `0.110921`
- `narrow`: `0.147465`

The preregistered final-error threshold was `<0.08`, hence the lane remains REVIEW. No threshold or epsilon grid is changed retrospectively.

## Scientific interpretation

The source Eq.(5)/(6) additive control is algebraically intact at the independent-edge tensor-product/pre-pullback level, and its finite-epsilon action converges in the tested direction. The frozen finite-epsilon panel is not uniformly converged enough to certify the control for gamma `0.2` under Iter068C.

This result does **not** establish that Eq.(5)/(6) survives a non-transverse correlated K4/K5 collision pullback. It also does not authorize multiplication of the separately contact-expanded distributions. A future smaller-epsilon convergence extension, if useful, must be a new prospective gate rather than a rescue of Iter068C.

No K5/G3/F9/G8 promotion is authorized.
