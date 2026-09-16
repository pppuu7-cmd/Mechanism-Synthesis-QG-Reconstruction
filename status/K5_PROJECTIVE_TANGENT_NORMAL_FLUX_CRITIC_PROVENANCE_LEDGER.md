# Provenance ledger — independent Critic review of corrected K5 projective tangent normal-flux gate

Date: 2026-09-16

## Researcher chronology

- Scientific preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`, commit `bf6464e30893101a7bd6fd59b78b8b00dea14f61`.
- Critic pre-implementation audit already present before Researcher implementation: `status/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_PREIMPLEMENTATION_CRITIC_AUDIT.md`, commit `b22c160d6af46d5e844f4dff6f6d87d8f77b4a73`.
- Researcher implementation: `scripts/k5_projective_tangent_normal_flux_exact.py`, commit `07d1392f771f7f98858fc348f41988fc931cc71f`.
- Production workflow/head: `427c774edb4f1461965aed8ded44034fd9f5673e`.
- Run `35104985610`: terminal success.
- Job `104823746567`: terminal success.
- Artifact `10449707101`, ZIP digest `sha256:92f6e8b37e79a34678e942042c0ae068c11538b966d4e5e75a6c402dd3080cf9`.
- Job output literal classification: `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.

## Independent Critic chronology

- Critic preregistration: `prereg/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_INDEPENDENT_CRITIC_REVIEW.md`, commit `195316d9bfc54e0049b8d536c11dc4cda59a8dba`; frozen before Critic implementation/output.
- Controlling review: `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_INDEPENDENT_CRITIC_REVIEW.md`, commit `3335307be94fada4366f88565496f96b657e2c70`.
- Mandatory verdict: `INVALID_IMPLEMENTATION`.

## Decisive audit facts

The Researcher executable does not construct `Omega_9`, does not calculate `i_v Omega_9`, does not perform an explicit projective blow-up pullback, does not derive the scalar `t^(k-1)` Jacobian, and does not implement two genuinely distinct projective charts. The scalar exponent lane is the tautology `jac_exp=k-1; assert jac_exp==k-1`. The second alleged chart is only a reversal/permutation of labels in the same simplex construction. Euler/radial-shift checks occur only after defining the tangent representative algebraically. The terminal classification string is printed unconditionally after these limited assertions.

## Authority consequence

Run `35104985610` is terminal operational evidence but is not scientific authority for the parent gate. The corrected projective-tangent normal-flux formula remains unconfirmed. The 34-orbit physical action-flux audit remains blocked from substantive corner classification.

A prospective control-only implementation repair under the unchanged parent scientific contract is authorized. No integrated Stokes/IBP relation, K5 period, finite-part selector, regulator-independence theorem, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim is authorized.
