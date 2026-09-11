# Iteration 006C — Toller oracle + working Lorentzian EPRL backend

**Date:** 2026-09-12  
**MSQGR Actions run:** `34655377819`  
**Physical sl2cfoam smoke run:** `34655377837`  
**Matrix result:** all research jobs completed and combined verdict published.  
**F9:** still `BLOCKED`.

## 1. Physical backend blocker removed

The corrected clean-runner `sl2cfoam-next` build completed successfully using sequential `make lib` then `make tools`.

A real minimal Lorentzian EPRL full tensor was then computed at

- `gamma = 1.2`;
- ten boundary spins `j = 1/2` (`two_j = 1`);
- shell cutoff `Dl = 0`.

The upstream log reports:

- 6j tensors: completed;
- booster tensors: completed in approximately `0.022 s`;
- amplitude assembly: completed;
- total reported vertex computation: approximately `0.022 s`.

Internal smoke verdict: `MINIMAL_LORENTZIAN_EPRL_VERTEX_COMPUTED`.

This removes the infrastructure question “can this repository drive a real Lorentzian EPRL backend on GitHub?” The answer is now yes.

## 2. Toller analytic oracle

The gamma-simple reference implementation was independently run on GitHub. Across its test grid,

`t_plus + t_minus = d`

was verified with worst relative residual

`1.4288035150476803e-69`.

Verdict: `TOLLER_REFERENCE_SUM_RULE_VERIFIED`.

## 3. Precision tier

Published `gamma=1.2, j=1.0, Dl=25` Delta_4 data remain the first baseline for a causal-projector prototype.

Power-tail modelling gives median estimated unresolved tails of approximately

- 1.91%;
- 0.83%;
- 1.15%

for the three published columns, with maximum fit-window spread approximately `4.72e-4`.

Therefore the run verdict is

`CRQN_V0_2_EPRL_PROJECTOR_PROTOTYPE_READY__PRECISION_F9_OPEN`.

Interpretation: the backend is adequate for an approximately 2% **prototype**, but not yet for a <1% quantitative F9 claim.

## 4. Important correction for the booster implementation

The causal vertex uses gamma-simple external representations, but the numerical EPRL booster decomposition calls reduced Wigner matrices with auxiliary `l >= j` when `Dl > 0`.

Therefore the diagonal closed form `t_{jjm}` alone is insufficient for a causal version of the existing booster algorithm. Iteration 007 must use the general Toller functions `t_{jlm}^{+/-}` and explicitly audit the phase convention against the existing `sl2cfoam_dsmall` implementation before modifying the integrator.

## 5. Next target

1. verify the general EPRL-relevant `j -> l` Toller sum rule;
2. quantify branch-cancellation conditioning;
3. probe upstream `sl2cfoam_dsmall` pointwise;
4. infer the exact Ruhl-to-sl2cfoam phase map;
5. only then implement causal reduced-matrix / booster branches.

No item above by itself grants physical F9 or novelty credit.
