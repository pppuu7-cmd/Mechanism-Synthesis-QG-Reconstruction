# Iter083N provenance-correct retry — control-only repair 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN AFTER TERMINAL IMPLEMENTATION FAILURE AND BEFORE REPAIR IMPLEMENTATION**

Parent scientific preregistration remains `prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md`, commit `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.
Retry preregistration remains `prereg/ITER083N_PROVENANCE_CORRECT_RETRY_1.md`, commit `d9edb0fd2a5c522ddec021f2b4f8e1a964ee3d96`.
Historical retry run `34925091322` on head `62407b98b51985d60ca1746af3aa2e9804ca314a` is non-authoritative and classified `INVALID_IMPLEMENTATION`; it produced no authoritative artifact.

## Defect found

The retry validator correctly consumed CURRENT, repaired Iter083M Critic authority, Iter082D/083B, parent preregistration, retry preregistration and all P1-P7 exact algebra. P0 alone failed because the historical invalid-review text check required the literal phrase `stale Iter083M Researcher result`, while the actual immutable review expresses the same authority defect with different wording: it says the executable opened the old Researcher Iter083M result and promoted stale `PASS_EXACT_SCOPED` text despite the controlling invalidation.

The run log reported exactly one missing lexical marker under `P0_historical_invalid_review`; all other dependency-missing lists were empty. This is a text-matching implementation defect, not a scientific result.

## Allowed repair

Replace only the brittle historical-review phrase check with robust exact authority markers that are actually present in `results/ITER083N_ADVERSARIAL_PROVENANCE_REVIEW.md`:

- verdict `INVALID_PROVENANCE`;
- statement that the validator used the old Researcher Iter083M result file / `PASS_EXACT_SCOPED` rather than controlling authority;
- actual source-lock commit `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`;
- actual theorem commit `70a756c9c7c66f822d0e5933e9522b2d359dafe8`;
- required recovery statement that a later Iter083N rerun must verify controlling repository authority.

No P1-P7 formula, threshold, source authority, scientific object, PASS/FAIL criterion, interpretation ceiling, control semantics or claim lock may change.

## Production rule

The repaired run must use the same retry workflow identity, a new checkout head, and full-history ancestry checks. Historical run `34925091322` remains non-authoritative forever. If the repaired run fails for any further implementation/provenance reason, do not extract a scientific verdict from partial values; repair only under another prospective control-only note.
