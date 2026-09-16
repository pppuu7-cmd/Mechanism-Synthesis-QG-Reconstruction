# Exact K5 Schwinger-corner Kirchhoff valuation / S5 orbit lemma

Date: 2026-09-16

Status: outcome-independent supporting lemma for a future Schwinger-boundary/Stokes gate. No numerator or period verdict is assigned.

## Setup

Let `Z` be any subset of the ten K5 Schwinger edges and scale

`alpha_e=t beta_e` for `e in Z`,

with fixed positive `beta_e`, while the remaining `alpha_e` stay fixed positive as `t -> 0+`.

Let `G_Z=K5\Z` be the graph of non-scaled edges and let `c(Z)` be its number of connected components.

The K5 Kirchhoff polynomial is the positive spanning-tree sum

`Psi_K5(alpha)=sum_(T spanning tree) prod_(e in T) alpha_e`,

with exactly 125 monomials and coefficient one.

## Exact valuation theorem

For every `Z`,

`ord_Z Psi_K5 = c(Z)-1`.

### Proof

Any spanning tree of K5 must connect the `c(Z)` connected components of `G_Z`, so it contains at least `c(Z)-1` edges from `Z`.

Conversely, because the original K5 is connected, the quotient graph obtained by contracting every connected component of `G_Z` is connected. A spanning tree of this quotient uses exactly `c(Z)-1` inter-component edges, all belonging to `Z`. Combining it with spanning trees inside the components gives a K5 spanning tree containing exactly `c(Z)-1` edges from `Z`.

Therefore the minimum `t`-degree among Kirchhoff monomials is exactly `c(Z)-1`.

All Kirchhoff coefficients and all frozen positive `beta_e` are positive, so the leading coefficient cannot cancel. Hence the valuation is exact, not merely a lower bound.

## S5 orbit compression

The action of the 120 vertex permutations on subsets of the ten edges has exactly **34** orbits. Therefore a complete denominator-side Schwinger corner audit needs only 34 unlabeled edge-subset types rather than 1024 labeled subsets.

Orbit counts grouped by `(|Z|, c(Z), ord_Z Psi)` are:

- `(0,1,0)`: 1 orbit;
- `(1,1,0)`: 1;
- `(2,1,0)`: 2;
- `(3,1,0)`: 4;
- `(4,1,0)`: 5;
- `(4,2,1)`: 1;
- `(5,1,0)`: 5;
- `(5,2,1)`: 1;
- `(6,1,0)`: 3;
- `(6,2,1)`: 3;
- `(7,2,1)`: 3;
- `(7,3,2)`: 1;
- `(8,3,2)`: 2;
- `(9,4,3)`: 1;
- `(10,5,4)`: 1.

The counts sum to 34.

## Boundary-use firewall

This lemma controls only the denominator valuation. It does **not** determine the valuation of either physical numerator `N_1,N_2`, of the annihilator-action numerator `B_v[N_c]`, or of the full gauge-projected boundary flux.

Therefore it cannot by itself establish local integrability, vanishing of higher-codimension boundary terms, or a global Stokes/IBP identity.

A future corner gate must combine these exact denominator valuations with exact numerator/flux valuations (or an equivalent sector-decomposition/analytic-continuation theorem) on all 34 orbit types.
