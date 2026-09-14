# Iter081O Critic exact corollary — generic-spin full projected Toller block has an invertible leading pole and the two branches differ by an overall minus sign

Date: 2026-09-14
Status: **EXACT ONE-WEDGE FULL-MATRIX COROLLARY; NO GENERIC-SPIN K5 BOUNDARY-CONTRACTION VERDICT**

## Inputs

1. Bianchi--Chen--Gamonal `arXiv:2604.24945v1`, Eq. (13), constructs the full Toller matrix from Cartan/KAK data:

`T^(±,rho,k)_(jp,ln)(g) = sum_m D^j_(pm)(U1) t^(±,rho,k)_(jlm)(beta) D^l_(mn)(U2)`

for

`g=U1 exp(-i beta K_z) U2`, `U1,U2 in SU(2)`, `beta>=0`.

2. Iter081N, prospectively frozen at `ccf9813204edde8e69a8c15b6770af14d3e36f26` and proved in `results/ITER081N_CRITIC_GENERIC_SPIN_TOLLER_BRANCH_LEADING_SIGN_RESULT.md`, establishes in the gamma-simple minimal block `j=l=k`, for every `m=-j,...,j` and fixed real `rho!=0`,

`t^+_(jjm)(beta) = C_(jm)(rho) beta^(-(2j+1)) + o(beta^(-(2j+1)))`,

`t^-_(jjm)(beta) = -C_(jm)(rho) beta^(-(2j+1)) + o(beta^(-(2j+1)))`,

with every `C_(jm)(rho) != 0`.

## Full projected block
Set `l=j=k` in BCG Eq. (13). Define the diagonal coefficient matrix

`C_j(rho) := diag(C_(j,-j),...,C_(j,j))`.

Then the finite magnetic sum gives

`P_j T^+(g) P_j`
`= beta^(-(2j+1)) D^j(U1) C_j(rho) D^j(U2) + o(beta^(-(2j+1)))`,

and

`P_j T^-(g) P_j`
`= - beta^(-(2j+1)) D^j(U1) C_j(rho) D^j(U2) + o(beta^(-(2j+1))).`

The little-o statement holds entrywise; because the magnetic sum is finite and the SU(2) Wigner matrices are bounded/unitary, it is preserved under the finite Cartan reconstruction.

Thus the two full projected Toller branches have the same leading matrix and differ only by the scalar sign `-1`.

## Invertibility of the leading matrix
For real `rho!=0`, Iter081N proves every diagonal entry of `C_j(rho)` is nonzero. Therefore `C_j(rho)` is invertible.

The matrices `D^j(U1)` and `D^j(U2)` are unitary and hence invertible. Consequently

`L_j(U1,U2;rho) := D^j(U1) C_j(rho) D^j(U2)`

is invertible for every `U1,U2 in SU(2)`.

In particular the leading projected Toller block cannot vanish as a matrix for any Cartan angular data.

Its singular values are exactly those of `C_j(rho)` because left/right multiplication by unitary matrices preserves singular values. Hence

`||P_j T^±(g) P_j||_op ~ beta^(-(2j+1)) max_m |C_(jm)(rho)|`,

and the smallest singular value likewise behaves as

`s_min(P_j T^± P_j) ~ beta^(-(2j+1)) min_m |C_(jm)(rho)|`.

Therefore every finite-spin gamma-simple minimal projected Toller block is unbounded and, at leading order, nonsingular in magnetic space as `beta->0+`.

## EPRL specialization
For a nonzero real Immirzi parameter with the usual gamma-simple relation `rho=gamma j` and `j>0`, one has `rho!=0`. Therefore the theorem applies edge by edge to every finite nonzero spin in that convention.

No claim is made here for `j=0` or `rho=0`; those were excluded by the prospective Iter081N domain.

## Exact branch-sign transport
For any fixed finite `j>0` in the frozen minimal block,

`Leading[P_j T^- P_j] = - Leading[P_j T^+ P_j]`.

This result is independent of the Cartan SU(2) angles. It is the full-matrix generalization of the `j=1/2` branch-sign transport used in Iter077I.

Classification:

`ITER081O_SM_GENERIC_FINITE_SPIN_GAMMA_SIMPLE_MINIMAL_FULL_PROJECTED_TOLLER_BLOCK_HAS_INVERTIBLE_BETA_MINUS_2J_PLUS1_LEADING_MATRIX_AND_BRANCH_MINUS_EQUALS_NEGATIVE_BRANCH_PLUS_EXACT_COROLLARY_SCOPED`.

## Conditional K5 consequence
Consider a K5 common-collision path for which every wedge `(ab)` has a nonzero finite spin `j_ab`, stays in the gamma-simple minimal projected block, and has rapidity `beta_ab -> 0` with well-defined source KAK data. At the level of the **uncontracted leading tensor product**, changing the Toller branch on an edge multiplies that edge's leading block by exactly `-1`.

Therefore a branch assignment `epsilon_ab=±1` changes the complete ten-edge leading tensor by the scalar

`prod_(a<b) epsilon_ab`.

For every proper causal K5 assignment `epsilon_ab=eta sigma_a sigma_b`,

`prod_(a<b) epsilon_ab = eta^10 prod_a sigma_a^4 = +1`.

Hence all proper causal assignments have the **same uncontracted leading tensor** as the all-plus assignment, for arbitrary finite nonzero edge spins within this minimal-block hypothesis.

This is a sign-transport statement only. It does not prove that contraction of that tensor with a given generic-spin boundary-intertwiner state is nonzero.

## Claim ceiling
This corollary does NOT establish:
- generic-spin full K5 non-L1 behavior;
- nonzero generic-spin boundary contractions;
- generic-spin scaling degree after full boundary contraction;
- behavior at `j=0` edges or nonminimal `j,l` blocks;
- distributional nonexistence/divergence;
- unique K5 extension;
- regulator independence, multivertex closure, G3/F9/G8/K5, new physics or complete QG.

It establishes a source-backed generic finite-spin **full wedge-block** leading-sign theorem and a conditional K5 branch-sign transport at the uncontracted tensor level.
