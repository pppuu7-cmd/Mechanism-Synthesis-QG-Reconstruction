# Iteration 004 — Causal Cylindrical Intertwining / F9 campaign

**Date:** 2026-09-12  
**GitHub Actions run:** `34653104048` (`MSQGR Parallel Research`, run #2)  
**Run conclusion:** `success`  
**Task completion:** **100%**.

## Campaign

Eleven parallel research jobs plus the aggregate verdict completed successfully.

New F9-focused streams tested:

- finite-scale Causal Cylindrical Intertwining (CCI);
- multiscale causal leakage over repeated random RG maps;
- exact linear codimension of the CCI/CARC constraint;
- fail-closed F9 promotion ledger;
- existing architecture, novelty and negative controls.

## CCI is independent of ordinary cylindrical consistency

The executable finite-boundary surrogate enforces

`iota_fc = iota_fm iota_mc`

exactly while adding a controlled cross-sector contamination `epsilon`.

The ordinary cylindrical residual remains zero, while the coarse-to-fine CCI residual is approximately

- `0` at `epsilon=0`;
- `2.828e-8` at `1e-8`;
- `2.828e-6` at `1e-6`;
- `2.828e-4` at `1e-4`;
- `2.828e-2` at `1e-2`;
- `2.828e-1` at `1e-1`.

Thus CCI is a genuinely additional condition, not a rewriting of cylindrical consistency.

## Repeated RG composition

For 400 random trials and 16 composed steps per leakage scale:

- exact block preservation (`epsilon=0`) keeps relative causal leakage exactly zero;
- microscopic cross-sector contamination accumulates under repeated composition;
- the final mean leakage scales approximately linearly with the injected violation in the sampled range.

Representative final means:

- `epsilon=1e-8`: `~5.10e-8`;
- `epsilon=1e-6`: `~5.10e-6`;
- `epsilon=1e-4`: `~5.10e-4`;
- `epsilon=1e-3`: `~5.10e-3`;
- `epsilon=1e-2`: `~5.09e-2`.

This is only a finite-dimensional surrogate, not a physical beta function.

## Constraint strength

For a generic complex linear map on

`H = H_+ direct-sum H_-`,

CCI/CARC eliminates the two cross blocks. The structural count is

`2 n_+ n_-`

complex conditions out of

`(n_+ + n_-)^2`

complex map entries. For equal sector dimensions this is exactly 50% of the generic linear map space.

Concrete spin-foam truncations can correlate parameters, so this count is not an independent-coupling count for EPRL.

## F9 verdict

The physical F9 gate remains

`F9_BLOCKED`.

Missing same-realization evidence includes:

- physical boundary Toller/Feynman projectors;
- dynamically justified embedding maps;
- physical cylindrical consistency;
- physical CCI residual;
- Toller pole/analytic closure after internal sums/integrals;
- absence of new independent cross-branch data;
- multi-step physical refinement control.

## Overall verdict

`CRQN_V0_2_F9_FORMULATED_NOT_PHYSICALLY_CLOSED`.

Iteration 005 moves from abstract +/- sector surrogates to the explicit gamma-simple Toller pole spectrum.
