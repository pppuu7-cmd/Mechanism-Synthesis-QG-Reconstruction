# Prospective preregistration — independent Critic review of exact uniform-point K5 annihilator action

Date: 2026-09-16

## RESULT UNDER REVIEW

Researcher derivation `sources/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_DERIVATION.md`, commit `d867d215c0c1a9b1777add8eab56749145dbde1e`.

The reviewed scoped claim is only that, for the independently confirmed degree-four Kirchhoff annihilator and terminal full-all-32 invariant-dual numerator channels, the exact uniform-point action satisfies

`B_v[N_c](1,...,1)=-150 N_c(1,...,1)`

and is nonzero for both physical channels. No statement about constant-2x2 closure or integrated periods is part of this review.

The separately running production `35045552470` is not an input to the scientific values of this Critic gate. Partial/cancelled production values are forbidden.

## FROZEN AUTHORITY

1. confirmed annihilator summary `results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`;
2. independent annihilator Critic result `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC_RESULT.md`;
3. terminal numerator summary `results/raw/k5_invariant_dual_deg27_canonical_dag_production_summary.json`;
4. exact projective-gauge action derivation `sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`;
5. controlling Iter077 contact erratum and source-order locks.

## INDEPENDENT OBLIGATIONS

The Critic implementation must reconstruct, without importing the Researcher uniform-action assertions as target inputs:

C1. the ten K5 edge variables and all 220 degree-three monomials;
C2. the order-12 fixed-edge stabilizer and complete 33-orbit basis, with orbit sizes matching the terminal annihilator authority;
C3. the 33-coefficient annihilator representative from the terminal production summary;
C4. the S5-transported edge polynomials `q_i`;
C5. exact uniform values `q_i=0` for every edge;
C6. exact diagonal derivatives `partial_i q_i=-15` for every edge and hence `div v=-150`;
C7. independently construct the 125-term K5 spanning-tree polynomial and verify the emitted vector field annihilates it coefficientwise, `v(Psi_K5)=0`;
C8. read only the already-terminal uniform numerator values from the canonical-DAG production summary and compute the action from the exact formula, obtaining the two Researcher witness integers;
C9. verify the nonzero conclusion depends on the full invariant-dual numerator authority, not on representative boundary component `00000`;
C10. preserve the interpretation ceiling: no constant-closure verdict, Stokes theorem, integrated-period zero/nonzero theorem, full K5 tensor theorem, finite-part selector, regulator-independence theorem, G3/F9/G8 promotion or new-physics claim.

## COUNTEREXAMPLE / MALFORMED CONTROLS

The same independent path must at minimum establish:

1. changing one nonzero annihilator coefficient destroys `v(Psi)=0`;
2. a zero numerator fixture produces zero action, so nonzero classification is not hard-coded;
3. substituting a representative `00000` numerator is rejected as the wrong reviewed object;
4. replacing `div v=-150` by a different value changes the computed action and cannot still satisfy the exact Researcher witness values.

## TERMINAL VERDICTS

Use exactly one mandatory review verdict:

- `CONFIRMED_SCOPED` if C1-C10 and all controls pass;
- `SCIENTIFIC_FAIL_CONFIRMED` if a valid independent exact reconstruction contradicts the uniform-point theorem;
- `INVALID_IMPLEMENTATION` if the Critic implementation/controls are circular or incomplete;
- `INVALID_PROVENANCE` if required terminal parent authority or chronology is broken;
- `BLOCKED_OBJECT_DEFINITION` if the exact reviewed object cannot be reconstructed from repository authority.

No other scientific scope may be promoted by this Critic gate.
