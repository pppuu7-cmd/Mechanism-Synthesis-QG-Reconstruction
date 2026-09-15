# K4 order-3 source-faithful cubic realization bridge — Researcher result

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED — independent Critic review pending**

## Prospective provenance

- preregistration: `prereg/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE.md`, commit `fd01325771e4161d332e09eb8456d679e6bf96e9`;
- post-prereg derivation: `sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md`, commit `a4c645ee920b5bc5047756542d38d70888fd74e0`;
- validator: `scripts/k4_order3_source_faithful_cubic_realization_bridge.py`, commit `616669186371b997dd85976dca530ca630fa9cac`;
- workflow/head: `.github/workflows/k4-order3-source-faithful-cubic-realization-bridge.yml`, commit `45293ae8191fcee74788a743442911f9e6ed7b3e`;
- GitHub Actions run `34976334040`, terminal success;
- job `104404869316`, terminal success;
- artifact `10399632086`, `k4-order3-source-faithful-cubic-realization-bridge`;
- artifact ZIP digest `sha256:a63a60a5c53608db9e8a1484d1bc2611df96e43271221e25fc7d9c41b0fa6630`;
- production JSON SHA256 `c3fd167e17b4f3cf10c69f481011d66844afd0958c6a376fb0aa8682a9fee6b7`;
- exact durable raw: `results/raw/k4_order3_source_faithful_cubic_realization_bridge.json`, commit `3f827f47db9208e4b9a2cd2be91e7aa5f4a03f36`.

## Classification

`K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DEFINED_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

This is Researcher authority only until independent Critic review.

## Dependency closed

The independently confirmed K4 reachability review had isolated three decisive missing explicit realization ingredients:

- `R3_TOLLER_ORDER3`;
- `R4_EXTERNAL_TOLLER_JETS`;
- `R6_Q_DEFINING_FUNCTION_ORDER3`.

The present gate constructs all three from already-authoritative exact source functions in one compatible source chart. It does **not** compute the K4 polar coefficient itself.

## Exact gauge-free full spin-half Toller reconstruction

For the source Cartan decomposition

`h=U1 exp(beta sigma_3/2) U2`,

write the two reduced magnetic entries of either causal branch as `t_+^kappa(beta)` and `t_-^kappa(beta)`, and define

`t0=(t_++t_-)/2`, `t3=(t_+-t_-)/2`.

With

`S=U1 U2`, `N=U1 sigma_3 U2`,

one has exactly

`h = cosh(beta/2) S + sinh(beta/2) N`,

`h^{-dagger} = cosh(beta/2) S - sinh(beta/2) N`.

Hence

`S=[h+h^{-dagger}]/[2 cosh(beta/2)]`,

`N=[h-h^{-dagger}]/[2 sinh(beta/2)]`,

and therefore

`T^kappa(h)=t0(beta)[h+h^{-dagger}]/[2 cosh(beta/2)] + t3(beta)[h-h^{-dagger}]/[2 sinh(beta/2)]`.

This is algebraically identical to the source Cartan formula and uses no separately chosen KAK angular section. It therefore defines the complete `2x2` spin-half Toller matrix jet directly from the group element, the source rapidity and the exact Table-II reduced functions.

Production mechanically verified the reconstruction identity.

## Exact reduced cubic controls

Using `z=i rho` and

`R(beta)=beta^2/sinh(beta)^2=1-beta^2/3+O(beta^4)`,

production verified exactly through degree 3

`exp(z beta)R = 1+z beta+(z^2/2-1/3)beta^2+(z^3/6-z/3)beta^3+O(beta^4)`

and

`exp(z beta)[cosh(beta)-2z sinh(beta)]R`

`=1-z beta+(1/6-3z^2/2)beta^2+(z/2-5z^3/6)beta^3+O(beta^4)`,

with the minus-branch series obtained by the exact source `z -> -z` relation and frozen branch signs.

No fitted cubic coefficient was introduced.

## R3 — internal K4 Toller jets

For any K4 block `C`, use the already-authoritative rapidity/X tubular chart. The six internal relative elements are kept noncommutatively as exact products of source group variables; no commuting-coordinate replacement is made.

Composing those exact relative elements with the gauge-free full-matrix formula defines the complete all-entry/all-branch source Toller jets through total K4 normal degree 3. The construction is a jet operator on the resolved front and keeps compact factors rather than replacing them by a scalar or frozen angular ray.

Production classification:

`R3_TOLLER_ORDER3 = CONSTRUCTED_EXACT_FULL_MATRIX_JET_OPERATOR`.

## R4 — four external-to-K4 Toller jets

Every K4 block has exactly six internal and four external K5 edges. Production enumerated all five K4 blocks and found `(6 internal, 4 external, 10 total)` in every case.

At the K4-face interior the external relative elements are smooth in the K4 normal variables. Applying the same exact full-matrix source function and taking its degree-3 source-chart jet defines all four external matrix jets while leaving outer/tangential group data symbolic.

No external edge is omitted and no representative boundary state or ray is chosen.

Production classification:

`R4_EXTERNAL_TOLLER_JETS = CONSTRUCTED_EXACT_SMOOTH_MATRIX_JET_OPERATOR`.

## R6 — exact sixteen-block defining-function jets

The already-confirmed source family remains

`q(h)=beta(h)^2=arcosh((1/2)Tr(hh^dagger))^2`,

`q_B=(1/|B|) sum_(a<b in B) q(g_b^-1 g_a)`.

Production verified the corrected inverse-cosh series

`q=2s-(1/3)s^2+(4/45)s^3+O(s^4)`,

`s=(1/2)Tr(hh^dagger)-1`,

by exact composition back to `s` through cubic order.

All 16 divergent K3/K4/K5 block parameters remain present. Their K4 cubic pullbacks are therefore the simultaneous degree-3 Taylor jets of the exact `q_B` functions in the same source chart; no regulator-space metric or fitted cross-coupling is added.

Production classification:

`R6_Q_DEFINING_FUNCTION_ORDER3 = CONSTRUCTED_EXACT_16_BLOCK_COMPOSITION_JET_OPERATOR`.

## Retained source structure

The gate retains rather than replaces:

- R1 authoritative K4 normal chart;
- R2 noncommutative group product/BCH authority;
- R5 original Haar/Jacobian authority, including corrected nested density powers `(5,8,11)`;
- R7 complete all-32 boundary contraction map;
- R8 resolved front/distributional pairing;
- R9 source branch normalization and published one-wedge spectral `i epsilon`;
- R10 induced-leg `S5` transport.

Production checked all 120 label permutations on the block incidence and found zero failures.

## Controls

All frozen predicates passed. The complete positive bridge fixture was accepted.

All 12 malformed constructions were rejected by the same validator, including scalar K4 surrogate, representative boundary component, frozen angular ray, commuting BCH, omitted external jets, flat Haar, one-parameter regulator, `beta+i epsilon`, termwise contact multiplication, post-hoc finite part, K3-to-K4 zero inference and an unproved KAK angular gauge.

## New scientific fact

The previously confirmed K4 reachability blocker is closed at the **cubic object-definition level** in the frozen all-`j=1/2` source scheme.

The decisive reason is that a separate KAK angular-gauge jet is unnecessary for spin one-half: the exact full Toller matrix can be reconstructed algebraically from `h`, `h^{-dagger}`, `beta(h)` and the two exact source reduced entries. This simultaneously defines the internal and external Toller matrix jets. The exact source-derived `q_B` family then supplies the required nested cubic defining-function jets by ordinary composition in the same chart.

Thus an actual full-32 K4 order-3 polar-coefficient computation is now mathematically **well-defined as the next dependency**, subject to independent Critic confirmation of this bridge.

## Interpretation ceiling

This gate does **not** evaluate the K4 polar coefficient, classify it zero/nonzero, compute its annihilator, select a physical finite part, establish regulator independence, or remove the exact `dim_C F_8=377` extension-selection freedom.

It does not authorize K5 order 8 before K4 coefficient extraction and independent review. No causal-vertex finiteness/divergence theorem, no generic-spin result, no global all-strata patching theorem, no E3/E4/E6 closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
