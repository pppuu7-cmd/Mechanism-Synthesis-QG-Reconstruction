# Iteration 066A preregistration — multivariate source-framework qualification

Date: 2026-09-13

## Purpose

Qualify whether any currently identified external mathematical/source framework is already sufficient to remove the Iter065A K5 blocker **without importing a post-hoc prescription**.

This is a source/math-object qualification gate, not a causal-vertex finiteness test and not a numerical K5 amplitude calculation.

## Frozen candidate frameworks

Four independently audited candidates:

1. `BCG2026_PRIMARY` — Bianchi–Chen–Gamonal causal spinfoam vertex, arXiv:2601.23162.
2. `BBK2009_WONDERFUL_EG` — Bergbauer–Brunetti–Kreimer, analytic regularization / wonderful models / Epstein–Glaser extension, arXiv:0908.0633.
3. `FELDER_KAZHDAN2018_FINITE_PART` — regularization dependence of finite parts on singular submanifolds, DOI 10.1007/s00029-017-0323-9.
4. `SELLIER1997_MULTIDIM_HFP` — multidimensional Hadamard finite part, change of variables and Fubini properties, DOI 10.1017/S030500419600148X.

## Frozen qualification predicates

A candidate counts as a complete bridge only if the source itself supplies all of:

- `P1_CORRELATED_MULTIVARIATE`: a genuinely multivariate correlated extension/regularization applicable to intersecting singular sets, not a sequential one-dimensional rule;
- `P2_SOURCE_SELECTED_UNIQUE`: a unique physical/source-selected extension for the present problem, without arbitrary counterterm coefficients, preferred tree/order, or an externally chosen subtraction scheme;
- `P3_ORDER_PERMUTATION_INDEPENDENT`: a stated theorem/prescription sufficient to guarantee the required regulator/integration-order and permutation/tree/cycle independence for the extension object;
- `P4_TOLLER_EPRL_COMPATIBLE`: an explicit derivation/equality tying the extension to the Bianchi–Chen–Gamonal spectral i-epsilon Toller prescription and preserving the Eq.(5)/(6) independent-wedge EPRL control at distributional level.

No criterion may be weakened after inspection of results.

## Frozen outputs

- If any one candidate satisfies P1–P4: `ITER066A_SOURCE_FRAMEWORK_BRIDGE_FOUND` and that candidate alone may seed a separately preregistered K5 construction gate.
- If no candidate satisfies P1–P4 but at least one supplies P1 and useful structural machinery: `ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING`.
- If no candidate even supplies a relevant P1-level multivariate framework: `ITER066A_NO_RELEVANT_MULTIVARIATE_FRAMEWORK_IDENTIFIED`.
- Parsing/source-access failure is `INFRASTRUCTURE_OR_SOURCE_ACQUISITION_FAIL`, never scientific FAIL.

## Scope locks

Even `SOURCE_FRAMEWORK_BRIDGE_FOUND` would not prove causal-vertex finiteness, F9, G3, G8, or new physics. Generic Epstein–Glaser/Hadamard machinery must not be silently identified with the physical Toller prescription. The published spectral `i epsilon` is not to be replaced by `beta+i*epsilon` or any fitted regulator.
