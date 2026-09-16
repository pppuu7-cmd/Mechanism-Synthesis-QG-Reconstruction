# K5 Schwinger projective blow-up normal-flux scaling — exact derivation

Controlling prospective preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING.md`, commit `06fc09a0355e6cc15889ac9f244ab03d4cb86569`.

Classification: `K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVED_EXACT_SCOPED`.

## Setup
Let the ten Schwinger coordinates satisfy `sum_e alpha_e=1`. Fix a nonempty proper subset `Z`, `k=|Z|`. Because Z is proper, choose an affine projective chart by eliminating one coordinate `alpha_r` with `r notin Z`. The remaining nine coordinates carry the restriction of `Omega_9` up to a nonzero constant sign, so valuation can be computed with ordinary affine Lebesgue measure.

Set

`t = sum_{e in Z} alpha_e`, `alpha_e=t beta_e` for `e in Z`, `sum_Z beta_e=1`.

Choose one edge `e_k in Z` and use independent angular coordinates `beta_1,...,beta_{k-1}`, with `beta_k=1-sum_{a<k} beta_a`.

## Exact Jacobian
For the k coordinates in Z,

`(alpha_1,...,alpha_k)=(t beta_1,...,t beta_{k-1},t(1-sum_{a<k}beta_a))`.

The determinant of `d(alpha_1,...,alpha_k)/d(t,beta_1,...,beta_{k-1})` has absolute value `t^(k-1)`. This follows by factoring t from the k-1 beta-columns; the remaining determinant is ±1. Hence

`d^k alpha_Z = ± t^(k-1) dt wedge d beta_1 ... wedge d beta_(k-1)`.

All coordinates outside Z are tangential and unscaled. Therefore the scalar projective measure contributes exactly `t^(k-1) dt` times a nonzero angular/tangential form on the relative interior of the blown-up face.

This proves that the geometric scalar-measure exponent is `k-1`, not `k`.

## Normal component of a logarithmic face-tangent field
Let `v_e=alpha_e q_e(alpha)` with every `q_e` polynomial. Since `t=sum_Z alpha_e`,

`v(t)=sum_{e in Z} v_e = sum_{e in Z} alpha_e q_e(alpha) = t * Q_Z(t,beta,alpha_notZ)`,

where `Q_Z=sum_Z beta_e q_e(t beta,alpha_notZ)` is polynomial in t after substitution. Thus

`ord_t v(t) >= 1`.

If the exact leading coefficient of `Q_Z` vanishes, the order is higher; this is precisely why the 34-orbit physical audit must collect the exact leading homogeneous coefficient rather than use a generic sample.

## Boundary flux
Write the projective volume form locally as

`Omega_9 = ± t^(k-1) dt wedge omega_Z`,

where `omega_Z` is the nonzero angular/tangential 8-form at the relative interior. Contracting with v and pulling back to `t=epsilon` kills all terms still containing `dt`; the normal term is

`pullback(i_v Omega_9) = ± t^(k-1) v(t) omega_Z`.

Therefore the normal-flux geometry contributes

`(k-1) + ord_t v(t)`

to the t-valuation. Equivalently, after writing `v(t)=t Q_Z`, it contributes the universal factor `t^k` times `Q_Z`; any additional order comes from exact cancellation in `Q_Z`.

For the physical integrand `prod_e alpha_e^(1/2) N_c / Psi^(21/2)`, the complete flux exponent at a proper Z is therefore

`E_flux = (k-1) + k/2 + ord_Z(N_c * v(t)) - (21/2) ord_Z(Psi)`

when `v(t)` is kept inside the exact flux numerator. If instead the implementation factors `v(t)=t Q_Z`, the equivalent form is

`E_flux = k + k/2 + ord_Z(N_c * Q_Z) - (21/2) ord_Z(Psi)`.

These are bookkeeping identities only; they do not assume that the leading coefficient of `N_c Q_Z` is nonzero.

## Frozen checks
- `k=1`: alpha_e=t, so `d alpha_e=dt`; scalar Jacobian exponent is 0=`k-1`. The pulled-back flux is `v_e=t q_e`, giving universal normal factor t, exactly as above.
- Different eliminated projective coordinate: any choice `r notin Z` changes the affine restriction of `Omega_9` only by a nonzero smooth chart Jacobian on overlap. Such a unit has t-valuation zero, so the derived exponent is unchanged.
- `Z=empty`: there is no normal blow-up variable and no boundary statement.
- `Z=E(K5)`: no coordinate outside Z exists to define this as a boundary face of `sum alpha=1`; common scaling is the removed radial direction. It is therefore a homogeneity control only.
- Malformed scalar exponent `k` fails the explicit k=1 chart, where the scalar measure is exactly `dt`, not `t dt`.

## Scope
This closes only the projective geometry/Jacobian ambiguity identified by the pre-implementation Critic. The 34-orbit production still must determine exact `ord_Z N_1`, `ord_Z N_2`, and exact normal-flux leading coefficients with physical dual transport. No integrated Stokes relation is authorized here.
