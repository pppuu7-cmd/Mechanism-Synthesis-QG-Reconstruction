# Iter080J-SM result — wavefront/conormal admissibility alone does not select the Iter077Q extension

Date: 2026-09-14

## Provenance

Prospective scientific preregistration was committed **before implementation**:

- prereg: `prereg/ITER080J_SM_MICROLOCAL_WF_ONLY_SELECTOR_MOTIVATION_AND_POWER.md`, commit `bffd6cf275d930203ff272cba3bbae8916fdc51b`;
- initial implementation: `distributional/iter080j_sm_microlocal_wf_only_selector.py`, commit `e11c1f8ebac7354ac9d5588f187a045d405425a2`;
- workflow / initial production head: `.github/workflows/iter080j_sm_microlocal_wf_only_selector.yml`, commit `521faa0c45d9030a18171a2ecaf218cba15cf8f7`.

Two historical runs are preserved as implementation-invalid controls, not scientific failures:

1. run `34859269730`: Lane B searched for Unicode `Hörmander` while authoritative Iter029 writes ASCII `Hormander`; classification `INVALID_IMPLEMENTATION_LEXICAL_CONTROL`. Control-only repair preregistered at commit `0dc17ae388f763e7c020e3e8add7c79d40fdbb2c` before repair commit `a9a34e05562023a7697e15a45c298f9681a53527`.
2. run `34859501380`: Lane B then exposed a second textual-control defect because the prereg writes Markdown `does **not** invent CRQN v0.3`, while the literal check expected plain text. Second control-only repair preregistered at commit `7eedb0f88e472c964795b72444a5ce4aa05bd1f1` before repair commit `cee47867a6ad892043b9cf3c088f60296d97d6b1`.

No scientific criterion, candidate selector definition, theorem hypothesis, classification, or interpretation ceiling changed in either repair.

Authoritative repaired production:

- run: `34859635560`;
- production head: `cee47867a6ad892043b9cf3c088f60296d97d6b1`;
- Lane A artifact `10353977634`, digest `sha256:671944893e51953a3a88ec0122faaee1f514ca0f37fd1d026186eccfb76992e2`;
- Lane B artifact `10354756461`, digest `sha256:958564ff14dfc4cae0183c8d224433d32b1d9e7ce9535ed4c1723452bf03e1de`;
- Lane C artifact `10354067590`, digest `sha256:c8095f7b34618d49a2f918ee9e504a173c4c651f51a8ea51842f2a91d01222b1`;
- Lane D artifact `10354132418`, digest `sha256:b2dcf4509368234c5c5de431f85a3d789d75886dacd055e67e56cc33425206c9`;
- aggregate artifact `10353917793`, digest `sha256:4bff0b6f691de010838e969fa67850a8cbafeff078d728f8cb0dfcc31a04561b`.

All five authoritative artifacts were consumed. A/B/C/D are `PASS`; aggregate is complete and execution-valid.

## Frozen independent motivation

The candidate principle was not invented after seeing Iter077Q. The repository already contained Iter029's exact microlocal cycle/wavefront audit, which used the standard wavefront/transversality criterion before Iter077Q existed. The prereg additionally froze standard extension-theory motivation from:

- Brunetti--Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000), arXiv:math-ph/9903028;
- N. V. Dang, *The extension of distributions on manifolds, a microlocal approach*, Ann. Henri Poincaré 17 (2016), arXiv:1412.2808.

This source lock motivates testing microlocal admissibility. It does **not** promote either paper into a CRQN-specific physical selector.

## Frozen selector class

`M_WF` was deliberately narrow:

- support on the already-authoritative common-collision submanifold `N`;
- `WF(u) subset N^*N \ 0`;
- no added differential equation, spectral recurrence, normalization functional, RG/cylindrical law, positivity condition, analyticity boundary-value prescription, or many-vertex law.

Thus the scientific question is only whether **wavefront/conormal admissibility by itself** selects a unique element of the Iter077Q ambiguity space.

## Exact theorem

Iter077Q supplies

`N = SU(2)^4 subset SL(2,C)^4`

and the exact linearly independent family

`u_n = Q(y)^n F(y) delta_N`,  `n = 0,1,2,...`,

where `F` is an authorized nonzero smooth tangential boundary coefficient and `Q` is smooth/real analytic and nonconstant.

Standard microlocal facts give

`WF(delta_N) = N^*N \ 0`

for a smooth embedded submanifold, and for every smooth multiplier `f`,

`WF(fu) subset WF(u)`.

Since every `f_n = Q^n F` is smooth on `N`, every Iter077Q witness obeys

`WF(u_n) subset N^*N \ 0`.

But Iter077Q independently proves the family `{u_n}` is linearly independent. Therefore `M_WF` contains an infinite-dimensional subspace of the already-authorized extension ambiguity and cannot uniquely select the K5 extension.

This is an exact theorem-level implication; no finite numerical sampling is extrapolated into the infinite-dimensional conclusion.

## Authoritative classification

`ITER080J_SM_WAVEFRONT_CONORMAL_ADMISSIBILITY_ALONE_CANNOT_SELECT_ITER077Q_INFINITE_SMOOTH_TANGENTIAL_AMBIGUITY_EXACT_THEOREM_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## What changed scientifically

The K5 selector search is narrower again. A candidate successor principle consisting only of support + ordinary conormal/wavefront admissibility is insufficient: smooth tangential freedom survives it unchanged at normal-derivative order zero.

Combined with earlier gates, the following standalone selector classes are now known insufficient within their exact scopes:

- finite permutation covariance;
- any fixed finite family of scalar complex-linear conditions;
- ordinary conormal/WF admissibility alone.

CRQN v0.2 therefore remains `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`.

## Interpretation ceiling

This result does **not** show that all microlocal selectors fail. A stronger independently motivated condition may still constrain tangential coefficient functions, for example a specific differential/transport equation, microlocal spectrum/boundary-value condition, source-derived spectral law, positivity law, or many-vertex/RG condition.

It does not define CRQN v0.3, does not produce a unique K5 extension, and does not imply `NEW_PHYSICS_FOUND`, G3 PASS, F9/G8/K5 promotion, regulator independence, a causal-vertex finiteness/divergence theorem, or complete quantum gravity.

## Next admissible step

Do not run another WF-only, S5, polynomial-multiplier, fixed-finite scalar-linear, frozen-corpus, or pre-Iter077Q census gate. A next selector test is admissible only if a **stronger function-space condition has independent pre-test physical/mathematical motivation or new/revised primary authority**, and that exact condition is prospectively frozen before implementation.
