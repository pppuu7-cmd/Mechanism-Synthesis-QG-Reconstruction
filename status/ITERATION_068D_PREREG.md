# Iteration 068D preregistration — S4 covariance of the Iter068A skeleton partition

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

Is the Iter068A denominator-skeleton compatible/obstructed classification covariant under arbitrary permutations of the four K4 vertices when the edge signs, canonical edge orientation and gauge representative `sigma_0=+1` are transformed consistently?

## Frozen object

Use exactly the Iter068A K4 incidence-normal skeleton and ordered-sign bridge. Start from each of the eight physical sigma classes with `sigma_0=+1` and both global conventions `c=±1`.

For every permutation `p in S4`:

1. relabel vertices and edge data;
2. recanonicalize each edge to `a<b`, including the orientation sign from reversing an edge when needed;
3. gauge-fix the transformed sigma tuple back to `sigma_0=+1` by a global sigma flip if necessary (which leaves `kappa_ab` invariant);
4. recompute the exact directed-cycle/positive-circulation classification from the transformed incidence normals.

## Frozen lanes

`8 sigma classes x 2 conventions = 16 lanes`.

Each lane internally evaluates all `24` vertex permutations. Total exact transformed cases: `384`.

## Frozen predicates

1. all 24 transformed cases reconstruct the relabeled physical `kappa` pattern exactly;
2. gauge recanonicalization leaves `kappa` invariant;
3. the transformed collision classification equals the original Iter068A classification for every permutation;
4. applying the inverse permutation recovers the original ordered-edge skeleton exactly up to the already-audited global convention reversal.

## Frozen classification

All 384 transformed cases pass:

`ITER068D_K4_MICROLOCAL_SKELETON_S4_COVARIANT`

otherwise:

`ITER068D_K4_MICROLOCAL_SKELETON_PERMUTATION_FAILURE`.

## Scope locks

This is a covariance audit of the denominator skeleton only. It does not turn the compatible half of Iter068A into physical sectors, does not establish a full Toller wavefront theorem, and does not alter the Iter068B contact-layer or Iter068C distributional-control questions. No K5/G3/F9/G8 promotion is authorized.
