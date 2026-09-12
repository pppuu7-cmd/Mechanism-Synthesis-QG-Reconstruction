# Iteration 055 — K4 signed-normal minimal positive-circuit atlas and S4 covariance

## Preregistration

This file is committed **before** implementation and before any Iter055 production output is inspected.

Iter055 is independent of the terminal outcome of Iter054. It does not read Iter054 artifacts and does not alter the frozen Iter054 feasibility criterion.

## Question

For each factorized K4 causal sign class `s` and each frozen K4 cycle basis, define the exact signed-normal matrix

`M = diag(s) A`,

where the rows of `A` are the six edge linear forms in the three cycle variables.

A strict affine sign chamber fails exactly when the signed row normals possess a positive dependence. Iter054 records at most one obstruction certificate per lane. Iter055 instead freezes the **complete atlas of minimal positive circuits** and asks whether that atlas is:

1. independent of the four frozen tree/cycle bases; and
2. covariant under every vertex permutation in `S4`, after the induced edge permutation and the standard global-sign regauging `sigma_0=+1`.

This is a structural hyperplane-arrangement/oriented-matroid audit. It is not a fitted contour prescription.

## Frozen objects

Edge order is fixed as

`01, 02, 03, 12, 13, 23`.

Causal classes are the eight factorized `sigma` gauge classes already used in Iter051A–Iter054. Tree/cycle bases are frozen as `S0,S1,P0,P1`.

For every `(sign_class, tree)`, enumerate all edge subsets of support size 1 through 4. A support is a **positive circuit** iff there exists an exact rational vector of weights with:

- all weights strictly positive;
- weights summing exactly to 1;
- weighted signed-normal sum exactly zero;
- no proper subset already satisfies the same positive-dependence condition.

Support size ≤4 is complete by Caratheodory in `R^3`.

No numerical tolerance, optimizer, post-hoc pruning threshold, or chosen obstruction certificate is allowed.

## S4 action

Enumerate all 24 permutations of K4 vertices. For each permutation:

1. permute the four `sigma` vertex signs;
2. apply the unique global sign flip, if needed, restoring `sigma_0=+1`;
3. identify the induced target causal sign class;
4. permute every circuit support by the induced permutation of the six undirected edges.

The transformed circuit atlas must match the target-class atlas exactly as a set of edge-index supports.

## Frozen validity checks

- all four cycle matrices are exact rank-3 bases of `ker(B)` with unimodular tree minor;
- all positive-circuit certificates reconstruct zero exactly and use strictly positive rational weights;
- every reported circuit is support-minimal;
- every possible support of size ≤4 is exhaustively tested;
- basis comparison is exact set equality;
- all 24 vertex permutations induce valid bijections of the six edges and valid causal gauge classes.

## Frozen terminal classifications

- `ITER055_CIRCUIT_ATLAS_INVALID` if any exact reconstruction, completeness, minimality, edge-permutation, or class-map check fails.
- `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_BASIS_DEPENDENT` if valid circuit support atlases differ between `S0,S1,P0,P1` for any causal class.
- `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT` if basis invariance passes but any of the 24 vertex permutations fails exact atlas covariance.
- `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_BASIS_AND_S4_COVARIANT` iff all validity checks, exact basis invariance and all S4 covariance checks pass.

The aggregate must also report the exact S4 orbit decomposition of the eight causal classes, circuit-support counts and circuit-size histograms for each class/orbit.

## Claim locks

Iter055 does **not** establish a physical amplitude, a contour prescription, K5, G3, F9, G8, new physics, or a general no-go theorem. It only classifies exact minimal positive dependencies of the frozen K4 signed-normal arrangement and their covariance.
