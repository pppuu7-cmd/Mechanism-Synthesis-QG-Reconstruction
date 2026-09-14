# Iter078O adversarial orientation/duality phase-sensitivity control result

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078O_CRITIC_ORIENTATION_PHASE_SENSITIVITY.md`, commit `5d2a087ca5a3b989942f1afb36a861f8c187f796`.
- Implementation: `distributional/iter078o_critic_orientation_phase_sensitivity.py`, commit `12ef62cbe2ee31069cbfdc401b4389f205483591`.
- Production workflow head: commit `95bf30c90e18670a322f0e9713bb03fa9d30eb9d`.
- Terminal run: `34816976447`, status `completed`, conclusion `success`.
- Aggregate artifact: `10337275415`, digest `sha256:2e5fe0b792e89109e100955243067e3eec8552fa0a4a996a151ff0f4474165a3`.

## Frozen adversarial question

Starting from the exact Iter078O slot-permutation representation `R(pi)`, replace it by the exact parity-character twist

`R_sign(pi) = sgn(pi) R(pi)`

without changing tensors, causal stabilizers, or any other input. The preregistered adversarial hypothesis passes iff at least one causal class changes its invariant-space dimension.

## Exact terminal findings

The implementation reproduces the original Iter078O fixed dimensions exactly and the parity-twisted dimensions are identical in all three classes:

- `0<->5`, stabilizer size `120`: original `2`, parity-twisted `2`;
- `1<->4`, stabilizer size `24`: original `3`, parity-twisted `3`;
- `2<->3`, stabilizer size `12`: original `5`, parity-twisted `5`.

The run records `classes_with_changed_fixed_dimension=[]`, `original_dimensions_match_terminal_result=true`, and `execution_valid=true`.

## Control verdict

`FAIL` for the prospectively frozen adversarial sensitivity hypothesis.

Classification:

`ITER078O_CRITIC_PARITY_PHASE_TWIST_DOES_NOT_CHANGE_FROZEN_FIXED_COUNTS`

This is a **control verdict**, not a new mandatory Researcher-result review verdict.

## Scientific scope

The result rules out one explicit counterexample candidate: multiplying the frozen permutation representation by the sign character does not alter the exact `2,3,5` invariant-space counts.

It does **not** prove that every admissible orientation/edge-duality convention leaves those counts unchanged, and it does not establish that the frozen slot action is the physical causal-Toller graph action. Therefore it does not upgrade Iter078O from a scoped control into a physical symmetry theorem.

The original Iter078O interpretation ceiling remains unchanged: the symmetry calculation is confined to the frozen equal-spin labelled control representation; it neither selects a unique K5 extension nor reduces the Iter077Q infinite-dimensional tangential ambiguity to a unique physical functional.

## Effect on current CRQN chain

None. The controlling physical blockers remain the K5 function-space extension selector and the causal multivertex E3/E4/E6 inheritance bridges. No E7/E8, G3, RG, F9/G8/K5, regulator-independence, new-physics, or complete-QG promotion is authorized by this control.
