# Iter080H-SM provenance ledger

**Date:** 2026-09-14

## Scientific contract

- preregistration: `prereg/ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_CRQN_SELECTOR_CENSUS.md`
- prereg commit: `3dcbb26dc1607cc6c05c6805fdb87b50846c9428`
- frozen v0.1 blob: `a3023dadb75f4c53d0c44a6de1c46958f4149178`
- frozen v0.2 blob: `3933c110f9bafabb6593f8301029adaa25458bb2`
- frozen A1-A5 and outcome criteria: unchanged through authoritative production.

## Statement-universe chronology

1. Initial line-aware universe head `9671a307cdc2c9e460620f898d3495d45fed3419`, run `34846628612`: **NON_AUTHORITATIVE_IMPLEMENTATION_FAILURE**. Python syntax error before data generation; no artifact and no scientific verdict.
2. Control-only universe syntax repair commit `0086bc3a45475946f6c7d57e4d34a1b719cbaf75`, run `34847113436`, job `103985649911`: success.
3. Frozen universe: schema `ITER080H_LINE_AWARE_UNIVERSE_V1`; SHA256 `08eb670969a99e01d02d320eaf388b03b73d829b85eb4fbfe7011c3c7bd56867`; 111 records = 30 headings + 81 scientific segments. Artifact `10348366832`.
4. Manifest freezer implementation `9f568d4468719e268d14415792c945891d17878d`; workflow head `d21d2882d1658933788673068e576b7975c5340b`; freeze run `34847374159`: success.
5. Frozen manifest commit `84cdd3ca27e0dccb20d62d0221aa7be1d117ae78`; manifest SHA256 `f35bbd10d5ef1fb53a2b56268d18c4754c9dfbc2eb126126a61c7cd5b55d895f`; exclusions used `0`.

## Production chronology

### Production attempt 1 — non-authoritative

- implementation commit `b082f855b3e3e333a7003b133b2d6228145f9189`
- workflow head `5e0d734c1a6d574df07a3af34181971fa39bd4ae`
- run `34847524728`: terminal `failure`
- A/B/C ran, D failed due two brittle textual source-lock checks; aggregate invalid.
- D defects: capitalization-sensitive Iter080D phrase and missing spaces in exact erratum matcher.
- status: `NON_AUTHORITATIVE_IMPLEMENTATION_FAILURE`; no scientific verdict promoted.

### Production attempt 2 — non-authoritative

- control wrapper commit `abdd1f70ab65489b53b44340ba67865c7a05714c`
- workflow head `1fa4429ab1a1a4efd7c2bd63818845a33274db64`
- run `34847714650`: terminal `failure`
- direct-script package import failed before frozen lane logic (`ModuleNotFoundError: analysis`).
- status: `NON_AUTHORITATIVE_IMPLEMENTATION_FAILURE`; no scientific verdict promoted.

### Production attempt 3 — authoritative

- control-loader repair commit `75d3410b9eae99449660af7b2268562df7b90ea0`
- workflow head `2a7dd58687fe38f74ce06b89abe544d96ee6b5eb`
- run `34847822308`: terminal `success`
- Lane A job `103987964900`: success / `PASS_PROVENANCE_UNIVERSE_MANIFEST`
- Lane B job `103987964779`: success / `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`
- Lane C job `103987965054`: success / `PASS_ADVERSARIAL_CONTROLS`
- Lane D job `103987964928`: success / `PASS_DEPENDENCY_CLAIM_LOCK`
- aggregate job `103988031187`: success

Artifacts:

- A `10348986489`, `sha256:2699989dd8e5715c9ed12b4519673e8ee897eb45c20cea2d820016d93f336d8b`
- B `10348502717`, `sha256:c6d6aa15f2a73876c8c8ce222936fa217705bd8ba404825a6696df843eefe43c`
- C `10349215509`, `sha256:1648b3ce4bcb243ecf371ba86254cabcf47d1f4b99a8451dab767cc5212e6463`
- D `10349185561`, `sha256:be53eec5089dcb40b050cb65a8ca82a2d8d3f53cb643c91022526ad00a9ce877`
- aggregate `10349165548`, `sha256:4de37f85ac19a512402f83baf7501a36ceb44fc8f60cf5cb90068cc46653db3d`

The attempt-2/3 repairs changed only execution plumbing and Lane-D authority matching. Candidate blobs, statement universe, frozen manifest, A1-A5 classifications, decision criteria, controls and interpretation ceiling were not changed.

## Authoritative result

- raw aggregate: `results/raw/iter080h_sm_aggregate.json`, commit `6b9a6602d108b45c5ce5416168b59751c7902d08`
- result note: `results/ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_SELECTOR_CENSUS_RESULT.md`
- verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`
- classification: `ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_CRQN_CORPUS_HAS_NO_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`
- qualifying pre-existing A1-A5-complete axioms: none.

## Independent Critic review

- durable audit: `results/ITER080H_ADVERSARIAL_REVIEW.md`
- audit commit: `c52b7fbded3f945809675abaa175870c90817858`
- Critic handoff commit: `5552e05d39b67c7659cc9ba371a1102512625e7f`
- verdict: `CONFIRMED_SCOPED`

The Critic independently re-read both frozen candidate blobs rather than accepting the pre-frozen A2/A3 booleans as scientific proof. The strongest apparent rescue candidates — v0.1 history amplitudes, alternate `Z`, `Gamma_k`/RG flow/fixed point, gauge/refoliation rule, local-amplitude programme, early-success/kill conditions, and v0.2 product amplitude, local-vertex placeholder, six causal-amplitude properties and `Phi` relation — do not act on the full Iter077Q extension space `W` while selecting among extension data.

Qualification: the manifest freezer prospectively sets A2/A3 false for every scientific segment rather than deriving those semantic predicates from executable tests. Green CI therefore does not independently prove A2/A3. This does not invalidate the gate because the preregistration freezes the classifications before production and the independent Critic full-corpus reading found no counterexample. The scoped negative conclusion is confirmed; no universal no-selector theorem follows.

## Authority effect

Iter080H supersedes Iter080F for the narrow pre-Iter077Q CRQN candidate-corpus anti-rescue census. Iter080F remains historically `INVALID_IMPLEMENTATION` and is not rewritten.

Iter080H is now independently `CONFIRMED_SCOPED`. It does not cure the Iter077Q extension ambiguity. It removes only the claim that the missing full-function-space selector was already present in CRQN v0.1/v0.2 before Iter077Q. Local amplitude remains blocked pending a genuinely new/revised source authority or independently motivated prospectively testable new candidate version.

The authorized next Researcher gate is a prospectively frozen `CRQN_V0_2_LOCAL_AMPLITUDE_ANTI_RESCUE_SURVIVAL_DECISION` using only already reviewed Iter077Q/Iter080A/repaired Iter080D/repaired Iter080E/Iter080H authority and adding no selector post hoc.