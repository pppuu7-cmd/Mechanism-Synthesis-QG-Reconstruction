# Iter077C-SM preregistration — first exceptional source strata at the common collision

**Date:** 2026-09-14  
**Status:** prospective / frozen before implementation

## Dependencies and scope

This source-map sibling depends on:

- `sources/CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md`;
- authoritative `Iter077A-SM`, result `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`;
- provenance ledger `status/ITER077_PROVENANCE_LEDGER.md`.

No new external formula is introduced. The gate studies the exact common-collision differential of the true coherent-spinor source map

`J_(ab),(c,i) = (delta_ac-delta_bc) n_ab^i`,

with root `0` gauge fixed, ten unit Bloch normals `n_ab in S^2`, and columns `(c,i)` for `c=1,...,4`, `i=x,y,z`.

This gate does not yet evaluate the nonlinear contact-distribution product, the full vertex integral, regulator removal, the physical source-to-K4 pushforward or any `epsilon^-1` coefficient.

## Exact rank-deficiency / self-stress statement

For edge coefficients `lambda_ab`, define the vector equilibrium at node `c`

`E_c(lambda,n) = sum_{b>c} lambda_cb n_cb - sum_{a<c} lambda_ac n_ac`.

Because each edge enters its two endpoints with opposite signs,

`sum_{c=0}^4 E_c = 0`.

Therefore, with root 0 removed,

`lambda^T J = 0  <=>  E_c=0 for c=1,...,4`,

and root equilibrium then follows automatically. Hence

`rank J < 10  <=>  exists lambda != 0 satisfying vector equilibrium at all five nodes`.

The implementation must verify this equivalence on all frozen discrete controls and must not replace it by scalar K5 cycle relations.

## Lane A — provenance / object lock

PASS-valid iff:

1. `Iter077A-SM` durable result is present with exact witness rank 10 and scalar-cycle non-transfer;
2. the provenance ledger distinguishes `Iter077A-SM`, `Iter077A-FF` and `Iter077B-BCH`;
3. the implementation uses ten wedge-local normals and the exact `10 x 12` source Jacobian;
4. scalar incidence relations are used only as negative/special-slice controls;
5. all global physical claim locks remain active.

If any dependency is missing or ambiguous: BLOCKED.

## Lane B — exact self-stress equivalence and lower-dimensional controls

Use exact rational axis normals.

PASS-valid iff:

1. for every frozen control, `dim left-null(J) = 10-rank(J)` exactly;
2. direct `lambda^T J=0` agrees exactly with the five-node vector-equilibrium equations, including automatic root redundancy;
3. the monochromatic controls have rank 4 and self-stress dimension 6;
4. a deterministic lexicographic planar `{e_x,e_y}` assignment of maximal rank has rank 8 and self-stress dimension 2;
5. no scalar-cycle identity is promoted beyond these special slices.

The planar control is selected by the frozen rule: lexicographically first binary axis assignment, in edge order

`01,02,03,04,12,13,14,23,24,34`,

whose exact rank equals the maximum attained among all `2^10` `{e_x,e_y}` assignments.

## Lane C — first full-span rank-9 stratum and structured transversality

### Frozen witness-selection rule

Enumerate the `3^10` axis assignments in lexicographic order with `x<y<z`, using the edge order above. Select the **first** assignment satisfying:

- all three axes occur;
- exact source rank is `9`.

The witness itself is therefore determined before implementation by this rule and cannot be changed after seeing the transversality result.

At this rank-9 witness:

- let `lambda` span the exact one-dimensional left nullspace of `J`;
- let `r_1,r_2,r_3` be the exact right-nullspace basis of `J`;
- for each edge normal use the two coordinate-axis tangent vectors orthogonal to that normal, giving 20 exact tangent directions in `(S^2)^10`.

For tangent direction `(e,t)`, let `delta J_(e,t)` be the derivative obtained by replacing only `n_e` by tangent vector `t`. Construct the exact `3 x 20` normal-variation matrix

`L[k,(e,t)] = lambda^T delta J_(e,t) r_k`.

This is the derivative from the structured normal manifold to the normal space of the rank-`<=9` determinantal variety at a rank-9 matrix.

### Scientific PASS

If `rank_Q(L)=3`, classify:

`ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED`

Interpretation: at this exact full-span source witness, the structured map is transverse to the rank-9 determinantal locus; locally the first exceptional stratum is a smooth codimension-3 subset of the 20-dimensional normal-direction manifold.

### Scientific FAIL

If the witness is valid but `rank_Q(L)<3`, classify:

`ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_NONTRANSVERSE_LOWER_CODIM_EXACT_SCOPED`

This is a scientifically valid negative result: the source-normal geometry hits the rank-deficient locus nontransversely at the frozen witness. Do not change the witness or PASS criterion.

### BLOCKED

If no full-span rank-9 axis witness exists or the nullspace/tangent object is not consistently defined, classify:

`ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATUM_BLOCKED_OBJECT_DEFINITION`

## Lane D — exact discrete stress taxonomy

Enumerate all `3^10=59049` axis assignments exactly. Report a joint census by:

- exact rank;
- normal-span dimension (`1`, `2` or `3` for the axis controls);
- self-stress dimension `10-rank`.

PASS-valid iff:

1. all 59049 assignments are counted exactly once;
2. marginal rank counts reproduce authoritative `Iter077A-SM` exactly:
   `4:3, 5:60, 6:600, 7:4800, 8:17766, 9:26100, 10:9720`;
3. the selected Lane-C witness belongs to the full-span rank-9 class;
4. exact direct matrix-rank/self-stress crosschecks agree with the graph/rational computation on the witness, all monochromatic controls, the selected planar control and at least 32 deterministic assignments.

This finite census is descriptive. It does not establish a continuum measure or codimension theorem away from the frozen witness.

## Aggregate rule

- A/B/D invalid -> aggregate `BLOCKED`.
- A/B/D valid and C scientific PASS -> aggregate PASS classification above.
- A/B/D valid and C scientific FAIL -> aggregate FAIL classification above; workflow execution must still succeed so the negative scientific result is preserved.
- C object BLOCKED -> aggregate BLOCKED.

## Consequence boundary

Even a codimension-3 local rank-9 stratum does **not** prove the contact-distribution product harmless. The next admissible source-map step would be to include the true nonlinear `B` jet normal to a frozen exceptional stratum and test the local pullback/scaling of the source contact terms. Only after exceptional-stratum control may the frozen full contracted vertex/regulator-removal test be attempted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no global full-rank theorem; no full causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.