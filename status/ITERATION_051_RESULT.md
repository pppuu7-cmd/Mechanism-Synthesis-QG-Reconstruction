# Iteration 051 — terminal result: exact K4 RR residue-geometry separation

**Date:** 2026-09-12

## Authoritative production

- workflow run: `34712814029`
- implementation head: `e668862616cf898ad269d49a55b0c40a83efe720`
- aggregate artifact: `10304298594` (`iter051-aggregate`)
- artifact digest: `sha256:68a2c96e7150950138f199219ea44fda17d7fca12f264961143586469316bcc1`
- frozen matrix: 9 conditions × 4 trees × 3 pairs = **108 lanes**

## Frozen classification

`K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION`

Additional structural flag:

`K4_RR_CANCELLATION_DOMINATED_SUBSET`

All 108/108 lanes are valid under the preregistered reconstruction/control gates. Exact lane counts are:

- `ORDERED_RESIDUE_DATA_IDENTICAL`: **37**
- `GEOMETRY_DIFFERS_BUT_SUM_CANCELS`: **31**
- `GEOMETRY_DIFFERS_AND_SUM_DIFFERS`: **40**
- `ITER051_INTERNAL_INCONSISTENCY`: **0**

The source RR commutator is nonzero in exactly **40/108** lanes, and every one of those 40 lanes is `GEOMETRY_DIFFERS_AND_SUM_DIFFERS`. Conversely, 31 RR-zero lanes have different exact ordered residue geometry while the selected upper-residue sums cancel exactly.

The BASE, gamma, epsilon and external-flow OAT conditions each have 4 RR-active lanes and class split `4 identical / 4 geometry-different-but-cancelling / 4 geometry-different-and-sum-different`. The two causal-sign conditions change this structure: `S_ALT1` has `6 / 1 / 5`, while `S_ALT2` has `3 / 2 / 7` across the same three non-error classes.

## Scientific interpretation

Within the unchanged sequential K4 finite-part diagnostic, the RR obstruction is localized more sharply than in Iter050: it is selected exactly by **ordered upper-residue-sum mismatch** on the frozen grid, not by upper-pole cardinality alone. The existence of 31 geometry-different yet exactly cancelling RR-zero lanes demonstrates that different pole/residue geometry is not sufficient; exact cancellation structure matters.

This is not yet a physical multivariate K4 extension and is not a finiteness/divergence theorem. It does not authorize a preferred sequential integration order or a finite counterterm.

## Next permitted gate

Because exact cancellation is widespread, the preregistered continuation allowed by Iter051 is an algebraic inclusion-exclusion/forest-cancellation identity test with coefficients fixed before implementation. Any structural identity found on this 108-lane matrix must later survive an independent held-out validation before receiving physical or model-building weight.

K5 remains `BLOCKED`; G3 remains `OPEN`; physical F9 remains `BLOCKED`; G8 remains `BLOCKED_CONVERGENCE_ONLY`.
