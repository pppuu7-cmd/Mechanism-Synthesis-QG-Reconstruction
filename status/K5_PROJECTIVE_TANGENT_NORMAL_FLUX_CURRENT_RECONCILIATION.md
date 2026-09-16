# Recovery reconciliation — corrected K5 projective tangent normal-flux gate

Date: 2026-09-16

This note records validated terminal repository state newer than the `status/CURRENT.md` cut that preceded Researcher production run `35104985610`.

Researcher corrected tangent-flux production:

- prereg `bf6464e30893101a7bd6fd59b78b8b00dea14f61`;
- implementation `07d1392f771f7f98858fc348f41988fc931cc71f`;
- workflow/head `427c774edb4f1461965aed8ded44034fd9f5673e`;
- run `35104985610`, terminal success;
- job `104823746567`, terminal success;
- artifact `10449707101`, ZIP digest `sha256:92f6e8b37e79a34678e942042c0ae068c11538b966d4e5e75a6c402dd3080cf9`;
- stdout classification `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.

Independent AUTOMATION B review is controlling for scientific consumption:

- Critic prereg `195316d9bfc54e0049b8d536c11dc4cda59a8dba`;
- review `3335307be94fada4366f88565496f96b657e2c70`;
- provenance ledger `5948e147e3de44cd972703b913f3eecf633dbf98`;
- Critic handoff reconciliation `1ad46c650604667e1084b56607aa2382e280687c`;
- mandatory verdict `INVALID_IMPLEMENTATION`.

Reason: the Researcher executable does not perform the frozen direct `Omega_9` contraction/blow-up pullback, uses a tautological `jac_exp=k-1` check, and substitutes a label permutation for the required second genuine projective chart. Euler/radial-shift controls operate only on the algebraically defined tangent representative, and the classification is printed unconditionally after those weaker checks.

Authority consequence: corrected projective tangent normal-flux geometry remains `?`; the 34-orbit physical action-flux audit remains blocked from substantive corner classification. A prospectively frozen control-only implementation repair of the unchanged scientific contract is authorized. Upstream claim locks remain unchanged.
