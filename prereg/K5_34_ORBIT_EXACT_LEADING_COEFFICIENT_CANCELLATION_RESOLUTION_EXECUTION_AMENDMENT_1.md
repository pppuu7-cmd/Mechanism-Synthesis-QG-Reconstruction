# K5 exact cancellation resolver — prospective execution amendment 1

Status: **FROZEN BEFORE ANY PHYSICAL PRODUCTION COEFFICIENTS**.

Scientific parent preregistration: `d6b0e805101c8590eafac71398cc2b1466691752`.
Implementation-detail freeze: `808492fe93369f27e7fcaee6a0f7af64583a35ae`.

This amendment changes only the execution mechanism used to materialize the already-frozen complete coefficient supports. Degree ceilings, weights, S5 action, physical objects, exact-zero rule, orbit/channel coverage and terminal classifier are unchanged.

## Reason fixed before outcome

Dense coefficient propagation through every five-pair Wick product carries substantial avoidable exact-rational convolution cost. Because the target objects have already-frozen finite degree ceilings, exact deterministic interpolation from a fixed number of exact rational evaluations is mathematically complete and does not perform an adaptive cancellation-depth search.

No physical corner coefficient or cancellation depth was inspected in making this execution choice.

## Primary route — frozen

For every one of the 32 proper orbit representatives and for each of the four frozen covariance lanes

- original `W1`;
- original `W2`;
- cyclically transported `W1` on the transported orbit;
- cyclically transported `W2` on the transported orbit,

evaluate the exact compressed all-32 rational algebra at the 32 prospectively frozen positive integer nodes

`t = 1,2,...,32`.

Arithmetic is exact `fractions.Fraction` only.

At each node use the original rational/cofactor path: exact authoritative 125-tree `Psi`, exact Laplacian cofactor inverse, exact order-four inverse/determinant-factor recurrence and exact compressed Wick contraction. Propagate the annihilator directional derivative by exact dual-number arithmetic and form the polynomial `B_v[N_c]` before division by `s1^4`.

Reconstruct monomial-basis coefficient vectors by exact rational interpolation over all 32 nodes. The complete reconstructed support is always length 32 before degree checks.

Frozen degree checks:

- `N_c`: coefficients `t^28...t^31` must be exactly zero; retain `t^0...t^27`;
- `B_v[N_c]`: retain the full `t^0...t^31` vector;
- `U_Z`: coefficients `t^6...t^31` must be exactly zero; retain `t^0...t^5`.

Failure of these exact degree checks is `INVALID_IMPLEMENTATION`; the support is never enlarged.

## Independent route — frozen

For **every** proper orbit, not only the preregistered minimum class representatives, independently reconstruct the original `W1` and `W2` coefficient objects using a denominator-cleared algebraic route at the distinct frozen nodes

`t = 33,34,...,64`.

The independent evaluator must not call the primary rational evaluator.

It uses

`C_0=Adj(L)`, `C_n=-Adj(L)Q C_(n-1)`

and the scaled determinant-factor recurrence from `det(I+x Adj(L)Q)^(-3/2)` so that the common `Psi^9` denominator is cancelled algebraically before the physical numerator is formed. Directional derivatives are propagated independently through this denominator-cleared recurrence.

Exact interpolation over nodes 33..64 must reproduce coefficient-by-coefficient the primary `W1` and `W2` vectors for `N_c`, `B_v[N_c]` and `U_Z` after the same frozen degree checks.

This all-orbit independent reconstruction is stronger than the parent minimum of one representative per orbit-size/collision-size class and provides direct support for any exact-zero claim.

## Parallel execution — frozen

The 32 proper orbits may be executed as independent GitHub Actions matrix jobs. Each job must output both physical channels, both asymmetric weights, both S5-transported covariance lanes, and both independent reconstruction lanes for its one fixed orbit.

A separate aggregate job must verify exactly 32 unique proper orbit IDs and exactly 64 unique channel-orbit components before classification.

## Covariance and certification — unchanged

S5 covariance is equality of the complete primary coefficient vectors between each original lane and its correctly transported cyclic lane. `W1` and `W2` are not required to have equal coefficients; they are required to give the same first nonzero order or the same complete-support exact-zero status for each target.

A target is exact-resolved only when:

1. primary complete-support degree checks pass for both `W1` and `W2`;
2. independent complete-support reconstructions at nodes 33..64 exactly reproduce the primary `W1` and `W2` coefficient vectors;
3. the two asymmetric witnesses agree on lowest nonzero order or exact-zero status;
4. both full coefficient objects pass frozen S5 cyclic covariance.

No post-outcome node, degree, weight, representative, route or threshold changes are permitted.
