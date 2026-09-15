# Iter083F-SM theorem derivation — finite common spectral epsilon does not regularize the K5 common collision

Date: 2026-09-15

Prospective contract: `prereg/ITER083F_SM_COMMON_SPECTRAL_EPSILON_NOT_K5_COLLISION_REGULATOR.md`, commit `18fbeca191aa05fe09e3e38ed60abec53e09a8c9`.

Public-source lock: `sources/ITER083F_PUBLIC_SOURCE_LOCK.md`, commit `d69eb1b5c187be257c507cdc3527ec4f9e824c97`.

## 1. Finite-epsilon contour object

The Toller companion defines the finite-epsilon linear functional

`I_epsilon^(+-)[f] = integral d rho_tilde/(2 pi i) [+- P_jl(rho_tilde;rho)/(rho_tilde-rho -+ i epsilon)] f(rho_tilde)`.

Write the Wigner function as `d=t^+ + t^-`.

For the plus functional, `P_jl t^+` has all Toller poles cancelled and the only remaining upper-half-plane pole is the Feynman pole `rho_tilde=rho+i epsilon`. The cross term `I_epsilon^+[t^-]` closes in the lower half-plane and contains no shifted Feynman pole. Therefore, already at fixed admissible `epsilon>0`,

`I_epsilon^+[d] = P_jl(rho+i epsilon;rho) t^+(rho+i epsilon,beta)`.

Analogously,

`I_epsilon^-[d] = P_jl(rho-i epsilon;rho) t^-(rho-i epsilon,beta)`.

The published Toller matrix is obtained only after the limit `epsilon->0+`. Iter083F deliberately studies the finite-epsilon expressions before that limit.

## 2. Exact j=1/2 kernel

For `j=l=1/2`, Eq. (16) has two factors:

`P = [(i rho_tilde+1/2)(i rho_tilde-1/2)] / [(i rho+1/2)(i rho-1/2)]`.

Both numerator and denominator equal minus the corresponding `rho^2+1/4`, so

`P_(1/2,1/2)(rho_tilde;rho)=(rho_tilde^2+1/4)/(rho^2+1/4)`.

This identity is exact for complex `rho_tilde`.

## 3. Fixed-epsilon plus branch, m=+1/2

Table II gives

`t^+(rho',beta) = - exp(i rho' beta) / [2 sinh(beta)^2 (rho'^2+1/4)]`.

Set `rho'=rho+i epsilon` and multiply by the kernel:

`I_epsilon^+[d]_(m=+1/2)`

`= [(rho'^2+1/4)/(rho^2+1/4)] [-exp(i rho' beta)/(2 sinh(beta)^2 (rho'^2+1/4))]`

`= - exp(i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`.

The shifted pole denominator has cancelled completely.

As `beta->0+`,

`exp(-epsilon beta)=1+O(beta)`,

`sinh(beta)^-2=beta^-2+O(1)`.

Therefore

`I_epsilon^+[d]_(m=+1/2) = -[2(rho^2+1/4)]^-1 beta^-2 + O(beta^-1)`.

The leading coefficient is independent of epsilon.

## 4. Fixed-epsilon plus branch, m=-1/2

Table II gives

`t^+(rho',beta)= exp(i rho' beta)[cosh(beta)-2 i rho' sinh(beta)] / [2 sinh(beta)^2(rho'^2+1/4)]`.

With `rho'=rho+i epsilon`,

`-2 i rho' = -2 i rho + 2 epsilon`.

After exact kernel cancellation,

`I_epsilon^+[d]_(m=-1/2)`

`= exp(i rho beta)exp(-epsilon beta)[cosh(beta)-2 i rho sinh(beta)+2 epsilon sinh(beta)]/[2(rho^2+1/4)sinh(beta)^2]`.

The bracket is `1+O(beta)`, hence

`I_epsilon^+[d]_(m=-1/2)=+[2(rho^2+1/4)]^-1 beta^-2+O(beta^-1)`.

Again the leading coefficient is epsilon independent.

## 5. Minus branch

For `m=+1/2`, Table II gives

`t^-(rho',beta)= exp(-i rho' beta)[cosh(beta)+2 i rho' sinh(beta)]/[2sinh(beta)^2(rho'^2+1/4)]`.

Set `rho'=rho-i epsilon`. Then

`exp(-i rho' beta)=exp(-i rho beta)exp(-epsilon beta)`

and

`2 i rho'=2 i rho+2 epsilon`.

Thus

`I_epsilon^-[d]_(m=+1/2)`

`= exp(-i rho beta)exp(-epsilon beta)[cosh(beta)+2 i rho sinh(beta)+2 epsilon sinh(beta)]/[2(rho^2+1/4)sinh(beta)^2]`

and the leading coefficient is

`+[2(rho^2+1/4)]^-1`.

For `m=-1/2`, Table II gives the pure exponential branch,

`t^-(rho',beta)=-exp(-i rho' beta)/[2sinh(beta)^2(rho'^2+1/4)]`,

so

`I_epsilon^-[d]_(m=-1/2)=-exp(-i rho beta)exp(-epsilon beta)/[2(rho^2+1/4)sinh(beta)^2]`

with leading coefficient

`-[2(rho^2+1/4)]^-1`.

## 6. Gamma-simple value

In the EPRL gamma-simple minimal-spin sector,

`rho=gamma j=gamma/2`.

Therefore

`1/[2(rho^2+1/4)]`

`=1/[2(gamma^2/4+1/4)]`

`=2/(1+gamma^2)`.

This is exactly the magnitude already frozen in Iter077I after the epsilon limit. The finite spectral epsilon has not changed the leading collision coefficient at all.

## 7. Full Toller matrix

The Cartan reconstruction multiplies the reduced `m=+-1/2` entries by finite SU(2) Wigner matrices. The finite-epsilon operation affects only the reduced spectral/boost factor. Since the leading reduced diagonal coefficients are exactly the same as at epsilon zero, the leading full matrix is the same Iter077I angular matrix with the same branch sign.

Schematically,

`T_epsilon^(+-)(beta,U1,U2)`

`= (+- sign) [2/(1+gamma^2)] beta^-2 A(U1,U2) + O(beta^-1)`

with the same nonzero `A` as in Iter077I, independently of fixed epsilon.

## 8. Ten-wedge common collision

Take the same frozen radial common-collision path and angular witness used in Iter077I. Every one of the ten rapidities scales as

`beta_e = r b_e + O(r^2)`

with nonzero frozen angular data `b_e` on the witness.

Each finite-epsilon Toller factor contributes the same nonzero order `r^-2` leading tensor as at epsilon zero. Consequently

`product_(e in E(K5)) T_epsilon^(kappa_e)`

has the same nonzero leading boundary-contracted tensor

`C_kappa(gamma,angles) r^-20 + O(r^-19)`.

The exponential factors satisfy

`product_e exp(-epsilon beta_e)=1+O(r)`

at fixed epsilon and therefore cannot change the leading radial order.

Thus the fixed-epsilon transverse scaling degree is exactly 20.

## 9. Finite epsilon is not a common-collision regulator

The normal codimension of `N` is 12. In polar normal coordinates the local measure contributes `r^11 dr`, while the leading integrand contributes `r^-20`, producing radial behavior

`r^-9 dr`.

This is not locally integrable at `r=0`.

Therefore the finite common spectral epsilon does not define the K5 product distribution across `N`. It shifts spectral poles and introduces factors regular at `beta=0`; it does not soften the normal collision singularity.

The same distributional extension problem remains at every fixed finite spectral epsilon unless additional joint information is supplied.

## 10. Regulator classification

The exact scoped conclusion is

`COMMON_FINITE_ONE_WEDGE_SPECTRAL_EPSILON_IS_NOT_A_K5_COLLISION_REGULATOR_IN_THE_FROZEN_J_HALF_SECTOR`.

This is a stronger refinement of Iter083E: not only is the published epsilon prescription applied too early to select the joint extension, but even the simplest reversed-order experiment — holding that same spectral epsilon finite across all ten wedges — leaves the K5 collision degree unchanged.

A successful genuinely joint prescription must therefore do something more than keep the existing spectral pole shift finite. It could, for example, regulate group-normal variables, alter scaling exponents analytically, impose a several-variable boundary value, define a renormalized multiplication plus normalization, or add a composition/gluing law acting on the supported ambiguity.

## Interpretation ceiling

This theorem does not rule out all common regulators or multivariable analytic prescriptions. It does not prove causal-vertex nonexistence/divergence as a renormalized distribution, generic-spin completeness, global all-strata patching, regulator dependence/independence, multivertex closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
