# Iteration 011 — Branch-resolved Toller B4

## Status

`COMPLETED_DIAGNOSTIC / STANDARD_B4_FACTORIZATION_REJECTED_FOR_SEPARATE_BRANCHES`

## Question

Can the ordinary `sl2cfoam_b4_accurate` algorithm be reused branch-by-branch by replacing each reduced Wigner matrix with a fixed Toller branch `t+` or `t-`, integrating each magnetic sector separately, and summing the resulting branch B4 blocks afterward?

## Campaign

Five GitHub streams were run on the same small-spin sectors used by the additive validation:

- one ordinary complex-QAGP baseline;
- four shards covering all `2^4 = 16` four-leg Toller masks;
- full complex post-Speziale QAGP values were recorded before upstream's ordinary-EPRL `crealq` projection.

The upstream Lorentzian measure, adaptive QAGP plumbing, magnetic labels, recoupling conventions and Speziale phase were otherwise left unchanged.

## Result

All five compute jobs completed, but the aggregate gate did not close:

- the ordinary complex baseline was finite;
- all 16 separately integrated branch masks developed non-finite (`NaN`) complex entries in the `j=1/2, l=1/2` sector;
- QAGP return codes were not signaling ordinary integration failure (`max_nonzero_qagp_rcodes_per_mask_case = 0`);
- the separately recorded real-projected additive control still reconstructed the ordinary B4 matrix with worst stored relative error `0.0`.

Subsequent high-precision endpoint scans (Iteration 014) show that this is structural: individual Toller branches have endpoint poles while `t+ + t-` cancels them.

## Interpretation

This rejects the **algorithmic factorization**

`integrate each Toller branch in each magnetic p-sector -> recouple afterward`

as a valid generic realization of the causal amplitude on the ordinary real-axis EPRL B4 quadrature.

It does **not** reject the causal spin-foam vertex. The causal vertex is defined at the level of correlated Toller matrices with a Feynman `i epsilon` prescription. Interchanging the singular branch integration with later magnetic/vertex contractions is not justified by this test.

## Consequence

Do not repair this by:

- arbitrary endpoint clipping;
- increasing long-double precision alone;
- replacing non-finite branch values by zero;
- assigning independent finite B4 values to all 16 masks by hand.

The next valid routes are:

1. test whether recoupling before radial integration removes the singular leading terms; and/or
2. implement the causal amplitude using the actual Feynman `i epsilon` Toller prescription at a level where the correlated causal structure is retained.

## Gate impact

- additive `t+ + t- -> D` plumbing: `PASS`;
- separately finite branch B4 building blocks under standard EPRL integration order: `FAIL`;
- causal vertex itself: `OPEN_BLOCKED`, not falsified;
- G3 quantum dynamics: remains `OPEN_BLOCKED`;
- G8 novelty/nontriviality: remains `HIGH_RISK_OPEN`.
