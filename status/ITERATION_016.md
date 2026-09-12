# Iteration 016 — j=l Toller residue-series validation

Status: **PASS / COMPLETED**

## Question
Can the diagonal gamma-simple reduced Toller branches `t+` and `t-` be evaluated for `j=l` by the exponentially weighted 2F1 power/residue series, avoiding the integer-degenerate analytic-continuation path, while reproducing the independent general Toller evaluator?

## GitHub campaign
Four independent gamma streams:
- gamma = 0.2
- gamma = 0.5
- gamma = 1.2
- gamma = 2.0

Per gamma: 84 `(j,m,beta)` cases with `j=1/2,1,3/2,2`, every allowed `m`, and beta in `{0.03,0.05,0.1,0.3,0.7,1.5}`.

## Result
All four streams passed. Across 336 cases:
- series non-convergences: **0**
- worst branch relative error: approximately **1.29e-64**
- worst additive error across the four gamma streams: approximately **1.40e-57**
- maximum residue/power-series terms: **2740**
- hardest point: beta = 0.03

The original run failed only because the *control* closed-form implementation was invoked without the already-established stable symmetric-limit wrapper for integer `c-a-b`; the residue series itself was not the source of that failure. After routing the control through `run_with_stable_hyp2f1.py`, all four jobs passed.

## Verdict
`J_EQUAL_L_RESIDUE_SERIES_MATCHES_GENERAL_TOLLER`

This closes the diagonal pure-boost numerical kernel. It does **not** close the causal vertex: a full vertex still needs reconstruction of `T(g)` for general Lorentz elements, ten correlated wedge factors, boundary magnetic/intertwiner contractions, and four gauge-fixed `SL(2,C)` integrations.
