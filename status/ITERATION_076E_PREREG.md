# Iter076E preregistration — source-relative tangent complex vs reduced K4 cycle space

Date: 2026-09-13

## Frozen question

At the local identity configuration of the source carrier Eq.(4), do the ten first-order relative arguments `g_b^-1 g_a` naturally produce the same linear space as the reduced K4 constrained cycle-flow object used by the distributional collision analysis, or is an additional nontrivial projection/dualization mathematically required?

This gate is structural only. It does not define the missing physical pushforward and does not assign a numerator/Jacobian or an `epsilon^-1` coefficient.

## Frozen source model

Use the complete graph K5 with vertices `1..5`, gauge-fix vertex 1, and orient each edge `(a,b)` with `a<b`. For one arbitrary Lie-algebra component, the linearization of the source relative argument is

`Y_ab = X_a - X_b`

(up to one globally frozen orientation convention; reversing all signs changes no rank/subspace conclusion). The 10-vector `Y` is therefore the image of the reduced K5 incidence transpose. Repeat componentwise; no metric on the Lie algebra is introduced.

For comparison only, use the already validated reduced K4 graph object: six oriented edges on four vertices, incidence matrix rank 3, cycle space `ker(B4)` dimension 3.

## Frozen lanes

### Lane A — exact K5 source tangent image

For each of the five gauge roots independently:
- construct reduced K5 incidence matrix `B5r`;
- require `rank(B5r)=4`;
- require source edge-difference image `im(B5r^T)` dimension 4;
- require its orthogonal cycle constraints `ker(B5r)` dimension 6;
- verify all fundamental cycle sums of source differences vanish exactly.

### Lane B — exact K4 comparison

For each of four K4 gauge roots / spanning-tree coordinate choices:
- require `rank(B4r)=3`;
- require cut space `im(B4r^T)` dimension 3;
- require cycle space `ker(B4)` dimension 3;
- require exact zero intersection between cut and cycle spaces under the canonical edge pairing used only as an algebraic comparison;
- verify the repository's constrained six-edge cycle-flow maps span the K4 cycle space, not the source cut space.

### Lane C — no-identity / rank-mismatch certificate

Freeze the following interpretation test:
- a direct identity map from the source K5 relative-edge tangent carrier to the reduced K4 cycle-flow carrier is impossible because the ambient edge sets and invariant dimensions differ (`10, rank 4, cycle-nullity 6` versus `6, cycle-dimension 3`);
- even after restricting source data to any K4 induced subgraph, source relative differences lie in the K4 **cut** space, whereas reduced constrained flows lie in the K4 **cycle** space;
- therefore an additional projection/dualization/submanifold prescription is mathematically required before the two can be identified.

This is not permission to choose such a prescription arbitrarily.

### Lane D — permutation/basis and negative controls

- exhaust all K5 vertex permutations and K4 vertex permutations at the level of ranks/subspace dimensions;
- verify tree/basis changes do not alter the conclusions;
- negative control 1: replace one source edge difference by an independent free edge variable and require at least one cycle-closure identity to fail;
- negative control 2: replace a K4 cycle-space basis vector by a cut-space vector and require the cycle constraint to fail.

## Frozen classifications

If every predicate passes:

`ITER076E_SOURCE_RELATIVE_TANGENT_IS_CUT_SPACE_K4_CYCLE_IDENTIFICATION_REQUIRES_EXTRA_MAP_SCOPED`

If a frozen exact predicate fails with valid implementation:

`ITER076E_STRUCTURAL_HYPOTHESIS_FAIL`

If implementation/runner prevents predicate evaluation:

`ITER076E_INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL`

## Interpretation lock

A PASS establishes only that the natural first-order source relative-coordinate image is an incidence/cut-space object and is not identical to the reduced constrained K4 cycle-space carrier. It narrows P3 by proving that some additional source-derived projection/dualization/submanifold prescription is required. It does **not** prove no such prescription exists, does not define it, and does not imply divergence/finiteness, sector selection, G3/F9/G8/K5 promotion, or `NEW_PHYSICS_FOUND`.

Frozen criteria may not be changed after implementation or result inspection.
