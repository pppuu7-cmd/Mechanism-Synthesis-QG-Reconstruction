# Iter076D preregistration — source-domain local Haar and relative-group jets

Date: 2026-09-13

## Purpose

Establish two independent local-geometry prerequisites of any future source-to-K4 pushforward, while explicitly stopping before a K4 coordinate identification:

1. the exact normalized radial Haar/KAK density jet implied by the repository's source-domain `sinh(beta)^2` measure object; and
2. the exact quadratic BCH jet of the source relative-group argument `g_b^{-1} g_a` in a generic traceless 2x2 Lie-algebra chart.

This gate does not define the reduced K4 variables, does not assign a physical overlap coefficient, and gives zero G3/F9/G8/K5 credit.

## Frozen lanes and predicates

### Lane A — exact radial Haar jet
For symbolic `beta`, define `R(beta)=sinh(beta)^2/beta^2` by analytic continuation at zero. Require exact series

`R(beta)=1 + beta^2/3 + 2 beta^4/45 + O(beta^6)`.

Predicates: exact coefficients `1`, `1/3`, `2/45`; evenness through tested order; no linear/cubic terms.

### Lane B — held-out numerical radial convergence
At frozen `beta={0.1,0.05,0.025,0.0125}`, independently evaluate `R(beta)` at 80-digit precision and the estimator `(R-1)/beta^2`. Require strict convergence of estimator error toward `1/3` and final absolute error `<2e-5`. Negative flat-density control coefficient `0` must be rejected by final estimator distance `>0.3`.

### Lane C — exact relative-group BCH jet
Use generic traceless symbolic matrices `X,Y` and formal scale `t`. Expand

`log(exp(-t Y) exp(t X))`

through order `t^2` by direct matrix-series multiplication and `log(I+Z)=Z-Z^2/2+O(t^3)`. Require exact equality to

`t(X-Y) + t^2 [X,Y]/2`.

Also require order reversal `log(exp(-t X)exp(t Y)) = -log(exp(-t Y)exp(t X)) + O(t^3)`.

### Lane D — negative controls / scope guards
Require both deliberately wrong alternatives to fail identically for the generic symbolic panel:

- BCH quadratic term with sign `-[X,Y]/2`;
- flat normalized radial density `R=1` as a substitute for the source-domain Haar radial jet.

Also require an explicit machine-readable scope field stating `K4_PUSHFORWARD_NOT_ESTABLISHED`.

## Frozen aggregate classification

Only if A-D all pass: `ITER076D_SOURCE_DOMAIN_HAAR_AND_RELATIVE_GROUP_QUADRATIC_JETS_EXACT_SCOPED`.

Any symbolic identity failure is scientific/algebraic FAIL for this scoped prerequisite. Tool/import/runtime failure before predicates is infrastructure failure. Thresholds and formulas are frozen by this commit and may not be weakened after results.

## Claim locks

No source-to-K4 pushforward is inferred; no epsilon^-1 coefficient is inferred; no causal-vertex finiteness/divergence theorem; no physical sector selection; no G3/F9/G8/K5 promotion; no counterterm/fitted cancellation; retain source spectral i-epsilon.
