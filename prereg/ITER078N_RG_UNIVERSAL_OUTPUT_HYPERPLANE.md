# Iter078N-RG preregistration — universal output-hyperplane identity of the fixed-j=1/2 refinement control

**Date:** 2026-09-14

## Scientific question

Iter078M found exact Jacobian rank `31` at all four prospectively frozen tensors A/B/C/L, but correctly classified generic rank as inconclusive. Is there an exact structural linear relation

`w · R(C) = 0`

for **every** local tensor `C in C^32` under the frozen fixed-`j=1/2` EPRL-edge-weight 1-to-5 control map?

If yes, the image of the polynomial refinement map lies in a fixed 31-dimensional hyperplane and the Jacobian has global rank at most 31. If no, repeated rank 31 at A/B/C/L remains a local sampling fact only.

## Frozen map and points

Use exactly the Iter078H map `R_EPRL:C^32->C^32`, with the same lexicographic basis, slot convention, `2^10` internal binary intertwiner sums, face factor `2^10`, and edge weights `d_k=2k+1`.

Reuse without modification the four Iter078M points:

- `A_i=i+1`;
- `B_i=(-1)^popcount(i)(i+1)`;
- `C_i=(i+1)^2`;
- `L` = compact Iter077N tensor.

No new rank-sampling point is admitted in this gate.

## Lane A — exact left-null comparison

For each of A/B/C/L:

1. compute the exact `32x32` Jacobian over `Q`;
2. compute a deterministic primitive integer **left** null vector `w_X`, i.e. a primitive right-null vector of `J_X^T`;
3. verify `w_X^T J_X=0` exactly;
4. normalize the first nonzero component positive;
5. compare all four vectors for exact equality/proportionality.

Record one of:

- `COMMON_IDENTICAL`;
- `COMMON_PROPORTIONAL`;
- `DIFFERENT`.

## Lane B — coefficientwise polynomial identity, conditional on a common left vector

If Lane-A recomputation yields one common primitive left vector `w`, construct

`P_w(C)=w·R_EPRL(C)`

**coefficientwise**, not by point sampling.

The map is homogeneous degree 5. Enumerate all `32*2^10=32768` output/internal configurations. Each configuration contributes an exact integer coefficient times a commutative degree-5 monomial in the 32 local tensor components. Canonicalize each monomial by sorting its five component indices and accumulate exact integer coefficients.

Required outputs:

- total raw configuration count `32768`;
- number of distinct monomials before dropping zeros;
- number of nonzero monomial coefficients after exact accumulation;
- deterministic checksum of the coefficient dictionary.

`P_w(C)≡0` iff **every** accumulated monomial coefficient is exactly zero.

If Lane-A vectors differ, Lane B must return `NO_COMMON_W`, not manufacture a candidate.

## Lane C — frozen simple-character catalogue

Before seeing `w`, compare any common primitive left vector against this frozen catalogue:

1. constant vector;
2. all 32 Walsh characters `chi_s(k)=(-1)^(s·k)`;
3. parity of total `sum_a k_a`;
4. Hamming-weight vectors `sum_a k_a` and `5-sum_a k_a`;
5. compact tensor `L`, its support indicator, zero-support indicator, and `sign(L)`.

A match requires exact proportionality over `Q`. No post-hoc catalogue entries may be added.

## Lane D — unit-edge-weight control

Repeat Lane A and the coefficientwise polynomial test for the Iter078H unit-edge-weight map, using the **same four frozen tensors**.

This determines whether any universal output hyperplane is a topology/basis identity independent of the EPRL edge weights, or a measure-specific feature.

## PASS

PASS iff the EPRL map has one common exact left-null vector across A/B/C/L **and** the coefficientwise calculation proves

`w·R_EPRL(C) ≡ 0`.

Classification:

`ITER078N_RG_FIXED_JHALF_REFINEMENT_CONTROL_IMAGE_LIES_IN_EXACT_UNIVERSAL_31D_OUTPUT_HYPERPLANE_STRUCTURAL_RANK_CEILING_SCOPED`

Allowed conclusion: global Jacobian rank `<=31` for this frozen polynomial control map.

## FAIL

FAIL iff a common candidate `w` exists at the frozen points but `P_w` has at least one nonzero exact monomial coefficient.

## INCONCLUSIVE

If the left nulls differ across A/B/C/L, classify

`ITER078N_RG_NO_COMMON_LEFT_NULL_ACROSS_FROZEN_RANK31_POINTS`

with verdict `INCONCLUSIVE_STRUCTURAL_RANK`.

## Interpretation ceiling

Even PASS concerns only the fixed all-`j=1/2`, pure order-zero, labelled tensor-network control map. A structural one-dimensional output constraint there is not automatically a gauge identity or physical constraint of the causal-Toller refinement map.

No unique K5 extension, physical RG fixed point, regulator independence, generic-spin result, G3 or complete-QG claim follows.