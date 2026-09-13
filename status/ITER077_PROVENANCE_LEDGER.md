# Iter077 provenance ledger

**Date:** 2026-09-14

This ledger resolves historical naming collisions created by parallel research lanes. Existing preregistration filenames, workflow names, JSON labels, run IDs and result files are immutable provenance and are **not renamed**. Stable prose aliases below should be used in future `status/`, recovery and result notes.

## Stable aliases

### `Iter077A-SM` — true source `B`-map transversality sibling

Historical frozen label: `Iter077A`.

- source/derived supplement: `sources/CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md`
- source commit: `08499d9cb1bd786adfdd842364606b4517d1962d`
- preregistration: `prereg/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md`
- prereg commit: `f8dbe2d008b46369fb45ef6fc7c5ff887967f299`
- implementation: `distributional/iter077a_true_source_b_map_transversality.py`
- implementation commit: `e8ddeb1acc6830e6620db02630088eae3b23b2d9`
- workflow head: `83eb3da869f3ad324471db61ec47f02dad36091e`
- authoritative run: `34784565177`
- durable result: `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`
- result commit: `fda83125747f530faff264eb6eea3fe4cb4b2f55`
- verdict: PASS
- classification: `ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED`

Scientific scope: true coherent-spinor source map at the common group collision. Exact witness `rank_Q(dB)=10`; scalar K5 incidence rank is 4 and its six cycle relations do not transfer to the true source differential.

### `Iter077A-FF` — K5 Toller front-face data-model sibling

Historical frozen label: `Iter077A`.

- source/derived input: `sources/ITER077_PARALLEL_FRONTIER_SOURCE_DERIVATION.md`
- preregistration: `prereg/ITER077A_K5_TOLLER_FRONT_FACE_DATA_MODEL.md`
- prereg commit: `0aa40cc290ec4c2d71e687d95c915f6f473a37cd`
- implementation commit: `7b75b548ddebdb3c2e15d8cfe2f8f7cff5d4b3bc`
- workflow launch lineage includes commit `339c71b2b5e211cbfa61d7613eeccdffe0c7d184`

Scientific scope: algebraic/covariant closure of the matrix/bundle-valued Toller front-face data type. This branch is logically independent of the true-source-map transversality sibling and does not replace a full source-amplitude pushforward theorem.

### `Iter077B-BCH` — source BCH K4 cycle-curvature sibling

Historical frozen label: `Iter077B`.

- preregistration: `prereg/ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md`
- prereg commit: `ee7338fc314847a2524544445baf01ea78e87994`
- implementation lineage: `8c43363781fdd450de8396ec2ede0a1602e680a1`
- pre-production predicate repair: `cdba02a770db55b4ff2c1bba5df0cdf49e257951`
- initial combined workflow launch: `339c71b2b5e211cbfa61d7613eeccdffe0c7d184`
- later independent canonical lane relaunch: `f5ac9f4c45c1460fe75329de244df5c65d406e6b`

Scientific scope: source BCH second-order relative-coordinate curvature projected into the reduced K4 cycle channel. By preregistration, it does **not** establish the physical Toller/front-face pushforward or the nominal `epsilon^-1` coefficient.

### `Iter077C-SM` — first true-source exceptional-strata sibling

Stable frozen label: `Iter077C-SM`.

- preregistration: `prereg/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA.md`
- prereg commit: `d2414780967cc36c4b2f31ba4fbcb8453e13f978`
- implementation: `distributional/iter077c_sm_source_collision_exceptional_strata.py`
- implementation commit: `9c11041e3ce1bce8148452c14e05103e1bed02e0`
- initial workflow head: `9cd251318135274b4fd7824f22d95b1bd84869ac`
- control-only source-notation repair: `54fe49f1041ef28ac324e2a503196c9b6a6d7ed3`
- authoritative retry/workflow head: `287c22078d275085888c173adfe395fec32bfc98`
- authoritative run: `34784868939`
- durable result: `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`
- result commit: `5cdafc091295526f49323f38be13e01dcd553926`
- verdict: PASS
- classification: `ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED`

Scientific scope: exact first rank-deficient source geometry at the common collision. Rank deficiency is a vector self-stress/equilibrium condition. The frozen first full-span rank-9 witness `xxxxxyyyzz` has a one-dimensional self-stress, three-dimensional right kernel, and a `3 x 20` structured normal-variation map of exact rank 3 with a nonzero minor `-1`; locally this tested rank-9 stratum is transverse codimension 3 in the 20-dimensional normal manifold. This does not establish that every exceptional stratum is codimension 3 or that the source contact pullback is harmless.

## Forward naming rule

From this ledger onward:

- use suffix `-SM` for the source-map/full-source-amplitude line;
- use suffix `-FF` for the Toller front-face algebra line;
- use suffix `-BCH` for the source-relative BCH/K4 line;
- do not reuse an existing bare `Iter077A` or `Iter077B` label for a new object;
- the next source-map gate after `Iter077C-SM` is `Iter077D-SM` unless that exact stable alias is already present.

## Claim firewall

Parallel execution does not merge scientific scopes. A PASS in `-FF` or `-BCH` cannot be imported as a source-amplitude existence theorem. A PASS in `-SM` does not establish physical K4/Hodge transport unless an explicit source pushforward is constructed. No source-map transversality result by itself establishes contact-distribution pullback, full-vertex finiteness, or regulator independence.