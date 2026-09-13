# Iter077E-SM preregistration — generic submersion vs exceptional contact pullback

**Date:** 2026-09-14

## Purpose

The source-map line now has:

- `Iter077A-SM`: an open generic rank-10 submersion region;
- `Iter077C-SM`: a frozen rank-9 exceptional point with nonzero self-stress `lambda`;
- `Iter077D-SM`: an exact nondegenerate mixed quadratic normal form at that point.

This gate asks whether the **standard canonical Hörmander pullback theorem** is sufficient for the exact source contact decomposition in both regions.

The gate deliberately distinguishes failure of the standard criterion from nonexistence of a source-selected boundary value.

## Frozen input

Use:

- `sources/CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_PULLBACK_MICROLOCAL_SUPPLEMENT.md`;
- `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`;
- `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`;
- `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`.

Frozen exceptional witness:

`xxxxxyyyzz`

with edge order

`01,02,03,04,12,13,14,23,24,34`

and

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

No witness reselection is allowed after execution.

## Lane A — source/provenance lock

PASS iff all of the following are present in frozen source/result files:

1. exact source wedge factor `theta(kappa B)+kappa delta^(rho,j)(B)`;
2. finite delta-derivative expansion of `delta^(rho,j)`;
3. exact `c_0^(rho,j)=1` and hence nonzero `-delta` component;
4. nonzero pure ten-contact monomial `prod_e delta(B_e)` in the termwise source decomposition;
5. `Iter077A-SM`, `Iter077C-SM`, `Iter077D-SM` PASS classifications;
6. no claim of full-amplitude nonexistence/finiteness/divergence.

## Lane B — exact point-contact Fourier/wavefront control

For a formal finite point-supported distribution

`u(x)=sum_{n=0}^N a_n delta^(n)(x)`

with `a_0=-1`, use the Fourier polynomial

`P(xi)=sum_n a_n (i xi)^n`.

PASS iff:

1. `P` cannot be identically zero because its constant coefficient is `-1`;
2. for `xi -> +infinity` and `xi -> -infinity`, a nonzero polynomial is not rapidly decreasing;
3. the ten-dimensional pure point monomial has Fourier transform equal to a nonzero constant and therefore the full nonzero cotangent fibre at the origin is wavefront-active;
4. this lane records only the point-contact summand, not the full combined `i epsilon` boundary value.

## Lane C — generic rank-10 submersion pullback

Reconstruct the frozen exact rank-10 true source Jacobian witness from `Iter077A-SM`.

PASS iff:

1. `rank(J)=10`;
2. `ker(J^T)={0}` exactly;
3. therefore the normal set of the true source map contains no nonzero target covector at this point;
4. standard local pullback of arbitrary target distributions is authorized there by the submersion theorem;
5. the aggregate records this only as a local/open-region result, not a global K5 theorem.

## Lane D — frozen rank-9 contact collision and scope firewall

Reconstruct the frozen rank-9 source Jacobian and `lambda`.

PASS iff:

1. `rank(J)=9`;
2. `lambda != 0` and `J^T lambda=0` exactly;
3. the ten-dimensional point-contact target summand has `lambda` in its wavefront fibre at `B=0`;
4. therefore the standard Hörmander wavefront/normal-set disjointness condition fails for that summand at this frozen point;
5. `Iter077D-SM` remains a nondegenerate nonlinear-normal-form input but is **not** reinterpreted as restoring the first-order pullback hypothesis;
6. the aggregate records all of:
   - `GENERIC_SUBMERSION_PULLBACK_AUTHORIZED=true`;
   - `RANK9_POINT_CONTACT_STANDARD_PULLBACK_CRITERION_FAILS=true`;
   - `FULL_SOURCE_SELECTED_BOUNDARY_VALUE_NONEXISTENT=false`;
   - `CORRELATED_SOURCE_SELECTED_EXTENSION_REQUIRED=true`;
   - `CORRELATED_K5_BOUNDARY_VALUE_ESTABLISHED=false`;
   - `PHYSICAL_SOURCE_TO_K4_PUSHFORWARD=false`;
   - `EPSILON_MINUS1_COEFFICIENT=false`;
   - no causal-vertex finiteness/divergence theorem or G3/F9/G8/K5 promotion.

## PASS classification

`ITER077E_SM_GENERIC_SUBMERSION_PULLBACK_ALLOWED_RANK9_CONTACT_HORMANDER_CRITERION_COLLIDES_CORRELATED_BOUNDARY_VALUE_REQUIRED_EXACT_SCOPED`

## FAIL classification

`ITER077E_SM_CONTACT_PULLBACK_SPLIT_PREDICTION_FAILS_EXACT_SCOPED`

## Next admissible gate on PASS

The ordinary termwise Hörmander route is terminally classified: PASS on the generic rank-10 region, not authorized on the frozen rank-9 contact point. The next source-map task is no longer another first-order rank test.

Instead, use the **published source-selected spectral `i epsilon` boundary value** together with the exact `Iter077D-SM` quadratic normal form to test whether the correlated rank-9 local distribution has a unique source-defined extension/scaling limit. This must keep distinct:

- existence of the source-selected boundary value;
- uniqueness/extension freedom;
- absolute integrability;
- conditional/distributional existence;
- regulator removal;
- full boundary contraction.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no claim that the full source-selected causal vertex fails to exist; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` and forbid arbitrary finite parts.