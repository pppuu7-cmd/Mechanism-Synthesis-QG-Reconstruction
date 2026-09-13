# Gamma-simple Toller matrix one-jet and intertwiner-closure supplement

Date: 2026-09-13

## Source inputs

Primary source: E. Bianchi, C. Chen, M. Gamonal, **Causal spinfoam vertex for 4d Lorentzian quantum gravity**, arXiv:2601.23162 (2026).

The source boundary state is

`|Psi_{j_ab,i_a}> = sum_{m_ab} (i_a)_{m_ab} |Psi_{j_ab,m_ab}>`,

with five SU(2) intertwiners `i_a`. Its fixed-causal vertex Eq. (4) contains

`T_{j_ab m_ba, j_ab m_ab}(g_b^{-1} g_a)`

for every ordered pair `a<b`. Eq. (7) gives compact covariance through the Cartan decomposition

`T(g)=D^j(U1) t(beta) D^j(U2)`.

The exact gamma-simple reduced branch asymptotics used below are the closed Iter076U result, derived from source Eq. (9).

## Derived leading and subleading diagonal coefficients

For `j>0`, `n=2j+1`, write the pure positive-z boost branch as

`t_m^(s)(beta) = beta^(-n) [ C_m^(s) + beta D_m^(s) + o(beta) ]`,

where `s=+/-` is the causal Toller branch.

From the Eq. (9) source prefactor and the leading hypergeometric continuation coefficient,

`C_m^(+) = 2^(-n) P_+ Gamma(c_+) Gamma(n)/[Gamma(a_+)Gamma(b_+)]`,

`C_m^(-) = 2^(-n) P_- Gamma(c_-) Gamma(n)/[Gamma(a_-)Gamma(b_-)]`.

Using the reflection identity `Gamma(z)Gamma(1-z)=pi/sin(pi z)` and the admissible magnetic step `m -> m-1`, one obtains exactly

`C_m^(-) = - C_m^(+)`,

and for either branch

`C_m/C_(m-1) = -(j-m+1)/(j+m)`.

For real `gamma != 0` and admissible `m`, the Gamma factors entering `C_m` are finite/nonzero in this source scope; hence the diagonal leading matrix `C=diag(C_m)` is invertible.

Iter076U gives the normalized first coefficient

`D_m^(s)/C_m^(s) = i gamma m`

for **both** causal branches. Therefore, with `J_z=diag(m)`, the matrix relation is

`D^(s) = C^(s) (i gamma J_z) = (i gamma J_z) C^(s)`

and consequently

`(C^(s))^(-1) D^(s) = D^(s) (C^(s))^(-1) = i gamma J_z`.

The magnetic dependence of the leading singular coefficient cancels completely in this relative matrix one-jet.

## Compact covariance and arbitrary boost axis

For a pure boost of magnitude `beta` along unit direction `n`, choose `U in SU(2)` with

`U J_z U^(-1)=J_n`.

Eq. (7) gives the leading and first-subleading matrices by conjugation:

`C_n = D^j(U) C_z D^j(U)^(-1)`,

`D_n = D^j(U) D_z D^j(U)^(-1)`.

Hence the relative matrix one-jet is exactly

`C_n^(-1) D_n = i gamma J_n`.

For the opposite boost direction `-n`, it is `-i gamma J_n`.

This statement concerns the normal pure-boost approach to the singular SU(2) locus. It does not define compact/rotation tangential derivatives at `beta=0`.

## Node-common boost and SU(2) intertwiner closure

Use node `5` in the source ordering. Every one of its four incident source wedges has the form `(a,5)` with `a<5`, so the relative group element is

`g_5^(-1) g_a`.

At the coincident control `g_a=1`, perturb only

`g_5(beta)=exp(beta K_n)`.

Then all four incident relative elements are the same opposite-direction boost

`g_5(beta)^(-1) g_a = exp(-beta K_n)`.

After factoring the leading singular matrix on each incident wedge, the derivative of the four-wedge product inserts

`-i gamma sum_{a=1}^4 J_n^(5a)`

on the four magnetic slots of the node-5 boundary intertwiner.

By definition of an SU(2) intertwiner,

`[sum_{a=1}^4 J_i^(5a)] i_5 = 0`, for `i=x,y,z`,

and therefore for every unit vector `n`,

`[sum_a J_n^(5a)] i_5 = 0`.

Thus the **node-common pure-boost relative matrix one-jet is annihilated exactly by boundary-intertwiner closure** at this source control.

The result is independent of the four wedge spins because the relative coefficient is `i gamma` multiplying the standard generator, and it is independent of the causal Toller branch signs because Iter076U gave the same relative one-jet for both branches.

## Scope firewall

This supplement does not establish:

- a compact/rotation tangential one-jet along the singular SU(2) locus;
- an arbitrary independent boost on each wedge (only a common node group perturbation is tested);
- a unique global singular-factorization prescription for the full ten-wedge product;
- the nonlinear source-to-K4 curvature;
- the nominal `epsilon^-1` coefficient.

The source group variables are node variables, so a common node perturbation is the correct linearized carrier for source relative-group cut-space directions. However, promotion from this scoped boost-normal cancellation to a complete source numerator one-jet requires a separate audit of compact/tangential directions and of compatibility of the matrix leading-factor extraction across the full source product.