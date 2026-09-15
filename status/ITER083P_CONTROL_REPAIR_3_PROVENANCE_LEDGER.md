# Iter083P control repair 3 provenance ledger

Date: 2026-09-15

## Scope

Control-only repair of `Iter083P-SM — ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION`. Scientific parent contract is unchanged from `prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md`, commit `ea29cd3e716d7b35457db493834347a0ca6176a6`.

## Historical quarantine

- original Iter083P run `34928916039`: historical `INVALID_IMPLEMENTATION`;
- repair-1 run `34932959109`: `INVALID_IMPLEMENTATION`;
- repair-2 run `34933068763`: Researcher `BLOCKED_OBJECT_DEFINITION` but independently invalidated as `INVALID_IMPLEMENTATION` by Critic commit `45c7595838ade746935a5d6d6ea495cfc4fd44a8`.

None of those executions is promoted by repair 3.

## Prospective chronology

- controlling repair-2 Critic result: `45c7595838ade746935a5d6d6ea495cfc4fd44a8`;
- repository status quarantining repair2: `8ef8e2c70474bc36e78a583ed705f4e64d61b6c5`;
- repair-3 prospective control contract: `prereg/ITER083P_CONTROL_ONLY_REPAIR_3.md`, commit `ec4b7b58b515fb7bc952a53ffb8da1732a0fda5d`;
- repair implementation/workflow head: `442c2f1e856b6c785483adecd37dc1edb9a2b2db`.

The repair-3 preregistration preceded implementation and production output.

## Production

- run: `34939978653`;
- run conclusion: `success`;
- job: `104286187876`, conclusion `success`;
- exact checkout/head: `442c2f1e856b6c785483adecd37dc1edb9a2b2db`;
- artifact: `10384488417`;
- artifact name: `iter083p-actual-source-residue-object-definition-repair3`;
- artifact ZIP digest: `sha256:c7819ac80d88c60c5eb26ee7b4f96cd7671030eb9e806857e1fdc28e6f5ba30e`;
- production JSON SHA256: `1ac4776a2b86ab3decc4347bed29a1c998ae72aefed415a0c1f94d689967fbae`;
- artifact size: `18718` bytes;
- hashed authority manifest entries: `82`;
- `manifest_complete=true`;
- `execution_valid=true`.

The exact artifact was independently downloaded after terminal completion and its contained production JSON reproduced the logged SHA256 `1ac4776a2b86ab3decc4347bed29a1c998ae72aefed415a0c1f94d689967fbae`.

## Frozen authority coverage

The runtime manifest now includes and hashes, among other controlling records:

- repaired Iter077I source-order/full-32 derivation `sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md`;
- `status/ITER077_CONTACT_FORMULA_ERRATUM.md`;
- Iter080K source matrix;
- Iter083E/F/G/H/J/K/L/M/N direct locks/derivations relevant to the gate;
- parent Iter083P preregistration;
- repair-1/2/3 contracts;
- controlling repair-2 Critic prereg/review/provenance;
- `status/CURRENT.md` plus Researcher and Critic handoffs.

This directly repairs the material manifest omission identified in repair2.

## Same-validator controls

The synthetic all-R1-R7 positive authority passes the same injectable requirement extractor and same candidate validator used for repository authority and returns `PASS_OBJECT_DEFINED_SCOPED`.

A synthetic missing-evidence authority intentionally omits R7 positive and negative evidence. The common extractor returns `R7=UNRESOLVED_EVIDENCE`; this control passes and proves that a lexical non-hit alone cannot produce a blocker classification.

All seven malformed candidate controls are executable and rejected by the common validator.

## Production scientific output

All seven frozen requirements R1-R7 are evidence-certified `ABSENT_OR_ONLY_CONDITIONAL`; none is `UNRESOLVED_EVIDENCE`. Production classification:

`ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED`

Verdict: `BLOCKED_OBJECT_DEFINITION`.

Durable terminal summary: `results/raw/iter083p_control_repair_3_terminal_authority.json`, commit `537a7e2782d21205a1845a66f63dc8843c9930c0`.

Durable Researcher result: `results/ITER083P_CONTROL_REPAIR_3_RESULT.md`, commit `57c4cb34146d53e244efaba9a2271f30d962db94`.

## Promotion lock

This repaired result is a Researcher classification awaiting independent Critic review. No source-faithful joint bridge, actual residue annihilator or downstream physical result may consume it before that review. Historical Iter083P executions remain quarantined.
