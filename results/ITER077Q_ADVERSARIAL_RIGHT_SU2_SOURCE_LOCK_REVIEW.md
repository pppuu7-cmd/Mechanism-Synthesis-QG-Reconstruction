# Iter077Q adversarial re-review — omitted node-wise right SU(2) boundary gauge symmetry invalidates the claimed source-compatible Q^n tangential family

Date: 2026-09-14
Status: **DURABLE CRITIC RE-REVIEW OF HISTORICAL AUTHORITY**

## RESULT_REVIEWED
Historical target: `results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md`, authoritative production run `34792482045`, artifact `10328598487`, historical classification `ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED`. The mathematical family reviewed is `w_n=Q^n F_SU2 delta_N`, where `N=SU(2)^4` after source global gauge fixing and `Q(g)=sum_(a<b) tr_(1/2)(g_b^-1 g_a)`. This re-review was triggered by auditing an exact source symmetry omitted from the Iter077Q lock set.

## SOURCE_OBJECT_CHECK
The Bianchi--Chen--Gamonal causal vertex is a boundary linear functional whose magnetic indices are contracted with five SU(2)-invariant boundary intertwiners. Historical Iter077M source derivation explicitly freezes this fact and defines `F_SU2(y;Psi)` as the ordinary compact spin-network functional built from the same ten spins, five SU(2)-invariant intertwiners, and relative compact matrices. BCG Toller Eq. (13) / causal-vertex Eq. (7) gives exact bi-SU(2) covariance: for compact `u_L,u_R`, `T(u_L g u_R)=D(u_L) T(g) D(u_R)` in the projected spin blocks. Therefore, after full boundary-intertwiner contraction, the scalar integrand is invariant under independent node-wise right compact transformations `g_a -> g_a u_a`, with `u_a in SU(2)` (and the root-node transformation fixed to the identity after global SL(2,C) gauge fixing). This source symmetry was not included in Iter077Q Lane D.

## SOURCE_ORDERING_CHECK
The new objection does not alter source ordering. It acts on the already source-ordered Toller-function K5 integrand and its compact restriction after full boundary contraction. No contact-distribution multiplication, spectral limit exchange, or surrogate vertex is introduced. The issue is purely that a required exact symmetry of the same source object was omitted when declaring the supported family source-compatible.

## PROVENANCE_CHECK
Iter077Q preregistration, source derivation, implementation and terminal run remain chronologically valid as an execution history. The defect is not post-run code corruption. It is a missing source lock: the frozen admissibility list checked common-left SL(2,C), S5 relabeling, boundary linearity, support, source ordering and scaling degree, but omitted independent right SU(2) node gauge invariance of the fully contracted boundary spin-network functional. Historical green CI therefore cannot certify the stronger phrase `source-compatible` against the omitted symmetry.

## ERRATUM_CHECK
`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling and unrelated to this defect. The right-SU(2) argument uses BCG's exact compact covariance of Toller matrices and SU(2)-invariant intertwiners, not the historical erroneous contact formula. No Iter077E/F authority is revived.

## BOUNDARY_COMPLETENESS_CHECK
This objection specifically requires the true boundary object and therefore strengthens, rather than weakens, the boundary-completeness standard. The source boundary states are gauge-invariant spin networks/intertwiners. For every such fixed boundary state `Psi`, the compact functional `F_SU2(y;Psi)` is invariant under independent node gauge rotations. The argument is not based on one representative magnetic component. It applies to the boundary-linear functional after the invariant intertwiner contraction that Iter077M itself froze.

## DISTRIBUTIONAL_CHECK
After fixing the common left SL(2,C) redundancy by `g_1=I`, the collision submanifold is `N=SU(2)^4`. The residual node-wise right action of `H=SU(2)^4` is `g_a -> g_a u_a` for `a=2,...,5`. On `N` this action is simply transitive: choosing `u_a=g_a^-1` sends any `(g_2,...,g_5)` to `(I,...,I)`. Therefore every scalar smooth tangential coefficient compatible with this exact gauge invariance is constant along `N` (for each fixed gauge-invariant boundary functional), or more generally an equivariant coefficient completely determined by finite fiber data for normal-jet sectors.

The distribution `delta_N` is invariant because the action preserves `N` and Haar/tubular density. `F_SU2 delta_N` from Iter077M is therefore still a valid supported ambiguity. But the Iter077Q multiplier `Q` is not invariant under this node-wise right action. On Iter077Q's own frozen path, `Q(t)=12+8 cos(t)`. The gauge transformation `u_2=g_2^-1`, `u_3=u_4=u_5=I` sends that point to the identity configuration, where `Q=20`; for generic `t`, `12+8 cos(t) !=20`. Thus `Q^n F_SU2 delta_N`, `n>0`, violates the omitted source gauge symmetry.

## REGULATOR_CHECK
No regulator issue is used to invalidate Iter077Q. One-wedge Feynman i-epsilon remains separate from the joint-K5 extension. The surviving constant/normal-jet extension freedom still requires a selector or boundary-value prescription. No regulator independence follows from the symmetry correction.

## COUNTEREXAMPLE_ATTEMPTS
Could `F_SU2` transform so as to compensate `Q`? No for the physical boundary space frozen by Iter077M: the five boundary tensors are SU(2)-invariant intertwiners, so the complete compact spin-network contraction is invariant under the node-wise compact gauge action. Could the right action change causal labels? No: compact frame rotations leave the frozen wedge branch signs unchanged and preserve the Cartan rapidities. Could Toller nonrepresentation invalidate the compact covariance? No: BCG Eq. (13) explicitly reconstructs Toller matrices with ordinary SU(2) Wigner matrices on the left and right, so bi-SU(2) covariance is exact even though general Lorentz-group composition fails. Could `Q` be invariant only on the quotient? No: the explicit gauge-equivalent path values above differ.

## SURROGATE_CHECK
No scalar K4, Hodge, BCH, numerical or toy surrogate is used. The correction is derived from the actual Toller Cartan formula, the actual K5 relative arguments, and the actual five SU(2)-invariant boundary intertwiners already used by Iter077M/Q. The transitivity statement is exact on the same `N=SU(2)^4` collision manifold.

## OVERCLAIM_CHECK
Invalidating the Iter077Q infinite-dimensional **tangential** family does not make the local amplitude unique. Iter077M's constant `c F_SU2 delta_N` ambiguity survives. Iter077L's normal jets through order 8 also remain possible; node-wise compact covariance converts arbitrary smooth tangential coefficient functions into equivariant finite fiber data rather than automatically eliminating all jets. The corrected source-compatible ambiguity space therefore remains nontrivial but is not established to be infinite-dimensional at fixed spin/boundary sector by Iter077Q. No G3, F9/G8/K5, regulator, causal-stack or complete-QG promotion follows.

## VERDICT
`INVALID_SOURCE_LOCK`

## QUALIFICATIONS
The pure mathematical statement that `{Q^n F delta_N}` is linearly independent is correct. What fails is the scientifically essential qualifier `source-compatible`: the frozen lock set omitted an exact node-wise SU(2) gauge symmetry implied by BCG's bi-SU(2) Toller covariance plus invariant boundary intertwiners. The historical Iter077Q run/artifact remain valid evidence for the narrower algebraic theorem only and must not remain controlling physical extension authority. Downstream claims whose essential premise is an infinite-dimensional source-compatible `W=span{Q^n F delta_N}` require dependency review. Results that need only a nonzero scalar ambiguity or Iter077I non-L1 behavior may survive.

## UPDATED_CRQN_CHAIN
`carrier/source F1-F8` -> `source-ordered K5` -> `Iter077I minimal-sector non-L1` -> `Iter077L sd20/codim12 extension freedom` -> `Iter077M nonzero constant source-compatible delta_N ambiguity survives` -> `Iter077Q historical infinite-dimensional tangential promotion INVALID_SOURCE_LOCK` -> `right-SU(2)^4 covariance collapses scalar tangential coefficient functions on N to constants; normal-jet equivariant fiber freedom still to classify` -> `repair exact source-compatible invariant normal-jet ambiguity dimension ?` -> `local amplitude remains BLOCKED_NONUNIQUE` -> `causal orientation sums do not cancel Iter077I leading term` -> `composition / regulator / RG remain downstream`.

## AUTHORIZED_NEXT_GATE
Immediately perform a dependency reconciliation before using any `full-W` result. Prospectively freeze `RIGHT_SU2_COVARIANT_K5_EXTENSION_JET_CLASSIFICATION_GATE`: start from Iter077L's normal jets through order 8 and impose the exact node-wise right SU(2)^4 covariance of the fully boundary-contracted source object, together with common-left gauge fixing, S5 relabeling and true boundary linearity. Determine the actual finite-dimensional/equivariant supported ambiguity space and exhibit at least one nonzero surviving ambiguity (Iter077M already supplies the order-zero scalar witness). Do not assume the space is one-dimensional: normal derivatives transform nontrivially. In parallel, mark Iter080D/E/H/I/J and Iter081I wherever their conclusion specifically depends on infinite-dimensional `W`; retain only conclusions independently supported by the surviving scalar ambiguity or source audits. Until repaired, replace `FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR` by `RIGHT_SU2_COVARIANT_K5_EXTENSION_SELECTOR / INVARIANT_JET_CLASSIFICATION` as the controlling local blocker.