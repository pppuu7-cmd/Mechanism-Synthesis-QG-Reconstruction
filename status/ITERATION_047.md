# Iteration 047 — exact K4 finite-part commutator localization

**Date:** 2026-09-12
**Prerequisite:** Iter046 terminal `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT` with valid exact EPRL/no-contact controls.

## Scientific question

Does the K4 order dependence already appear as noncommutativity of pairs of the unchanged Iter045 one-dimensional finite-part operators, before the third cycle integration? If so, which cycle-basis/pair sectors carry the obstruction?

This is a localization/diagnostic gate. It does not itself define a new multivariate amplitude.

## Frozen source objects

Exactly the same two K4 cases as Iter046:

- Case A: `gamma=0.83`, `epsilon=0.06`, signs `++++++`, external flow `0.19,-0.31,0.27,-0.15`.
- Case B: `gamma=1.43`, `epsilon=0.12`, signs `-++-++`, external flow `-0.22,0.37,-0.28,0.13`.

Exactly the same four cycle bases: `S0,S1,P0,P1`.

Exactly the same `finite_part_1d` operator as Iter045/046; no coefficient, contour, subtraction or residue rule may be changed.

For each case and tree, test the three unordered cycle-coordinate pairs `01,02,12`. For pair `ij`, compute exactly

`C_ij = FP_j(FP_i(K)) - FP_i(FP_j(K))`

as a rational/symbolic function of the remaining cycle variable.

The ordinary no-contact `F=1` EPRL control is computed identically in every lane.

Total frozen lanes: `2 cases x 4 trees x 3 pairs = 24` with `fail-fast:false`.

## Frozen validity and classification rules

Per lane:

- `source_commutator_zero` iff exact symbolic cancellation gives `C_ij == 0`.
- `control_commutator_zero` iff exact symbolic cancellation gives zero for the EPRL/no-contact control.
- no numerical tolerance can turn a symbolic nonzero into zero.

Aggregate classifier:

1. If any EPRL/no-contact control commutator is nonzero: `K4_FP_COMMUTATOR_CONTROL_INVALID`.
2. Else if all 24 source commutators are exactly zero: `K4_PAIRWISE_FP_COMMUTATORS_ZERO`.
3. Else: `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`.

The aggregate must report the nonzero lane set separately for Cases A and B, plus exact numerator/denominator degrees in the remaining variable wherever defined.

## Interpretation lock

A source nonzero with exact-zero controls localizes failure of the **sequential 1D extension algebra**. It does not imply physical divergence. It does not authorize a preferred integration order, a counterterm, K5, G3, F9 or G8.

If pairwise commutators are nonzero, the next gate must localize them into overlapping polynomial/contact subtraction pieces and derive/preregister a genuinely multivariate forest/inclusion-exclusion candidate before testing covariance. If all pairwise commutators vanish despite Iter046 order dependence, the next gate must instead isolate cycle-basis/coordinate-change covariance as the obstruction.
