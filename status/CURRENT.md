# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `EPSILON_MINUS1_OVERLAP_COEFFICIENT / TRANSITIVE_FACE_COEFFICIENTS / TOLLER_BRANCHFLIP_RECURRENCE / CORRELATED_BOUNDARY_VALUE`

## Controlling recent results

- Iter068A run `34739048517`: denominator-skeleton Hörmander audit is mixed 8/8, necessary condition only.
- Iter068B run `34740962426`: separate-contact ordinary Hörmander product route obstructed for all frozen K4 source classes; jointly regulated family remains distinct.
- Iter069A/B: exact generic radial degree `+6`; naive ordinary improper real-cycle integral route closed for the reduced K4 rational family only.
- Iter070A: every fixed `epsilon>0` reduced member is tempered; no zero-regulator theorem follows.
- Iter071A run `34741938861`: common-epsilon Schwartz QMC remains REVIEW because small-epsilon variance prevents the frozen convergence/basis gates from closing.
- Iter072B run `34744334585`: strict-positive full-set cut-space kernel has nullity 3 exactly for transitive source sigma `++++`, `+++-`, `++--`, `+---`.
- Iter073A run `34746503186`, artifact `10314755546`, digest `sha256:b1c46b3ac61eb4416df337514f1610a34c40e74901e6b765c8ffbd84f345fe7a`: four transitive source classes each have proper histogram `(3,1)x2,(4,1)x1,(5,2)x3`; four nontransitive source classes have no positive-admissible proper face.
- Iter073B run `34748536488`, job `103700759855`, artifact `10315061564`, digest `sha256:b5d1638a7bada9ed6371d46bcee6526d9f61abd06668458370fe63e482cc96cd`: complete independent-wedge census gives `24/64` transitive/full-positive and `40/64` cyclic; maximal proper nullity distribution `-1:24, 1:16, 2:24`.
- Iter073C run `34748542204`, job `103700784152`, artifact `10315585117`, digest `sha256:27fd61945577078dd4dd16d85015b067073943ba87745dbdaa167450f81514c5`: exact Stiemke/Gordan certificates for all `1008/1008` nontransitive `(class,basis,subset)` cases.
- Iter073D run `34748577817`, job `103701076340`, artifact `10314703065`, digest `sha256:f7509f97716e7736471b850e2205ff0cebf19801b94c6653b88d1d1ef4767b6a`: all six admissible proper faces per transitive source class have exact extreme rays and strict relative-interior witnesses; five-edge/nullity-two sections are nondegenerate.
- Iter074A run `34748799901`, job `103701442665`, artifact `10315446037`, digest `sha256:c6888b4eca98055b6bb6fff5c0b5585ba02a812cd50f4864483520ccb9027c70`: exact 64-sign/S4 alternating cancellation removes nominal full-collision `epsilon^-3` and `epsilon^-2`; degree-two / nominal `epsilon^-1` overlap remains OPEN.
- Iter074B run `34748900260`, job `103701957025`, artifact `10315162039`, digest `sha256:34d40a7c34f7aafac37d0c3deb8f451e1479178519222a878ac43755e4747419`: strict dual certificates exist for all `1008/1008` nontransitive cases, global exact L1-normalized margin `1/7`.
- Iter075A run `34750595140`, job `103706458814`, artifact `10315304394`, digest `sha256:e76003536c5dec1a9b7a02c9d22765d6237233a56040020b0dde98ca62bb4c2d`: all `1008/1008` nontransitive positive-real faces satisfy exact L1 coercivity; actual global exact minimum is `1/3`.
- Iter075B run `34753179897`, job `103713045234`, artifact `10315658865`, digest `sha256:23143a335551347f5f88836f456616d911ccf87d3d83f158132fd1c08bd0ebe0`: `BLOCKED_SOURCE_LAW_NOT_ESTABLISHED`; available sources do not establish a full branchwise Toller inversion/order-reversal law.
- Iter075C prereg `0106e9b658aa37171e60262352810be48e6b674f`, head `f0d9b7fda85e4a05c9d2dbca100c59104abf835f`, run `34753274168`, job `103713294964`, artifact `10316637744`, digest `sha256:095e3057b03d2eb2d0ff5863b708c91bb0c708e1cac7d4cd059f3ee050107163`: `ITER075C_SIMPLE_TOLLER_INVERSION_CANDIDATE_SURVIVES_KERNEL_GATE_SCOPED`. The branch-flipped `(s,j,l)->(-s,l,j)` conjugated Feynman-kernel candidate is constant-ratio compatible in all frozen lanes to about `1e-91`, with unit magnitude and phase pi; the same-branch candidate fails the frozen tolerance. This is kernel-level only, not a full Toller-function inversion law. Durable result `status/ITERATION_075C_RESULT.md`.
- Iter075D prereg commit `c7166bdeeb0f5dc2adb65b1a3d28b4d664bf2f31`; implementation `e613ffa8b4a10f82b99733149e26d79fc1b649fd`; workflow/head `d8b24077897a89ca40efa5f1ee2e00e2eba58adc`: active six-lane held-out branch-flip recurrence certificate. Frozen thresholds and interpretation are in `status/ITERATION_075D_PREREG.md`.

## Next prospective gates

- Degree-two / nominal `epsilon^-1` overlap: compute the overlap-subtracted local coefficient on the transitive strata with numerator/Jacobian factors; do not infer cancellation from degree 0/1 symmetry.
- Transitive proper-stratum coefficients: determine actual coefficients on the six admissible proper faces per transitive source class, with explicit overlap bookkeeping and basis/S4 controls.
- Toller inversion: terminally consume Iter075D. Only if it passes may a full-group branch/order-reversal transformation gate be preregistered; do not promote a kernel identity to a group-function identity.
- Source-backed correlated boundary value: establish the full Toller/group object and Eq.(5)/(6) under non-transverse pullback before any K5 promotion.

## Exact blocker

The reduced K4 collision geometry is closed at the sign/cone level. The first two nominal full-collision powers cancel, and nontransitive positive-real faces have exact global L1 coercivity at least `1/3`. Iter075C has now identified a sharply constrained surviving branch-flip/minus-sign candidate at the published Feynman-kernel level, while Iter075B still blocks any direct promotion to a full Toller inversion law. Remaining decisive tasks are coefficient and boundary-value questions plus the full group-level transformation:

1. resolve the degree-two / nominal `epsilon^-1` overlap coefficient rather than extrapolating S4 cancellation;
2. determine actual coefficients on transitive proper strata, including overlap subtraction and numerator/Jacobian factors;
3. terminally classify Iter075D and, only if supported, test the full Toller branch/index/phase/order-reversal law on the group;
4. prove that the source-backed full Toller/group correlated boundary value exists and that Eq.(5)/(6) survives non-transverse pullback;
5. only then revisit K5.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no physical causal-sector selection from tournament/microlocal/asymptotic results;
- no G3 PASS or F9/G8/K5 promotion;
- no arbitrary counterterm, fitted cancellation, or preferred sequential order/tree;
- retain published spectral `i epsilon`; do not replace it by `beta+i epsilon`;
- do not transfer Wigner-D representation identities branchwise to Toller functions without derivation;
- distinguish reduced denominator theorem, fixed-epsilon temperedness, correlated distributional boundary value and full source-backed Toller vertex.
