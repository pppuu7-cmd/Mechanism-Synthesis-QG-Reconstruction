# Iter080J-SM second control-only repair preregistration — Markdown normalization

Date: 2026-09-14

## Historical retries preserved

- run `34859269730`: `INVALID_IMPLEMENTATION_LEXICAL_CONTROL`; no scientific verdict.
- run `34859501380`: still implementation-invalid in Lane B; A/C/D passed again.

## Exact remaining defect

Lane B's frozen scope requirement is that the gate must not construct or declare CRQN v0.3. The preregistered document states this explicitly as Markdown:

`This gate does **not** invent CRQN v0.3 ...`

The implementation searched for the plain literal substring

`does not invent CRQN v0.3`

without Markdown normalization. Therefore the predicate fails solely because `**` interrupts the literal token sequence.

## Frozen repair

Only the Lane B textual control for this already-frozen scope statement may change:

- normalize Markdown emphasis markers before checking the semantic phrase `does not invent CRQN v0.3`, or equivalently accept the exact authoritative Markdown spelling;
- do not alter the independent-motivation requirement, source locks, M_WF definition, theorem proof, PASS/FAIL classification, or interpretation ceiling.

All scientific criteria remain those prospectively frozen in `prereg/ITER080J_SM_MICROLOCAL_WF_ONLY_SELECTOR_MOTIVATION_AND_POWER.md` at commit `bffd6cf275d930203ff272cba3bbae8916fdc51b`.

## Classification handling

The two historical failed runs remain implementation-invalid and cannot support a scientific conclusion. Only a subsequent complete repaired run with all A/B/C/D plus aggregate execution-valid may receive the original frozen scientific classification.
