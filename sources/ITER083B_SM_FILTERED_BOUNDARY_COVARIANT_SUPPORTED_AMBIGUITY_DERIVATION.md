# Iter083B-SM source/theorem derivation — intrinsic filtered boundary-covariant supported ambiguity

Date: 2026-09-15

Status: **theorem proved conditionally; numerical promotion requires authoritative Iter083A production PASS**

Prospective contract: `prereg/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_EXACTNESS.md` at commit `c395c445c0b72ef897d1f7cb2e0bca023d64f4cd`.

## 1. Frozen upstream geometry

Iter077L establishes, after the source common-left gauge fixing,

`M = SL(2,C)^4`, `N = SU(2)^4 subset M`, `codim_R N = 12`,

with source transverse scaling degree `sd_N=20`. Brunetti--Fredenhagen extension theory therefore allows same-scaling-degree local extensions, and the difference of two such extensions is supported on `N` with normal derivative order at most

`20-12 = 8`.

Iter077M fixes the source measure as product Haar and records that the induced quotient/tubular density on the common-collision locus is invariant. Iter077Q's source-lock correction fixes the exact node-wise compact gauge symmetry. Iter081R packages the compact orbit as

`SU(2)^5 / SU(2)_diag ~= N`

and the normal fiber at the identity orbit as

`V = spin1_SO(3) tensor Std5_S5`.

The fully boundary-linear all-`j=1/2` fiber is

`H_boundary = tensor_{a=1}^5 Inv_SU2[(V_{1/2})^tensor4]`, `dim_C H_boundary=32`.

No source-selected normal connection, normal-coordinate splitting, K5 finite part, collision boundary value, subtraction condition, or joint K5 regulator is added here.

## 2. Intrinsic normal-order filtration

Let `D'_N(M;H_boundary^*)_<=k` denote boundary-linear distributions on the common-collision neighborhood, supported on `N`, of transverse order at most `k`.

This is intrinsic. One local tubular chart may write a representative as

`T = sum_{|alpha|<=k} T_alpha(y) partial_n^alpha delta_N`,

but a nonlinear change of tubular coordinates mixes the displayed coefficients triangularly. The individual `T_alpha` are therefore not canonical data.

What is canonical is the filtration

`0 = F_-1 subset F_0 subset ... subset F_8`,

where `F_k` is the source-symmetry-compatible subspace of `D'_N(M;H_boundary^*)_<=k`.

A diffeomorphism preserving `N` preserves distributional normal order, so the exact compact node action and `S5` relabeling preserve this filtration.

## 3. Principal normal symbol and its kernel

For a distribution supported on a smooth submanifold, quotienting order `k` by order `k-1` removes precisely the lower-order triangular coordinate mixing. The resulting principal normal symbol is an intrinsic distributional section over `N` with fiber

`H_boundary^* tensor Sym^k(NN)`,

where `NN = TM|_N/TN` is the normal bundle. Equivalently, test-function normal `k`-jets live in `Sym^k N^*N` and the supported distributional symbol is their dual, hence `Sym^k NN`.

Thus there is an equivariant exact sequence before taking source symmetries,

`0 -> D'_N,_<=k-1 -> D'_N,_<=k -> D'(N; H_boundary^* tensor Sym^k NN tensor density_factor) -> 0`.

The source Haar/tubular convention removes any additional orientation character: the ambient product Haar density and induced density on `N` are invariant under the compact node action and vertex relabeling. Distributions are paired with densities, not with a chosen oriented top form. Therefore there is no unmotivated determinant-sign twist in the frozen source object.

The kernel of the principal-symbol map is exactly order `<=k-1` by definition of normal order.

## 4. Homogeneous-space reduction eliminates hidden tangential distributions

Let

`G0 = SU(2)^5`, `H0 = SU(2)_diag`.

The frozen compact node action is transitive on

`N ~= G0/H0`.

Include vertex relabeling by the finite group `S5`; the identity collision is fixed by relabeling, and its isotropy action on the normal fiber is precisely the Iter081R representation

`V = spin1_SO(3) tensor Std5_S5`.

Consider any finite-rank equivariant coefficient bundle `E -> N`. A `G0`-invariant distributional section cannot carry an arbitrary distribution along `N`. Indeed, for any smooth compactly supported test section `phi` on this compact homogeneous space and invariant distribution `T`,

`T(phi) = T( integral_G0 g.phi dg )`.

The Haar average of `phi` is a smooth `G0`-invariant test section. Hence `T` factors through the finite-dimensional averaging projector onto invariant smooth sections. Such sections are determined by their value at the identity coset, subject exactly to `H0` isotropy invariance.

Therefore invariant distributional coefficient data along `N` are finite fiber data; no hidden infinite-dimensional tangential distribution sector survives the exact node gauge symmetry.

After also imposing `S5`, the degree-`k` invariant principal-symbol space is

`G_k = (H_boundary^* tensor Sym^k V)^(SO(3) x S5)`.

Here the diagonal `SU(2)` acts on the boost-vector factor through its spin-1/SO(3) representation. The normal representation is real orthogonal and self-dual, so using the dual jet convention gives the same character multiplicity. This self-duality is not used to absorb a density twist; density invariance was fixed separately above.

## 5. Surjectivity on invariant symbols without a canonical splitting

The subtle point is whether an invariant principal symbol necessarily lifts to an invariant supported distribution when no preferred normal connection has been selected.

Take `s in G_k`.

1. Choose any tubular neighborhood and any order-`k` supported distribution `T0` whose principal normal symbol is `s`. Standard local supported-distribution theory supplies such a representative.
2. Average over the compact source symmetry group (continuous compact node group and finite `S5`):

   `Tbar = integral_G g.T0 dg`.

3. Every `g` preserves `N`, so `supp(Tbar) subset N`.
4. Every `g` preserves normal order, so `Tbar` still has order at most `k`.
5. Principal symbol commutes with the action and with averaging. Since `s` is invariant,

   `sigma_k(Tbar) = integral_G g.s dg = s`.

6. `Tbar` is invariant by construction.

Therefore the invariant principal-symbol map is surjective.

Crucially, the choice of initial tubular representative was arbitrary. Different choices differ by lower-order terms. Averaging proves existence of an equivariant lift, not a source-selected or canonical coefficient splitting.

## 6. Exact filtered sequence

For every `0<=k<=8` we therefore have an intrinsic short exact sequence of complex vector spaces

`0 -> F_{k-1} -> F_k -> G_k -> 0`,

where

`G_k=(H_boundary^* tensor Sym^k V)^(SO(3) x S5)`.

Consequently

`dim_C F_k = dim_C F_{k-1} + dim_C G_k`,

and inductively

`dim_C F_8 = sum_{k=0}^8 m_k`,

with

`m_k = dim_C G_k`.

This dimension formula is independent of the choice of tubular coordinates or connection. A noncanonical equivariant splitting may always be constructed by compact averaging, but the source does not pick one.

## 7. Scaling-degree ceiling

The transverse delta on a codimension-12 submanifold has scaling degree 12. Each normal derivative raises transverse scaling degree by one, so an order-`k` term has

`sd_N = 12+k`.

Thus precisely orders `0<=k<=8` are compatible with the frozen maximal scaling degree 20. The present theorem neither admits nor classifies order `k>8` same-scaling-degree differences.

## 8. Conditional numerical consequence from Iter083A

If, and only if, Iter083A receives authoritative production `PASS_EXACT_SCOPED` for

`m_0..m_8 = (2,0,5,1,22,10,72,48,217)`,

then

`dim_C F_8 = 2+0+5+1+22+10+72+48+217 = 377`.

Unlike Iter081R's scalar 28-dimensional subspace, this would be the **exact dimension of the full frozen all-j=1/2 boundary-linear compact-gauge/S5-covariant supported extension-difference space through normal order 8**, subject to the scope locks stated here.

It would not be the dimension of every possible generic-spin or every-singular-stratum physical extension problem.

## 9. Selector remains absent

This theorem separates two questions that had previously been conflated:

1. **Classification/dimension of the admissible supported ambiguity space:** intrinsic and, conditionally on Iter083A, exactly computable.
2. **Choice of the physical extension within that affine space:** not supplied by invariant-jet classification.

Iter077M's source audit remains controlling: the published causal vertex and Toller companion do not state a joint-K5 finite part, subtraction condition, common regulator, collision boundary-value prescription, or gluing/composition identity selecting these coefficients.

Therefore exact dimension does not imply uniqueness.

## 10. Frozen adversarial conclusions

- Compact averaging gives an equivariant lift, **not** a canonical/source-selected splitting.
- No arbitrary tangential function/distribution survives transitive node-gauge invariance.
- No density sign twist is imported.
- One-wedge Feynman/Toller ordering is not promoted into a joint K5 selector.
- The theorem is local to the frozen common-collision ambiguity and does not prove global patching across every partial-collision stratum.
- No generic-spin, regulator-independence, multivertex, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.

## Theorem status

The structural theorem T1--T7 is proved within the frozen source geometry.

Current numerical verdict until Iter083A production terminates:

`PROVED_CONDITIONAL_PENDING_ITER083A_PRODUCTION`.
