# Boundary-S5 independent Critic — pre-execution classifier audit

Date: 2026-09-17
Status: **OUTCOME-BLIND CODE/CONTRACT AUDIT; NO SCIENTIFIC VERDICT**

## Frozen authority

Critic scientific contract remains `prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md`, commit `cf8576acb7237b751c26d5b5942aa60874bcd00e`.

Current independent reconstruction implementation is commit `64a4f4935d0238d67e2d60e0b202f81f1195330a`, file `scripts/critic_k5_full_source_boundary_s5_symbolic_independent_reconstruction.py`.

This audit was performed before consuming any substantive output from that implementation. No q18 partial values and no Boundary-S5 scientific result were inspected.

## Contract defect found

The frozen Critic contract distinguishes:

- `CONFIRMED_EXACT_SCOPED` when the complete coefficient-level transport theorem is reconstructed exactly;
- `REFUTED_EXACT_SCOPED` when a valid implementation produces an exact coefficient-level counterexample;
- `BLOCKED` for a named missing primitive;
- `INVALID_IMPLEMENTATION` when the executable does not implement the frozen contract or mandatory controls fail.

The current implementation reconstructs the required source/boundary and covariance ingredients, but its terminal classifier does not preserve this outcome distinction.

Specifically:

1. `polynomial_checks` contains substantive theorem checks, including exact C/T covariance-numerator transport and complete-matching orientation-factor checks.
2. `implementation_valid` requires **all** `polynomial_checks` to be true.
3. Therefore an exact failure of covariance transport or matching orientation transport forces `implementation_valid=False` and yields `INVALID_IMPLEMENTATION`, even if source/provenance/coverage/arithmetic and malformed controls are all valid.
4. `scientific_exact` is currently only
   `generator_results['C']['exact'] and generator_results['T']['exact']`,
   i.e. the source/boundary dictionary contragredient equality. It does not itself include the covariance-numerator and complete-Wick orientation conditions needed for the frozen full all-alpha theorem.

Thus the executable can confirm the theorem only because substantive covariance/orientation conditions are hidden inside `implementation_valid`, but it cannot correctly distinguish a genuine exact scientific refutation of those conditions from an implementation defect.

## Required prospective implementation-only repair

Before any output from this implementation is promoted to scientific authority, the Critic must prospectively freeze and apply a classifier-only/diagnostic repair that leaves the scientific question, source object, conventions, controls and interpretation ceiling unchanged.

The repaired classifier must separate:

### A. implementation/provenance validity

Examples: required files/source hashes, exact arithmetic path, complete 32-component/100000-term coverage, all-120 group construction machinery, 945-matching completeness, malformed-control sensitivity, no interpolation/fits/q18 contamination.

Failure here => `INVALID_IMPLEMENTATION` (or the already-frozen source/block classification where applicable).

### B. substantive frozen theorem conditions

At minimum the final scientific condition must include the conjunction required to establish the factorized coefficient-level theorem:

- C and T source/boundary contragredient dictionary identities;
- C and T formal covariance-numerator transport identities;
- complete-Wick orientation/source sign cancellation required by the frozen factorization;
- exact inverse/composition consistency necessary to extend generator identities to all 120 S5 elements.

If implementation/provenance validity passes but any required substantive identity fails, output `REFUTED_EXACT_SCOPED` with a machine-readable exact counterexample identifying generator/permutation, component or covariance pair/matching, and the unequal exact coefficients/polynomials.

If every substantive identity passes, output `CONFIRMED_EXACT_SCOPED`.

## Scope

This is not a change of hypothesis or a post-hoc scientific criterion. It is an outcome-neutral repair required so that the already-frozen PASS/REFUTED/INVALID distinctions are actually implemented. The Critic must not use any scientific output from the defective classifier to design the repair.

No Boundary-S5 theorem is independently confirmed by this audit. The 64-component resolver remains blocked until a terminal valid independent Critic scientific result exists.
