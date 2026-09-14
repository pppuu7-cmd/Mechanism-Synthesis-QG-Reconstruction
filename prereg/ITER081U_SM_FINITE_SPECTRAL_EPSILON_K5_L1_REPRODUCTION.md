# Iter081U-SM prereg — independent reproduction of finite BCG spectral-epsilon K5 L1 diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE ITER081U IMPLEMENTATION/PRODUCTION**
Date: 2026-09-14

## Provenance motivation
A prior Critic diagnostic using the label `Iter081T` collided with an earlier Researcher-A reservation of the same iteration name and is `INVALID_PROVENANCE` as an Iter081T object by `status/ITER081T_DUPLICATE_LABEL_PROVENANCE_ERRATUM.md`.

This successor independently reproduces the scientific question under a fresh name. Historical duplicate Iter081T outputs may be treated only as adversarial hypotheses/controls and must not be imported as pass values.

## Source scope
Use Bianchi--Chen--Gamonal `arXiv:2604.24945v1` one-wedge spectral projector and Toller formula, plus the source-order finding already frozen in authoritative Iter077K: published ordering removes the one-wedge spectral epsilon before K5 group integration.

Therefore keeping `epsilon>0` through K5 is explicitly a **diagnostic rearrangement**, not the published causal-vertex definition.

## Frozen formula object
For branch `sigma=+1/-1`, representation label `rho` and finite positive epsilon, derive from the BCG contour proof the pre-limit residue object

`I_epsilon^sigma[d](rho,beta) = P_jl(rho+i sigma epsilon;rho) t^(sigma,rho+i sigma epsilon,k)(beta)`

within the same analyticity/pole-cancellation domain used in the source contour argument.

Specialize only after this source step to

- `j=l=k=1/2`;
- real finite `rho!=0`;
- `beta->0+`;
- fixed positive epsilon small enough that no exceptional singular parameter is crossed.

Mechanically derive `P_(1/2,1/2)(R;rho)` from the frozen product definition rather than hard-coding the simplified identity.

## Frozen K5 transport
If the exact one-wedge leading matrix is established, transport it to exactly the authoritative Iter077I K5 object:

- ten all-`j=1/2` wedges;
- actual K5 incidence;
- one of the already validated fixed causal branch assignments;
- complete 32-component frozen boundary-intertwiner basis;
- authoritative nondegenerate common-collision ray;
- transverse dimension `d=12`.

Test both:
1. common fixed positive epsilon on all wedges;
2. independent fixed positive `epsilon_ab` wedge by wedge.

## Frozen classifications
- `ITER081U_SM_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED` iff the exact finite-epsilon projected wedge leading matrix is epsilon-independent and equal to the Iter077I leading matrix, implying all 32 contractions retain `q=-20`, radial absolute exponent `-9` and fail local L1.
- `ITER081U_SM_FINITE_SPECTRAL_EPSILON_SOFTENS_K5_COLLISION_EXACT_SCOPED` iff exact source-formula transport changes the power/coefficient sufficiently to restore local L1.
- `ITER081U_SM_ANALYTIC_CONTROL_INSUFFICIENT` if the contour-residue or small-beta transport cannot be established.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` for chronology/source/control failure.

## Controls
1. Derive the spectral polynomial from its finite product at `j=l=1/2`.
2. Derive the shifted one-wedge Toller leading coefficients independently from the BCG gamma-simple formula/algebraic coefficient, not from duplicate Iter081T result files.
3. Verify the epsilon->0 limit reproduces authoritative Iter077I leading matrices.
4. Keep common and independent epsilons logically separate.
5. Use no contact-distribution multiplication.
6. Do not infer regulator independence or distributional nonexistence.

## Claim ceiling
This tests only finite BCG **spectral-parameter** epsilon as an ordinary local L1 regulator when retained in a non-source diagnostic ordering. It does not rule out correlated group-variable analytic continuation, Epstein-Glaser/Hadamard extension, subtraction, dimensional/analytic regularization or a future joint-K5 boundary-value law. No regulator-independence, generic-spin full-boundary theorem, G3/F9/G8/K5, `NEW_PHYSICS_FOUND` or complete-QG claim follows.
