# Iteration 070C preregistration — low-gamma smaller-epsilon pre-pullback convergence extension

Date: 2026-09-13

This is a **new prospective secondary gate**. It does not change or rescue the terminal Iter068C classification.

## Question

For the gamma=`0.2` lane that remained `CONTROL_REVIEW` in Iter068C, does the exact one-wedge branch-sum action continue monotonically toward the identity distribution on the same frozen held-out Schwartz tests when `epsilon` is extended to smaller values?

## Frozen object and tests

Use exactly the Iter068C finite-spectral `j=1/2` distributional branch sum and the same three held-out tests:

`even`, `oddmix`, `narrow`.

Gamma is fixed at `0.2`.

New epsilon sequence, frozen before output:

`0.0125, 0.00625, 0.003125, 0.0015625`.

## Frozen predicates

1. exact `delta'` branch coefficients cancel;
2. exact residual `delta` coefficient is `epsilon*c2`;
3. for each of the three tests, relative action error decreases strictly at every step of the new epsilon sequence;
4. for each test the final error at epsilon `0.0015625` is `<0.08` (the same numerical scale used in Iter068C, but applied only in this new prospective gate);
5. the final error is smaller than the terminal Iter068C epsilon=`0.025` error for the same test.

Record empirical halving ratios/errors, but do not fit or require a post-hoc convergence exponent.

## Frozen classification

All predicates pass:

`ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`

otherwise:

`ITER070C_LOW_GAMMA_PREPULLBACK_CONVERGENCE_REVIEW`.

## Scope locks

- Iter068C remains terminal as `...REVIEW_1_OF_3`; this gate is additional evidence only.
- This is still pre-pullback and one-edge branch-sum control. It does not prove a non-transverse correlated K4/K5 boundary-value identity.
- No K5/G3/F9/G8 promotion, physical vertex theorem, or retroactive threshold change is authorized.
