# Iter079G-SM — E4 parent face/edge weight inheritance audit

Status: PROSPECTIVELY PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-14

## Question
Can E4 (face/edge weights, internal sums and normalization) be promoted from `missing` to an inherited object when the generalized causal construction is interpreted as replacing only the **local EPRL-KKL vertex amplitude**, leaving the parent state-sum measure/weights unchanged?

This gate separates two statements that must not be conflated:
1. a conditional algebraic inheritance theorem if the parent weights are fixed by hypothesis;
2. a source-authority question: does the primary causal construction actually state or derive that full-state-sum inheritance?

## Frozen source facts
1. Beltran 2026 explicitly frames the work as extending causal studies to the EPRL-KKL model and introduces generalized **causal vertex amplitudes** on arbitrary 2-complexes.
2. In the frozen source audit, no explicit full causal partition function/state-sum formula with inherited face amplitude, edge amplitude, internal spin/intertwiner sums and normalization has yet been identified.
3. The parent EPRL-KKL framework supplies a state-sum/composition skeleton and its own non-vertex weights/normalizations.
4. Iter079C proved that local causal vertex data plus the combinatorial skeleton alone do not uniquely determine E4 absent an inheritance/normalization rule.

## Frozen lanes
### Lane A — primary-source authority
Record separately whether the source explicitly provides: causal vertex replacement; full causal state sum; face weights; edge weights; internal spin/intertwiner sums; normalization/inheritance statement.

### Lane B — exact conditional inheritance algebra
Represent a parent state-sum term as `W_F * W_E * S_internal * N * product_v A_v`. Replace only `A_v -> C_v`, keeping all other factors fixed. Verify exactly that E4 data are unchanged by the local replacement for arbitrary vertex count `N_v`.

### Lane C — adversarial reweighting control
Introduce an independent non-unit factor `lambda` into any one E4 factor. Verify that the full amplitude changes generically while local causal vertex factors are unchanged. This proves that E4 is not determined by local vertex data alone.

### Lane D — frozen classification/scope
PASS as **physical/source-explicit E4 inheritance** only if Lane A records an explicit primary-source inheritance/full-state-sum statement and B/C pass.

If B/C pass but Lane A lacks that source statement, classify only:
`ITER079G_SM_E4_PARENT_WEIGHTS_CONDITIONALLY_INHERIT_UNDER_VERTEX_ONLY_REPLACEMENT_BUT_SOURCE_BRIDGE_NOT_EXPLICIT_EXACT_SCOPED`

If the conditional algebra fails:
`ITER079G_SM_E4_PARENT_WEIGHT_INHERITANCE_FAILS_UNDER_FROZEN_VERTEX_ONLY_REPLACEMENT`

## Claim locks
No arbitrary choice of face/edge weights; no physical E4 promotion from a merely conditional theorem; no E3/E6/E7/E8 promotion; no G3/F9/G8/K5 or RG promotion; no complete-QG claim; no `NEW_PHYSICS_FOUND`.
