# K5 34-orbit matching-key frame repair3 preflight — provenance

Date: 2026-09-19
Status: **PRE-RESULT PROVENANCE; NO N/B SCIENTIFIC VERDICT**

## Controlling authority

Current repository state supersedes the stale Boundary-S5 prompt. Boundary-S5 remains independently closed.

Parent resolver scientific prereg remains `d6b0e805101c8590eafac71398cc2b1466691752`.

Independent G8 matching-label diagnosis remains terminal:

- Critic prereg `e0b8432e71b97cd169a909c27d1a93b92d9f0ef5`;
- run `35412815680`;
- job `105815631932`;
- classification `K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED`;
- result JSON SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13`.

## Prospective repair freeze

Minimal matching-key frame repair3 preflight preregistration:

`prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_CONTROL_REPAIR_3_PREFLIGHT.md`

commit `4ee6c6f3056c5934a5209a4f05616b73354b4e6e`.

The repair changes only matching-table keys by exact forward pushforward

`MC_target[P(mt)] = MC_pullback[mt]`

and leaves coefficient values, source, geometry, orientation, covariance, channels, orbit representatives, W1/W2, 945 matching set, DAG, degree ceilings, projective-normal authority, exact arithmetic and scientific classifier unchanged.

## Implementation frozen before execution

Repair3 core:

`scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py`

commit `6d6dd17e579d7aeb2a793bfa1becbe611174f191`.

Dedicated preflight implementation:

`scripts/k5_34_orbit_matching_key_frame_repair3_preflight.py`

commit `7b4dab8b0de253931db628d7726ee74d92dcba52`.

No workflow output existed when the prereg, core and preflight implementation were frozen.

## Frozen preflight scope

The preflight checks only implementation/control relations:

- all-945 forward matching-key bijection and inverse roundtrip;
- exact pullback/canonical coefficient relation;
- exact pushed-target/canonical coefficient relation;
- exact coefficient-value multiset preservation;
- exact Fraction arithmetic;
- frozen G8 H1-H6 unchanged and H7 repaired only by target-key pushforward;
- malformed direct-pullback, inverse-map, extra-minus, key-swap and coefficient-mutation controls;
- q18 and N/B firewalls.

The preflight does not compute or promote any 34-orbit N/B leading coefficient or order and launches no heavy resolver shard.

## Interpretation ceiling

Even a terminal `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` authorizes only a separately reviewed implementation-only heavy resolver repair using the pushed target-key table. Resolver scientific authority remains `0/64` until a valid terminal aggregate exists.

Global Stokes/IBP, K5 periods, finite-part selection, regulator independence, downstream CRQN promotion, `NEW_PHYSICS_FOUND`, and complete QG remain unauthorized.
