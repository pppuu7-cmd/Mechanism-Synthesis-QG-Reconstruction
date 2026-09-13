# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_063B / SOURCE_BACKED_DIRECT_VERTEX_EPRL_CONTROL_QUALIFICATION_REPAIRED_RETRY`

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
- Iter062 `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED`: run `34726816242`, aggregate job `103642356021`, artifact `10307958661`, digest `sha256:ee15cdda66899082d10d207bfa5c4647c01fd4d149b99d9c64299bf8921f61fa`.
- Iter063A `K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENT`: prereg `bc61d185d0ab5b5b5e91ffb3626854dd16c70d11`, head `cb94a44dfd2966caf394314e81cbcf5ac672d7fc`, run `34729151990`, aggregate job `103648649087`, artifact `10308523372`, digest `sha256:05e4cf30e42fa8702a7272eadeff81a425ec64679e109e9cc5f6b70c7a07cb73`; 16 lanes / 6144 exact cases. Durable result commit `554b7b2e2d0f6aab4ccdcba3adec16aee60def1f`.

## Iter063B authority state

Frozen preregistration: `75fb19ed4644ca422a3954ef8e231d8e35c92fc4`.

Initial production head `11c6823e00473650f63ca7ed7464718e1049ae7b`, run `34729216381`, job `103648792303`, artifact `10308837692`, digest `sha256:46ea46cc0c0b9e7882252c7dfc359719856813b1c62cb07569bae25ab079a5ff` is **diagnostic / non-authoritative**. Raw artifact inspection showed its only `qualified_files` were the Iter063B preregistration and the audit script itself. This is classified `ITER063B_IMPLEMENTATION_INVALID_SELF_REFERENCE`, not a scientific PASS.

Minimal implementation-only repair commit: `ecc99cb078dd2f41007cac429c5cb080bf79d145`. No frozen science was changed or weakened. The repaired audit excludes self-generated status/scripts/workflows/code from source authority and retains the original stronger same-file qualification rule.

Repaired authoritative retry head: `6102be4255016b43aa49af9f8ee6293abc6a3090`; run `34731891190`. Durable authority record: `status/ITERATION_063B_AUTHORITY.md`.

Until the retry is terminal and its raw artifact is consumed, Iter063B is OPEN. No direct causal-vertex/EPRL production gate is authorized.

## Source status relevant to Iter063B

The tracked August-2026 Toller literature anchor gives a concrete primary-source identifier and the exact additive identity `T^(+) + T^(-) = D`. Existing MSQGR code also contains pointwise direct ten-wedge integrand smoke machinery. However repository-derived implementation is not itself source authority for the frozen Iter063B qualification; an explicit source-backed causal/direct vertex object and its exact EPRL-control relation must survive the repaired audit.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
