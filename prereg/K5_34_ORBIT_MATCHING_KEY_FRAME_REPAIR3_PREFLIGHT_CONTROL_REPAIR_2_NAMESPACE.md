# K5 matching-key repair3 preflight — control-only repair 2: authority namespace binding

Date: 2026-09-19
Role: AUTOMATION B / MSQGR Adversarial Critic
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR OR RETRY**

## Parent authority

Parent repair3 preflight contract remains commit `4ee6c6f3056c5934a5209a4f05616b73354b4e6e`.

Control repair1 remains commit `a05e1e29d2f39b678b2cf5f6b187cc165c787f9d`; run `35414481158` remains terminal `INVALID_IMPLEMENTATION_OR_PROVENANCE`.

Outcome-blind static diagnostic prereg commit `a42ae5afb4742211f96b7cca41efce274bb398e6`; terminal diagnostic run `35414672193` identifies the remaining implementation defect exactly. Durable diagnosis: `status/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_STATIC_VALIDITY_DIAGNOSTIC_RESULT.md`.

## Frozen defect

The repair3 core defines G8 Critic authority names and then broadly re-exports every non-dunder name from repair1 using `globals()[name]=...`. This overwrites generic repair3 names such as `CRITIC_AUTH`, `CRITIC_RUN` and `CRITIC_CLASS` with inherited Boundary-S5 values.

The resulting static failures are purely authority-binding failures:

- `label_frame_critic_raw_blob_locked=false`;
- `label_frame_critic_run_locked=false`;
- `label_frame_critic_N_B_unused=false`.

Every inherited parent control and every scientific/preflight relation remains true; q18/N-B data flags remain intentionally false.

## Frozen repair

Change only the namespace binding of repair3-specific authority data after the repair1 re-export, by either:

1. using uniquely prefixed constants/paths such as `G8_CRITIC_AUTH`, `G8_CRITIC_RUN`, `G8_CRITIC_CLASS`; or
2. restoring the repair3 authority bindings immediately after the inherited re-export.

The repaired static checks must read exactly:

- raw G8 Critic authority `results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json`, blob SHA1 `a738852e012f0d7e9b157ab9a1517df3696e6993`, authority commit `daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7`;
- terminal G8 Critic provenance `status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md`, authority commit `81b85171bb2432438b853bca37cca7bafa3c8d2e`;
- G8 classification `K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED`;
- run `35412815680`, job `105815631932`;
- result JSON SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13`;
- `q18_values_used=false` and `N_B_orders_or_coefficients_used=false`.

## Explicit no-change lock

Repair 2 MUST NOT change:

- matching-key pushforward or any table key/value relation;
- any coefficient value;
- source object/order;
- endpoint transpose or orientation signs;
- covariance/geometry arithmetic;
- all-945 census/relation checks;
- G8 H1-H7 definitions;
- malformed controls;
- q18/N-B firewalls;
- the three frozen preflight classifications;
- promotion ceiling.

The intentionally false data fields `q18_values_used` and `N_B_orders_or_coefficients_used` remain data, not positive validity predicates, and continue to be checked separately as `...not_used=true`.

## Retry rule

After the namespace-only correction, execute the complete repaired preflight again from scratch through the already-frozen control-repair wrapper. Do not reuse run-1/run-2 scientific or control outputs as the retry result.

A heavy resolver remains forbidden unless the retry terminally returns `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT`, every positive validity/census/G8/malformed control is true, q18/N-B remain unused, and the terminal artifact is independently reviewed.
