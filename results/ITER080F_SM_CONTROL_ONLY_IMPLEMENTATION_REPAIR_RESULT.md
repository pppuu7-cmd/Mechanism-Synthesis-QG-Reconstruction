# Iter080F-SM — control-only implementation repair result

**Date:** 2026-09-14

## Authority

This is the authoritative repaired execution of the already-preregistered Iter080F scientific contract.

- original preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`
- unchanged gate: `CRQN_V0_2_EXISTING_AXIOM_FUNCTION_SPACE_SELECTOR_CENSUS / ANTI_RESCUE_DECISION_GATE`
- Critic invalidation of historical implementation: `results/ITER080F_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `e4d90e29c9bcbb9fd7ec6f54a4e42a432b5bc503`
- control-only implementation repair plan: `4b5e1d1638f366e8384fef3a03da59db9c42dde6`
- authoritative repaired implementation/head: `71b5551c034506b7bb0c07bf222d08d7756f31ca`
- durable repaired aggregate: `analysis/iter080f_sm_control_only_implementation_repair_aggregate_result.json`, commit `01539238222b42128d051444d6baa91cf5de45d8`

The scientific HYPOTHESIS, OBJECT, DEPENDENCY, frozen candidate corpus, A1-A5 selector predicates, PASS/BLOCKED/INVALID criteria and interpretation ceiling were not changed.

## Frozen positive-evidence corpus

Only the two candidate specifications that pre-date Iter077Q are eligible positive selector evidence:

- `candidates/CANDIDATE_A_CRQN.md`, blob `a3023dadb75f4c53d0c44a6de1c46958f4149178`, origin `906c903892803b9a08b97340a1efc5a369a31061`;
- `candidates/CANDIDATE_A_CRQN_V0_2.md`, blob `3933c110f9bafabb6593f8301029adaa25458bb2`, origin `75250042861f613fe8048a1d001352da478ace0d`.

The controlling ambiguity is the full Iter077Q function space `W`, not a finite-dimensional surrogate.

A candidate principle qualifies only if all five predicates hold:

- `A1_PREEXISTING`;
- `A2_FULL_W_ACTION`;
- `A3_SELECTION_POWER`;
- `A4_OBJECT_REACH`;
- `A5_INDEPENDENT_MOTIVATION`.

## Non-authoritative repair attempt

Commit `f435f0a0edf88c83c21eb830e052d9d49ba50f2f` triggered run `34841208883`. Lane A/C/D succeeded, but Lane B failed before aggregate because the first completeness checker used an over-broad relevance scan and one brittle exact anchor. No aggregate was produced. This run is implementation-invalid and scientifically non-authoritative; no substantive conclusion is taken from it.

The scientific contract was not changed. The coverage implementation was repaired only by replacing the over-broad scan with an explicit independent exact-text coverage manifest spanning the preregistered relevant categories.

## Authoritative repaired execution

Run `34841351539` at head `71b5551c034506b7bb0c07bf222d08d7756f31ca` completed all required lanes and aggregate with `success`.

Jobs:

- Lane A `103966834681`: `PASS_PROVENANCE_TIMING`;
- Lane B `103966834664`: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`;
- Lane C `103966834585`: `PASS_ANTI_RESCUE_CONTROLS`;
- Lane D `103966834678`: `PASS_DEPENDENCY_LOCK`;
- aggregate `103966883834`: success.

Artifacts:

- Lane A artifact `10345649802`, digest `sha256:cf806e51999dc093555f02e0d158b02f036da8518eb6c40a70ed96d7bc4a77bd`;
- Lane B artifact `10345799538`, digest `sha256:bbd7e6811c525ad8ac3bf70e91a4a3b8e3b7abec63256b1d7a065602257106fa`;
- Lane C artifact `10345904100`, digest `sha256:f85599b41d18d464cf2a74bc6d20a30df8a41245a5db89b65de122874609bee4`;
- Lane D artifact `10346401464`, digest `sha256:2470f900e5b896922473bd01f875d6ad3b13529d2c2c633322c5b1ea7d389904`;
- aggregate artifact `10346645528`, digest `sha256:8dffd7c2804e12cafb875721b6c322169404f2a44c2c00167c967b511d4f8c54`.

Green CI is execution evidence only. The scientific result follows from the frozen predicates and the repaired auditable census.

## Repaired audit controls

Lane B evaluates 35 census statements and an independent exact-text coverage manifest with 42 required anchors. Coverage is complete and `uncovered_required_anchors=[]`.

No census row satisfies all A1-A5:

`qualifying_preexisting_axioms=[]`.

Lane C now tests the classifier predicate by predicate:

- synthetic explicit full-function-space selector: A1-A5 all true and accepted;
- fixed finite scalar normalization condition: A2=false, A3=false and rejected;
- aspirational future RG/gauge closure statement: A1=false, A2=false, A3=false and rejected.

Lane C also executes the frozen dependency-isolation control rather than asserting a Boolean. Relative to Iter077Q commit `5941b3a064d93f2898d9e9a48545826e950455f1`, it identified 116 post-Iter077Q changed tracked paths, found no frozen candidate-file changes, temporarily removed all 116 post-Iter077Q paths in the ephemeral checkout, reran the scientific census from the surviving frozen candidate blobs, obtained an exactly identical scientific fingerprint, and restored all removed paths. Recorded controls:

- `replay_executed=true`;
- `fingerprint_equal=true`;
- `restore_ok=true`;
- isolation `valid=true`.

Therefore later Iter077Q/Iter080 interpretations are not silently supplying positive selector evidence to the repaired candidate-axiom census.

## Scientific result

**Verdict:** `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

**Classification:**

`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.

Within the frozen pre-Iter077Q CRQN v0.1/v0.2 candidate specifications, there is no explicit independently motivated pre-existing principle satisfying all A1-A5 and therefore no already-present full-function-space selector that can uniquely remove the Iter077Q extension ambiguity.

The candidate documents contain amplitude/composition desiderata, analyticity/unitarity filters, gauge/refoliation requirements, RG targets, normalized-observable requirements, the finite `Phi` existence question and explicit open/blocker language. None of these, as actually specified before Iter077Q, defines an operation on the whole ambiguity function space `W` with enough selection power to determine a unique extension.

## Scientific effect

This closes the anti-rescue question for current `CRQN v0.2` in the frozen candidate-specification scope: the missing selector cannot be claimed to have already been implicit in v0.2 before the Iter077Q obstruction was discovered.

Consequently the current candidate remains blocked at the unique-local-amplitude arrow unless one of the following genuinely changes authority:

1. new/revised primary source authority supplies a valid joint-K5 full-function-space selector; or
2. a separately motivated, prospectively preregistered new candidate version introduces a new selector principle and survives direct source-faithful tests.

Anti-rescue forbids retroactively describing such a future principle as an existing v0.2 axiom.

The independent causal multi-vertex E3/E4/E6 source bridge remains `BLOCKED_SOURCE_BRIDGE` under Iter080B.

## Interpretation ceiling

This is not a universal theorem that no mathematical selector exists, nor a theorem that no future CRQN-like model can define one. It does not prove nonexistence/divergence of the full causal vertex, regulator independence, E7/E8, G3, RG, continuum geometry, massless spin-2, GR recovery, matter/QFT IR, normalized predictions, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

Claim locks remain: no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no G3 PASS or F9/G8/K5 promotion. Retain published one-wedge spectral `i epsilon` only in source scope.
