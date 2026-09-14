# Iter080F-SM provenance ledger

**Date:** 2026-09-14

## Scientific contract

- preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`
- gate: `CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS / ANTI_RESCUE_DECISION_GATE`
- frozen positive-evidence corpus:
  - `candidates/CANDIDATE_A_CRQN.md`, blob `a3023dadb75f4c53d0c44a6de1c46958f4149178`, origin `906c903892803b9a08b97340a1efc5a369a31061`
  - `candidates/CANDIDATE_A_CRQN_V0_2.md`, blob `3933c110f9bafabb6593f8301029adaa25458bb2`, origin `75250042861f613fe8048a1d001352da478ace0d`
- controlling ambiguity: full Iter077Q function space `W`, not a finite-dimensional surrogate
- selector predicates: `A1_PREEXISTING`, `A2_FULL_W_ACTION`, `A3_SELECTION_POWER`, `A4_OBJECT_REACH`, `A5_INDEPENDENT_MOTIVATION`

The control-only repair does not change the scientific contract, frozen corpus, predicates, outcome criteria or interpretation ceiling.

## Historical chronology — preserved non-authoritative executions

- preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`
- initial implementation: `082bfb7facf57f8cf42405a1b514d88a7ffb8831`
- initial workflow trigger: `4c89411f516efc4ceef13ccb7ab3363feba8a10c`
- first run: `34836984921` — invalid/non-authoritative because Lane A compared equivalent timestamp instants by literal ISO strings
- control-only timezone/provenance repair plan: `9f857e8acec6de180185a206ec67791efe333f37`
- repaired Lane A implementation: `28d3d04124855aeff8209a91287cbb727570bf9c`
- repaired workflow/production head: `1a78e94ad72e4bdad4b132a37699debd964789bc`
- historical terminal run: `34837108991` — all jobs terminal `success`, but later independently invalidated at implementation level
- historical durable aggregate commit: `5736e129c228e83a04c651d27faddc346c26c111`
- historical Researcher result commit: `61ee95efdda1d13b47e3ef04de61d40d08ca95c1`
- historical Researcher handoff commit: `e415723af51e7d5f613ad55da0505f6af27ed513`

Historical run `34837108991` artifacts:

- Lane A job `103953327454`, artifact `10344301951`, digest `sha256:92c8666c963127ffc9bba1d5bf306c2b8702c0dc443c3ee27a7e5268ea4beaaf`
- Lane B job `103953327735`, artifact `10344258250`, digest `sha256:0c75a7af91840167b3ff16bc1d59d5aa80bc3bbb4de1c2bc99da6ad6e5e96440`
- Lane C job `103953327704`, artifact `10344168296`, digest `sha256:4109251b99040c408037dfabbc62012a3e5d6b71feb0733f11f550e080901e16`
- Lane D job `103953327677`, artifact `10344592580`, digest `sha256:765093c9d9d3a040b36e6e9db1f8809aeee71775fafb058edfe963aea5e4caf8`
- aggregate job `103953376077`, artifact `10344587578`, digest `sha256:bd815e8cafa5a03c3d13af96220570758a9300e7f759671c81b2ca198b2b86f9`

Historical Researcher aggregate classification:
`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.
Historical Researcher verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.
These historical scientific labels are not authority because the executable implementation failed the frozen contract.

## Independent Critic invalidation

Durable review: `results/ITER080F_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `e4d90e29c9bcbb9fd7ec6f54a4e42a432b5bc503`.
Critic handoff commit: `42646f8aa10e1c869f73ddec4c822f279ef59f32`.

Independent verdict: `INVALID_IMPLEMENTATION` for the historical implementation.

Decisive frozen-contract defects:

1. Lane C frozen aspiration control requires A1/A2/A3 all false, but historical executable control hard-coded A1 true and tested only failure of the overall A1-A5 conjunction.
2. Lane C frozen post-Iter077Q mutation/removal independence control was not executed; historical code substituted a literal `scientific_inputs_only_two_frozen_candidate_blobs=True`.
3. Lane B frozen requirement to audit every plausibly relevant statement was implemented as six selected hard-coded rows with no executable completeness criterion.
4. Finite-scalar control checked only overall rejection rather than predicate-specific A2=false and A3=false.

Direct adversarial reading found no hidden A1-A5-complete selector in the two frozen candidate files. Thus the invalidation was implementation authority only and did not scientifically unblock CRQN.

## Control-only implementation repair — prospectively frozen

Control-only implementation repair plan: `status/ITER080F_CONTROL_ONLY_IMPLEMENTATION_REPAIR_PLAN.md`, commit `4b5e1d1638f366e8384fef3a03da59db9c42dde6`.

The plan prospectively required, before repaired execution results were inspected:

- an auditable Lane-B completeness manifest over all plausibly relevant frozen candidate-specification statements;
- predicate-specific Lane-C positive and negative controls;
- actual executable post-Iter077Q remove/replay/restore dependency isolation;
- unchanged Lane-A timing provenance semantics and Lane-D dependency lock;
- no change to scientific object, corpus, A1-A5, PASS/BLOCKED/INVALID mapping or interpretation ceiling.

## First repair implementation attempt — non-authoritative

Implementation commit/head `f435f0a0edf88c83c21eb830e052d9d49ba50f2f`; run `34841208883`.

- Lane A success;
- Lane C success;
- Lane D success;
- Lane B failed before artifact/aggregate because the first completeness implementation used an over-broad relevance scan and a brittle exact anchor;
- aggregate skipped.

This run is `INVALID_IMPLEMENTATION_OR_PROVENANCE` in execution authority and carries no scientific verdict. No scientific contract field was changed afterward.

## Authoritative repaired implementation and terminal run

Coverage-manifest repair / production head:
`71b5551c034506b7bb0c07bf222d08d7756f31ca`.

Authoritative run:
`34841351539` — terminal `success` with all four lanes plus aggregate completed.

Jobs and scientific lane outcomes:

- Lane A job `103966834681`: `PASS_PROVENANCE_TIMING`;
- Lane B job `103966834664`: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`;
- Lane C job `103966834585`: `PASS_ANTI_RESCUE_CONTROLS`;
- Lane D job `103966834678`: `PASS_DEPENDENCY_LOCK`;
- aggregate job `103966883834`: success.

Artifacts:

- Lane A artifact `10345649802`, digest `sha256:cf806e51999dc093555f02e0d158b02f036da8518eb6c40a70ed96d7bc4a77bd`;
- Lane B artifact `10345799538`, digest `sha256:bbd7e6811c525ad8ac3bf70e91a4a3b8e3b7abec63256b1d7a065602257106fa`;
- Lane C artifact `10345904100`, digest `sha256:f85599b41d18d464cf2a74bc6d20a30df8a41245a5db89b65de122874609bee4`;
- Lane D artifact `10346401464`, digest `sha256:2470f900e5b896922473bd01f875d6ad3b13529d2c2c633322c5b1ea7d389904`;
- aggregate artifact `10346645528`, digest `sha256:8dffd7c2804e12cafb875721b6c322169404f2a44c2c00167c967b511d4f8c54`.

Durable repaired aggregate:
`analysis/iter080f_sm_control_only_implementation_repair_aggregate_result.json`, commit `01539238222b42128d051444d6baa91cf5de45d8`.

Durable repaired result:
`results/ITER080F_SM_CONTROL_ONLY_IMPLEMENTATION_REPAIR_RESULT.md`, commit `97980ecf17e60392389f519f70fb6629dc82a1dc`.

## Authoritative repaired controls

Lane B:

- 35 explicit census statements;
- 42 independent exact-text required coverage anchors;
- `coverage_complete=true`;
- `uncovered_required_anchors=[]`;
- `qualifying_preexisting_axioms=[]`.

Lane C predicate-specific controls:

- synthetic full-function-space prescription has A1-A5 true and is accepted;
- fixed finite scalar condition has A2=false and A3=false and is rejected;
- aspirational future RG/gauge closure has A1=false, A2=false, A3=false and is rejected.

Lane C post-Iter077Q dependency isolation:

- changed tracked paths after Iter077Q: 116;
- frozen candidate files among changed paths: none;
- removed in ephemeral checkout: 116;
- replay executed: true;
- exact scientific fingerprint equal: true;
- restore successful: true;
- isolation valid: true.

Thus later post-Iter077Q repository interpretation does not provide hidden positive evidence to the repaired frozen candidate-axiom census.

## Current scientific authority

**Verdict:** `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

**Classification:**
`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.

Scoped authoritative fact: the frozen pre-Iter077Q CRQN v0.1/v0.2 candidate specifications contain no explicit, independently motivated, already-existing principle satisfying all A1-A5 and therefore no pre-existing full-function-space selector axiom capable of uniquely selecting the Iter077Q extension ambiguity.

This closes the anti-rescue interpretation for current CRQN v0.2: a future selector cannot be retroactively described as already implicit in the pre-Iter077Q v0.2 specification.

It is not a universal no-selector theorem. A genuinely new/revised primary authority or a separately motivated, prospectively preregistered new candidate version could define a selector, but that would be new authority and must be tested as such.

## Independent upstream authority retained

- Iter077Q: infinite-dimensional source-compatible K5 extension ambiguity;
- Iter080A: finite K5 permutation covariance does not select (`CONFIRMED_SCOPED`);
- repaired Iter080D: fixed finite scalar complex-linear conditions do not select (`CONFIRMED_SCOPED`);
- repaired Iter080E: frozen primary BCG/Beltran causal-Toller corpus has no P1-P5-complete joint-K5 selector (`BLOCKED_OBJECT_DEFINITION`, scoped);
- Iter080B: causal multivertex E3/E4/E6 remains `BLOCKED_SOURCE_BRIDGE`.

The controlling contact-formula erratum remains `status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical Iter077E/F source-dependent siblings remain quarantined.

## Forward authority

Do not repeat the same pre-Iter077Q candidate-specification census, finite K5 symmetry variants, fixed finite scalar selectors, or the frozen primary BCG/Beltran selector scan absent changed authority.

Current `CRQN v0.2` remains blocked at the unique-local-amplitude arrow. A subsequent gate may formalize the current-version survival/anti-rescue decision, but it must not invent a selector. Any new selector principle requires independently motivated new/revised source authority or an explicitly new, prospectively frozen candidate version and direct source-faithful testing.

E7/E8, G3, regulator independence and RG remain downstream-locked while the local amplitude and E3/E4/E6 composition bridge are undefined.
