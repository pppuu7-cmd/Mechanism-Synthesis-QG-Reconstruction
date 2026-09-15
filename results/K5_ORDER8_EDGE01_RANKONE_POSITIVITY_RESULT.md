# K5 order-8 edge01 rank-one positivity — terminal result

Date: 2026-09-16

## Authority

- workflow: `K5 order8 edge01 rank-one positivity`
- head: `657edbaa32a6cc807d8f3d8248580cfac48eb2f4`
- run: `35027986124`, terminal `success`
- artifact: `10420064433`
- artifact ZIP digest: `sha256:2454accda24a15d08823b934d83f7d4692f7f52ddbaa95e1f56643697e95ddd8`
- production JSON SHA256 (artifact manifest): `2d52d706978f603564f13855b07785e65a88a18802ff47030b25294d07b3af7c`
- classification: `K5_00000_EDGE01_RANKONE_RADIAL_MOMENT_POSITIVE_FOR_ALL_T_GT_0_EXACT_SCOPED`
- gate status: `PASS_EXACT_SCOPED`

The preceding failed attempt was infrastructure-only JSON serialization failure; this repaired run reaches the frozen scientific assertions and uploads the terminal artifact.

## Exact content

The frozen rank-one edge01 family uses all ten authoritative K5 edges and all `1024` source choices. The exact effective covariance is `c=2/5`. The source polynomial has purely real coefficients and factorizes

`F(u)=128/78125 (5-2u)(7u^2+15u+25)`.

The common radial denominator has power 7. After extracting the positive scalar `2688/78125`, the primitive numerator in `t` is

`1910223 - 29283 t + 3816195 t^2 + 6711090 t^3 + 4171545 t^4 + 1168937 t^5 + 126293 t^6`.

Its leading nonzero coefficient is positive; the only negative coefficient is linear. The frozen exact positivity certificate uses a quadratic discriminant

`-29158276351851 < 0`,

and establishes strict positivity for every `t>0`. All interpolation holdouts and all full-general-engine cross-checks are exact. The general-engine values at `t=1,16,1/16` are respectively

- `3075072/390625`,
- `89614359168/45956640625`,
- `138899462352/6103515625`.

Controls reject the malformed linear coefficient, preserve the full source-choice census, and prohibit promotion of a finite/rank-one ray theorem to the full simplex period.

## Scientific scope

This is a strict exact positivity theorem only for the frozen one-dimensional rank-one K5 ray. The full projective angular/simplex problem is nine-dimensional. Therefore this result does **not** prove that the full K5 order-eight principal-symbol period is nonzero and does not assign a K5 zero/nonzero theorem.

It does, however, remove cancellation on this exact source-faithful ray and supplies a constructive positive anchor for the next higher-dimensional Schwinger-family or global SOS/IBP noncancellation analysis.

## Locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical finite-part selector; no K5 full-period verdict; no G3/F9/G8 promotion; no preferred sequential continuation; retain the published spectral `i epsilon`.