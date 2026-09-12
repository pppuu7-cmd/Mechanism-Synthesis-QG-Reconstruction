# Iteration 050 — terminal result

**Date:** 2026-09-12

## Frozen gate

Prospectively preregistered one-factor-at-a-time K4 RR sensitivity audit on a new held-out baseline, using the unchanged Iter048 `FP=R+A` algebra and exact EPRL/no-contact controls.

Matrix: 9 conditions × 4 trees × 3 pairs = **108 lanes**.

## Authoritative provenance

- implementation/main commit: `410ab8e2c1f2bb1f3f13f3129ee9eeaec730a0eb`
- workflow run: `34710540567`
- aggregate job: `103601174984`
- aggregate artifact: `iter050-aggregate`
- artifact ID: `10303507511`
- artifact digest: `sha256:709001c7a5cf5058a9c64ce3d80da8b0322e7ff9d69ed97326f41afb10acb468`

## Terminal machine result

Classification: **`K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`**.

Validity:
- lanes: `108/108`
- all lane reconstructions valid: `true`
- all EPRL/no-contact control totals exactly zero: `true`
- all EPRL/no-contact control channel commutators exactly zero: `true`

The coarse predicate `RR_nonzero == pole_count_asymmetry` is **not** exact. Frozen contingency:

- `RR=1, pole-asym=1`: 24
- `RR=1, pole-asym=0`: 16
- `RR=0, pole-asym=1`: 30
- `RR=0, pole-asym=0`: 38

## Factor localization

Hamming transitions of the 12-bit `(tree,pair)` RR mask relative to BASE, summed over each factor family's two OAT perturbations:

- `gamma`: **0**
- `epsilon`: **0**
- causal signs: **10**
- external flow `k`: **0**

Thus on this frozen grid only the factorized causal-sign perturbations changed the RR mask. This is a localization result, not a universality theorem.

BASE RR mask has four nonzero positions:

- `S0/01`
- `P1/01`
- `P1/02`
- `P1/12`

`S_ALT1` changes five positions relative to BASE; `S_ALT2` changes five positions. Both gamma perturbations, both epsilon perturbations and both k perturbations reproduce the BASE mask exactly.

## Scientific interpretation

The Iter048 RR subset is not controlled by a universal graph/tree/pair label and is not explained by simple upper-pole-count asymmetry. Over the prospectively frozen Iter050 grid, the observable switch is localized to the causal-sign sector. Therefore the next admissible work is an exhaustive factorized causal-sign validation plus a prospectively fixed residue/cancellation audit.

This result concerns the sequential K4 finite-part diagnostic only. It does not define a physical multivariate causal amplitude, prove physical divergence/finiteness, authorize K5, or promote G3, F9 or G8.
