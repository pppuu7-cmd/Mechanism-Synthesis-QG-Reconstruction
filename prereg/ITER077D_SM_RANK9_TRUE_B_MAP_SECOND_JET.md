# Iter077D-SM preregistration — rank-9 true B-map mixed second jet

**Date:** 2026-09-14

## Purpose

`Iter077A-SM` proves that the true ten-component causal-vertex `B`-map is generically rank 10 at the common group collision. `Iter077C-SM` isolates the first full-span rank-9 exceptional stratum and proves exact codimension-3 transversality in source-normal space.

This gate asks the next local nonlinear question:

> At the frozen rank-9 witness, does the source-defined second jet of the exact Eq. (32) `B`-map remove the three-dimensional linear group-kernel degeneracy once the source-normal tangent directions are included?

This gate is a local source-map normal-form test. It is **not** a Hörmander product theorem and it does not classify the full causal vertex as finite or divergent.

## Frozen inputs

- `sources/CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md`
- `sources/CAUSAL_SPINFOAM_VERTEX_2026_B_MAP_SECOND_JET_SUPPLEMENT.md`
- `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`
- `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`

Use the frozen K5 edge order

`01,02,03,04,12,13,14,23,24,34`,

the frozen rank-9 witness

`xxxxxyyyzz`,

and its exact self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

No witness reselection is allowed after execution.

## Frozen source prediction

For fixed wedge normal `n` and relative boost coordinate `d=x_a-x_b`, source Eq. (32) predicts the second jet

`B = n.d + (1/2)(|d|^2-(n.d)^2) + O(3)`.

For a first tangent variation `n -> n+eta`, `eta.n=0`, the mixed jet is

`B = n.d + eta.d + (1/2)(|d|^2-(n.d)^2) + O(3)`.

Define the contracted rank-deficient target direction

`Phi = sum_e lambda_e B_e`.

## Lane A — provenance and frozen-object lock

PASS iff:

1. both source supplements exist and contain the exact first- and second-jet formulas;
2. `Iter077A-SM` is PASS with generic rank-10 witness;
3. `Iter077C-SM` is PASS with frozen witness `xxxxxyyyzz`, left nullity 1 and codimension 3;
4. the frozen self-stress and edge order match exactly;
5. all microlocal/physical firewalls remain unpromoted.

## Lane B — exact Pauli-matrix second-jet identity

Using exact symbolic Pauli matrices, set

`A=(a.sigma)/2`, `C=(c.sigma)/2`.

Expand

`exp(-t C) exp(2 t A) exp(-t C)`

to order `t^2` by multiplying the exact truncated exponential polynomials.

PASS iff symbolically:

1. the coefficient of `t` is `(a-c).sigma`;
2. the coefficient of `t^2` is `(1/2)|a-c|^2 I_2`;
3. therefore the normalized spinor expectation has coefficients `n.(a-c)` and `(1/2)|a-c|^2`;
4. scalar logarithm expansion gives the frozen quadratic term `(1/2)(|d|^2-(n.d)^2)`;
5. differentiating the linear term with respect to a tangent normal variation yields the frozen mixed term `eta.d`.

## Lane C — frozen rank-9 quadratic normal form

Construct the exact `10 x 12` true source Jacobian for `xxxxxyyyzz`.

PASS iff all of the following hold exactly:

1. `rank(J)=9`;
2. `lambda^T J=0` and the left nullity is 1;
3. the following three group directions form a basis of `ker J`:
   - common y at nodes `1,2,3,4`;
   - z at node `1` only;
   - common z at nodes `2,3,4`;
4. the group-only Hessian of `Phi` on that kernel has rank `2`, with one positive, one negative and one zero direction;
5. for normal-tangent coordinates `(eta_01^y, eta_01^z, eta_02^z)`, the mixed block `L` against the three kernel directions has rank `3` and `|det L|=1`;
6. the full symmetric `6 x 6` Hessian `[[H_group,L],[L^T,0]]` has rank `6` and determinant `-1` in the frozen normalization;
7. an exact congruence reduces this Hessian to `[[0,L],[L^T,0]]`, proving inertia `(3 positive, 3 negative)` without numerical eigenvalue fitting.

## Lane D — scaling and scope firewall

PASS iff:

1. `Phi` has no linear term along the frozen group kernel because `lambda^T J=0`;
2. the frozen second jet scales homogeneously as `t^2` under simultaneous scaling of the selected group-kernel and normal-tangent coordinates;
3. the mixed rank-3 block is recorded as the nonlinear lifting mechanism for the three linear kernel directions;
4. all of these remain false/unproved:
   - `HORMANDER_PULLBACK_AT_EXCEPTIONAL_STRATUM`;
   - `CORRELATED_TOLLER_GROUP_BOUNDARY_VALUE`;
   - `PHYSICAL_SOURCE_TO_K4_PUSHFORWARD`;
   - `PHYSICAL_REDUCED_K4_NUMERATOR_COEFFICIENT`;
   - `EPSILON_MINUS1_COEFFICIENT`;
   - causal-vertex finiteness/divergence;
   - G3/F9/G8/K5 promotion.

## PASS classification

`ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED`

## FAIL classification

`ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_DEGENERACY_PERSISTS_OR_SOURCE_PREDICTION_FAILS_EXACT_SCOPED`

## Next admissible gate on PASS

Use the exact six-dimensional quadratic normal form together with the source-selected one-dimensional contact distribution to test the local microlocal pullback/scaling criterion at the rank-9 exceptional stratum. That later gate must distinguish:

- existence of the source-selected boundary value;
- ordinary Hörmander pullback/product admissibility;
- extension freedom;
- absolute integrability;
- regulator removal.

No one of these may be substituted for another.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.