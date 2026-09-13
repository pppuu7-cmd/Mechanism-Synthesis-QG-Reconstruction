# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `COMMON_EPSILON_BOUNDARY_VALUE / TRANSITIVE_FACE_COEFFICIENTS / INDEPENDENT_WEDGE_EPRL_CONTROL`

## Controlling recent results

- Iter068A run `34739048517`, artifact `10311807799`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. Denominator-skeleton necessary condition only.
- Iter068B run `34740962426`, aggregate artifact `10311749011`: `ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES`. Separate-contact ordinary Hörmander-product route only; jointly regulated family remains distinct.
- Iter069A run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: exact generic radial degree `+6`.
- Iter069B run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `192/192` held-out exact support for degree `+6`; naive ordinary improper real-cycle integral route is closed for the reduced K4 rational family only.
- Iter070A run `34741624207`, aggregate job `103682359416`, artifact `10312736337`, digest `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`: every fixed `epsilon>0` reduced member is tempered; no zero-regulator theorem follows.
- Iter070C run `34741632282`, aggregate job `103682249488`, artifact `10313090332`, digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: low-gamma smaller-epsilon pre-pullback convergence support; historical Iter068C remains REVIEW.
- Iter071A run `34741938861`, aggregate job `103683058319`, artifact `10312601343`, digest `sha256:53adba7a50db94dfdeac5f340d569bc5b079672f310536858a86f12602904544`: `ITER071A_K4_COMMON_EPSILON_SCHWARTZ_ACTION_REVIEW`; 32/32 lanes numerically valid, frozen convergence/basis predicates fail under rising small-epsilon QMC variance; no divergence theorem.
- Iter072A run `34744136699`, artifact `10313745085`, digest `sha256:263f46b94d10835e3ec156e553697f98ca213d5619ef1f58a6ff57c8d9ffb96d`: `ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL`; cycle-space positive circulation is not the Schwinger cut-space constraint.
- Iter072B run `34744334585`, aggregate job `103689386630`, artifact `10313588852`, digest `sha256:4ab193fb0e66cabfe48ce6fa1bdad180154d00c2f7a258b933f729f9e09db48f`: `ITER072B_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_TRANSITIVE_TOURNAMENT_SCOPED`. Strict-positive full-set cut-space kernel has nullity 3 exactly for source sigma `++++`, `+++-`, `++--`, `+---`.
- Iter073A prereg `8b87abc4aea6636b9e554729bba4670b91d9e7f3`, head `9fb30be9831c01b4e13571e5dac2569fb95667d5`, run `34746503186`, aggregate job `103695339471`, artifact `10314755546`, digest `sha256:b1c46b3ac61eb4416df337514f1610a34c40e74901e6b765c8ffbd84f345fe7a`: `ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_EXACT_SCOPED`. Four transitive source classes each have proper histogram `(3,1)x2,(4,1)x1,(5,2)x3`; four nontransitive source classes have no positive-admissible proper face. Durable result `status/ITERATION_073A_RESULT.md`.
- Iter073B prereg `e89805765ba2c993ba5b1f082586675543cd9eba`, head `dbd3fcf56a8060c508bf065e012961b99a7c366f`, run `34748536488`, job `103700759855`, artifact `10315061564`, digest `sha256:b5d1638a7bada9ed6371d46bcee6526d9f61abd06668458370fe63e482cc96cd`: `ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_EXACT_SCOPED`. Full independent-wedge census: 24/64 transitive/full-positive, 40/64 cyclic; maximal proper nullity distribution `-1:24, 1:16, 2:24`. The eight source-factorized vectors are recovered exactly as a strict subset. Durable result `status/ITERATION_073B_RESULT.md`.
- Iter073C prereg `77af541dfe371632c92eb3e5cda176511be7eef7`, head `291a9f6a71265c9e768960bbc0d00f039ca352c5`, run `34748542204`, job `103700784152`, artifact `10315585117`, digest `sha256:27fd61945577078dd4dd16d85015b067073943ba87745dbdaa167450f81514c5`: `ITER073C_NONTRANSITIVE_ALL_FACES_EXACT_STIEMKE_SEPARATED_SCOPED`. Exact Stiemke/Gordan certificates exist for all 1008 nontransitive `(source class,basis,nonempty subset)` cases; 1000 certificates have primitive L1=1 and 8 have L1=2; minimum positive integer margin is 1. This is positive-real nonpinch separation, not epsilon->0 boundedness. Durable result `status/ITERATION_073C_RESULT.md`.
- Iter073D is prospectively frozen and launched as run `34748577817` on head `48a21509026968b7bd7edc72f1ef759c585f1882`; it audits exact extreme-ray/relative-interior geometry of the six allowed proper faces in each transitive source class. At this snapshot it is queued and non-terminal.

## Exact blocker after Iter073B/C

The reduced K4 signed cut-space geometry is now unusually constrained:

1. the complete 64-sign independent-wedge space is exactly classified;
2. the four nontransitive source classes have no positive full or proper face and possess explicit exact Stiemke separation certificates on every nonempty subset;
3. the four transitive source classes retain a finite set of positive full/proper faces, whose cone geometry is being audited in Iter073D.

What remains scientifically decisive is not another sign census. The next high-value work is:

- determine actual regulated asymptotic coefficients on the transitive positive faces, including numerator/Jacobian factors and possible cancellations;
- convert exact separation for nontransitive source classes into a scoped analytic bound or boundary-value theorem, rather than assuming no positive pinch implies convergence;
- study the independent-wedge 64-sign sum at the **correlated boundary-value** level and determine whether the Eq.(5)/(6)-type control survives non-transverse pullback;
- lift any K4 theorem from the reduced rational family to the source-backed full Toller/group object before using it in K5.

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
