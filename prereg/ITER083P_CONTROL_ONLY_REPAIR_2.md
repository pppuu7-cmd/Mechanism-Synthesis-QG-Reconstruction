# Iter083P control-only repair 2

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR-2 IMPLEMENTATION / REPAIRED PRODUCTION OUTPUT**

Parent scientific preregistration remains `prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md` at commit `ea29cd3e716d7b35457db493834347a0ca6176a6`.
Repair-1 preregistration remains `prereg/ITER083P_CONTROL_ONLY_REPAIR_1.md` at commit `0554c312d3254fc1a7a7cc47a39278cb102fff34`.
Repair-1 implementation head `aa47e4fde8e0ef297c631743dd9ef70edd45c32c`, run `34932959109`, is `INVALID_IMPLEMENTATION` because the synthetic positive fixture failed only R3.

## Exact repair-2 defect

The evidence parser intentionally rejects a paragraph containing negation markers from positive-definition evidence. The synthetic all-32 positive fixture sentence was:

`The residue map uses the full boundary contraction on all 32 components with no representative-component reduction.`

The words `with no` caused the same parser to reject this otherwise positive synthetic R3 fixture. Main repository R1-R7 substantive values were not used for a scientific verdict because `execution_valid=false` and the run failed before artifact promotion.

## Frozen control-only change

Change only the synthetic positive R3 fixture wording to an unambiguously positive sentence with identical intended fixture semantics:

`The residue map uses the full boundary contraction on all 32 components.`

No evidence rule, corpus manifest rule, R1-R7 requirement, source-order lock, candidate validator, malformed negative control, PASS/FAIL/BLOCKED/INVALID criterion, interpretation ceiling, or scientific object may change in repair 2.

The workflow ancestry check may additionally require this repair-2 preregistration commit. It must remain outcome-neutral and must not assert the repaired scientific verdict.

## Historical-run lock

Run `34932959109` remains `INVALID_IMPLEMENTATION` and cannot support any Iter083P scientific classification. Repair 2 is permitted only because this failure is a synthetic positive-control wording bug under the already-frozen repair-1 machinery.
