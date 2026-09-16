# Critic control-only repair 1 — uniform K5 annihilator action review

Date: 2026-09-16

Parent Critic preregistration: `prereg/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_INDEPENDENT_CRITIC.md`, commit `5f386aeda775e5513fc37ac5767248f0b561fb45`.

Historical Critic run `35049778265` is `INVALID_IMPLEMENTATION` only because the implementation mapped an exact mismatch of the Researcher witness into `INVALID_IMPLEMENTATION` instead of the prospectively frozen scientific branch `SCIENTIFIC_FAIL_CONFIRMED`. The run independently reconstructed all prerequisite structural facts, including `q_i=0`, `partial_i q_i=-15`, `div v=-150`, `v(Psi)=0`, the terminal numerator values, and a nonzero exact action; it then found the action differed from the Researcher witness by an exact factor of ten.

This repair is frozen before repaired implementation/production. It changes no scientific input, reviewed claim, authority corpus, expected Researcher witness, counterexample, or interpretation ceiling. It changes only the terminal classification logic:

- if all structural/provenance/control checks pass and the computed action equals the Researcher witness, return `CONFIRMED_SCOPED`;
- if all structural/provenance/control checks pass and the computed exact action contradicts the Researcher witness, return `SCIENTIFIC_FAIL_CONFIRMED`;
- retain `INVALID_IMPLEMENTATION` only for broken Critic implementation/controls.

The repaired workflow must accept either scientific terminal branch and must continue to forbid any constant-closure or integrated-period verdict.
