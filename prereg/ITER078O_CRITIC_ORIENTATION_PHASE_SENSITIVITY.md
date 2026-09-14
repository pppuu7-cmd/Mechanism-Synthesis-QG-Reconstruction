# Iter078O adversarial control preregistration — orientation/duality phase sensitivity

**Date:** 2026-09-14

## Reviewed result

`results/ITER078O_RG_CAUSAL_STABILIZER_SYMMETRY_RESULT.md` reports exact fixed-subspace dimensions `2,3,5` for the slot-permutation representation induced from the frozen all-`j=1/2` intertwiner tensors. Its preregistration explicitly requires `BLOCKED_CONVENTION` if an additional edge-duality/orientation phase convention is needed to identify the physical graph-permutation action.

## Adversarial hypothesis

The exact arithmetic of the frozen slot-permutation representation is correct, but the absolute fixed-space dimensions can depend on an unresolved representation-level phase convention. Therefore `2,3,5` may be authoritative only for the explicitly frozen slot action unless the physical causal boundary convention fixes the phase/duality action independently.

## Frozen control

Use the exact Iter078O representation `R(pi)` without modifying its tensors or subgroup definitions. Define the parity-twisted representation

`R_sign(pi) = sgn(pi) R(pi)`.

This is an exact representation of `S5`, and its restriction to each frozen causal stabilizer remains an exact representation. It is not asserted to be the physical causal action; it is an adversarial convention-sensitivity control representing the simplest nontrivial one-dimensional phase character compatible with group composition.

For each causal stabilizer compute exactly:

- the original invariant multiplicity `m_triv=(1/|G|) sum Tr R(g)`;
- the parity-twisted invariant multiplicity `m_sign=(1/|G|) sum sgn(g) Tr R(g)`;
- whether `m_sign != m_triv`.

## PASS

PASS for the adversarial sensitivity hypothesis iff at least one frozen causal class has a different invariant dimension after the exact parity twist. This proves that representation-level phase conventions can change the absolute fixed-space count, so physical promotion requires a source-fixed orientation/duality convention.

## FAIL

FAIL iff all three twisted invariant dimensions equal the original `2,3,5`.

## Interpretation ceiling

A PASS does not prove that the physical causal action actually carries the parity twist. It proves only convention sensitivity and therefore narrows the scope of Iter078O to its explicitly frozen slot-permutation representation unless the missing phase/duality convention is independently fixed. It does not affect the physical Iter077Q infinite-dimensional ambiguity result, define the causal-Toller refinement map, or establish any downstream physics.