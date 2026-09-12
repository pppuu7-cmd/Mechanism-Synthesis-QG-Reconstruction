# Iteration 049 — preregistration: RR selector covariance under cycle-coordinate permutations

## Motivation
Iter048 terminally established `K4_FP_OBSTRUCTION_MIXED_CHANNELS`: `RR` is nonzero in 8/24 frozen source lanes, while `RA/AR/AA` are nonzero in 24/24. Before interpreting the RR subset structurally, we must determine whether its activation follows the underlying cycle pair or merely positional labels in the implementation.

This file freezes the gate **before implementation and before viewing Iter049 outputs**.

## Frozen scientific object
Use exactly the same K4 source kernels, held-out physical cases, four spanning-tree/fundamental-cycle bases, and unchanged one-dimensional `FP=R+A` functional as Iter048. No physics parameters, contour rules, pole selection, quotient subtraction, residue formula, or infinity coefficient are changed.

Cases:
- A: `gamma=0.83`, `epsilon=0.06`, signs `++++++`, `k=(0.19,-0.31,0.27,-0.15)`
- B: `gamma=1.43`, `epsilon=0.12`, signs `-++-++`, `k=(-0.22,0.37,-0.28,0.13)`

Trees: `S0,S1,P0,P1`.

## Frozen permutation protocol
For each `(case, tree)`, start from the three cycle variables `(y0,y1,y2)` produced by the existing K4 kernel. Apply each of the six permutations `p` of `(0,1,2)` by a pure symbolic variable relabeling, with no algebraic retuning. In the permuted representation, evaluate the exact channel commutator for the **canonical ordered pair `(0,1)`**.

Record the corresponding original ordered pair `(p[0],p[1])`, the remaining original coordinate `p[2]`, exact source/control total commutators, exact `RR/RA/AR/AA` channel deltas, and all reconstruction identities.

Matrix: 2 cases × 4 trees × 6 permutations = **48 lanes**. Use `fail-fast:false` and parallel execution.

## Mandatory validity gates per lane
A lane is scientifically valid only if all are true:
1. symbolic permutation round-trip returns the original kernel exactly;
2. each one-step `R+A` equals the frozen `finite_part_1d` result exactly;
3. ordered channel sums reconstruct each ordered two-step FP result exactly;
4. `Delta_RR+Delta_RA+Delta_AR+Delta_AA` reconstructs the full frozen commutator exactly;
5. ordinary EPRL/no-contact control total commutator is exactly zero;
6. all control channel commutators are recorded explicitly.

Any failure => `ITER049_CONTROL_OR_RECONSTRUCTION_INVALID`; do not interpret selector physics.

## Frozen selector tests
For each `(case,tree)`, compare permutations after mapping the canonical pair back to the original ordered pair.

Define:
- `mapped_pair_covariant`: RR zero/nonzero status is identical for the two permutations representing the same unordered original pair, independent of orientation of that pair;
- `position_locked`: RR status is identical across all six permutations regardless of mapped original pair;
- `pair_selective`: at least one original unordered pair is RR-nonzero and at least one is RR-zero.

Global classifications:
1. `K4_RR_SELECTOR_PAIR_COVARIANT` if every lane is valid, controls are exact zero, every `(case,tree)` is mapped-pair covariant and pair-selective, and the selected unordered-pair pattern is consistent across held-out cases for each tree.
2. `K4_RR_SELECTOR_POSITION_LOCKED` if every lane is valid and RR zero/nonzero depends only on canonical positions rather than mapped original pair (no pair selectivity after remapping).
3. `K4_RR_SELECTOR_NONCOVARIANT` if valid but orientation/permutation changes RR status for the same mapped unordered pair, or held-out cases disagree on selected pair pattern.
4. `ITER049_CONTROL_OR_RECONSTRUCTION_INVALID` if any mandatory validity gate fails.

No threshold fitting or post-hoc redefinition is allowed.

## Interpretation rule
- `PAIR_COVARIANT`: RR activation is a real algebraic feature of a subset of cycle-pair relations in the frozen kernel, not a trivial positional artifact. Next gate should identify the exact graph/overlap invariant selecting that pair and separate it from the universal A-containing obstruction.
- `POSITION_LOCKED`: treat the RR subset as implementation/coordinate artifact until repaired; do not build multivariate physics on it.
- `NONCOVARIANT`: the current R/A decomposition is not coordinate-stable enough for physical construction; diagnose the algebra before any forest prescription.

## Claim lock
Iter049 is a covariance/selector audit of the existing diagnostic decomposition only. It cannot establish a physical causal-vertex divergence, a unique multivariate extension, K5 readiness, G3 PASS, F9, G8, or a new quantum-gravity theory.
