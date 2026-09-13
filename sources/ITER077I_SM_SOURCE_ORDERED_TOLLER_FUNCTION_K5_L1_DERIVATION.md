# Iter077I-SM source/derived supplement — source-ordered j=1/2 Toller-function K5 leading collision

**Date:** 2026-09-14

## Primary sources

1. E. Bianchi, C. Chen, M. Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162, especially Eq. (3), Eq. (4), Eq. (7), and the gamma-simple reduced Toller formula Eq. (9).
2. E. Bianchi, C. Chen, M. Gamonal, **“Toller matrices and the Feynman i epsilon in spinfoams”**, arXiv:2604.24945, especially Sec. II-III and Eq. (13), Eq. (20), Eq. (46).

Primary HTML was re-checked on 2026-09-14.

Source facts used here:

- the causal vertex Eq. (4) is a product of ten Toller matrices followed by four gauge-fixed `SL(2,C)` integrations;
- the Feynman prescription uniquely projects the two Toller branches from the Wigner matrix;
- Toller matrices are polynomially bounded **functions** on `SL(2,C)`, not group representations;
- after the one-wedge spectral/spinor construction, the gamma-simple reduced Toller matrices have explicit hypergeometric closed forms.

Therefore this gate uses the source ordering

`one-wedge source construction -> ordinary Toller function -> K5 product -> group integration`,

not the termwise product of ten spinor-contact distributions that failed the rank-9 pullback criterion in Iter077G/H.

Machine-readable equivalent source-order lock used by the audit:

`one-wedge source construction -> Toller function -> K5 product -> group integration`.

The two displayed orderings are identical scientifically; `ordinary` only emphasizes that the already constructed one-wedge Toller object is treated as a function before K5 multiplication.

## Exact j=1/2 small-boost leading term from source Eq. (9)

For the gamma-simple diagonal reduced branch

`t^(plus/minus, gamma j,j)_(jjm)(beta)`,

source Eq. (9) has hypergeometric argument `z=e^(-2 beta)`. Its parameters obey

`c-a-b = -(2j+1)`.

At `j=1/2`, `c-a-b=-2`, so the leading singularity is `(1-z)^(-2) ~ (2 beta)^(-2)`.

Evaluating the gamma prefactors exactly gives, in the ascending magnetic basis `m=(-1/2,+1/2)`,

`t^(+,gamma/2,1/2)(beta) = [2/(1+gamma^2)] beta^(-2) diag(1,-1) + O(beta^(-1))`.

The opposite causal branch changes the common leading scale by a minus sign,

`t^(-,gamma/2,1/2)(beta) = -[2/(1+gamma^2)] beta^(-2) diag(1,-1) + O(beta^(-1))`.

For finite real gamma, the common scalar `2/(1+gamma^2)` is nonzero.

This agrees with the already closed source-backed Iter076U/V/X leading-shape recurrence and branch-scale relation.

## Off-axis leading matrix

Source compact covariance transports the z-axis leading matrix to a boost direction `n`:

`C_n = D^(1/2)(U_n) C_z D^(1/2)(U_n)^(-1)`,

`C_z=diag(1,-1)`.

In the ascending `(-1/2,+1/2)` basis, with Pauli generators,

`C_n = - n . sigma` up to an irrelevant common sign convention.

For an unnormalized nonzero relative boost vector `v`, a zero/nonzero equivalent exact matrix is

`M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]`.

The physical leading wedge coefficient additionally contains the nonzero scalar factor

`[2/(1+gamma^2)] r^(-2) |v|^(-3)`

(up to the branch sign) along a collision ray with `beta=r|v|+O(r^2)`. These omitted edge scalars cannot change whether the contracted angular coefficient vanishes.

## Frozen common-collision ray

Gauge fix `x_0=(0,0,0)` and freeze

- `x_1=(1,2,3)`
- `x_2=(2,3,5)`
- `x_3=(3,5,7)`
- `x_4=(5,7,11)`.

Use

`g_a(r)=exp[r (x_a . sigma)/2]`.

All ten differences `v_ab=x_a-x_b` are nonzero. Hence every wedge has

`beta_ab(r)=r |v_ab|+O(r^2)`

and every `j=1/2` Toller branch contributes leading radial power `r^(-2)`.

The ten-wedge product therefore has raw radial power `r^(-20)` before boundary contraction.

## Complete all-j=1/2 boundary basis

Each four-valent node with four `j=1/2` legs has two SU(2)-invariant recoupling states, intermediate spin `k=0` or `k=1`. The five-node boundary basis therefore has exactly

`2^5=32`

components.

For exact zero/nonzero contraction certificates, strip only nonzero common node normalizations. In ascending magnetic order `(-,+)` the scaled integer tensors are:

### node k=0, scale factor 2

- `(-,+,-,+) -> +1`
- `(-,+,+,-) -> -1`
- `(+,-,-,+) -> -1`
- `(+,-,+,-) -> +1`

### node k=1, after stripping common sqrt(3)/6

- `(-,-,+,+) -> +2`
- `(-,+,-,+) -> -1`
- `(-,+,+,-) -> -1`
- `(+,-,-,+) -> -1`
- `(+,-,+,-) -> -1`
- `(+,+,-,-) -> +2`.

The stripped normalizations are nonzero, so exact zero/nonzero status is unchanged.

Edge-matrix orientation follows the causal-vertex repository convention: for wedge `(a,b)` with `a<b`, row index is the target half-edge `(b,a)` and column index the source half-edge `(a,b)`.

## Local absolute-integrability criterion

Near the common collision, the four non-root boost variables give transverse dimension

`d = 4*3 = 12`.

The radial volume element is `r^(d-1) dr = r^11 dr` times a smooth nonzero angular density.

If the complete leading boundary contraction is nonzero at one exact angular witness, analyticity makes it nonzero on an open angular neighborhood. With ten wedge powers `r^-2`, the absolute radial behavior there is

`r^(11-20) dr = r^-9 dr`.

Equivalently the first-moment margin is

`q+d = -20+12 = -8 < 0`.

Therefore such a component is **not locally absolutely integrable** around the common collision in the source-ordered Toller-function representation.

This criterion is only local `L^1`. It does not prove nonexistence of an oscillatory/distributional boundary value, nor the divergence of the full causal vertex as a distribution.

## Causal-branch scope

At leading order, switching a wedge from `T+` to `T-` multiplies its matrix by a nonzero common sign and does not alter the angular matrix shape or radial power. For a fixed factorized causal assignment, the ten-edge leading boundary contraction therefore changes by an overall nonzero sign only.

No sum over causal sectors is used in the verdict; possible cancellations between different causal sectors remain outside this gate.

## Claim firewall

No full source-vertex divergence/nonexistence theorem; no correlated boundary-value theorem; no regulator-independence theorem; no source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion.