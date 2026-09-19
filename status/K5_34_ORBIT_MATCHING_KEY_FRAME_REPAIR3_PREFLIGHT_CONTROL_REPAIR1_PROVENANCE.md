# K5 34-orbit matching-key frame repair3 preflight — control repair1 provenance

Date: 2026-09-19
Status: **PRE-RETRY PROVENANCE; NO PREFLIGHT PASS AUTHORITY**

## Parent contract

Matching-key repair3 preflight prereg remains commit `4ee6c6f3056c5934a5209a4f05616b73354b4e6e`.

Run 1 is terminal `INVALID_IMPLEMENTATION_OR_PROVENANCE`: run `35414228669`, job `105819570539`, artifact `10575960402`, result SHA256 `1d9f2ec87f6ea1b9936d964f5c32323cc111218df26cfb8eaebf1b13185e8e3a`.

Run-1 durable diagnosis: `status/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_RUN1_INVALID.md`, commit `c15f89b29c99d18858a11fe600392332cc902d1d`.

## Prospective control repair

Frozen control-only repair prereg:

`prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_CONTROL_REPAIR_1.md`, commit `a05e1e29d2f39b678b2cf5f6b187cc165c787f9d`.

The repair changes only durable Critic provenance validation. It does not change matching keys, coefficient values, all-945 relations, G8 H1-H7, malformed controls, firewalls, classifications, or interpretation ceiling.

## Repaired implementation frozen before retry

Repair3 core provenance correction:

`scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py`, commit `ae1e2cf51d7da51ccbcbdbc289d0dc5326802a7c`.

It now validates the independent G8 Critic through:

- raw authority blob SHA1 `a738852e012f0d7e9b157ab9a1517df3696e6993` / raw authority commit `daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7`;
- terminal provenance file `status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md`, authority commit `81b85171bb2432438b853bca37cca7bafa3c8d2e`;
- run `35412815680`, job `105815631932`, result JSON SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13` recorded in that provenance file.

Control-repair wrapper:

`scripts/k5_34_orbit_matching_key_frame_repair3_preflight_control_repair1.py`, commit `09b5a4971e812bce479300b167fabb5632744f3f`.

The wrapper re-executes the complete preflight from scratch to an immutable raw-base JSON, repairs only the prospectively frozen provenance field, records the raw-base SHA256 and independently re-applies the unchanged validity/census/G8/malformed classifier.

No repaired retry output existed when this provenance record was committed.

## Firewalls

No q18 partial values are permitted. No N/B leading coefficients/orders or heavy resolver shard are permitted in the preflight. Resolver scientific authority remains `0/64`.

A heavy resolver remains forbidden unless the repaired retry terminally returns `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` and its artifact/provenance is reviewed.
