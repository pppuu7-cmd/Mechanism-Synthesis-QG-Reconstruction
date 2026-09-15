# Actual K4 order-3 parity gate — control-only repair 2

Date: 2026-09-15
Status: prospectively frozen after historical run `34994071337` returned `INVALID_IMPLEMENTATION`, before repair/retry.

## Trigger

Run `34994071337` had P1-P8 all true except P0. P0 failed solely because the Critic-result text matcher expected literal phrases (`all R1-R10`, `no K4 polar coefficient`) not present verbatim in the durable Critic note, even though that note records:

- authoritative classification `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED`;
- run `34993531171`, job `104463943299`, artifact `10406716330`;
- `All C1-C10 checks and the exact R1-R10 state check are true`;
- scope statement that the confirmation `does not itself compute that coefficient` and only authorizes a new prospectively frozen K4 coefficient gate.

This is a control/provenance matcher defect. Run `34994071337` is permanently `INVALID_IMPLEMENTATION` and has no scientific verdict.

## Frozen repair

Change only the Critic authority matcher. It must require the exact durable classification, run/job/artifact identifiers, the actual sentence that C1-C10 and exact R1-R10 state check are true, and the actual no-computation scope statement. Do not change any parity calculation, degree partition, source object, hypothesis, PASS/FAIL/BLOCKED definitions, malformed controls, or interpretation ceiling.

Historical runs `34993972013` and `34994071337` remain `INVALID_IMPLEMENTATION`.
