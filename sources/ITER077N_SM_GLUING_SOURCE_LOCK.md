# Iter077N-SM source lock — supported ambiguity survival and standard gluing

**Date:** 2026-09-14

## Causal-vertex source

Primary source: E. Bianchi, C. Chen, M. Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.

Frozen source facts:

- Eq. (4) defines the fixed-causal single-vertex amplitude as a linear functional on a spin-network boundary state, with ten Toller matrices and four gauge-fixed `SL(2,C)` integrations.
- The one-wedge causal labels are `kappa_ab=sigma_a sigma_b`.
- The Discussion explicitly says that finiteness of the causal vertex must be investigated again because Toller poles may introduce new divergences.
- The Discussion explicitly says the paper focused on a single vertex; construction/questions for many vertices are identified as an important next step.
- No projector/idempotency, cylindrical-consistency, refinement, transfer-matrix, or c-independent multi-vertex composition equation for the new causal vertex is stated in this source.

## Standard EPRL state-sum / gluing authority

Source: P. Donà, P. Frisoni, *How-to Compute EPRL Spin Foam Amplitudes*, arXiv:2202.04360 / Universe 8 (2022) 208.

Frozen source facts:

The general EPRL state sum on a 2-complex has the form

`Z_Delta = sum_{j_f,i_e} prod_f A_f(j_f) prod_e A_e(i_e) prod_v A_v(j_f,i_e)`.

The paper states that the correct convolution property at fixed boundary fixes the standard face and edge amplitudes, and it explains multi-vertex decomposition by inserting resolutions of the identity in intertwiner spaces. Multi-vertex amplitudes are then sums/contractions of products of vertex tensors.

Thus the standard composition rule is bilinear/multilinear in the supplied vertex amplitudes. It is a rule for constructing the amplitude of a chosen 2-complex from local vertex tensors; by itself it is not an equation equating a modified vertex tensor to a separately fixed c-independent target.

## Compact restriction used in Lane A

On the common-collision set after root gauge fixing,

`N=SU(2)^4`.

For edge holonomies of pure-gauge form `u_b^-1 u_a`, contraction with invariant node intertwiners makes the closed compact K5 spin-network evaluation gauge independent. With normalized Haar measure, its integral equals its evaluation after setting every node gauge element to the identity, equivalently every edge matrix to the 2x2 identity in the frozen `j=1/2` representation.

Lane A therefore needs no numerical group quadrature: it is an exact tensor contraction with the Iter077I node tensors.

## Algebraic gluing control

For one universal local extension coefficient `c`, write

`A_c = A_0 + c L`.

A two-vertex standard contraction across an internal basis `alpha` with source-backed weight `mu_alpha` is

`G_c = sum_alpha mu_alpha A_c^(1)(alpha) A_c^(2)(alpha)`.

Bilinearity gives identically

`G_c = G_00 + c(G_L0+G_0L) + c^2 G_LL`.

This identity holds for every value of `c`. Therefore standard state-sum composition can select `c` only if supplemented by an additional equation or normalization with a c-independent right-hand side. The frozen causal-vertex source does not supply such an equation.