# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_059 / SOURCE_BACKED_EQUAL_SPIN_TOLLER_WEDGE_REVERSAL_LAW`

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
- Iter057 `K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT`: complete 64-vector domain, four S4 tournament orbits, one feasible 24-orbit.
- **Iter058 terminal `K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT`**. Authoritative run `34719879504`, job `103623650207`, head `dff2803ca240760861233c766b447e026fea16ae`, artifact `10305894028`, digest `sha256:24d06807b51f87d4751d3df3e4804c4e839e5e6cfce75ffb8d202492790bd84f`. All 64 sign vectors satisfy the frozen equivalence; 24 strong tournaments have deterministic strictly-positive circulation certificates and 40 non-strong tournaments have exact one-way-cut obstructions. Durable result: `status/ITERATION_058_RESULT.md`.

## Exact scoped interpretation after Iter058

For the K4 signed-normal / affine contour surrogate,

`exists x in ker(B) with s_e x_e > 0 on every edge`

iff the oriented K4 sign vector defines a strongly connected tournament. This upgrades the finite enumeration to a graph-flow characterization. It is **not** a physical Toller causal-sector selector and carries no causal-vertex finiteness/divergence claim.

## Active Iter059 — source-backed equal-spin Toller wedge-reversal law

Prospectively preregistered before implementation at commit `d8e1ed549f1810cbf61da78f4cf881d83c745ade`; implementation commit `0b13c1e0efd1b6256204c465ac4738c8ba2dcd1b`; workflow commit/head `3832616ffb80ba9fedc0b293c94b2f9f3ddb3708`.

Frozen proposed equal-spin causal-wedge law:

`T^(+)_{jm,jn}(g^-1) = conjugate(T^(-)_{jn,jm}(g))`

and the branch-swapped companion relation, derived/tested from the published Feynman spectral formula plus the ordinary Wigner-D unitary inverse identity. No Toller representation composition rule is assumed. Exact obligations include `P_jj` kernel reality, the Feynman-kernel branch swap including conjugation of `1/(2 pi i)`, additive-control compatibility, and an explicit unequal-spin negative-control report. No `beta+i epsilon` modification is allowed.

Frozen classifiers: `ITER059_SOURCE_OR_IMPLEMENTATION_INVALID`, `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_LAW_FAIL`, or `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED`.

If Iter059 passes, only then may the strong-tournament / positive-circulation geometry be tested as a candidate analyticity input for the direct causal vertex. K5 remains blocked until a source/analyticity-selected K4 prescription passes tree/cycle-basis/permutation/order independence plus exact EPRL control.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
