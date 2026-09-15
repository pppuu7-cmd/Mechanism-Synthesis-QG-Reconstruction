# K5 order-8 principal symbol — exact Schwinger/projective reduction

Date: 2026-09-15
Parent preregistration: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`, commit `7466325187f22043d1794379fd6e6dcf62e05abd`.

Status: POST-PREREGISTRATION DERIVATION / COMPUTATIONAL REDUCTION ONLY. No K5 zero/nonzero verdict is assigned here.

## 1. Scope

The authoritative K5 reduction has already isolated the actual order-eight principal-symbol problem at the primitive physical-origin K5 face. Proper K3 and K4 simple residues are exact zero, and the leading spin-half edge factor is

`M(v_ab)/(v_ab^2)^(3/2)`

with `M(v)` linear in the three Cartesian components of `v`.

For either exact S5-invariant boundary **dual** channel, let `N_c(x)` denote the resulting complete ten-edge leading numerator. It is homogeneous of degree 10 in the 12 barycentric K5 normal coordinates. Let `P_8(x)` be any homogeneous order-eight normal probe. Then

`H_c,P(x)=N_c(x) P_8(x)`

has homogeneous degree 18.

The reduction below applies channel-by-channel to the exact full-boundary numerator. It does not replace the 32-component source object by a representative component and does not assign a physical one-parameter regulator.

## 2. Gauge-fixed K5 incidence and weighted Laplacian

Gauge fix vertex 0 and write the four remaining three-vectors as `x_1,...,x_4`. For every unordered K5 edge `e={a,b}` define the oriented incidence row `b_e` on the four non-root vertices. The ten relative vectors are

`v_e = b_e x`.

For positive Schwinger parameters `alpha_e`, define the exact 4x4 reduced weighted graph Laplacian

`L(alpha)=B^T diag(alpha_e) B`.

The scalar quadratic form from the ten denominators is

`sum_e alpha_e |v_e|^2 = sum_{i,j=1}^4 L_ij(alpha) x_i . x_j`.

For all `alpha_e>0`, `L(alpha)` is positive definite. The full 12x12 Gaussian matrix is `L(alpha) tensor I_3`, hence

`det(L tensor I_3)^(-1/2)=det(L)^(-3/2)`.

By the matrix-tree theorem,

`Psi_K5(alpha)=det L(alpha)`

is the Kirchhoff polynomial of K5. It is homogeneous of degree 4 and is the sum of one square-free monomial for every spanning tree. Cayley's theorem gives exactly

`5^(5-2)=125`

such monomials.

## 3. Exact Schwinger representation

For each edge,

`(v_e^2)^(-3/2) = Gamma(3/2)^(-1) integral_0^infinity alpha_e^(1/2) exp[-alpha_e v_e^2] d alpha_e`.

Therefore the homogeneous K5 order-eight pairing can be represented, initially in a convergent analytic domain and then by the already-authorized meromorphic continuation, as

`Gamma(3/2)^(-10) integral_(R_+^10) [prod_e alpha_e^(1/2) d alpha_e] integral_(R^12) H_c,P(x) exp[-x^T(L(alpha) tensor I_3)x] dx`.

This is a computational representation of the already-frozen K5 principal-symbol coefficient. It does not alter the published one-wedge spectral `i epsilon` and does not introduce `beta+i epsilon`.

## 4. Degree-18 Gaussian moment is exactly a ninth Wick contraction

Define

`D_L = sum_(i,j=1)^4 (L^(-1))_ij (partial_(x_i) . partial_(x_j))`.

For the Gaussian convention used above,

`integral_(R^12) H(x) exp[-x^T(L tensor I_3)x] dx`

`= pi^6 det(L)^(-3/2) [exp((1/4) D_L) H](0)`.

Since `H_c,P` has degree exactly 18, every term in the exponential vanishes at the origin except the ninth contraction. Thus

`G_c,P(alpha) = pi^6 det(L(alpha))^(-3/2) / (4^9 9!) * [D_L^9 H_c,P](0)`.

This is exact. No angular ray, numerical quadrature, fitted coefficient or incomplete order-eight partition family is used.

Because each `L^(-1)` is `adj(L)/det(L)`, the Wick contraction is an exact rational function of the ten Schwinger parameters. The only square-root algebraic factor is the explicit positive-domain `det(L)^(-3/2)`.

## 5. Exact common-scale pole extraction

Set

`alpha_e = t u_e`,

with `t>0`, `u_e>0`, and `sum_e u_e=1`.

The ten-parameter measure transforms as

`d^10 alpha = t^9 dt d sigma(u)`.

The remaining homogeneous factors scale exactly as

- `prod_e alpha_e^(1/2) -> t^5 prod_e u_e^(1/2)`;
- `det L(tu)^(-3/2) -> t^(-6) det L(u)^(-3/2)` because `deg Psi=4`;
- `D_(L(tu))^9 -> t^(-9) D_(L(u))^9`.

Hence the complete common-scale exponent is

`5 + 9 - 6 - 9 = -1`.

The K5 logarithmic pole is therefore the exact radial/projective factor

`integral_0 dt / t`.

This independently reproduces `omega_5=8` and isolates the order-eight residue coefficient as a projective Schwinger period on the open 9-simplex.

## 6. Exact projective period

Up to the fixed nonzero normalization

`C = pi^6 / (Gamma(3/2)^10 4^9 9!)`,

the channel/probe coefficient is the meromorphic/projective continuation of

`P_c[P_8] = integral_(Delta_9) [prod_e u_e^(1/2)] Psi_K5(u)^(-3/2) [D_(L(u))^9 (N_c P_8)](0) d sigma(u)`.

This is the highest-information reduced object for the current K5 gate.

For the first nonzero-witness lane one may take the source K5 quadratic radial probe

`P_8 = (R_K5^2)^4`,

but the reduction is valid for every degree-eight probe and therefore for the complete order-eight tensor if evaluated on a basis.

## 7. Relation to the 16-parameter meromorphic family

This projective common-scale extraction is not a replacement of

`U(lambda)=[prod_(B in D) q_B^(lambda_B/2)] A_source`

by a one-parameter physical regulator.

It is a homogeneous computational coordinate for the already-authorized **simple K5 face principal symbol** after the exact K3/K4 proper-face residues have been proved zero. Boundary faces of the Schwinger simplex encode subgraph/subcollision regions and remain subject to the existing multivariate-meromorphic provenance. No finite part or sequential subtraction is selected here.

## 8. S5 covariance

Vertex relabeling permutes the ten edges, hence permutes the Schwinger coordinates `u_e`. The Kirchhoff polynomial, simplex measure and common-scale decomposition are invariant under this action. The channel dependence resides only in the exact dual boundary numerator `N_c`, whose S5 covariance is already reconstructed in the controlling reduction.

Therefore the reduction introduces no preferred edge, vertex, spanning tree or maximal collision chain.

## 9. New computational consequence

The unresolved 12-dimensional angular/Mellin moment has been reduced exactly to a 9-dimensional projective graph period with:

- 10 positive Schwinger coordinates;
- one overall scale carrying the complete logarithmic pole;
- the 125-term K5 Kirchhoff polynomial of degree four;
- a finite ninth-order Wick contraction of the exact degree-18 numerator/probe polynomial.

This opens exact sector-decomposition, integration-by-parts, graphical-function and high-precision/PSLQ exploratory lanes without changing the frozen scientific criterion.

A numerical value alone is not sufficient for the K5 scientific verdict. Exact zero/nonzero still requires a structural proof or an exact representation satisfying the preregistration.

## Interpretation ceiling

No K5 zero/nonzero classification is made. No physical finite part, unique extension, regulator independence, one-parameter physical residue, global patching, F9/G3 promotion, new physics or complete-QG claim follows.
