# Iteration 052 — preregistration: canonical triple-residue antisymmetry / inclusion-exclusion gate

**Date:** 2026-09-12
**Prerequisite:** terminal Iter051 `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` with `K4_RR_CANCELLATION_DOMINATED_SUBSET`.

This file freezes Iter052 before implementation and before any Iter052 production output is viewed.

## Scientific question

Iter051 localized the sequential pairwise RR obstruction exactly to ordered upper-residue-sum mismatch and found 31/108 RR-zero lanes with different ordered residue geometry but exact residue-sum cancellation. Iter052 asks whether the three K4 cycle-residue operations obey a fixed higher-order inclusion-exclusion cancellation identity, rather than fitting any selector to pairwise RR labels.

## Frozen algebraic object

For one K4 tree let `R_i` denote exactly the same one-variable upper-half-plane residue component already used in Iter048–051, acting on cycle coordinate `y_i`, `i in {0,1,2}`. No contour, finite-part coefficient, pole classifier, source kernel, threshold or counterterm is changed.

For every permutation `pi=(pi1,pi2,pi3)` of `(0,1,2)`, compute the pure triple-residue ordered value

`T_pi = R_pi3 R_pi2 R_pi1 F`.

Define the **canonical full antisymmetrizer**

`A_RRR = sum_{pi in S3} sgn(pi) T_pi`.

The six coefficients are fixed uniquely by permutation parity: `+1` for even permutations and `-1` for odd permutations. No coefficient fitting, rescaling, class-dependent sign, threshold, or post-hoc selector is permitted.

This is the only primary Iter052 identity.

## Frozen source matrix

Reuse the exact nine Iter050/051 conditions, but one lane now contains all six triple orders, so pair labels are absent:

- `BASE`
- `G_LO`, `G_HI`
- `E_LO`, `E_HI`
- `S_ALT1`, `S_ALT2`
- `K_ALT1`, `K_ALT2`

Cross with the four frozen K4 spanning-tree/fundamental-cycle bases `S0,S1,P0,P1`.

Total: **36 source lanes**. Each lane also evaluates the identical `F=1` EPRL/no-contact control.

The numerical/rational parameter values and sign strings are exactly those frozen in Iter050/051. No denser parameter scan is part of Iter052.

## Mandatory exact validity gates

For every one of the six triple orders in every source/control lane:

1. each of the three one-variable residue steps must use the unchanged `R` component of the frozen `FP=R+A` decomposition;
2. at every residue step, `R + A` must exactly reproduce the frozen one-variable finite part for that current intermediate expression;
3. all three cycle coordinates must be consumed exactly once;
4. no unexpected real-axis/nonlinear pole may enter the unchanged pole classifier;
5. the ordinary `F=1` control must have `A_RRR = 0` exactly.

Any violation gives aggregate `ITER052_CONTROL_OR_RECONSTRUCTION_INVALID`.

## Frozen diagnostics

For each lane record:

- the six exact `T_pi` values;
- the even-permutation exact sum;
- the odd-permutation exact sum;
- exact `A_RRR`;
- whether all six `T_pi` are equal;
- number of distinct exact `T_pi` values;
- whether `A_RRR` is exactly zero.

The equality/distinct-count fields are descriptive only and cannot replace the primary classifier.

## Frozen aggregate classifier

1. `ITER052_CONTROL_OR_RECONSTRUCTION_INVALID` if any mandatory validity gate fails.
2. `K4_RRR_CANONICAL_ANTISYMMETRY_IDENTITY_EXACT` iff all 36 source lanes and all controls are valid, all controls have exact `A_RRR=0`, **all 36 source lanes have exact `A_RRR=0`**, and at least one source lane has more than one distinct ordered `T_pi` value (nontriviality guard).
3. `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO` iff all validity gates pass but at least one source lane has exact `A_RRR != 0`.

Report nonzero positions by condition/tree and the distribution of distinct-order counts. No post-hoc weakening is allowed.

## Interpretation lock

An exact antisymmetry identity would show a specific higher-order algebraic cancellation of the sequential residue operators on the frozen K4 matrix despite pairwise RR noncommutativity. It would **not** by itself define a simultaneous multivariate distributional extension; any such structural promotion requires independent held-out validation and then tree/cycle-basis/permutation/order-independence tests of an explicitly constructed multivariate prescription.

A nonzero `A_RRR` would rule out this particular canonical inclusion-exclusion identity and push the programme toward a source/analyticity-selected simultaneous multivariate K4 extension rather than coefficient fitting.

No Iter052 outcome authorizes K5, a preferred sequential order, arbitrary counterterm, physical causal-vertex finiteness/divergence, G3 PASS, physical F9, G8 novelty, or a new quantum-gravity theory.
