# Iter083B-SM — exact filtered boundary-covariant supported-ambiguity dimension

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

## Prospective provenance

- preregistration: `prereg/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_EXACTNESS.md`, commit `c395c445c0b72ef897d1f7cb2e0bca023d64f4cd`;
- theorem derivation: `sources/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DERIVATION.md`, commit `8e4d9e5440a2ab3767a5a993350719b6a1351b80`;
- conditional adversarial review: `results/ITER083B_ADVERSARIAL_REVIEW.md`, commit `536c3b9bb50aac014779eb19144dd107c21df11c`;
- numerical dependency Iter083A authoritative result: `results/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_RESULT.md`, commit `4a56e325dad2c42f5ab7566c0e2f91d585cf4c9e`;
- Iter083A adversarial confirmation: `results/ITER083A_ADVERSARIAL_REVIEW.md`, commit `8c75e5ca96728d11091c8f22a69b4a4d6d766f86`;
- Iter083A production run `34910602967`, job `104197010950`, artifact `10374461752`.

The structural theorem and interpretation ceiling were frozen before the authoritative Iter083A production value was available. The current promotion only substitutes the now-authoritative graded multiplicities into the preregistered exact dimension formula.

## Classification

`ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DIMENSION_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Frozen supported-distribution space

After common-left `SL(2,C)` gauge fixing, upstream authority gives

`M = SL(2,C)^4`,

`N = SU(2)^4 subset M`,

`codim_R N = 12`,

and source transverse scaling degree

`sd_N = 20`.

Let `F_k` be the complex vector space of source-symmetry-compatible, boundary-linear distributions on the frozen common-collision neighborhood that

- are supported on `N`;
- have transverse normal order at most `k`;
- use the source Haar/tubular density convention;
- take values in the dual of the true 32-dimensional all-`j=1/2` boundary intertwiner space;
- obey the exact compact node gauge symmetry and S5 relabeling covariance.

Set `F_-1=0`.

No preferred normal coordinate, connection or coefficient splitting is part of the definition.

## Intrinsic filtration

Normal distributional order is coordinate independent. A local formula

`sum_(|alpha|<=k) u_alpha(y) partial_n^alpha delta_N`

is only a representative. Under a nonlinear tubular-coordinate change, displayed coefficients mix triangularly in normal order.

Therefore

`0=F_-1 subset F_0 subset ... subset F_8`

is intrinsic even though individual coefficient tuples are not.

## Exact principal-symbol sequence

For every `0<=k<=8`, the order-`k` principal normal symbol gives an equivariant map

`sigma_k : F_k -> G_k`,

where

`G_k = (H_boundary^* tensor Sym^k V)^(SO(3) x S5)`

and

`V = spin1_SO(3) tensor Std5_S5`.

The kernel is exactly `F_(k-1)`.

Surjectivity follows without choosing a canonical splitting: choose any tubular representative of an invariant principal symbol and average it over the compact source symmetry group and finite S5 relabeling group. Averaging preserves support on `N`, normal order and the invariant principal symbol.

Thus there is a short exact sequence

`0 -> F_(k-1) -> F_k -> G_k -> 0`.

## No hidden tangential distribution sector

The compact node action is transitive:

`N ~= SU(2)^5 / SU(2)_diag`.

For any invariant distributional section `T` of a finite-rank equivariant coefficient bundle and any test section `phi`, invariance gives

`T(phi) = T( integral_G g.phi dg )`.

The Haar average is a smooth invariant section and the averaging projection has finite-dimensional image. Such sections are determined by isotropy-invariant fiber data at one point.

Therefore arbitrary tangential functions or distributions do not restore an infinite-dimensional freedom after the exact node gauge symmetry is imposed.

## Density/Jacobian scope

The product Haar measure and induced tubular density are invariant under the frozen compact actions; S5 permutes identical Haar factors. Distributions pair with densities, so no extra orientation-sign character enters the principal-symbol pairing.

A nonlinear coordinate change may change lower-order displayed coefficients through Jacobian and transition jets, but it cannot change the intrinsic filtration, its graded quotients or the total dimension.

Thus the earlier coefficient-splitting concern is real only for a preferred explicit coefficient realization, not for the dimension theorem.

## Authoritative graded input

Iter083A production gives

`m_k = dim_C G_k`

for `k=0..8` as

`(2,0,5,1,22,10,72,48,217)`.

The exact sequence implies inductively

`dim_C F_8 = sum_(k=0)^8 m_k`.

Hence

`dim_C F_8 = 377`.

This is the exact dimension of the **full frozen all-`j=1/2`, boundary-linear, compact-gauge/S5-covariant, same-scaling-degree common-collision supported extension-difference space through normal order 8**.

## Scaling ceiling

The transverse delta distribution has scaling degree 12. An order-`k` normal derivative has scaling degree

`12+k`.

Thus exactly the orders `0<=k<=8` fit the frozen maximal scaling degree 20. No order `k>8` direction is included in this same-scaling-degree space.

## Relation to Iter081R

The old scalar result

`dim = 28`

is now understood as a proper scalar invariant subspace/lower bound within the frozen 377-dimensional boundary-covariant space. In particular, Iter083A opens genuine odd-order channels at `k=3,5,7` that are absent in the scalar sector.

## Selector remains absent

Exact classification of the ambiguity space is not the same as selecting a physical extension.

The source audit remains controlling: the published causal vertex and Toller companion provide no joint-K5 finite part, subtraction condition, common K5 regulator, collision boundary-value prescription or gluing/composition normalization selecting a point in the affine 377-dimensional extension family.

Compact averaging proves existence of equivariant lifts; it does not make one lift source-selected or canonical.

## Interpretation ceiling

The number 377 is exact only in the frozen all-`j=1/2`, common-K5-collision, boundary-linear, exact compact-gauge/S5-covariant same-scaling-degree sector. It is not a theorem about generic spins, every partial-collision stratum or a globally patched physical vertex.

No finite part/selector, regulator independence, causal-vertex divergence/nonexistence, generic-spin completeness, multivertex closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity follows.
