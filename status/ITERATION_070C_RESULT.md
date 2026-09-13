# Iteration 070C result — low-gamma smaller-epsilon pre-pullback convergence extension

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `5d8f184f4c8b52a936bdf88b188b0f070e8e0c6f`
- Implementation: `558f7a52810dcb48b4c1bf42e2eeb2bb50ff00dd`
- Launch/head: `2655c05ce4a91a6b21a88a899fc2a94eee5ee7e1`
- Workflow run: `34741632282`
- Raw job: `103682199101`
- Aggregate job: `103682249488`
- Raw artifact: `10312646506`
- Raw digest: `sha256:ca2e8503cd717ed1113435f0cae2b158ebbb99b6c0f85344c461f0a486faac0b`
- Aggregate artifact: `10313090332`
- Aggregate digest: `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`

Both the raw artifact and frozen aggregate were consumed before classification.

## Frozen terminal result

All preregistered predicates passed.

Terminal classification:

`ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`

At gamma `0.2`, for the new prospective epsilon sequence

`0.0125, 0.00625, 0.003125, 0.0015625`,

all three held-out Schwartz tests (`even`, `oddmix`, `narrow`) showed strictly decreasing relative action error. Final errors at epsilon `0.0015625` were approximately:

- `even`: `0.00342450`
- `oddmix`: `0.00706514`
- `narrow`: `0.00935182`

All are below the frozen `0.08` threshold and below their corresponding terminal Iter068C epsilon=`0.025` errors. Successive halving error ratios approach `2` on every test, but no convergence exponent was fitted or required.

The exact algebraic controls also passed: the `delta'` branch coefficients cancel exactly and the residual `delta` coefficient is exactly `epsilon*c2`.

## Scientific interpretation

This supplies additional evidence that the low-gamma one-edge independent branch-sum action converges toward the identity distribution as finite spectral `epsilon -> 0+` on the frozen held-out test panel.

It does **not** retroactively change Iter068C, which remains terminal as `ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`. It also remains a pre-pullback one-edge/tensor-product control and does not establish that Eq.(5)/(6) survives a non-transverse correlated K4/K5 collision boundary value.

No K5/G3/F9/G8 promotion, physical causal-vertex theorem, fitted counterterm, or preferred sequential prescription is authorized.
