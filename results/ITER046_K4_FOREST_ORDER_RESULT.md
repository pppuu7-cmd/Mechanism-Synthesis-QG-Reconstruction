# Iteration 046 — K4 sequential finite-part forest/order result

**Date:** 2026-09-12

## Frozen object

Complete K4 edge-flow kernel with three independent cycle variables. The Iter045 one-dimensional polynomial-subtraction + residue/PV finite-part operator was applied sequentially **without retuning** across four spanning-tree/fundamental-cycle bases (`S0,S1,P0,P1`), all six integration orders, and two held-out source cases. Every lane included the ordinary EPRL/no-contact `F=1` control.

Frozen terminal classes were:

- `K4_FINITE_PART_FOREST_ORDER_COVARIANT`
- `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`
- `K4_CONTROL_INVALID`

## Provenance

Production run: `34703268212`

- workflow head: `0bffee79ca20e8b8f19746ec2ab734a27582333b`
- aggregate job: `103579503058`
- aggregate artifact: `10300791640`
- aggregate artifact SHA256: `8209ccc73c4eaee4f13340032b6f84041d7a1a148987e5950c867ecbbe771c2a`

Case-B infrastructure-only repair:

- run: `34703606792`
- repair head: `d9f1b29489dfe7a72e44e950da3374c1e956aee5`
- aggregate job: `103579919585`
- aggregate artifact: `10301246140`
- aggregate artifact SHA256: `a84727b8c9bd5b612bdeeceb41c6e7aea3509357d735b4cc0907236b57cbc388`

The original Case-B failures were technical serialization/import-path failures. Frozen physics, parameters, formulas and criteria were not changed by the repair.

## Terminal scientific classification

`K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`

### Case A

- 24/24 frozen lanes available.
- source exact equality: false.
- source relative spread: `0.09946564554779194`.
- EPRL control exact equality: true.
- EPRL control relative spread: `0.0`.
- maximum source witness difference: `1226.3990616650633`.

Witness: `P0/order102 = -9716.256671749351300744073 - 7395.661165068184248057705 i` versus `P0/order201 = -10378.91042569324932713423 - 6363.699605301053990249234 i`.

### Case B

After the minimal infrastructure repair, 24/24 frozen lanes are valid.

- source exact equality: false.
- source relative spread: `0.5903762046739115`.
- EPRL control exact equality: true.
- EPRL control relative spread: `0.0`.
- maximum source witness difference: `231.10329057111215`.

Witness: `P0/order210 = 148.3411417653609952967291 + 178.1028830014885424045242 i` versus `S0/order120 = 372.2794601126873799933901 + 121.0033165533324625781631 i`.

## Interpretation lock

This is a **scientific negative result for the naive sequential extension of the Iter045 one-dimensional finite-part rule to a multi-cycle K4 object**. The exactly invariant EPRL/no-contact control argues against a generic measure/integration implementation defect.

It is **not**:

- a physical causal-vertex divergence theorem;
- a proof that no correlated Feynman/distributional extension exists;
- a G3 PASS/FAIL;
- F9 evidence;
- G8 novelty evidence.

K5 is not authorized from this result. The next admissible route is a genuinely multivariate/correlated K4 construction. Before proposing any finite counterterm, first localize the obstruction through exact finite-part commutators and overlapping subtraction/contact structure. Any eventual finite term must be source/analyticity selected, never post-hoc tuned.
