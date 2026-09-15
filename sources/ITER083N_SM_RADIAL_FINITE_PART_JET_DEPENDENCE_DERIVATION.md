# Iter083N-SM derivation — finite-part change equals residue times defining-function jet

Date: 2026-09-15
Status: PRE-PRODUCTION DERIVATION AFTER PROSPECTIVE PREREGISTRATION

Preregistration: `prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md`, commit `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.

## 1. Formal Laurent transformation
Let rho be a smooth positive defining regularizer off N and assume the analytic family has a simple Laurent pole

`U_rho(z)=rho^z u=A_-1/z+A_0+A_1 z+...`.

For a conformal change

`rho'=exp(phi) rho`,

we have

`U_rho'(z)=exp(z phi)U_rho(z)`.

Since

`exp(z phi)=1+z phi+O(z^2)`,

multiplication gives

`U_rho'(z)=A_-1/z + (A_0+phi A_-1)+O(z)`.

Therefore

`Res_rho'=A_-1`,

`FP_rho' u-FP_rho u=phi A_-1`.

This is distribution-valued and requires no scalarization of the residue.

## 2. Supported-distribution jet annihilator
In one normal coordinate n,

`n delta^(k)=-k delta^(k-1)`.

Iteration gives

`n^q delta^(k)=(-1)^q k!/(k-q)! delta^(k-q)` for `q<=k`,

and zero for `q>k`.

The multivariable statement is the standard ideal-filtration version: if T is supported on N with normal order at most omega, then

`I_N^(omega+1) T=0`.

Conversely, if phi has a first nonzero normal Taylor term of degree q<=omega, an order-q normal derivative delta distribution in the matching direction gives a nonzero product `phi T`.

Thus `phi in I_N^(omega+1)` is the sharp **universal** condition that annihilates every possible supported residue of order <=omega.

This is a universal-space statement. A particular physical residue may have smaller order or lie in an annihilator subspace and therefore require fewer jets.

## 3. K3/K4/K5 thresholds
The authoritative forest ceilings are

`omega_K3=0`,

`omega_K4=3`,

`omega_K5=8`.

Therefore universal conformal defining-function independence requires

- K3: `phi in I_N^1`;
- K4: `phi in I_N^4`;
- K5: `phi in I_N^9`.

## 4. What the Iter083M tangent metric fixes
Take two conformally related Morse–Bott functions with the same quadratic Hessian on the normal bundle,

`rho'=exp(phi) rho`.

Along N, Hessian scaling gives

`Hess_N(rho')=exp(phi|_N) Hess_N(rho)`.

Equality of the normalized Hessians therefore requires

`phi|_N=0`,

so `phi in I_N`.

That is exactly enough to annihilate every order-zero residue, hence the K3 universal residue space.

It is not enough, by itself, to annihilate arbitrary order-1..3 K4 residues or order-1..8 K5 residues. Higher normal jets of phi must be fixed or the actual residue must annihilate them.

## 5. Constant scale
If `rho'=c rho` with positive constant c, then `phi=log c` and

`FP_(c rho)u-FP_rho u=(log c) A_-1`.

Thus a free overall scale matters whenever the residue is nonzero. If the source rapidity convention fixes the normalization of rho, this specific constant freedom is removed; the higher-jet issue for omega>0 remains.

## 6. Relation to external finite-part theory
Felder–Kazhdan independently obtain the same structural phenomenon for Hadamard finite parts defined with Morse–Bott functions: conformal changes of the regularizer alter the finite part by a local residue term.

Their additional parity theorem belongs to their differential-form singularity class and is not assumed here for the Toller object.

## 7. Exact research consequence
Iter083M supplies canonical tangent radial geometry, but a universal finite-part selector for K4/K5 requires more:

- an exact nonlinear source-defined radial function whose relevant normal jets are fixed through the required order; or
- an actual residue theorem showing that the unfixed defining-function jets annihilate the source residue.

## 8. Scope ceiling
No actual nonzero physical scheme dependence is proved. No statement is made that the Toller residue fills the whole supported-jet space. No automatic Felder–Kazhdan applicability, K4 parity simplification, global K5 renormalization, regulator dependence/independence, unique extension, G3/F9/G8/K5 promotion, NEW_PHYSICS_FOUND or complete-QG claim follows.