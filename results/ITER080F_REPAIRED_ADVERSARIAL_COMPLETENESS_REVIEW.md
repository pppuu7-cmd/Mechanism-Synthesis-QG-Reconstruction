# Iter080F-SM repaired execution — adversarial completeness review

**Date:** 2026-09-14

## Reviewed authority

Reviewed the repaired Researcher claim in `results/ITER080F_SM_CONTROL_ONLY_IMPLEMENTATION_REPAIR_RESULT.md`, commit `97980ecf17e60392389f519f70fb6629dc82a1dc`, based on production head `71b5551c034506b7bb0c07bf222d08d7756f31ca` and run `34841351539`.

Original scientific preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`.
Control-only repair plan: `4b5e1d1638f366e8384fef3a03da59db9c42dde6`.

Researcher classification:
`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.
Researcher verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

## Terminal execution / artifact identity

Run `34841351539` is terminal `success` at exact head `71b5551c034506b7bb0c07bf222d08d7756f31ca`.

Jobs:

- Lane A `103966834681` — success;
- Lane B `103966834664` — success;
- Lane C `103966834585` — success;
- Lane D `103966834678` — success;
- aggregate `103966883834` — success.

Artifacts:

- A `10345649802`, digest `sha256:cf806e51999dc093555f02e0d158b02f036da8518eb6c40a70ed96d7bc4a77bd`;
- B `10345799538`, digest `sha256:bbd7e6811c525ad8ac3bf70e91a4a3b8e3b7abec63256b1d7a065602257106fa`;
- C `10345904100`, digest `sha256:f85599b41d18d464cf2a74bc6d20a30df8a41245a5db89b65de122874609bee4`;
- D `10346401464`, digest `sha256:2470f900e5b896922473bd01f875d6ad3b13529d2c2c633322c5b1ea7d389904`;
- aggregate `10346645528`, digest `sha256:8dffd7c2804e12cafb875721b6c322169404f2a44c2c00167c967b511d4f8c54`.

Green execution is therefore established. It is not by itself scientific authority.

## Frozen contract attacked

The original preregistration requires Lane B to parse/audit **every candidate statement plausibly relevant** to amplitude uniqueness, normalization, composition, RG, gauge/refoliation, analyticity/unitarity and finite `Phi`, with exact frozen-text anchors and A1-A5 values.

After the first Critic invalidation, the prospective repair plan strengthened this requirement: Lane B must use an auditable coverage manifest spanning **every frozen-corpus statement plausibly relevant** to the listed categories. An uncovered required anchor must make Lane B implementation-invalid.

The frozen positive-evidence corpus remains exactly:

- `candidates/CANDIDATE_A_CRQN.md`, blob `a3023dadb75f4c53d0c44a6de1c46958f4149178`;
- `candidates/CANDIDATE_A_CRQN_V0_2.md`, blob `3933c110f9bafabb6593f8301029adaa25458bb2`.

The target remains full Iter077Q function space `W`; A1-A5 and the interpretation ceiling are unchanged.

## Decisive executable defect — self-referential completeness

The final Lane-B implementation defines a hand-authored `REQUIRED_COVERAGE_ANCHORS` list of 42 strings and then declares coverage complete exactly when every string in that same list is present in a candidate blob and represented in a census row.

Schematically the executable test is:

`REQUIRED_COVERAGE_ANCHORS -> represented anchors -> uncovered=[] -> coverage_complete=true`.

There is no independent executable operation that derives or verifies that `REQUIRED_COVERAGE_ANCHORS` itself exhausts the preregistered universe of plausibly relevant candidate statements. Therefore the program can return `coverage_complete=true` while omitting a relevant statement from the hand-authored manifest. That is precisely the failure mode the repair plan was intended to prevent.

This is not a philosophical objection to a finite manifest. It is an explicit mismatch between the frozen requirement (“every ... plausibly relevant statement”) and the executable predicate (“every anchor I manually put in this list”).

## Concrete omitted relevant witnesses

Direct comparison against the two frozen blobs gives explicit witnesses that are plausibly relevant under the preregistered categories but absent from the final 42-anchor manifest and final 35-row census as distinct audited statements.

From CRQN v0.1:

1. the actual history-amplitude formula
   `A[B_f,B_i] = Sum_H (1/|Aut(H)|) W_causal[H] W_geom[H] W_matter[H]`;
2. the alternate microscopic-history expression
   `Z = Sum_H integral dmu(lambda) exp(i S_micro[H,lambda]) Chi_causal(H)`;
3. the explicit RG effective-functional target, including `Gamma_k` and the finite-dimensional UV critical-surface statement;
4. the schematic functional flow `k dGamma_k/dk = B[Gamma_k]` and fixed-point equation `B[Gamma_*]=0`;
5. the early-success criterion requiring an explicitly defined microstate/amplitude pair.

From CRQN v0.2:

6. the explicit local-vertex placeholder
   `A_v^CRQN = A_v^geom(j,i) F_causal(o;j,i;theta)`.

These statements need not qualify as selectors. In fact, adversarial reading finds no A1-A5-complete selector in them. The defect is that the frozen gate required them to be audited when plausibly relevant, whereas the final executable completeness certificate cannot detect their omission.

## First-repair-run counterexample to the final completeness claim

The issue is strengthened by the immediately preceding repair run `34841208883` at head `f435f0a0edf88c83c21eb830e052d9d49ba50f2f`.

That Lane B failed with `coverage_complete=false` and emitted a machine list of uncovered candidate lines. The output included both obvious false positives and materially relevant lines. Among the latter were the v0.1 `Gamma_k` effective-functional/UV-critical-surface statement and the v0.2 local-vertex placeholder. The first implementation also attempted to audit the v0.1 history-amplitude ansatz but failed an overly brittle exact anchor.

The final implementation at `71b555...` then replaced the broad relevance check with a manually selected 42-anchor manifest after this failed output had been observed. It retained some newly exposed relevant lines but omitted other clearly relevant ones listed above.

Thus the final `coverage_complete=true` is not an independent corpus-completeness certificate; it is consistency with a post-failure hand-selected manifest.

This creates a provenance warning about partial-result-informed manifest narrowing. The mandatory verdict below does not need to rely on that warning because the final executable has an independently demonstrable completeness defect.

## Controls that do survive review

Lane C is materially repaired relative to the historical invalid implementation:

- synthetic full-function selector is tested predicate-by-predicate;
- finite scalar control explicitly has A2=false and A3=false;
- aspirational RG/gauge control explicitly has A1=false, A2=false and A3=false;
- the post-Iter077Q dependency-isolation replay is actually executed, with removal/replay/fingerprint/restore rather than a hard-coded Boolean.

Lane A timezone normalization and Lane D claim/dependency lock are also consistent with the repair plan.

Therefore the review does not invalidate every lane; Lane B alone is sufficient to invalidate the repaired aggregate authority.

## Source / physical firewalls

Iter080F remains an anti-rescue candidate-specification census. It does not alter authoritative source ordering:

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

No scalar K4/K5/Hodge/BCH surrogate is promoted. No termwise `theta/delta/delta'` product is substituted for the source-ordered full Toller object. No representative boundary state, special spin sector, saddle-only result, regulator path or one-wedge `i epsilon` is used as a full-K5 selector.

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical source-dependent Iter077E/F siblings remain quarantined.

## Scientific consequence

The repaired Iter080F result cannot be used as authoritative proof that the pre-Iter077Q CRQN v0.1/v0.2 corpus contains no A1-A5-complete selector.

This does **not** provide a selector and does **not** rescue CRQN. Direct adversarial reading of the omitted witnesses still finds no explicit operation on the whole Iter077Q ambiguity space with unique selection power. Upstream authority remains:

- Iter077Q: infinite-dimensional source-compatible K5 extension ambiguity;
- Iter080A: finite K5 permutation covariance does not select (`CONFIRMED_SCOPED`);
- repaired Iter080D: fixed finite scalar complex-linear conditions do not select (`CONFIRMED_SCOPED`);
- repaired Iter080E: frozen BCG/Beltran causal-Toller corpus contains no P1-P5-complete joint-K5 selector (`BLOCKED_OBJECT_DEFINITION`, scoped);
- Iter080B: causal multivertex E3/E4/E6 remains `BLOCKED_SOURCE_BRIDGE`.

Unique local amplitude therefore remains blocked independently of Iter080F.

## VERDICT

`INVALID_IMPLEMENTATION`

This verdict is intentionally narrower than `INVALID_PROVENANCE`: even if the post-failure manifest rewrite is treated as an admissible implementation repair, the final Lane-B executable still does not test the frozen completeness requirement.

## Required successor / no third post-hoc manifest patch

Do not launch `CRQN_V0_2_LOCAL_AMPLITUDE_ANTI_RESCUE_SURVIVAL_DECISION` from the repaired Iter080F result.

A further hand-edit of `REQUIRED_COVERAGE_ANCHORS` under the same already-inspected repair sequence would not cure the epistemic problem. The next admissible gate should be a **new prospectively preregistered successor census** with the candidate-statement universe and relevance/exclusion rule frozen before any production execution.

At minimum it must prospectively bind every non-heading paragraph/list/formula block of both frozen candidate blobs to a stable statement ID, then either classify it A1-A5 or exclude it by a pre-frozen machine-checkable relevance rule/reason. The manifest itself must be hashed/frozen before the first production run. The omitted witnesses above must be explicitly classified. A failed production run must not be repaired by narrowing the statement universe after inspecting substantive output; such a change requires another prospective successor.

Until that successor is terminal and independently reviewed, Iter080F remains non-authoritative and all downstream gates requiring its anti-rescue conclusion stay locked.