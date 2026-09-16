# Prospective preregistration — independent Critic review of corrected K5 projective tangent normal-flux gate

Date: 2026-09-16
Status: FROZEN BEFORE CRITIC IMPLEMENTATION/OUTPUT.

## RESULT UNDER REVIEW
Researcher production run `35104985610`, head `427c774edb4f1461965aed8ded44034fd9f5673e`, claims `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED` under parent prereg `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`.

## FROZEN ACCEPTANCE CRITERIA
The Critic must not trust the Researcher classification string. It must independently check:

1. chronology/provenance and terminal Actions state;
2. direct use of the projective form `Omega_9=i_E(dalpha_1 wedge ... wedge dalpha_10)` rather than only algebraic tangency identities;
3. direct blow-up pullback/contraction establishing the claimed normal-flux factor for proper nonempty `Z`;
4. that the scalar Jacobian exponent `k-1` is derived mechanically, not assigned as `jac_exp=k-1`;
5. that at least two genuinely different projective/simplex chart choices are implemented; a relabeling/permutation of the same chart is not sufficient;
6. Euler control `v=E` gives zero projective flux by actual contraction/horizontality;
7. radial-shift invariance `v -> v+fE` is checked on the contracted projective form/leading coefficient, not only after replacing `v` by the canonical tangent representative by definition;
8. exceptional angular strata/vanishing leading normal component are not silently promoted to generic valuation statements;
9. empty/full edge sets remain controls, not physical projective corners;
10. no physical corner classification, Stokes theorem, integrated K5 period, regulator-independence or downstream promotion is inferred.

## COUNTEREXAMPLE-FIRST TARGETS
Attempt to invalidate the implementation using: hard-coded acceptance booleans/classification; tautological exponent checks; one-chart relabeling presented as chart independence; a field whose tangent representative vanishes at the sampled point; exceptional angular points; radial fields; and malformed blow-up coordinates where direct pullback would expose a missing factor/sign/order.

## TERMINAL VERDICTS
Use exactly one Automation-B verdict from the repository taxonomy: `CONFIRMED`, `CONFIRMED_SCOPED`, `QUALIFIED`, `SCIENTIFIC_FAIL_CONFIRMED`, `BLOCKED_OBJECT_DEFINITION`, `INVALID_SOURCE_LOCK`, `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, `REQUIRES_NEW_PREREGISTERED_GATE`.

Green CI alone is not scientific confirmation. If the executable does not test the prospectively frozen mathematical obligations, return `INVALID_IMPLEMENTATION` even if the underlying corrected formula is plausible or true.

## INTERPRETATION CEILING
This review concerns only the corrected projective normal-flux geometry sub-gate. It cannot classify the 34 Schwinger corner orbits, establish global Stokes/IBP, determine either invariant-dual K5 period, select a finite part, promote F9/G3/G8, claim regulator independence, `NEW_PHYSICS_FOUND`, or complete QG.
