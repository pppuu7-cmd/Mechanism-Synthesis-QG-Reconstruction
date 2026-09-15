# Iter083H-SM preregistration — primitive deepest K5 simple pole is Q-independent under S5

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083G proved that S5 symmetry alone leaves a three-sector family of positive regulator-space quadratic forms Q. Does that freedom already change the renormalized value of the isolated primitive deepest K5 overall pole, or is a single S5-invariant simple pole insensitive to Q so that any genuine scheme dependence must enter through nested/subdivergence pole geometry?

## Frozen scope
This gate studies only the **primitive deepest radial pole model** obtained after isolating the common K5 collision and separating lower/nested collision contributions. It is not the full K3/K4/K5 forest meromorphic germ.

Let the ten edge regulator variables be

`x_e = s_e - 1`, e in E(K5).

The common radial scaling of the frozen all-j=1/2 leading K5 product is regularized edgewise by replacing each wedge radial factor `r^-2` by `r^(-2 s_e)`.

At physical point s_e=1, the normal codimension is 12 and the divergence degree is 8. The Taylor-normal order n=8 radial coefficient therefore has the local model

`integral_0^1 r^(11+8) product_e r^(-2(1+x_e)) dr`

whose meromorphic continuation has one simple pole through the physical point with denominator proportional to

`L(x) = sum_e x_e`.

The holomorphic numerator is allowed to be valued in the true 32-dimensional boundary dual representation and must be S5-equivariant.

## Mathematical projection framework
Use only the algebraic polar-germ decomposition of Dang–Zhang / Guo–Paycha–Zhang: for a nondegenerate regulator-space quadratic form Q, a simple polar germ has denominator L and numerator variables Q*-orthogonal to L. The projection pi_Q removes the polar part and keeps the holomorphic part.

No external Euclidean Feynman theorem is promoted to Lorentzian K5 source authority.

## Prospective predicates
P0 SOURCE_ORDER_FIREWALL: analytic regularization acts on the post-Toller ten-wedge common-collision product, not on historical pre-product contact distributions.

P1 SIMPLE_OVERALL_POLE: exact radial power counting must give a unique physical-point pole from Taylor order n=8 and denominator `L=sum_e x_e`; orders n!=8 are holomorphic at x=0 in this primitive radial model.

P2 TRIVIAL_POLE_SECTOR: under the exact ten-edge S5 action, L spans the unique trivial [5] regulator covector inside

`E = [5] + [4,1] + [3,2]`.

P3 Q_ORTHOGONAL_COMPLEMENT_INDEPENDENT: for every nondegenerate S5-invariant Q=`aI+bA+cB`, the trivial line and the two nontrivial irreducible sectors are mutually Q/Q*-orthogonal. Therefore the Q*-orthogonal complement of L is the same `[4,1]+[3,2]` subspace for every such Q. This must be checked exactly, not numerically for one Q.

P4 TRUE_BOUNDARY_COVARIANCE: consume authoritative Iter083A boundary representation

`H_boundary^* = 2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]`.

The space of S5-equivariant linear regulator numerators `Hom_S5(E,H_boundary^*)` must have dimension `2+1+2=5`. Exactly two of those maps originate from the trivial regulator input [5]; the other three originate from nontrivial regulator sectors.

P5 SIMPLE_POLE_FINITE_PART_THEOREM: for any S5-equivariant holomorphic H_boundary^*-valued numerator

`h(x)=h_0+h_1(x)+h_2(x)+...`,

prove that

`ev_0 pi_Q(h/L)`

receives no contribution from h_0/L, receives a constant only from the trivial-L component of h_1/L, and receives no constant from h_m/L for m>=2 by homogeneous degree. Because the trivial/nontrivial split is Q-independent under P3, the evaluated finite part is independent of the choice of S5-invariant Q.

P6 NONTRIVIAL_LINEAR_CHANNEL_CONTROL: the three equivariant linear maps from regulator [4,1] and [3,2] sectors must remain in the polar numerator sector and contribute zero to the evaluated constant for the simple denominator L. They must not be silently discarded from the boundary representation.

P7 NESTED_POLE_FIREWALL: the theorem must explicitly retain the possibility of Q-dependence when two or more independent pole forms from K3/K4/K5 forests occur simultaneously. No full meromorphic-germ Q-independence claim is allowed.

## Expected classification
If P0-P7 and all controls pass:

`ITER083H_SM_PRIMITIVE_DEEPEST_K5_SINGLE_SIMPLE_S5_POLE_FINITE_PART_Q_INDEPENDENT_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Negative/adversarial controls
- reject replacing the true boundary representation by a scalar numerator;
- reject assuming all five equivariant linear maps are trivial-regulator maps;
- reject a non-S5-invariant Q that mixes the trivial regulator line with nontrivial sectors;
- reject extending the theorem to multiple independent pole forms;
- reject extending it to higher pole order without proof;
- reject using this primitive-pole theorem as a global K3/K4/K5 forest renormalization theorem;
- retain the possibility that nested poles generate actual Q dependence inside F8;
- retain the possibility that a stronger locality/functoriality law fixes Q before projection.

## Research consequence if PASS
Iter083G Q-freedom would be shown to be harmless for the isolated simple overall K5 pole. The next scientifically nonredundant calculation would then move directly to the nested forest polar structure (K3/K4/K5 simultaneous linear poles), where more than one pole direction can make the Q-dependent polar complement physically relevant.

## Interpretation ceiling
No full K5 meromorphic continuation theorem; no all-strata renormalization map; no claim that the actual full K5 amplitude is Q-independent; no generic-spin theorem; no regulator independence; no unique physical selector; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.