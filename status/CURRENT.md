# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_062 / ORDERED_ORIENTATION_KAPPA_SPECTRAL_BRIDGE`

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
- **Iter061 terminal `K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_OBSTRUCTED`**: prereg `7549bb44a3e4d58225df67f5f1becbe8be46c066`, implementation `0b23cc4eb7b14e9a2e711162fba4b0cf695483cd`, head `73c33197f6b38c4516b99a2c80f49312eda11a6f`, run `34724072187`, job `103635002582`, artifact `10307780179`, digest `sha256:adb4b2f15f8846f7cc4bf41fba75149f4716b23d1bddc42ad1d98f43c732588a`. Direct candidates compatible `0/16`; reversal-covariant orientation-blind edge-local maps `0/4`. Durable result: `status/ITERATION_061_RESULT.md`.

## Exact scoped interpretation after Iter061

The source-backed equal-spin Toller branch sign flips under wedge-order reversal, whereas unordered physical `kappa_ab=sigma_a sigma_b` does not. Therefore no orientation-blind direct identification `s=f(kappa)` is compatible with both frozen laws. This is a scoped algebraic obstruction. It does not rule out an orientation-sensitive ordered-wedge bridge and does not select a physical causal sector.

## Active Iter062 — ordered-wedge orientation-sensitive bridge

Prospectively preregistered at commit `8b31b9b1f3d852301e2a20ea76cc59c3da861a35` before implementation. Implementation head before workflow: `b7d8acc8fdeade0091a87cae06002752dc96e079`; workflow/head `a08c1705d1bc17fae3f13e7711ba500575066fee`; authoritative run `34726816242`.

Frozen bridge family:

`s(a,b)=c * eta(a,b) * kappa_ab`,

where `eta(a,b)=+1` for `a<b`, `-1` for `a>b`, and global convention `c=±1` remains unfixed. No edge-dependent fitted signs or weights are allowed.

Frozen production: 16 independent lanes (`8` physical sigma classes × `2` global branch conventions), each exhaustively checking all 24 S4 relabelings and both order states. Tests include source-reversal covariance, Iter056 orientation-cocycle covariance, Iter058 positive-circulation / directed-cut certificates, Iter057 orbit consistency, and invariance under the global branch convention.

Frozen classifiers: `ITER062_SOURCE_OR_IMPLEMENTATION_INVALID`, `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANCE_FAIL`, or `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED`.

Even a PASS only establishes an orientation-compatible bookkeeping bridge up to an unfixed global branch convention. A subsequent direct-causal-vertex analyticity gate would still need prospective tree/cycle-basis/permutation/order independence plus exact EPRL controls. K5 remains blocked until such a source-selected K4 prescription is established.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
