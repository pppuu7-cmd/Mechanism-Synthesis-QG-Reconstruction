# K5 34-orbit matching-key frame repair3 preflight — run 1 terminal INVALID_IMPLEMENTATION_OR_PROVENANCE

Date: 2026-09-19

## Terminal production

- run `35414228669`;
- job `105819570539`;
- head `4b4e9fe68e1c44217a57bbe14e2bbc67e75ad971`;
- workflow conclusion `failure` because the frozen preflight classification was non-PASS;
- artifact `10575960402`, `k5-34-orbit-matching-key-frame-repair3-preflight`;
- artifact ZIP SHA256 `a3667d77cc92e9bd8049d0463b26bce2f6618e3e0fd694f2dddd8cff7a85dac1`;
- `repair3_preflight.json` SHA256 `1d9f2ec87f6ea1b9936d964f5c32323cc111218df26cfb8eaebf1b13185e8e3a`;
- stdout SHA256 `38790a33ba8827a7573f439c31e2000035ec2b0e19851915c5d4d1bd680cd887`;
- exit-code-file SHA256 `53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3`.

Frozen classification:

`INVALID_IMPLEMENTATION_OR_PROVENANCE`.

## Exact failure

Only the provenance aggregation prevents PASS:

- `critic_run_locked=false`;
- consequently `static_repair3_controls=false`.

The preflight implementation attempted to read the independent G8 Critic production run as

`auth['provenance']['run_id']`,

but the durable raw authority `results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json` intentionally contains no `provenance` object. The terminal production run is instead durably recorded by `status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md`, commit `81b85171bb2432438b853bca37cca7bafa3c8d2e`.

This is a provenance-field lookup defect in the new preflight, not a scientific mismatch.

## Outcome-blind exact controls that already pass

Every all-945 and frozen-lane substantive/control relation passed in run 1:

- canonical/pullback/target matching counts are all 945;
- forward matching map is bijective on all 945;
- inverse roundtrip is exact on all 945;
- repair-1 pullback table equals canonical coefficients on all 945 old keys;
- pushed target table obeys the exact target relation on all 945 keys;
- coefficient value multiset is unchanged;
- every pushed scalar remains an exact `Fraction`;
- G8 H1-H6 remain exact;
- G8 H7 becomes exact using only the pushed target-key lookup;
- old/target geometry base transport remains exact;
- direct pullback-as-target, inverse map, extra minus, key swap and coefficient mutation malformed controls all reject.

Frozen table hashes remain:

- canonical/pullback `cee5a38677919965c66a785349286163b4ebd5dda8731bcdccdc71eec2543cbc`;
- pushed target `0fadf222c22368dfac0f0c1e2ea93774ad9c103ed1506685292152e49cbe182b`.

No q18 value and no N/B leading coefficient/order was consumed. No heavy resolver shard was launched. Resolver scientific authority remains `0/64`.

## Required prospective repair

Before any retry, freeze a control-only repair that changes only how the already-terminal independent G8 Critic provenance is validated:

- lock the raw authority blob/commit and terminal provenance file/commit;
- validate run `35412815680` from that durable provenance file;
- do not change the matching-key construction, all-945 relations, G8 H1-H7 definitions, malformed controls, firewalls, classifications or promotion ceiling.

The run-1 exact all-945/H7 values are diagnostic only and cannot be promoted through a repaired retry by changing scientific criteria.
