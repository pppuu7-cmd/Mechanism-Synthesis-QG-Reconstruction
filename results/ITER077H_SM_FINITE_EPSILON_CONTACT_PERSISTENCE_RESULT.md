# Iter077H-SM result — finite spectral epsilon leaves the rank-9 pure-contact obstruction termwise

**Date:** 2026-09-14

## Authority

- source/derived supplement: `sources/ITER077H_SM_FINITE_EPSILON_JHALF_CONTACT_DERIVATION.md`, commit `b7abbd430313b0624e1b0dfeb12025f5e8753539`
- prospective preregistration: `prereg/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE.md`, commit `cf6620e91ae9ef24091594eed0c1fa81e8829fc8`
- implementation: `distributional/iter077h_sm_finite_epsilon_contact_persistence.py`, commit `b42272217c22001cbe6c486767e5f2ad5c21a812`
- workflow/production head: `24cb5abef3bf0f425b9dcba6eca841cbc8182549`
- authoritative run: `34785966710`
- jobs: A `103801388369`, B `103801388153`, C `103801388319`, D `103801388401`, aggregate `103801545934`

Artifacts:

- A `10326796106`, `sha256:e5a8bf9e247f54471e1c8435b7ce8c5775d9f184855197f1143a47aaebf2cee8`
- B `10326064601`, `sha256:4b4a26893658f3b21ec44a14e4746ab8eb77adcbb27541f0a826b0ca3aa70353`
- C `10326571887`, `sha256:76cb6cfe0855b7c90290e801b70caeb8d50522858c786f4958c06a99d6e55ea9`
- D `10326910664`, `sha256:604b25be3257f06c9e294c496214fede8168cd36b9469ae9fa7ca60ea0a62ac4`
- aggregate `10326811897`, `sha256:e8dd522e9b5af081032bb6a4ee14ad6b1116c7fabf43a5f491e3909afdae4175`

All frozen lanes A/B/C/D and aggregate passed.

## Classification

`ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`

## Exact finite-epsilon identity

For the source spectral kernel and `j=1/2`, with

`D=rho^2+1/4`,

exact polynomial division gives

`Theta_(sigma,rho,1/2;epsilon)(x)`

`= [1+(2 i sigma rho epsilon-epsilon^2)/D] theta(sigma x) exp(-epsilon |x|)`

`  + [(epsilon-2 i sigma rho)/D] delta(x)`

`  - [sigma/D] delta'(x)`.

Thus the delta-prime coefficient is independent of finite `epsilon>0` and never vanishes for finite real `rho`. The `epsilon->0+` limit reproduces the corrected Appendix-D contact distribution.

For gamma-simple `rho=gamma/2`,

`A_(sigma,epsilon)=4(epsilon-i sigma gamma)/(1+gamma^2)`,

`C_sigma=-4 sigma/(1+gamma^2)`.

Finite spectral epsilon therefore does not act as a coordinate-space mollifier for the contact derivative.

## Frozen rank-9 sign census

At `gamma=6/5`, `epsilon=1/7`, and frozen self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`,

all `2^10=1024` wedge-sign assignments were checked exactly.

Result:

- `1024/1024` pure-contact Fourier restrictions have exact degree `3` in the self-stress parameter;
- `1024/1024` have nonzero leading coefficient;
- failures: `0`;
- distinct exact leading coefficients in this control: `16`.

Symbolically, for finite real gamma and `epsilon>0`, every finite-epsilon delta coefficient `A_e` and delta-prime coefficient `C_e` is nonzero, so the order-3 pure-contact self-stress coefficient is termwise nonzero for every wedge-sign assignment.

## Scientific consequence

Keeping the published spectral `epsilon` finite does **not** by itself legalize the rank-9 termwise spinor-contact pullback. The contact derivatives remain present before the limit and the frozen rank-9 `n_eff=3` pure-contact obstruction survives termwise.

This does **not** prove nonexistence of the full source-selected causal amplitude and does not prove non-cancellation after summing Heaviside/contact support strata. It rules out only the naive cure `finite epsilon => smoothed local contacts => ordinary termwise K5 pullback`.

The next source-faithful question is therefore an **ordering question**. The primary construction defines Toller matrices themselves as polynomially bounded functions on `SL(2,C)` and supplies closed reduced hypergeometric forms. The next admissible gate should compare the source order

`wedge spectral/spinor integration -> Toller function -> K5 product/group integration`

against the non-admissible termwise multiplication of the ten spinor-contact distributions at the rank-9 source point.

## Claim locks

No full source-selected boundary-value nonexistence theorem; no full causal-vertex finiteness/divergence theorem; no cancellation/non-cancellation theorem after all support strata; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; no new-physics or complete-QG claim.