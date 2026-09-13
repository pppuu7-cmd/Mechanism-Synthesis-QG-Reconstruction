# Iteration 071A preregistration — correlated K4 epsilon-to-zero Schwartz-action pilot

Date: 2026-09-13

This gate is frozen **before implementation and production**, after terminal Iter070A qualification of every fixed-`epsilon>0` reduced K4 family member as a tempered distribution.

## Question

Along the **source-defined common spectral epsilon ray** (one positive scalar `epsilon` used in every wedge denominator, with the frozen causal signs), do pairings of the reduced K4 joint-spectral family with several physical edge-flow Schwartz test functions show numerically controlled convergence as `epsilon -> 0+`, consistently across the four exact K4 tree/cycle bases?

This is a convergence **pilot**, not a proof of a full Toller/K5 boundary value.

## Frozen object

Use the same reduced source-backed K4 rational family as Iter069/070A,

`K_s(y;epsilon) = prod_e [1 + c1*x_e + (c2/2)*x_e^2] / [x_e - i*s_e*epsilon]`,

with `gamma=6/5`, `rho=gamma/2`, zero external flow `k=(0,0,0,0)`, and signs derived from the eight physical factorized sigma classes

`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

Tree/cycle bases:

`S0, S1, P0, P1`.

Matrix: **32 independent jobs = 8 sigma classes x 4 tree bases**, `fail-fast:false`.

## Frozen physical Schwartz tests

Define the six exact edge flows `x_e(y)` from the incidence solve and use test functions on edge-flow space, pulled back to each cycle basis:

- `G0 = exp(-sum_e x_e^2)`;
- `G1 = (1 + x01 - 2*x13 + x23) * G0`;
- `G2 = (1 + x01*x23 - x02*x13) * G0`.

These are fixed before output and are basis-independent functions of the physical six-edge flow configuration.

## Frozen epsilon sequence

Common source epsilon ray:

`0.20, 0.10, 0.05, 0.025, 0.0125`.

No independent wedge-dependent epsilon ratios are fitted or selected in this gate.

## Frozen numerical estimator

For `k=0`, write `sum_e x_e(y)^2 = y^T Q y`, with exact positive-definite `Q=L^T L` generated from the incidence solve. Whiten this Gaussian exactly/numerically and evaluate each pairing by randomized Sobol quasi-Monte-Carlo under the corresponding normalized Gaussian measure.

Frozen estimator controls:

- four independent Sobol scrambles with seeds `7101,7102,7103,7104`;
- `2^16` points per scramble;
- identical sample budget for every sigma/tree/epsilon/test;
- no adaptive increase after looking at results.

## Frozen lane predicates

For every tree/sigma lane:

1. `Q` is positive definite and the whitening Jacobian is finite/nonzero;
2. all four scramble estimates are finite for every epsilon/test;
3. scramble stability at every epsilon/test:

   `max_r |A_r - mean(A)| / max(1, |mean(A)|) <= 0.05`;

4. for every test, the final two common-epsilon means satisfy

   `|A(0.0125)-A(0.025)| / max(1,|A(0.0125)|) <= 0.20`;

5. for every test, the final-step difference is no larger than the preceding step difference by more than 10%:

   `D_final <= 1.10 * D_previous`,

   where `D_final=|A(0.0125)-A(0.025)|` and `D_previous=|A(0.025)-A(0.05)|`.

The numerical thresholds are deliberately modest because this is a pilot; they are frozen now and may not be weakened after output.

## Frozen aggregate basis-covariance predicate

For each fixed `(sigma,epsilon,test)`, compare the four tree-basis grand means. Require

`max_tree |A_tree - mean_tree(A)| / max(1, |mean_tree(A)|) <= 0.08`.

This tests the same edge-flow Schwartz pairing in four exact cycle coordinate systems. No preferred basis may be selected after output.

## Frozen classification

All 32 lanes valid and all lane + aggregate predicates pass:

`ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_CONVERGENCE_PILOT_SUPPORTED`

Otherwise, if numerical controls are valid but any convergence/covariance predicate fails:

`ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_REVIEW`

If estimator validity fails:

`ITER071A_NUMERICAL_VALIDITY_FAIL`.

## Interpretation locks

- A PASS is only finite-panel numerical support for convergence along the source-defined common epsilon ray in the reduced K4 rational family.
- It is not a theorem of a unique `S'` boundary value, path independence under arbitrary epsilon ratios, a full Toller wavefront/tube theorem, or K5 causal-vertex existence/fin\-iteness.
- A REVIEW does not prove nonexistence/divergence; it localizes either slow convergence, basis inconsistency, or numerical resolution limits for the frozen panel.
- No arbitrary subtraction/counterterm, preferred tree/order, K5/G3/F9/G8 promotion, or physical sector selection is authorized.
