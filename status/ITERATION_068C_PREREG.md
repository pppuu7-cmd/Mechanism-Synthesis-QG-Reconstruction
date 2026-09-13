# Iteration 068C preregistration — distributional pre-pullback EPRL control bridge

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

Does the validated `j=1/2` finite-spectral-`i epsilon` one-wedge distribution recover the source Eq.(5) additive control in the boundary limit on held-out Schwartz tests, and does the independent-wedge sum Eq.(6) follow exactly at the **tensor-product pre-pullback** level?

This gate deliberately stops before the correlated K4/K5 collision pullback.

## Frozen source object

Use the Iter043A exact finite-epsilon distribution

`Theta_(sigma,eps) = A theta(sigma x)e^{-eps|x|} + B delta(x) - sigma c2/2 delta'(x)`

with `rho=gamma/2`, and compare

`S_eps = Theta_(+,eps) + Theta_(-,eps)`

against the identity distribution on fixed Schwartz test functions.

The exact contact controls to record are:

- `delta_prime_plus + delta_prime_minus = 0` identically;
- `delta_plus + delta_minus = eps*c2`, hence tends to zero linearly;
- the bulk coefficients tend to one as `eps -> 0+`.

## Frozen lanes

Gamma values: `1/5`, `6/5`, `2`.

Epsilon sequence in every lane: `0.2, 0.1, 0.05, 0.025`.

Fixed held-out Schwartz tests are those already defined by the source-faithful Iter043A implementation (`even`, `oddmix`, `narrow`), but this gate evaluates the **branch sum**, not the previous branchwise identity.

Matrix: `3 gamma lanes`; each lane evaluates all four epsilons and all three tests.

## Frozen predicates

1. `P1_DPRIME_CANCELS_EXACTLY`: exact one-wedge `delta'` branch coefficients sum to zero for every gamma/epsilon.
2. `P2_DELTA_CONTACT_SCALES_LINEARLY`: the residual `delta` coefficient equals exactly `epsilon*c2`.
3. `P3_BRANCH_SUM_CONVERGES_TO_IDENTITY`: for every test function, the absolute action error decreases monotonically along the frozen epsilon sequence; final-epsilon relative error must be `< 0.08`.
4. `P4_TENSOR_PRODUCT_EQ6_ALGEBRA`: for six abstract K4 edges, the independent `2^6` branch sum factorizes exactly as `prod_e(Theta_e^+ + Theta_e^-)` before any diagonal/collision pullback. This is checked symbolically as a distributive polynomial identity.

## Frozen classification

All predicates pass:

`ITER068C_PREPULLBACK_DISTRIBUTIONAL_EPRL_CONTROL_PASS`

otherwise:

`ITER068C_PREPULLBACK_CONTROL_REVIEW`.

## Scope locks

- This is a pre-pullback/tensor-product control only.
- It does not prove that Eq.(5)/(6) survives a non-transverse correlated K4/K5 pullback or that a unique physical multivariate boundary value exists.
- It does not authorize multiplication of the separately expanded contact distributions on the collision diagonal.
- No K5/G3/F9/G8 promotion, vertex finiteness/divergence theorem, physical sector selection, fitted counterterm, or preferred order follows.
