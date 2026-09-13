# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `COMMON_EPSILON_SIGNED_CUTSPACE / EPSILON_TO_ZERO_DISTRIBUTIONAL_BOUNDARY_VALUE`

## Controlling recent results

- Iter068A run `34739048517`, artifact `10311807799`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. Denominator-skeleton necessary condition only.
- Iter068B run `34740962426`, aggregate artifact `10311749011`: `ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES`. Separate-contact ordinary Hörmander-product route only; jointly regulated family remains distinct.
- Iter069A run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: exact generic radial degree `+6`.
- Iter069B run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `192/192` held-out exact support for degree `+6`; naive ordinary improper real-cycle integral route is closed for the reduced K4 rational family only.
- Iter070A run `34741624207`, aggregate job `103682359416`, artifact `10312736337`, digest `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`: every fixed `epsilon>0` reduced member is tempered; no zero-regulator theorem follows.
- Iter070C run `34741632282`, aggregate job `103682249488`, artifact `10313090332`, digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: low-gamma smaller-epsilon pre-pullback convergence support; historical Iter068C remains REVIEW.

## Terminal Iter071A

- Preregistration: `dd13d17c729447d01fd262bce3d2ae5bcc06396b`.
- Initial run `34741885070`: implementation-invalid only (NumPy boolean JSON serialization), no scientific classification.
- Minimal repair / authoritative head: `9c78128d144741f528338ec7613c4b268c7b76f7`.
- Authoritative run `34741938861`; aggregate job `103683058319`; artifact `10312601343`; digest `sha256:53adba7a50db94dfdeac5f340d569bc5b079672f310536858a86f12602904544`.
- `32/32` lanes numerically valid.
- Frozen classification: `ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_REVIEW`.
- `all_lane_convergence_predicates=false`, `basis_covariance_pass=false`; worst normalized finite-sample basis spread `4.40981603077861` at `sigma=+-++`, `epsilon=0.0125`, `G1`.
- Causal raw audit: finite valid geometry but rapidly growing small-epsilon QMC variance and failed Cauchy/step-improvement predicates. This is a scoped numerical-resolution REVIEW, not a divergence/non-existence theorem.
- Durable result commit: `7e88c075e9d05976eb7337a0462361ebfbdb296f`.

## Terminal Iter072A

Gate: `K4_COMMON_EPSILON_LEADING_COLLISION_SCHWINGER_CONE_THEOREM`.

- Prospective preregistration: `1e011e9804ee2cde41260039c551f77562c68a4c`.
- Lane implementation: `39a60064ea666dc9d021396eec20324d70b2b9cc`.
- Aggregate implementation: `1a4ff3698a119f7e20acfe7f55c77fd3e7bab1f5`.
- Authoritative production head: `9ac6e5f766b73531c58de9d5cf636033189274a5`.
- Run: `34744136699`.
- Aggregate artifact: `10313745085`.
- Aggregate digest: `sha256:263f46b94d10835e3ec156e553697f98ca213d5619ef1f58a6ff57c8d9ffb96d`.
- Frozen classification: `ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL`.

Causal classification is scientific, not infrastructure/numerical. The run correctly recovers the strong-tournament classes and the same constructive positive-circulation classes, and all proper denominator strata have degree below the full-collision degree 3. The failed premise is the attempted identification of the Schwinger delta space with the circulation space. For `x=L y`, Schwinger/Fourier integration imposes `L^T diag(s)t=0`; hence `diag(s)t` lies in `ker(L^T)`, the K4 cut space, whereas Iter058's positive circulation lives in `ker(B)`, the cycle space. The spaces are dual, not identical. Frozen Iter072A is therefore not repaired or rerun under changed science.

Durable result: `status/ITERATION_072A_RESULT.md`, commit `17ab9e05174ebd10037163237a1a84e985782198`.

## Active Iter072B

Gate: `K4_SCHWINGER_SIGNED_CUTSPACE_LEADING_COEFFICIENT`.

- Prospective preregistration before implementation: `b334f75f4ffa15a1148a178fca20bc6def465ecf`.
- Exact lane implementation: `7f987a81f657cbe0c1ced4cca53db0648a2d99e4`.
- Frozen aggregate: `f3763327e6e44eeb806e00b5d63062868e6a576d`.
- Production workflow/head: `c04afc38db5d8ff454246574e784b89648a73b5e`.
- Production run: `34744334585`.
- Eight source sigma lanes, `fail-fast:false`; every lane recomputes all four cycle bases with exact algebra.

Frozen hypothesis: the strict-positive Schwinger kernel `L^T diag(s)t=0`, `t>0`, has nonempty 3D relative interior iff the source tournament is acyclic/transitive. The gate independently checks topological order, exhaustive vertex-potential orders, exact cut-space witness, rank/kernel dimension, proper-stratum power separation, source/test constant terms, basis covariance, and a wrong-sign-map negative control.

No scientific classification before terminal raw artifacts + aggregate are consumed.

## Exact blocker / next decision

The missing bridge remains the source-selected correlated `epsilon -> 0+` boundary value and Eq.(5)/(6) inheritance through non-transverse K4/K5 pullback. Even an Iter072B PASS would classify only the leading full-collision `epsilon^-3` coefficient of the reduced K4 common-epsilon rational family. For classes with vanishing leading coefficient, subleading and proper-collision behavior remains open.

K5 remains blocked until a source-faithful correlated extension object and distributional inheritance theorem are available.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL/contour no-go theorem;
- no physical causal-sector selection from tournament/microlocal/asymptotic results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation, or preferred sequential order/tree;
- retain published spectral `i epsilon`; do not replace it by `beta+i epsilon`;
- distinguish ordinary/absolute integrability, conditional/PV finite part, fixed-epsilon tempered distribution, source-defined boundary value and microlocal product existence.
