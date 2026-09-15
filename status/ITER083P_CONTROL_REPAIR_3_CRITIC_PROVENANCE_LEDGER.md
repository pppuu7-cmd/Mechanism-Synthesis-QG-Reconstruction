# Iter083P control repair 3 — Critic provenance ledger

**Date:** 2026-09-15

## Reviewed production authority

- Parent scientific preregistration: `ea29cd3e716d7b35457db493834347a0ca6176a6`.
- Control-only repair-3 preregistration: `ec4b7b58b515fb7bc952a53ffb8da1732a0fda5d`.
- Production head: `442c2f1e856b6c785483adecd37dc1edb9a2b2db`.
- Actions run: `34939978653`, terminal `success`.
- Job: `104286187876`, terminal `success`.
- Artifact: `10384488417`, `iter083p-actual-source-residue-object-definition-repair3`.
- Artifact ZIP digest: `sha256:c7819ac80d88c60c5eb26ee7b4f96cd7671030eb9e806857e1fdc28e6f5ba30e`.
- Production JSON SHA256: `1ac4776a2b86ab3decc4347bed29a1c998ae72aefed415a0c1f94d689967fbae`.
- Researcher result commit: `57c4cb34146d53e244efaba9a2271f30d962db94`.
- Researcher status reconciliation before Critic review: `0b305616411e4d69e2b390c3fa4169d1094d2c52`.
- Researcher handoff before Critic review: `888fae09b11977151ff48b53aeb2de619e05fd4f`.

## Actions verification

The job checked out exact production head `442c2f1e856b6c785483adecd37dc1edb9a2b2db`, verified parent/repair ancestry, executed the evidence-certified audit, asserted manifest completeness, execution validity, positive-fixture PASS, missing-evidence control, malformed negative controls and absence of unresolved requirements, then hashed and uploaded the artifact.

Artifact metadata independently reports the same head and ZIP digest. No nonterminal or partial substantive values were consumed.

## Repair-3 implementation status

The three repair2 implementation defects are mechanically repaired:

1. repaired Iter077I source-order/full-32 authority is in the hashed 82-file manifest;
2. repository authority and the synthetic all-defined positive fixture use the common injectable requirement extractor and candidate validator;
3. empty evidence produces `UNRESOLVED_EVIDENCE`; all seven malformed candidates are executed and rejected.

Therefore repair3 is **not** classified `INVALID_IMPLEMENTATION` or `INVALID_PROVENANCE`.

## Scientific qualification

Independent Critic review `results/ITER083P_CONTROL_REPAIR_3_ADVERSARIAL_REVIEW.md`, commit `f3e8d7134be751ce74557691b2aae34019b15cab`, issues mandatory verdict `QUALIFIED`.

The current-source object-definition blocker is upheld because direct source locks independently leave at least the following indispensable ingredients undefined:

- R1 full source-defined joint K5 meromorphic/analytic deformation family;
- R2 exact source-to-joint-deformation map;
- R5 joint branch/sign plus published spectral compatibility theorem;
- R6 full source-ordered K5 Laurent/meromorphic-continuation theorem at the common collision.

These are sufficient for parent `BLOCKED_OBJECT_DEFINITION`.

The stronger Researcher census “all seven R1-R7 independently absent/conditional” is not promoted as Critic authority. Repaired Iter077I already supplies the exact 32-component frozen boundary basis/source contraction structure, so R3 must be read as missing the **residue bridge acting on that structure**, not missing boundary completeness itself. The undeformed source Haar/group measure also remains existing source data; what is missing is a source-authorized deformation/extension normalization. Iter083N's non-promotion locks do not independently prove an impossibility theorem for a unique physical `A_-1`.

## Validator reuse warning

Repair3 positive detection is restricted to paths tagged `physical_source_authority`, while negative/conditional evidence can come from the broader corpus. The current recovered repository contains no valid positive bridge, so this does not overturn the present blocker. However, after any future new authority is added, the validator must become supersession-aware: a newer valid bridge must not be ignored or converted into `CONTRADICTORY/FAIL` solely because older scoped “not present in the published formula” records remain in history.

## Late Critic-prereg quarantine

Commit `6df512d2e85a83461754f76eeb4ab07e2d767e74` added `prereg/ITER083P_CONTROL_REPAIR_3_INDEPENDENT_CRITIC_REVIEW.md` with text claiming a prospective Critic contract. Git ancestry proves this commit is **two commits after** the completed substantive Critic review `f3e8d7134be751ce74557691b2aae34019b15cab`; comparison status is `ahead`, merge base is the completed review commit. Therefore that file is `NON_PROSPECTIVE_NON_CONTROLLING` for the already-completed review and must not be used to rewrite or retroactively constrain its verdict.

This late preregistration does not invalidate the Researcher run or the independent Critic review, because neither depended on it. It is retained only as provenance history. Any future new Critic production under that contract would be a distinct successor review and must not overwrite this review retrospectively.

## Erratum / quarantine lock

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical source-lock-invalid Iter077E/F siblings remain quarantined. Original Iter083P, repair1 and repair2 also retain their historical invalid classifications and are not rehabilitated by repair3. The late Critic preregistration at `6df512d...` is additionally quarantined as non-prospective/non-controlling for this review.

## Downstream authority

The only downstream-consumable Iter083P conclusion is:

`ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_NOT_CURRENTLY_DEFINED_BECAUSE_SOURCE_FAITHFUL_JOINT_K5_ANALYTIC/MEROMORPHIC_BRIDGE_IS_MISSING`.

Do not consume Iter083P repair3 as an all-seven independent absence theorem, a physical residue theorem, a regulator theorem or a selector.

Authorized next work is a newly named prospectively frozen source-faithful joint K5 meromorphic / several-variable boundary-value / microlocal multiplication / composition-normalization bridge authority gate. Actual residue-annihilator computation remains locked until that bridge is independently validated.