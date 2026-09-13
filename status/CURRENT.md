# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_063A / K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENCE`

## Controlling closed K4 chain

- Iter046 `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`.
- Iter047 `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`.
- Iter048 `K4_FP_OBSTRUCTION_MIXED_CHANNELS`.
- Iter049 `K4_RR_SELECTOR_NONCOVARIANT`.
- Iter050 `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`; denominator control stable.
- Iter051 `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + cancellation-dominated subset.
- Iter051A/B/C establish frozen sign-class nuisance/range stability but no global physical sign theorem.
- Iter052 `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`.
- Iter053 `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`.
- Iter054 `K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT`.
- Iter055 `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT` under naive class-only relabeling.
- Iter056 `K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_NOT_CLOSED`.
- Iter057 `K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT`.
- Iter058 `K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT`: run `34719879504`, job `103623650207`, artifact `10305894028`, digest `sha256:24d06807b51f87d4751d3df3e4804c4e839e5e6cfce75ffb8d202492790bd84f`.
- Iter059 `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED`: run `34721276444`, job `103627484707`, artifact `10306671166`, digest `sha256:7e35f534cd9dac42d53107ff8536c2be9c68cf0e59546f3864c88c8a3cf4884e`.
- Iter060 `K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANT`: run `34724006585`, job `103634827689`, artifact `10307765024`, digest `sha256:c8bce3178df43b99657d4463155dd153d64185e0eb62686cd440a4c52da124c5`.
- Iter061 `K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_OBSTRUCTED`: run `34724072187`, job `103635002582`, artifact `10307780179`, digest `sha256:adb4b2f15f8846f7cc4bf41fba75149f4716b23d1bddc42ad1d98f43c732588a`.
- **Iter062 terminal `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED`**: prereg `8b31b9b1f3d852301e2a20ea76cc59c3da861a35`, head `a08c1705d1bc17fae3f13e7711ba500575066fee`, run `34726816242`, aggregate job `103642356021`, artifact `10307958661`, digest `sha256:ee15cdda66899082d10d207bfa5c4647c01fd4d149b99d9c64299bf8921f61fa`. All 16 lanes valid; strong/non-strong census is 4/4 for each global convention and pairwise convention status is invariant. Durable result: `status/ITERATION_062_RESULT.md`.

## Exact scoped interpretation after Iter062

The minimal ordered-wedge bridge `s(a,b)=c eta(a,b) kappa_ab` is covariance-compatible for all frozen K4 sigma classes, S4 relabelings, order reversal, and both unfixed global conventions `c=±1`. This is bookkeeping/analyticity geometry only. It does not select a physical causal sector or establish a causal-vertex amplitude/prescription.

## Active Iter063A — tree/fundamental-cycle representation independence prerequisite

Prospectively preregistered at `bc61d185d0ab5b5b5e91ffb3626854dd16c70d11` before implementation. Frozen production uses 16 lanes (`8 sigma classes × 2 global conventions`), with each lane testing all 24 S4 relabelings and all 16 K4 spanning trees/fundamental-cycle bases, exact kernel rank/reconstruction, constructive positive circulation for strong tournaments, one-way-cut obstruction for non-strong tournaments, order reversal, and global-convention invariance.

Authoritative production run: `34729151990`, workflow/head `cb94a44dfd2966caf394314e81cbcf5ac672d7fc`.

Frozen classifiers: `ITER063A_SOURCE_OR_IMPLEMENTATION_INVALID`, `K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_DEPENDENCE_FAIL`, `K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENT`.

Even a PASS is only an exact K4 representation-independence prerequisite. A separate source-backed direct-vertex / exact-EPRL control gate remains mandatory before K5 can be considered.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
