# Prospective preregistration — K5 projective-normal polynomial numerator degree/support

Date: 2026-09-17
Role: AUTOMATION A — Researcher / Constructor

This gate is frozen before implementation and before inspecting any exact `U_Z` polynomial output.

## HYPOTHESIS

For the independently confirmed degree-four S5-equivariant logarithmic annihilator

`v_i(alpha)=alpha_i q_i(alpha)`

with each `q_i` homogeneous cubic, and for the independently confirmed projective-tangent representative

`u = v - (S/s1) E`,

where `S=sum_i v_i`, `s1=sum_i alpha_i`, `E=sum_i alpha_i partial_i`, the normal component for any Schwinger edge subset `Z`

`u_Z = sum_(e in Z) u_e`

has the exact polynomial numerator

`U_Z = s1 V_Z - S A_Z`,

with `V_Z=sum_(e in Z) v_e` and `A_Z=sum_(e in Z) alpha_e`, so that

`u_Z = U_Z/s1`.

The complete a priori polynomial degree ceiling is exactly five: every nonzero `U_Z` is homogeneous degree five. Therefore under any linear corner substitution in one blow-up parameter `t`, complete exact coefficient support is exhausted by powers `t^0,...,t^5`; no coefficient above order five can occur.

The gate will additionally determine, without post-hoc selection, whether any proper labeled K5 edge subset has `U_Z` identically zero for the confirmed annihilator.

## exact OBJECT

The object is the exact family of polynomial dictionaries `U_Z(alpha)` for all `2^10=1024` labeled subsets of the ten canonical K5 edges, with empty/full sets retained as nonphysical controls and all 1022 proper labeled subsets audited. S5 orbit representatives and orbit sizes are computed exactly from the canonical K5 vertex action only for census compression; the verdict does not rely on the unconfirmed full-source boundary S5 transport theorem.

This gate does **not** evaluate the physical degree-27 numerator `N_c`, the degree-31 action numerator `B_v[N_c]`, any boundary-state contraction coefficient, or any physical corner exponent.

## DEPENDENCY

`independently confirmed degree-four Kirchhoff annihilator + independently confirmed corrected projective-tangent geometry -> exact projective-normal numerator degree/support -> bounded-support prerequisite for K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`.

This dependency is independent of the still-pending Critic reconstruction of the full-source boundary S5 symbolic transport theorem.

## SOURCE AUTHORITY

1. Canonical K5 edge ordering and source-order provenance: corrected Iter077I authority, run `34786586785`, alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; historical run `34786550378` remains non-authoritative failure.
2. Exact degree-four annihilator authority: `results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`, Researcher run `35043883583`, classification `K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED`, independently confirmed by Critic result commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`.
3. Corrected projective-tangent geometry: Researcher repair-2 result `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_REPAIR2_RESULT.md`, commit `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`, independently confirmed by repaired Critic commit `57109026cf5bc95262395a3f42e5f121aa9be3ae`.
4. Downstream frozen consumer: `prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`, whose frozen bounded representation explicitly requires the projective-normal polynomial numerator degree ceiling to be derived before production.

Historical source-lock-invalid Iter077E/F remain quarantined. Published one-wedge spectral `i epsilon` is unchanged and is not modified by this algebraic gate.

## FROZEN INPUTS

- ten canonical K5 edges in the authoritative ordering;
- all 120 K5 vertex permutations only for labeled-subset orbit census;
- the exact 33 emitted annihilator coefficients from the terminal degree-four annihilator summary;
- the exact fixed-edge cubic-orbit construction already used by the terminal annihilator/action authority;
- exact rational/integer sparse polynomial dictionaries only;
- all 1024 labeled subsets, with empty/full sets as controls and every 1022 proper subset audited;
- exact formulas `A_Z=sum_Z alpha_e`, `V_Z=sum_Z alpha_e q_e`, `U_Z=s1 V_Z-S A_Z`;
- no numerical Schwinger weights, no finite witnesses, no interpolation, no floating arithmetic, no modular zero test, no fitted phase/matrix/character, no physical boundary-state selection.

## POSITIVE CONTROLS

P1. Reconstruct exactly 10 canonical K5 edges and the 33 fixed-edge cubic orbit basis used by the authoritative annihilator coefficients.

P2. Reconstructed `q_i` are homogeneous degree three for every edge and are not all zero.

P3. `v_i=alpha_i q_i` are homogeneous degree four for every edge.

P4. Reconstruct `Psi_K5` from the authoritative 125 coefficient-one spanning-tree polynomial and verify exact `v(Psi_K5)=0` as a source/annihilator lock.

P5. `S=sum_i v_i` is homogeneous degree four and `s1=sum_i alpha_i` is homogeneous degree one.

P6. Empty set gives `U_empty=0` exactly; full ten-edge set gives `U_full=0` exactly.

P7. For every proper labeled subset, every nonzero monomial of `U_Z` has total alpha degree five.

P8. The complete degree support of every proper `U_Z` is therefore contained in degree five and any linear one-parameter substitution can contain no `t^n` with `n>5`.

P9. S5 orbit census of all 1024 labeled edge subsets gives exactly 34 orbits, with exactly 32 proper orbit representatives and total orbit sizes summing to 1024.

P10. Radial-class invariance is verified algebraically on the polynomial numerator: for a frozen nonzero homogeneous cubic test polynomial `f(alpha)`, replacing `v_i` by `v_i+f alpha_i` leaves every `U_Z` unchanged exactly.

## NEGATIVE CONTROLS

N1. Raw ambient normal numerator `V_Z` must fail the frozen radial-shift invariance test on at least one proper subset.

N2. A malformed projective subtraction `U_Z^(bad)=s1 V_Z-2 S A_Z` must fail radial-shift invariance on at least one proper subset.

N3. Replacing one emitted annihilator coefficient by `c+1` must break exact `v(Psi_K5)=0`; this malformed annihilator must be rejected before any degree/support verdict.

N4. Any implementation that samples numerical alpha values or uses floating/modular equality for polynomial zero is invalid.

## PASS

Return `K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_COMPLETE_SUPPORT_EXACT_SCOPED` if all controls pass, all proper labeled `U_Z` are nonzero homogeneous degree-five polynomials, and the exact uniform ceiling `t^0,...,t^5` is certified.

Return `K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_CEILING_WITH_IDENTICALLY_ZERO_PROPER_FACES_EXACT_SCOPED` if all controls pass and one or more proper labeled subsets have `U_Z` identically zero; the exact zero masks/orbits must be emitted. The uniform complete coefficient ceiling for nonzero `U_Z` remains five.

## FAIL

Return `SCIENTIFIC_FAIL_PROJECTIVE_NORMAL_NUMERATOR_STRUCTURE` only if the authoritative reconstructed object itself violates the frozen projective formula/homogeneity assumptions: e.g. an authoritative `q_i` is not homogeneous cubic, exact `v(Psi_K5)` is nonzero, or a correctly formed nonzero `U_Z` contains alpha degree other than five. Such a failure is an obstruction to the bounded-support consumer and must not be repaired post hoc.

## BLOCKED

Return `BLOCKED_OBJECT_DEFINITION` if the exact annihilator coefficients/orbit basis, canonical edge map, or corrected tangent formula cannot be reconstructed from repository authority. Do not substitute a scalar surrogate.

## INVALID

Return `INVALID_IMPLEMENTATION` for code/provenance/control failures, including numerical sampling, incomplete labeled-subset coverage, or malformed-control failure.

## INTERPRETATION CEILING

This gate establishes only the exact polynomial numerator and its complete a priori degree/support bound for the projective-normal component of the already-confirmed annihilator geometry. It does not determine the first nonzero `t` coefficient at any physical corner, does not consume or confirm the pending full-source boundary S5 symbolic theorem, does not classify a physical corner as finite/logarithmic/divergent, and does not prove global Stokes/IBP, an invariant-dual K5 period, a full order-eight tensor result, reduction of `dim_C F_8=377`, a physical finite-part selector, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
