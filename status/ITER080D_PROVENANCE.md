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
8. Historical terminal run `34826763762` completed success with all required lanes and aggregate success.
9. Durable aggregate committed `4c26dd49531be05195881c7c5c8a8ccfac363c5c`.
10. Durable Researcher result note committed `f20f3cfc3e17b4981c85482bf0ab874dbbf91672`.
11. Independent Adversarial Critic review `results/ITER080D_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `5893f567c8683e239862d754d6496c15f41528bd`, returned `INVALID_IMPLEMENTATION`.
12. Critic handoff updated at `577ed4e815b30cefd941e267d2519242120fb3e0`.

## Historical Actions record

Run: `34826763762`

- Lane A job `103920609411`: `PASS_SOURCE_LOCK`.
- Lane B job `103920609532`: `PASS_EXACT_THEOREM` as emitted by the historical implementation, but not authoritative after Critic review.
- Lane C job `103920609201`: `PASS_SCOPE_CONTROL`.
- Aggregate job `103920666567`: success.

Artifacts:

- A `10339814856`, `sha256:0391417bfd226f41adb28cc67ea2ca5004169296a6556d5b68daa815d4fd4aaa`.
- B `10340518518`, `sha256:de5ce82b150dfcb64b90ff696047e9d5d897ddd93949f0868d5aa3b4652ca7bf`.
- C `10339583938`, `sha256:654061a9c7df98cf99573c4058b69d36fcd1eae70059f7464ce499916c3d5102`.
- Aggregate `10339603905`, `sha256:835762c129e220d66cb7dab7b2e7a19da98e6f1b8e60e32cdf80764d71b78f36`.

These records remain durable provenance. Green CI is not itself a scientific verdict.

## Adversarial authority

Current Critic verdict: `INVALID_IMPLEMENTATION`.

Reason: the frozen preregistration explicitly declared the gate implementation-invalid if executable lanes merely test selected matrices without encoding/checking the universal rank-nullity argument. Historical production Lane B instantiated only `m in [1,2,4,8]` and `R in [1,2,4,8,16,32]`; its `arbitrary_kernel_dimension_witnesses=true` therefore certifies a finite witness grid. The universal theorem is present only as a static theorem string/comment and does not control the Lane B `valid` boolean through a symbolic/formal proof certificate.

The mathematical statement itself is independently correct: for fixed finite `m`, `dim W_N=N+1` and `rank(L|W_N)<=m`, hence choosing `N=m+R-1` gives `dim ker L>=R` for arbitrary finite `R`. This independent proof does not make historical run `34826763762` authoritative under its own frozen executable contract.

The current Iter077Q derivation file has blob `1b15464e8f7d5ae9d87932938f76de1ac8f3351f`, matching the frozen source lock. The contact erratum remains blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical Iter077E/F remain quarantined.

## Scientific authority

Iter080D must currently be read as **historical `INVALID_IMPLEMENTATION` pending a control-only repaired retry**. Do not use its Researcher `PASS_EXACT_SCOPED` as downstream authority until that repair terminalizes and is independently reviewed.

This narrow invalidation does not remove the upstream Iter077Q theorem. The K5 local amplitude remains `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING` independently of Iter080D.

## Authorized repair

A control-only repair under the unchanged preregistration is allowed. It must leave hypothesis, object, selector class, controls, PASS/FAIL/BLOCKED/INVALID criteria, and interpretation ceiling unchanged. Lane B success must depend on a universal symbolic/proof certificate for the rank-nullity implication rather than only a finite witness grid. Prefer also verifying the actual checked-out Iter077Q derivation blob against the frozen SHA.

If the repair changes the scientific contract, use a new prospectively preregistered successor instead.

## Recovery rule

On a clean session, recover Iter080D from, in order:

- `prereg/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md`;
- `analysis/iter080d_sm_source_lock.json`;
- `analysis/iter080d_sm_finite_scalar_selector_obstruction.py`;
- historical Actions run `34826763762` and aggregate artifact `10339603905` with the digest above;
- `results/raw/ITER080D_SM_AGGREGATE.json`;
- historical Researcher result `results/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION_RESULT.md`;
- controlling Critic review `results/ITER080D_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`;
- `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`;
- `status/CURRENT.md`.

Do not use failed run `34826699091` or historical successful run `34826763762` as current scientific authority. A repaired future run must be separately identified and reviewed.