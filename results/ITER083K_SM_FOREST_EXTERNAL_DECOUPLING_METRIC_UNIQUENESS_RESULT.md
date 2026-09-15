# Iter083K-SM — authoritative forest-external decoupling plus S5 forces the Euclidean metric ray

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance
- preregistration `6d6edc09eb2ed8e2fee59b62d0277429e63d76c0`;
- locality source/framework lock `26e26410ed3ca31fffdb7dc47f6d54eae23f4e84`;
- validator initial `79a4cbe9f935b61becc9664563d353a7462d4b47`;
- workflow `f361083ee7e5ef9cee30254ddd9059890df4fb75`;
- first run `34916472367` failed only the Iter083I literal provenance phrase while P0-P5/P7 and all exact forest equations already passed;
- wording-only repair `a5d12b56dfdd6e49e88f59ded668c125dbb3b103`;
- authoritative run `34916567578`, job `104215356766`, terminal success;
- artifact `10376651844`, ZIP digest `sha256:06d3c114e51811d5a3891af96744b2603c119ae85d1bd5ed0e169a3e14de933c`;
- production JSON SHA256 `3d2b42bf7530d5316ccee17cee1b980773d06e487041cd384590c1bfc13f9d27`.

## Classification
`ITER083K_SM_AUTHORITATIVE_FOREST_EXTERNAL_DECOUPLING_PLUS_S5_FORCES_Q_EUCLIDEAN_RAY_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Conditional locality axiom
For every authoritative proper divergent block B and each edge regulator e not internal to B, require

`Q*(L_B,e_e^*)=0`,

where

`L_B=sum_(f internal B) x_f`.

This prevents a pure subgraph pole `1/L_B` from converting a holomorphic external regulator coordinate into a finite constant solely through the Q-based polar/holomorphic splitting.

The theorem proves the consequence of this axiom; it does not yet claim the Lorentzian causal-K5 source authorizes it.

## Complete authoritative enumeration
Using exactly the Iter082D K5 forest, production enumerates all proper-block/external-edge pairs:

- 10 K3 blocks x 7 external edges = 70;
- 5 K4 blocks x 4 external edges = 20;
- total **90** conditions.

They split into exactly three S5/combinatorial types:

1. 60 K3 cross edges: `(n_adj,n_disjoint)=(2,1)`;
2. 10 K3 complement edges: `(0,3)`;
3. 20 K4 external edges: `(3,3)`.

## Exact metric constraints
Write the general S5-invariant dual form as

`Q*=alpha I + beta A + gamma B`.

Because the tested edge is external to the block, the alpha term never contributes. The three condition types are therefore

`2 beta + gamma = 0`,

`3 gamma = 0`,

`3 beta + 3 gamma = 0`.

The full 90x2 coefficient system has exact rank 2.

Two independent minimal subsystems already suffice:

- K3 cross + K3 complement has determinant `6`;
- K3 cross + K4 external has determinant `3`.

Hence

`beta=gamma=0`.

Therefore

`Q*=alpha I`,

and for a positive nondegenerate metric

`Q=alpha^-1 I`.

As in Iter083J, an overall common scale is irrelevant to orthogonality/polar projection. The allowed Q-family collapses to the Euclidean ray.

## Reconciliation with Iter083G/I
Iter083G remains correct: S5 alone permits a three-sector family of Q.

Iter083I remains correct: the positive S5-invariant non-Euclidean witness Q2 changes proper/nested polar complements. In fact Iter083I gives exact Q2 external pairings `-25/176` for K3 and `-15/88` for K4, so Q2 violates the present conditional locality axiom.

Thus Iter083K narrows the admissible scheme class rather than invalidating the broader S5-only results.

## Relation to external locality frameworks
Dang–Zhang locality keeps separated subgraph renormalizations factorized while cross-edge factors remain outside internal renormalization; disjoint unions factor exactly. This motivates the forest-external condition, but does not automatically prove its regulator-coordinate version for the connected Lorentzian Toller K5 vertex.

That applicability bridge is now the central open issue for this selector candidate.

## Research consequence
Two independent conditional uniqueness results now agree:

- Iter083J: universal tensor-product factorization -> Euclidean ray;
- Iter083K: authoritative K3/K4 forest-external decoupling -> Euclidean ray.

The second uses only the actual frozen subdivergence architecture and is therefore the more relevant candidate bridge to physical K5.

## Interpretation ceiling
No source authorization of forest-external decoupling; no unique physical extension; no full K5 meromorphic continuation; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.