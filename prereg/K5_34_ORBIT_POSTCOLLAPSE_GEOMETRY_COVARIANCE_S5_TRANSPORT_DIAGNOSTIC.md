# Prospective diagnostic — K5 34-orbit post-collapse geometry/covariance S5 transport

Date: 2026-09-19

Status: FROZEN BEFORE IMPLEMENTATION.

## Trigger

Heavy resolver repair-1 run `35271187040` is terminal `INVALID_IMPLEMENTATION` because `S5_full_coefficient_covariance_all=false`.

The repaired component-1 source-support mismatch was independently confirmed by Critic run `35402998823`, but the prospectively frozen resolver repair-2 source-side hypothesis failed its corrected preflight.

Corrected preflight run `35404110282`, head `684dcb3a0250f995b487603daaeb8be04a35cbc1`, artifact `10571731222`, leaves exactly one frozen failed control:

`repair1_pullback_frame_object_rejected=false`.

All independent-Critic/full32/100000/target-mixing/hash/cardinality/945-matching controls pass. Therefore the full-component mismatch is quotiented away by the physical invariant-dual/Wick collapse and the physical matching object consumed by the resolver is unchanged.

No heavy repair-2 production is authorized.

## Frozen question

On the single predeclared lane

- mask `1`;
- ray `W1`;
- cycle `C=(1,2,3,4,0)`;

with the already locked physical source matching objects, what is the **first post-collapse exact geometry/covariance object** for which the original route and S5-permuted route fail to transport covariantly?

No N/B leading order, first-nonzero coefficient, q18/q19/q21 value, physical corner class, invalid heavy-run coefficient payload or fitted convention may be consumed.

## Exact source lock

The diagnostic must first verify:

1. repair-1 physical S5 matching object has exactly 945 exact-rational keys;
2. the corrected full32 endpoint/orientation + target `A^{-T}` mixing + invariant-dual/Wick collapse from repair-2 produces the same 945-matching object;
3. component-1 independent Critic remains `CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH`;
4. q18 values were not used.

Failure here is `INVALID_IMPLEMENTATION_OR_PROVENANCE`, not a new defect class.

## Frozen post-collapse decomposition

Let old edge `i` map to target edge `j=ep(C,i)`. Use exact rational/polynomial arithmetic only.

### G1 — ray permutation

Construct the univariate projective ray exactly as in `route_a`. Require

`alpha_target[ep(C,i)] = alpha_original[i]`

for all ten edges.

### G2 — incidence quotient representation

Construct the unique 4x4 exact matrix `G_C` from the first four canonical root-edge rows by the frozen relation

`ROWS[ep(C,i)] = edge_sign(C,i) * ROWS[i] * G_C`.

Require the same relation for all ten canonical edges and exact invertibility of `G_C`.

### G3 — Laplacian congruence

With value-only ray variables require

`L_target = G_C^T L_original G_C`

exactly.

### G4 — uniform regulator matrix

Require the frozen `Q=L_uniform/5` to obey the same S5 quotient symmetry:

`Q = G_C^T Q G_C`.

### G5 — annihilator/tangent transport

Recompute the frozen degree-4 annihilator from the original and target ray. Require its edge components and the full dual-jet Laplacian to transport through the same edge/G_C representation. No annihilator coefficient may be fit after output.

### G6 — adjugate/covariance series transport

For every old edge pair and series order `n=0..4`, compare the exact covariance series entry with its target edge pair, including the two frozen edge-orientation signs induced by the canonical target orientation.

Record only equality booleans, hashes and the lexicographically first failing `(edge_i,edge_j,n)`; do not emit physical coefficient values.

### G7 — determinant factor transport

Compare the exact determinant-factor series `F[0..4]` between the two routes.

### G8 — matching/covariance composition

Using the already locked base and transported 945-matching source objects, compare exact matching contributions before the 945-term sum under the canonical edge/matching transport. Record only hashes/first failing matching.

### G9 — final local polynomial equality

As a downstream diagnostic only, compare complete N and B polynomials for both channels on mask=1/W1. Record booleans/hashes only, never their coefficients or leading orders.

## Mandatory malformed controls

- identity/no vertex permutation must be distinguishable from the nontrivial incidence transform on at least one non-root edge;
- omit one required edge orientation sign in covariance transport and require rejection;
- replace `G_C` by identity and require Laplacian-congruence rejection on the nontrivial target ray;
- alter one covariance-series entry prospectively and require matching-composition rejection;
- all route-internal exact checks must remain true;
- no floating tolerance, interpolation fit, fitted phase/character/channel matrix or invalid N/B payload.

## Frozen classifications

Classify by the earliest failed valid stage:

- `K5_S5_POSTCOLLAPSE_DEFECT_RAY_PERMUTATION`
- `K5_S5_POSTCOLLAPSE_DEFECT_INCIDENCE_BASIS_TRANSPORT`
- `K5_S5_POSTCOLLAPSE_DEFECT_LAPLACIAN_CONGRUENCE`
- `K5_S5_POSTCOLLAPSE_DEFECT_Q_INVARIANCE`
- `K5_S5_POSTCOLLAPSE_DEFECT_ANNIHILATOR_TANGENT_TRANSPORT`
- `K5_S5_POSTCOLLAPSE_DEFECT_COVARIANCE_SERIES_TRANSPORT`
- `K5_S5_POSTCOLLAPSE_DEFECT_DETERMINANT_FACTOR_TRANSPORT`
- `K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION`
- `K5_S5_POSTCOLLAPSE_DEFECT_NUMERATOR_FLUX_ASSEMBLY`
- `K5_S5_POSTCOLLAPSE_NO_DEFECT_ON_FROZEN_LANE`
- `INVALID_IMPLEMENTATION_OR_PROVENANCE`.

No outcome authorizes heavy resolver execution by itself. A separately prospectively frozen repair is required after a localized defect.

## Interpretation ceiling

Implementation diagnosis only. Resolver authority remains `0/64`. No local physical N/B order, global Stokes/IBP, K5 period, finite-part selector, reduction of `dim_C F8=377`, regulator independence, G3/composition, NEW_PHYSICS_FOUND or complete-QG claim follows.
