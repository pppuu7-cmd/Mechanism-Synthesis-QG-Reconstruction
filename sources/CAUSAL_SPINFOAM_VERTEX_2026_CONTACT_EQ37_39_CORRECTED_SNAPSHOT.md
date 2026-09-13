# Corrected source snapshot — causal contact Eq. (37)-(39) and local extension theorem input

**Date:** 2026-09-14

## Primary causal-vertex source

Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162, Phys. Rev. D 113, 126020 (2026), DOI `10.1103/fwql-t4yr`.

Primary arXiv HTML re-checked on 2026-09-14:
`https://arxiv.org/html/2601.23162`.

The formulas below are transcribed from Appendix D Eqs. (37)-(39), not inferred from the earlier repository supplement.

### Exact contact formula

The causal spinor-basis restrictor is

`Theta_(sigma,rho,j)[x] = theta(sigma x) + sigma delta^(rho,j)(x)`.

Appendix D Eq. (37) gives

`delta^(rho,j)(x) = sum_{n=0}^{2j} [c_{n+1}^(rho,j)/(n+1)!] (-i)^(n+1) d^n/dx^n delta(x)`.

Appendix D Eq. (38) defines `c_n^(rho,j)` by derivatives, at equal spectral parameters, of the gamma-ratio polynomial `F_j`.

Appendix D Eq. (39) equivalently expands

`F_j(rho + sigma q,rho) = 1 + sum_{n=1}^{2j+1} c_n^(rho,j) (sigma q)^n/n!`.

**Source-lock warning:** Eq. (37) uses `c_{n+1}`, not `c_n`, and the factor is `(-i)^(n+1)`, not `(-1)^(n+1)`.

## Exact `j=1/2` consequence

For `j=1/2`, the gamma ratio reduces exactly to

`F_(1/2)(rho+q,rho) = ((rho+q)^2+1/4)/(rho^2+1/4)`.

Let

`D = rho^2 + 1/4`.

Comparison with Eq. (39) gives

`c_1 = 2 rho/D`,

`c_2 = 2/D`.

Substitution into source Eq. (37) gives the exact local contact distribution

`delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)`.

In the gamma-simple all-spin-half sector `rho=gamma/2`,

`A_gamma := coefficient(delta) = -4 i gamma/(1+gamma^2)`,

`C_gamma := coefficient(delta') = -4/(1+gamma^2)`.

Thus

`delta^(gamma/2,1/2)(x) = A_gamma delta(x) + C_gamma delta'(x)`.

For finite real `gamma`, `C_gamma` is always nonzero. For finite real `gamma != 0`, `A_gamma` is also nonzero.

For the frozen exact control `gamma=6/5`, `rho=3/5`,

`A_gamma = -120 i/61`,

`C_gamma = -100/61`.

## Fourier polynomial for the ten-contact target tensor

Using the convention `Fourier[delta]=1`, `Fourier[delta']=i xi`, one all-spin-half contact factor has polynomial

`P_e(xi_e)=A_gamma + i C_gamma xi_e`

`= -4 i (gamma+xi_e)/(1+gamma^2)`.

Therefore the ten-wedge pure contact tensor has Fourier polynomial

`P_10(xi)=K_gamma prod_e (gamma+xi_e)`,

where

`K_gamma = [-4 i/(1+gamma^2)]^10`.

At the frozen rank-9 self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`

in edge order `01,02,03,04,12,13,14,23,24,34`, the exact restriction is

`P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2 (gamma-t)`.

For finite real `gamma != 0`, this is a nonzero cubic polynomial in `t`. Hence along this exact conormal/self-stress direction the target contact tensor is not rapidly decreasing in Fourier space. This is sufficient for the corrected microlocal collision test at the frozen rank-9 source point; no false universal `-delta` normalization is needed.

## Generic versus exceptional pullback input

Authoritative source-map results already establish:

- `Iter077A-SM`: an exact rank-10 common-collision witness, so the true `B` map is a local submersion on an open neighborhood of that witness;
- `Iter077C-SM`: the frozen full-span rank-9 witness `xxxxxyyyzz` with nonzero left-null/self-stress `lambda` satisfying `J^T lambda=0`;
- canonical mixed `Iter077D-SM`: a nondegenerate six-dimensional quadratic excess normal form at the same rank-9 witness, determinant `-1`, inertia `(3+,3-)`.

The standard Hörmander pullback theorem is therefore locally automatic on the rank-10 submersion region. At the frozen rank-9 point, the exact self-stress covector belongs to the source-map normal set. The Fourier restriction above supplies the source-correct contact-wavefront witness in the same covector direction for `gamma != 0`.

Failure of this standard criterion is **not** a theorem that the source-selected spectral boundary value does not exist. It means that the exceptional point requires a correlated source-selected extension/boundary-value analysis.

## Scaling-degree theorem input

Primary mathematical source:
Romeo Brunetti and Klaus Fredenhagen, **“Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds”**, Commun. Math. Phys. 208, 623-661 (2000), arXiv:math-ph/9903028.

For a distribution on `R^d\{0}` of finite scaling degree `sd`:

- if `sd<d`, the extension across the origin preserving scaling degree is unique;
- if `sd>=d`, extension freedom is local at the origin and is bounded by the degree of divergence `sd-d`.

For a nondegenerate quadratic form `q` in six variables,

`delta^(n)(q(t x)) = t^[-2(n+1)] delta^(n)(q(x))`,

so

`sd[delta^(n)(q)] = 2(n+1)`.

Hence in transverse dimension `d=6`:

- `n=0`: `sd=2`, unique extension by scaling degree;
- `n=1`: `sd=4`, unique extension by scaling degree;
- `n=2`: `sd=6`, first marginal ambiguity, local order at most `0`;
- `n=3`: `sd=8`, extension nonunique by scaling degree alone, local derivative order at most `2`.

Before source symmetries/prescriptions, the unconstrained number of derivative-of-delta monomials of total order at most 2 in six variables is

`1 + 6 + 21 = 28`.

This number is only a dimension of the unconstrained local ambiguity space. The published spectral `i epsilon` prescription may select or cancel combinations; that is a separate source-selected correlated-extension gate.

## Scope firewall

This snapshot establishes the corrected local contact formula and the exact inputs for a new prospective gate. It does not establish full boundary contraction, a full causal-vertex finiteness/divergence theorem, regulator independence, a physical source-to-K4 pushforward, or a nominal `epsilon^-1` coefficient.