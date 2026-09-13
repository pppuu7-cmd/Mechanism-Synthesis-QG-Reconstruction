# Iter078B-RG preregistration — minimal 1-to-5 causal refinement orientation gate

**Date:** 2026-09-14

## Motivation / anti-rescue lock

A same-boundary refinement map is required for regulator independence and background-independent RG even if the Iter077 extension ambiguity did not exist. Therefore this gate is independently motivated and is not introduced merely to rescue CRQN.

This gate defines only the causal-combinatorial part of a prospective refinement map. It does not alter the causal-Toller vertex or choose an extension coefficient.

## Frozen coarse/fine complexes

Coarse region: one Lorentzian 4-simplex, represented by one spin-foam vertex with five boundary dual edges labelled `a=0,...,4` and frozen coarse boundary causal signs

`sigma_a in {−1,+1}`.

Fine region: the standard `1 -> 5` subdivision obtained by inserting one interior primal vertex. The five refined 4-simplices are labelled `v_a` by the original boundary tetrahedron they contain. Their internal dual adjacency graph is `K5`: every pair `v_a,v_b` shares one internal tetrahedron.

The external boundary is unchanged: fine vertex `v_a` carries exactly boundary tetrahedron/dual edge `a`, with external orientation inherited from the coarse sign `sigma_a`.

## Frozen causal rule

Primary causal-vertex source associates `sigma=−1` to an ingoing edge and `sigma=+1` to an outgoing edge at a spin-foam vertex, and states that oriented edges determine a partial order of spin-foam vertices.

For the fine `K5` internal dual graph:

1. every internal edge has one global orientation;
2. at its source endpoint its local sign is `+1` and at its target endpoint its local sign is `−1`;
3. the internal directed graph must be acyclic;
4. to preserve the coarse boundary transition, every fine vertex attached to an ingoing coarse boundary edge must precede every fine vertex attached to an outgoing coarse boundary edge.

Condition 4 is the prospectively frozen coarse-to-fine causal compatibility condition. It is not readjusted after enumeration.

## Frozen sectors

Enumerate **all 32** coarse boundary sign vectors. Do not pick only one transition class.

For each sign vector:

- enumerate all `2^10=1024` orientations of the ten internal K5 edges;
- test acyclicity exactly;
- test boundary-order compatibility exactly;
- record the number of compatible internal orientations;
- record the induced five local sign 5-tuples at all refined vertices for every compatible orientation;
- classify each local fine vertex into `0↔5`, `1↔4`, or `2↔3` up to overall sign reversal, matching the three source causal classes.

## Exact prediction / analytic control

An acyclic orientation of a complete graph K5 is equivalent to a total order of its five vertices. If the coarse sign vector has `p` ingoing and `q=5-p` outgoing boundary edges, condition 4 requires the p incoming-attached vertices to occupy the first p positions and the q outgoing-attached vertices the last q positions. Therefore the frozen prediction is

`N_compatible(p,q) = p! q!`.

This gives:

- `p=0 or 5`: `120`;
- `p=1 or 4`: `24`;
- `p=2 or 3`: `12`.

The brute-force enumeration must independently reproduce these counts for all 32 boundary patterns.

## PASS

PASS iff:

- all 32 coarse boundary sign vectors admit at least one compatible acyclic internal orientation;
- exact counts equal `p!q!` for every vector;
- every induced local fine-vertex sign tuple belongs to one of the source-allowed three causal classes;
- reversing all coarse boundary signs maps the compatible set bijectively under global orientation reversal.

Classification:

`ITER078B_RG_1TO5_CAUSAL_BOUNDARY_ORIENTATIONS_EXTEND_TO_FINE_ACYCLIC_K5_ALL32_EXACT_COMBINATORIAL_SCOPED`

## FAIL

FAIL iff at least one frozen coarse causal pattern has zero compatible fine orientations or violates the exact count/control.

## BLOCKED

BLOCKED iff the 1-to-5 dual adjacency or source edge-orientation convention cannot be fixed unambiguously.

## Interpretation ceiling

PASS supplies only the causal-label part of a refinement map. It does **not** define the fine amplitude, internal spin/intertwiner measure, local distributional extension, embedding map, coarse-graining projection, RG flow, fixed point, regulator independence, or G3.

Exact next dependency on PASS: freeze the fine-complex amplitude/measure and the coarse/fine boundary matching map while carrying the Iter077 extension freedom as explicit coupling data.