# Iteration 051A — preregistration: exhaustive factorized causal-sign RR census

**Date:** 2026-09-12

## Motivation

Iter050 terminally classified the frozen K4 RR diagnostic as `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`: on its one-factor-at-a-time grid, changing `gamma`, finite spectral `epsilon`, or external K4 flow `k` changed no RR mask, while the two causal-sign perturbations produced 10 total mask transitions. The independently response-blind denominator-only control was valid and stable across its epsilon/k nuisance variations. The next admissible test is therefore an exhaustive factorized causal-sign census on new nuisance points, not a fitted selector.

This file freezes the gate before Iter051A implementation or production output.

## Frozen causal-sign classes

Use vertex orientation variables

`sigma = (+1, sigma1, sigma2, sigma3)`, `sigma_i in {+1,-1}`,

fixing the irrelevant global vertex-sign flip. For each K4 edge `(a,b)`, use the source-backed factorized sign

`kappa_ab = sigma_a sigma_b`.

Enumerate all eight classes, labelled by `(sigma1,sigma2,sigma3)`:

`+++`, `++-`, `+-+`, `+--`, `-++`, `-+-`, `--+`, `---`.

No arbitrary six-edge sign pattern is admitted.

## Frozen held-out nuisance points

These values were not used in Iter050 production and are fixed before viewing Iter051A outputs:

- `H1`: `gamma=0.74`, `epsilon=0.052`, `k=(0.27,-0.18,-0.24,0.15)`.
- `H2`: `gamma=1.32`, `epsilon=0.117`, `k=(-0.13,0.26,-0.38,0.25)`.

Both external flows sum exactly to zero. The same unchanged j=1/2 source kernel and unchanged Iter048 `FP=R+A` diagnostic algebra are used.

## Frozen matrix

For every held-out point, sign class, spanning-tree/fundamental-cycle basis and unordered cycle pair:

- nuisance points: 2 (`H1`,`H2`)
- sign classes: 8
- trees: 4 (`S0`,`S1`,`P0`,`P1`)
- pairs: 3 (`01`,`02`,`12`)

Total: **192 independent lanes**, `fail-fast:false`.

Each lane computes source and ordinary EPRL/no-contact `F=1` control using the unchanged channel decomposition. Record exact RR zero/nonzero status and the RA/AR/AA statuses; no numerical threshold may turn a symbolic nonzero into zero.

## Mandatory validity gates

A lane is scientifically valid only if:

1. each one-dimensional `R+A` recombination equals the frozen finite-part result exactly;
2. ordered four-channel sums reconstruct the frozen two-step result exactly;
3. channel commutators reconstruct the full commutator exactly;
4. the ordinary EPRL/no-contact control total commutator is exactly zero;
5. every control channel commutator is exactly zero;
6. the six edge signs stored in the artifact exactly equal `sigma_a sigma_b` for the declared class.

Any failure => `ITER051A_CONTROL_OR_RECONSTRUCTION_INVALID`.

## Frozen classifier

For each sign class form the 12-bit RR mask over `(tree,pair)` separately at H1 and H2.

- `K4_RR_SIGN_CLASS_NUISANCE_STABLE` iff all 192 lanes are valid and every one of the eight H1 masks is exactly identical to the corresponding H2 mask.
- `K4_RR_SIGN_CLASS_NUISANCE_DEPENDENT` iff all lanes are valid but at least one class changes at one or more `(tree,pair)` positions between H1 and H2.
- `ITER051A_CONTROL_OR_RECONSTRUCTION_INVALID` otherwise.

The aggregate must report every class mask, RR count, H1/H2 Hamming distance, and all changed positions. No clustering, threshold fitting or post-hoc redefinition is allowed.

## Interpretation lock

A nuisance-stable eight-class census would establish only that the RR pattern of this sequential diagnostic is controlled primarily by the factorized causal-sign sector over the tested source points. It would not identify the algebraic mechanism and would not define a physical multivariate amplitude. A nuisance-dependent result would instead show that the apparent sign control is incomplete.

No outcome authorizes a preferred integration order, arbitrary finite counterterm, K5, G3 PASS, physical F9, G8 novelty, or a new quantum-gravity theory.
