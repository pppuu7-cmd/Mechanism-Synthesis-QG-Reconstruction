# Iter080E-SM — Joint-K5 function-space selector primary-source audit result

**Date:** 2026-09-14

## Frozen contract and provenance

- prospective preregistration: `prereg/ITER080E_SM_JOINT_K5_FUNCTION_SPACE_SELECTOR_SOURCE_AUDIT.md`, commit `f1a465a059f7c4da8270bed8021f920013b7f5da`
- source snapshot: `sources/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_SNAPSHOT.md`, commit `d51f7cc0f6970670cef1e73223b30cb70b00b8c0`
- machine source matrix: `analysis/iter080e_sm_joint_k5_selector_source_matrix.json`, commit `57de797b4db6c179a9dea7c05ef45dc0ae05f990`
- initial implementation: `analysis/iter080e_sm_joint_k5_selector_source_audit.py`, commit `5b438cfc54cfe218add8fdbe4b32269c26a763a6`
- workflow: `.github/workflows/iter080e_sm_joint_k5_selector_source_audit.yml`, commit/head `542d81dc53d4b9afae5bab3d08ad0d01da0727c2`

The exact audited object was a source-derived **correlated joint-K5 extension selector** acting on the full authoritative Iter077Q tangential ambiguity space

`W = span_C { Q^n F_SU2 delta_N : n >= 0 }`

and respecting source ordering

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

A real primary-source selector had to satisfy all five prospectively frozen predicates: `P1_JOINT_K5`, `P2_SOURCE_ORDER`, `P3_FULL_OBJECT_REACH`, `P4_FUNCTION_SPACE_UNIQUENESS`, and `P5_REGULATOR_BRANCH_AUTHORITY`.

## Initial production run — non-authoritative implementation failure

Initial run `34831623440`, head `542d81dc53d4b9afae5bab3d08ad0d01da0727c2`, terminated `failure` before aggregate authority. Lane D failed only because two dependency locks were implemented as brittle natural-language substrings against `status/CURRENT.md`. No scientific verdict is assigned to this run; lane partial values are non-authoritative.

The control-only repair was frozen in `status/ITER080E_CONTROL_ONLY_REPAIR_PLAN.md`, commit `18cc3355d86d02b1705ce593a73560409c6e460a`. It changed no hypothesis, object, source corpus, selector predicate, control, PASS/FAIL/BLOCKED criterion, or interpretation ceiling. The two brittle prose matches were replaced by exact durable Iter080A and repaired Iter080D classification identifiers.

Repaired implementation commit: `ff8b1b1c4eaff1d91ad0e71f5932991b0fae81c3`.

## Authoritative terminal execution

Authoritative repaired run: `34831723415`, head `ff8b1b1c4eaff1d91ad0e71f5932991b0fae81c3`.

All required lanes and aggregate completed successfully:

- Lane A source coverage job `103936364224`: `PASS_SOURCE_COVERAGE`
- Lane B selector predicates job `103936364455`: `BLOCKED_OBJECT_DEFINITION`
- Lane C classifier controls job `103936364066`: `PASS_CLASSIFIER_CONTROLS`
- Lane D dependency provenance job `103936364289`: `PASS_DEPENDENCY_LOCK`
- aggregate job `103936438154`: success

Artifacts and digests:

- Lane A: artifact `10342502693`, `sha256:6a0bc056d524d9f9a833fdef8ca9b3c20e91586807340fdf55213572127cd9b6`
- Lane B: artifact `10342313058`, `sha256:0acd16487d54680887df42e91606bf3869d73837f0b604343de7fb1df085cc57`
- Lane C: artifact `10342551437`, `sha256:bef4ca1c95302f6f507e9b32319bdaea40115686ad017ace46fa380822ab2ae8`
- Lane D: artifact `10341873858`, `sha256:f3bed004b5789cbde61c353e0a6284e906d212d29e49bf86b8f5d282f2e18f69`
- aggregate: artifact `10342288214`, `sha256:deb957247a902aa92f6c432639da02c9c8492ca54edfd430b3e94ad7a6ed42e6`

Durable aggregate: `analysis/iter080e_sm_aggregate_result.json`, commit `c99451e73cda9cafe63ee082a6eaf139769b79a0`.

## Result

**Verdict:** `BLOCKED_OBJECT_DEFINITION`.

**Classification:**

`ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED`

The complete frozen primary causal/Toller corpus represented in-repo has no real source record satisfying all P1-P5. `eligible_real_primary_sources = []`.

Source-specific result:

- **BCG arXiv:2601.23162:** Eq. (3) supplies the physical one-wedge spectral Toller branch and Eq. (4) supplies the formal ten-Toller single-vertex product/group-integral formula. That formal full local-vertex expression is not accompanied by an explicit correlated joint-K5 distributional extension, finite part, contour, interchange theorem, or uniqueness prescription acting on the Iter077Q common-collision function-space ambiguity.
- **BCG arXiv:2604.24945:** the represented exact Toller-matrix identities strengthen the one-wedge/local analytic source lock but do not define a correlated joint-K5 extension selector on the full Iter077Q `W`.
- **Beltran arXiv:2603.22661v2:** arbitrary-oriented-2-complex causality and generalized causal local vertices are source-explicit, but the represented source does not provide the missing joint Iter077Q collision-extension selector or uniqueness theorem.

Therefore the currently source-defined CRQN v0.2 local causal amplitude still lacks a unique joint-K5 function-space extension selector. The published one-wedge spectral `i epsilon` is retained exactly as source authority; it is not promoted to a joint K5 regulator/selector without a theorem.

## Scientific effect

This gate closes the most direct source-rescue route left after Iter077Q, Iter080A and repaired Iter080D: the already frozen BCG/Beltran primary corpus does not contain a hidden function-valued/differential/spectral/microlocal joint-K5 selector satisfying the full object requirements. Repeating the same source scan without genuinely new or revised primary authority has no information value.

The independent physical composition blockers E3/E4/E6 remain `BLOCKED_SOURCE_BRIDGE`; E7/E8 remain downstream of both the local extension definition and composition bridge. G3, regulator removal, RG/E9, continuum geometry, spin-2, Einstein recovery, matter/QFT IR and predictions remain locked.

## Interpretation ceiling

This is a source-object-definition obstruction for the frozen corpus, **not** a theorem that no mathematically valid selector can exist, that the causal vertex does not exist as a distribution, or that the full amplitude diverges. It does not justify inventing a selector post hoc. A new selector would require either genuinely new/revised primary authority or an independently motivated, prospectively testable candidate-version mechanism.

Claim locks remain unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no G3 PASS; no F9/G8/K5 promotion; retain published one-wedge spectral `i epsilon`.

## Next admissible Researcher gate

Do not run another frozen-primary-source selector scan. The next high-information anti-rescue gate is a prospective census of the **pre-existing CRQN v0.2 model/axiom specification** for an independently motivated full-function-space selector already present before the Iter077Q obstruction was known. If no such pre-existing mechanism exists, record that CRQN v0.2 remains blocked at the local-amplitude arrow until genuinely new/revised primary authority or a separately motivated prospective candidate version is introduced. Do not manufacture a selector as a repair of this result.
