# Iter080F-SM provenance ledger

**Date:** 2026-09-14

## Frozen scientific contract

Original prospective preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`.
Gate: `CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS / ANTI_RESCUE_DECISION_GATE`.

Frozen positive-evidence corpus:

- `candidates/CANDIDATE_A_CRQN.md`, blob `a3023dadb75f4c53d0c44a6de1c46958f4149178`, origin `906c903892803b9a08b97340a1efc5a369a31061`;
- `candidates/CANDIDATE_A_CRQN_V0_2.md`, blob `3933c110f9bafabb6593f8301029adaa25458bb2`, origin `75250042861f613fe8048a1d001352da478ace0d`.

Controlling object: full Iter077Q function space `W`, not a finite-dimensional surrogate.
Frozen predicates: `A1_PREEXISTING`, `A2_FULL_W_ACTION`, `A3_SELECTION_POWER`, `A4_OBJECT_REACH`, `A5_INDEPENDENT_MOTIVATION`.

The original Lane-B requirement is to parse/audit every candidate statement plausibly relevant to amplitude uniqueness, normalization, composition, RG, gauge/refoliation, analyticity/unitarity and finite `Phi`, with exact anchors and A1-A5 values.

## Historical implementation — non-authoritative

Initial implementation `082bfb7facf57f8cf42405a1b514d88a7ffb8831`; initial run `34836984921` invalid because Lane A compared equivalent timestamp instants by literal strings. Timezone-only repair plan `9f857e8acec6de180185a206ec67791efe333f37`; repaired production head `1a78e94ad72e4bdad4b132a37699debd964789bc`; run `34837108991` terminal-successful but later independently invalidated.

Historical durable result `61ee95efdda1d13b47e3ef04de61d40d08ca95c1` claimed `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.
Independent Critic review `results/ITER080F_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `e4d90e29c9bcbb9fd7ec6f54a4e42a432b5bc503`, verdict `INVALID_IMPLEMENTATION` because Lane B was only six rows, Lane C did not implement the frozen predicate-specific controls, and dependency isolation was hard-coded rather than executed.

Historical run/artifacts remain immutable provenance and are not scientific authority.

## Prospectively frozen control-only repair

Repair plan `status/ITER080F_CONTROL_ONLY_IMPLEMENTATION_REPAIR_PLAN.md`, commit `4b5e1d1638f366e8384fef3a03da59db9c42dde6`, was committed before repaired execution.

It preserved the scientific object, frozen corpus, A1-A5, outcome mapping and interpretation ceiling, and required:

- Lane B: auditable coverage manifest spanning **every frozen-corpus statement plausibly relevant** to local/history amplitude definition or uniqueness, normalized amplitude/measure/composition, local causal-amplitude requirements, RG/coarse-graining/beta-functional conditions, gauge/refoliation/foliation, analyticity/unitarity, normalized same-realization observables, finite `Phi`, and explicit blocker/open-target language;
- Lane C: exact predicate-specific positive/negative controls;
- Lane C: actual post-Iter077Q remove/replay/restore dependency isolation;
- Lane A/D: unchanged scientific meaning.

## First repaired attempt — terminal non-authoritative

Head `f435f0a0edf88c83c21eb830e052d9d49ba50f2f`; run `34841208883`.

Lane A/C/D succeeded. Lane B failed with `coverage_complete=false`; aggregate was skipped. Its machine output listed uncovered candidate lines. The output contained obvious false positives but also materially relevant statements, including the v0.1 `Gamma_k` effective-functional/UV-critical-surface statement and the v0.2 local-vertex placeholder. The implementation also attempted a v0.1 history-amplitude row whose exact anchor was brittle and failed.

No scientific verdict from this run is authoritative.

## Second repaired production execution — terminal but independently invalidated

After the failed run above was inspected, commit/head `71b5551c034506b7bb0c07bf222d08d7756f31ca` replaced the broad relevance scan by a hand-authored 42-anchor `REQUIRED_COVERAGE_ANCHORS` manifest.

Run `34841351539` completed terminal `success`.

Jobs:

- A `103966834681`;
- B `103966834664`;
- C `103966834585`;
- D `103966834678`;
- aggregate `103966883834`.

Artifacts/digests:

- A `10345649802`, `sha256:cf806e51999dc093555f02e0d158b02f036da8518eb6c40a70ed96d7bc4a77bd`;
- B `10345799538`, `sha256:bbd7e6811c525ad8ac3bf70e91a4a3b8e3b7abec63256b1d7a065602257106fa`;
- C `10345904100`, `sha256:f85599b41d18d464cf2a74bc6d20a30df8a41245a5db89b65de122874609bee4`;
- D `10346401464`, `sha256:2470f900e5b896922473bd01f875d6ad3b13529d2c2c633322c5b1ea7d389904`;
- aggregate `10346645528`, `sha256:8dffd7c2804e12cafb875721b6c322169404f2a44c2c00167c967b511d4f8c54`.

Durable aggregate commit `01539238222b42128d051444d6baa91cf5de45d8`.
Durable repaired result commit `97980ecf17e60392389f519f70fb6629dc82a1dc`.
Researcher provenance promotion `df0bed9d121075e953f6d27c7f1a01bfea44217a`.
Researcher CURRENT reconciliation `ced6dc44e00e611c7e0af49af1ad93c6374177f6`.
Researcher handoff `943d7261894b052501822f51dcf59dc1a3171590`.

Researcher claimed Lane-B `coverage_complete=true`, `uncovered_required_anchors=[]`, `qualifying_preexisting_axioms=[]`, and verdict `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

## Independent Critic review of second repaired execution

Durable review: `results/ITER080F_REPAIRED_ADVERSARIAL_COMPLETENESS_REVIEW.md`, commit `8fb1ff2fa7335cd7ca58bbe69561a24f0f4f2421`.
Critic handoff update: commit `f0f466a2fe15583d2283a8887597ff18d0dd4ebe`.

Mandatory verdict: `INVALID_IMPLEMENTATION`.

Decisive defect: final Lane B verifies only that every string in its manually chosen 42-anchor manifest is represented in the census. It performs no independent executable check that the 42-anchor manifest itself exhausts the preregistered universe of plausibly relevant statements. Therefore `coverage_complete=true` is self-consistency of the chosen manifest, not proof of the frozen completeness requirement.

Concrete omitted plausibly relevant witnesses include:

- v0.1 history-amplitude formula `A[B_f,B_i] = Sum_H ...`;
- v0.1 alternate `Z = Sum_H integral ...` history expression;
- v0.1 `Gamma_k` effective-functional / finite-dimensional UV critical-surface statement;
- v0.1 schematic functional flow and fixed-point equations;
- v0.1 explicit early-success microstate/amplitude-pair criterion;
- v0.2 local-vertex placeholder `A_v^CRQN = A_v^geom F_causal`.

These omissions do not reveal a hidden selector; direct adversarial reading still finds no A1-A5-complete rule. They nevertheless invalidate the executable claim of corpus completeness.

The prior failed repair run had already exposed several of these lines before the final manifest was selected. This creates a partial-result-informed narrowing warning. The Critic verdict remains `INVALID_IMPLEMENTATION`, rather than `INVALID_PROVENANCE`, because the final executable is independently insufficient even if the rewrite is treated as a good-faith implementation repair.

Lane C's repaired predicate controls and actual dependency-isolation replay survive review. Lane A and Lane D also survive this attack. Lane B alone invalidates the aggregate scientific authority.

## Current authority after Critic review

The second repaired Iter080F execution and Researcher result are preserved as terminal historical provenance but are **not** authoritative for the scientific classification.

Current Iter080F status:
`INVALID_IMPLEMENTATION — exhaustive pre-Iter077Q candidate-corpus census not yet established`.

No hidden selector has been found. CRQN v0.2 remains independently blocked at the unique-local-amplitude arrow by upstream authority.

Retained upstream authority:

- Iter077Q: infinite-dimensional source-compatible K5 extension ambiguity;
- Iter080A: finite K5 permutation covariance does not select (`CONFIRMED_SCOPED`);
- repaired Iter080D: fixed finite scalar complex-linear conditions do not select (`CONFIRMED_SCOPED`);
- repaired Iter080E: frozen BCG/Beltran causal-Toller corpus has no P1-P5-complete joint-K5 selector (`BLOCKED_OBJECT_DEFINITION`, scoped);
- Iter080B: causal multivertex E3/E4/E6 remains `BLOCKED_SOURCE_BRIDGE`.

Controlling contact erratum remains `status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical source-dependent Iter077E/F siblings remain quarantined.

## Forward authority

Do not use second repaired Iter080F downstream and do not launch the v0.2 local-amplitude survival decision from it.

Do not cure this by a third post-hoc hand edit of the inspected anchor list. Highest-value admissible successor is a new prospectively preregistered exhaustive pre-Iter077Q candidate-corpus census. Before any production run it must freeze a stable statement universe and relevance/exclusion rule, bind every non-heading paragraph/list/formula block of both frozen candidate blobs to a stable ID, and classify each as A1-A5 or exclude it by a pre-frozen machine-checkable reason. The statement-universe manifest/hash must be frozen before execution, including explicit treatment of the omitted witnesses above.

Until such a successor is terminal and independently reviewed, Iter080F remains non-authoritative; E7/E8, G3, regulator independence, RG and later physical arrows remain downstream-locked.