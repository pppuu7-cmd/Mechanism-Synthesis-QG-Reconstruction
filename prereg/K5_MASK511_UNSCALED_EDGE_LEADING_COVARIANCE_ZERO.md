# K5 mask-511 unscaled-edge leading-covariance zero theorem

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION / RESULT.
Date: 2026-09-17
Role: outcome-blind analytic/structural companion to the already-running q18 production. It must not consume q18 shard values or replace the frozen q18 aggregate contract while that run is valid/non-terminal.

## Hypothesis

For mask `511`, the first nine canonical K5 edge parameters carry common filtration degree one and the tenth canonical edge parameter `alpha_9` (zero-based edge index 9) carries filtration degree zero. Let `r_*` be the reduced incidence row of that unique unscaled edge and write the reduced Laplacian as

`L = alpha_9 r_*^T r_* + terms of filtration >= 1`.

The exact mask-511 leading adjugate coefficient `A_2 = in_2(adj L)` obeys

`A_2 r_*^T = 0` and `r_* A_2 = 0`.

Consequently every minimum-filtration covariance numerator coefficient

`C_n^(min) = in_{2(n+1)}( r_i (adj L Q)^n adj L r_j^T )`

vanishes whenever `i=9` or `j=9`, for all source-series orders `n=0,...,4` used by the frozen order-four physical numerator.

Every perfect matching of the ten edge-source slots contains exactly one pair incident to edge slot 9. Therefore every five-pair Wick contribution at the naive minimum filtration degree is zero. The full physical numerator has no mask-511 degree-18 term, independently of the numerical values of the retained source/matching coefficients:

`N_{1,18} = N_{2,18} = 0`.

This is a structural theorem about the frozen all-j=1/2 numerator construction; it is not inferred from q18 partial output.

## Dependency / authority

- canonical degree-27 numerator DAG and exact K5 reduced Laplacian/adjugate authority already frozen in the repository;
- canonical ten-edge ordering from the corrected source object;
- mask `511` means edges `0,...,8` scaled and edge `9` unscaled;
- exact determinant minimum filtration degree `3` and adjugate minimum degree `2`, already independently encoded/audited in the mask-511 structural work;
- exact source order four / ten edge-source slots / Wick perfect matchings;
- no Boundary-S5 transport theorem is consumed;
- no q18 shard or aggregate value is consumed.

## Analytic mechanism

Use the polynomial identity

`adj(L) L = det(L) I`.

The determinant begins at filtration degree 3. The only degree-0 part of `L` is `alpha_9 r_*^T r_*`. Taking filtration degree 2 in the identity gives

`A_2 alpha_9 r_*^T r_* = 0`.

Since the polynomial ring is an integral domain and `alpha_9` and `r_*` are nonzero, this implies `A_2 r_*^T = 0`. Symmetry of the Laplacian/adjugate gives the left-kernel statement.

At minimum degree, the covariance source-series matrices are recursively

`B_0^(min)=A_2`,
`B_n^(min)=(-A_2 Q)^n A_2`,

so the outer `A_2` factors force every minimum covariance with edge slot 9 to vanish.

Every perfect matching of `{0,...,9}` pairs slot 9 exactly once; hence each product of five minimum covariances contains a zero factor. Determinant prefactors cannot lower filtration degree, so the total numerator degree-18 slice vanishes.

## Frozen exact implementation checks

A confirmatory checker must independently reconstruct from frozen source/code:

1. exact canonical edge ordering and verify edge index 9 is the unique unscaled edge under mask 511;
2. exact `A_2 = in_2(adj L)`;
3. exact right and left annihilation by `r_*`;
4. exact minimum covariance matrices for `n=0,...,4` and all pairs involving edge 9 are zero;
5. at least one minimum covariance not involving edge 9 is nonzero, excluding the trivial all-zero implementation;
6. all 945 perfect matchings of 10 slots are covered and each contains one pair incident to slot 9;
7. a malformed leading-adjugate perturbation in the `r_*` direction breaks the kernel condition, serving as a negative control;
8. no q18 result artifact, q18 shard payload, Boundary-S5 theorem, numerical sampling or interpolation is read.

## PASS

All frozen exact checks hold. Classification:

`K5_MASK511_UNSCALED_EDGE_FORCES_Q18_ZERO_EXACT_SCOPED`.

Scientific conclusion is limited to exact structural vanishing of the mask-511 numerator degree-18 slice for both frozen physical invariant-dual channels in the all-j=1/2 order-four construction. Together with already-terminal independent authorities, it may later support the same mask-511 structural-order conclusion, but it does not rewrite or pre-empt the currently running q18 production authority.

## FAIL

Any exact kernel/covariance/matching implication above is false with source/code locks intact. Classification:

`K5_MASK511_UNSCALED_EDGE_Q18_ZERO_THEOREM_REFUTED_EXACT_SCOPED`.

This refutes this analytic mechanism only; it does not by itself decide the running q18 polynomial aggregate.

## INVALID

Wrong source/code identity, wrong edge ordering/mask, incomplete matching census, missing negative control, q18-partial contamination, or non-exact arithmetic => `INVALID_IMPLEMENTATION`.

## Interpretation ceiling

No result here establishes another mask/orbit, Boundary-S5 transport, full K5 corner integrability, boundary-flux cancellation, global Stokes/IBP, invariant-dual K5 periods, a physical finite-part selector, regulator independence, predictive local K5 amplitude, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
