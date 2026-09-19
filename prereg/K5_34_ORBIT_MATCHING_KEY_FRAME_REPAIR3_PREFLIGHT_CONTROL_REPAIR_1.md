# K5 34-orbit matching-key frame repair3 preflight — control-only repair 1

Date: 2026-09-19
Role: AUTOMATION B / MSQGR Adversarial Critic
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR OR RETRY**

## Parent preflight contract

Parent preflight remains unchanged:

`prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_CONTROL_REPAIR_3_PREFLIGHT.md`, commit `4ee6c6f3056c5934a5209a4f05616b73354b4e6e`.

Parent repair3 core commit: `6d6dd17e579d7aeb2a793bfa1becbe611174f191`.
Parent preflight implementation commit: `7b4dab8b0de253931db628d7726ee74d92dcba52`.

Run-1 terminal authority:

- run `35414228669`;
- job `105819570539`;
- artifact `10575960402`;
- ZIP SHA256 `a3667d77cc92e9bd8049d0463b26bce2f6618e3e0fd694f2dddd8cff7a85dac1`;
- result JSON SHA256 `1d9f2ec87f6ea1b9936d964f5c32323cc111218df26cfb8eaebf1b13185e8e3a`;
- classification `INVALID_IMPLEMENTATION_OR_PROVENANCE`.

Durable run-1 diagnosis: `status/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_RUN1_INVALID.md`.

## Frozen defect

The only observed validity defect is an incorrect lookup path for the already-terminal independent G8 Critic production run.

The repair3 core/preflight currently evaluates run lock through

`auth.get('provenance', {}).get('run_id') == 35412815680`.

However the raw authority file

`results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json`

has no `provenance` member. Its durable raw blob is `a738852e012f0d7e9b157ab9a1517df3696e6993`, created at commit `daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7`.

The independent production run `35412815680` is durably recorded in

`status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md`, commit `81b85171bb2432438b853bca37cca7bafa3c8d2e`.

## Frozen control-only repair

Change only provenance validation:

1. add the terminal G8 Critic provenance file as an explicit required authority;
2. lock its expected authority commit as a constant;
3. require its text to contain the exact terminal production run `35412815680`, job `105815631932`, result JSON SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13`, and raw authority commit `daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7`;
4. lock the raw authority blob SHA1 `a738852e012f0d7e9b157ab9a1517df3696e6993`;
5. replace the invalid nested `auth['provenance']['run_id']` lookup with these durable authority checks.

## Explicit no-change lock

Repair 1 MUST NOT change:

- the matching-key pushforward `MC_target[P(mt)] = MC_pullback[mt]`;
- any coefficient value;
- source object or source ordering;
- endpoint/orientation conventions;
- covariance or geometry construction;
- 945 matching set or forward matching map;
- all-945 census/relation checks;
- G8 H1-H7 definitions;
- malformed direct-pullback, inverse-map, extra-minus, key-swap or coefficient-mutation controls;
- q18/N-B firewalls;
- the three frozen preflight classifications;
- interpretation/promotion ceiling.

Run-1 all-945/H7 outputs may not be used to alter any acceptance criterion.

## Retry rule

After implementing this provenance-only correction, execute the complete dedicated preflight again from scratch. Do not reuse run-1 output as the repaired result.

A heavy resolver remains forbidden unless the repaired retry terminally returns `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` with all frozen validity, census/relation, G8 and malformed-control maps true.
