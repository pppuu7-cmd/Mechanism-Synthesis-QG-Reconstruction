# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_051C / SIGN_CLASS_RANGE_VALIDATION` + `ITERATION_055 / POSITIVE_CIRCUIT_ATLAS_AND_S4_COVARIANCE`

## Closed results controlling the front

The Lorentzian EPRL/Toller carrier, exact `T+ + T- = D` control, native general Toller kernel, residue-series pure-boost kernel and direct ten-wedge topology are validated. Ordinary EPRL booster factorization is not a valid fixed-Toller-branch causal carrier; direct relative-group causal integration remains the selected architecture.

Key K4 chain:

- Iter046 `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`.
- Iter047 `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`.
- Iter048 `K4_FP_OBSTRUCTION_MIXED_CHANNELS`.
- Iter049 `K4_RR_SELECTOR_NONCOVARIANT`.
- Iter050 `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`; denominator control `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`.
- Iter051 `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + `K4_RR_CANCELLATION_DOMINATED_SUBSET`.
- Iter051A `K4_RR_SIGN_CLASS_NUISANCE_STABLE` on H1/H2.
- Iter051B `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`; none of eight preregistered coarse selectors exactly matches RR.
- Iter052 `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`; run `34716166419`, artifact `10305101542`, 36/36 valid, controls exact zero, source full-S3 antisymmetrizer nonzero 9/36. No coefficient refitting.
- Iter053 `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`; run `34718231048`, artifact `10305646600`, digest `sha256:3aa44b8f4d65f096120c299c303c20e5e20061e1b084761d82e3fda9fedcfd6f`. All 32/32 valid and basis-consistent; exact `A v=s` fails for all 8 causal classes. Scope: equal-magnitude one-vector affine translation only.
- **Iter054 terminal `K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT`**; run `34718445213`, artifact `10305511999`, digest `sha256:32f701abd1359ccb60ab22d14edc012f886c47d7225d8088a7337dcb48ae6c42`. All 32/32 valid and basis-consistent. Strict `diag(s)A v>0` is feasible in all four bases for 4/8 classes: `+-+`, `-++`, `-+-`, `--+`; infeasible with exact positive-dependence certificates for `+++`, `++-`, `+--`, `---`. This 4/8 partition is **not yet a physical sector selection**; vertex-relabeling/orientation covariance must be audited first.

Durable notes include `status/ITERATION_052_RESULT.md`, `status/ITERATION_053_RESULT.md`, and `status/ITERATION_054_RESULT.md` plus earlier result files.

## Active Iter051C — wider held-out RR sign-class range validation

Preregistered `1d3cd2b28d4f33cb18b89408962628254a2ed920` before implementation/workflow. Run `34717183041`.

Matrix: 192 exact lanes = H4/H5 × 8 sign classes × 4 trees × 3 pairs. Frozen Iter051A masks are references. Consume only terminal aggregate. PASS means finite-range mask stability only; FAIL means retain range dependence without retuning.

## Active Iter055 — complete positive-circuit atlas + S4 covariance

Preregistered **before implementation/output** at commit `5ef00a72f034d2dbf943ccd5e0c7ab5662bb8d21`; implementation `a5695b6df0643b7132f7db7afabd91a5268142d7`; workflow `4554cc601009827996d53317a9f04e0642d63fec`; PR #57 merged as `65ac810ce64d63375a4d57bd9163826c8198cfc4`; run `34719188955`.

Iter055 exhaustively enumerates all 56 edge supports of size 1..4 for each of 8 causal classes × 4 bases, builds the complete exact support-minimal positive-circuit atlas of `M=diag(s)A`, and tests:

- exact equality of circuit-support atlases across `S0,S1,P0,P1`;
- covariance under all 24 K4 vertex permutations after induced edge permutation and causal `sigma_0=+1` regauging;
- exact S4 orbit decomposition, circuit counts and support-size histograms.

Frozen terminal outcomes: invalid; basis-dependent; S4-noncovariant; or `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_BASIS_AND_S4_COVARIANT`.

This is deliberately independent of Iter054 artifacts. It tests whether the obstruction structure behind the 4/8 oriented-flow taxonomy is a graph-covariant invariant or an orientation/relabeling artifact.

## Next allowed decisions

1. Consume terminal Iter051C and Iter055 aggregates immediately and record durable results.
2. If Iter055 is S4-noncovariant, do not promote the raw Iter054 4/8 partition. Prospectively derive and test the **orientation-corrected** vertex-permutation action, including reversal signs of the oriented edge-flow variables, before any physical sector statement.
3. If Iter055 is S4-covariant, independently validate the resulting S4 orbit taxonomy before using it as analyticity input.
4. Equal-`epsilon` one-vector reconstruction remains excluded by Iter053. Unequal-magnitude sign-compatible directions from Iter054 are only candidate tube chambers, not the published spectral `i epsilon` prescription itself.
5. Do not fit residue selectors, cancellation coefficients, counterterms, or preferred orders. K5 remains blocked until a source/analyticity-selected K4 construction passes tree/cycle-basis/permutation/order independence and exact EPRL control.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no global causal-sign universality from finite scans;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` with an unproved `beta+i epsilon` rule;
- keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
