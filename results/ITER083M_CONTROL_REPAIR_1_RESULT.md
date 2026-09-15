# Iter083M control-only repair 1 result — source-normal radial basis

**Date:** 2026-09-15

## Status

Researcher verdict: **`PASS_EXACT_SCOPED`** under the unchanged Iter083M scientific preregistration.

Classification:

`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`

This repaired Researcher result is **pending independent Critic review**. It supersedes the earlier implementation-invalid production only for Researcher-side evidence; the historical files and invalidating Critic review remain immutable provenance.

## Frozen contract

Parent preregistration: `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`, commit `c801299beb44816941fd441715e3eb03c73740c7`.

Controlling pre-repair invalidation: `results/ITER083M_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`.

Prospective control-only repair freeze: `prereg/ITER083M_CONTROL_ONLY_REPAIR_1.md`, commit `9da79bd7cf1e78c546017340e234eeffdaef52dc`.

Repair implementation / production head: `463ba012c4b3f8d465ab7df99995f5f40f3e7e44`.

No hypothesis, source authority, P0-P7 predicate, scientific PASS class or interpretation ceiling changed.

## Production authority

GitHub Actions run `34921183332`, terminal `success`.

Job `104229460141`, terminal `success`.

Artifact `10378026902`, `iter083m-source-normal-geometric-radial-basis`.

Artifact ZIP digest:

`sha256:06d6c560942a73bd78c31557f9fb3f4714a17b495857ed17071d271409700f11`.

Production JSON SHA256:

`6572765b7a760a7505d6dc1c23d9239d5ede80cd37e1174c171951635f26c3e2`.

Durable copied raw output: `results/raw/iter083m_sm_control_repair_1.json`.

## Positive predicates

All unchanged P0-P7 passed.

The exact positive calculations reproduce the parent scoped theorem:

- for p=3,4,5, the ambient S_p-invariant symmetric-form space has dimension 2 and restricts to dimension 1 on `Std_p`;
- the 24-element orientation-preserving signed-permutation subgroup forces boost-vector symmetric-form dimension 1;
- `L_Kp=pP_p` exactly for p=3,4,5;
- all nested K3->K4 and K4->K5 projector increments satisfy the exact variance/projector identities;
- all 20 maximal K3-K4-K5 chains have label ranks `(2,1,1)` and physical ranks `(6,3,3)`, total 12;
- all frozen S5 block/projector transports pass: 1920 block checks and 7200 chain-increment checks;
- P7 retains the original interpretation ceiling.

The canonical local tangent/tubular form remains

`R_B^2 = sum_a |x_a-xbar_B|^2 = (1/|B|) sum_(a<b)|x_a-x_b|^2`,

with source tangent relation

`sum beta_ab(r)^2 = |B| r^2 R_B^2 + O(r^3)`.

## Repaired malformed-control execution

The implementation-invalid alias controls were replaced by actual injected malformed objects/claims.

1. **Rooted metric:** `diag(1,2,3,4,5)` was passed through an exact S5-invariance validator and rejected; production records `rooted_metric_s5_invariant=false`.
2. **Edge-Q identification:** a structured ten-edge regulator object `(kind=edge_regulator_metric, domain=R10_edge_regulator_space, dim=10)` was compared to the physical deepest normal object `(kind=normal_fiber_metric, domain=R3_tensor_Std5, dim=12)` and the attempted identity was rejected.
3. **J deformation:** the all-ones J form was explicitly restricted to `Std_p` for p=3,4,5 and vanishes in all three cases.
4. **Nonorthogonal increment:** a valid chain was mutated to `B_bad=B+A`; the same chain validator accepts the good chain and rejects the mutated chain.
5. **Single-chain-only:** the all-chain validator rejects a list truncated to one maximal chain while accepting the full set of 20.
6. **Nonlinear-beta overclaim:** the source-authority object authorizes only `tangent_O_r2`; an injected `exact_global` beta claim is mechanically rejected.
7. **Finite-part/scale promotion:** a structured interpretation claim asserting unique finite part and fixed subtraction scale is rejected.
8. **Global patching promotion:** a structured claim asserting unique nonlinear defining function / all-strata global patching is rejected.

All these control outcomes are emitted as explicit witnesses in the production JSON, rather than aliases to positive predicates or theorem prose.

## Scientific result

Within the frozen all-`j=1/2` local common-collision scope, the source small-boost geometry together with the authoritative barycentric forest projectors determines a unique invariant **tangent/tubular radial quadratic basis** on each K3/K4/K5 normal fiber, up to the already-frozen overall normalization tied to source rapidity convention.

This does **not** determine a finite part or a physical extension. It only restores the local radial-geometry input that the earlier implementation failed to certify correctly.

## Dependency effect

The prior reason for `ITER083M_FROZEN_NEGATIVE_CONTROL_REPAIR` is repaired at the Researcher implementation level.

However, repository authority should not yet promote Iter083N. The controlling Critic handoff required **terminal repaired Iter083M plus independent Critic review** before rerunning Iter083N. Therefore Iter083N remains `INVALID_PROVENANCE`, and Iter083O remains preparation-only, until an independent Critic reviews this repaired production.

## Interpretation ceiling

No physical finite-part selector; no source-authorized analytic continuation; no exact global nonlinear radial function; no all-strata global renormalization; no regulator dependence or independence theorem; no generic-spin theorem; no unique K5 extension; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.
