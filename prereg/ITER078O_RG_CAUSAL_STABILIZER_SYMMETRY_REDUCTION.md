# Iter078O-RG preregistration — exact causal-stabilizer symmetry reduction of the all-j=1/2 labelled boundary dual

**Date:** 2026-09-14

## Scientific question

Iter078E/G establish a 32-dimensional order-zero ambiguity in the **labelled** all-`j=1/2` boundary dual, and the adversarial qualification correctly notes that graph automorphisms preserving a fixed causal pattern may reduce the physical symmetry-compatible subspace.

What is the exact dimension of the subspace invariant under the stabilizer of each causal sign class when the action is computed using the actual four-valent `j=1/2` intertwiner tensors and induced leg permutations?

## Frozen local intertwiner basis

Use the normalized repository tensors from Iter077I:

- `|0>`: stripped tensor entries `(+1,-1,-1,+1)` with physical common factor `1/2`;
- `|1>`: stripped entries `(2,-1,-1,-1,-1,2)` with physical common factor `sqrt(3)/6`.

These two tensors are orthonormal in the 16-dimensional four-spin magnetic basis.

No recoupling matrix may be imported from memory; every local permutation matrix must be derived by explicitly permuting the four tensor slots and taking exact inner products with this frozen normalized basis.

## Frozen S5 action on the five-node boundary basis

Nodes are labelled `a=0,...,4`. At node `a`, its four legs are ordered by the ascending neighbour list

`NEIGHBORS[a]=[b in 0..4, b!=a]`.

For a vertex permutation `pi in S5`:

1. node `a` maps to node `pi(a)`;
2. old leg labelled by neighbour `b` maps to leg labelled `pi(b)`;
3. at the destination node, reorder the four mapped legs into the canonical ascending `NEIGHBORS[pi(a)]` order;
4. derive the resulting exact `2x2` local intertwiner matrix from the tensor permutation above;
5. assemble the exact `32x32` global action on the tensor-product basis `(k_0,...,k_4)`.

All arithmetic is over `Q(sqrt(3))`; no floating thresholds.

## Frozen causal classes / stabilizers

Global reversal identifies `p` incoming and `5-p` outgoing with `5-p` incoming, so test representatives:

- class `0<->5`: `sigma=(-,-,-,-,-)`; stabilizer `S5`;
- class `1<->4`: `sigma=(-,+,+,+,+)`; stabilizer `S1 x S4`;
- class `2<->3`: `sigma=(-,-,+,+,+)`; stabilizer `S2 x S3`.

For each class use the full subgroup of vertex permutations preserving the frozen sign vector exactly.

## Lane A — local permutation representation controls

For all `24` permutations of four tensor slots:

- derive the exact `2x2` matrix;
- verify orthogonality/unitarity in the real frozen basis;
- verify the representation composition law;
- record the finite set of distinct matrices.

Invalid if the permuted tensor leaves the two-dimensional invariant subspace or exact composition fails.

## Lanes B/C/D — invariant subspace dimensions

For each causal class separately:

1. build every exact `32x32` stabilizer action matrix;
2. verify group composition on the frozen basis for deterministic generator pairs;
3. compute the exact dimension of the common fixed subspace
   `Fix(G)={v: R(g)v=v for every g in stabilizer}`;
4. compute the same dimension independently by the character average
   `dim Fix(G)=(1/|G|) sum_g Tr R(g)`;
5. require exact agreement.

Also record the rank of stacked `(R(g)-I)` constraints and a deterministic checksum of the character table.

## PASS

PASS iff all representation controls hold and exact invariant dimensions are obtained consistently for all three causal classes.

Classification:

`ITER078O_RG_CAUSAL_STABILIZER_RECOUPLING_SYMMETRY_REDUCES_LABELLED_FULL32_BOUNDARY_DUAL_EXACT_CONTROL_SCOPED`

The result must report the three dimensions explicitly; no prediction of their values is frozen.

## FAIL / INVALID

- `INVALID_IMPLEMENTATION` if tensor permutation / representation / character checks disagree.
- `BLOCKED_CONVENTION` if the repository tensor convention is insufficient to determine the physical graph-permutation action without an additional edge-duality/orientation phase convention.

If a missing phase convention is discovered, do **not** guess it to force a dimension.

## Interpretation ceiling

Even a small invariant dimension is only a symmetry-compatible **control-space** count for one fixed equal-spin causal sector under the frozen tensor/leg convention. It does not by itself prove that the exact causal-Toller distributional extension must be invariant rather than covariant, and it does not select a point in that subspace.

No unique extension, RG fixed point, generic-spin coupling count, regulator independence, G3 or complete-QG claim follows.