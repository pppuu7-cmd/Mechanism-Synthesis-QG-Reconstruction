# K5 order-8 edge-01 rank-one positivity derivation

Date: 2026-09-15

Parent frozen K5 scientific contract: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`, commit `7466325187f22043d1794379fd6e6dcf62e05abd`.
Parent nonuniform diagnostic prereg: `prereg/K5_ORDER8_NONUNIFORM_SCHWINGER_SIGN_DIAGNOSTIC.md`, commit `18900e175ae1934eb770730f3e89e14eb577aad7`.

Status: POST-PREREG EXACT DERIVATION. This result strengthens the surviving sign route on one analytic Schwinger ray. It does **not** assign the frozen K5 residue zero/nonzero verdict.

## 1. Rank-one Schwinger family

Use the authoritative K5 edge order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`

and set

`alpha_01=t`, all other `alpha_e=1`, with `t>0`.

Let `L0=L(1,...,1)` be the reduced uniform K5 Laplacian in the four-coordinate translation gauge. Its edge-01 effective covariance is

`c = r_01^T L0^(-1) r_01 = 2/5`.

Introduce the radial-probe deformation parameter by

`a=1+s/5`,

so the exact quadratic form is

`L(t,s)=a L0 + (t-1) r_01 r_01^T`.

Sherman-Morrison gives

`L(t,s)^(-1)=a^(-1)[L0^(-1)-u L0^(-1) r_01 r_01^T L0^(-1)]`,

with

`u=(t-1)/(a+(2/5)(t-1))`.

The determinant is

`det L(t,s)=125 a^3 [a+(2/5)(t-1)]`.

These identities are exact.

## 2. Full source contraction polynomial

For the fixed stripped boundary component `k=(0,0,0,0,0)`, retain all `4^5=1024` node-tensor choice terms from the authoritative source module and all Wick pairings. Because the numerator has degree ten, the Gaussian moment is homogeneous degree five in the edge covariance. The rank-one covariance update therefore gives

`W(t,s)=a^(-5) F(u)`

for a polynomial `F` of degree at most five.

Exact full-source contraction yields

`F(u)=128/625 + (128/3125)u + (128/15625)u^2 - (1792/78125)u^3`,

with the degree-four and degree-five coefficients exactly zero. Equivalently,

`F(u)=(128/78125)(125+25u+5u^2-14u^3)`

and the cubic factors exactly as

`F(u)=(128/78125)(5-2u)(7u^2+15u+25)`.

At `s=0`,

`u=5(t-1)/(2t+3)`.

For `t>0`, this lies strictly in `(-5/3,5/2)`. Hence `5-2u>0`. The quadratic factor is strictly positive for all real `u` because its discriminant is

`15^2-4*7*25 = -475 < 0`.

Therefore the base Gaussian leading-numerator moment is strictly positive for every finite `t>0` on this ray.

## 3. Exact order-eight radial-probe moment

The zero-equivalent unnormalized Gaussian function used by the frozen diagnostic is

`J(s)= [det L(t,s)/det L(t,0)]^(-3/2) W(t,s)`.

The fourth derivative at zero is a positive common multiple of the actual insertion `(R_K5^2)^4`; under the frozen normalization it is exactly

`R(t)=2688 P(t) / [78125 (2t+3)^7]`,

where

`P(t)=126293 t^6 + 1168937 t^5 + 4171545 t^4 + 6711090 t^3 + 3816195 t^2 - 29283 t + 1910223`.

This reproduces, as exact special cases,

- `t=1`: `3075072/390625`;
- `t=16`: `89614359168/45956640625`;
- `t=1/16`: `138899462352/6103515625`.

## 4. Positivity certificate for all t>0

All coefficients of `P(t)` are positive except the linear coefficient. Isolate

`3816195 t^2 - 29283 t + 1910223`.

Its exact discriminant is

`(-29283)^2 - 4*3816195*1910223 = -29158276351851 < 0`.

Since its leading coefficient is positive, this quadratic is strictly positive for every real `t`. Every remaining term in `P(t)` is nonnegative for `t>0`, with strictly positive constant/high-order contributions. Therefore

`P(t)>0` for every `t>0`,

and since `2t+3>0`,

`R(t)>0` for every `t>0`.

Thus the actual order-eight radial-probe projective integrand for boundary component `00000` is strictly positive on the complete one-edge rank-one Schwinger ray `alpha_01=t>0`, all other edge weights one.

## 5. Interpretation ceiling

This is a continuum exact ray theorem, not a full positive-cone theorem. The ray has measure zero inside the 9-dimensional projective simplex, and positivity on this ray does not by itself exclude cancellations elsewhere in the simplex. Therefore this result does **not** prove the projective period nonzero and does not assign the K5 residue verdict.

Authorized next work is to generalize the rank-one/Sherman-Morrison structure to larger positive-dimensional Schwinger families, or derive a global factorization/SOS/IBP certificate for the invariant-dual projective integrand.

No finite part, selector, regulator-independence theorem, physical amplitude, F9/G3 promotion, new physics, or complete-QG claim follows.
