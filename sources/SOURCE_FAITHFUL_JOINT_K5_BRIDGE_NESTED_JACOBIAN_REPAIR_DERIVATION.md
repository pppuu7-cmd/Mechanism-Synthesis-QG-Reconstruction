# Source-faithful joint K5 bridge — nested blow-up Jacobian / Mellin repair derivation

Date: 2026-09-15
Parent scientific gate: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.
Repair preregistration: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md`, commit `148dd5130c448420419a807826fdfd84bb1228ef`.

This file supersedes only the nested-density/Mellin portions of `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md`. All source-order, boundary, branch, Cartan-radius, block-radius, covariance and interpretation-ceiling statements remain unchanged unless explicitly corrected here.

## 1. Exact quotient geometry

Let `G=SL(2,C)`, `K=SU(2)`, `X=G/K`.

For source group variables,

`g_b^-1 g_a in K  <=>  g_a K = g_b K`.

Hence every compact block-collision stratum `N_B` is the inverse image under the smooth quotient submersion

`G^5 -> X^5`

of the ordinary polydiagonal where the points indexed by `B` coincide in the three-dimensional symmetric space `X`.

Therefore the full 26-block compact collision arrangement is locally a pullback of the usual clean polydiagonal arrangement. The wonderful/iterated real blow-up construction applies locally and permutation-equivariantly.

The exact source Cartan rapidity is the symmetric-space radial variable. The pair function

`q(g_b^-1 g_a)=beta(g_b^-1 g_a)^2`

is the local squared symmetric-space distance for the source normalization. Thus the block function

`q_B=(1/|B|) sum_(a<b in B) beta_ab^2`

is a nonnegative analytic defining function for the block diagonal near the compact locus and has the authoritative Iter083M quadratic normal form.

## 2. Orthogonal incremental normal decomposition

For every maximal chain

`B3 subset B4 subset B5={0,1,2,3,4}`

with `|Bp|=p`, authoritative Iter082D gives orthogonal projector increments of physical real ranks

`dim E3=6`, `dim E4=3`, `dim E5=3`.

Write corresponding normal vectors as

`u3 in E3`, `u4 in E4`, `u5 in E5`.

The nested strata are

- K3: `u3=0`;
- K4: `u3=u4=0`;
- K5: `u3=u4=u5=0`.

The previous derivation incorrectly treated absolute polar radii of `E3,E4,E5` as the boundary defining functions of the nested blow-up. They are not.

## 3. Hierarchical blow-up coordinates and correct Haar Jacobian

At the maximal nested corner, after resolving deepest-to-shallower nested diagonals, choose boundary scales so that to leading order

`u5 = rho5 * omega5`,

`u4 = rho5 rho4 * omega4`,

`u3 = rho5 rho4 rho3 * omega3`,

where the angular variables range over smooth compact front-face charts and smooth nonzero factors are suppressed.

The overall K5 scale `rho5` scales all 12 normal dimensions, the relative K4 scale `rho4` scales the 9 dimensions `E3+E4`, and the relative K3 scale `rho3` scales the 6 dimensions `E3`.

Therefore the pullback of the smooth product Haar/tubular density has leading radial Jacobian

`rho5^(12-1) rho4^(9-1) rho3^(6-1)`

or

`rho3^5 rho4^8 rho5^11 d rho3 d rho4 d rho5`

up to a smooth nonvanishing angular/tangential density.

Thus the correct cumulative normal dimensions and density powers are

`cumulative normal dimensions = (6,9,12)`,

`nested density powers = (5,8,11)`

ordered `(K3,K4,K5)`.

The historical `(5,2,2)` tuple is quarantined as an incremental-orthogonal-polar diagnostic and must not be used in the resolved Mellin theorem.

## 4. Exact source singular powers on a maximal nested corner

In the frozen `j=1/2` sector each source Toller wedge has leading order `beta_ab^-2`.

On a maximal chain:

### Internal K3 edges

There are `C(3,2)=3` edges inside B3. Their relative rapidities scale as

`beta_ab ~ rho5 rho4 rho3 * smooth_nonzero`.

Therefore these three factors contribute

`rho3^-6 rho4^-6 rho5^-6`.

### Additional K4 edges

There are

`C(4,2)-C(3,2)=6-3=3`

edges inside B4 but not inside B3. Their rapidities scale as

`rho5 rho4`.

They add

`rho4^-6 rho5^-6`.

Hence all K4-internal factors cumulatively contribute

`rho3^-6 rho4^-12 rho5^-12`.

### Additional K5 edges

There are

`C(5,2)-C(4,2)=10-6=4`

edges inside K5 but outside B4. Their rapidities scale as `rho5` and add `rho5^-8`.

Thus the complete ten-wedge leading source product scales as

`rho3^-6 rho4^-12 rho5^-20`

at the maximal nested corner, up to a smooth angular boundary matrix whose authoritative nonzero witness is inherited from repaired Iter077I.

Multiplying by the corrected Haar density gives

`rho3^-1 rho4^-4 rho5^-9`.

Therefore the resolved superficial divergence degrees are exactly

`omega_K3=0`, `omega_K4=3`, `omega_K5=8`,

in agreement with the independently established scaling-degree chain and Iter083N formal annihilator thresholds.

## 5. Incidence linear forms for the multivariate regulator

The regulator parameters remain attached to the 16 divergent blocks:

- 10 K3 blocks;
- 5 K4 blocks;
- 1 K5 block.

For a resolved face corresponding to a cluster `C`, a block radius `q_B` vanishes with the scale of `C` exactly when `B subseteq C`. Thus in hierarchical blow-up coordinates

`q_B^(lambda_B/2)`

contributes the face factor `rho_C^(lambda_B)` iff `B subseteq C`.

Define the incidence linear form

`L_C(lambda) = sum_(B subseteq C, |B|>=3) lambda_B`.

At a maximal chain:

`L_B3 = lambda_B3`,

`L_B4 = lambda_B4 + sum_(B3 subset B4) lambda_B3`,

`L_K5 = lambda_K5 + sum_(all K4) lambda_K4 + sum_(all K3) lambda_K3`.

The complete map from the 16 block parameters `lambda_B` to the 16 face forms `L_C` is triangular when blocks are ordered by increasing cardinality: every `L_C` contains `lambda_C` with coefficient one and only parameters of proper subblocks otherwise. Therefore its determinant is exactly one and it is invertible over the integers.

This supplies a canonical normal-crossing coordinate system in regulator space without choosing a metric or sequential finite part.

## 6. Corrected local form of the regularized family

At a maximal nested corner, after absorbing smooth nonzero angular factors, the full source family has the form

`U(lambda) ~ rho3^(L_B3-1) rho4^(L_B4-4) rho5^(L_K5-9) A(rho,angles,lambda)`,

where `A` is polyhomogeneous conormal in the boundary variables and holomorphic in `lambda` in the initial convergence region.

A sufficient local convergence chamber is

`Re L_B3 > 0`,

`Re L_B4 > 3`,

`Re L_K5 > 8`

for every maximal nested chain. Because the `lambda -> L` map is invertible and taking every `Re lambda_B` sufficiently large and positive makes every `Re L_C` large positive, the intersection of all such conditions is nonempty.

Thus the corrected density does not obstruct the bridge; it supplies the exact convergence chamber required by B6.

## 7. Mellin pole hyperplanes through the physical point

Expand the smooth/polyhomogeneous coefficient in nonnegative integer radial powers.

For a factor

`rho^(L_C - omega_C - 1) sum_(n>=0) a_n rho^n`,

the radial Mellin integral has poles where

`L_C = omega_C - n`.

At the physical parameter origin `lambda=0`, hence `L_C=0`, the pole-producing radial Taylor orders are exactly

- K3: `n=omega=0`;
- K4: `n=omega=3`;
- K5: `n=omega=8`.

Therefore the hyperplanes through the physical point are

`L_C(lambda)=0`

for the divergent blocks, while the actual source polar coefficient at such a face probes normal Taylor order `omega_C`.

This derives, rather than assumes, the normal-order thresholds `0,3,8` from the actual source family and corrected blow-up geometry.

It does not yet compute the full boundary-contracted coefficient tensors at those orders; that remains the downstream polar-normal-jet task.

## 8. Meromorphic continuation after repair

The geometric resolution and the polyhomogeneous lift of the actual Toller/full-boundary object are unchanged. The correction modifies only the exact boundary-density exponents and therefore the numerical convergence/pole bookkeeping.

With the corrected local model and nonempty convergence chamber, the standard Mellin theorem for polyhomogeneous conormal distributions on manifolds with corners applies componentwise. The multivariate continuation is meromorphic in the invertible linear face coordinates `L_C`, equivalently in the original block parameters `lambda_B`.

No holomorphic projection, finite part, subtraction constant, regulator-space metric or sequential specialization is required to define this meromorphic continuation.

## 9. Defining-function scheme covariance remains mandatory

For an allowed smooth positive rescaling

`q'_B = exp(phi_B) q_B`,

one has

`U'(lambda)=exp[(1/2)sum_B lambda_B phi_B] U(lambda)`.

This holomorphic gauge factor does not change existence of the meromorphic continuation or its polar divisor, but it can mix lower Laurent coefficients when higher-order poles occur. Therefore the bridge remains scheme-scoped and does not imply regulator independence or a physical finite-part selector.

## 10. Repaired B4/B6 claim

B4 can be re-established only with the cumulative nested density powers `(5,8,11)` and the explicit hierarchical derivation above.

B6 can be re-established only with the corrected local exponents

`(-1,-4,-9)`

plus regulator shifts `(L_K3,L_K4,L_K5)`, the explicit nonempty convergence chamber, and the standard polyhomogeneous Mellin continuation theorem.

All other B predicates retain their previous content.

## Interpretation ceiling

Even if fresh production re-establishes B1-B9, it defines only the frozen local multivariate meromorphic family/polar germ in the chosen source-derived `q_B` scheme. No unique physical finite part, regulator independence, one-parameter residue, causal-vertex finiteness/divergence, generic-spin completeness, global patching, E3/E4/E6, G3/F9, RG/continuum/GR/matter/prediction or complete-QG claim follows.