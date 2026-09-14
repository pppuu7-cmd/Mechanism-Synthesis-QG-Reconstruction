# Iter081E-SM — independent Researcher reproduction of actual Toller Han-bound counterexamples

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective chain
- prereg: `0f5414c9471a382527ca06c7f29ef2da6b8f8c1d`
- implementation: `8ceb7cc99925bb1d2a262b304ce29731f438ffdb`
- production workflow/head: `5743b4e0d6f5ce247ebe207b0ad48b0f17f3f664`
- run: `34877725730`
- job: `104088973504`
- artifact: `10361621460`
- artifact digest: `sha256:f2a4c52535799fad2aa7ad94b7bb2eeedde1933dde62cb66281dcff7493b4a82`

All workflow steps completed successfully; the aggregate artifact was downloaded and consumed before classification.

## Frozen classification
`ITER081E_SM_ACTUAL_TOLLER_ONE_WEDGE_AND_NATURAL_TWO_WEDGE_HAN_BOUNDS_COUNTEREXAMPLES_REPRODUCED_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Subgate A — actual one-wedge projected contraction
From BCG Eq. (46), with `j=k=1/2`, branch `+`, `m=+1/2`, `rho>0`, and `g_beta=exp(-i beta K_z)`, `beta>0`, the implementation independently verifies `b=c` and uses `2F1(a,b;b,z)=(1-z)^(-a)` only after exact parameter matching.

The exact result is

`t_+(beta) = -2 exp[-(2-i rho) beta] / [(rho^2+1/4)(1-exp(-2 beta))^2]`,

hence

`|t_+(beta)| = 1 / [2 (rho^2+1/4) sinh^2(beta)]`.

Therefore

`lim_{beta->0+} |t_+(beta)| = +infinity`,

so the actual selected Toller branch violates the Han-type projected contraction `||P_j T^+(g) P_j||<=1` on the frozen path for sufficiently small admissible positive `beta`.

Subgate classification: **`A_COUNTEREXAMPLE`**.

## Subgate B — natural two-wedge selected-branch face
The implementation independently derives both magnetic components from Eq. (46). For `m=-1/2` it verifies `b=c+1` and derives

`2F1(1,c+1;c,z) = 1/(1-z) + z/[c(1-z)^2]`

from the hypergeometric series ratio `(c+1)_n/(c)_n=(c+n)/c`.

The exact leading coefficients are

`lim beta^2 t_{m=+1/2}^+ = -1/[2(rho^2+1/4)]`,

`lim beta^2 t_{m=-1/2}^+ = +1/[2(rho^2+1/4)]`.

For the preregistered natural two-wedge branch term

`tau_{++,2}(beta)=2[(t_{m=+1/2}^+)^2+(t_{m=-1/2}^+)^2]`,

squaring removes the opposite-sign leading terms rather than cancelling them, and the exact symbolic limit is

`lim_{beta->0+} beta^4 tau_{++,2}(beta) = 1/(rho^2+1/4)^2 > 0`.

Thus `|tau_{++,2}(beta)| -> infinity`, so for sufficiently small `beta>0` it exceeds Han's standard `d_j^2=4` face bound.

Subgate classification: **`B_FACE_BOUND_COUNTEREXAMPLE`**.

## Controls
Exact symbolic regression passed for `rho=1/2, 1, 2`, giving the expected limits `4`, `16/25`, and `16/289`. A bounded surrogate `exp(-beta)` correctly fails both positive counterexample predicates: one-wedge limit `1`, and `beta^4` times the surrogate two-wedge face tends to `0`.

## Scientific meaning
This independently upgrades the previous Critic controls into the Researcher chain. The unchanged Han projected-unitary contraction and the unchanged Han `d_j^2` face bound cannot be transplanted to these frozen actual selected-Toller-branch objects.

This is stronger than Iter081B's source-inheritance blocker because it uses the actual BCG gamma-simple formula, not an abstract additive toy decomposition.

## Claim ceiling
The result does **not** prove that every causal face functional is unbounded or divergent. It does not rule out branch sums, subtractions, renormalized face functionals, alternative causal stack constructions, or new source-authorized transport theorems. It does not define the joint-K5 extension selector, causal E3/E4/E6 composition, regulator independence, G3, F9/G8, or a complete QG model.

No `NEW_PHYSICS_FOUND` claim is made.