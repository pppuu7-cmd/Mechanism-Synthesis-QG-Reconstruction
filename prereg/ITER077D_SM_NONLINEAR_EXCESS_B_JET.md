# Iter077D-SM preregistration — nonlinear excess `B` jet on the frozen rank-9 source stratum

**Date:** 2026-09-14  
**Status:** prospective / frozen before implementation

## Dependencies

- source formula: causal-vertex Eq. (32), frozen in `sources/ITER077D_SM_NONLINEAR_EXCESS_B_JET_DERIVATION.md`;
- source/derived input commit: `3ca5442410f9c592807e4db239902e3cdc3eafca`;
- authoritative `Iter077C-SM`: `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`;
- frozen rank-9 witness: `xxxxxyyyzz` in edge order `01,02,03,04,12,13,14,23,24,34`;
- frozen self-stress: `lambda=(1,-1,0,0,1,0,0,0,0,0)`.

No witness, stress vector, path basis, Taylor order or PASS criterion may be changed after implementation begins.

## Mathematical object

Define

`Phi(t;a,b,c)=B_01(t)-B_02(t)+B_12(t)`

with the exact source function

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`.

Use the exact right-kernel coordinates of the frozen rank-9 Jacobian:

`x_1=b e_y+a e_z`,

`x_2=x_3=x_4=b e_y+c e_z`,

`g_a(t)=exp[t (x_a.sigma)/2]`, `g_0=I`.

For stressed edges `01,02,12`, use the frozen axis spinor representative `z_x=(1,1)` with Bloch normal `e_x`.

## Lane A — source/provenance lock

Valid iff:

1. the exact source Eq. (32) object is used;
2. `Iter077C-SM` witness, right-kernel and self-stress are consumed unchanged;
3. no scalar incidence surrogate replaces the true relative group matrices;
4. no symmetry-only argument is used to set higher Taylor coefficients to zero;
5. all global claim locks remain active.

Otherwise BLOCKED.

## Lane B — source matrix expansion control

Using exact `2 x 2` Pauli matrices and truncated exponential series, independently verify for a generic single edge with Hermitian generators `X_a,X_b` that

`g_ab g_ab^dagger = I+t(X_a-X_b)+t^2 (X_a-X_b)^2/2+O(t^3)`.

For Pauli `X=x.sigma` and Bloch vector `n`, verify from the logarithm that

`B_ab(t)=t n.d + t^2 [|d|^2-(n.d)^2]/2+O(t^3)`, `d=x_a-x_b`.

Lane B is valid only if both identities are obtained algebraically, not fitted numerically.

## Lane C — frozen kernel excess jet

Compute `Phi(t;a,b,c)` symbolically from the exact `2 x 2` source matrix expression through order `t^4` without substituting the predicted coefficients into the calculation.

### Frozen PASS predictions

1. coefficient `t^1` is exactly zero;
2. coefficient `t^2` is exactly `a(a-c)`;
3. coefficient `t^3` is exactly zero;
4. coefficient `t^4` is exactly

   `-(a-c)(a^3-a^2 c+2 a c^2+2 b^2 c)/6`;

5. the quadratic Hessian in convention `Phi_2=(1/2)u^T H u`, `u=(a,b,c)`, is

   `H=[[2,0,-1],[0,0,0],[-1,0,0]]`;

6. exact `rank(H)=2`;
7. exact inertia/signature is one positive, one negative, one zero eigenvalue.

If all hold, Lane C scientific PASS classification is

`ITER077D_SM_RANK9_EXCESS_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_SCOPED`.

If the source-faithful calculation gives a different valid jet, the scientific result is FAIL relative to the frozen prediction and the actual coefficients must be preserved; do not repair the hypothesis.

## Lane D — flat-plane and quartic-lift controls

Test two qualitatively different zeros of the quadratic form.

### D1 exact diagonal plane

For `a=c`, verify directly from group equality `g_1=g_2` that

- `B_12=0` exactly;
- `B_01=B_02` exactly;
- therefore `Phi=0` identically, not merely through a finite Taylor order.

### D2 second isotropic branch

Set `a=0` while keeping symbolic `b,c`. The quadratic coefficient vanishes. Compute through `t^4` source-faithfully and test the frozen prediction

`Phi(t;0,b,c) = (b^2 c^2/3) t^4 + O(t^5)`.

Require the quartic coefficient to be generically nonzero and positive as a polynomial square coefficient for real nonzero `b,c`.

### D3 pure Hessian-kernel axis

Set `a=c=0`; verify it is contained in D1 and hence `Phi=0` exactly for arbitrary `b`.

Lane D PASS means the quadratic singularity has an exact flat diagonal plane, while the distinct quadratic-isotropic branch `a=0` is generically lifted first at quartic order.

## Aggregate PASS

Aggregate PASS requires A/B valid and C/D PASS. Frozen classification:

`ITER077D_SM_RANK9_EXCESS_CONSTRAINT_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_DIAGONAL_FLAT_PLANE_AND_QUARTIC_LIFTED_SECOND_ISOTROPIC_BRANCH_EXACT_SCOPED`

## Aggregate FAIL

If A/B are valid but any frozen C/D prediction fails under the true source calculation, preserve the actual symbolic coefficients and classify

`ITER077D_SM_FROZEN_NONLINEAR_EXCESS_JET_PREDICTION_FAILS_EXACT_SCOPED`.

Scientific FAIL must not make the workflow itself fail after a valid symbolic result is produced.

## Aggregate BLOCKED

If source/provenance or exact symbolic object definition fails:

`ITER077D_SM_NONLINEAR_EXCESS_B_JET_BLOCKED_OBJECT_DEFINITION`.

## Consequence boundary

Even aggregate PASS is not a distributional existence theorem. It determines a local nonlinear excess-constraint germ on one frozen exceptional source stratum. The next admissible step is a local scaling/pullback test for the actual contact distributions using this non-Morse normal form, including the exact flat plane and quartically lifted isotropic branch.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.