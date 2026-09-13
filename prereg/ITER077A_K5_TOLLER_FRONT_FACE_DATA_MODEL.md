# Iter077A preregistration — covariant K5 Toller front-face data model

**Date:** 2026-09-14

## Purpose

Iter076Z shows that a scalar radial strip leaves a genuinely direction-dependent matrix/bundle-valued front face. This gate asks the next object-definition question:

> Do the minimal front-face data `(radial weight, normal direction, leading C_n matrix, first angular connection)` form a covariantly closed algebraic data type on the gauge-fixed K5 source relative-coordinate complex under incidence, root change, node relabeling, and compact source-node gauge action?

This is not a correlated analytic boundary-value theorem.

## Frozen input

Use `sources/ITER077_PARALLEL_FRONTIER_SOURCE_DERIVATION.md` and authoritative Iter076W-X-Y-Z results.

## Lane A — provenance and scope

PASS iff the frozen source note and authoritative result files establish all of:

- Iter076W compact common-node gauge closure;
- Iter076X nontrivial normal-direction connection;
- Iter076Y a concrete mixed source path entering that connection;
- Iter076Z generic scalar-flattening obstruction;
- the typed wedge datum `FF_e=(w_e,n_e,C_e,A_e)`;
- all physical firewalls remain false.

## Lane B — exact K5 incidence/relabel/root covariance

Use K5 nodes `0..4` and one lexicographically oriented edge `(a,b)` with `a<b` for each unordered pair.

PASS iff exact integer linear algebra verifies:

1. the signed incidence matrix `B5` has rank 4;
2. deleting any one node row gives rank 4;
3. every reduced incidence transpose spans the same 4-dimensional cut space in edge coordinates;
4. for every `p in S5`, the orientation-aware signed edge permutation `E_p` and node permutation `P_p` satisfy `P_p B5 = B5 E_p` exactly;
5. the induced edge action maps the cut space and the 6-dimensional cycle space to themselves;
6. all five root choices are equivalent as coordinate descriptions of the same cut space.

## Lane C — exact front-face representation controls

For `j in {1/2,1,3/2,2}` use the primitive leading matrices from Iter076X-Z and exact SU(2) generators.

PASS iff:

1. each `C_z` is invertible;
2. `[J_z,C_z]=0`;
3. a transverse generator has `[J_y,C_z] != 0` for every frozen spin;
4. for `j>=1` the right-relative angular connection `C_z^-1[J_y,C_z]` is not a scalar multiple of `J_y`;
5. conjugating `C_z` and its connection by an exact nontrivial compact rotation preserves the data type and the expected adjoint covariance;
6. the common overall branch scale `C -> -C` leaves the relative connection unchanged.

## Lane D — boundary/gauge closure and firewall

Use the seven exact four-valent invariant controls already frozen in Iter076V-W-X-Z.

PASS iff:

1. a common compact node generator annihilates all `7/7` invariant input intertwiners;
2. after application of the leading `C` tensors, the transverse connection remains nonzero in exactly the frozen generic `5/7` controls and zero in the two all-spin-half controls;
3. these two facts are recorded as distinct gauge and front-face tangent structures rather than conflated;
4. the aggregate records:
   - `front_face_data_schema_complete=true`;
   - `K5_incidence_covariance_exact=true`;
   - `compact_gauge_action_closed=true`;
   - `generic_transverse_connection_independent=true`;
   - `correlated_analytic_boundary_value_established=false`;
   - `physical_source_to_K4_pushforward_established=false`;
   - `epsilon_minus1_coefficient_established=false`;
   - no G3/F9/G8/K5 promotion.

## PASS classification

`ITER077A_MINIMAL_TOLLER_FRONT_FACE_DATA_TYPE_CLOSES_COVARIANTLY_ON_K5_INCIDENCE_EXACT_SCOPED`

## FAIL classification

`ITER077A_K5_FRONT_FACE_DATA_TYPE_CLOSURE_FAIL`

A FAIL is an object-definition obstruction and does not authorize a physical divergence/finiteness claim.

## Next admissible gate on PASS

Use this exact data type as the source-side schema for a correlated blown-up/polyhomogeneous K5 boundary object. Analytic extension/growth/wavefront hypotheses must still be established separately before K5 promotion.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full ten-wedge correlated blow-up; no physical source-to-K4 map; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain source spectral `i epsilon`.