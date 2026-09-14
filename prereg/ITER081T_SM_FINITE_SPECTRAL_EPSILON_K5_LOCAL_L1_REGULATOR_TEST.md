# Iter081T-SM prereg — finite one-wedge spectral epsilon as a K5 common-collision L1 regulator?

Status: **PROSPECTIVE CRITIC DIAGNOSTIC GATE — frozen before derivation/implementation**
Date: 2026-09-14

## Motivation
Authoritative Iter077K established that the published BCG source order takes `epsilon->0+` in each one-wedge spectral projector before inserting the ten already-defined Toller functions into the K5 group integral. Therefore retaining finite spectral epsilons through the group integration is **not** a published source prescription.

Nevertheless, after the right-SU(2) repair leaves a finite but nontrivial invariant normal-jet ambiguity, test the strongest natural regulator rescue: if one hypothetically retains the BCG one-wedge spectral projector at finite `epsilon>0`, does this soften the authoritative Iter077I common-collision singularity enough to make the all-`j=1/2` K5 integrand locally `L1` before epsilon removal?

A negative result would not be a regulator-independence theorem; it would show only that spectral epsilon does not act as an ordinary local UV/L1 regulator of this collision.

## Frozen source formulas
Use BCG arXiv:2604.24945 Eq. (17)/(20) and companion arXiv:2601.23162 Eq. (3):

`I_epsilon^(sigma)[d](rho,beta) = integral_R d rho_tilde/(2 pi i) [ sigma P_jl(rho_tilde;rho)/(rho_tilde-rho-i sigma epsilon)] d^(rho_tilde,k)(beta)`,

with `sigma=+1/-1`, `epsilon>0`.

Freeze the exact contour consequence before any K5 inference:

`I_epsilon^(sigma)[d] = P_jl(rho+i sigma epsilon;rho) t^(sigma,rho+i sigma epsilon,k)`

provided the same BCG pole cancellation/asymptotic contour closure applies at finite epsilon. The gate must independently verify this equality from the source contour argument rather than assume it.

## Frozen K5 object
Use exactly the authoritative Iter077I minimal sector and collision geometry:

- all ten wedges `j=l=k=1/2`;
- fixed real nonzero EPRL representation labels `rho_ab` (equal-rho control allowed, but theorem should permit finite real nonzero labels wedge by wedge);
- one of the 16 proper causal branch assignments already frozen in Iter077I;
- complete frozen 32-dimensional boundary-intertwiner basis;
- the exact Iter077I nondegenerate common-collision ray and source incidence;
- either one common epsilon or independent positive epsilons `epsilon_ab`, all sufficiently small and fixed while the collision radius `r->0+`.

The finite-epsilon object is a **diagnostic rearrangement**, not source-authorized amplitude, because published source ordering removes epsilon before the K5 integral.

## Exact subquestions
1. Derive the small-`beta` leading matrix of each finite-epsilon projected `j=1/2` wedge.
2. Test whether the boost power changes from `beta^-2`.
3. Test whether the leading matrix is a nonzero scalar multiple of the authoritative Iter077I leading matrix for every fixed sufficiently small epsilon.
4. Propagate the result through the actual K5 incidence and all 32 boundary contractions already proven nonzero by Iter077I.
5. Compute the transverse K5 radial power and local-L1 margin at fixed epsilon.

## Classification
- `FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED` iff every fixed sufficiently small epsilon retains nonzero total `r^-20` leading behavior and radial L1 exponent `-9` in all 32 frozen boundary components.
- `FINITE_SPECTRAL_EPSILON_SOFTENS_K5_COLLISION_EXACT_SCOPED` iff the exact finite-epsilon projector changes the local power/coefficient enough to restore local L1 in the frozen object.
- `ANALYTIC_CONTROL_INSUFFICIENT` if finite-epsilon contour equality or small-beta transport cannot be proved.

## Controls
- `epsilon->0+` must reproduce the Iter081E/Iter077I leading coefficients.
- For fixed small epsilon, all spectral prefactors used in the K5 leading product must be finite and nonzero; exceptional values must be stated, not silently crossed.
- The result may not rely on contact-distribution multiplication.
- A common epsilon and independent epsilon_ab variants must be distinguished.

## Claim ceiling
Even a negative-regulator result does NOT prove that no correlated group-variable regulator/analytic regularization can work, that the causal vertex fails distributionally, or that no selector exists. It only tests the finite BCG **spectral-parameter** epsilon rearrangement as an ordinary local L1 regulator. No regulator-independence, G3, F9/G8/K5, generic-spin physical vertex, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
