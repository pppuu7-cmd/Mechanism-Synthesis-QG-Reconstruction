# Iter077D-SM result — rank-9 true B-map has a nondegenerate mixed six-dimensional second jet

**Date:** 2026-09-14

## Authority

Stable alias: `Iter077D-SM`.

- source second-jet supplement: `95da32f764381c26cd5c465c502cb1dbb9895d75`
- prospective preregistration: `3dbc24dd5c3dff17c832fe5cbc98d7b456157a27`
- implementation: `29e3f7a6fe843779061e4431985f4960f7d7a9e2`
- production/workflow head: `16a06049e6c1010e204d50eea597392a332651f3`
- authoritative run: `34785200044`
- jobs: A `103799289367`, B `103799289415`, C `103799289260`, D `103799289387`, aggregate `103799323384`

Artifacts:

- A `10326725635`, `sha256:c0896573e39adb0a27afc86d36f37386f68854b85226a733b7694c70f4bd71a7`
- B `10326426321`, `sha256:a571219ec7179ef5fbe9738b9e27345b991f5f4f3eeb41834da48a062cc414c0`
- C `10326108301`, `sha256:1d52340ab3f75709f6dedb00e28af6aff81ca17bd32ffe6d350771eb0c13e4b5`
- D `10325749197`, `sha256:8fcd95deb741f1865548ec01e8cbf28962db4b454875021e37f9517340b54a46`
- aggregate `10326287862`, `sha256:3ce9ff89385c905fba09c4d47bac7f7a30eef0312fdbd5e03c8311eb73e34347`

All frozen lanes A/B/C/D and the aggregate completed successfully.

## Frozen classification

`ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED`

## Exact source second jet

Starting from the source Eq. (32)

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`,

with `g_ab=g_b^-1 g_a`, `g_a=exp[(x_a.sigma)/2]`, the exact quadratic boost jet at the common collision is

`B_ab = n_ab.d_ab + (1/2)(|d_ab|^2-(n_ab.d_ab)^2) + O(3)`,

where `d_ab=x_a-x_b`.

For a tangent wedge-normal variation `n_ab -> n_ab+eta_ab`, `eta_ab.n_ab=0`, the source-selected mixed term is

`eta_ab.d_ab`.

Lane B verified the Pauli-matrix expansion symbolically: the order-one matrix coefficient is `(x_a-x_b).sigma` and the order-two coefficient is `(1/2)|x_a-x_b|^2 I` before taking the logarithm.

## Frozen rank-9 normal form

For the `Iter077C-SM` witness

`xxxxxyyyzz`

and self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`,

the true Jacobian retains:

- rank `9`;
- left nullity `1`;
- right nullity `3`.

A convenient exact right-kernel basis is:

1. common y displacement of nodes 1,2,3,4;
2. z displacement of node 1;
3. common z displacement of nodes 2,3,4.

On that basis the group-only Hessian of

`Phi=sum_e lambda_e B_e`

is

`[[0,0,0],[0,2,-1],[0,-1,0]]`,

so it has rank `2` and inertia `(+,-,0)`. Thus fixed normals alone leave one quadratic flat direction.

However, using the three source-normal tangent coordinates frozen by the previous exact transversality minor,

`eta_01^y, eta_01^z, eta_02^z`,

the mixed block is exactly

`L=diag(-1,-1,+1)`,

with `rank(L)=3` and `det(L)=1`.

The full symmetric six-dimensional Hessian

`H6=[[H_group,L],[L^T,0]]`

therefore has:

- rank `6`;
- determinant `-1`;
- exact congruence to the off-diagonal exchange form;
- inertia `(3 positive, 3 negative)`.

Hence the three-dimensional linear group-kernel degeneracy at this frozen rank-9 source point is fully lifted at second order once the source-normal tangent directions are included.

## Scientific consequence

The first tested exceptional source stratum is not protected by an exact higher-order flatness in the full local source-variable space. Its self-stress direction has a nondegenerate mixed quadratic normal form on a six-dimensional transverse slice.

This materially sharpens the next distributional question, but does **not** answer it: one must now combine this exact quadratic normal form with the source-selected one-dimensional causal/contact distribution and test local pullback/scaling, wavefront compatibility, extension freedom and regulator removal as distinct predicates.

The 2026 Toller analysis independently establishes that the `i epsilon` prescription uniquely projects the two Toller branches from the Wigner matrix and that the branches are polynomially bounded; this supports retaining the source selector rather than inventing an arbitrary finite part, but it does not by itself establish the correlated K5 pullback.

## Next admissible gate

Preregister the microlocal exceptional-stratum gate using this exact quadratic normal form. In parallel, the generic rank-10 region may be closed under the standard submersion pullback criterion, because it is logically independent of the rank-9 critical-point analysis. The final K5 boundary-value verdict must merge both regions and still retain all ten wedge factors and boundary contractions.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no exceptional-stratum Hörmander pullback theorem; no correlated K5 boundary-value theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.