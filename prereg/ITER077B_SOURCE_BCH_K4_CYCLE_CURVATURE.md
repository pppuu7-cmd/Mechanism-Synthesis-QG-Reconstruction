# Iter077B preregistration — source BCH quadratic K4 cycle curvature

**Date:** 2026-09-14

## Purpose

Iter076R-S identify a symmetry-allowed nonlinear quadratic-curvature channel, but do not show that the source group law actually selects a nonzero representative. This independent gate asks a narrower source-coordinate question:

> Does the exact BCH second-order term in the source relative variables `log(g_b^-1 g_a)` generate a nonzero K4 cycle component after one K5 node is gauge fixed, with coefficient fixed by the group law rather than fitted?

A PASS is a source-relative-coordinate result only. It is not yet the physical Toller/front-face numerator pushforward.

## Frozen input

Use `sources/ITER077_PARALLEL_FRONTIER_SOURCE_DERIVATION.md`, canonical K4 incidence and Hodge conventions from Iter076H-Q, and the exact BCH formula

`Y_ab = X_a - X_b + (1/2)[X_a,X_b] + O(X^3)`.

## Lane A — exact graph/Hodge algebra

For oriented K4 edges `(01,02,03,12,13,23)` with standard signed incidence:

PASS iff exact rational/integer algebra verifies:

1. reduced incidence rank is 3;
2. cut dimension is 3 and cycle dimension is 3;
3. the canonical complement Hodge matrix has `H^2=I`;
4. H maps the cut space to the cycle space and the cycle space to the cut space;
5. for all `p in S4`, the orientation-aware edge action `E_p` satisfies incidence covariance and `E_p H E_p^-1 = sgn(p) H`.

## Lane B — source BCH curvature controls

Use exact rational `su(2)` vector controls with bracket given by the cross product. For each control and each choice of K5 root, restrict to the complementary K4 and form

- linear edge datum `L_ab = X_a - X_b`;
- quadratic datum `Q_ab = (1/2)(X_a x X_b)` componentwise;
- exact cycle projection `Q_cyc` using the K4 incidence projector.

PASS iff:

1. every `L` lies exactly in the cut space;
2. a frozen generic family has nonzero `Q_cyc` for at least one Lie-algebra component for every root choice;
3. a frozen collinear commuting control has `Q_cyc=0` exactly;
4. scaling all node variables by `s` scales `L` by `s` and `Q_cyc` by `s^2`;
5. replacing the BCH coefficient `1/2` by a symbolic coefficient shows the cycle term is linear in that coefficient and therefore source fixes its normalization at this order.

## Lane C — S4/root covariance of the quadratic cycle datum

PASS iff:

1. for all 24 permutations of the four non-root nodes, relabeling node controls before constructing `Q_cyc` agrees exactly with the signed edge action on the already-constructed `Q_cyc`;
2. cycle membership is preserved under every relabeling;
3. applying H to `Q_cyc` produces a cut-space datum with the expected sign-twisted S4 covariance;
4. all five K5 root choices satisfy the same algebraic classification; root choice changes coordinates but does not create or remove the generic BCH cycle-curvature mechanism.

## Lane D — scope firewall and relation to the Iter076R-S channel

PASS iff the aggregate records all of:

- `source_BCH_quadratic_cycle_curvature_selected=true` in exponential relative-coordinate scope;
- `source_BCH_coefficient=1/2`;
- `commuting_control_curvature_zero=true`;
- `canonical_Hodge_twisted_representative_available=true`;
- `front_face_Toller_pushforward_established=false`;
- `physical_reduced_K4_numerator_coefficient_established=false`;
- `epsilon_minus1_coefficient_established=false`;
- `correlated_K5_boundary_value_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

The result may be compared structurally with the unique symmetry-allowed quadratic channel of Iter076R-S, but equality with the physical reduced numerator channel is forbidden unless a later gate constructs the front-face/Toller pushforward.

## PASS classification

`ITER077B_SOURCE_BCH_SECOND_ORDER_SELECTS_NONZERO_K4_CYCLE_CURVATURE_EXACT_COORDINATE_SCOPED`

## FAIL classification

`ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE_SELECTION_FAIL`

## Next admissible gate on PASS

Construct the map from the Iter077A blown-up Toller front-face data through the source BCH relative-coordinate curvature into the reduced K4 quadratic channel. Only that composed, source-backed map may be used in an `epsilon^-1` coefficient analysis.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical Toller/front-face pushforward; no physical reduced K4 numerator coefficient; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain source spectral `i epsilon`.