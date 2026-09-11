# Iteration 005 — Explicit gamma-simple Toller pole campaign

**Date:** 2026-09-12  
**GitHub Actions run:** `34653540503` (`MSQGR Parallel Research`, run #3)  
**Run conclusion:** `success`  
**Parallel streams:** **14/14 success + aggregate success**  
**Task completion:** **100%**.

## Exact gamma-simple pole-lattice control

For gamma-simple Toller poles

`omega_n^± = ∓ gamma j - i(2n+j±m+1)`,

raw multiplication of two same-branch modes at fixed nonzero gamma can match one coarse gamma-simple pole only if

`N = n1+n2+1/2`.

The GitHub exact-arithmetic scan tested **2,294,082** configurations over the declared spin/radial ranges and found

`exact_integer_N_matches = 0`.

Verdict:

`NO_NAIVE_SAME_BRANCH_GAMMA_SIMPLE_POLE_CLOSURE`.

This is an exact negative control for a naive single-mode blocking ansatz, not a no-go theorem for full causal EPRL coarse graining.

## CCI hierarchy preserved

The independent taxonomy stream confirmed

`CCI_STRICTLY_WEAKER_THAN_SINGLE_LABEL_CLOSURE`.

A boundary map can map one basis pole mode to a superposition of several modes in the **same causal sector** and still satisfy CCI. Therefore failure of single-pole closure does not falsify the physical F9 programme.

## Gamma-flow topology diagnostic

For gamma-simple poles and `j>0`,

`Re omega_n^+ = -gamma j`,

`Re omega_n^- = +gamma j`.

Thus `gamma=0` is a degeneracy surface for causal labels defined by the sign of boost frequency. This is a labeling/topology warning only; no physical beta_gamma for causal EPRL has been derived here.

## Aggregate verdict

`CRQN_V0_2_TOLLER_STRUCTURE_SHARPENED__PHYSICAL_F9_OPEN`.

The established CRQN feature set is still covered by source-family union, so G8 remains blocked. F9 also remains fail-closed BLOCKED.

## Next step

Move from analytic structural controls to a real Lorentzian EPRL computational backend and ultimately evaluate

`P_b'^∓ iota_b'b P_b^±`

on a dynamically justified boundary map after internal sums/recoupling, with cutoff/convergence control.
