# Iter029 — exact microlocal cycle / wavefront audit

Date: 2026-09-12

## Purpose

Iter028 found Gaussian-mollifier divergence exponents matching complete-graph cycle nullity. Iter029 asks whether this was regulator-specific or reflects an exact conormal dependence of the simultaneous boundary hypersurfaces.

Linearized common-spectral boundary forms are represented by

`ell_ij(x) = x_i - x_j`

after quotienting the global translation mode. Their conormals are rows of the reduced oriented incidence matrix `B`.

For a naive product of delta-like boundary factors, a nonzero vector `c` with

`B^T c = 0`

is an exact conormal dependence and blocks the standard transverse/Hormander product criterion.

## GitHub runs

### Iter029A — Microlocal Cycle Wavefront Audit

Run `34671531875`, commit `8a10e81de137350d55d92f6fddc37d0724a6a92e`.

Seven independent lanes, all SUCCESS:

- K3 complete;
- K4 complete;
- K5 complete;
- K3 spanning-tree control;
- K4 spanning-tree control;
- K5 spanning-tree control;
- all 16 source-induced K5 causal sign sectors `kappa_ij=sigma_i sigma_j` (global flip quotiented).

Exact complete-graph results:

- K3: rank 2, left-nullity / cycle nullity 1;
- K4: rank 3, left-nullity / cycle nullity 3;
- K5: rank 4, left-nullity / cycle nullity 6.

All spanning-tree controls have left-nullity 0 and satisfy the transverse criterion.

For K5, every one of the 16 source-induced causal sign sectors has rank 4 and left-nullity 6. Row sign changes therefore do not remove the microlocal obstruction.

### Iter029B — Cycle-Breaking Forest Audit

Run `34671550029`, commit `314b594543e1e068fccbbaf558e7e058f4950f38`.

Three independent lanes K3/K4/K5, all SUCCESS.

For K5:

- complete edges: 10;
- maximum transverse subset: 4 edges;
- minimum removals required for a transverse subset: 6;
- exact spanning-tree count: 125, matching Cayley `5^(5-2)=125`;
- no transverse subsets exist with 5 or more edges.

Thus the exact number of redundant constraints is 6, matching both the K5 cycle nullity and the Iter028 fitted mollifier divergence exponent `~ eta^-6.000905`.

## Scientific classification

`EXACT_CYCLE_CONORMAL_DEPENDENCE_BLOCKS_STANDARD_NAIVE_MULTIWEDGE_DELTA_PRODUCT_ON_COMPLETE_GRAPH_COLLISIONS__OBSTRUCTION_DIMENSION_EQUALS_GRAPH_CYCLE_NULLITY_AND_SURVIVES_ALL_SOURCE_INDUCED_K5_CAUSAL_SIGN_SECTORS__SPANNING_TREE_CONTROLS_ARE_TRANSVERSE__CORRELATED_SOURCE_BACKED_IEPSILON_OR_RENORMALIZED_EXTENSION_STILL_OPEN`

## Meaning

This upgrades Iter028 from a regulator-dependent warning to an exact structural statement about the tested linearized boundary hypersurface geometry. The naive product cannot be justified by the standard transverse/Hormander criterion on cyclic complete-graph collisions.

It does **not** prove that the physical causal EPRL/Toller vertex is divergent or undefined. The remaining legitimate escape routes are narrower and more specific:

1. a source-backed correlated spectral `i epsilon` prescription that defines the full multi-wedge object before taking boundary values;
2. a renormalized distributional extension with physically fixed finite parts;
3. cancellations produced by the complete matrix/intertwiner contraction before multiplication is interpreted termwise;
4. a different source-defined representation of the same amplitude whose wavefront set is compatible.

Choosing a spanning tree is only a diagnostic of redundancy and is not a physical prescription for deleting wedge factors.
