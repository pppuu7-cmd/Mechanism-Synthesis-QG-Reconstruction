# Iter077A-SM result — true source B-map has a full-rank common-collision witness

**Date:** 2026-09-14

`Iter077A-SM` is the stable prose alias for the source-map sibling historically frozen and executed under the label `Iter077A`. Frozen filenames, JSON labels, workflow names, commits and artifacts are not renamed.

## Authority

- source/derived supplement: `08499d9cb1bd786adfdd842364606b4517d1962d`
- prospective preregistration: `f8dbe2d008b46369fb45ef6fc7c5ff887967f299`
- implementation: `e8ddeb1acc6830e6620db02630088eae3b23b2d9`
- production/workflow head: `83eb3da869f3ad324471db61ec47f02dad36091e`
- authoritative run: `34784565177`
- jobs: A `103797568496`, B `103797568499`, C `103797568462`, D `103797568340`, aggregate `103797589743`

Artifacts:

- A `10325773212`, `sha256:2119c3058ee908ccfba5f251ee58b21231ee7377b4ee1edd777bb42850de789a`
- B `10325798243`, `sha256:297c68f1aeeeddea5a35208a7f0e3ee49b3674d3ac6d25ae834c3eeefc4a87f6`
- C `10325838201`, `sha256:a38f60965dce8373b86abae7e47474d1ade9aa63b113b6efe622a3ade9e716a9`
- D `10326192252`, `sha256:c193367c6595330bbd03514094ca9aa0874d05b5ff7e1f6331c85785151d512e`
- aggregate `10326301884`, `sha256:e101c11b752cd53663f7a445c6c837c578cd389ddc9d3396a84621e5a91245d4`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED`

## Exact source-map differential

For the source function

`B_ab(z_ab,g_b^(-1)g_a)=log(<g_ab^dagger z_ab|g_ab^dagger z_ab>/<z_ab|z_ab>)`

at the common group collision and in gauge-fixed Hermitian boost coordinates, the exact first differential is

`dB_ab = n_ab . (dx_a-dx_b)`,

where each `n_ab` is the Bloch vector of the independent wedge spinor `z_ab`.

The frozen exact witness used

- `e_x` on `01,12,23,34`,
- `e_y` on `02,03,13,14`,
- `e_z` on `04,24`.

The corresponding `10 x 12` rational Jacobian has

`rank_Q(J)=10`,

left nullity `0`, and an exact nonzero maximal minor

`det J_minor = -1`.

The minor uses columns

`v1x,v1y,v2x,v2y,v2z,v3x,v3y,v4x,v4y,v4z`.

Because this maximal minor is a nonzero analytic function of the wedge-normal data, full rank persists on an open neighbourhood of the frozen witness. This is a local common-collision transversality statement, not a global full-vertex theorem.

## Scalar-surrogate non-transfer

The rooted scalar K5 incidence matrix has exactly

`rank_Q(I)=4`, left nullity `6`.

At the true source witness the Jacobian has rank `10` and left nullity `0`. All six exact basis relations in the scalar left nullspace were applied to the true source Jacobian; `0/6` annihilate it.

Therefore the six scalar K5 cycle relations are **not identities of the true source differential**. They cannot be promoted to constraints of the coherent-spinor causal amplitude without an additional, explicit source pushforward theorem.

## Exact discrete normal-direction census

As a descriptive exact control, all `3^10=59049` assignments of axis normals `e_x,e_y,e_z` to the ten wedges were enumerated. The rank histogram is

| rank | count |
|---:|---:|
| 4 | 3 |
| 5 | 60 |
| 6 | 600 |
| 7 | 4800 |
| 8 | 17766 |
| 9 | 26100 |
| 10 | 9720 |

For these axis controls, rank 10 occurs exactly when each of the three color subgraphs is a forest: `9720/59049` assignments. The three monochromatic controls each have rank 4. Exact direct matrix-rank checks agree with the graph formula for the frozen witness, all monochromatic controls and the frozen deterministic sample.

No continuum measure statement is inferred from this finite census.

## Scientific consequence

The rank-4 scalar incidence picture is a special collinear slice of the true source coherent-spinor geometry, not its generic first-order structure at the common collision. Consequently, further scalar K5/K4 cycle/Hodge calculations remain conditional algebra until a physical source pushforward is derived.

The local distributional risk is now concentrated on the exceptional source set

`Sigma = {(g,z): rank dB < 10}`,

and on global/noncompact integration and regulator removal. The present result does not establish finiteness or existence of the causal vertex.

## Next admissible gate

Characterize the first exact common-collision rank-deficient strata through the left-null/self-stress equations of the true Jacobian. Establish which geometric normal configurations force `rank dB<10` and which merely belong to special surrogate slices. Only after this classification should their contribution to products of source contact distributions be tested.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full causal-vertex finiteness/divergence theorem; no global integrability theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.