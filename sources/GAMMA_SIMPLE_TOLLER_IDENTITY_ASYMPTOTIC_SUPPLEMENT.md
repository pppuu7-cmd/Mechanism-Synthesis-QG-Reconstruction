# Gamma-simple Toller identity asymptotic supplement

Date: 2026-09-13

## Primary source formula

Primary source: E. Bianchi, C. Chen, M. Gamonal, **Causal spinfoam vertex for 4d Lorentzian quantum gravity**, arXiv:2601.23162 (2026), Eq. (9), together with the companion Toller-matrix paper arXiv:2604.24945.

For the gamma-simple representation `(rho,k)=(gamma j,j)`, the reduced causal Toller branch is

`t_±(beta) = exp[-E_± beta] P_± * 2F1(a_±,b_±;c_±; exp(-2 beta))`,

where

`E_+ = j - i gamma j + m + 1`,

`E_- = j + i gamma j - m + 1`,

`a_+ = j + m + 1`, `b_+ = j + 1 - i gamma j`, `c_+ = 1 + m - i gamma j`,

`a_- = j - m + 1`, `b_- = j + 1 + i gamma j`, `c_- = 1 - m + i gamma j`,

and the beta-independent source prefactors are

`P_+ = Gamma(2j+2) Gamma(i gamma j - m) / [Gamma(j-m+1) Gamma(j+1+i gamma j)]`,

`P_- = Gamma(2j+2) Gamma(-i gamma j + m) / [Gamma(j+m+1) Gamma(j+1-i gamma j)]`.

Scope for the local derivation below: `j` is a positive half-integer, `m=-j,-j+1,...,j`, and real `gamma != 0`. Thus `n:=2j+1` is an integer with `n>=2`.

## Derived hypergeometric identity-singularity structure

The following is an algebraic consequence of the source Eq. (9), not an additional source quote.

For both branches,

`c_± - a_± - b_± = -(2j+1) = -n`.

Set

`w = 1-exp(-2 beta)`.

The hypergeometric differential equation becomes

`w(1-w) F_ww + [n+1-(a+b+1)w] F_w - ab F = 0`.

For `n>=2`, write its leading singular expansion as

`F(w) = A0 w^(-n) [1 + r w + O(w^2)] + later resonant/log terms`.

The first two singular coefficients are fixed before any possible logarithmic term. Substitution into the exact differential equation gives

`r = (n c - a b)/(n-1)`.

For the two gamma-simple branches this simplifies exactly to

`r_+ = -(1+i gamma)(j-m)/2`,

`r_- = -(1-i gamma)(j+m)/2`.

The leading continuation coefficient is proportional to

`A0 = Gamma(c) Gamma(n) / [Gamma(a) Gamma(b)]`.

For the frozen scope `j>0`, real `gamma!=0`, and admissible `m`, the relevant Gamma-function arguments have no pole or zero that annihilates this leading coefficient; consequently the leading `beta^(-n)` branch coefficient is nonzero.

## Minimal power-stripped normalized C1 germ

Define only as an algebraic source-control object

`G_±(beta) := beta^n t_±(beta) / C_±`,

where

`C_± := lim_(beta->0+) beta^n t_±(beta)`.

This removes only the frozen leading power and normalizes the constant to one. It is **not** asserted to be the unique physical singular/contact factorization of the full causal vertex.

Using

`w = 2 beta (1-beta+O(beta^2))`,

we have, to first order,

`(beta/w)^n / (1/2)^n = 1 + n beta + O(beta^2)`,

`exp(-E_± beta) = 1-E_± beta+O(beta^2)`,

and

`1+r_± w = 1+2 r_± beta+O(beta^2)`.

Therefore

`G_±'(0+) = n - E_± + 2 r_±`.

Both branches simplify to the same exact result

`G_+'(0+) = G_-'(0+) = i gamma m`.

Consequences inside this strictly wedge-level minimal-power normalization:

- for `m=0`, the one-jet vanishes;
- for `m!=0` and `gamma!=0`, the one-jet is nonzero;
- branch sign alone does not flip this normalized one-jet;
- the result has not yet been contracted with boundary intertwiners and has not been converted into source cut-space or K4 cycle coordinates.

## Resonant/logarithmic caution

Because `c-a-b=-n` is a negative integer, the continuation around `w=0` is resonant and logarithmic terms can occur after the finite singular tower. For `n>=2`, after multiplication by `beta^n` these terms begin no earlier than `O(beta^n log beta)`, which does not alter the finite right one-jet at `beta=0`. This supplement therefore freezes only the leading singular order and first normalized derivative; it does not claim a full analytic Taylor series for `G_±`.

## Scope lock

This supplement does not establish:

- a unique physical EPRL/Toller singular-contact factorization;
- the full wedge matrix one-jet in arbitrary tangent direction (KAK coordinates are singular at the identity);
- cancellation or survival after boundary-intertwiner contraction;
- a source-to-K4 map or its physical quadratic curvature;
- the nominal `epsilon^-1` coefficient.

The next meaningful question after exact confirmation is whether the `i gamma m` wedge-level first coefficient is annihilated, reorganized, or survives when the full source boundary/intertwiner contraction and gauge-fixed relative-group tangent structure are treated covariantly.