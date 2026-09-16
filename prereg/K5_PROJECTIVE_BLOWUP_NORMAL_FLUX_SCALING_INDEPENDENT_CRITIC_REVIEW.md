# Prospective preregistration — independent Critic review of K5 projective blow-up normal-flux scaling

Date: 2026-09-16
Status: FROZEN BEFORE CRITIC IMPLEMENTATION/PRODUCTION.

## RESULT UNDER REVIEW
Researcher geometry sub-gate `K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING`, prereg commit `06fc09a0355e6cc15889ac9f244ab03d4cb86569`, derivation commit `d756f0507c8b7816344fd75b1f8882bca071ede5`, implementation commit `a0b2ba1da34a7488af21b647a3213a4f39841de3`, production head `b94733dda1083db76eb3a8abd64f6a43c60e788b`, run `35087556685`, artifact `10441874454`.

## FROZEN CRITIC QUESTION
Does the Researcher normal-flux formula use the true projective vector-field class / tangent representative on the simplex, or does it incorrectly contract the restricted affine form with the raw ambient logarithmic vector field? In particular the Critic must distinguish the raw ambient field `v` from the simplex-tangent/projective representative `u=v-(S/s1)E`, `S=sum_i v_i`, already fixed by controlling source `sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`.

## FROZEN CHECKS
1. Reconstruct the standard projective Schwinger form `Omega_9=i_E(dalpha_1...dalpha_10)` and verify exactly that `i_E Omega_9=0`.
2. Verify projective contraction is invariant under `v -> v+fE`.
3. On the slice `s1=1`, independently derive the tangent representative `u_i=v_i-(S/s1)alpha_i` and the physical boundary-normal component `u(t)=v(t)-t S/s1` for `t=sum_{e in Z}alpha_e`.
4. Test the admissible polynomial-field counterexample `v=E` (`q_i=1`): true projective flux must vanish identically, whereas any formula proportional to raw `v(t)=t` would predict a nonzero normal flux.
5. Preserve the Researcher scalar blow-up Jacobian result `t^(k-1)` separately; failure of the flux contraction must not be misreported as failure of the scalar Jacobian.
6. Check Researcher implementation for hard-coded target facts and whether frozen checks 3,4,6,7 were actually executed rather than asserted.
7. Preserve the parent 34-orbit firewall: no physical corner classification or integrated Stokes result is authorized by this review.

## TERMINAL VERDICTS
Use exactly one user-authorized review verdict: `CONFIRMED`, `CONFIRMED_SCOPED`, `QUALIFIED`, `SCIENTIFIC_FAIL_CONFIRMED`, `BLOCKED_OBJECT_DEFINITION`, `INVALID_SOURCE_LOCK`, `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `REQUIRES_NEW_PREREGISTERED_GATE`.

If the Researcher universal normal-flux identity is contradicted by the exact projective-form calculation, prefer `SCIENTIFIC_FAIL_CONFIRMED` even if the scalar Jacobian sub-result survives. If only the executable fails while the mathematical result remains independently established, use `INVALID_IMPLEMENTATION` or `QUALIFIED` as appropriate.

## INTERPRETATION CEILING
No K5 physical period, Stokes theorem, corner valuation, finite-part selector, regulator-independence theorem, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim may follow from this Critic gate.
