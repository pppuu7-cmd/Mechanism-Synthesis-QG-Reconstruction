# K5 full-source Boundary-S5 symbolic transport — independent Critic result

Date: 2026-09-17

## Terminal scientific classification

`CONFIRMED_EXACT_SCOPED`

Status: `PASS_EXACT_SCOPED`.

The frozen coefficient-level identity

`a_p(p alpha) = A_p^(-T) a(alpha)`

for the complete unprojected order-zero all-`j=1/2` K5 source/boundary Wick covector on the formal domain `Psi_K5 != 0` is independently confirmed in the exact frozen scope, with trivial residual character.

## Frozen contract and implementation history

Parent independent Critic preregistration: `prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md`, commit `cf8576acb7237b751c26d5b5942aa60874bcd00e`.

Independent reconstruction implementation: commit `64a4f4935d0238d67e2d60e0b202f81f1195330a`, blob `948f32653872e0920b4450d60d56d48a2a0cc24d`.

An outcome-blind pre-execution audit found a classifier separation defect before scientific execution was consumed; repair1 was frozen at `2d510ae4ef0dab2e15a763a520864869eff2d71b`. Run `35267187779` was terminal `INVALID_IMPLEMENTATION` only because the wrapper incorrectly treated the required datum `q18_values_used=false` as a failed positive boolean control. That run has no scientific authority.

The defect was diagnosed durably at commit `5c9db0c0e756fbdaa2e9db1e7200d8d0b3e02dfd`; repair2 was prospectively frozen at commit `1440e07b8a3d6295020cba50d0ac73f44d4be641` and changed only that boolean aggregation. The independent reconstruction and substantive theorem-B map were not changed.

## Production authority

- workflow/head: `992a5889656b2cf5925caf1c770824ab557e5833`;
- run: `35267432939`, terminal `success`;
- job: `105357990301`, terminal `success`;
- artifact: `10516529280`, `k5-full-source-boundary-s5-independent-critic-repair2`;
- artifact ZIP digest: `sha256:087ee496daf8a9aafa255d908c062fb8bba2a5481addef10da6d7b4b170cc479`;
- repaired `critic_result.json` SHA256: `b0a0b94e22d76600c27c148c0072741b5e04a8652939ed58a228b9fbebda70ee`;
- raw independent-reconstruction JSON SHA256: `d34ba7fa016e4ac0f9332e2bd41de624c86c92b625b36cb6a7a21065d6062d66`;
- repaired runner blob: `a6922bc72459132ab92e559b6213d4c863e8266a`.

Durable compact machine authority: `results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json`.

## Independent reconstruction coverage

The Critic reconstruction independently recovered and checked:

- canonical ten K5 edges;
- `125` unit-coefficient spanning-tree monomials of `Psi_K5`;
- exact Kirchhoff determinant/tree equality and exact C/T covariance transport;
- exact `32`-dimensional boundary representation;
- group size `120` with exact composition and inverses;
- Reynolds rank `2`, pivots `[1,4]`;
- exact orientation-sensitive edge maps;
- endpoint transpose under canonical reversal;
- exact source reversal sign;
- all `32` source/boundary dictionaries;
- exactly `100000` original source node-choice terms;
- all `945` complete perfect matchings;
- exact complete-Wick orientation/source sign cancellation.

The base dictionary SHA256 is `f220a5023ec6fda4c8f2d82e5b1a6ec80cf657046eb6be22c5db7bafa0a27e2b`. The independently reconstructed `Psi_K5` SHA256 is `9343cf446f95cb8fb95717849355b0afd9f97cd105053118e08b6e8519e1951f`.

## Substantive theorem conditions

All frozen substantive conditions passed exactly:

- C and T source/boundary contragredient dictionaries;
- C and T source-dictionary inverse roundtrips;
- C and T boundary inverses;
- all-120 boundary-representation composition;
- all-120 edge-orientation-map composition;
- C and T `Psi` / covariance-numerator transport;
- C and T orientation factors on all `945` complete matchings.

No failed substantive condition remains.

## Mandatory malformed controls

All frozen malformed controls were detected/rejected:

- omit endpoint transpose;
- omit source-reversal sign;
- omit covariance-orientation sign;
- add extra permutation-sign character;
- historical source-fixed object.

The odd generator T has orientation character `-1`, and the source/covariance sign factors cancel exactly on complete Wick monomials.

## Forbidden-method audit

No numerical Schwinger witness, interpolation, floating tolerance, fitted phase/character, fitted `2x2` channel matrix, Researcher symbolic implementation import, or q18 result was used. `q18_values_used=false`.

## Scientific consequence

The Researcher theorem `K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED` now has terminal independent Critic scientific confirmation at coefficient level in the frozen all-`j=1/2` source/boundary scope.

Therefore the dependency that blocked the already-frozen `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION` is closed. That resolver is now admissible **unchanged**, subject to its own frozen preregistration `d6b0e805101c8590eafac71398cc2b1466691752` and exact provenance/coverage requirements.

## Interpretation ceiling

This result does not establish q18 physics, exact physical cancellation orders on the other orbit components, full K5 integrability, global Stokes/IBP, invariant-dual K5 periods, a physical finite-part selector, reduction of `dim_C F_8=377`, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
