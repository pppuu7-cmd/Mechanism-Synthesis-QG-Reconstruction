# K5 projective-normal polynomial numerator degree/support — terminal result

Date: 2026-09-17

## Status

Researcher production status: `PASS_EXACT_SCOPED`.

Classification:

`K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_COMPLETE_SUPPORT_EXACT_SCOPED`.

This is a bounded-support/object-definition result only. It does not consume the still-unconfirmed full-source boundary S5 symbolic transport theorem and it does not execute the downstream physical leading-coefficient cancellation resolver.

## Frozen contract

Prospective preregistration:

`prereg/K5_PROJECTIVE_NORMAL_POLYNOMIAL_NUMERATOR_DEGREE_CEILING.md`, commit `96d7f3acebf37809c15c1ae104d7a98efe462fdc`.

The gate was frozen before implementation and before any exact `U_Z` polynomial output was inspected.

Its dependency is

`independently confirmed degree-four Kirchhoff annihilator + independently confirmed corrected projective-tangent geometry -> exact projective-normal numerator degree/support -> bounded-support prerequisite for K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`.

The gate is independent of the pending Critic reconstruction of the separate full-source boundary S5 symbolic theorem.

## Source authority

The exact degree-four annihilator coefficients are taken from

`results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`, Researcher run `35043883583`, independently confirmed by Critic result commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`.

The corrected projective-tangent geometry is the Researcher repair-2 result `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_REPAIR2_RESULT.md`, commit `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`, independently confirmed by repaired Critic commit `57109026cf5bc95262395a3f42e5f121aa9be3ae`.

The downstream frozen consumer is `prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`. Its contract explicitly required the projective-normal polynomial numerator degree ceiling to be derived and frozen before production.

Iter077I source ordering remains anchored to corrected run `34786586785`, alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; historical run `34786550378` remains non-authoritative failure. Historical Iter077E/F remain quarantined and the published one-wedge spectral `i epsilon` is unchanged.

## Exact object

For the confirmed logarithmic annihilator

`v_i(alpha)=alpha_i q_i(alpha)`

with homogeneous cubic `q_i`, define

`S=sum_i v_i`, `s1=sum_i alpha_i`,

and the corrected tangent representative

`u=v-(S/s1)E`.

For every labeled Schwinger edge subset `Z`, define

`A_Z=sum_(e in Z) alpha_e`,

`V_Z=sum_(e in Z) v_e=sum_(e in Z) alpha_e q_e`,

and

`U_Z=s1 V_Z-S A_Z`.

Then exactly

`u_Z=sum_(e in Z)u_e=U_Z/s1`.

The production reconstructs `U_Z` as an exact sparse rational polynomial for all `2^10=1024` labeled K5 edge subsets. Empty and full subsets are retained as controls; all `1022` proper labeled subsets are audited.

## Exact degree theorem

The production independently reconstructs the authoritative 33 fixed-edge cubic orbit coefficients and verifies:

- every `q_i` is a nonzero homogeneous polynomial of degree 3;
- every `v_i=alpha_i q_i` is homogeneous degree 4;
- `S=sum_i v_i` is homogeneous degree 4;
- `s1` and every `A_Z` are homogeneous degree 1.

Therefore each correctly formed nonzero

`U_Z=s1 V_Z-S A_Z`

is homogeneous degree 5. This was then verified mechanically on every proper labeled subset.

Consequently, after any frozen linear corner substitution in one blow-up parameter `t`, the complete possible coefficient support is exhausted by

`t^0,t^1,t^2,t^3,t^4,t^5`.

No `t^n` coefficient with `n>5` can occur in the projective-normal polynomial numerator.

## Full labeled-subset result

All `1022` proper labeled subsets have **nonzero** `U_Z` exactly.

Thus:

`proper_identically_zero_count = 0`.

No proper Schwinger face is annihilated identically by the projective normal numerator of the confirmed degree-four annihilator.

Across proper labeled subsets, exact sparse `U_Z` coefficient counts range from `315` to `740`; the observed exact counts are

`315, 500, 525, 622, 636, 646, 661, 688, 689, 700, 703, 710, 714, 722, 735, 740`.

This coefficient-count census is descriptive only; it is not used to infer a physical corner exponent.

## S5 subset census control

Independent labeled-subset enumeration gives exactly:

- 34 S5 orbits among all 1024 labeled edge subsets;
- 32 proper orbit representatives;
- empty and full sets as the two nonphysical controls;
- total orbit sizes summing exactly to 1024.

This orbit census is only a combinatorial coverage control. The scientific degree/support verdict is obtained on every labeled subset and does not consume the still-unconfirmed full-source boundary S5 transport theorem.

## Source/annihilator lock

The production reconstructs the exact 125 coefficient-one spanning-tree polynomial `Psi_K5` and verifies exactly

`v(Psi_K5)=0`.

The reconstructed `Psi_K5` polynomial SHA256 is

`7b1b6b293cf1467b762330cfe526a17a157ae525d311d497435b8fb91a54be18`.

The reconstructed `S=sum_i v_i` polynomial SHA256 is

`1da4ae4d8be30706e82d4492167edd9d6bb37ed560c7bb7cdea05d3247c992c3`.

A malformed control that increments one authoritative annihilator coefficient breaks exact `v(Psi_K5)=0` and is rejected.

## Projective/radial controls

For the frozen nonzero homogeneous cubic radial-shift fixture

`f(alpha)=sum_i alpha_i^3`,

production replaces

`v_i -> v_i+f alpha_i`.

The exact projective numerator `U_Z` is unchanged for **all 1024 subsets**, confirming radial-class invariance of the polynomial numerator.

By contrast:

- raw ambient `V_Z` fails this invariance on proper subsets;
- malformed `s1 V_Z-2 S A_Z` fails this invariance on proper subsets.

These controls distinguish the corrected projective object from the historical raw-ambient normal component.

## Authoritative production

Implementation commit:

`1586b293d819ff58cca917d6ee5190e2b7677dd7`.

Workflow/head:

`6217ec7b675a5f1a41fe4a400bd2e7b00481d81d`.

Terminal production:

- run `35215941730`, terminal success;
- job `105184321294`, terminal success;
- artifact `10494771790`, `k5-projective-normal-polynomial-degree-ceiling`;
- artifact ZIP digest `sha256:c13382c4c6cb32296e2c40517b94993bf89eb75cab54d3796911e60d2d245f33`;
- full production JSON SHA256 `661e3999a1e6b9c798cbc63fa5865df4b118b44fad634437f819beeae9536223`;
- executed script SHA256 `962f5482ae9be8f460fb821b34cff7a2f9fd134f478905ab0aaebb74627cde6d`.

All frozen positive and negative controls passed.

A durable compact machine authority is stored at

`results/raw/k5_projective_normal_polynomial_numerator_degree_ceiling_authoritative.json`.

The full 1024-row machine output remains in GitHub Actions artifact `10494771790` and is pinned by the production JSON SHA256 above.

## New scoped scientific fact

The corrected projective normal component of the independently confirmed degree-four annihilator has an exact universal polynomial numerator

`U_Z=s1 V_Z-S A_Z`

whose complete alpha-degree is five for every proper K5 Schwinger edge subset. No proper labeled subset has `U_Z` identically zero.

Therefore the projective-normal branch of the already-frozen exact cancellation resolver has a rigorously closed a priori one-parameter coefficient window `t^0,...,t^5`. The resolver no longer needs an unknown/adaptive degree ceiling for this target.

This does **not** determine which coefficient within `0,...,5` is the first nonzero coefficient at any frozen physical corner; that remains the job of the downstream exact-cancellation resolver after its separate transport dependency is independently confirmed.

## Interpretation ceiling

This result does not determine any degree-27 physical numerator `N_c` leading order, degree-31 action numerator `B_v[N_c]` leading order, or physical interior/flux/action exponent. It does not classify any corner as finite/logarithmic/divergent.

It does not consume or confirm the pending full-source boundary S5 symbolic transport theorem. It does not authorize substantive execution of the frozen cancellation resolver while that independent Critic reconstruction is pending.

It does not prove global projective Stokes/IBP, an invariant-dual K5 period, a full 217-dimensional order-eight tensor theorem, reduction of `dim_C F_8=377`, a physical finite-part selector, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
