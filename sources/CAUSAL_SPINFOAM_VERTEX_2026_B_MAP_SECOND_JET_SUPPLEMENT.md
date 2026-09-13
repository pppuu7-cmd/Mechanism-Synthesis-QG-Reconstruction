# Source/derived supplement — true causal-vertex B-map second jet at the rank-9 source stratum

**Date:** 2026-09-14

## Scope and authority

Primary source: Bianchi, Chen, Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

This supplement starts from the source Eq. (32)

`B(z,g) = log(<g^dagger z|g^dagger z>/<z|z>)`

and the already frozen common-collision coordinates

`g_a(x_a)=exp[(x_a . sigma)/2]`, `x_0=0`,

with wedge relative variable `g_ab=g_b^-1 g_a` and wedge-local Bloch vector `n_ab`.

It derives only the local second jet needed after `Iter077C-SM`. It does not establish a Hörmander product theorem, a global correlated K5 boundary value, a full-vertex finiteness theorem, or a physical source-to-K4 pushforward.

## Fixed-normal second-order expansion

Write

`A=(x_a . sigma)/2`, `C=(x_b . sigma)/2`.

Then

`g_ab g_ab^dagger = exp(-C) exp(2A) exp(-C)`.

To quadratic order in the boost variables,

`exp(-C) exp(2A) exp(-C)`

`= I + 2(A-C) + 2(A-C)^2 + O(3)`.

Because `(v . sigma)^2 = |v|^2 I`, taking the normalized spinor expectation gives

`<g_ab^dagger z|g_ab^dagger z>/<z|z>`

`= 1 + n_ab . d_ab + (1/2)|d_ab|^2 + O(3)`,

where `d_ab=x_a-x_b`.

Taking the logarithm therefore yields the exact second jet

`B_ab = n_ab . d_ab + (1/2)(|d_ab|^2-(n_ab . d_ab)^2) + O(3)`.

Equivalently, the fixed-normal boost Hessian on the relative coordinate is

`H_ab = I_3 - n_ab n_ab^T`.

Thus the quadratic boost response is the Euclidean projector transverse to the wedge Bloch direction.

## Including first normal-direction variation

Let `n_ab -> n_ab + eta_ab` with `eta_ab . n_ab = 0` at first order. Since `B(z,1)=0` identically in the spinor variable, there is no pure-normal term at the collision. The mixed second jet is

`B_ab = n_ab . d_ab + eta_ab . d_ab + (1/2)(|d_ab|^2-(n_ab . d_ab)^2) + O(3)`.

The bilinear term `eta_ab . d_ab` is therefore source-selected; it is not an added regulator or fitted counterterm.

## Frozen Iter077C-SM rank-9 witness

Use K5 edge order

`01,02,03,04,12,13,14,23,24,34`.

The frozen first full-span rank-9 axis witness is

`xxxxxyyyzz`,

so

- edges `01,02,03,04,12` have `n=e_x`;
- edges `13,14,23` have `n=e_y`;
- edges `24,34` have `n=e_z`.

The exact one-dimensional left null/self-stress is

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

Hence only the x-normal triangle `01,02,12` appears in the contracted singular direction

`Phi = sum_e lambda_e B_e`.

The group-variable right kernel of the rank-9 Jacobian has dimension 3. One convenient exact basis is:

1. `r_y`: common y displacement at nodes 1,2,3,4;
2. `r_z1`: z displacement at node 1 only;
3. `r_z234`: common z displacement at nodes 2,3,4.

On this basis the purely group quadratic term of `Phi` is

`Phi_group^(2) = q_z1^2 - q_z1 q_z234`,

with the common-y direction flat at fixed normals. Therefore the group-only Hessian has rank 2 and signature `(1,1,1 zero)`.

## Mixed normal/group transversality

Choose the three normal-tangent coordinates already identified by the exact `Iter077C-SM` structured-normal minor:

- `eta_01^y`,
- `eta_01^z`,
- `eta_02^z`.

Against the right-kernel basis `(r_y,r_z1,r_z234)`, the mixed second derivative block is diagonal up to basis/orientation signs and has determinant of absolute value 1. In the explicit basis above it is

`L = diag(-1,-1,+1)`.

Therefore `rank(L)=3`.

The symmetric Hessian of `Phi` on the six variables

`(r_y,r_z1,r_z234, eta_01^y,eta_01^z,eta_02^z)`

has block form

`H_6 = [[H_group, L],[L^T,0]]`.

Because `L` is invertible, `H_6` is nondegenerate with

- rank `6`;
- determinant `-det(L)^2 = -1` in this exact normalization;
- inertia/signature `(3 positive, 3 negative)`.

This provides an exact quadratic source normal form at the frozen rank-9 witness. It does **not** by itself determine the wavefront set or the existence/uniqueness of the pulled-back contact distribution.

## Firewall

The following remain unproved:

- `HORMANDER_PULLBACK_AT_EXCEPTIONAL_STRATUM`;
- `CORRELATED_TOLLER_GROUP_BOUNDARY_VALUE`;
- `PHYSICAL_SOURCE_TO_K4_PUSHFORWARD`;
- `PHYSICAL_REDUCED_K4_NUMERATOR_COEFFICIENT`;
- `EPSILON_MINUS1_COEFFICIENT`;
- causal-vertex finiteness/divergence;
- regulator independence;
- G3/F9/G8/K5 promotion.

Retain the published finite-spectral `i epsilon` prescription.