# Iteration 071A result — K4 common-epsilon Schwartz-action pilot

Date: 2026-09-13

## Authoritative provenance

- Frozen preregistration commit: `dd13d17c729447d01fd262bce3d2ae5bcc06396b`
- Initial production run: `34741885070` — implementation/infrastructure invalid only (NumPy boolean JSON serialization after the science calculation; no usable raw result artifact), therefore non-authoritative for scientific classification.
- Minimal serialization-only repair / authoritative head: `9c78128d144741f528338ec7613c4b268c7b76f7`
- Authoritative repaired run: `34741938861`
- Scientific matrix lanes: `32/32` completed successfully and numerically valid.
- Aggregate job: `103683058319`
- Aggregate artifact: `10312601343`
- Aggregate digest: `sha256:53adba7a50db94dfdeac5f340d569bc5b079672f310536858a86f12602904544`

## Frozen result

Terminal classification:

`ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_REVIEW`

Aggregate predicates:

- `all_numerically_valid = true`
- `all_lane_convergence_predicates = false`
- `basis_covariance_pass = false`
- worst normalized finite-sample basis spread: `4.40981603077861`
- worst key: `sigma=+-++`, `epsilon=0.0125`, `G1`

The frozen gate therefore does **not** support convergence of the reduced K4 common-epsilon Schwartz actions at the fixed QMC resolution used in Iter071A.

## Causal audit

The failure is not an invalid geometry, NaN, parser, or workflow failure. Representative raw artifacts for the aggregate worst sigma `+-++` were consumed in all four cycle bases (`S0`, `S1`, `P0`, `P1`). In each basis:

- the quadratic form / whitening geometry predicate is valid;
- all estimates are finite;
- the small-epsilon fixed-budget Sobol scramble variance grows sharply;
- the final Cauchy step worsens rather than contracts;
- P3/P4/P5 fail together.

At `epsilon=0.0125`, the `G1` normalized scramble spread is approximately `1.85` (S0), `2.49` (S1), `5.81` (P0), and `2.18` (P1). This is qualitatively consistent with an unresolved singular-collision scaling regime under the original x-space QMC estimator.

This causal audit does **not** reclassify the frozen REVIEW as a divergence theorem. It localizes the blocker: fixed-budget x-space QMC is not a reliable discriminator of the `epsilon -> 0+` boundary-value behavior at the current resolution.

## Scientific interpretation

Iter071A is a **SCOPED REVIEW / numerical-resolution blocker** for the finite-panel reduced K4 common-epsilon pilot.

It does not prove:

- non-existence of an `S'` boundary value;
- divergence of the source-defined causal vertex;
- arbitrary-path dependence;
- any physical causal-sector selection;
- a K5 correlated extension;
- G3/F9/G8 promotion.

The historical first run remains implementation-invalid and is not rewritten as a scientific result. Frozen thresholds are unchanged.

## Next admissible gate

Do **not** simply increase the same quadrature density. The next gate must introduce a mathematically justified singular-collision object. The preferred route is a prospective common-epsilon blow-up/scaling audit obtained from the exact change of variables `x = epsilon y` near the full K4 collision, with the leading `epsilon^{-3}` candidate coefficient tested independently and with basis covariance frozen before production. Such a gate can distinguish a genuine nonzero leading collision coefficient from the variance blow-up seen by Iter071A without modifying Iter071A criteria post hoc.

K5 remains blocked pending a source-faithful correlated extension/boundary-value object and distributional Eq.(5)/(6) inheritance.
