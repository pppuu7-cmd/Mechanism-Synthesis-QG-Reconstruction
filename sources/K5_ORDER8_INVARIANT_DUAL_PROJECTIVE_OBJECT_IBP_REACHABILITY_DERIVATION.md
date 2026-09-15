# K5 order-8 invariant-dual projective object and first IBP reachability derivation

Date: 2026-09-16

Prospective gate: `prereg/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_PERIOD_IBP_NONCANCELLATION.md`, commit `4a92113d33addb7c00bcb294f35fa78c35e18691`.

Status: POST-PREREG OBJECT / REACHABILITY DERIVATION. No invariant-dual integrated period is declared zero or nonzero here.

## 1. Exact local boundary basis and dual action

The authoritative stripped local four-spin tensors from `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py` have exact Euclidean coefficient norms

- `||T_0||^2=4`;
- `||T_1||^2=12`;
- `T_0.T_1=0`.

Thus the stripped `k=0/k=1` basis is orthogonal but not orthonormal. Under each of the 24 incident-leg permutations, the permuted tensor is re-expanded exactly in this two-dimensional basis. There are six distinct rational 2x2 local action matrices.

For a vertex permutation `sigma in S5`, the tensor at old vertex `v` moves to `sigma(v)` and its four incident legs are permuted according to the induced permutation of the sorted neighbor list. Tensoring the five exact local actions gives the complete rational 32x32 boundary action.

Direct reconstruction gives class character

`(32,0,8,2,0,0,2)`

on the standard S5 class order and the Reynolds projector has exact rank two. Its transpose is the correct projector for boundary covectors.

A deterministic RREF basis for the invariant dual row space has pivot components `00001` and `00100`. One convenient exact basis is:

`ell_1:`

`00001 - 00010 +4*00111 -01000 +01001 +01010 -01011 +01101 -01110 +10000 +10001 +10010 +10011 -10101 +10110 +11001 -11010 +4*11100 +12*11111`;

`ell_2:`

`00100 -00111 -01001 -01010 -2*01011 +2*01101 -2*01110 -10001 -10010 +2*10011 -2*10101 +2*10110 +2*11001 -2*11010 -11100 -3*11111`.

These are basis choices inside the invariant dual space, not physical normalizations.

## 2. Full-32 uniform point check

Recompute the order-eight uniform Schwinger radial moment from the complete all-32 source object:

- all 32 boundary components;
- all `100000` source node-choice terms;
- all 945 Wick pairings before uniform-covariance sparsity;
- exact rational arithmetic.

Project the resulting boundary **covector** with `P^T`, not `P`.

In the RREF dual basis above, the exact projected coordinates at the uniform Schwinger point are

`(-9225216/9765625, -7175168/9765625)`.

Both are nonzero. This is only a pointwise object-definition/reachability check; it is not the integrated projective period.

Using the vector projector `P` instead gives a different result, as required by the non-orthonormal stripped basis. This provides an exact adversarial discriminator against vector/covector confusion.

## 3. Exact projective Schwinger structure

For one leading edge,

`|v|^(-3) = Gamma(3/2)^(-1) integral_0^infty d alpha alpha^(1/2) exp(-alpha |v|^2)`.

Ten source edges therefore contribute `product_e alpha_e^(1/2)`.

After common-left gauge fixing there are 12 real Gaussian normal variables. The reduced weighted K5 Laplacian has determinant

`Psi_K5(alpha)=det L(alpha)`,

homogeneous degree four. Exact determinant expansion equals the K5 Kirchhoff polynomial: 125 spanning-tree monomials, all coefficient one.

The leading boundary numerator has degree ten and the order-eight radial probe adds degree eight, so the 12D Gaussian numerator has total degree 18. Wick contraction pairs these 18 linear factors into nine covariances. Each covariance is an entry of `L^-1=adj(L)/Psi`, with `adj(L)` homogeneous degree three.

Hence every scalar dual channel can be represented exactly as

`Omega_9 * [product_e alpha_e^(1/2)] * N_c(alpha) / Psi_K5(alpha)^(21/2)`

up to a common nonzero source normalization, with

`deg N_c = 9*3 = 27`.

The function multiplying the complete projective volume has homogeneity

`5 + 27 - 4*(21/2) = -10`.

The complete projective nine-form carries the compensating degree +10. Thus the form is exactly projective.

This derivation is equivalent to the previously validated common-scale exponent `-1` before separating the radial `dt/t` factor.

## 4. Schwinger-simplex boundary behavior for regular polynomial IBP fields

For any single edge `e`, setting `alpha_e=0` deletes that edge from the Kirchhoff polynomial. `K5-e` remains connected. Exact tree counting gives 75 spanning trees not using any fixed edge, so

`Psi_K5|_(alpha_e=0)`

is a nonzero positive polynomial in the interior of that codimension-one Schwinger face.

`N_c(alpha)` is polynomial and therefore finite there, while the explicit measure weight contributes `alpha_e^(1/2)`. Consequently the projective integrand tends to zero like `alpha_e^(1/2)` on every open codimension-one simplex face.

Therefore projective IBP vector fields with polynomial coefficients regular at the simplex boundary have zero codimension-one boundary contribution for this target integrand.

This statement does **not** authorize arbitrary index-lowering identities with `1/alpha_e`, nor does it identify Schwinger faces with K3/K4 collision faces. Singular IBP fields or shifted integrals require a fresh boundary analysis.

## 5. First exact IBP reachability check

The Euler/radial vector field gives only the projective homogeneity identity. If `f(alpha)` is the scalar function multiplying the affine ten-parameter volume, then

`sum_e alpha_e d_e f = -10 f`.

Thus

`sum_e d_e(alpha_e f) = 10 f - 10 f = 0`.

This is an exact but tautological projective identity and does not evaluate either invariant-dual period.

No higher-degree exact projective IBP/syzygy system sufficient to decide the two target periods is established in this first reachability step. Therefore the scientifically correct scoped classification at this stage, provided the exact object and all controls validate in production, is

`K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED`.

This is not a zero result and not evidence that an exact reduction is impossible.

## 6. External mathematical bridge

Artico and Magnea, arXiv:2310.03939 / JHEP 03 (2024) 096, formulate Feynman-parametric integrands as projective forms and derive parameter-space integration-by-parts relations using the fact that exterior differentiation preserves projectivity. This supplies a mathematically relevant IBP framework for the present Schwinger object.

It does not evaluate this K5 tensor period automatically. In particular, the K5 numerator is tensor-derived, the exponent `21/2` is half-integral, and every boundary term generated by any chosen shifted/IBP family remains subject to the frozen source-specific boundary audit.

## Interpretation ceiling

The two invariant-dual projective objects are exact and nontrivial pointwise, and regular polynomial projective IBP fields have controlled codimension-one boundary behavior. The actual two integrated periods remain undecided.

No parent K5 order-eight zero/nonzero theorem, no complete 217-dimensional tensor rank/annihilator, no finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.