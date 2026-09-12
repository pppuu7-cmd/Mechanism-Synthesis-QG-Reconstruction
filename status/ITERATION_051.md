# Iteration 051 — preregistration: exact K4 RR pole/residue geometry and cancellation audit

**Date:** 2026-09-12
**Prerequisites:** Iter050 terminal `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`; independent denominator control terminal `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`.

This file freezes the gate before implementation and before any Iter051 production output is viewed.

## Scientific question

Iter050 showed that causal-sign changes can switch the exact RR commutator while gamma, epsilon and external-flow OAT changes did not on the frozen grid; upper-pole counts are not an exact selector. Iter051 asks what exact residue geometry distinguishes RR-active and RR-inactive lanes without fitting a selector to the observed labels.

## Frozen object

Use the unchanged Iter050 K4 source kernel and unchanged `FP=R+A` algebra. No contour, finite-part coefficient, source factor, threshold, pole classifier, counterterm or preferred integration order may be changed.

Use the same 108 source lanes:

- conditions: `BASE,G_LO,G_HI,E_LO,E_HI,S_ALT1,S_ALT2,K_ALT1,K_ALT2`;
- trees: `S0,S1,P0,P1`;
- ordered pair labels: `01,02,12`.

Every lane must also compute the identical EPRL/no-contact F=1 control.

## Frozen exact diagnostics

For both orders `i→j` and `j→i`, record at the second R-after-R stage:

1. all exact denominator roots in the integration variable after polynomial division;
2. the exact imaginary-part sign used by the unchanged contour classifier;
3. the exact individual residue attached to each upper-half-plane root;
4. the exact sum of upper residues before multiplication by `2πi`;
5. the resulting exact RR ordered contribution.

After expressing both orderings in the same remaining cycle coordinate, compare prospectively defined objects only:

- `upper_count_equal`;
- `upper_root_multiset_equal` by exact symbolic equality after deterministic sorting/canonicalization;
- `upper_residue_multiset_equal` by exact symbolic equality after deterministic sorting/canonicalization;
- `upper_residue_sum_equal` by exact symbolic equality.

No new feature may be introduced after viewing production results.

## Frozen lane classes

A valid source lane is assigned exactly one class:

- `ORDERED_RESIDUE_DATA_IDENTICAL`: root and residue multisets are both exactly equal;
- `GEOMETRY_DIFFERS_BUT_SUM_CANCELS`: at least one multiset differs, but upper-residue sums are exactly equal, hence RR is zero;
- `GEOMETRY_DIFFERS_AND_SUM_DIFFERS`: at least one multiset differs and upper-residue sums differ, hence RR is nonzero;
- `ITER051_INTERNAL_INCONSISTENCY`: any logical mismatch, e.g. RR status disagrees with exact residue-sum equality.

These classes are diagnostics, not a fitted physical selector.

## Mandatory validity gates

Each lane is valid only if:

1. all unchanged Iter050 one-step `R+A=FP` recombinations are exact;
2. ordered/channel reconstruction is exact;
3. source RR zero/nonzero agrees exactly with equality/inequality of second-stage upper-residue sums;
4. EPRL/no-contact total and all channel commutators are exactly zero;
5. no unexpected real-axis or nonlinear pole enters the frozen pole classifier.

Any failure gives aggregate `ITER051_CONTROL_OR_RECONSTRUCTION_INVALID`.

## Frozen aggregate classifiers

After all 108 lanes:

1. `ITER051_CONTROL_OR_RECONSTRUCTION_INVALID` if any validity condition fails.
2. `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` if every RR-nonzero lane is `GEOMETRY_DIFFERS_AND_SUM_DIFFERS`, every RR-zero lane is either `ORDERED_RESIDUE_DATA_IDENTICAL` or `GEOMETRY_DIFFERS_BUT_SUM_CANCELS`, and all logical equivalences are exact.
3. `K4_RR_CANCELLATION_DOMINATED_SUBSET` if, in addition to validity, at least one RR-zero lane has different exact residue geometry but equal residue sum. This classifier is reported as an additional structural flag, not as a replacement for item 2.

The aggregate must report counts by condition/tree/pair and by lane class. No post-hoc residue invariant or selector fitting is allowed.

## Interpretation lock

A PASS only localizes the sequential K4 RR obstruction to exact ordered residue geometry/cancellation. It does not identify a unique source-selected multivariate extension and does not authorize a counterterm, preferred order, K5, physical causal-vertex finiteness/divergence, G3, F9 or G8.

If exact cancellation is widespread, the next admissible gate is a prospectively defined algebraic inclusion-exclusion/forest cancellation identity test. If RR-active lanes show exact residue-sum mismatch without a universal canonical invariant, the next gate is a source-analyticity-selected simultaneous multivariate extension audit, not selector fitting.
