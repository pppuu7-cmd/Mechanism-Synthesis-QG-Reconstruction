# K5 order-8 Schwinger/projective reduction — production result

Date: 2026-09-15
Status: **REDUCTION_VALIDATED_EXACT**

This is a computational lemma under the prospectively frozen scientific gate
`prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`
(commit `7466325187f22043d1794379fd6e6dcf62e05abd`).

It assigns **no** K5 zero/nonzero scientific verdict.

## Provenance

- derivation: `sources/K5_ORDER8_SCHWINGER_PROJECTIVE_REDUCTION.md`, commit `bd7b558922db549784e46c141fac03fb75822f2f`;
- exact validator: `scripts/k5_order8_schwinger_projective_reduction.py`, commit `3f43dec3eedaf9861aaef3e89ad7d3b7d032ba5b`;
- workflow/head: `.github/workflows/k5_order8_schwinger_projective_reduction.yml`, commit `e0141f2c2f8cc824c5ccbf0b382b8444b55702be`;
- production run: `35016573070`, terminal `success`;
- job: `104541421510`, terminal `success`;
- artifact: `10415553863`, `k5-order8-schwinger-projective-reduction`;
- artifact ZIP digest: `sha256:74d5d63b02f3189ed4c00493ee586fc03078115b8136d7efc61a4a844a161489`;
- production JSON SHA256: `e2a30c07dc3239a70f5c3d9baef6e2612aac71890f2e815575f585f010a49871`.

## Exact production checks

Production independently constructs the gauge-fixed 4x4 weighted reduced Laplacian of K5 from the ten incidence rows and expands its determinant as a sparse polynomial.

It independently enumerates all four-edge subsets of K5 and identifies the connected spanning trees.

Exact output:

- K5 edges: `10`;
- reduced Laplacian dimension: `4`;
- determinant monomials: `125`;
- independently enumerated spanning trees: `125`;
- determinant support equals spanning-tree support: `true`;
- every determinant coefficient equals `+1`;
- Kirchhoff degree: `4`;
- all `120` S5 vertex relabelings preserve the tree support;
- S5 covariance failures: `0`.

Thus the determinant is exactly the K5 Kirchhoff polynomial

`Psi_K5(alpha)=det L(alpha)`

with the 125 Cayley-tree monomials.

## Gaussian/Wick reduction

For an exact invariant-dual leading numerator `N_10` and any order-eight homogeneous normal probe `P_8`, the Gaussian numerator degree is

`10+8=18`.

Therefore the Gaussian heat/Wick operator contributes only at exact contraction order

`18/2 = 9`.

Production verifies `wick_order=9`.

## Common-scale pole

Under `alpha_e=t u_e`, `sum u_e=1`, the exact powers are

- ten edge factors `prod alpha_e^(1/2)`: `t^5`;
- ten-parameter radial Jacobian: `t^9`;
- `det L(tu)^(-3/2)`: `t^-6`;
- ninth Wick contraction: `t^-9`.

Hence

`5+9-6-9=-1`.

Production verifies the common-scale exponent exactly as `-1`.

The logarithmic K5 scale is therefore isolated as `dt/t`, leaving a nine-dimensional projective simplex period in the Schwinger ratios `u_e`.

## Controls

The same validator rejects all frozen malformed reduction lanes used here:

- omitted K5 edge;
- wrong edge denominator exponent;
- lower-order probe;
- wrong Wick order;
- wrong Kirchhoff degree;
- fake tree count;
- determinant/tree mismatch;
- broken S5 tree covariance;
- promotion of the common Schwinger scale to a one-parameter **physical** regulator;
- assignment of a K5 zero/nonzero verdict from the reduction alone.

No rejection is assigned by a literal predeclared boolean; each mutation re-enters the same validation path.

## Scientific consequence

The unresolved actual K5 order-eight angular/Mellin calculation is reduced exactly from a 12-dimensional homogeneous normal integral to a projective K5 graph period whose scalar geometry is controlled by the 125-term Kirchhoff polynomial and whose numerator is a finite ninth Wick contraction of the exact degree-18 source numerator/probe polynomial.

The next object is

`PROJECTIVE_K5_ORDER8_INVARIANT_DUAL_PERIODS`.

The first admissible nonzero-witness lane is the two-dimensional S5-invariant **dual** boundary sector, retaining the full source construction and the correct covector action.

## Interpretation ceiling

No K5 zero/nonzero theorem yet; no finite-part selector; no unique K5 extension; no one-parameter physical regulator; no regulator-independence theorem; no global patching; no F9/G3 promotion; no new physics or complete-QG claim.
