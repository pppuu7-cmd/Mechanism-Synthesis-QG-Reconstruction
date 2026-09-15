# Iter083O-SM preregistration — exact Cartan-rapidity squared gives a nonlinear Morse–Bott collision-radius candidate

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083M fixes the invariant tangent normal quadratic geometry, while Iter083N tests the fact that finite parts can depend on higher defining-function jets. Does the published Cartan rapidity beta itself supply an exact smooth nonlinear defining function whose entire jet is fixed by a source-native formula?

This gate tests a **candidate nonlinear defining function**, not a physical finite-part prescription and not uniqueness among all possible nonlinear source-compatible functions.

## Primary source input
The Toller companion paper uses the exact Cartan decomposition

`g = U1 exp(-i beta K_z) U2`,

`U1,U2 in SU(2)`, `beta>=0`, `K_z=(i/2)sigma_z`.

Therefore

`g g^dagger = U1 exp(beta sigma_z) U1^dagger`

and hence exactly

`c(g):=(1/2)Tr(g g^dagger)=cosh beta`.

For a collision block B of size p define

`mu_B(g_1,...,g_p) = (1/p) sum_(a<b in B) beta(g_b^-1 g_a)^2`.

The coefficient 1/p is chosen to match the authoritative Iter083M product-normal/barycentric quadratic normalization at tangent order.

## Prospective predicates
P0 SOURCE_CARTAN_LOCK: source lock must record the exact Cartan formula, generator normalization and beta>=0 rapidity interpretation.

P1 TRACE_IDENTITY: derive exactly `c(g)=cosh beta`, and verify beta=0 iff g is in SU(2).

P2 SMOOTH_BETA_SQUARED: prove `beta^2=F(c-1)` is real-analytic near c=1. One admissible proof is to set `y=beta^2` and use

`c-1 = h(y) = cosh(sqrt(y))-1 = y/2 + y^2/24 + ...`,

whose derivative at y=0 is 1/2 !=0, so the analytic inverse-function theorem gives analytic `y=F(c-1)`. Production must independently verify the first seven rational coefficients

`F(t)=2t - t^2/3 + 4t^3/45 - t^4/35 + 16t^5/1575 - 8t^6/2079 + 32t^7/21021 + O(t^8)`.

P3 BLOCK_ZERO_SET: prove `mu_B>=0` and `mu_B=0` iff every internal relative element `g_b^-1 g_a` is in SU(2). Equivalently, the block variables lie in one common left coset of SU(2). This is exactly the compact relative-collision locus before/after the usual common-left gauge fixing.

P4 MORSE_BOTT_HESSIAN: in source-normal boost coordinates `g_a=u_a exp(X_a.sigma/2)` transported to any compact-collision point, verify

`mu_B = (1/p) sum_(a<b)|X_a-X_b|^2 + O(|X|^3)`

and hence its normal Hessian is nondegenerate and equals the Iter083M barycentric normal quadratic form `R_B^2=sum_a |X_a-Xbar_B|^2` up to the standard Hessian factor convention. Thus mu_B is Morse–Bott locally with critical/zero manifold equal to the compact block collision.

P5 EXACT COVARIANCE: verify exact common-left invariance, independent right-SU(2) invariance on the block variables and S_p/S5 label covariance of mu_B. No preferred root label is allowed.

P6 FOREST TANGENT_COMPATIBILITY: for every K3->K4->K5 maximal chain, the Hessians of the exact mu_B reproduce the Iter083M orthogonal increment ranks `(6,3,3)` and variance coefficients `3/4,4/5`. Do not require an exact nonlinear variance identity away from the collision.

P7 HIGHER_JET_AND_AUTHORITY_FIREWALL: the explicit formula for mu_B fixes all of its higher jets mathematically, thereby realizing one concrete nonlinear extension of the Iter083M tangent radius. However the audited causal/Toller source does not state that analytic renormalization must use this particular sum-of-squared-rapidities defining function. PASS must therefore classify mu_B as a source-native geometric candidate, not as a source-authorized physical selector.

## Negative controls
- reject beta itself as a smooth radial defining function at beta=0; only beta^2 is claimed smooth;
- reject an exact nonlinear Euclidean variance identity for group rapidities;
- reject replacing beta by an arbitrary reparameterization with the same Hessian and calling it source-selected;
- reject a rooted/pair-subset formula that breaks label covariance;
- reject promotion of mu_B to a finite-part selector;
- retain multiplicative/functional defining-function choice as a physical-authority issue;
- retain actual-residue/finite-part and global forest-patching blockers.

## Expected classification if PASS
`ITER083O_SM_EXACT_CARTAN_RAPIDITY_SQUARED_GIVES_SMOOTH_SOURCE_NATIVE_MORSE_BOTT_FOREST_RADIUS_CANDIDATE_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
The higher-jet problem identified by Iter083N will have a concrete exact candidate solution: mu_B fixes all nonlinear jets by an explicit group-theoretic formula rather than arbitrary tubular continuation. The next gate must then test the radial analytic finite part built from mu_B itself, including rescaling/reparameterization dependence and actual residue activation, before any physical-selector claim.

## Interpretation ceiling
No proof that the causal/Toller source physically mandates mu_B for renormalization; no unique finite part; no global nonlinear forest variance theorem; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.