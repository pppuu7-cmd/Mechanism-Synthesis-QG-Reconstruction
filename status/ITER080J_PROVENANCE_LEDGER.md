# Iter080J-SM provenance ledger — microlocal WF-only selector power

Date: 2026-09-14

## Scientific contract

- Original prospective preregistration: `bffd6cf275d930203ff272cba3bbae8916fdc51b`.
- Frozen object: Iter077Q supported ambiguity family `u_n = Q^n F delta_N` on `N=SU(2)^4 subset SL(2,C)^4`.
- Frozen candidate restriction `M_WF`: support on `N` and `WF(u) subset N^*N \\ 0` only; no added coefficient equation, differential/spectral recurrence, boundary-value condition, normalization, RG/cylindrical law, positivity, or composition law.
- Frozen PASS classification: `ITER080J_SM_WAVEFRONT_CONORMAL_ADMISSIBILITY_ALONE_CANNOT_SELECT_ITER077Q_INFINITE_SMOOTH_TANGENTIAL_AMBIGUITY_EXACT_THEOREM_SCOPED`.
- Interpretation ceiling unchanged throughout repairs.

## Chronology

1. Scientific preregistration `bffd6cf275d930203ff272cba3bbae8916fdc51b`.
2. Initial implementation `e11c1f8ebac7354ac9d5588f187a045d405425a2`.
3. Workflow / initial production head `521faa0c45d9030a18171a2ecaf218cba15cf8f7`.
4. Historical run `34859269730`: implementation-invalid Lane B Unicode/ASCII surname control; no scientific verdict.
5. Control-only repair preregistration `0dc17ae388f763e7c020e3e8add7c79d40fdbb2c`.
6. First lexical repair `a9a34e05562023a7697e15a45c298f9681a53527`.
7. Historical run `34859501380`: implementation-invalid Lane B Markdown-emphasis raw-substring control; lanes A/C/D passed; no scientific verdict.
8. Second control-only repair preregistration `7eedb0f88e472c964795b72444a5ce4aa05bd1f1`.
9. Markdown-normalization repair / authoritative production head `cee47867a6ad892043b9cf3c088f60296d97d6b1`.
10. A redundant same-scope repair note was later committed as `c1301b8f52c1b082531261821738b1e6174932ac`; it changes no scientific contract and is not needed for production chronology because `7eedb0f...` already prospectively froze the exact repair before `cee4786...`.
11. Authoritative repaired run `34859635560`: terminal success.
12. Durable raw aggregate commit `77bb729dc8225379cc946de2cddcd217baa028f9`.
13. Durable result commit `e9d1867fc8a1026ed678aac0e3c768c654c39487`.
14. `status/CURRENT.md` synchronization commit `db9a49fa1a42c5755b5805e0a2a7f92b89798d68`.

## Authoritative Actions record

Run `34859635560`, head `cee47867a6ad892043b9cf3c088f60296d97d6b1`, conclusion `success`.

Jobs:

- Lane A `104028122432`: success.
- Lane B `104028122783`: success.
- Lane C `104028123076`: success.
- Lane D `104028123050`: success.
- Aggregate `104028188175`: success.

Artifacts:

- Lane A `10353977634`, `sha256:671944893e51953a3a88ec0122faaee1f514ca0f37fd1d026186eccfb76992e2`.
- Lane B `10354756461`, `sha256:958564ff14dfc4cae0183c8d224433d32b1d9e7ce9535ed4c1723452bf03e1de`.
- Lane C `10354067590`, `sha256:c8095f7b34618d49a2f918ee9e504a173c4c651f51a8ea51842f2a91d01222b1`.
- Lane D `10354132418`, `sha256:b2dcf4509368234c5c5de431f85a3d789d75886dacd055e67e56cc33425206c9`.
- Aggregate `10353917793`, `sha256:4bff0b6f691de010838e969fa67850a8cbafeff078d728f8cb0dfcc31a04561b`.

Durable raw aggregate: `results/raw/iter080j_sm_aggregate.json`.

## Exact scientific result

Iter077Q gives an exact linearly independent family

`u_n = Q(y)^n F(y) delta_N`, `n=0,1,2,...`,

with smooth tangential coefficients `Q^n F` on the embedded common-collision submanifold `N`.

The frozen standard microlocal implications are:

- `WF(delta_N)=N^*N \\ 0`;
- smooth multiplication cannot enlarge wavefront set: `WF(fu) subset WF(u)`.

Therefore every `u_n` satisfies the standalone `M_WF` admissibility requirement. Since Iter077Q independently proves the family linearly independent, an infinite-dimensional subspace of the extension ambiguity survives. `M_WF` cannot uniquely select the K5 extension.

Authoritative verdict: `PASS_EXACT_SCOPED`.

## Scope / claim locks

This excludes only ordinary support + conormal/wavefront admissibility **alone** as a unique selector. It does not show that all microlocal, differential, spectral, analytic boundary-value, positivity, composition, or RG selectors fail. It does not define a successor candidate and does not change the status of CRQN v0.2: `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE` remains controlling.

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no G3 PASS; no F9/G8/K5 promotion; retain published one-wedge spectral `i epsilon` only in source scope.
