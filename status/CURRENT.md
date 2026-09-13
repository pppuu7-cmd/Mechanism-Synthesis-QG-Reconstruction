# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `COMMON_EPSILON_SCHWARTZ_ACTION / EPSILON_TO_ZERO_DISTRIBUTIONAL_BOUNDARY_VALUE`

## Controlling recent results

- Iter068A run `34739048517`, artifact `10311807799`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. Denominator-skeleton necessary condition only.
- Iter068C authoritative run `34740924423`, artifact `10312555350`: `ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`; exact pre-pullback Eq.(5)/(6) algebra passes, gamma `0.2` missed its original finite-epsilon threshold.
- Iter069A run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: `ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT`.
- Iter069B run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`, `192/192` exact held-out cases. The naive ordinary improper real-cycle integral route is closed for the reduced K4 rational family only.
- Iter070C prereg `5d8f184f4c8b52a936bdf88b188b0f070e8e0c6f`, implementation `558f7a52810dcb48b4c1bf42e2eeb2bb50ff00dd`, head `2655c05ce4a91a6b21a88a899fc2a94eee5ee7e1`, run `34741632282`, aggregate job `103682249488`, artifact `10313090332`, digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: `ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`. At gamma `0.2`, frozen held-out final errors at epsilon `0.0015625` are about `0.00342`, `0.00707`, `0.00935`. This does not change Iter068C's terminal REVIEW classification and does not prove correlated pullback inheritance.
- Iter070A prereg `026f1ee074a0961b464226bfdb305f14fbc1bde0`, implementation `5944d57f68a4275203a852c1d45fa171cb66787e`, head `b72e0b70eab70ebf1a47eb24a195e6039e354d49`, run `34741624207`, aggregate job `103682359416`, artifact `10312736337`, digest `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`: `ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED`. `32/32` raw jobs and `64/64` exact cases valid; radial degree `{+6}`, explicit global polynomial-bound degree `{12}`. Every fixed `epsilon>0` reduced member defines a tempered distribution; no zero-regulator theorem follows.

## Active Iter071A

Gate: `ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_PILOT`.

- Frozen preregistration: `dd13d17c729447d01fd262bce3d2ae5bcc06396b`.
- Original implementation: `918623d8be4e5e59d8f40cb29e1f9deac6c1a301`.
- Initial production head/run: `61f1c83d96388c51a15e516862c8a9bb60307ed2` / `34741885070`.
- First causal failure: after the scientific estimator completed, JSON serialization rejected a NumPy boolean scalar (`TypeError: Object of type bool is not JSON serializable`) before any raw artifact could be written. This is `INFRASTRUCTURE/IMPLEMENTATION_INVALID`, not a scientific FAIL or REVIEW.
- Minimal repair: `9c78128d144741f528338ec7613c4b268c7b76f7` casts output metadata/predicate scalars to native Python JSON types only. Frozen test functions, epsilon grid, Sobol seeds/sample budget, thresholds and interpretation rule are unchanged.
- **Authoritative repaired run:** `34741938861`, head `9c78128d144741f528338ec7613c4b268c7b76f7`.
- Frozen matrix: `8` physical sigma classes x `4` K4 tree/cycle bases = `32` independent jobs, `fail-fast:false`.
- Three preregistered physical edge-flow Schwartz tests, common source epsilon ray `0.20 -> 0.0125`, four independent Sobol scrambles of `2^16` points, plus aggregate tree-basis covariance.

No Iter071A scientific classification is permitted until the repaired run is terminal and its raw artifacts plus frozen aggregate are consumed.

## Exact blocker / next decision

Fixed positive epsilon is now qualified at the reduced K4 level; the missing bridge is the source-selected correlated `epsilon -> 0+` boundary value and its Eq.(5)/(6) inheritance through non-transverse K4/K5 collision pullback.

After Iter071A terminal classification, the next gate must be theorem-oriented: controlled Schwartz-seminorm/tube-holomorphy or microlocal proof/localization. A finite-panel numerical PASS cannot itself promote K5.

Do not return to ordinary improper real-cycle integration or preferred sequential finite parts: Iter069 and Iter046 already close those routes for the reduced K4 family.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL/contour no-go theorem;
- no physical causal-sector selection from tournament/microlocal-skeleton results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation, or preferred sequential order/tree;
- retain published spectral `i epsilon`; do not replace it by `beta+i epsilon`;
- distinguish ordinary/absolute integrability, conditional/PV finite part, fixed-epsilon tempered distribution, source-defined boundary value and microlocal product existence.
