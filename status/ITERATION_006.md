# Iteration 006 — Published Lorentzian EPRL backend audit

**Date:** 2026-09-12  
**GitHub Actions run:** `34654476402`  
**Task completion:** **100%** for the published-data reproducibility/cutoff audit.  
**Physical F9:** still `BLOCKED`.

## Run result

All **15/15** research matrix jobs plus the aggregate job completed successfully.

The new physical-backend stream parsed published `HowToSpinFoamAmplitude` Delta_4 data produced with `sl2cfoam-next` and verified that the gamma=1.2, j=1.0 `maxDl=15` data are an exact numerical prefix of the `maxDl=25` data:

- maximum absolute prefix difference: `0.0`;
- maximum relative prefix difference: `0.0`;
- verdict: `PREFIX_IDENTICAL`.

## Observed shell convergence

For the deepest published gamma=1.2, j=1.0 series at `Dl=25`, the final shell-to-shell relative changes are approximately:

- column 0: `1.407e-3` (0.1407%);
- column 1: `6.488e-4` (0.0649%);
- column 2: `8.775e-4` (0.0878%).

The four-point relative spans at the same cutoff are approximately 0.476%, 0.220% and 0.297% respectively.

These numbers make the gamma=1.2, j=1.0, Dl=25 dataset a defensible **computational baseline** for the first causal-projector prototype. This is a numerical planning choice, not a claim that gamma=1.2 is physically preferred.

## What this closes

The project no longer needs to guess whether the published Lorentzian EPRL backend is internally reproducible at overlapping cutoffs. It is.

## What remains open

This iteration gives **zero F9 credit** because the published amplitudes do not contain the causal Toller/Feynman projector. The decisive object remains

`P_b'^∓ iota_b'b P_b^±`

for a dynamically justified boundary/refinement map extracted from the same Lorentzian realization.

## Iteration 006b

The next campaign adds:

1. an automatic observed-stability cutoff selector;
2. a back-test of cheap tail extrapolators against the deepest published series;
3. exponential-vs-power-law tail model comparison;
4. a fail-closed backend readiness gate;
5. an independent clean-runner `sl2cfoam-next` source-build and shell-0 vertex smoke calculation.

Only after these backend controls are passed should expensive Toller-projected EPRL calculations be scaled up.
