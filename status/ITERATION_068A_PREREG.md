# Iteration 068A preregistration — K4 microlocal product collision skeleton

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

For the source-backed ordered spectral-sign bridge from Iter059/062, does the K4 finite-spectral-`i epsilon` **denominator skeleton** satisfy or violate the Hörmander product criterion at the full K4 collision, and is that classification invariant under the unfixed global branch convention?

This is a necessary microlocal skeleton audit only. It is not a computation of the full Toller wavefront set.

## Frozen object

Use vertices `0,1,2,3`, canonical edges `(a,b)` with `a<b`, and the eight physical vertex-sign classes represented by `sigma_0=+1`, `sigma_1,2,3 in {+1,-1}`. Freeze the Iter062 ordered bridge

`s_ab = c * eta(a,b) * kappa_ab`, `kappa_ab=sigma_a sigma_b`, `eta(a,b)=+1` for `a<b`, with global convention `c in {+1,-1}`.

For each canonical edge define the incidence normal `n_ab=e_a-e_b`. The boundary-value denominator skeleton is modeled only at the microlocal-normal level by the oriented covectors `s_ab n_ab`.

## Frozen lanes

`8 sigma classes x 2 global conventions = 16` independent lanes.

Each lane must recompute the graph/covector facts independently rather than importing a cached Iter058 classification.

## Frozen predicates

1. `P1_ORDER_REVERSAL_COVARIANCE`: reversing an ordered wedge flips both `eta` and the spectral sign, consistent with Iter059 branch swap.
2. `P2_EXACT_COLLISION_TEST`: determine exactly whether there exists a nonempty set of edges and strictly positive rational coefficients on that set such that the corresponding oriented normals sum to zero. This is the Hörmander opposing-covector collision test for the denominator skeleton at the common collision.
3. `P3_DIRECTED_CYCLE_EQUIVALENCE`: the exact collision witness exists iff the induced tournament contains a directed cycle; an explicit directed-cycle witness must be returned when obstructed, and an exact topological-order certificate when unobstructed.
4. `P4_FACTOR_CLASS_STRUCTURE`: within the eight physical sigma classes, the obstruction census must be reported without interpreting it as physical sector selection.
5. `P5_GLOBAL_CONVENTION_INVARIANCE`: paired `c=+1/-1` lanes for the same sigma class must have identical obstruction status.

## Frozen lane classifications

- collision witness present and all predicates valid: `K4_HORMANDER_PRODUCT_SKELETON_OBSTRUCTED_AT_FULL_COLLISION`;
- no collision witness and exact transitive/topological-order certificate valid: `K4_HORMANDER_PRODUCT_SKELETON_COMPATIBLE_AT_FULL_COLLISION`;
- otherwise: `ITER068A_INVALID_OR_INCONSISTENT`.

## Frozen aggregate interpretation

The aggregate must require all 16 lanes valid and paired convention invariance. It must report the exact compatible/obstructed census and sigma classes. No post-hoc threshold exists: all checks are exact integer/rational graph identities.

Allowed terminal summaries are descriptive only, e.g. a mixed-domain skeleton classification. There is no allowed `physical sector selected` interpretation.

## Scope / claim locks

- The gate does not establish the full Toller wavefront set, joint holomorphy, growth/temperedness, or distributional Eq.(5)/(6).
- Skeleton compatibility is necessary evidence for a canonical product route, not proof that the full Toller product exists.
- Skeleton obstruction only means the simple Hörmander product theorem cannot canonically define that common-collision product from these oriented denominator covectors; it is not a causal-vertex divergence/nonexistence theorem.
- No physical causal-sector selection, K5/F9/G3/G8 promotion, complete-QG, or `NEW_PHYSICS_FOUND` claim is authorized.
- No fitted counterterm, preferred tree/order, or replacement of the published spectral `i epsilon` is allowed.
