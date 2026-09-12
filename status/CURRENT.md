# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active programme front: parallel `ITERATION_051C / SIGN_CLASS_RANGE_VALIDATION` + `ITERATION_053 / GLOBAL_UNIFORM_CONTOUR_COMPATIBILITY` + `ITERATION_054 / SIGN_COMPATIBLE_CONTOUR_CHAMBERS`

## Closed results controlling the current front

1. Source-backed Lorentzian EPRL/Toller carrier, exact `T+ + T- = D` control, native general Toller kernel, residue-series pure-boost kernel and direct ten-wedge topology have been independently validated.
2. Ordinary-function causal collision layers show strong Toller poles; magnetic sums, 16 causal-sector wiring and full j=1/2 boundary-intertwiner contraction do not remove the dangerous higher multi-collision powers. This is not a physical divergence theorem.
3. Appendix-D distributional primitives are reproduced; j=1/2 contains `delta` and `delta_prime`, with an epsilon-independent `delta_prime` contact coefficient.
4. Standard Christensen positive absolute spanning-tree proof does not close for the `beta^-2` Toller carrier. Naive complete-graph products also fail the standard transversality/Hormander criterion. A correlated/source-backed extension is required.
5. The regular pointwise j=1/2 boundary-contracted carrier is genuinely S5 covariant, but S5/source-support audits leave higher extension ambiguity.
6. Iter044: joint K3 pre-contact spectral integrand has a nonzero polynomial quotient; symmetric cutoff has an `R^3` obstruction. This is not a physical divergence theorem.
7. Iter045: exact quotient subtraction plus residue/PV finite part is coordinate-covariant on 40 held-out K3 points: `FP_q1=FP_q2=FP_q3` exactly. This is a viable structural K3 extension candidate only.
8. Iter046 terminal `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`: the same sequential 1D FP is not a covariant K4 extension; EPRL/no-contact control is invariant. K5 blocked.
9. Iter047 terminal `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`: run `34708051922`; 24/24 source pairwise FP commutators nonzero, 24/24 controls exactly zero.
10. Iter048 terminal `K4_FP_OBSTRUCTION_MIXED_CHANNELS`: run `34708541480`; 24/24 valid; controls exactly zero; source channel counts `RR=8/24`, `RA=24/24`, `AR=24/24`, `AA=24/24`; 16 `INFINITY_ONLY`, 8 `MIXED`.
11. Iter049 terminal `K4_RR_SELECTOR_NONCOVARIANT`: repaired run `34709710387`, artifact `10302939028`; 48/48 valid and all controls exact zero. No universal graph/tree/pair-only RR selector exists on the frozen held-out cases.
12. Iter050 terminal `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`: run `34710540567`, aggregate artifact `10303507511`. All 108/108 lanes valid; gamma, epsilon and external-flow OAT changes caused no RR transitions; causal-sign changes caused 10. Coarse upper-pole-count asymmetry is not an exact selector.
13. Independent Iter050 denominator control terminal `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`: run `34710672477`, artifact `10302654486`; 32/32 jobs valid and stable under frozen epsilon/k nuisance variants.
14. Iter051 terminal `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + `K4_RR_CANCELLATION_DOMINATED_SUBSET`: run `34712814029`, artifact `10304298594`, digest `sha256:68a2c96e7150950138f199219ea44fda17d7fca12f264961143586469316bcc1`. 108/108 valid; exact classes 37 identical, 31 geometry-different-but-sum-cancelling, 40 geometry-and-sum-different, 0 inconsistencies. RR is nonzero in exactly those 40 residue-sum-mismatch lanes.
15. Iter051A terminal `K4_RR_SIGN_CLASS_NUISANCE_STABLE`: run `34713025288`, artifact `10303884916`, digest `sha256:56270b122eee124d02388d246d687f4b85337c5ba5aa6307bb5d68b0f5265a0c`. All 192/192 lanes valid, all controls exactly zero, all factorized-sign checks pass, and total H1↔H2 Hamming distance across all eight 12-bit sign-class masks is exactly 0. This is scoped nuisance stability, not global sign universality.
16. Iter051B terminal `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`: run `34713037668`, artifact `10304474485`, digest `sha256:3c0483a01b283178193965a5dc54fe92ab19b85f7998041834336967cc27af43`. All 96/96 lanes valid; source RR is active in 48/96; none of eight prospectively frozen coarse discrete residue/cancellation booleans exactly matches RR (`exact_matching_diagnostics=[]`). No post-hoc selector fitting is authorized.
17. Iter052 terminal `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`: run `34716166419`, aggregate artifact `10305101542`, digest `sha256:7ac12a5666cd337062ae143da864372eb011223563b47f36b733261b102ccc8f`. All 36/36 lanes valid and all F=1 control antisymmetrizers are exactly zero, but the fixed canonical full-S3 source antisymmetrizer is nonzero in 9/36 lanes. The universal canonical-antisymmetry identity branch is therefore closed without coefficient refitting.

Durable results:
- `status/ITERATION_048_RESULT.md`
- `status/ITERATION_049_RESULT.md`
- `status/ITERATION_050_RESULT.md`
- `status/ITERATION_050_DENOMINATOR_CONTROL_RESULT.md`
- `status/ITERATION_051_RESULT.md`
- `status/ITERATION_051A_RESULT.md`
- `status/ITERATION_051B_RESULT.md`
- `status/ITERATION_052_RESULT.md`

## Active Iter051C — wider held-out sign-class range validation

Preregistered in `status/ITERATION_051C.md` at commit `1d3cd2b28d4f33cb18b89408962628254a2ed920` before implementation `e40189337d29efdda04c530f43242c21b8f54d3a` and workflow `9a68ab092b68cb2897d54006eab770fc7ebcf572`.

Frozen held-out points are H4 (`gamma=31/100`, `epsilon=31/1000`, `k=(41,-37,12,-16)/100`) and H5 (`gamma=245/100`, `epsilon=163/1000`, `k=(-22,47,-31,6)/100`). The eight complete Iter051A H1/H2 reference masks were frozen before production. Matrix: **192 exact lanes** = 2 points × 8 sign classes × 4 trees × 3 pairs, each with identical F=1 control.

Primary outcomes are `ITER051C_CONTROL_OR_RECONSTRUCTION_INVALID`, `K4_RR_SIGN_CLASS_RANGE_STABLE`, or `K4_RR_SIGN_CLASS_RANGE_DEPENDENT`.

PR #54 merged as `676760962d5177b7a045f4ebfac30c0ad4ca0da8`; authoritative run `34717183041`. H4 production is largely complete and H5 production has begun; consume only the terminal aggregate.

## Active Iter053 — exact global uniform contour-translation compatibility

Preregistered at `69e7786391b9f7e40b94acdbe73a9e7fc6828834` before implementation `8d88b179490c98e3670446f11dc28ca96914e4e2` and workflow `0bbf161eac2923af57e727e6d9b173a044f18077`. For `x_e=b_e+a_e·y`, collect exact 6×3 `A` and test whether all six frozen shifts arise from one common translation `y -> y-i epsilon v`, i.e. exact `A v=s`. Independently verify graph cycle-space criterion `B s=0` and tree-basis consistency.

Frozen matrix: **32 lanes** = 8 causal sign classes × 4 tree/cycle bases. Frozen classifiers: invalid, all-compatible, class-dependent, or `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`.

PR #55 merged as `6f06f99ea9fb6a261059757a9f7f80708558d9c5`; authoritative run `34718231048`, currently queued behind the active Iter051C load.

## Active Iter054 — exact sign-compatible affine contour chambers

Preregistered at `da8f756e3478d561d6001f251f93e70669b56aed` before implementation `cb500ce926ec0e987f78ecc5b04333fce6d8bc43` and workflow `7dd1b3052229b9d7d416e8f32ac3ad774a178732`. This stream is prospectively independent of Iter053 output.

With `M=diag(s)A`, test exact strict feasibility of one common affine direction

`M v > 0`.

Unlike Iter053, unequal positive edge shift magnitudes are allowed, but all six must arise from the same 3-vector `v`. Feasibility is decided exactly by strict separation/Gordan: zero must not lie in the convex hull of the six signed row normals. Infeasible lanes require exact Carathéodory obstruction certificates with support ≤4; feasible lanes require an independently verified exact integer witness.

Frozen matrix: **32 lanes** = 8 causal sign classes × 4 tree/cycle bases. Frozen classifiers: `ITER054_RECONSTRUCTION_OR_CERTIFICATE_INVALID`, `K4_CAUSAL_SIGN_CHAMBER_ALL_CLASSES_FEASIBLE`, `K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT`, or `K4_CAUSAL_SIGN_CHAMBER_NO_CLASS_FEASIBLE`.

PR #56 merged as `83dbee09ea0df0b7c3f65e373701dec36d7a960a`; authoritative run `34718445213`, currently queued behind the active runner load.

## Next allowed decisions

1. Consume Iter051C only at terminal aggregate. PASS = wider scoped sign-mask stability only; FAIL = retain range dependence without retuning.
2. Consume Iter053 only at terminal aggregate. Failure is scoped to equal-magnitude one-vector affine translation and is not a general contour no-go.
3. Consume Iter054 only at terminal aggregate. Its class taxonomy must be basis-consistent; do not alter the strict sign criterion or witness/certificate rules after output.
4. Iter051B rules out the eight preregistered coarse residue/cancellation selectors and Iter052 rules out the fixed canonical S3 cancellation identity. Do not fit replacement selectors or cancellation coefficients post hoc.
5. If affine contour tests are insufficient, the next gate must be a prospectively fixed genuinely correlated/multivariate contour or mathematically canonical residue construction with graph/permutation/tree-basis invariance built in.
6. K5 remains blocked until a genuinely multivariate source/analyticity-selected K4 prescription passes tree/cycle-basis/permutation/order independence plus exact EPRL control.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no physical causal-vertex finiteness/divergence theorem;
- no universal no-go theorem for causal EPRL;
- no global causal-sign universality theorem from finite held-out scans;
- no G3 PASS from a finite-part diagnostic;
- no F9/G8 promotion from symmetry/distributional surrogates;
- no arbitrary counterterm, fitted cancellation coefficient or preferred integration order;
- fixed causal-sector claims may not borrow `T+ + T- = D` cancellation without proof;
- distinguish ordinary absolute integrability, conditional/PV finite part and a source-defined distributional amplitude.
