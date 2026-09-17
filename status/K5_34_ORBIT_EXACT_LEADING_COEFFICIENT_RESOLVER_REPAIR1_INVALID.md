# K5 34-orbit exact leading-coefficient resolver repair-1 — terminal INVALID_IMPLEMENTATION

Date: 2026-09-18 (Europe/Helsinki)

## Frozen parent and repair contracts

Parent scientific preregistration remains immutable:

- `prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`
- commit `d6b0e805101c8590eafac71398cc2b1466691752`

Prospective control-only repair-1:

- `prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_CONTROL_REPAIR_1.md`
- commit `2193692c90d8ee1fa097200dbbac6ab70fd3a159`

## Immutable production

- run: `35271187040`
- attempt: `1`
- head: `42daba28fd0c2545be386f63e89f6bcafdbed9a3`
- run status: `completed`
- run conclusion: `success`
- aggregate job: `105376689955`
- aggregate artifact: `10519073488`
- artifact ZIP SHA256: `6de47e29303091d4cabf48c59591d56634a5817be344e701b3dc435ddb1770db`
- raw `result.json` SHA256: `7c14d5746cf287d9d66872daec6334f2b8c7bb9c9f1430f6456ea3e1a3f1866e`
- canonical decompressed coefficient payload SHA256: `1ebd19078b33cf6936d37d0223f2d58bbfe47d0c4866bdb6c2d7f33a06471c4d`
- gzip coefficient payload SHA256: `0d9cfab20ce5c718c51126b9db8e728d8af31f36f010a5a20b418e646a899fad`
- recomputed `projective_normal_full.json` SHA256: `80e614f10a8fcc0f1e96732ca5cd27feffb7b1683f1e26be3685417635ecaba8`

All eight deterministic shard jobs completed successfully and aggregate completed successfully. Green CI is not the scientific verdict.

## Frozen classifier result

The complete aggregate itself returns:

`classification = INVALID_IMPLEMENTATION`

`status = INVALID_IMPLEMENTATION`

The mandatory failed control is exactly:

`S5_full_coefficient_covariance_all = false`.

All of the following aggregate controls are true: exact eight-shard completion, 32 proper-orbit coverage, complete `N[0..27]` / `B[0..31]` vectors for all 64 channel-orbit rows and both W1/W2 paths, route-internal exact controls, second-path coverage for every frozen `(orbit_size,k)` class, W1/W2 state/order agreement, recomputed projective-normal authority, exact mask511 parent reproduction, and independent Boundary-S5 Critic authority lock.

However the frozen repair-1 contract requires simultaneous physical S5 full-coefficient covariance. Failure of that control forces `INVALID_IMPLEMENTATION` regardless of all other checks.

## Failure surface

The immutable coefficient payload was inspected only for control booleans, not for scientific N/B order interpretation.

All 32 proper orbit rows fail all eight S5 full-coefficient equality checks:

- channel 1 / W1 / N;
- channel 1 / W1 / B;
- channel 1 / W2 / N;
- channel 1 / W2 / B;
- channel 2 / W1 / N;
- channel 2 / W1 / B;
- channel 2 / W2 / N;
- channel 2 / W2 / B.

Thus the defect is systematic across the complete S5 comparison surface, not localized to one orbit/channel/order.

## Scientific firewall

No N/B coefficient, first-nonzero order, exact-zero state, local integrability classification or physical corner verdict from run `35271187040` is authority.

The aggregate field `certified_components=64` is an implementation-internal row certificate and cannot override the failed mandatory S5 control. For scientific authority after this run:

- resolved components: `0/64`;
- unresolved components: `64/64`;
- local physical N/action/flux classification remains blocked.

This is not a scientific refutation of CRQN and is not evidence for finiteness/divergence.

## Immediate admissible next step

Localize the common implementation defect outcome-blind before any new production. The strongest current hypothesis is an S5 source/matching **label-frame mismatch**: repair-1 constructs the theorem's pullback-to-old-label source dictionary and passes it directly into a route evaluated in the permuted target edge frame. This hypothesis is not yet authority and must be tested by a separately frozen implementation-only diagnostic before repair.

Do not rerun the resolver until that diagnostic identifies the exact frame map and a new prospective repair is frozen.

## Claim ceiling

Unchanged: no 34-orbit N/B order authority, no local physical corner classification, no global Stokes/IBP, no K5 period, no physical finite-part selector, no reduction of `dim_C F_8=377`, no regulator independence, no predictive local K5 amplitude, no F9/G3/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, no complete-QG claim.
