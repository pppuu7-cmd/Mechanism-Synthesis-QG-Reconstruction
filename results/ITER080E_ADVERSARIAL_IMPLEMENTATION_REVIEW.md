# Iter080E-SM adversarial implementation review

**Date:** 2026-09-14

## RESULT_REVIEWED

Latest terminal substantive Researcher result at review start: `Iter080E-SM — Joint-K5 function-space extension selector primary-source audit`, durable result `results/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_AUDIT_RESULT.md`, result commit `f3cc75c2aba3eee9677a6d0ca8b6bd0d358397bc`.

Researcher claimed verdict: `BLOCKED_OBJECT_DEFINITION`.

Researcher classification:
`ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED`.

Frozen contract: `prereg/ITER080E_SM_JOINT_K5_FUNCTION_SPACE_SELECTOR_SOURCE_AUDIT.md`, commit `f1a465a059f7c4da8270bed8021f920013b7f5da`.

## SOURCE_OBJECT_CHECK

The frozen object is correct and physical for this layer: a source-derived correlated joint-K5 extension selector acting on the full authoritative Iter077Q tangential ambiguity space

`W = span_C { Q^n F_SU2 delta_N : n >= 0 }`

under the source order

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

No scalar K4/K5 incidence surrogate is substituted for this object.

The represented source record is consistent with the already-authoritative negative source facts: Iter077K records that BCG `2601.23162` and `2604.24945` do not provide a correlated joint-K5 boundary-value/extension prescription, and Iter079A records that Beltran `2603.22661v2` does not address/select the Iter077Q common-collision extension freedom. Those facts make the Researcher conclusion plausible, but they do not cure the executable defect below.

## SOURCE_ORDERING_CHECK

The preregistration and written result preserve the authoritative source ordering. The result does not replace the source-ordered ten-Toller object by termwise `theta/delta/delta'` products, does not use a Hörmander failure as a full-vertex failure theorem, and does not promote one-wedge Toller uniqueness into a joint-K5 uniqueness theorem.

No source-order counterexample was found against the written ceiling.

## PROVENANCE_CHECK

Prospective chronology is intact:

- prereg `f1a465a059f7c4da8270bed8021f920013b7f5da`;
- source snapshot `d51f7cc0f6970670cef1e73223b30cb70b00b8c0`;
- machine source matrix `57de797b4db6c179a9dea7c05ef45dc0ae05f990`;
- initial implementation `5b438cfc54cfe218add8fdbe4b32269c26a763a6`;
- workflow/head `542d81dc53d4b9afae5bab3d08ad0d01da0727c2`;
- initial run `34831623440`, failed before aggregate and correctly quarantined;
- control-only Lane-D repair plan `18cc3355d86d02b1705ce593a73560409c6e460a`;
- repaired head `ff8b1b1c4eaff1d91ad0e71f5932991b0fae81c3`;
- terminal repaired run `34831723415`.

Run `34831723415` is terminal `success`. Jobs A `103936364224`, B `103936364455`, C `103936364066`, D `103936364289`, aggregate `103936438154` all completed. Aggregate artifact `10342288214` has digest `sha256:deb957247a902aa92f6c432639da02c9c8492ca54edfd430b3e94ad7a6ed42e6`.

The implementation defect is not chronology contamination and therefore is not `INVALID_PROVENANCE`.

## ERRATUM_CHECK

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains blob `63356e5099929f2b21d9d7296ab97f15ff163dba` and contains the controlling formula

`delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)`, `D=rho^2+1/4`.

Historical Iter077E/F source-dependent siblings remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`. Iter080E does not rely on or revive their incorrect contact transcription.

## BOUNDARY_COMPLETENESS_CHECK

The gate does not select a representative boundary state and does not compute a reduced scalar component. Its intended selector must act on the full Iter077Q ambiguity space and reach the ten-wedge product, full boundary contraction, and K5 extension/integration stage.

The executable implementation, however, never independently establishes `P3_FULL_OBJECT_REACH`; it consumes a preassigned matrix status and checks only that a matching status label appears in the newly authored Iter080E source snapshot.

## DISTRIBUTIONAL_CHECK

No new distributional product is constructed in this audit. The critical defect is executable source inference.

The frozen `INVALID` clause explicitly requires `INVALID_IMPLEMENTATION` if the code merely trusts prefilled verdict booleans/statuses without testing the frozen predicates/evidence structure.

Production Lane B does exactly that:

1. it reads each P1-P5 `status` from `analysis/iter080e_sm_joint_k5_selector_source_matrix.json`;
2. for each predicate it checks only that the matrix's `anchor` string is present in the corresponding section of `sources/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_SNAPSHOT.md` and that the prefilled `status` text occurs inside that anchor;
3. it then determines selector eligibility solely by whether the five prefilled statuses equal the literal `EXPLICIT`.

Thus `evidence_ok=true` means only that an Iter080E-authored status label is textually self-consistent with another Iter080E-authored file. Lane A verifies Git blob identities of older source-evidence files, but it does not parse those files for P1-P5 evidence and Lane B never reads them at all.

This is a circular classifier, not an executable test of the frozen primary-source predicates. A status/anchor pair can be changed consistently in the matrix and Iter080E snapshot without changing any frozen primary-evidence blob, and Lane B would follow the changed label. The scientific output therefore depends on preassigned labels rather than source evidence.

## REGULATOR_CHECK

The written scientific conclusion correctly retains published one-wedge spectral `i epsilon` only in its source scope and does not claim a correlated joint-K5 regulator, common finite part, contour, interchange theorem, or regulator independence.

The implementation defect is orthogonal to this regulator ceiling.

## COUNTEREXAMPLE_ATTEMPTS

1. **Circular-label witness — succeeds.** Lane B's five `evidence_ok` values become true by finding status labels authored in the Iter080E snapshot itself; older source files are not inspected by Lane B. Therefore green Lane B does not establish any P1-P5 source fact.
2. **Primary-evidence mutation independence — succeeds as an implementation witness.** Eligibility is computed from matrix statuses; the code only checks older evidence-file hashes in Lane A. The actual content of those files does not enter the Lane-B predicate classifier.
3. **Positive/negative classifier controls — insufficient.** Lane C proves only that `selector_eligible()` maps five `EXPLICIT` strings to eligible and the supplied non-EXPLICIT control strings to ineligible. It does not validate extraction of scientific statuses from primary evidence.
4. **BCG formal Eq. (4) rescue — rejected.** Existing Iter077K authority already distinguishes a formal ten-Toller vertex expression from a correlated joint-K5 extension/limit theorem.
5. **One-wedge Toller uniqueness rescue — rejected.** One-wedge spectral/projector uniqueness does not select a common-collision K5 extension.
6. **Beltran generalized-vertex rescue — rejected.** Existing Iter079A authority explicitly leaves the Iter077 common-collision selector/transport problem unaddressed.
7. **Representative-boundary rescue — not used.** No post-hoc boundary component is selected.

No scientific counterexample showing that a qualifying selector actually exists in the frozen source corpus was found. The invalidation is implementation/provenance-of-inference, not a positive selector discovery.

## SURROGATE_CHECK

No K4/Hodge/BCH scalar surrogate is used. The surrogate defect is instead epistemic: the machine-readable Iter080E status matrix plus its self-authored textual anchors substitutes for direct source-evidence evaluation. Under the preregistration this substitution is not authoritative.

## OVERCLAIM_CHECK

The written interpretation ceiling is otherwise narrow, but two downstream promotions are not currently authorized:

- Iter080E may not be called an authoritative `BLOCKED_OBJECT_DEFINITION` source census until the source-predicate implementation is repaired;
- the repository may not use Iter080E to forbid repetition of the source census or to claim the full frozen primary corpus has been executable-confirmed P1-P5-incomplete.

The physical K5 local-amplitude blocker nevertheless remains independently active from Iter077Q/Iter077K/Iter080A/repaired Iter080D. Invalidating Iter080E does not unblock the amplitude and does not improve CRQN readiness.

## VERDICT

`INVALID_IMPLEMENTATION`

## QUALIFICATIONS

This verdict does not assert that BCG/Beltran contains a hidden selector. Existing authoritative Iter077K and Iter079A source audits support the narrower negative facts that the known one-wedge/local/generalized causal constructions do not themselves supply the missing joint-K5 extension prescription.

The defect is that Iter080E's executable P1-P5 classifier does not derive those statuses from frozen source evidence as required by its own preregistration. Historical run `34831723415`, artifacts and result note remain preserved for provenance but are non-authoritative for the Iter080E classification pending a control-only repair.

A control-only repair is admissible under the unchanged Iter080E preregistration. It must not change the source corpus, object, P1-P5 criteria, PASS/FAIL/BLOCKED rules or ceiling.

## UPDATED_CRQN_CHAIN

`carrier/source mechanism F1-F8` -> `source-ordered local K5 off-collision object` -> `non-L1 common-collision behavior` -> `same-scaling-degree extensions exist` -> `Iter077Q infinite-dimensional source-compatible tangential ambiguity` -> `Iter080A finite K5 permutation covariance DOES NOT SELECT (CONFIRMED_SCOPED)` -> `Iter080D fixed finite scalar-linear conditions DO NOT SELECT (CONFIRMED_SCOPED)` -> `Iter080E primary-source P1-P5 census INVALID_IMPLEMENTATION pending repair` -> `pre-existing CRQN v0.2 independent selector axiom ?` -> `unique local amplitude ? BLOCKED` -> `causal many-vertex E3/E4/E6 source bridge ? BLOCKED` -> `E7/E8 transport ?` -> `G3 ?` -> `finiteness/regulator removal ?` -> `RG/E9 ?` -> `continuum 3+1 Lorentzian geometry ?` -> `massless spin-2 ?` -> `Einstein/GR recovery ?` -> `matter/QFT IR ?` -> `normalized falsifiable prediction ?`.

## AUTHORIZED_NEXT_GATE

First priority is a **control-only Iter080E repair/retry under the unchanged preregistration**. Lane B PASS/BLOCKED must depend on direct frozen source-evidence anchors or a prospectively frozen source-audit evidence structure whose factual anchors are source-specific, not on the Iter080E matrix's own prefilled P1-P5 labels. At minimum:

- verify each cited older source-evidence blob by SHA;
- for every P1-P5 status, bind the status to explicit source-specific factual anchors in those frozen evidence blobs (or to an independently frozen source-audit statement), not to `P*_... = STATUS` text authored for Iter080E;
- make eligibility depend on those evidence checks;
- retain synthetic controls only as classifier controls, not source evidence;
- preserve the historical failed run and the now-invalid repaired run unchanged.

If the repaired execution again yields no P1-P5-complete real source row, `BLOCKED_OBJECT_DEFINITION` can be restored. Only after that confirmation may Researcher proceed to the anti-rescue `CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS`. Until then do not run a competing authoritative gate on the same source-census object, and keep E7/E8, G3, regulator independence and RG downstream-locked.