# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `COMMON_EPSILON_LEADING_COLLISION / EPSILON_TO_ZERO_DISTRIBUTIONAL_BOUNDARY_VALUE`

## Controlling recent results

- Iter068A run `34739048517`, artifact `10311807799`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. Denominator-skeleton necessary condition only.
- Iter068B run `34740962426`, aggregate artifact `10311749011`: `ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES`. This closes the separate-contact ordinary Hörmander-product route, not the jointly regulated source family.
- Iter068C authoritative run `34740924423`, artifact `10312555350`: `ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`; exact pre-pullback Eq.(5)/(6) algebra passes, gamma `0.2` missed its original finite-epsilon threshold.
- Iter069A run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: `ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT`.
- Iter069B run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`, `192/192` exact held-out cases. The naive ordinary improper real-cycle integral route is closed for the reduced K4 rational family only.
- Iter070A run `34741624207`, aggregate job `103682359416`, artifact `10312736337`, digest `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`: `ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED`. Every fixed `epsilon>0` reduced member defines a tempered distribution; no zero-regulator theorem follows.
- Iter070C run `34741632282`, aggregate job `103682249488`, artifact `10313090332`, digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: `ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`. This does not change Iter068C's terminal REVIEW and does not prove correlated pullback inheritance.

## Terminal Iter071A

Gate: `ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_PILOT`.

- Frozen preregistration: `dd13d17c729447d01fd262bce3d2ae5bcc06396b`.
- Initial run `34741885070`: implementation-invalid only because NumPy boolean JSON serialization prevented raw artifacts; no scientific classification.
- Minimal serialization-only repair / authoritative head: `9c78128d144741f528338ec7613c4b268c7b76f7`.
- Authoritative repaired run: `34741938861`.
- Aggregate job: `103683058319`.
- Aggregate artifact: `10312601343`.
- Aggregate digest: `sha256:53adba7a50db94dfdeac5f340d569bc5b079672f310536858a86f12602904544`.
- `32/32` scientific matrix lanes completed and are numerically valid.
- Frozen terminal classification: `ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_REVIEW`.
- `all_lane_convergence_predicates=false`; `basis_covariance_pass=false`; worst finite-sample normalized basis spread `4.40981603077861` at `sigma=+-++`, `epsilon=0.0125`, `G1`.

Raw causal audit across all four cycle bases for the worst sigma confirms valid geometry and finite estimates but rapidly growing small-epsilon QMC variance, failed final Cauchy contraction and failed step-improvement predicates. This is a `SCOPED REVIEW / NUMERICAL-RESOLUTION BLOCKER`, not a theorem of divergence or non-existence. Frozen Iter071A criteria are unchanged. Durable result: `status/ITERATION_071A_RESULT.md` commit `7e88c075e9d05976eb7337a0462361ebfbdb296f`.

## Active Iter072A

Gate: `K4_COMMON_EPSILON_LEADING_COLLISION_SCHWINGER_CONE_THEOREM`.

- Prospective preregistration, before implementation: `1e011e9804ee2cde41260039c551f77562c68a4c`.
- Lane implementation: `39a60064ea666dc9d021396eec20324d70b2b9cc`.
- Frozen aggregate implementation: `1a4ff3698a119f7e20acfe7f55c77fd3e7bab1f5`.
- Production workflow/head: `9ac6e5f766b73531c58de9d5cf636033189274a5`.
- Production run: `34744136699`.
- Matrix: eight physical factorized sigma lanes, `fail-fast:false`, each recomputing all four K4 cycle bases with exact rational/integer algebra.

Iter072A replaces denser x-space quadrature with the exact blow-up `y=epsilon z` and Schwinger/Fourier cone representation of the candidate `epsilon^-3` full-collision coefficient. It tests exact rank, strict positive circulation, independent strong-tournament equivalence, positive-cone dimension, all proper-stratum divergence degrees, source numerator/test constant terms, basis covariance and a deliberately wrong orientation negative control. It is not a repeat of Iter068A: the target is the leading common-epsilon boundary-value asymptotic coefficient, not merely denominator-product Hörmander compatibility.

No scientific classification is permitted until run `34744136699` is terminal and its lane artifacts plus frozen aggregate are consumed.

## Exact blocker / next decision

The missing bridge remains the source-selected correlated `epsilon -> 0+` boundary value and its Eq.(5)/(6) inheritance through non-transverse K4/K5 collision pullback.

If Iter072A validates a nonzero `epsilon^-3` leading coefficient for some source classes, that result remains scoped to the reduced common-epsilon K4 rational family and does not physically select sectors or prove divergence of the complete causal vertex. If the coefficient vanishes for other classes, their subleading boundary-value behavior remains open.

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
