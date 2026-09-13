# Iter077D-SM source/derived supplement — nonlinear excess `B` jet on the frozen rank-9 source stratum

**Date:** 2026-09-14

## Source authority

Primary source remains Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162, especially Eq. (17) and Appendix C Eq. (32):

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`.

No new external physical assumption is introduced here.

## Frozen exceptional source point

Authoritative `Iter077C-SM` fixes the first full-span rank-9 axis witness

`xxxxxyyyzz`

in edge order `01,02,03,04,12,13,14,23,24,34`, with exact source self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

Hence the excess source constraint is

`Phi = B_01 - B_02 + B_12`.

All three stressed wedges have Bloch normal `n=e_x`; use the same projective representative `z_x=(1,1)` on these axis controls.

## Exact relative-group expansion through second order

Use Hermitian boost coordinates

`g_a(t)=exp[t X_a/2]`,  `X_a=x_a.sigma`,  `X_0=0`.

For edge `(ab)`,

`g_ab=g_b^(-1)g_a=exp[-t X_b/2] exp[t X_a/2]`.

Because the generators are Hermitian,

`g_ab g_ab^dagger = exp[-t X_b/2] exp[t X_a] exp[-t X_b/2]`.

Direct multiplication gives

`g_ab g_ab^dagger = I + t(X_a-X_b) + t^2 (X_a-X_b)^2/2 + O(t^3)`.

For Pauli generators `(d.sigma)^2=|d|^2 I`. Therefore, with `d_ab=x_a-x_b` and Bloch vector `n_ab`,

`B_ab(t) = t n_ab.d_ab + t^2 [|d_ab|^2-(n_ab.d_ab)^2]/2 + O(t^3)`.

This is the true source Eq. (32) Hessian at the common collision; it is not a scalar-incidence surrogate.

## Frozen right-kernel coordinates

Use the exact right-kernel basis recorded by `Iter077C-SM` and coordinates `(a,b,c)`:

- `r1`: `x_1=e_z`, other non-root nodes zero;
- `r2`: `x_1=x_2=x_3=x_4=e_y`;
- `r3`: `x_2=x_3=x_4=e_z`, `x_1=0`.

Thus on `ker dB`,

`x_1 = b e_y + a e_z`,

`x_2=x_3=x_4 = b e_y + c e_z`.

Since the stressed normals are `e_x`, every stressed first-order projection `n.d` vanishes on this kernel.

The quadratic excess coefficient is therefore prospectively predicted as

`Phi(t) = a(a-c) t^2 + O(t^3)`.

Equivalently, in the convention `Phi_2=(1/2) u^T H u`, `u=(a,b,c)`,

`H = [[2,0,-1],[0,0,0],[-1,0,0]]`.

Frozen prediction: `rank(H)=2`, signature `(1 positive, 1 negative, 1 zero)`.

## Exact flat and isotropic controls to test

1. **Exact diagonal plane `a=c`.** Then `X_1=X_2`, so `g_1=g_2`, `B_12=0`, and because the stressed root wedges use the same `e_x` spinor, `B_01=B_02`. Hence

   `Phi(t)=0` exactly for all `t` on the plane `a=c` within this frozen path family.

2. **Hessian-kernel axis `a=c=0`.** This is contained in the exact diagonal plane and is therefore exactly flat.

3. **Second quadratic isotropic branch `a=0`.** The quadratic term vanishes but exact equality of the two node group variables is absent when `c != 0`. The preregistered symbolic gate will determine the first nonzero higher-order term rather than declaring it zero from the Hessian.

## Scope firewall

- This supplement concerns one frozen exact rank-9 common-collision source stratum and one source-faithful exponential path family through its group-variable right kernel.
- It does not establish a full normal form including all spinor-normal directions.
- It does not yet establish a distributional pullback, local integrability, a regulator-independent vertex, a physical source-to-K4 map, or a nominal `epsilon^-1` coefficient.
- Odd/even higher-order cancellations must be checked from the exact source matrix expression; they are not assumed by symmetry.