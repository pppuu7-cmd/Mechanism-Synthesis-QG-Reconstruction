# Iteration 018 — direct ten-wedge causal integrand carrier

Status: **PASS / COMPLETED**

## Scope
First test following the causal vertex topology directly, without B4 booster factorization. For five explicit `SL(2,C)` group elements (`g1=1` gauge fixed), every relative element `g_b^-1 g_a` is Cartan-decomposed and the full Toller matrix is reconstructed as

`T(g) = D(U1) t(beta) D(U2)`.

Ten wedge factors are then multiplied using the correlated signs `kappa_ab=sigma_a sigma_b`.

## Campaign
8 independent GitHub jobs:
- gamma = `0.2, 0.5, 1.2, 2.0`
- two independent group configurations (`seed=7,23`)

Boundary carrier: `j=1/2` magnetic-basis component with a deterministic nontrivial magnetic pattern.

## Controls
All 8 jobs passed.

Across the campaign:
- maximum KAK reconstruction error: < **1.9e-15**
- maximum edgewise relative error in `T+ + T- = D`: approximately **3.6e-63**
- unconstrained `2^10` wedge-sign sum vs pointwise EPRL integrand: approximately **3.3e-63** worst case
- global `sigma -> -sigma` duplication error: approximately **3.7e-81** worst case
- maximum reduced residue terms in these samples: **237**

## Constrained-vs-unconstrained signal
The 16-class causal sum is generically very different from the unconstrained/EPRL pointwise integrand. The relative difference is sample- and gamma-dependent, ranging in this small campaign from ~`1.30` to ~`1.30e7`.

This magnitude is **not** interpreted as a physical amplitude effect yet: group integration and boundary intertwiner contraction can produce substantial cancellations. The result establishes only that the direct implementation correctly distinguishes the constrained causal combinatorics from the unconstrained EPRL decomposition at integrand level.

## Verdict
`DIRECT_CAUSAL_INTEGRAND_SMOKE_PASS`

Next bottleneck: the four gauge-fixed `SL(2,C)` group integrations. The next stage must respect the non-compact Haar measure and expose any rapidity cutoff explicitly rather than treating a finite domain as the full vertex.
