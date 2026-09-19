# Implementation-only repair 1 — K5 post-collapse geometry/covariance diagnostic

Date: 2026-09-19

Status: FROZEN BEFORE CORRECTED IMPLEMENTATION.

## Trigger

This repair is frozen from an outcome-blind static audit of the already-frozen diagnostic implementation at commit `b47198b9f4fa9d4b9726b2fd76971a76a29992c5`, before consuming any terminal diagnostic payload, stage boolean, hash, coefficient, N/B order, or q18 value from the workflow launched by `ebf328ebede611c830fcb9c0f598e51630e32d37`.

Parent scientific/diagnostic prereg remains immutable:

`prereg/K5_34_ORBIT_POSTCOLLAPSE_GEOMETRY_COVARIANCE_S5_TRANSPORT_DIAGNOSTIC.md`
commit `b7495db85844111b947bc902e5df2a496bf614ad`.

## Static implementation defects

### R1 — G3 scope leakage

Frozen G3 requires the **value-only** ray Laplacian congruence

`L_target = G_C^T L_original G_C`.

The initial implementation constructs only `L` from `D(alpha,v)` and uses that dual-jet matrix in G3. This folds tangent/derivative information into the earlier G3 stage and can misclassify a first G5 defect as G3.

### R2 — G5 dependency alias

Frozen G5 must test annihilator/tangent transport including the **full dual-jet Laplacian**. The initial implementation defines G5 using the same G3 boolean. Once G3 is corrected to value-only, G5 requires its own exact dual-jet congruence boolean.

### R3 — malformed identity control scope

The frozen `G_C -> I` malformed control belongs to the value-only Laplacian congruence surface. The initial implementation applies it to the dual-jet matrix.

### R4 — nontrivial incidence control too weak

The frozen control requires the identity/no-vertex-permutation construction to be distinguishable from the nontrivial incidence transform on at least one non-root edge. The initial implementation checks only `G != I` plus that at least one correct non-root row relation is true. It must instead explicitly verify that replacing `G_C` by identity fails the required non-root row transport for at least one non-root edge.

## Frozen correction

The corrected implementation may change only:

1. construct and retain a value-only Laplacian from `alpha`;
2. use that value-only Laplacian exclusively in G3 and its identity-G malformed control;
3. retain the existing `D(alpha,v)` dual-jet Laplacian and test its congruence explicitly in G5;
4. replace the weak nontrivial-incidence malformed boolean with an explicit non-root identity-map rejection;
5. add hashes/booleans needed to distinguish value-only and dual-jet matrices;
6. lock this repair preregistration in the corrected implementation.

Everything else remains byte-semantically unchanged in scientific meaning: mask=1, W1, cycle C=(1,2,3,4,0), physical source, 945 matching objects, exact arithmetic, G1/G2/G4/G6/G7/G8/G9 definitions, malformed covariance controls, frozen classification names/order, interpretation ceiling, no N/B coefficient/order emission, q18 unused, heavy resolver unauthorized.

## Classifier semantics

The corrected classifier still uses the original earliest-failed-stage ordering G1 through G9. This repair does not add, delete, merge, weaken, or reorder any frozen scientific/diagnostic classification.

The workflow launched from `ebf328eb...` is not authority for localization if its implementation realizes the leaked G3/G5 decomposition. Its terminal execution may be recorded operationally, but a corrected production is required for the frozen diagnostic classifier.

## Interpretation ceiling

Implementation repair only. Resolver authority remains `0/64`. No heavy resolver run, local N/B order, global Stokes/IBP, K5 period, finite-part selector, regulator-independence, F8-dimension reduction, G3/composition, NEW_PHYSICS_FOUND or complete-QG claim is authorized.
