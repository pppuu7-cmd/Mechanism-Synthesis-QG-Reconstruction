# Iter080D-SM provenance

**Date:** 2026-09-14

## Contract ordering

1. Duplicate Iter080C E3/E4/E6 preregistration was administratively aborted before scientific execution because fresh recovery showed Iter080B had already terminalized that same gate. See `status/ITER080C_DUPLICATE_PREREG_ABORT.md`. This does not count as a scientific gate.
2. Iter080D prospective contract was committed before substantive computation: `a61780f9f84cf2ecff0e4a09993322f37e310d4c`.
3. Frozen source lock committed: `24e4f8a33efe9305e62656bf942157b00223ca62`.
4. Initial implementation committed: `965a9dbcb4fe44b0148a8a7d6317e2d307691dc1`.
5. Workflow committed: `1d561cfe4e076f3d2674ebe0fc06c9ecaa6391c4`.
6. First run `34826699091` terminal failure: Lane A `INVALID_SOURCE_LOCK` due solely to a brittle text matcher for the already-correct erratum formula. No scientific verdict promoted.
7. Control-only implementation repair commit `849eddbac5fab7dd44fdea3b6d2b3f083a8e9c9a`; frozen scientific contract unchanged.
8. Authoritative terminal run `34826763762` completed success with all required lanes and aggregate success.
9. Durable aggregate committed `4c26dd49531be05195881c7c5c8a8ccfac363c5c`.
10. Durable result note committed `f20f3cfc3e17b4981c85482bf0ab874dbbf91672`.

## Authoritative Actions record

Run: `34826763762`

- Lane A job `103920609411`: `PASS_SOURCE_LOCK`.
- Lane B job `103920609532`: `PASS_EXACT_THEOREM`.
- Lane C job `103920609201`: `PASS_SCOPE_CONTROL`.
- Aggregate job `103920666567`: success.

Artifacts:

- A `10339814856`, `sha256:0391417bfd226f41adb28cc67ea2ca5004169296a6556d5b68daa815d4fd4aaa`.
- B `10340518518`, `sha256:de5ce82b150dfcb64b90ff696047e9d5d897ddd93949f0868d5aa3b4652ca7bf`.
- C `10339583938`, `sha256:654061a9c7df98cf99573c4058b69d36fcd1eae70059f7464ce499916c3d5102`.
- Aggregate `10339603905`, `sha256:835762c129e220d66cb7dab7b2e7a19da98e6f1b8e60e32cdf80764d71b78f36`.

## Scientific authority

Verdict: `PASS_EXACT_SCOPED`.

Classification:

`ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`.

The theorem is exact rank-nullity on the already-authoritative Iter077Q source-compatible ambiguity family. It excludes only selectors made of a fixed finite number of scalar-valued complex-linear conditions. The K5 local amplitude remains `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.

## Recovery rule

On a clean session, recover Iter080D from, in order:

- `prereg/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md`;
- `analysis/iter080d_sm_source_lock.json`;
- `analysis/iter080d_sm_finite_scalar_selector_obstruction.py`;
- Actions run `34826763762` and aggregate artifact `10339603905` with the digest above;
- `results/raw/ITER080D_SM_AGGREGATE.json`;
- `results/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION_RESULT.md`;
- `status/CURRENT.md` and the latest Researcher/Critic handoffs.

Do not use failed run `34826699091` as scientific authority. Green CI is not itself a scientific verdict.
