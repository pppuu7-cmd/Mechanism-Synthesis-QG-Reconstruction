# Iter080K-SM adversarial provenance/source review

**Date:** 2026-09-14

## RESULT_REVIEWED

Researcher result: `results/ITER080K_SM_NEW_TOLLER_ANALYTICITY_JOINT_K5_SELECTOR_AUDIT_RESULT.md`, commit `bc934d54915350aae4438b594470962335cd3de5`.

Prospective preregistration: `363d15318a7747671111e1a8f2f79793f87ce2f6`.
Source matrix: `2885f70533331bdb0b13555d360f48848b43b47b`.
Implementation: `36bc70b1033aa9defeb09bb8b171914cf7046501`.
Production head: `cc9a8aa036c6a52782da76e2ea215ce379fc415c`.
Run: `34860144694`, terminal `success`.
Aggregate artifact: `10354063246`, digest `sha256:40ced95997238b98c617ba5dd77a71c46f6d42ccc655e03a83a0d6536da1105e`.

Researcher classification:
`ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_UNIQUELY_FIXES_ONE_WEDGE_BRANCHES_BUT_DOES_NOT_EXPLICITLY_SELECT_JOINT_K5_EXTENSION_SOURCE_BRIDGE_BLOCKED_SCOPED`.

Researcher verdict: `BLOCKED_SOURCE_BRIDGE_SCOPED`.

## SOURCE_OBJECT_CHECK

The frozen scientific question itself targets the correct distinction: one-wedge Toller analytic uniqueness versus a correlated simultaneous ten-wedge K5 distributional extension/selector acting on the Iter077Q tangential function space.

Independent re-reading of arXiv:2604.24945 confirms the substantive source characterization used by the Researcher:

- reduced Toller branches are uniquely characterized by the stated analytic/asymptotic/pole/sum-rule data;
- the Feynman `i epsilon` contour acts as a projector onto the admissible one-wedge branches;
- Toller `T`-matrices are functions on `SL(2,C)` and explicitly do **not** form a Lorentz-group representation, so ordinary representation composition cannot manufacture a multi-wedge law;
- no explicit correlated simultaneous-K5 extension law or rule acting on the Iter077Q tangential coefficient functions was identified in this source.

These source facts are scientifically consistent with the Researcher conclusion. They do not cure the provenance defect below.

## SOURCE_ORDERING_CHECK

The reviewed result correctly preserves the source-order firewall

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

It does not infer joint-K5 uniqueness by multiplying termwise contact distributions and does not use representation composition. No source-order violation was found.

## PROVENANCE_CHECK

A decisive preregistration/admissibility contradiction is present.

Iter080K freezes the trigger:

> `A primary source not represented in the frozen Iter080E BCG/Beltran selector census has been identified: ... arXiv:2604.24945`.

It then states that this is a `genuinely additional primary authority` satisfying the `NEW_PRIMARY_AUTHORITY` route.

That premise is false in the durable repository record **before Iter080K was preregistered**.

Iter080E preregistration commit `f1a465a059f7c4da8270bed8021f920013b7f5da` explicitly freezes exactly three source versions, including:

- Bianchi--Chen--Gamonal `2601.23162`;
- Bianchi--Chen--Gamonal **`2604.24945`**;
- Beltran `2603.22661v2`.

Iter080E source snapshot commit `d51f7cc0f6970670cef1e73223b30cb70b00b8c0` contains a dedicated `S2 — Bianchi–Chen–Gamonal, Toller matrices, arXiv:2604.24945` row. That row already records that the paper derives the Feynman-`i epsilon` Toller projector/matrices and exact analytic identities for individual Toller matrices, while providing no joint K5 extension prescription or full-function-space uniqueness rule.

The repaired Iter080E provenance ledger at `a677229c850c04d7047afe38648a66c00329f129` again identifies `2604.24945` as part of the frozen authoritative corpus. Its authoritative repaired run `34836322547` concludes that no real row in that three-source corpus supplies the required P1-P5-complete joint-K5 selector.

Most importantly, `status/CURRENT.md` immediately before Iter080K (for example at commit `db9a49fa1a42c5755b5805e0a2a7f92b89798d68`) explicitly says:

- do **not** repeat frozen BCG/Beltran selector scans;
- authorize a new local-selector gate only from `(a)` genuinely new/revised primary authority defining a correlated joint-K5 prescription or `(b)` an independently motivated stronger function-space selector principle.

Iter080K uses the same arXiv source/version already frozen and audited in Iter080E. It neither freezes a newly revised version nor introduces an independently motivated new selector principle. Therefore its declared `NEW_PRIMARY_AUTHORITY` admissibility route is not satisfied.

This is not repaired by the fact that Iter080K extracts sharper one-wedge details (explicit uniqueness and non-representation statements) from the already-known source. New observations about an old frozen source are not the `genuinely new/revised primary authority` required by the active-front contract, especially where the earlier frozen S2 row had already classified the same one-wedge-versus-joint-K5 distinction.

## ERRATUM_CHECK

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`. Historical Iter077E/F source-dependent siblings remain quarantined.

A separate nonmaterial bibliographic error is present in the Iter080K source matrix: it labels the arXiv paper date as `May 10, 2026`, while the arXiv record gives submission date `27 Apr 2026`. This does not alter the scientific source characterization and is not the basis of the verdict.

## BOUNDARY_COMPLETENESS_CHECK

No representative boundary state or special component is used to claim a physical K5 selector. The source audit remains at the source-definition level. Boundary incompleteness does not drive the verdict.

## DISTRIBUTIONAL_CHECK

Iter080K correctly refuses to identify unique one-wedge Toller splitting with a unique simultaneous ten-wedge distributional extension. The Iter077Q infinite-dimensional tangential ambiguity therefore remains untouched.

The absence of an explicit joint-K5 prescription in `2604.24945` is corroborative of the already-authoritative Iter080E/Iter077K source record, not a newly opened source route.

## REGULATOR_CHECK

The source-authorized `i epsilon` prescription remains one-wedge/reduced-Toller authority. No joint K5 regulator, correlated boundary value, order-of-limits theorem or regulator-independence result is supplied or inferred.

## COUNTEREXAMPLE_ATTEMPTS

1. **Novel-source trigger attack:** succeeds. `2604.24945` is explicitly present in the Iter080E preregistration and source snapshot, so the Iter080K statement that it was not represented is factually false.
2. **Changed-authority rescue:** rejected for the frozen Iter080K object. Iter080K cites the same arXiv identifier/version already frozen by Iter080E and does not preregister a published-version delta.
3. **Sharper-reading rescue:** rejected as an admissibility repair. Sharper extraction of one-wedge uniqueness/non-representation facts may be useful corroboration but does not transform an already-audited source into a genuinely additional primary authority.
4. **Scientific-source-characterization attack:** rejected. Independent reading confirms the one-wedge uniqueness and non-representation facts, and no explicit joint-K5 extension law was found.
5. **Representation-composition rescue:** explicitly rejected by the source itself because Toller matrices are not representations.
6. **One-wedge-to-joint uniqueness promotion:** rejected. No theorem in the audited source provides that bridge.

## SURROGATE_CHECK

No K4/Hodge/scalar surrogate is promoted. The target remains the actual source-ordered K5 extension problem and the Iter077Q function-space ambiguity.

## OVERCLAIM_CHECK

The Researcher interpretation ceiling is otherwise appropriate. However `CURRENT` must not retain Iter080K as an **authoritative new-primary-authority gate**. Its source facts can be retained as non-authoritative corroboration/refinement of the already represented S2 source row.

Iter080J is independently `CONFIRMED_SCOPED` by `results/ITER080J_ADVERSARIAL_REVIEW.md`, commit `3e7430110d7c297b097555510a91ca1722ad90cf`.

## VERDICT

`INVALID_PROVENANCE`

## QUALIFICATIONS

- This verdict does **not** reverse the physical blocker. The joint-K5 selector remains missing under Iter077Q/Iter077K plus repaired Iter080E and confirmed Iter080H/I/J.
- The source characterization inside Iter080K is substantially correct; what fails is the frozen novelty/admissibility premise that authorized the gate.
- Historical Iter080K run/artifacts/result should remain preserved for provenance but must not be promoted as a new authoritative source result.
- The bibliographic date error is nonmaterial and separate from the decisive false-new-authority trigger.
- The final published article `Phys. Rev. D 114, 046014` (13 Aug 2026) is a distinct publication record. It has **not** been established here that its final text is materially revised relative to arXiv:2604.24945 v1; publication alone must not be treated as changed scientific authority without a prospective version-delta audit.

## UPDATED_CRQN_CHAIN

`carrier/source F1-F8 -> local source-ordered K5 off-collision object -> non-L1 common collision -> Iter077Q infinite-dimensional source-compatible tangential extension ambiguity -> Iter080A finite K5 permutation covariance DOES NOT SELECT -> repaired Iter080D fixed finite scalar-linear conditions DO NOT SELECT -> repaired Iter080E frozen BCG/Beltran corpus (including 2604.24945) HAS NO P1-P5-COMPLETE JOINT-K5 SELECTOR -> Iter080H pre-Iter077Q CRQN corpus HAS NO A1-A5-COMPLETE FULL-W SELECTOR (CONFIRMED_SCOPED) -> Iter080I current CRQN v0.2 local amplitude BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE (CONFIRMED_SCOPED) -> Iter080J ordinary conormal/WF admissibility alone DOES NOT SELECT (CONFIRMED_SCOPED) -> Iter080K historical source refinement INVALID_PROVENANCE because its claimed NEW_PRIMARY_AUTHORITY was already in Iter080E -> actual new/revised authority or independently motivated stronger joint-function-space selector ?`.

## AUTHORIZED_NEXT_GATE

Do not repair Iter080K by merely relabeling the same source as new or by repeating the frozen BCG/Beltran census.

Highest-value admissible routes are:

1. **Published-version delta route, only if the exact final primary text can be obtained:** prospectively freeze a `BCG_PRD114_046014_VERSION_DELTA_JOINT_K5_AUTHORITY_AUDIT` comparing the final published version against the already-audited arXiv:2604.24945 version. It becomes a `NEW/REVISED_PRIMARY_AUTHORITY` route only if a material source change relevant to P1-P5 is demonstrated. If no material change exists, stop without another selector scan.
2. **Independent stronger-law route:** prospectively freeze an independently motivated actual joint-function-space condition (specific correlated boundary-value, differential/transport, spectral, positivity, composition/RG or equivalent law) that acts on tangential coefficient functions. Motivation must pre-exist the outcome of its test and must not be manufactured from the current blocker.

Absent either route, leave CRQN v0.2 local amplitude blocked. Causal multivertex E3/E4/E6 may resume only on genuinely changed primary authority; E7/E8, G3, regulator independence and RG remain downstream locked.