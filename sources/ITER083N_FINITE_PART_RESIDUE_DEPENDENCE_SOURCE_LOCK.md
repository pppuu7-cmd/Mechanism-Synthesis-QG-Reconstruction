# Iter083N source lock — finite-part dependence on Morse–Bott regularizer via residue

Date: 2026-09-15
Status: EXTERNAL MATHEMATICAL CROSSCHECK, NOT AUTOMATIC TOLLER APPLICABILITY

## External source
Giovanni Felder and David Kazhdan, “Regularization of divergent integrals”, Selecta Mathematica 24 (2018), 157–186, arXiv:1611.05057.

The paper studies divergent integrals of differential forms singular along a submanifold Y, regularized by a nonnegative Morse–Bott function mu vanishing on Y.

Theorem 1.1 / Theorem 2.7 gives the conformal-regularizer dependence of the Hadamard finite part. For a smooth function phi and conformally related regularizer `mu' = exp(2 phi) mu`, the finite part changes by a local residue term:

`I_finite(mu',omega) = I_finite(mu,omega) + I_0(mu,omega phi)`.

The residue coefficient `I_0=res_(s=0) zeta(s;mu,omega)` is independent of mu within the conformal class. The paper further identifies this coefficient locally through a residue map supported on Y.

The paper also proves additional parity statements in its differential-form singularity class, including vanishing of the residue in odd codimension. Iter083N does **not** import that odd-codimension conclusion to the K4 Toller object because membership of the Toller singularity in the required Felder–Kazhdan class has not been established.

## Algebraic distribution-valued version used in Iter083N
Independently of the full external theorem, if a distribution-valued analytic regularization has a Laurent expansion

`U_rho(z)=rho^z u=A_-1/z+A_0+O(z)`

and `rho'=exp(phi) rho`, then

`U_rho'(z)=exp(z phi)U_rho(z)`

implies formally and exactly

`Res_rho'=A_-1`,

`FP_rho' u-FP_rho u=phi A_-1`.

This formal Laurent identity is the actual theorem input. Felder–Kazhdan is an independent mathematical crosscheck that finite-part regularizer dependence is governed by local residue data.

## Repository scope
Iter083M fixes a unique local/tubular tangent radial quadratic basis but explicitly does not define a finite part.

Iter082D gives normal Taylor ceilings `omega=(0,3,8)` for K3/K4/K5.

Iter083B gives the deepest supported-distribution filtration through normal order 8.

## Forbidden implications
- Do not claim the physical Toller residue is nonzero in every supported-jet channel.
- Do not import Felder–Kazhdan odd-codimension residue vanishing to K4 without proving applicability.
- Do not claim that tangent metric data fix higher jets of a nonlinear Morse–Bott defining function.
- Do not promote the formal Laurent transformation law to a complete global K5 renormalization theorem.