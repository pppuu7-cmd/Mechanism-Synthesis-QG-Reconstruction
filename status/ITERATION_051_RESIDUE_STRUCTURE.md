# Iteration 051B — preregistration: exact residue-zero/cancellation structure audit

**Date:** 2026-09-12

## Motivation

Iter050 terminally rejected the coarse upper-half-plane pole-count asymmetry as an exact RR selector. RR changed under causal-sign perturbations, while gamma/epsilon/k perturbations on the frozen grid did not; the independent denominator-only control also showed stable pole topology under its epsilon/k nuisance variations. The next response-blind question is whether RR is selected by a prospectively fixed set of exact residue-zero/cancellation structures rather than by pole counts alone.

This file freezes the diagnostic list and classifier before implementation or Iter051B production output.

## Frozen source grid

Use all eight factorized K4 causal-sign classes generated from

`sigma=(+1,sigma1,sigma2,sigma3)`, `kappa_ab=sigma_a sigma_b`,

with class labels `+++`, `++-`, `+-+`, `+--`, `-++`, `-+-`, `--+`, `---`.

Use one new held-out nuisance point not used by Iter050/Iter051A:

- `H3`: `gamma=1.78`, `epsilon=0.071`, `k=(0.11,0.33,-0.29,-0.15)`.

The external flow sums exactly to zero.

Matrix: 8 sign classes × 4 trees (`S0,S1,P0,P1`) × 3 unordered cycle pairs (`01,02,12`) = **96 independent lanes**, `fail-fast:false`.

## Frozen algebra

Do not change the Iter048 finite-part rule. For a one-variable rational expression after the same polynomial quotient subtraction, define only the already-existing residue component

`R_u = 2*pi*i*sum(upper-half-plane residues)`.

For each ordered pair `i->j`, compute the exact first R step and the exact second R step. The resulting ordered `RR_ij` must be symbolically identical to the RR channel returned by the frozen `ordered_channels` implementation. Repeat for `j->i`.

No new finite part, contour, counterterm, pole prescription, branch rule or tolerance is introduced.

## Prospectively frozen residue diagnostics

At each R step record exactly:

- total simple pole count;
- upper-half-plane pole count;
- number of selected upper residues that are symbolically nonzero;
- whether the selected upper-residue sum is exactly zero;
- whether internal cancellation occurs (`nonzero_residue_count > 0` but total selected residue sum is exactly zero).

From the two ordered paths form the following **fixed booleans only**:

1. `first_upper_count_asymmetry`;
2. `second_upper_count_asymmetry`;
3. `first_nonzero_residue_count_asymmetry`;
4. `second_nonzero_residue_count_asymmetry`;
5. `first_residue_sum_zero_asymmetry`;
6. `second_residue_sum_zero_asymmetry`;
7. `internal_cancellation_asymmetry`;
8. `combined_discrete_residue_signature_asymmetry`, comparing the complete ordered tuple of the preceding discrete data.

No additional feature may be added after production output is inspected.

## Mandatory validity gates

Every lane must satisfy:

1. the diagnostic first/second R outputs reproduce the frozen source `RR_ij` and `RR_ji` exactly;
2. frozen source ordered/channel reconstructions are exact;
3. the same checks hold for the `F=1` control;
4. the control RR commutator is exactly zero;
5. declared edge signs exactly equal `sigma_a sigma_b`.

Any failure => `ITER051B_CONTROL_OR_RECONSTRUCTION_INVALID`.

## Frozen classifier

For each of the eight preregistered booleans compute the exact 2×2 contingency against source `RR_nonzero` across all 96 lanes.

A diagnostic boolean is an `exact_match` only if its truth value equals `RR_nonzero` on all 96 lanes and both truth values occur in the grid.

- `K4_RR_PREREG_RESIDUE_STRUCTURE_EXACT` iff at least one of the eight prospectively frozen booleans is an exact match and all validity gates pass. Report every exact-matching diagnostic; do not choose one post hoc by preference.
- `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE` iff all validity gates pass but none of the eight diagnostics is an exact match.
- `ITER051B_CONTROL_OR_RECONSTRUCTION_INVALID` otherwise.

## Interpretation lock

An exact match would localize the RR switch to a specific discrete residue/cancellation structure of this sequential diagnostic and would require independent held-out validation before receiving structural weight. Failure of all eight would force the next gate to inspect exact residue values/pole-location geometry rather than invent a fitted coarse selector.

Neither outcome defines the physical multivariate causal vertex, proves a divergence/finiteness theorem, authorizes K5, promotes G3/F9/G8, or establishes new quantum gravity.
