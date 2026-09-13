# Iter076U preregistration — j=1/2 intertwiner-contracted regularized K5 one-jet

**Date:** 2026-09-13

**Status:** `PREREGISTERED / PREINTEGRATION_CONTRACTION_WITNESS_GATE`

## Motivation

Iter076T establishes an exact nonzero one-jet in a single source gamma-simple `j=1/2` Toller/Haar-regularized magnetic component. That defeats a universal local wedge-evenness claim but does not decide whether magnetic sums and the five four-valent boundary intertwiners cancel all such linear terms.

The next admissible question is an existence/no-universal-cancellation witness at the **fully magnetic/intertwiner-contracted, pre-group-integration K5 tensor layer**.

A nonzero witness here still does not establish the four-`SL(2,C)` integrated vertex one-jet.

## Frozen source sector

Use:

- all ten spins `j_ab=1/2`;
- source causal signs `kappa_ab=sigma_a sigma_b` with `sigma_1=+1`, hence all `16` source causal K5 patterns;
- the two normalized four-valent `j=1/2` SU(2) recoupling intertwiners `two_i in {0,2}` at each of five nodes, hence all `2^5=32` basis boundary states;
- the repository Eq.(4) index convention already used by `vertex/boundary_intertwiner_collision_power.py`.

No coherent-state boundary data, fitted intertwiner or non-source causal wedge pattern is introduced.

## Source-consistent one-parameter collision paths

Gauge-fix `g_1=1`. For four frozen generic coefficient vectors `v^(q)` with distinct entries and no pair equality, use collinear boost paths

`g_a(r)=diag(exp(v_a r/2), exp(-v_a r/2))`, `r>0`,

with `v_1=0`.

Frozen vectors:

- P0: `(0, 1, 2, 4, 7)`;
- P1: `(0, -1, 2, 5, 9)`;
- P2: `(0, 1, -3, 4, 8)`;
- P3: `(0, -2, 1, 6, 10)`.

Every wedge relative group is exactly source-consistent as `g_b^-1 g_a`; no independent wedge rapidities are assigned.

## Maximal-pole regularized edge tensor

For every wedge and branch define

`R_ab^(kappa)(r) = sinh(beta_ab(r))^2 T_ab^(kappa)(g_b^-1 g_a)`

using the full `2x2` magnetic Toller matrix reconstructed by Eq.(7).

This is a common `j=1/2` maximal collision-pole removal, motivated by the exact extremal source specialization of Iter076T. It is a **preintegration regularized tensor diagnostic**, not a claim that the physical K5 measure factorizes into ten independent Haar radial factors.

## Lane A — common-factor finiteness control

For both branches, both diagonal magnetic labels and `gamma in {0.4,1.2}`, verify numerically with the source-backed Toller oracle that `sinh(beta)^2 t(beta)` stays finite as `beta -> 0+` on

`beta in {2e-2,1e-2,5e-3,2.5e-3}`.

PASS-A requires no blow-up in the regularized values and stable extrapolation. This lane does not require every component to have a nonzero limit.

## Lane B — exhaustive intertwiner-contracted census

For each `gamma in {0.4,1.2}`, each of the four frozen collision paths, all `16` causal sigma patterns and all `32` basis boundary intertwiner states, compute

`F(r)=Contract[ product_(a<b) R_ab^(sigma_a sigma_b)(r), product_a i_a ]`.

Use frozen one-sided radii

`r = {0.020,0.015,0.010,0.0075,0.0050,0.0035}`.

Fit complex quadratic models `F(r)=c0+c1 r+c2 r^2` independently on:

- the full six-point window;
- the last four-point small-r window.

A case is a **robust nonzero one-jet witness** iff

1. both fits are finite;
2. `|c1_small| > 1e-7 * max(1, |c0_small|)`;
3. `|c1_full-c1_small| <= 0.15 * max(|c1_small|,1e-30)`.

PASS-B requires at least one robust nonzero witness in every tested `gamma`, and reports the complete `2 x 4 x 16 x 32 = 4096` census.

A witness is existential: it disproves universal intertwiner cancellation but does not claim generic nonzero behavior.

## Lane C — basis and source controls

For every path/gamma:

- verify the 32 boundary states use only the normalized `two_i=0,2` invariant node tensors already present in the repository;
- verify all 16 wedge-sign patterns are source-factorizable `kappa_ab=sigma_a sigma_b`;
- verify KAK reconstruction errors remain below `1e-10`;
- run the EPRL edge control `T+ + T-` on the same paths for numerical sanity, without using it as the causal verdict.

PASS-C requires all structural controls.

## Lane D — scope firewall

PASS-D requires all of the following to remain false:

- four-group Haar-integrated causal vertex one-jet established;
- general-spin contracted one-jet theorem established;
- physical nonlinear source-to-K4 curvature selected;
- nominal `epsilon^-1` coefficient established;
- generic finite-spin signed P3 promoted;
- physical finiteness/divergence theorem;
- G3/F9/G8/K5 promotion.

The next missing layer on PASS is

`CORRELATED_GROUP_INTEGRATED_CONTRACTED_NUMERATOR_ONEJET`.

## Frozen classifications

If A-D pass and Lane B finds robust witnesses:

`ITER076U_JHALF_INTERTWINER_CONTRACTED_REGULARIZED_K5_TENSOR_HAS_NONZERO_ONEJET_WITNESS_GROUP_INTEGRATED_ONEJET_STILL_REQUIRED_SCOPED`

If A/C/D pass but no robust Lane-B witness is found:

`ITER076U_NO_INTERTWINER_CONTRACTED_ONEJET_WITNESS_ON_FROZEN_JHALF_PATHS_INCONCLUSIVE_SCOPED`

If source/structure controls fail:

`ITER076U_JHALF_INTERTWINER_CONTRACTED_ONEJET_GATE_FAIL`

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no general-spin or integrated-vertex one-jet theorem; no generic finite-spin signed P3; no physical source-to-K4 nonlinear map; no causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.
