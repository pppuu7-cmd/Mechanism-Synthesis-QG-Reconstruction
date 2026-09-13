# Iteration 068B preregistration — Appendix-D contact-layer wavefront obstruction

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

Does the source-backed `j=1/2` finite-spectral-`i epsilon` Toller contact layer strengthen the Iter068A denominator-skeleton microlocal classification when one attempts to multiply the separately transformed wedge distributions at a K4 common collision?

This is a test of the **separate contact-expanded product**, not of the source-defined joint spectral integral before boundary-value expansion.

## Frozen source input

Use the validated Iter043A one-wedge identity

`Theta_(sigma,eps)(x) = A theta(sigma x)e^{-eps|x|} + B delta(x) - sigma c2/2 delta'(x)`

with gamma-simple `j=1/2`, `rho=gamma/2`,

`c2 = 2/(rho^2+1/4)`.

For every finite real `gamma`, `c2>0`; hence every fixed branch has a nonzero `delta'` contact coefficient. The wavefront set of `delta'` contains both nonzero conormal orientations at `x=0`.

## Frozen graph and lanes

K4 vertices `0,1,2,3`, all six edges. Physical sigma classes are

`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

Frozen gamma values: `1/5`, `6/5`, `2`.

Matrix: `8 sigma classes x 3 gamma values = 24 lanes`.

## Frozen exact predicates

1. `P1_CONTACT_NONZERO`: `c2 != 0` and all six branch `delta'` coefficients are nonzero.
2. `P2_SYMMETRIC_CONORMAL`: each contact factor supplies both `+n_ab` and `-n_ab` nonzero conormal directions, independent of the branch coefficient sign.
3. `P3_K4_CYCLE_COLLISION`: using the fixed triangle `(0,1),(1,2),(0,2)`, choose allowed conormal orientations so their exact sum is zero: `n_01+n_12-n_02=0`.
4. `P4_BRANCH_SUM_CONTROL`: on each wedge the `delta'` coefficients of the two branches cancel exactly under the independent `+/-` branch sum.

## Frozen lane classification

If all predicates hold:

`K4_SEPARATE_CONTACT_PRODUCT_HORMANDER_OBSTRUCTED_JHALF`

Otherwise:

`ITER068B_INVALID_OR_INCONSISTENT`.

## Frozen aggregate interpretation

PASS requires all 24 lanes valid and obstructed in the above scoped sense. The aggregate must report whether the result is independent of causal sigma class and the frozen gamma grid.

## Scope locks

- This does **not** prove that the source-defined joint finite-spectral-`i epsilon` causal vertex is undefined.
- It only shows that expanding each wedge first into boundary-supported contact distributions and then multiplying them naively does not satisfy the ordinary Hörmander product criterion at a K4 cycle collision.
- Joint spectral integration, analytic boundary values, Epstein-Glaser/wonderful-model extensions, or other correlated prescriptions remain logically open.
- Exact branch-sum cancellation of the one-wedge `delta'` term is a control, not proof that the multi-wedge EPRL identity survives a correlated K5 boundary value.
- No physical sector selection, divergence theorem, K5/G3/F9/G8 promotion, arbitrary counterterm, or preferred order is authorized.
