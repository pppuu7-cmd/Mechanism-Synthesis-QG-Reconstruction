# Iter083M-SM preregistration — source-normal geometric radial basis for the K3/K4/K5 forest

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Can the frozen source collision geometry itself provide a canonical local radial quadratic structure for analytic regularization, bypassing the artificial ten-edge regulator metric Q that is not source-authorized by Iter083L?

This gate concerns only the local/tubular normal quadratic geometry. It does not define or select a finite part.

## Frozen source/authority inputs
1. Iter077I source-ordered Toller geometry: on a small common-collision ray `g_a(r)=exp[r(x_a.sigma)/2]`, each relative boost rapidity satisfies `beta_ab(r)=r |x_a-x_b|+O(r^2)`.
2. Iter082D exact barycentric projectors for every K3/K4/K5 block:

`P_B = I_B - (1/|B|) J_B`,

with `rank(P_B)=|B|-1`, and for every maximal chain `B3 subset B4 subset B5` the increments `P3`, `P4-P3`, `P5-P4` are pairwise orthogonal projectors of one-component ranks `(2,1,1)`, hence physical normal ranks `(6,3,3)` after tensoring with the three boost components.
3. Iter083B identifies the deepest normal representation as `V=spin1_SO(3) tensor Std5_S5` and uses the source Haar/tubular density convention.

## Canonical block quadratic form
For a collision block B of size p define tangent boost variables `x_a in R^3`, block mean `xbar_B`, and

`R_B^2 = sum_(a in B) |x_a-xbar_B|^2`.

Equivalently the complete-graph Laplacian identity should give

`sum_(a<b in B) |x_a-x_b|^2 = p R_B^2`.

Because source rapidities satisfy `beta_ab^2 = r^2 |x_a-x_b|^2 + O(r^3)`, the normalization

`R_B^2 = (1/p) sum_(a<b in B) beta_ab^2 / r^2 + O(r)`

is tied to the source rapidity convention at tangent order.

## Prospective predicates
P0 AUTHORITY_LOCK: exact repository locks must confirm the small-boost beta relation, Iter082D projector geometry/ranks, and Iter083B normal representation/Haar-tubular scope.

P1 UNIQUE_LABEL_METRIC: for each p=3,4,5, solve exactly the symmetric bilinear forms on R^p invariant under all S_p permutations. The full invariant space must have dimension 2 (same-label and different-label entries). On the translation-free standard subspace `Std_p={v:sum v_i=0}`, the J-part vanishes, leaving exactly one invariant symmetric form up to scale.

P2 PRODUCT_NORMAL_METRIC: combining the unique label metric on Std_p with the unique SO(3)-invariant Euclidean form on the boost-vector irrep gives a one-dimensional invariant quadratic-form space on `R^3 tensor Std_p`. No edge-regulator Q is used.

P3 COMPLETE_GRAPH_IDENTITY: verify exactly for p=3,4,5 the matrix identity

`L_Kp = p P_p`,

where `L_Kp` is the complete-graph Laplacian. Hence pairwise relative-boost norm and barycentric normal norm are the same quadratic geometry up to the frozen factor p.

P4 NESTED_VARIANCE: for every chain `B_p subset B_(p+1)` with added vertex v, verify the exact quadratic identity

`R_(B union {v})^2 = R_B^2 + p/(p+1) |x_v-xbar_B|^2`

for p=3 and p=4. In projector language the difference `P_(p+1)-P_p` must be an orthogonal rank-one label projector.

P5 ALL_FOREST_CHAINS: verify P4 and the full orthogonal decomposition on all 20 maximal K3-K4-K5 chains, giving physical normal ranks `(6,3,3)` and total 12.

P6 S5_COVARIANCE: verify exact transport of block radial projectors and chain increments under all 120 S5 permutations; no preferred root or base vertex may enter.

P7 INTERPRETATION_FIREWALL: PASS may establish a canonical **tangent/tubular radial quadratic basis** tied to source boost/Haar geometry. It must not claim a unique nonlinear global defining function, finite-part prescription, subtraction scale, renormalized extension, regulator independence, or physical selector.

## Negative controls
- reject label-dependent/rooted normal metrics;
- reject treating the ten-edge regulator Q of Iter083G as this normal metric;
- reject a metric with a nontrivial J component on the translation-free normal fiber as physically distinct (J acts trivially there);
- reject non-orthogonal forest increments;
- reject using only one maximal chain;
- reject promoting tangent `beta_ab=r|x_a-x_b|+O(r^2)` to an unproved exact nonlinear distance identity;
- retain finite-part/scale freedom after the radial basis is fixed;
- retain nonlinear chart/global patching blockers.

## Expected classification if PASS
`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
A source-faithful next gate can test analytic regularization directly in actual collision-normal radii rather than inventing edge-regulator metric data. The immediate successor should determine whether meromorphic finite parts built from these canonical local radii are unique or retain logarithmic/scale and forest-weight scheme dependence.

## Interpretation ceiling
No physical finite-part selector; no source-authorized analytic continuation yet; no full nonlinear group-manifold radial theorem; no all-strata global renormalization; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.