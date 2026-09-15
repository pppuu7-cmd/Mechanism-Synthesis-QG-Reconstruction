# Iter083P control-repair provenance ledger

Date: 2026-09-15

## Scientific contract

Parent scientific preregistration is unchanged:

`prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md`

commit `ea29cd3e716d7b35457db493834347a0ca6176a6`.

## Historical invalid production

Original Iter083P production:

- head `bab913eabfb73cc42b3d62a1dd81672ceb0208df`;
- run `34928916039`;
- job `104252818974`;
- artifact `10380702602`;
- artifact digest `sha256:cd307c25dc69c776f310a47ea810bcee0683566f61603ed03a6cd1059b9f9fe8`;
- JSON SHA256 `f06e6268efbe9dbeaf7881b948103a3cc26553575e14b251e9aaba8e0b70b46d`.

Critic implementation invalidation:

`results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `d5641407ce661f6fe125d926880c7f36ef8b7625`.

Reason: R1-R7 were preset to desired booleans, directly relevant source locks were omitted, and malformed controls were not executed through the same validator. Historical scientific verdict remains quarantined permanently.

## Control repair 1

Prospective repair preregistration:

`prereg/ITER083P_CONTROL_ONLY_REPAIR_1.md`, commit `0554c312d3254fc1a7a7cc47a39278cb102fff34`.

Evidence-driven validator implementation:

commit `2f111db087c708839d4e5f1a74d401e7e1745560`.

Outcome-neutral workflow repair/head:

commit `aa47e4fde8e0ef297c631743dd9ef70edd45c32c`.

Run `34932959109` was terminal failure and is `INVALID_IMPLEMENTATION`. It did not produce scientific authority. The only failure was the synthetic positive fixture R3: the fixture contained the phrase `with no`, which the positive-evidence parser treats as negated text. No scientific outcome was promoted from this run.

## Control repair 2

Prospective repair-2 preregistration, frozen before implementation:

`prereg/ITER083P_CONTROL_ONLY_REPAIR_2.md`, commit `46bc10e4dba55f5fb2ae8051beb88941f6eb3060`.

Frozen sole change: remove the negation token from the synthetic positive R3 fixture while preserving identical positive semantics. No evidence rule, corpus rule, R1-R7 requirement, source-order lock, negative control, verdict taxonomy, or interpretation ceiling changed.

Implementation / authoritative production head:

`c7d16b77bac36273942d733be6360be2f681302a`.

The head is a direct descendant of repair-2 prereg commit `46bc10e4dba55f5fb2ae8051beb88941f6eb3060`; therefore the repaired production remains prospective despite the unchanged workflow ancestry checks naming the parent and repair-1 preregistrations.

## Authoritative repaired production metadata

- run `34933068763`: terminal `success`;
- job `104265151196`: terminal `success`;
- artifact `10382228012`;
- artifact name `iter083p-actual-source-residue-object-definition-repair1`;
- artifact ZIP digest `sha256:d56a961a5360ac8bf209a626316982a2d34318dfc85086797661e2f19d165208`;
- exact production JSON SHA256 `1a51f41cdd011ab1d4527e8af255819eb5a5461ac6453d02bea715c65896eb64`;
- authority manifest count `51`;
- `manifest_complete=true`;
- `execution_valid=true`;
- synthetic positive fixture `PASS_OBJECT_DEFINED_SCOPED`;
- all seven malformed negative controls rejected by the same validator.

Durable terminal summary:

`results/raw/iter083p_control_repair2_terminal_summary.json`, commit `5a8766e501e26291563f6289a88590e3226fd193`.

Durable result note:

`results/ITER083P_CONTROL_REPAIR_2_RESULT.md`, commit `9462af0f0f2a76f65eb310b86a1fa9d9e9ac1f34`.

## Scientific result from valid repair

All seven frozen requirements R1-R7 are mechanically classified:

`ABSENT_OR_ONLY_CONDITIONAL`.

Researcher verdict:

`BLOCKED_OBJECT_DEFINITION`.

Classification:

`ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED`.

This repaired result awaits independent Critic review before any downstream source-bridge gate can be opened.

## Claim locks

No physical residue value/order/sign/cancellation; no physical finite-part selector; no regulator dependence/independence theorem; no unique K5 extension; no source-to-K4 surrogate promotion; no F9/G3/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.
