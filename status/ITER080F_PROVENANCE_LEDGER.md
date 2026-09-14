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

## Chronology

- preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`
- initial implementation: `082bfb7facf57f8cf42405a1b514d88a7ffb8831`
- initial workflow trigger: `4c89411f516efc4ceef13ccb7ab3363feba8a10c`
- first run: `34836984921` — invalid/non-authoritative because Lane A compared equivalent timestamp instants by literal ISO strings
- control-only timezone/provenance repair plan: `9f857e8acec6de180185a206ec67791efe333f37`
- repaired Lane A implementation: `28d3d04124855aeff8209a91287cbb727570bf9c`
- repaired workflow/production head: `1a78e94ad72e4bdad4b132a37699debd964789bc`
- terminal run: `34837108991` — all jobs terminal `success`
- durable aggregate commit: `5736e129c228e83a04c651d27faddc346c26c111`
- Researcher result commit: `61ee95efdda1d13b47e3ef04de61d40d08ca95c1`
- Researcher handoff commit: `e415723af51e7d5f613ad55da0505f6af27ed513`

## Terminal run provenance

Run `34837108991` at head `1a78e94ad72e4bdad4b132a37699debd964789bc`:

- Lane A job `103953327454`, artifact `10344301951`, digest `sha256:92c8666c963127ffc9bba1d5bf306c2b8702c0dc443c3ee27a7e5268ea4beaaf`
- Lane B job `103953327735`, artifact `10344258250`, digest `sha256:0c75a7af91840167b3ff16bc1d59d5aa80bc3bbb4de1c2bc99da6ad6e5e96440`
- Lane C job `103953327704`, artifact `10344168296`, digest `sha256:4109251b99040c408037dfabbc62012a3e5d6b71feb0733f11f550e080901e16`
- Lane D job `103953327677`, artifact `10344592580`, digest `sha256:765093c9d9d3a040b36e6e9db1f8809aeee71775fafb058edfe963aea5e4caf8`
- aggregate job `103953376077`, artifact `10344587578`, digest `sha256:bd815e8cafa5a03c3d13af96220570758a9300e7f759671c81b2ca198b2b86f9`

Historical Researcher aggregate classification:
`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.
Historical Researcher verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

## Independent Critic review

Durable review: `results/ITER080F_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `e4d90e29c9bcbb9fd7ec6f54a4e42a432b5bc503`.
Critic handoff commit: `42646f8aa10e1c869f73ddec4c822f279ef59f32`.

Independent verdict: `INVALID_IMPLEMENTATION`.

Decisive frozen-contract defects:

1. Lane C frozen aspiration control requires A1/A2/A3 all false, but executable control hard-codes A1 true and tests only failure of the overall A1-A5 conjunction.
2. Lane C frozen post-Iter077Q mutation/removal independence control is not executed; code substitutes a literal `scientific_inputs_only_two_frozen_candidate_blobs=True`.
3. Lane B frozen requirement to audit every plausibly relevant statement is implemented as six selected hard-coded rows with no executable completeness criterion; additional plausibly relevant frozen statements are omitted from the machine census.
4. Finite-scalar control checks only overall rejection rather than predicate-specific A2=false and A3=false.

Direct adversarial reading found no hidden A1-A5-complete selector in the two frozen candidate files. Thus invalidation is implementation authority only; it does not scientifically unblock CRQN.

## Current authority

Iter080F historical run/result are preserved but non-authoritative for the scientific classification pending a control-only repair under the unchanged preregistration.

Independent upstream authority remains:

- Iter077Q: infinite-dimensional source-compatible K5 extension ambiguity;
- Iter080A: finite K5 permutation covariance does not select (`CONFIRMED_SCOPED`);
- repaired Iter080D: fixed finite scalar complex-linear conditions do not select (`CONFIRMED_SCOPED`);
- repaired Iter080E: frozen primary BCG/Beltran causal-Toller corpus has no P1-P5-complete joint-K5 selector (`BLOCKED_OBJECT_DEFINITION`, scoped);
- Iter080B: causal multivertex E3/E4/E6 remains `BLOCKED_SOURCE_BRIDGE`.

The controlling contact-formula erratum remains `status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical Iter077E/F source-dependent siblings remain quarantined.

## Forward authority

Only a control-only Iter080F repair/retry is authorized on this frozen anti-rescue object. It must execute predicate-specific Lane C controls, actually test post-Iter077Q dependency isolation, and make Lane B plausible-statement census completeness auditable over both frozen candidate blobs without changing the scientific contract.

If that repair requires changing corpus, predicates, PASS/BLOCKED/INVALID criteria or interpretation ceiling, require a new prospectively preregistered successor rather than rewriting Iter080F.
