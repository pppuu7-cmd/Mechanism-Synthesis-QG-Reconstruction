# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / authoritative front

- Candidate: `CRQN v0.2`, `CARRIER_SELECTED` only for source-backed F1-F8 carrier/mechanism structure.
- Predictive local K5 amplitude: `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`.
- Physical F9: `BLOCKED`.
- Deepest coefficient-selector blocker: `RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.
- Stratified collision/forest geometry is defined and physical K3/K4/K5 non-L1 strata are prospectively validated in the frozen minimal-spin sector.
- Linearized/tubular local nested-normal forest scheme construction is now closed in scoped form by Iter082D.
- Current analytic blocker: **`K5_NONLINEAR_TUBULAR_CHART_OVERLAP_AND_EXTENSION_CLASS_INDEPENDENCE`**.
- Causal composition blocker: `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
- Han causal-stack blocker: `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
- RG/refinement: `BLOCKED_E9_COARSE_FINE_MAP_MISSING`.
- G3 remains downstream-locked.

**Physical active front:**

`K5_NONLINEAR_TUBULAR_CHART_OVERLAP_AND_EXTENSION_CLASS_INDEPENDENCE / RIGHT_SU2_COVARIANT_INVARIANT_JET_SELECTOR / RUHL_MOTIVATED_CORRELATED_ANALYTIC_BOUNDARY_VALUE / CAUSAL_MULTIVERTEX_E3_E4_E6_SOURCE_BRIDGE`.

## Latest authoritative scoped result — Iter082D

Durable result:

`results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md`

commit `ccd69c0c204b45aa58a0cde3e2a9ab08fe75a794`.

Prospective chain:

- preregistration `09b1affb5489e0dfcbe01b0100e0fc8a44aded98`;
- implementation `ed15c5436a3d83b0119faea9a94e9f7a74b76189`;
- production `6b60bdeb6497883b92429719988b4869cd552e5b`;
- Action run `34894909845`, job `104146361380`, terminal success;
- artifact `10368183868`;
- artifact ZIP digest `sha256:9d53b4e491e3b9698acb7f1a4880413ea123c0f4508d3b9296328226175e930e`;
- extracted aggregate JSON SHA256 `59da0938b82730bf51c6ed98f3da838216732a279a4559fee7e48ba8c867c35f`.

Classification:

`ITER082D_SM_K5_NESTED_NORMAL_PROJECTOR_TAYLOR_FOREST_SCHEME_CLASS_CONSTRUCTED_EXACT_SCOPED`.

Verdict: `PASS_EXACT_SCOPED`.

### Exact nested-normal geometry

For each collision block `B`, Iter082D constructs the label-free barycentric projector

`P_B[i,j] = delta_ij - 1/|B|` for `i,j in B`.

For every maximal chain `B3 subset B4 subset B5`, define

`A=P_B3`, `B=P_B4-P_B3`, `C=P_B5-P_B4`.

All 20 maximal chains satisfy exactly:

- one-component ranks `(2,1,1)`;
- pairwise orthogonality and idempotence;
- `A+B+C=P_B5`;
- after tensoring with the physical three boost-vector components, transverse dimensions `(6,3,3)` and total 12.

All 16 block projectors are symmetric, idempotent, have rank `|B|-1`, and annihilate common translation.

### Exact S5 transport

All 120 permutations were checked:

- 1920/1920 block-projector covariance checks pass;
- 7200/7200 chain-increment covariance checks pass;
- a deliberately label-dependent projector is rejected by the same validator.

### Taylor / scheme control

The exact finite polynomial control contains all 286 degree triples `(a,b,c)` with total degree <=10 in the three orthogonal nested normal groups.

Taylor visibility is frozen by the physical scaling-degree bounds:

- K3: `a<=0`, `omega_3=0`;
- K4: `a+b<=3`, `omega_4=3`;
- K5: `a+b+c<=8`, `omega_5=8`.

Required subtraction gives radial remainder exponent 0 for K3/K4/K5; one-order under-subtraction gives exactly `-1` in each case.

Two genuinely distinct admissible weight-jet schemes were applied through the full inner-to-outer operator `W5 o W4 o W3`:

- scheme difference is nonzero;
- 198 input degree classes contribute to it;
- 88 input classes lie in the common kernel of all allowed Taylor-jet maps;
- all 88/88 common-kernel inputs are annihilated by the scheme difference;
- invisible-input violations: 0.

The direct sequential operator equals the exact noncommutative expansion of `(I-T5)(I-T4)(I-T3)`. This equality is a same-graph consistency identity only and is not counted as a selector equation, in accordance with CDSR T4.

### Negative controls

All six frozen invalid constructions were injected and mechanically rejected:

1. label-dependent projector;
2. under-subtraction;
3. bad weight with forbidden low-order normal jet;
4. source-order/contact-multiplication violation;
5. numeric finite-part smuggling;
6. reassociation-as-selector smuggling.

No finite coefficient, scale or invariant-jet value was selected.

### Iter082D ceiling

Iter082D establishes an explicit **linearized/tubular local** source-covariant nested-normal forest scheme class. It does **not** establish:

- nonlinear chart independence on `SL(2,C)^4`;
- a global Toller forest extension;
- physical equivalence of different symbolic weight schemes;
- a source-derived finite-part selector;
- exact total physical ambiguity dimension;
- sufficiency of 28 conditions;
- regulator independence;
- causal closure, RG closure, CRQN v0.3, `NEW_PHYSICS_FOUND`, or complete QG.

## Iter082C implementation quarantine

Historical chain:

- prereg `3a8dcdd732065540abf753f5f0e891ddc9257632`;
- implementation `8c07f6f6dd8fe5f1191a1bdd783a7e20d470797a`;
- production `11a6bfd2ca8d9ac4d336e2c9528b694955316076`;
- run `34894401672`, job `104144670722`, terminal CI success;
- artifact `10367754339`, ZIP digest `sha256:d80d2fb36a0a14edc531bc9b21a402215daed1d34d7393068bb5f169e6d3e661`.

Controlling review:

`results/ITER082C_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `974bb1c9d1c1d0dd3ff4078aed199e7d1691226f`.

Verdict: **`INVALID_IMPLEMENTATION`**.

The green CI must not be cited as a scientific PASS. It failed to implement the preregistered quotient-normal coordinates and nontrivial nested scheme comparison, and several negative controls were preassigned outcomes. Its useful single-block Taylor observations are superseded by the prospectively repaired Iter082D implementation.

## Physical forest authority before Iter082D

### Iter082A — partial-stratum physical non-L1 witnesses

`results/ITER082A_SM_INDEPENDENT_NESTED_PARTIAL_COLLISION_REPRODUCTION_RESULT.md`, commit `3c55965658ea319b4491a468507ed57d97344835`.

- K4: 32/32 nonzero minimal boundary components, `q=-12`, normal dimension 9, absolute-L1 margin `-3`.
- K3: 24/32 nonzero minimal boundary components, `q=-6`, normal dimension 6, logarithmic absolute-L1 failure (`margin=0`) where the leading coefficient is nonzero.
- deepest K5 sanity: 32/32 nonzero.

### Iter082B — exact forest combinatorics

`results/ITER082B_SM_K5_SOURCE_COVARIANT_FOREST_EXTENSION_ARCHITECTURE_RESULT.md`, commit `be61c2fb5cc16a7b92e240906c17f87fcb61b5ec`.

- 16 divergent blocks: 10 K3, 5 K4, 1 K5;
- 72 forests, sizes `{0:1,1:16,2:35,3:20}`;
- 20 maximal `K3 subset K4 subset K5` chains;
- all 120 S5 permutations checked;
- 8 forest orbits.

Iter082B is combinatorial architecture only; Iter082D supplies the later linearized nested-normal/Taylor operator realization.

## Critical right-SU2 repair and selector target

Historical Iter077Q infinite-dimensional tangential physical application remains `INVALID_SOURCE_LOCK`: exact node-wise right-SU2 covariance makes nonconstant historical scalar tangential multipliers non-source-compatible on `N=SU(2)^4`.

Corrected authority Iter081R:

- invariant scalar normal-jet dimensions `d_0..d_8=[1,0,1,0,3,0,7,0,16]`;
- demonstrated deepest-stratum scalar invariant subspace/lower bound: `dim J_inv=28`.

This is not the exact total physical ambiguity dimension and does not imply that 28 conditions suffice.

Iter081S gives only

`m<28 => dim ker(L|J_inv) >= 28-m >0`.

At `m>=28`, injectivity is algebraically possible on the demonstrated subspace only; physical authority, full-sector sufficiency and the physical equivalence quotient remain open.

Iter081W further shows exact transverse dilation covariance still leaves the 16-dimensional invariant order-8 resonant sector.

Iter081T establishes that CRQN v0.1/v0.2 contains no pre-existing corrected source-ordered selector for this target.

## Finite spectral epsilon

Iter081U remains authoritative in scope:

`ITER081U_SM_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED`.

Finite one-wedge spectral epsilon leaves the frozen minimal-sector deepest leading `beta^-2` matrices / K5 `q=-20` collision unchanged. This is a diagnostic only and does not exclude correlated group-variable/forest analytic regularization.

## Causal / Han locks

Selected-Toller one-wedge and natural two-wedge Han-type `d^2` bounds fail in the frozen minimal block; standard Han stack machinery cannot simply be inherited by one selected Toller branch.

Causal E3/E4/E6 many-vertex inheritance remains `BLOCKED_SOURCE_BRIDGE`.

No universal causal-vertex divergence/nonexistence theorem follows.

## CDSR structural interface

Controlled import records:

- `status/CDSR_STRUCTURAL_IMPORT_AND_INTERFACE.md`;
- `status/CDSR_STRUCTURAL_IMPORT_MANIFEST.json`.

CDSR remains independent.

Imported structural tools:

1. `SAME_GRAPH_REASSOCIATION_SELECTOR_BLIND_SCOPED`: reassociation/parenthesization of the same fixed decorated graph gives no independent selector equation.
2. `REGULAR_CONTEXT_NORMAL_JET_PAIRING_DIAGNOSTIC_SCOPED`: a regular context sees supported extension data through normal jets; for a declared context family the invisible sector is `ker J_K`, but distinguishing extensions is not selecting one without independently source-fixed target values/relations.

Iter082D obeys these firewalls. The CDSR selector audit interface is **not yet ready**, because MSQGR still lacks a nonlinear chart-independent extension object and complete physical insertion/composition/context maps.

`CDSR_REMAINS_INDEPENDENT = YES`.

## Exact blockers

1. `K5_NONLINEAR_TUBULAR_CHART_OVERLAP_AND_EXTENSION_CLASS_INDEPENDENCE`.
2. `RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR` plus partial-stratum finite coefficient/scale selector.
3. `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
4. `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
5. `E7_E8_DISTRIBUTIONAL_EXTENSION_TRANSPORT_OR_SELECTOR`.
6. `RG_REFINEMENT_E9_COARSE_FINE_BOUNDARY_MAP_AND_MATCHING_FUNCTIONAL`.
7. `REGULATOR_INDEPENDENCE_AFTER_NONLINEAR_ANALYTIC_OBJECT_DEFINITION`.

## Corrected survival chain

`F1-F8 carrier`
`-> source-ordered K5`
`-> Iter081X / Iter082A / Iter082B exact physical stratified forest architecture`
`-> Iter077I deepest non-L1 + Iter077L/M supported extension freedom`
`-> Iter077Q physical infinite tangential W INVALID_SOURCE_LOCK`
`-> Iter081R >=28 invariant deepest scalar normal jets`
`-> Iter081T no hidden corrected CRQN selector`
`-> Iter081W >=16 resonant jets after exact dilation law`
`-> Iter081U finite spectral epsilon does not L1-regularize deepest collision`
`-> Iter082C green CI INVALID_IMPLEMENTATION`
`-> Iter082D explicit label-free linearized/tubular nested-normal + Taylor forest scheme class PASS_EXACT_SCOPED`
`-> nonlinear SL(2,C)^4 tubular chart-overlap / chart-independence ?`
`-> chart-independent local/global Toller forest extension class ?`
`-> finite coefficient/scale/invariant-jet selector ?`
`-> causal E3/E4/E6 ?`
`-> CDSR rank/equivalence/no-smuggling audit once immutable physical interface exists`
`-> regulator independence / RG / continuum / GR / matter / observables ?`.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no physical selector; no exact total extension-space dimension; no theorem that 28/16 conditions suffice physically; no generic-spin fully contracted non-L1 theorem; no causal-vertex distributional nonexistence theorem; no nonlinear/global forest-extension theorem; no regulator independence; no G3/F9/G8/K5 promotion; no arbitrary fitted subtraction constants/scales or preferred finite parts.

## Next admissible work

1. Prospectively freeze `K5_NONLINEAR_TUBULAR_CHART_OVERLAP_AND_EXTENSION_CLASS_INDEPENDENCE_GATE`.
2. Compare at least two explicit nonlinear local charts on the relevant `SL(2,C)^4` neighborhood of the compact collision strata, with transition maps frozen before outcome inspection.
3. Transport the Iter082D nested normal projectors/Taylor jets through the nonlinear transitions and test whether chart changes modify the extension only by supported jets within the authoritative K3/K4/K5 order bounds `(0,3,8)`.
4. Keep all finite coefficients, analytic scales and deepest invariant-jet coefficients symbolic.
5. Treat chart compatibility as an admissibility/extension-class question, not a selector equation.
6. In parallel, continue genuinely independent source work on correlated Ruhl/Toller boundary-value laws and the causal E3/E4/E6 many-vertex bridge.
