# Source-faithful joint K5 meromorphic bridge — derivation under frozen bridge preregistration

Date: 2026-09-15
Parent preregistration: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.

## Scope

This derivation addresses only the frozen all-`j=1/2`, local K3/K4/K5 collision sector. It attempts to define a source-faithful **joint meromorphic polar germ/residue object** for the actual ten-Toller/full-32-boundary source object. It deliberately stops before any holomorphic projection, Hadamard finite part, subtraction constant, or physical extension selector.

The authoritative source order is retained:

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full 32-component boundary contraction -> K5 group integration / distributional extension`.

## 1. Exact source-derived nonlinear collision radii

For every `h in SL(2,C)`, the source Toller construction uses the Cartan decomposition

`h = U1 exp(-i beta(h) K_z) U2`, `U1,U2 in SU(2)`, `beta(h)>=0`, `K_z=i sigma_z/2`.

Hence

`exp(-i beta K_z)=diag(exp(beta/2),exp(-beta/2))`

and therefore exactly

`(1/2) Tr(h h^dagger) = cosh beta(h)`.

Define

`s(h)=(1/2)Tr(h h^dagger)-1 >= 0`,

`q(h)=beta(h)^2 = arcosh(1+s(h))^2`.

Although `beta` itself is only radial-smooth at the compact locus, `q=beta^2` is real analytic there because

`arcosh(1+s)^2 = 2 s - (1/3)s^2 + O(s^3)`.

Thus `q` is a real-analytic nonnegative function in a neighborhood of `SU(2)`, with

`q(h)=0 <=> h in SU(2)`

and nondegenerate positive quadratic Hessian in the three noncompact normal directions. The normalization is fixed by the source generator convention for `K_z`; no regulator-parameter metric is introduced.

For a vertex block `B subset {0,1,2,3,4}`, `|B|=p>=2`, define the exact block radius

`q_B(g_0,...,g_4) = (1/p) sum_{a<b in B} q(g_b^{-1} g_a)`.

Then:

1. `q_B>=0`;
2. `q_B=0` iff all relative elements `g_b^{-1}g_a` in the block lie in `SU(2)`, i.e. on the compact collision stratum `N_B`;
3. `q_B` is invariant under common-left `SL(2,C)` gauge transformations;
4. it is invariant under independent compact left/right factors acting on the relative Cartan variables because Cartan rapidity is `SU(2) x SU(2)` bi-invariant;
5. block relabeling sends `q_B -> q_{pi(B)}` exactly;
6. wedge reversal leaves it fixed because `beta(h^{-1})=beta(h)`.

Near a compact collision ray of Iter077I,

`beta_ab(r)=r |x_a-x_b|+O(r^2)`.

Therefore

`q_B = r^2 (1/p) sum_{a<b in B}|x_a-x_b|^2 + O(r^3)`

`     = r^2 R_B^2 + O(r^3)`,

where `R_B^2=sum_{a in B}|x_a-xbar_B|^2` is exactly the source-normal radial quadratic form independently confirmed in repaired Iter083M. Thus `q_B` is an exact nonlinear source-derived continuation of the authoritative tangent radial normalization, not an auxiliary ten-edge regulator-space `Q`.

## 2. Full collision arrangement and blow-up

The ten source Toller factors are singular when individual relative Cartan rapidities vanish. For a mathematically clean joint object, resolve the complete compact polydiagonal arrangement, not only the divergent strata.

Use all nontrivial blocks of five labels:

- 10 K2 blocks;
- 10 K3 blocks;
- 5 K4 blocks;
- 1 K5 block;

for a total of 26 collision blocks.

K2 faces are locally integrable in the frozen `j=1/2` source problem and receive no subtraction coefficient, but including them in the resolution makes every pairwise Toller singularity a resolved boundary singularity.

The local quotient-normal geometry is the usual polydiagonal arrangement tensored with the physical three boost components. Iter082D already constructs the label-free block projectors and, on every maximal divergent chain `K3 subset K4 subset K5`, the orthogonal normal ranks

`6 + 3 + 3 = 12`.

A De Concini-Procesi/Fulton-MacPherson/Ulyanov-type iterated real blow-up of the complete clean collision arrangement gives a manifold with corners `M_tilde` on which nested collision loci become boundary hypersurfaces meeting with normal crossings. The construction is permutation-equivariant and does not choose a root/base label.

On this blow-up each pairwise rapidity lifts locally as

`beta_ab = (monomial in boundary defining functions) * b_ab`,

where `b_ab` is smooth and positive away from the corresponding resolved angular zero. Equivalently, each analytic `q_B` pulls back to a monomial of even order in the relevant boundary defining functions times a smooth positive factor.

## 3. Polyhomogeneous lift of the actual all-j=1/2 Toller object

The source companion paper gives the explicit `j=l=k=1/2` Toller branches as finite combinations of

- `exp(+/- i rho beta)`;
- `sinh(beta)^(-2)`;
- `cosh(beta)` and `sinh(beta)`;
- finite compact Wigner factors.

At a resolved face, `beta` is a smooth boundary radial variable and the boost direction is an angular variable on the front face. Hence

`exp(+/- i rho beta)`, `beta/sinh(beta)`, `cosh(beta)`

are smooth in the radial variable, while the only leading singular factor is an integer power of the boundary radius. Consequently every frozen `j=1/2` Toller matrix lifts to a polyhomogeneous conormal matrix-valued function on `M_tilde`.

A finite product of the ten lifted Toller matrices is polyhomogeneous conormal. Contraction with the already-authoritative complete 32-dimensional boundary intertwiner tensors is finite linear algebra and therefore preserves polyhomogeneity. Thus every one of the 32 frozen boundary components of the actual source-ordered ten-Toller object has a polyhomogeneous conormal lift.

This is stronger than using a representative boundary component and does not alter the published one-wedge Feynman prescription.

## 4. Source-faithful multivariate meromorphic family

Let `D` denote the 16 divergent blocks `|B|=3,4,5`. For complex parameters `lambda=(lambda_B)_(B in D)`, define off the collision set

`U(lambda) = [ product_(B in D) q_B^(lambda_B/2) ] A_source`,

where `A_source` is the actual source-ordered ten-Toller/full-32-boundary local integrand, paired with the unchanged product Haar density.

This family is not obtained by modifying a one-wedge Toller contour. The Toller matrices are first constructed exactly as in the source; only then is the full joint source object multiplied by the source-derived collision radii. Therefore the published spectral `i epsilon` remains untouched and no `beta+i epsilon` substitution occurs.

For sufficiently large real parts of the parameters the boundary exponents are shifted into the locally integrable range. On `M_tilde`, the family is a product of complex powers of boundary defining functions times a polyhomogeneous conormal coefficient and a smooth lifted Haar density.

The Mellin transform theorem for polyhomogeneous conormal distributions on manifolds with corners gives meromorphic continuation in the complex exponents, with polar hyperplanes determined by the boundary index sets. Equivalently, the general meromorphic-continuation theorems for complex powers of real-analytic functions (Atiyah/Bernstein-Sato/Hironaka; in multivariate distribution form, Dang) give distribution-valued meromorphic continuation with linear poles after resolution.

The meromorphic continuation is unique because it agrees with the convergent family on a nonempty open parameter domain.

Crucially, no Guo-Paycha-Zhang/Dang-Zhang holomorphic projection is used at this stage. Therefore no regulator-parameter quadratic form `Q`, no preferred sequential subtraction order, and no finite-part evaluator is required to define the **meromorphic polar germ itself**.

## 5. Haar density / Jacobian

No change of the physical integration measure is made: the original product Haar density is multiplied by the scalar analytic regulator above.

For the analytic proof on a blow-up, the pullback of a smooth density under the real blow-up of a codimension-`c` clean submanifold has local radial form

`rho^(c-1) d rho d Omega d y * smooth_positive_factor`.

Along a maximal divergent K3-K4-K5 corner, Iter082D gives incremental normal ranks `(6,3,3)`. Hence the resolved Haar density has the exact radial Jacobian powers

`rho_3^5 rho_4^2 rho_5^2 d rho_3 d rho_4 d rho_5`

up to a smooth nonvanishing angular/tangential factor. This is the density used in the Mellin exponent test. No Jacobian is omitted and no transformed measure is declared physical independently of the original Haar measure.

## 6. Branch/sign compatibility

The regulator is built only from `beta(g_b^{-1}g_a)^2`. It is independent of the Toller branch and satisfies

`q(g^{-1})=q(g)`.

Thus it does not alter:

- the one-wedge `T+ + T- = D` identity;
- the published branch extraction in the spectral rho-plane;
- the exact wedge/order-reversal relations of the Toller functions;
- causal sign assignments.

All branch/sign data remain those of the already-constructed source Toller matrices.

## 7. Covariance and basis independence

The family `U(lambda)` is equivariant under `S5` if the regulator parameters are relabeled simultaneously,

`lambda_B -> lambda_{pi(B)}`.

The construction uses every divergent block, every source wedge, and the full 32-dimensional boundary contraction. It contains no representative-component selection, preferred label, preferred maximal chain, or chosen edge-coordinate basis.

The meromorphic germ is therefore defined invariantly as a family over the parameter representation indexed by physical collision blocks. No metric on that parameter representation is used.

## 8. What this bridge defines

The bridge defines a canonical, source-faithful **multivariate meromorphic polar germ** of the frozen local all-`j=1/2` source object, once the exact source-derived functions `q_B` above are adopted.

Its negative Laurent coefficients are supported on the resolved collision strata and push forward to supported distributions on the original group manifold. These are actual full-boundary-contracted source-ordered polar/residue distributions, not the formal arbitrary `A_-1` of Iter083N and not an auxiliary scalar/Hodge surrogate.

This is enough to authorize a new prospective downstream gate that computes the normal-jet order and annihilator of the actual polar coefficients. That downstream gate must consume the **multivariate polar germ**. It must not silently replace it by a one-parameter family `rho^z u`; a one-parameter specialization would be an additional choice and requires its own prospective authority test.

## 9. B1-B9 mapping

B1 — satisfied in the frozen local sector: `U(lambda)` is explicit, simultaneous, uses all ten source wedges and the true K5 incidence.

B2 — satisfied: source Toller functions are constructed first; the exact joint map is multiplication of the full source object by source-derived `q_B^(lambda_B/2)`. No spectral prescription is replaced.

B3 — satisfied: the regulator is scalar and multiplies the already-authoritative full 32-component boundary contraction.

B4 — satisfied: original Haar/group measure and source order are retained; blow-up Jacobian powers are derived from the exact normal ranks.

B5 — satisfied: `q_B` is branch-blind, reversal-invariant, and leaves all source Toller sign identities untouched.

B6 — satisfied in the frozen local sector: the lifted object is polyhomogeneous conormal on the resolved clean polydiagonal arrangement; Mellin/complex-power continuation gives a unique distribution-valued meromorphic family.

B7 — satisfied **for the polar-germ bridge only**: defining the meromorphic continuation needs no finite-part projection. The radial functions are not an arbitrary regulator-space Q; they are exact functions of the source Cartan rapidities with source-normal tangent normalization. No subtraction constant or evaluator is selected.

B8 — satisfied: block-indexed parameter covariance is S5-equivariant and no basis/root/chain is preferred.

B9 — satisfied with a scope qualification: the bridge defines the actual multivariate polar coefficients needed for a residue normal-jet calculation. It does **not** authorize a one-parameter physical finite part or selector.

## 10. Interpretation ceiling

This derivation does not prove a unique physical finite part or K5 extension. It does not choose a holomorphic projection of the multivariate germ and therefore does not resolve the 377-dimensional extension-selection problem.

It does not prove regulator independence: replacing the exact source-derived block radii by other nonlinear defining functions can change finite parts when residues are nonzero, as formalized by Iter083N.

It does not establish generic-spin applicability, global all-strata partition-of-unity patching, causal multivertex E3/E4/E6 closure, RG/refinement, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

The scientific advance is narrower but important: the previous Iter083P transition blocker can be removed for the **existence/definition of a frozen local full-source multivariate meromorphic polar object**, while physical finite-part selection remains a separate downstream problem.

## Public mathematical/source authority

- Bianchi, Chen, Gamonal, arXiv:2604.24945: exact Cartan rapidity, Toller functions, non-representation property, and one-wedge spectral projector.
- Bianchi, Chen, Gamonal, arXiv:2601.23162: causal vertex source ordering as a product of ten already-defined Toller matrices followed by group integration and full boundary contraction.
- Ulyanov, `Polydiagonal compactification of configuration spaces`, arXiv:math/9904049: permutation-equivariant iterated blow-up resolving polydiagonals to a normal-crossing boundary arrangement.
- Melrose b-calculus / Mellin theorem for polyhomogeneous conormal functions on manifolds with corners: Mellin transform is meromorphic with poles fixed by boundary index sets.
- N. V. Dang, arXiv:1503.00995, especially Theorem 1.3 and the multivariate wavefront/renormalization framework: products of complex powers of real-analytic functions admit distribution-valued meromorphic continuation with linear poles after resolution.
