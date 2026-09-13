# Iter078J-RG result — the unique linearized null direction is measure-dependent and lifted at quadratic order

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078J_RG_LINEARIZED_NULL_DIRECTION_CLASSIFICATION.md`, commit `0c2a0173f7d33ba55ac577b13bde7cb890b102dd`.
- Implementation: `distributional/iter078j_rg_null_direction_classification.py`, commit `1944d39d0cee0f6ca2f11edf3beedfe96d236a33`.
- Workflow/production head: `.github/workflows/iter078j_rg_null_direction_classification.yml`, commit `410210a98f2e58572c4647906823c4f0e9fd8927`.
- Authoritative run: `34790878791`.
- Lane A artifact `10328720834`, digest `sha256:7fb1e907fdab8c77a7f618b6c80757f01f62be503a939c10dd1d104a5fa0a961`.
- Lane B artifact `10327821952`, digest `sha256:2cca6843942a27b5c9177ff2480a727dc415aa5e0dde2b9f52ffd5577c104aca`.
- Lane C artifact `10327697096`, digest `sha256:4a8b391a1272667d73974762dcceeeaee79b80f3d489eb6bdb37b16829259b43`.
- Lane D artifact `10328156312`, digest `sha256:e4867bc5450079443a9be93226f5ace5e20bf9be97c829d2d5318306a2a092bd`.
- Aggregate artifact `10327733172`, digest `sha256:baccd759dd966051e00fb1054d268e5b20f9dbe39e86882fae303d6d0011b9af`.

## Classification

`ITER078J_RG_UNIQUE_LINEARIZED_NULL_IS_NONLINEARLY_LIFTED_AT_ORDER_2_EXACT_CONTROL_SCOPED`

Scientific verdict: **CONTROL_RESULT / NONLINEARLY_LIFTED**.

## Exact null vectors

The Iter078H rank/nullity result is reproduced exactly for both measures:

- rank `31`;
- nullity `1`;
- exact primitive integer right-null vectors verified.

EPRL-edge-weight null vector:

`(3,-3,-3,-9,0,2,-10,0,-6,0,-12,2,-1,1,1,3,-6,6,6,2,-3,1,1,-11,-3,1,1,-11,0,-8,-8,0)`.

Unit-edge-weight control null vector:

`(1,-1,-1,-3,0,0,-4,0,-2,0,-4,2,-1,1,1,3,-2,2,2,2,-1,1,1,-5,-1,1,1,-5,0,-2,-2,0)`.

They are **different and not proportional**. Therefore equality of the coarse rank/nullity diagnostics in Iter078H did not imply equality of the null geometry.

## Frozen discrete-candidate census

Neither null vector is proportional to any preregistered obvious candidate:

- compact tensor `L`;
- constant vector;
- compact-support or zero-support indicator;
- signed compact support;
- any of all `32` Walsh-Hadamard characters `(-1)^(s dot k)`.

Thus no simple parity/relabeling/normalization interpretation is supported by this exact catalogue.

## Exact nonlinear line test

For each measure the exact degree-5 polynomial

`R(L+t n)-R(L) = sum_(m=1)^5 t^m V_m`

was reconstructed from exact arithmetic and checked against direct evaluations.

### EPRL-edge-weight measure

- `V_1 = 0` exactly, as required by the Jacobian null relation;
- first nonzero order: `m=2`;
- nonzero component counts:
  - order 2: `32/32`;
  - order 3: `32/32`;
  - order 4: `32/32`;
  - order 5: `32/32`;
- exact coefficient-vector digest: `a9c955caaa6853262550d04f498a0c72063ac1ae078da6b71651a418b304c8cd`.

### Unit-edge-weight control

- `V_1 = 0` exactly;
- first nonzero order: `m=2`;
- nonzero component counts:
  - order 2: `32/32`;
  - order 3: `31/32`;
  - order 4: `32/32`;
  - order 5: `28/32`;
- exact coefficient-vector digest: `fce2baef892df9d33df3892108bffb58438b3bd307064875963aeb208032f636`.

## New scientific fact

The unique first-order null direction of the fixed-spin 1-to-5 control map is **not an exact flat direction**. The refinement becomes sensitive to it immediately at quadratic order, and under the EPRL convolution control that quadratic response reaches all 32 output components.

Therefore the rank-31 Jacobian at `L` should not be interpreted as a missing/gauge coupling direction. It is a local singularity of the nonlinear degree-5 map whose degeneracy is lifted beyond first order.

The fact that the primitive null vectors differ between the EPRL and unit-edge measures also provides a sharper form of measure sensitivity than the coarse Iter078H summary flag: the two maps have the same rank/nullity at `L` but different first-order kernels and different higher-order coefficient patterns.

## Interpretation ceiling

This remains a fixed all-`j=1/2`, pure order-zero tensor-network control. It does not prove that the physical causal-Toller refinement selector is locally injective, because the physical map still lacks the selected reference extension, higher spins, causal-orientation sum, full supported jets and regulator/closure proof.

No RG fixed point, beta function, regulator independence, unique K5 extension, G3, continuum or complete-QG claim follows.

## Exact next admissible step

The exact control now supports moving away from local differential rank tests. The next high-information RG task is to test **finite global closure / fixed-point structure in the full 32-dimensional fixed-spin order-zero control map**, prospectively and without assuming the BF tensor is special:

1. solve or bound projective fixed rays `R(C)=lambda C` under the EPRL-weighted map;
2. include the trivial zero solution separately and impose a frozen normalization to remove overall degree-5 scaling;
3. search for exact symmetry-reduced branches only if the reduction is frozen before solving;
4. use independent numerical algebra only as a candidate generator, followed by exact substitution certificates;
5. keep this as a control for theory-space geometry, not as the physical CRQN RG fixed-point problem.