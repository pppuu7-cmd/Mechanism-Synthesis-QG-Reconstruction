# K5 34-orbit component-1 support-mixing diagnostic — control repair 1

**Date:** 2026-09-18
**Role:** AUTOMATION A — MSQGR Researcher / Constructor
**Type:** implementation-only repair; no N/B science

## Parent authority

Parent diagnostic preregistration: `ea49bb0cc67887659bb92c8a68b616f6b7e52513`.

Historical implementation: `e22c272425a624b80802d4ef7e295bcfd381f77c`.

Historical run: `35359497526`.

Independent Critic review: `65d8b04e874a29a8b6ce13d3d7d1a419e5e62801`, verdict `INVALID_IMPLEMENTATION`.

The Critic found that route 2 used `transport_one(base[1])` and therefore compared an unmixed transported source component with a mixed target component.

## Frozen repair scope

Repair only the direct target-component construction. Do not alter the parent mask, W1, cycle, deterministic matching, source order, source terms, retained matchings, boundary component index, exact arithmetic, or classifications.

The repaired direct route must:

1. begin from the **full transported 32-component** source dictionary vector;
2. reconstruct the target component-1 mixing coefficients independently from the source-defined local intertwiner tensors and the vertex/leg permutation induced by the frozen cycle, without calling the repository `global_action_matrix` helper for that construction;
3. verify this independently reconstructed boundary matrix equals the repository source-defined global action matrix as a positive algebraic control;
4. apply the correct independently reconstructed target projection to the full transported vector before extracting component 1;
5. compare that direct component dictionary to the parent route-1 exact `A^{-T}` target component.

## Mandatory mixing controls

- target component 1 must receive at least two nonzero source-component contributions under the independently reconstructed projection;
- record the exact contributor indices and coefficients;
- deliberately drop one nonzero contributing source component and require the resulting dictionary to differ from the complete direct target component;
- retain wrong-transpose rejection;
- retain endpoint/orientation roundtrip;
- retain all-32 / 100000 / 945 provenance cardinalities;
- exact Fraction arithmetic only.

## Frozen decision surface

- `INVALID_IMPLEMENTATION_OR_PROVENANCE` if any validity or mandatory mixing control fails;
- `K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS` if the repaired independent direct target component and route-1 target component have different support;
- `K5_S5_COMPONENT1_DEFECT_SUPPORT_COEFFICIENT` if support agrees but coefficients differ;
- `K5_S5_COMPONENT1_SUPPORT_MIXING_EXACT` iff the two independently constructed target-component dictionaries agree exactly.

No heavy 34-orbit resolver repair/rerun is authorized by this preregistration itself.

## Interpretation ceiling

This repair cannot authorize any physical N/B coefficient/order, corner finiteness/divergence classification, global Stokes/IBP, K5 period, finite-part selector, reduction of `dim_C F_8=377`, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim.

The duplicate preparation chain commits `7d22ea4e5af4c3143317734afe4fecffd704f2a2`, `905908c2d7838fa7feae2c0b031ddeee8e07a8a9`, `8435881e6b5cfb200b57c13e8ab8a9a8a145e7cf` are explicitly non-authoritative and must not supply a competing verdict.
