# Iter077H-SM source/derived supplement — finite spectral epsilon does not smooth the j=1/2 contact term

**Date:** 2026-09-14

## Primary source

E. Bianchi, C. Chen, M. Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162, especially Eq. (35)-(39).

The source defines, before taking the limit, the one-wedge spectral kernel

`Theta_(sigma,rho,j;epsilon)(x) := integral dp/(2 pi i) [sigma/(p-i sigma epsilon)] F_j(rho+p,rho) exp(i p x)`,

with `epsilon>0`. The published distribution `Theta_(sigma,rho,j)` is the `epsilon -> 0+` boundary value.

This supplement derives the finite-epsilon `j=1/2` distribution exactly. It does not assume that finite epsilon is a coordinate-space mollifier.

## Exact j=1/2 spectral polynomial

Let

`D=rho^2+1/4`,

`c1=2 rho/D`,

`c2=2/D`.

Then

`F_(1/2)(rho+p,rho)=1+c1 p+(c2/2) p^2`.

Set `a=i sigma epsilon`. Exact polynomial division gives

`F/(p-a) = (c2/2) p + c1 + a c2/2 + [1+a c1+a^2 c2/2]/(p-a)`.

Multiplying by the source numerator `sigma`, the polynomial part is

`sigma(c2/2)p + sigma c1 + i epsilon c2/2`.

The pole remainder is

`sigma[1+i sigma epsilon c1-epsilon^2 c2/2]/(p-i sigma epsilon)`.

## Exact Fourier identities

With the source convention `1/(2 pi i)`:

`integral dp/(2 pi i) exp(i p x) = -i delta(x)`,

`integral dp/(2 pi i) p exp(i p x) = -delta'(x)`,

and

`sigma integral dp/(2 pi i) exp(i p x)/(p-i sigma epsilon) = theta(sigma x) exp(-epsilon |x|)`.

Therefore

`Theta_(sigma,rho,1/2;epsilon)(x)`

`= [1+i sigma epsilon c1-epsilon^2 c2/2] theta(sigma x) exp(-epsilon |x|)`

`  + [epsilon c2/2-i sigma c1] delta(x)`

`  - sigma c2/2 delta'(x)`.

Equivalently,

`Theta_(sigma,rho,1/2;epsilon)(x)`

`= [1+(2 i sigma rho epsilon-epsilon^2)/D] theta(sigma x) exp(-epsilon |x|)`

`  + [(epsilon-2 i sigma rho)/D] delta(x)`

`  - [sigma/D] delta'(x)`.

The delta-prime coefficient is **independent of epsilon** and nonzero for every finite real rho and every epsilon>0.

Taking `epsilon -> 0+` gives exactly

`theta(sigma x)+sigma delta^(rho,1/2)(x)`

with the corrected Appendix-D contact formula

`delta^(rho,1/2)=-(2 i rho/D)delta-(1/D)delta'`.

## Gamma-simple form

For `rho=gamma/2`,

`D=(1+gamma^2)/4`.

The finite-epsilon contact coefficients are

`A_(sigma,epsilon)=4[epsilon-i sigma gamma]/(1+gamma^2)` multiplying `delta`,

`C_sigma=-4 sigma/(1+gamma^2)` multiplying `delta'`.

For every finite real gamma and every epsilon>0, `A_(sigma,epsilon)` and `C_sigma` are both nonzero.

At frozen `gamma=6/5`,

`A_(sigma,epsilon)=(100 epsilon-120 i sigma)/61`,

`C_sigma=-100 sigma/61`.

## Rank-9 pure-contact consequence

For ten wedges, expand the tensor product of the ten finite-epsilon `Theta` factors by support type. Its all-contact subterm is the tensor product

`prod_e [A_(sigma_e,epsilon) delta(B_e)+C_(sigma_e) delta'(B_e)]`.

For the frozen source self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`

on edges `01,02,12`, the Fourier polynomial of this pure-contact subterm restricted to `xi=t lambda` has degree 3. Its leading coefficient is

`prod_(e notin supp lambda) A_(sigma_e,epsilon)`

`* prod_(e in supp lambda) [i C_(sigma_e) lambda_e]`.

For finite real gamma and epsilon>0 this coefficient is nonzero for **every** assignment of wedge signs `sigma_e=+/-1`. Hence finite spectral epsilon does not remove the rank-9 order-3 pure-contact obstruction termwise.

This is deliberately weaker than a theorem for the full sum of Heaviside/contact support strata. It rules out only the naive claim that finite spectral epsilon itself smooths the contact distributions so that the standard termwise pullback becomes automatically legal.

## Scope firewall

- No full correlated boundary value is constructed here.
- No cancellation/non-cancellation theorem after summing support strata is claimed.
- No CP1 spinor integration, smooth phase/measure factor or boundary intertwiner contraction is included in this finite-epsilon identity.
- No causal-vertex finiteness/divergence theorem or nominal epsilon^-1 coefficient follows.