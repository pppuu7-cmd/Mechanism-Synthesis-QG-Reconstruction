# Iteration 068B result — Appendix-D contact-layer wavefront obstruction

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `7ef76367e465f833efa21623446a24720ea673ab`
- Implementation: `95f55a9e7df123d1e8b21e6790f1720930bf0ba1`
- Initial workflow commit: `b53addddd6fda0c5352b090b2d5f4ae6e4e2a6dc`
- Initial run `34740815975`: infrastructure-only artifact-name failure because rational gamma labels contained `/`; the exact science step itself passed.
- Minimal workflow-only repair: `d1f0e6ba9f0aed5f51540cdad60bc632e10be0cf`, representing the same exact rational gamma points as `0.2`, `1.2`, `2` for safe artifact names.
- Authoritative repaired run: `34740962426`
- Aggregate job: `103680507321`
- Aggregate artifact: `10311749011`
- Digest: `sha256:c9439647f4bb9a37830165c3fb644831ccf5fb6b865f82f2e56621e66320b0ad`

## Frozen result

`24/24` frozen lanes passed all exact predicates across all eight physical K4 sigma classes and gamma = 1/5, 6/5, 2.

Terminal classification:

`ITER068B_CONTACT_LAYER_OBSTRUCTS_SEPARATE_K4_PRODUCT_ALL_FROZEN_CLASSES`

For gamma-simple `j=1/2`, the source-backed Appendix-D coefficient

`c2 = 2/(rho^2+1/4)`

is nonzero for every frozen finite gamma. Therefore every fixed Toller branch contains a nonzero `delta'` contact term. Since `WF(delta')` contains both nonzero conormal orientations, the K4 triangle identity

`n_01 + n_12 - n_02 = 0`

provides an opposing-covector collision independently of the causal sigma class. The independent `+/-` branch sum cancels the one-wedge `delta'` coefficient exactly, as required by the source control.

## Scientific interpretation

This closes the route that first expands every wedge separately into bulk + contact distributions and then tries to form the ordinary Hörmander product on the K4 collision diagonal. The obstruction is stronger than the denominator-only Iter068A split: once the source-backed `delta'` contact layer is included, all frozen K4 causal classes are obstructed for that **separate-contact multiplication route**.

This is **not** a theorem that the source-defined causal vertex is undefined. In particular it does not exclude a joint finite-spectral-`i epsilon` multivariate boundary value in which spectral variables are kept correlated until after the joint analytic/distributional limit. It does not authorize counterterms, a preferred sequential order, physical sector selection, a vertex finiteness/divergence claim, K5, G3, F9, or G8 promotion.

## Consequence for the frontier

The primary route must now keep the finite-spectral source jointly defined through the multivariate K4 boundary-value construction. Naive multiplication of individually contact-expanded fixed-causal wedges is closed as a physical carrier candidate.
