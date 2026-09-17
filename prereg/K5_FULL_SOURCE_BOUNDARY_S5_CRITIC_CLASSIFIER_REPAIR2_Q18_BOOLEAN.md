# K5 full-source Boundary-S5 independent Critic — classifier repair2 (q18 boolean semantics only)

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR2 IMPLEMENTATION OR RETRY**.
Date: 2026-09-17

## Parent authority

Scientific contract remains `prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md`, commit `cf8576acb7237b751c26d5b5942aa60874bcd00e`.

Independent reconstruction remains exactly commit `64a4f4935d0238d67e2d60e0b202f81f1195330a`, blob `948f32653872e0920b4450d60d56d48a2a0cc24d`.

Repair1 execution run `35267187779` is terminal `INVALID_IMPLEMENTATION`; its substantive diagnostic values have no scientific authority. Durable diagnosis: `status/K5_BOUNDARY_S5_CRITIC_CLASSIFIER_REPAIR1_INVALID_Q18_FLAG.md`, commit `5c9db0c0e756fbdaa2e9db1e7200d8d0b3e02dfd`.

## Frozen repair2

Change **only** implementation-validity evaluation of the base `forbidden_checks` map:

- positive absence-of-forbidden-method controls (`no_numerical_schwinger_witness`, `no_interpolation`, `no_floating_tolerance`, `no_fitted_phase_or_character`, `no_fitted_2x2_channel_matrix`, `no_researcher_result_import`, `no_researcher_symbolic_implementation_import`, `pre_invariant_dual_full32_object`) must all be `true`;
- `q18_values_used` is a negatively phrased datum and must be required explicitly to be `false` only through the frozen `q18_not_used` control.

Do not include `q18_values_used` inside `all(bool(v) for ...)`.

## Explicit no-change lock

Repair2 MUST NOT change:

- source files/hashes;
- parent/repair prereg identities;
- independent reconstruction implementation;
- S5 generators, group action, endpoint transpose, reversal signs or orientation conventions;
- 32 boundary components, 100000 source terms or 945 matchings;
- malformed controls;
- implementation-validity A members other than the boolean aggregation described above;
- **any substantive theorem B member or its truth criterion**;
- refutation-witness requirements;
- the four frozen terminal classifications;
- interpretation ceiling.

## Retry rule

After implementing the one semantic correction, execute the complete independent reconstruction again from scratch. Do not reuse raw scientific values from run `35267187779`.

Allowed terminal classes remain exactly:

- `CONFIRMED_EXACT_SCOPED`;
- `REFUTED_EXACT_SCOPED`;
- `BLOCKED`;
- `INVALID_IMPLEMENTATION`.

Green CI alone is not science; validate the complete repaired result artifact and hashes before terminalizing.
