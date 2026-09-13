# Iter077A preregistration — true source B-map transversality and scalar-surrogate non-transfer

**Date:** 2026-09-14  
**Status:** prospective / frozen before implementation

## Authority and scope

Source/derived input commit: `08499d9cb1bd786adfdd842364606b4517d1962d`  
Source formula: causal-vertex Eq. (17), Appendix C Eq. (32), Appendix D Eqs. (35)-(39), arXiv:2601.23162.

This gate is intentionally upstream of full vertex integration. It tests the exact first differential of the true ten-component source map at the common group collision and whether the six linear cycle relations of the scalar K5 incidence surrogate can be promoted to source identities.

It does **not** test full causal-vertex finiteness, regulator independence, the physical source-to-K4 pushforward, or the nominal `epsilon^-1` coefficient.

## Frozen mathematical object

Gauge-fix node `0` and use boost coordinates

`g_a = exp[(x_a . sigma)/2]`, `a=1,...,4`, `x_0=0`.

For each of the ten unordered K5 wedges `e=(ab)`, define

`B_e(z_e,g_b^(-1)g_a) = log(<g_e^dagger z_e|g_e^dagger z_e>/<z_e|z_e>)`

and the Bloch vector

`n_e^i = <z_e|sigma_i|z_e>/<z_e|z_e>`.

At the common group collision, freeze the exact differential

`J_e,(c,i) = (delta_ac-delta_bc) n_e^i`, `c=1,...,4`, `i=x,y,z`.

The scalar surrogate is the ordinary rooted K5 incidence matrix `I` of size `10 x 4`, corresponding to one common collinear normal direction.

## Frozen witness

Use independent projective wedge spinors realizing the following Bloch directions:

- `n=e_x` on edges `01,12,23,34`, represented by `z_x=(1,1)`;
- `n=e_y` on edges `02,03,13,14`, represented by `z_y=(1,i)`;
- `n=e_z` on edges `04,24`, represented by `z_z=(1,0)`.

No witness may be changed after implementation begins.

## Lane A — source lock

PASS iff all frozen source facts are present and the implementation uses the true wedge-local `B(z,g)` object with ten independent auxiliary spinors. FAIL if the implementation substitutes the scalar incidence model for the source map. BLOCKED if source provenance cannot be verified.

## Lane B — exact full-rank witness

Construct the exact integer `10 x 12` Jacobian from the frozen witness.

PASS iff:

1. `rank_Q(J)=10` exactly;
2. at least one exact `10 x 10` minor is nonzero and its determinant is recorded;
3. each witness Bloch vector is verified exactly from its projective spinor.

FAIL iff `rank_Q(J)<10`. BLOCKED iff the source derivative formula cannot be represented without an unstated convention.

If PASS, the nonzero analytic minor also certifies rank 10 on an open dense subset of nearby wedge-spinor directions at the common collision; this is a local genericity statement only.

## Lane C — scalar-surrogate non-transfer

Construct the rooted scalar K5 incidence matrix `I` exactly.

PASS iff:

1. `rank_Q(I)=4` and left-nullity is `6`;
2. `rank_Q(J)=10` and left-nullity is `0` at the frozen true-source witness;
3. every basis vector of the scalar left nullspace fails to be a left-null relation of `J`.

This PASS means the six scalar cycle relations are not identities of the true source differential and cannot be transferred without an additional pushforward theorem.

FAIL iff a nonzero scalar cycle relation annihilates the true `J` identically at the full-rank witness, which would contradict item 2 and signal an implementation error or a wrong frozen derivative.

## Lane D — exact discrete normal-direction census

Enumerate all `3^10 = 59049` assignments of `e_x,e_y,e_z` to the ten K5 wedges. For these axis-aligned controls, use the exact graph identity

`rank(J) = sum_{axis in {x,y,z}} rank(rooted incidence of axis-colored subgraph)`.

For a color subgraph on all five vertices, its rooted incidence rank is `5 - number_of_connected_components`, with isolated vertices counted as components.

The lane is a computational-validity/descriptive lane, not part of the main physical PASS. It is valid iff:

- all 59049 assignments are enumerated exactly;
- the rank histogram sums to 59049;
- the frozen witness has rank 10;
- each of the three monochromatic controls has rank 4;
- direct matrix rank crosschecks agree with the graph formula on the frozen witness, the three monochromatic controls, and a deterministic sample of at least 32 assignments.

The exact histogram and the number of full-rank axis assignments must be reported regardless of outcome. No continuum exceptional-stratum measure claim may be inferred from this discrete census.

## Aggregate verdict

PASS classification, frozen in advance:

`ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED`

Aggregate PASS requires A, B and C PASS and D valid.

Aggregate FAIL classification:

`ITER077A_TRUE_SOURCE_B_MAP_FULL_RANK_WITNESS_FAILS_EXACT_SCOPED`

if Lane B validly returns rank below 10.

Aggregate BLOCKED classification:

`ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_BLOCKED_OBJECT_OR_SOURCE_DEFINITION`

if source conventions or the derivative object cannot be frozen consistently.

## Scientific consequence if PASS

The scalar K5 incidence rank-4/cycle-nullspace structure is a special collinear slice, not the generic first-order structure of the source coherent-spinor map. The next mathematically admissible front is the exceptional set

`Sigma = {(g,z): rank dB < 10}`,

followed by the fully contracted source-amplitude local-limit test. Reduced K4/Hodge coefficients remain conditional until an actual source pushforward is derived.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full causal-vertex finiteness/divergence theorem; no global integrability theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.