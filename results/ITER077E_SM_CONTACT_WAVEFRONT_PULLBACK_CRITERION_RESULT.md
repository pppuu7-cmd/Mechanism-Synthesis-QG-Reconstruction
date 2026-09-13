# Iter077E-SM result — generic source pullback is canonical, rank-9 point-contact term requires correlated boundary value

**Date:** 2026-09-14

## Authority

Stable alias: `Iter077E-SM`.

- source/microlocal supplement: `c4e199a0fe6fda5341bdcc7e26478782bf384abd`
- prospective preregistration: `60d3b0daaa013100dc864cf2a23b6582b54810fc`
- implementation: `d4abfebb09ffb8fd64413c369f25287778b5ccd5`
- production/workflow head: `91e38effa5008a831f99a9b6c96c2a01bbb66609`
- authoritative run: `34785411389`
- jobs: A `103799875440`, B `103799875545`, C `103799875630`, D `103799875622`, aggregate `103799899075`

Artifacts:

- A `10326138586`, `sha256:082c083686f08f756f50063c28a747afe2fc4156eab15c98bd16a2003b2800bb`
- B `10325689875`, `sha256:e3a5401480d02a7b84e7d1e3d4db6acb2c6acb404df482dc4532776cf7035c97`
- C `10326675972`, `sha256:a0e03dca2954ae76c4a4e4370b43d97aa41ba606edf70f4e8c1f0f85f3596ccd`
- D `10326357904`, `sha256:fa753a67af147d97f7f66460394419413eeefe3df48e5991e39dc626f04fcde8`
- aggregate `10325904117`, `sha256:97903b8bb26c6781320ceab791a127af873867ad65a149008472fac846d07680`

All four frozen lanes and the aggregate completed successfully.

## Frozen classification

`ITER077E_SM_GENERIC_SUBMERSION_PULLBACK_ALLOWED_RANK9_CONTACT_HORMANDER_CRITERION_COLLIDES_CORRELATED_BOUNDARY_VALUE_REQUIRED_EXACT_SCOPED`

## Exact split

The exact source coherent representation contains, in every wedge,

`theta(kappa B)+kappa delta^(rho,j)(B)`

and `delta^(rho,j)` always contains a nonzero ordinary `-delta(B)` component because `c_0^(rho,j)=1`. Consequently the ten-wedge termwise expansion contains a nonzero pure point-contact monomial

`prod_e delta(B_e)`.

The ten-dimensional point contact has the full nonzero cotangent fibre at `B=0` in its wavefront set.

### Generic rank-10 region

At the frozen `Iter077A-SM` witness the true source Jacobian has rank 10, hence

`ker(J^T)={0}`.

Therefore the true source map is a local submersion and the standard canonical distribution pullback theorem has no nonzero normal covector obstruction there. This is a local/open-region result, not a global K5 theorem.

### Frozen rank-9 exceptional point

At the frozen `Iter077C-SM` witness

`xxxxxyyyzz`,

with

`lambda=(1,-1,0,0,1,0,0,0,0,0)`,

one has exactly

`J^T lambda=0`.

Because the pure ten-contact target summand has every nonzero covector in its wavefront fibre, this same nonzero `lambda` lies in both the target wavefront fibre and the normal set of the source map. Therefore the standard Hörmander wavefront/normal-set disjointness criterion fails for that termwise point-contact summand at the frozen rank-9 point.

## Interpretation

This is **not** a proof that the source-selected causal amplitude does not exist. It is a terminal classification of the ordinary termwise canonical pullback route:

- `GENERIC_SUBMERSION_PULLBACK_AUTHORIZED=true`;
- `RANK9_POINT_CONTACT_STANDARD_PULLBACK_CRITERION_FAILS=true`;
- `FULL_SOURCE_SELECTED_BOUNDARY_VALUE_NONEXISTENT=false`;
- `CORRELATED_SOURCE_SELECTED_EXTENSION_REQUIRED=true`;
- `CORRELATED_K5_BOUNDARY_VALUE_ESTABLISHED=false`.

`Iter077D-SM` independently proves a nondegenerate mixed quadratic normal form at the same rank-9 point. That nonlinear information is now the correct input for a source-selected boundary-value/scaling analysis; it does not retroactively restore the hypotheses of the first-order canonical pullback theorem.

## Next admissible gate

Use the published spectral `i epsilon` selector and the exact `Iter077D-SM` quadratic normal form to classify the local scaling/extension problem on the exceptional stratum. In particular, distinguish the ordinary point-contact channel from higher delta-derivative channels and determine where scaling degree permits a unique extension before any full boundary-contracted K5 verdict is attempted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no claim of full source-amplitude nonexistence; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` and forbid arbitrary finite parts.