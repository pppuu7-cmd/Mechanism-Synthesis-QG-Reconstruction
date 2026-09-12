# Iteration 017 — general gamma-simple reduced Toller residue kernel

Status: **PASS / COMPLETED**

## Question
Does the residue/power-series evaluation remain equivalent to the independent closed-form Toller implementation away from the diagonal, for `k=j` and `l=j,j+1,j+2`?

## GitHub campaign
Four independent gamma streams: `0.2, 0.5, 1.2, 2.0`.

Per gamma: **252** `(j,l,m,beta)` cases; total **1008** cases. Spins `j=1/2..2`, all allowed magnetic indices, `l=j,j+1,j+2`, beta in `{0.03,0.05,0.1,0.3,0.7,1.5}`.

## Result
All 4/4 streams passed:
- series non-convergences: **0 / 1008**
- worst branch relative error across all streams: approximately **1.32e-61**
- worst additive relative error: approximately **2.64e-47**
- maximum number of series terms: **2739**

Worst branch errors stay at the same ~1e-61 scale for all three shells:
- `l=j`: ~1.28e-61
- `l=j+1`: ~1.30e-61
- `l=j+2`: ~1.32e-61

The hardest sampled point is `j=2, l=4, m=2, beta=0.03` in ordinary-spin notation (`two_j=4, two_l=8, two_m=4`).

## Verdict
`GENERAL_RESIDUE_SERIES_MATCHES_TOLLER`

The stable reduced pure-boost branch kernel is therefore available on the current small-spin carrier. The next bottleneck is no longer the branch evaluator. It is assembly and integration of the direct causal vertex using the Cartan reconstruction of a general Toller matrix,

`T(g) = D(U1) t(beta) D(U2)`, with `g = U1 exp(beta sigma_z/2) U2`,

and the correlated ten-wedge causal structure `kappa_ab = sigma_a sigma_b`.
