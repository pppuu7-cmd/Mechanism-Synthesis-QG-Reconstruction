# Iter078M-RG preregistration — fixed-causal stabilizer restricted Jacobian injectivity

**Date:** 2026-09-14

## Motivation and prerequisite provenance

This gate is prospectively frozen after, and motivated by, the terminal retrospective Iter078J critic run `34790969496`, but **before** computing any stabilizer-restricted Jacobian ranks.

Established inputs only:

1. Iter078J-RG: for both the EPRL-edge-weight and unit-edge-weight all-`j=1/2` order-zero 1-to-5 control maps, the exact Jacobian at the compact tensor `L` has rank `31`, nullity `1`, with a verified primitive null vector; the null is lifted nonlinearly at order 2.
2. Iter078E critic boundary representation: exact `32 x 32` action of vertex-label permutations on the frozen five-node boundary basis and exact stabilizers `S_p x S_(5-p)`, `p=0,...,5`.
3. Retrospective Iter078J null-stabilizer audit: the already-known one-dimensional full-space null vectors are not invariant under any of the six fixed-causal stabilizers. This observation is **not itself** the scientific gate and is not promoted to restricted injectivity without the prospective exact calculation below.

## Frozen question

For each `p = 0,...,5` and for both measures (`eprl`, `unit`), let

`V_p = Fix(S_p x S_(5-p)) subset Q^32`

be the exact fixed-causal stabilizer-invariant boundary subspace. At the compact tensor `L`, does the exact Jacobian `J = D R_L` become injective when its **domain** is restricted to `V_p`?

Equivalently, is

`ker(J) intersect V_p = {0}`

for every `p` and both measures?

## Frozen construction

All arithmetic is exact over `Q`; no floating thresholds are allowed.

For each `p`:

1. Reconstruct the exact stabilizer generators using the independently implemented Iter078E boundary action.
2. Stack `(P_g - I)` for all stabilizer generators and compute an exact basis of `V_p` as the nullspace of the stacked constraints.
3. Independently verify every basis vector is fixed by every generator.
4. Reconstruct the compact tensor `L` and exact Iter078H/J Jacobians for `eprl` and `unit`.
5. Verify the previously established full-space rank is exactly `31` and the full-space nullity is exactly `1` for each measure.
6. Form the exact restricted Jacobian matrix `J|V_p` by multiplying `J` by the invariant-basis matrix.
7. Compute exact restricted rank and nullity.
8. Directly compute `ker(J) intersect V_p` through the stacked system `[J; P_g-I]` and require agreement with the restricted-rank result.
9. Symmetry consistency control: verify `L` is fixed by the stabilizer and verify exact Jacobian intertwining `J P_g = P_g J` for each frozen generator. If this fails, no injectivity interpretation is permitted and the gate is invalid/scoped-blocked.

## Frozen outputs

The implementation must emit, for every `p` and both measures:

- `dim(V_p)`;
- full rank/nullity;
- restricted rank/nullity;
- direct intersection dimension `dim(ker J intersect V_p)`;
- `L` invariance flag;
- exact Jacobian-equivariance flag;
- exact internal cross-check flags.

## Frozen classifications

Only the following scientific classifications are permitted after terminal artifacts are consumed:

1. `ITER078M_RG_FIXED_CAUSAL_STABILIZER_RESTRICTION_REMOVES_LINEARIZED_NULL_ALL_CLASSES_EXACT_CONTROL_SCOPED`
   - iff every `p` and both measures have restricted nullity `0`, direct intersection dimension `0`, and all symmetry/cross-check predicates pass.

2. `ITER078M_RG_FIXED_CAUSAL_STABILIZER_RESTRICTION_RETAINS_LINEARIZED_NULL_SOME_CLASS_EXACT_CONTROL_SCOPED`
   - iff all implementation/symmetry predicates pass but at least one frozen `(p,measure)` has restricted nullity > 0.

3. `ITER078M_RG_INVALID_OR_SYMMETRY_INTERTWINING_NOT_ESTABLISHED`
   - iff any exact construction, rank reproduction, invariance, equivariance, or cross-check predicate fails.

No criterion may be changed after production output is seen.

## Interpretation ceiling

Even the strongest PASS is only a **fixed all-`j=1/2`, pure order-zero, exact tensor-network control**. It would show that the previously observed rank-31 local singularity is absent after restriction to each fixed-causal stabilizer-invariant domain. It would **not** establish:

- a physical causal-Toller refinement map;
- a selected K5 distributional extension;
- generic-spin injectivity;
- an RG fixed point, beta function, regulator independence, G3, F9/G8 promotion, continuum limit, or complete quantum gravity.

The physical selector remains blocked until a source-faithful causal 1-to-5 amplitude/refinement map with extension transport is defined.
