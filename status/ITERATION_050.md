# Iteration 050 — preregistration: K4 RR parameter sensitivity and pole-topology audit

**Date:** 2026-09-12
**Prerequisite:** Iter049 terminal `K4_RR_SELECTOR_NONCOVARIANT` with 48/48 valid lanes and exact-zero EPRL/no-contact controls.

## Scientific question
Iter049 rules out a universal graph/tree/pair-only selector for the residue-residue (`RR`) commutator: the same tree/pair changes RR status between held-out source cases. Which source-dependent ingredient controls that switch, and is the switch already explained by a discrete change in the upper/lower Feynman-pole count along the two ordered residue paths?

This file freezes the production matrix and interpretation **before implementation and before viewing Iter050 outputs**.

## Frozen kernel and algebra
Use the same exact K4 constrained-flow kernel, four tree/fundamental-cycle bases `S0,S1,P0,P1`, pairs `01,02,12`, and unchanged Iter048 `FP=R+A` channel algebra. `RR` is the exact commutator `R_j(R_i(K))-R_i(R_j(K))`. No finite-part coefficient, contour prescription, polynomial quotient handling, residue rule or control definition may be changed.

Each lane must also compute the ordinary EPRL/no-contact `F=1` control identically.

## Frozen held-out baseline
The following point was not used in Iter046–049 production:

- `gamma = 1.07`
- `epsilon = 0.085`
- causal signs `++++++`
- external K4 flow `k=(0.23,-0.34,0.18,-0.07)` (exact sum zero)

## Frozen one-factor-at-a-time conditions
Each condition changes only the named ingredient relative to the baseline.

1. `BASE`: `(gamma,epsilon,signs,k)=(1.07,0.085,++++++,(0.23,-0.34,0.18,-0.07))`
2. `G_LO`: `gamma=0.61`
3. `G_HI`: `gamma=1.61`
4. `E_LO`: `epsilon=0.035`
5. `E_HI`: `epsilon=0.16`
6. `S_ALT1`: signs `+-+-+-` (factorized K4 causal sign pattern)
7. `S_ALT2`: signs `--++--` (independent factorized K4 causal sign pattern)
8. `K_ALT1`: `k=(-0.17,0.29,-0.33,0.21)`
9. `K_ALT2`: `k=(0.31,0.14,-0.26,-0.19)`

All unspecified parameters remain exactly at BASE. Total frozen matrix: `9 conditions × 4 trees × 3 pairs = 108 lanes`, `fail-fast:false`.

## Mandatory per-lane outputs
For source and control record exactly:

- total pairwise FP commutator zero/nonzero;
- `RR/RA/AR/AA` exact zero/nonzero and degrees;
- exact reconstruction identities;
- first-stage `R+A` metadata for `i->j` and `j->i`;
- the second-stage `R`-after-`R` metadata for both orderings;
- for those four residue stages: total pole count and upper-half-plane pole count.

Define the ordered residue-count signatures

- `sig_ij = (upper_count(R_i on K), upper_count(R_j on R_i(K)))`
- `sig_ji = (upper_count(R_j on K), upper_count(R_i on R_j(K)))`.

Define `pole_count_asymmetry = (sig_ij != sig_ji)`.

This is only a coarse pole-topology diagnostic. Equality of pole counts does not imply equality of residues.

## Mandatory validity gates
A lane is valid only if:
1. every one-dimensional `R+A` recombination equals the unchanged frozen `finite_part_1d` exactly;
2. ordered channel sums and total channel commutator reconstruction are exact;
3. EPRL/no-contact total commutator is exactly zero;
4. all EPRL/no-contact channel commutators are recorded explicitly;
5. no unexpected real-axis or nonlinear pole enters the frozen contour classifier.

Any failure => `ITER050_CONTROL_OR_RECONSTRUCTION_INVALID`.

## Frozen aggregate diagnostics
For each of the 12 `(tree,pair)` positions, compare every non-BASE condition to BASE and count exact RR on/off transitions. Aggregate separately for factor families:

- `gamma`: G_LO/G_HI;
- `epsilon`: E_LO/E_HI;
- `signs`: S_ALT1/S_ALT2;
- `k`: K_ALT1/K_ALT2.

Also construct the exact 2×2 contingency table `RR nonzero` versus `pole_count_asymmetry` across all 108 source lanes.

## Frozen classifier
1. `ITER050_CONTROL_OR_RECONSTRUCTION_INVALID` if any mandatory validity gate fails.
2. `K4_RR_PARAMETER_STABLE_ON_FROZEN_GRID` if no non-BASE condition changes any of the 12 RR statuses relative to BASE.
3. `K4_RR_FACTOR_DEPENDENT_WITH_POLE_COUNT_SELECTOR` if at least one factor causes an RR transition and `RR_nonzero == pole_count_asymmetry` for all 108 source lanes.
4. `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT` if at least one factor causes an RR transition but the coarse pole-count selector is not exact.

The aggregate must report transition counts by factor family and condition, baseline/condition RR masks, and the full contingency table. No post-hoc feature selection is allowed in Iter050.

## Interpretation lock
Iter050 can establish which frozen source-factor changes are capable of switching the diagnostic RR channel and whether a simple discrete pole-count change is sufficient. It cannot establish a unique physical multivariate extension. If the result is `BEYOND_POLE_COUNT`, the next gate must inspect exact pole/residue geometry or algebraic cancellation prospectively, not fit a selector to the observed labels.

K5 remains BLOCKED. No physical causal-vertex finiteness/divergence, G3 PASS, F9, G8 or new-QG claim is authorized by this gate.
