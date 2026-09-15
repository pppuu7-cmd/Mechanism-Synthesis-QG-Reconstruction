# Iter083P control-repair-2 Critic provenance ledger

**Date:** 2026-09-15

## Reviewed production

- scientific preregistration: `ea29cd3e716d7b35457db493834347a0ca6176a6`;
- repair-1 preregistration: `0554c312d3254fc1a7a7cc47a39278cb102fff34`;
- repair-2 preregistration: `46bc10e4dba55f5fb2ae8051beb88941f6eb3060`;
- production head: `c7d16b77bac36273942d733be6360be2f681302a`;
- Researcher result commit: `9462af0f0f2a76f65eb310b86a1fa9d9e9ac1f34`;
- independent Critic preregistration: `6139df48dbeca09d329ed847fc3e2476cbeaba12`;
- run: `34933068763`, terminal success;
- job: `104265151196`, terminal success;
- artifact: `10382228012`;
- artifact ZIP digest: `sha256:d56a961a5360ac8bf209a626316982a2d34318dfc85086797661e2f19d165208`;
- production JSON SHA256: `1a51f41cdd011ab1d4527e8af255819eb5a5461ac6453d02bea715c65896eb64`.

Actions provenance/head/artifact identity are valid. Historical original Iter083P run `34928916039` and repair-1 run `34932959109` remain quarantined as `INVALID_IMPLEMENTATION`.

## Controlling Critic result

`results/ITER083P_CONTROL_REPAIR_2_ADVERSARIAL_REVIEW.md`, commit `45c7595838ade746935a5d6d6ea495cfc4fd44a8`.

Mandatory verdict: `INVALID_IMPLEMENTATION`.

## Exact implementation defects

1. **Incomplete controlling authority manifest.** The parent scientific preregistration explicitly freezes repaired Iter077I source-order authority, and the Critic C1 contract requires source locks relevant to the K5 off-collision/source-order/full-boundary object. Production's 51-file manifest is generated only from `ITER080K_`, `ITER083E_` through `ITER083N_`, and selected status files. It omits `sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md`, commit `f7f0a957e7a0379be39f164bd6903a6e78425f95`, which contains the ten-Toller/four-group-integration ordering and exact 32-component minimal boundary basis used by the frozen chain.

2. **Special positive-fixture requirement extractor.** Repository authority uses `derive_requirements()`. The synthetic fixture does not; `synthetic_positive_fixture()` duplicates a positive-only requirement loop and directly assigns `DEFINED` before calling the candidate validator. The frozen repair contract requires the same requirement and candidate validator, and Critic C3 forbids a special positive-fixture bypass.

3. **R3 absence without exact absence evidence.** Production reports R3 `positive_matches=[]` and `negative_or_absence_matches=[]`, yet mechanically assigns `ABSENT_OR_ONLY_CONDITIONAL`. Repair-1 froze that absence status requires the complete manifest plus exact source-lock evidence records of absence/conditional-only status. A no-keyword-hit on a restricted prefix corpus is not that evidence.

These defects invalidate certification of the repaired `BLOCKED_OBJECT_DEFINITION` verdict. They do not show that the scientific blocker is false.

## Independent source cross-check retained

Earlier source locks still independently favor the same qualitative blocker: Iter080K records no explicit simultaneous ten-wedge collision-extension rule; Iter083L records one-wedge spectral epsilon before the ten-factor K5 product and no common collision regulator/joint subtraction/composition normalization; Iter083H remains conditional rather than a full K5 meromorphic theorem; Iter083N is a formal local Laurent theorem. These prior scoped facts remain usable in their own scopes, but they do not rescue the invalid Iter083P repair-2 execution.

## Downstream lock

Repaired Iter083P may not be consumed as authoritative `BLOCKED_OBJECT_DEFINITION`. No source-faithful bridge/residue-annihilator gate may be opened from it. Only another control-only Iter083P repair under the unchanged scientific contract is authorized, unless correcting the defect requires changing the scientific object/criteria, in which case a new prospective successor preregistration is required.

Claim locks and Iter077 contact erratum quarantine remain unchanged.