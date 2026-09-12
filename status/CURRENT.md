# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_060 / SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANCE`

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
- **Iter059 terminal `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED`**: run `34721276444`, job `103627484707`, head `3832616ffb80ba9fedc0b293c94b2f9f3ddb3708`, artifact `10306671166`, digest `sha256:7e35f534cd9dac42d53107ff8536c2be9c68cf0e59546f3864c88c8a3cf4884e`. Equal-spin `2j=0..12` exact branch-swap/kernel-reality controls pass; 312 numeric controls pass with max error `6.1354647881160596e-100 < 1e-40`; unequal-spin same-form self-conjugacy is `0/32`. Durable result: `status/ITERATION_059_RESULT.md`.

## Exact scoped interpretation after Iter059

For the source-backed equal-spin causal EPRL wedge,

`T^(+)_{jm,jn}(g^-1) = conjugate(T^(-)_{jn,jm}(g))`

with the branch-swapped companion. This is a source-backed inversion/order-reversal law, not a Toller representation-composition law. It does not select a physical causal sector and does not establish contour existence or vertex finiteness.

## Active Iter060 — source-reversal analyticity-geometry covariance

Prospectively preregistered before implementation at commit `d52f79289f9004b346a0de59e79e099389fdcd56`; implementation commit `8eace2c3f4897e19f5ffec84b14df36eed4c45d0`; workflow/head `30d1ebea02d7ddb09cbd38fb71ab0029b439a413`; authoritative run `34724006585`.

Frozen domain: all 64 K4 oriented sign vectors × all 24 S4 relabelings × ordinary/source-reversed operation = 3072 exact lanes. The gate checks that the Iter056 orientation cocycle plus Iter059 global branch swap agrees with direct tournament relabeling/reversal, preserves strong connectivity and Iter058 feasibility status, transports exact positive-circulation / one-way-cut certificates, preserves the `8,8,24,24` orbit structure, and keeps the unordered additive branch control invariant.

Frozen classifiers: `ITER060_SOURCE_OR_IMPLEMENTATION_INVALID`, `K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANCE_FAIL`, or `K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANT`.

Even a PASS only authorizes a subsequent prospective source-selected K4 branch-assignment gate with tree/cycle-basis/permutation/order independence plus exact EPRL control. K5 remains blocked until that is established.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
