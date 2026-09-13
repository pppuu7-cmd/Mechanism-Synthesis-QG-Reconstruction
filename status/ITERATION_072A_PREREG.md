# Iteration 072A preregistration — K4 common-epsilon leading-collision Schwinger-cone theorem

Date frozen: 2026-09-13

## Scientific question

Iter071A is terminal `REVIEW`: fixed-budget x-space QMC cannot resolve the `epsilon -> 0+` common-epsilon limit. Iter072A therefore does **not** increase the same quadrature density. It freezes a new analytic object: the leading full-collision coefficient obtained from the exact blow-up `y = epsilon z` of the reduced K4 common-epsilon rational family.

For the six K4 edge linear forms `ell_e(z)` and frozen source causal signs `s_e`, define the leading collision kernel

`K_s(z) = product_e (ell_e(z) - i s_e)^(-1)`.

The source-family numerator and the three Iter071A Gaussian-polynomial Schwartz tests all have constant term 1 at the full collision, so their candidate leading full-collision scaling is `epsilon^(3-6) = epsilon^-3` times the same coefficient.

## Frozen Schwinger/Fourier route

For real `x` and `s = +/-1`, use the exact identity

`1/(x - i s) = i s integral_0^infinity exp(-t) exp(-i s t x) dt`.

After multiplying all six factors and Fourier-integrating over the three blow-up coordinates, the candidate leading coefficient is proportional to

`(product_e s_e) * integral_{t >= 0} exp(-sum_e t_e) delta(A_s t) dt`,

where `A_s` is the signed-normal map. The exponential is strictly positive. Therefore the coefficient is nonzero exactly when `ker(A_s)` has a full-dimensional intersection with the positive orthant, equivalently when there exists a strictly positive circulation `t_e > 0` on every edge. This equivalence is to be recomputed independently in this gate; Iter058 is a control, not an input classification.

## Frozen lanes

Eight independent physical factorized sigma lanes:

`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

Each lane must recompute all of the following in all four cycle bases `S0,S1,P0,P1`.

## Frozen predicates

P1. **Exact incidence/rank validity.** Every signed-normal map has exact rank 3 and all basis transformations preserve the kernel/cycle-space dimension.

P2. **Strict-positive-cone criterion.** Independently enumerate directed simple cycles and construct a strictly positive circulation iff one exists. Verify it exactly satisfies `A_s t = 0` and `t_e > 0`.

P3. **Independent tournament criterion.** Compute strong connectivity directly from the six oriented edges, without using P2. Require exact equivalence between strong connectivity and existence of a strictly positive circulation.

P4. **Full-dimensional cone criterion.** If a strict-positive point exists, require the positive circulation cone to have relative dimension 3 inside `ker(A_s)`; otherwise require empty relative interior. This freezes whether the Schwinger delta-cone measure is strictly positive or zero at full dimension.

P5. **Proper-stratum power separation.** Enumerate every nonempty proper subset of the six denominator hyperplanes and compute `degree = number_of_factors - rank(normals)`. Require every proper stratum to have degree strictly below the full-collision degree `6-3 = 3`. This prevents a proper collision stratum from producing another `epsilon^-3` term capable of cancelling the full-collision coefficient.

P6. **Source numerator/test leading term.** Symbolically verify that the Iter071A source numerator and each frozen test `G0,G1,G2` have product constant term exactly 1 at the full collision, so none can cancel the leading coefficient locally.

P7. **Basis covariance.** P1-P6 and the strong/non-strong classification must be identical across all four cycle bases.

P8. **Negative control.** A deliberately wrong edge-orientation/sign map (`s_e -> sigma_a` rather than source pair sign `sigma_a sigma_b`) must disagree with the source classification for at least one of the eight lanes. The negative control is diagnostic only and cannot define the source result.

## Frozen interpretation

If all exact predicates pass, classify:

`ITER072A_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_STRONG_TOURNAMENT_SCOPED`

Interpretation permitted only at the reduced K4 common-epsilon rational-family level:

- for source sigma classes with a strict positive circulation, the full-collision `epsilon^-3` coefficient is nonzero, so the corresponding reduced Schwartz action cannot have a finite `epsilon -> 0+` limit for the frozen tests with nonzero value at the collision;
- for classes without a strict positive circulation, only the `epsilon^-3` full-collision coefficient is shown to vanish; slower divergences or finite boundary values remain open;
- this may explain the variance blow-up seen in Iter071A but does not retroactively change Iter071A's frozen REVIEW.

If any mathematical equivalence/power-separation predicate fails, classify `ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL` and preserve the exact counterexample. Invalid symbolic/implementation execution is `ITER072A_INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL`, not a scientific result.

## Claim locks

This gate does **not** authorize:

- physical causal-sector selection;
- a theorem about the complete source causal vertex;
- a K5 amplitude or correlated extension;
- arbitrary regularization-path independence;
- absolute integrability or a source Eq.(5)/(6) distributional inheritance theorem;
- G3, F9, or G8 promotion;
- NEW_PHYSICS_FOUND or complete-QG claims.

No threshold tuning is permitted after production. The gate is exact/combinatorial and has no fit parameter.
