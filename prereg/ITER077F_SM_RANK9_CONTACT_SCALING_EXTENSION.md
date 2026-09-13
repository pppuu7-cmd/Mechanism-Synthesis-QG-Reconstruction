# Iter077F-SM preregistration — rank-9 contact scaling and extension threshold

**Date:** 2026-09-14

## Purpose

`Iter077E-SM` terminally classifies the ordinary termwise Hörmander route: generic rank-10 source points are local submersions, while the frozen rank-9 pure point-contact summand violates the standard wavefront/normal-set disjointness criterion.

`Iter077D-SM` supplies a nondegenerate six-dimensional quadratic normal form at that rank-9 point.

This gate asks the next sharply defined question:

> Which source contact derivative orders have a unique local extension across the quadratic critical origin by scaling degree alone, and does the exact all-`j=1/2`, gamma-simple ten-wedge source contact product reach a nonunique excess derivative order along the frozen self-stress direction?

This is still pre-contraction/source-local analysis. It does not classify the full vertex as finite or divergent.

## Frozen inputs

Use:

- `sources/CAUSAL_SPINFOAM_VERTEX_2026_RANK9_CONTACT_SCALING_SUPPLEMENT.md`;
- `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`;
- `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`;
- `results/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION_RESULT.md`.

Frozen self-stress:

`lambda=(1,-1,0,0,1,0,0,0,0,0)`

in edge order

`01,02,03,04,12,13,14,23,24,34`.

Assume the first complete control sector is gamma-simple with `j_e=1/2`, `rho_e=gamma/2` on all ten wedges and finite real `gamma != 0`. No numerical value of `gamma` is fitted.

## Lane A — exact j=1/2 contact coefficient

PASS iff exact symbolic algebra verifies from the frozen gamma-ratio recurrence that:

1. `c_0=1`;
2. `c_1=2 rho/(rho^2+1/4)` for `j=1/2`;
3. `delta^(rho,1/2)=-delta+[rho/(rho^2+1/4)]delta'`;
4. after `rho=gamma/2`, the delta-prime coefficient is `a_gamma=2 gamma/(1+gamma^2)`;
5. `a_gamma` is nonzero for finite real `gamma != 0`.

## Lane B — highest excess derivative on the frozen self-stress

Let target coordinate `s=lambda.B` and complete it by nine regular target coordinates.

PASS iff exact symbolic/combinatorial expansion verifies:

1. only edges `01`, `02`, `12` have nonzero `lambda_e`;
2. with one possible delta-prime per all-spin-half wedge, the maximum pure `partial_s` order is exactly `3`;
3. the unique order-3 contribution chooses delta-prime on `01,02,12` and ordinary delta on the other seven edges;
4. its coefficient is proportional to
   `lambda_01 lambda_02 lambda_12 a_gamma^3 = -(2 gamma/(1+gamma^2))^3`;
5. this coefficient is not identically zero and is nonzero for finite real `gamma != 0`;
6. no wedge with `lambda_e=0` can contribute to `partial_s`, so there is no second order-3 all-spin-half target term that can cancel it before full smooth/boundary contraction.

## Lane C — exact six-dimensional scaling-degree threshold

For nondegenerate quadratic `q` in six transverse dimensions, use

`delta^(n)(q(t x))=t^[-2(n+1)] delta^(n)(q(x))`.

PASS iff the frozen table is recovered exactly:

- `n=0`: scaling degree `2`, unique extension by scaling degree (`2<6`);
- `n=1`: scaling degree `4`, unique extension by scaling degree (`4<6`);
- `n=2`: scaling degree `6`, marginal/nonunique by scaling alone;
- `n=3`: scaling degree `8`, nonunique by scaling alone, ambiguity supported at the critical origin through total derivative order at most `2` before extra symmetries/prescriptions.

The lane must distinguish unique **distributional extension** from ordinary absolute integrability/measure interpretation.

## Lane D — scoped synthesis and firewall

PASS iff the aggregate records:

- `PURE_DELTA_EXCESS_N0_UNIQUE_EXTENSION=true`;
- `EXCESS_N1_UNIQUE_DISTRIBUTIONAL_EXTENSION=true`;
- `FIRST_SCALING_AMBIGUITY_AT_N2=true`;
- `ALL_SPIN_HALF_HIGHEST_EXCESS_ORDER_N3_NONZERO_FOR_GAMMA_NE_0=true`;
- `N3_SCALING_DEGREE=8`;
- `TRANSVERSE_DIMENSION=6`;
- `SCALING_ALONE_SELECTS_N3_EXTENSION=false`;
- `SOURCE_SELECTED_I_EPSILON_EXTENSION_ESTABLISHED=false`;
- `FULL_BOUNDARY_CONTRACTION_CANCELLATION_TESTED=false`;
- no vertex finiteness/divergence, regulator independence, physical source-to-K4 pushforward, nominal `epsilon^-1`, or G3/F9/G8/K5 promotion.

## PASS classification

`ITER077F_SM_ALL_SPIN_HALF_RANK9_CONTACT_REACHES_N3_SCALING_NONUNIQUENESS_SOURCE_I_EPSILON_EXTENSION_REQUIRED_EXACT_SCOPED`

## FAIL classification

`ITER077F_SM_RANK9_CONTACT_SCALING_PREDICTION_FAILS_EXACT_SCOPED`

## Next admissible gate on PASS

The local missing object is frozen as

`SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL`.

The next gate must derive this object from the published spectral `i epsilon` prescription, then insert the exact smooth Toller phases, CP1 measure and boundary intertwiners and test whether the order-3 excess channel survives, cancels, or is uniquely fixed after the **full correlated source contraction**.

Arbitrary counterterms or fitted finite parts are forbidden.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no causal-vertex finiteness/divergence theorem; no assertion that source-selected `i epsilon` is nonunique; no arbitrary counterterm; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion.