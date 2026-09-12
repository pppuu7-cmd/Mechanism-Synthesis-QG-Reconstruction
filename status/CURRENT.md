# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_051C / SIGN_CLASS_RANGE_VALIDATION` + `ITERATION_054 / SIGN_COMPATIBLE_CONTOUR_CHAMBERS`

## Closed results controlling the current front

The source-backed Lorentzian EPRL/Toller carrier, exact `T+ + T- = D` control, native general Toller kernel, residue-series pure-boost kernel and direct ten-wedge topology have been independently validated. Ordinary EPRL booster factorization is not a valid fixed-Toller-branch causal carrier; the direct relative-group causal vertex remains the selected architecture.

Distributional K3/K4 chain:

- Iter045: exact quotient subtraction + residue/PV finite part is coordinate-covariant on the frozen K3 held-out set.
- Iter046: `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`.
- Iter047: `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`.
- Iter048: `K4_FP_OBSTRUCTION_MIXED_CHANNELS`.
- Iter049: `K4_RR_SELECTOR_NONCOVARIANT`.
- Iter050: `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`; independent denominator control is `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`.
- Iter051: `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + `K4_RR_CANCELLATION_DOMINATED_SUBSET`.
- Iter051A: `K4_RR_SIGN_CLASS_NUISANCE_STABLE` on frozen H1/H2.
- Iter051B: `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`; none of eight preregistered coarse residue/cancellation selectors exactly matches RR.
- Iter052: `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`; run `34716166419`, artifact `10305101542`, digest `sha256:7ac12a5666cd337062ae143da864372eb011223563b47f36b733261b102ccc8f`; 36/36 valid, controls exact zero, source full-S3 antisymmetrizer nonzero in 9/36. No coefficient refitting.
- **Iter053 terminal:** `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`; run `34718231048`, aggregate artifact `10305646600`, digest `sha256:3aa44b8f4d65f096120c299c303c20e5e20061e1b084761d82e3fda9fedcfd6f`. All 32/32 lanes valid, tree/cycle-basis consistency PASS, compatible causal sign classes `0/8`. Exact `A v=s` fails for every factorized causal sign class in all four frozen bases; independent graph criterion `B s=0` fails for all eight classes. Scope: equal-magnitude one-vector affine translation only, not a general correlated-contour no-go.

Durable result notes include `status/ITERATION_048_RESULT.md` through `status/ITERATION_053_RESULT.md` where applicable.

## Active Iter051C — wider held-out sign-class range validation

Preregistered commit `1d3cd2b28d4f33cb18b89408962628254a2ed920` before implementation `e40189337d29efdda04c530f43242c21b8f54d3a` and workflow `9a68ab092b68cb2897d54006eab770fc7ebcf572`. Run `34717183041`.

Matrix: 192 exact lanes = H4/H5 × 8 sign classes × 4 trees × 3 pairs. Frozen Iter051A H1/H2 masks are references. Terminal classifier only from aggregate: `ITER051C_CONTROL_OR_RECONSTRUCTION_INVALID`, `K4_RR_SIGN_CLASS_RANGE_STABLE`, or `K4_RR_SIGN_CLASS_RANGE_DEPENDENT`. H5 production is actively progressing; do not classify partial lanes or retune.

## Active Iter054 — exact sign-compatible affine contour chambers

Preregistered commit `da8f756e3478d561d6001f251f93e70669b56aed` before implementation `cb500ce926ec0e987f78ecc5b04333fce6d8bc43` and workflow `7dd1b3052229b9d7d416e8f32ac3ad774a178732`. PR #56 merged as `83dbee09ea0df0b7c3f65e373701dec36d7a960a`; run `34718445213`.

For `M=diag(s)A`, test strict exact feasibility `M v>0`: one common affine direction, unequal positive edge-shift magnitudes allowed. Infeasible lanes require exact Gordan/Caratheodory obstruction certificates; feasible lanes require independently verified exact witnesses. Frozen matrix: 32 lanes = 8 causal sign classes × 4 tree/cycle bases. Frozen classifiers: invalid, `K4_CAUSAL_SIGN_CHAMBER_ALL_CLASSES_FEASIBLE`, `...CLASS_DEPENDENT`, or `...NO_CLASS_FEASIBLE`.

Latest observed production state: 21/32 lanes completed successfully and the remaining lanes queued. Consume only the terminal aggregate.

## Next allowed decisions

1. Consume Iter051C and Iter054 only at terminal aggregates and write durable result notes before advancing.
2. If Iter054 is class-dependent, prospectively audit physical causal-sector/permutation stability of the feasible/infeasible partition before using it as prescription input.
3. If Iter054 has no feasible class, do **not** claim a general contour no-go; move to a prospectively fixed genuinely correlated/multivariate contour or canonical multivariate residue/boundary-value construction.
4. If Iter054 has feasible classes, distinguish that from Iter053: unequal positive edge magnitudes may admit a common direction even though the original equal-`epsilon` shift vector is impossible.
5. Do not invent post-hoc residue selectors or fitted cancellation coefficients. K5 remains blocked until a source/analyticity-selected K4 prescription passes tree/cycle-basis/permutation/order independence plus exact EPRL control.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no new complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL no-go theorem;
- no global causal-sign universality theorem from finite scans;
- no G3 PASS or F9/G8 promotion from these surrogates;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential integration order;
- fixed causal-sector claims may not borrow `T+ + T- = D` cancellation without proof;
- keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
