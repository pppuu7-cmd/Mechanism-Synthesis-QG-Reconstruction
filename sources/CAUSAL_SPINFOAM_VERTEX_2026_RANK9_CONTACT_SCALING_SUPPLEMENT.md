# Source/derived supplement — rank-9 contact derivative order and quadratic scaling

**Date:** 2026-09-14

## Scope

This supplement combines four already frozen ingredients:

1. the exact causal-vertex contact distribution `delta^(rho,j)`;
2. the `Iter077C-SM` self-stress covector at the first rank-9 source witness;
3. the `Iter077D-SM` nondegenerate six-dimensional quadratic normal form;
4. the all-`j=1/2`, gamma-simple source sector proposed as the first complete boundary-contracted control.

It determines a **local scaling/extension threshold**. It does not define the final correlated `i epsilon` extension and does not prove vertex finiteness or divergence.

## Exact j=1/2 contact coefficients

The source distribution is

`delta^(rho,j)(x) = sum_{n=0}^{2j} [c_n^(rho,j)/(n+1)!] (-1)^(n+1) delta^(n)(x)`,

with

`c_n^(rho,j) = [d^n/d(rho_tilde)^n R_j(rho_tilde;rho)]_(rho_tilde=rho)`,

`R_j = Gamma(-j-i rho) Gamma(j-i rho_tilde+1) / [Gamma(-j-i rho_tilde) Gamma(j-i rho+1)]`.

For every `j`, `c_0=1`.

For `j=1/2`, set

`z=-1/2-i rho`.

Using `psi(z+2)=psi(z)+1/z+1/(z+1)`,

`c_1 = i[psi(z)-psi(z+2)]`

`= 2 rho/(rho^2+1/4)`.

Therefore

`delta^(rho,1/2)(x) = -delta(x) + [rho/(rho^2+1/4)] delta'(x)`.

In the gamma-simple sector `rho=gamma/2`,

`a_gamma := rho/(rho^2+1/4) = 2 gamma/(1+gamma^2)`.

Hence `a_gamma != 0` for every finite real `gamma != 0`.

## Frozen self-stress support

At the frozen rank-9 witness from `Iter077C-SM`, in edge order

`01,02,03,04,12,13,14,23,24,34`,

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

Define a target coordinate `s=lambda.B`; complete it with nine regular linear target coordinates `u_1,...,u_9`.

Then by the chain rule

`partial/partial B_e = lambda_e partial/partial s + (regular derivatives)`.

Only edges `01`, `02`, `12` can contribute an `s` derivative.

In the product of ten all-spin-half contact distributions

`prod_e delta^(gamma/2,1/2)(B_e)`,

the unique way to produce the highest pure excess derivative `partial_s^3` is to choose the `delta'` term on all three self-stress-support edges and the ordinary `delta` term on the other seven edges.

Its coefficient is proportional to

`(lambda_01 lambda_02 lambda_12) (a_gamma)^3`

`= -(2 gamma/(1+gamma^2))^3`,

up to the nonzero product of causal signs `prod_e kappa_e` and the invertible linear target-coordinate Jacobian convention.

For finite real `gamma != 0`, this coefficient is nonzero. No edge outside the self-stress support can contribute to `partial_s`, so there is no second all-spin-half term of the same highest excess order that can cancel it at the target-distribution level.

This is a statement before full smooth phase/intertwiner/spinor contraction; a later full-amplitude cancellation remains logically possible and must be tested rather than assumed.

## Quadratic critical pullback scaling

`Iter077D-SM` gives a nondegenerate quadratic normal form `q` on a six-dimensional transverse slice with inertia `(3+,3-)`.

Away from the critical origin, `q` is a submersion on its null cone. For the one-dimensional contact derivative,

`delta^(n)(q(t x)) = t^[-2(n+1)] delta^(n)(q(x))`.

Therefore on the punctured six-dimensional transverse space,

`sd[delta^(n)(q)] = 2(n+1)`.

The standard scaling-degree extension theorem gives:

- `n=0`: scaling degree `2 < 6`; unique extension across the origin; this is the ordinary point-contact channel;
- `n=1`: scaling degree `4 < 6`; unique distributional extension;
- `n=2`: scaling degree `6 = 6`; first marginal extension ambiguity;
- `n=3`: scaling degree `8 > 6`; nonunique extension by scaling alone, with local counterterm freedom supported at the critical origin up to total derivative order `2` before imposing further source symmetries/prescriptions.

Thus the exact all-spin-half highest self-stress contact channel reaches `n_eff=3`, beyond the unique-extension threshold.

## Scientific interpretation

The failure of the first-order Hörmander criterion in `Iter077E-SM` is not, by itself, fatal: the ordinary `delta(q)` channel has a unique local extension because the exact quadratic critical set lives in six transverse dimensions.

However, the exact all-spin-half source contact distribution contains a nonzero highest excess channel of order `delta'''(q)` for `gamma != 0`. Scaling degree alone does **not** select a unique extension of that channel.

Therefore the remaining local K5 question is no longer an unspecified “distributional problem”. It is the concrete object:

`SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL`

including its contraction with the exact smooth Toller phases, CP1 measures, boundary intertwiners and the other nine regular target directions.

A source-selected spectral `i epsilon` boundary value may fix the extension. An arbitrary fitted finite part or counterterm is forbidden.

## Claim locks

No assertion that the full causal vertex diverges; no assertion that the source-selected `i epsilon` extension is nonunique; no arbitrary counterterm; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; no new-physics or complete-QG claim.