# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `COMMON_EPSILON_SCHWARTZ_ACTION / EPSILON_TO_ZERO_DISTRIBUTIONAL_BOUNDARY_VALUE`

## Controlling source/direct chain

- Primary source snapshot commit `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`: Bianchi-Chen-Gamonal arXiv `2601.23162`, DOI `10.1103/fwql-t4yr`; pins Eq.(3) spectral Feynman `i epsilon`, Eq.(4) direct ten-wedge fixed-causal vertex, Eq.(5) `T+ + T-=D`, Eq.(6) unconstrained independent-wedge EPRL sum, Eq.(7) Cartan/magnetic representation.
- Iter064A run `34732198011`: `ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`.
- Iter064B run `34732360103`: `ITER064B_K4_SOURCE_PREREQUISITES_CLOSED_FOR_K5_QUALIFICATION`.
- Iter065A run `34732545131`: `ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`.
- Iter066A run `34734333416`: `ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING`.
- Iter067A run `34736725079`: `ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN`.
- Iter068A run `34739048517`, artifact `10311807799`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. Necessary denominator-skeleton classification only.
- Iter068C run `34740924423`, artifact `10312555350`: `ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`. Exact Eq.(5)/(6) pre-pullback algebra passes; gamma `0.2` missed the original frozen finite-epsilon threshold.
- Iter069A run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: `ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT`. All four exact bases give source radial degree `+6`, control `-6`; source leading homogeneous coefficient is causal-sign/epsilon/external-flow independent.
- Iter069B run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`, `192/192` exact held-out cases. This closes naive ordinary improper real-cycle integration only for the reduced K4 rational family.
- Iter070C prereg `5d8f184f4c8b52a936bdf88b188b0f070e8e0c6f`, head `2655c05ce4a91a6b21a88a899fc2a94eee5ee7e1`, run `34741632282`, aggregate job `103682249488`, aggregate artifact `10313090332`, digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: `ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`. At gamma `0.2`, the three held-out errors decrease strictly to approximately `0.00342`, `0.00707`, `0.00935` at epsilon `0.0015625`. Iter068C remains terminal REVIEW; no correlated pullback theorem follows.
- Iter070A prereg `026f1ee074a0961b464226bfdb305f14fbc1bde0`, implementation `5944d57f68a4275203a852c1d45fa171cb66787e`, head `b72e0b70eab70ebf1a47eb24a195e6039e354d49`, run `34741624207`, aggregate job `103682359416`, aggregate artifact `10312736337`, digest `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`: `ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED`. `32/32` raw jobs and `64/64` exact cases valid; radial degree `{+6}`, explicit global polynomial-bound degree `{12}`. Every fixed `epsilon>0` reduced family member is smooth on real cycle space and defines a tempered distribution. This is not an `epsilon->0+` boundary-value theorem.

## Active production

### Iter071A — correlated common-epsilon K4 Schwartz-action convergence pilot

- Preregistration: `dd13d17c729447d01fd262bce3d2ae5bcc06396b`
- Implementation: `918623d8be4e5e59d8f40cb29e1f9deac6c1a301`
- Authoritative launch/head: `61f1c83d96388c51a15e516862c8a9bb60307ed2`
- Production run: `34741885070`
- Matrix: `8` physical sigma classes x `4` exact K4 tree/cycle bases = `32` independent jobs, `fail-fast:false`.
- Frozen source ray: common epsilon `0.20,0.10,0.05,0.025,0.0125` at gamma `6/5`, zero external flow.
- Three preregistered edge-flow Schwartz tests `G0/G1/G2` are paired with the full reduced joint kernel using four independent Sobol scrambles (`2^16` points each).
- Frozen controls: Gaussian whitening validity, finite estimates, scramble stability, final common-epsilon Cauchy bound/trend, and aggregate tree-basis covariance. No adaptive sample increase or threshold weakening is allowed after output.
- Allowed terminal results: scoped convergence-pilot support, REVIEW, or numerical-validity failure. Even PASS is not a theorem of a unique `S'` boundary value or arbitrary-path independence.

## Exact K5 blocker after Iter070A/070C

The reduced K4 finite-spectral family is now qualified as a tempered distribution at every fixed positive epsilon, but the physical correlated zero-regulator bridge is still missing.

Unresolved requirements:

1. demonstrate or prove a source-selected correlated `epsilon->0+` boundary value in `S'` (Iter071A is only a finite-panel numerical pilot);
2. establish a canonical tube/holomorphy or microlocal construction and uniqueness without arbitrary local counterterms or preferred tree/cycle/integration order;
3. prove Eq.(5)/(6) inheritance through the non-transverse correlated K4/K5 boundary value/pullback, not merely the independent-edge pre-pullback tensor product;
4. only after those steps may a K5 direct causal-vertex construction be qualified.

This remains `BLOCKED`, not a theorem of physical vertex divergence or nonexistence.

## Retained structural localization

- Iter046: the sequential one-dimensional K4 finite-part rule is order/forest dependent; preferred order/tree is forbidden.
- Iter058: exact K4 strict-chamber feasibility iff strong tournament connectivity.
- Iter059: source-backed equal-spin Toller wedge reversal gives branch swap under group inversion.
- Iter060: the K4 tournament/positive-circulation analyticity surrogate is covariant under that reversal law.
- Iter061: orientation-blind physical-kappa / ordered-spectral-sign identification is obstructed.
- Iter062: minimal ordered bridge `s(a,b)=c eta(a,b) kappa_ab` is covariant but retains an unfixed global convention.

## Next admissible step

Consume every terminal Iter071A raw artifact and frozen aggregate. If its numerical-validity controls pass, use its result only to decide the next theorem-oriented gate: either strengthen common-ray `S'` convergence with analytically controlled Schwartz seminorm bounds / source tube holomorphy, or localize any sigma/basis/test failure before attempting a K5 collision construction. Do not promote a finite-panel numerical PASS into a boundary-value theorem.

Do not return to ordinary improper real-cycle integration or a preferred sequential finite part: Iter069 and Iter046 already close those routes for the reduced K4 family.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament or microlocal-skeleton results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order/tree;
- do not replace published spectral `i epsilon` with `beta+i epsilon`;
- keep ordinary/absolute integrability, conditional/PV finite part, fixed-epsilon tempered distribution, source-defined distributional boundary value, and microlocal product existence distinct.
