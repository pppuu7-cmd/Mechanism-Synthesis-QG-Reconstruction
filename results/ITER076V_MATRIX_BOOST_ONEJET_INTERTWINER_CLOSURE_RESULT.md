# Iter076V result — relative Toller boost one-jet is `i gamma J_n` and SU(2) intertwiners kill the node-common boost

**Date:** 2026-09-13

## Authority

- source supplement: `af0f8913dd4a51bdaa471140e6f7f396af107d1f`
- prospective preregistration: `8d90f1bf6cf86a9ff7870f62b76e15b4c53683fa`
- implementation: `515fad18dd6d7333cffe903293da0df16748c165`
- workflow head: `14bc9bcf7f5130db5fb9451cb267f32d2491279f`
- notation/source-lock-only repair: `cfd2286c4bc6733cf7d9af1c326270b1af5c27ea`
- authoritative run: `34783477289`
- jobs: A `103794609002`, B `103794609186`, C `103794609173`, D `103794609128`, aggregate `103794652691`

Artifacts:

- A `10326255535`, `sha256:5de6c80177b5d7b42de2265ed7050a9bda9dd4862119b7ed9f61e20ae0232738`
- B `10325911262`, `sha256:679c836e162546caf396377bbe5dff13d6f5c80b06c6fbe5bf3749c23fc183fa`
- C `10324779447`, `sha256:68630bb836eea5dd2319d0dcaf9e79c76338408fbdb4e0e88dd8d20f9ad2d835`
- D `10326095926`, `sha256:04061486ff3c153b4f17027fd6cddc4c45433e55f80284d7ba18df304d7db04f`
- aggregate `10326046124`, `sha256:fbf45078186fe796c353d90fc34d4a72bc319f862109f35721dd00f9d34a0ce6`

The first run had only an Eq.(4) notation-string mismatch in the provenance lane (`g_b^(-1)g_a` versus `g_b^{-1}g_a`). Lanes B/C/D already passed. The repair changed only the source-lock matcher; no frozen mathematical predicate, threshold, or interpretation changed. The authoritative rerun passes all lanes and aggregate.

## Frozen classification

`ITER076V_RELATIVE_TOLLER_BOOST_ONEJET_IS_I_GAMMA_J_AND_SU2_INTERTWINER_KILLS_NODE_COMMON_BOOST_EXACT_SCOPED`

## Exact matrix result

For `j>0`, write the pure boost-normal branch expansion

`t_m^(s)(beta)=beta^(-(2j+1))[C_m^(s)+beta D_m^(s)+o(beta)]`.

The exact source leading coefficients satisfy

`C_m^(-)=-C_m^(+)`

and, for either branch,

`C_m/C_(m-1)=-(j-m+1)/(j+m)`.

In the frozen scope the leading diagonal matrix `C=diag(C_m)` is invertible. Iter076U gives

`D_m/C_m=i gamma m`

for both causal branches. Therefore exactly

`C^(-1)D = D C^(-1) = i gamma J_z`.

By source Eq.(7) compact covariance, for a boost axis `n`,

`C_n^(-1)D_n = D_n C_n^(-1) = i gamma J_n`.

The opposite-axis control returns `-i gamma J_z` exactly.

## Exact intertwiner closure result

For source node `5`, all four incident ordered wedges are `(a,5)`, so at the coincident control a common node perturbation

`g_5(beta)=exp(beta K_n)`

induces the same opposite-direction relative boost on all four incident wedges:

`g_5(beta)^(-1)g_a=exp(-beta K_n)`.

After leading-matrix extraction the relative first correction inserts

`-i gamma sum_(a=1)^4 J_n^(5a)`

on the four magnetic slots of the node-5 boundary intertwiner.

Seven exact 4-valent SU(2) invariant controls were constructed by Clebsch-Gordan coupling:

- `(1/2,1/2,1/2,1/2)`, intermediate `k=0,1`;
- `(1/2,1,1/2,1)`, intermediate `k=1/2,3/2`;
- `(1,1,1,1)`, intermediate `k=0,1,2`.

For every control:

- nonzero magnetic support obeys `m1+m2+m3+m4=0`;
- total `J_z` annihilates the intertwiner exactly;
- total `J_+` and `J_-` annihilate it exactly;
- therefore total `J_n` annihilates it for arbitrary direction `n`.

Hence the **node-common boost-normal factorized one-jet vanishes after exact SU(2)-intertwiner contraction**. The mechanism is independent of the causal branch sign because the relative matrix one-jet is the same `i gamma J_n` on both branches.

## Scientific consequence

This closes a genuine part of the source one-jet blocker. The nonzero wedge-level `i gamma m` found in Iter076U is not a surviving physical node-common boost one-jet after boundary contraction: its magnetic dependence reorganizes into the standard SU(2) generator and is removed by intertwiner closure.

The result does not yet establish the full source one-jet. Compact/rotation tangential directions along the singular SU(2) locus remain to be audited, as does global compatibility of the extracted leading singular matrix over mixed boost/compact directions.

## Next admissible gate

Use Eq.(7) compact covariance and the exact boundary-state intertwiner invariance to audit common compact perturbations of an integrated source node. Then use the gauge-root stabilizer/relabeling covariance to extend the pure boost and compact directional cancellation from node 5 to all four integrated nodes. Keep mixed-direction differentiability and the physical nonlinear source-to-K4 curvature separate.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.