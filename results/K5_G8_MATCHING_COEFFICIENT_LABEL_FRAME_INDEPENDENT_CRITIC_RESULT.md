# K5 G8 matching-coefficient label-frame relation — independent Critic result

Date: 2026-09-19

Terminal classification: **`K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED`**.

This is an implementation-diagnostic result only. It is not a physical N/B verdict and does not authorize a heavy resolver run by itself.

## Parent authority

The current repository state had already closed Boundary-S5 independently. The active frontier was the frozen G8 matching-covariance composition diagnostic.

Parent G8 production:

- prereg commit `a9781b3c6b61ecaa1940ae796ae0a68b9b29c9b6`;
- implementation commit `8c0b2d7d4efb266be7cac2a9cd07c6e55de36713`;
- run `35411497229`;
- job `105811869437`;
- head `d87f8ed389f0cf418e1ec0abd49077604c73f853`;
- artifact `10573657808`;
- ZIP SHA256 `168c0826839c7480dd6fb0df0e6bf7711361fdd7c46d9b75e396640f0075ae59`;
- raw JSON SHA256 `a706245b311c9e8d4b573747724fd75cd0ccb7efc5e09a63485addafe1a72361`;
- classification `K5_G8_DEFECT_FINAL_MATCHING_CONTRIBUTION`.

That parent established H1-H6 exact and H7 false on mask `1`, ray `W1`, cycle `C=(1,2,3,4,0)`, frozen matching

`((0,1),(2,3),(4,5),(6,7),(8,9))`.

## Prospective Critic contract and implementation

Critic preregistration was frozen before implementation/output at commit

`e0b8432e71b97cd169a909c27d1a93b92d9f0ef5`.

Independent implementation:

- file `scripts/critic_k5_g8_matching_coefficient_label_frame_relation.py`;
- implementation commit `1bca635917504fac167c2ac5646775b1b5c223a8`;
- implementation blob `b554769a3d8f5645a2e2f62bd93115b9601427b7`;
- pre-execution provenance commit `7f180552571dc834651f1be63ed28f95b0c79388`.

No result from the new Critic diagnostic was consumed before these locks were persisted.

## Terminal independent production

- run `35412815680`;
- job `105815631932`;
- head `4ece5b57517c620084c8e404e5e43cbf66e95245`;
- workflow conclusion `success`;
- artifact `10574960563`, `k5-g8-matching-coefficient-label-frame-critic`;
- artifact ZIP SHA256 `5bc931a7bb0cb11e4b2a131a8d42f2b172182a040701366d471b32614ca55aba`;
- `critic_g8_label_frame.json` SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13`;
- stdout SHA256 `012204d240afd84c48f131e194e5fb30c22cf4795f212ba08269544e242dbe5f`;
- exit-code file SHA256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`;
- runner exit code `0`.

Raw terminal payload is durably mirrored at

`results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json`.

## Exact diagnosis

The independent Critic derived the ten-edge permutation directly from the canonical edge list, verified agreement with the authoritative S5 edge map, and constructed the forward matching permutation on all 945 retained perfect matchings.

The forward matching map is a bijection on all 945 matchings and its inverse roundtrip is exact on all 945.

Let `P(mt)` be the forward target matching under `C` and let the repair-1 matching table be `MC_pull`.

The exact relations are:

1. **L1 pullback-frame identity: PASS**

   `MC_pull[mt] = MATCH_COEFF[mt]`

   for all 945 old-frame matchings.

   Canonical table SHA256 and pullback-table SHA256 are both

   `cee5a38677919965c66a785349286163b4ebd5dda8731bcdccdc71eec2543cbc`.

2. **L2 correct target pushforward: PASS**

   Defining

   `MC_push[P(mt)] = MC_pull[mt]`,

   the exact target-frame relation

   `MC_push[P(mt)] = MATCH_COEFF[mt]`

   holds for all 945 matchings.

   Pushforward table SHA256:

   `0fadf222c22368dfac0f0c1e2ea93774ad9c103ed1506685292152e49cbe182b`.

3. **L3 direct pullback-as-target lookup used by parent H7: FAIL**

   `MC_pull[P(mt)] = MATCH_COEFF[mt]`

   is false.

   On the frozen parent matching, canonical old coefficient is

   - channel 1: `(-96/5, 0)`;
   - channel 2: `(-4144/15, 0)`.

   The malformed direct lookup at target key gives

   - channel 1: `(32, 0)`;
   - channel 2: `(-272/3, 0)`.

   The corrected pushforward lookup at the same target key returns exactly the canonical old coefficient.

4. **L4 frozen H7 contribution: REPAIRED EXACTLY by label pushforward**

   Parent geometry/covariance base transport remains exact; old and target base hashes are both

   `caecba00c3bfc406c3acc5f648e6360a7c2f2bb943e47508ee4fbefce771222a`.

   The parent direct lookup contribution is unequal, while the corrected pushforward lookup contribution equals the old contribution exactly.

5. **L5 repair-2 source-collapse consistency: PASS**

   The collapsed repair-2 matching table equals the repair-1 pullback table exactly, consistent with the earlier source-collapse no-go. Its SHA256 is again

   `cee5a38677919965c66a785349286163b4ebd5dda8731bcdccdc71eec2543cbc`.

Thus the remaining G8/H7 discrepancy is not a covariance geometry failure and not a coefficient-value failure. It is an exact **matching-table key/frame mismatch**: an old/pullback-frame table was consumed as though its keys were forward target-frame labels.

## Validity and negative controls

Every frozen validity check passes, including:

- exact parent run/job/head/artifact/hash locks;
- parent H1-H6 true and H7 false;
- q18 unused and N/B leading values/orders unused;
- ten canonical edges;
- 945 canonical and 945 pullback matchings;
- every key is a complete perfect matching of slots `0..9`;
- forward-map bijection and inverse roundtrip on all 945;
- exact `Fraction` coefficients;
- exactly 100000 source terms.

Every mandatory malformed control is rejected:

- direct pullback table treated as target-frame keyed;
- inverse edge permutation used where forward map is required;
- extra global minus sign;
- swapping the target keys of the first two lexicographic matchings.

## q18 and scientific ceiling

`q18_values_used=false`.

No N/B leading coefficient or order was consumed or emitted. No heavy resolver shard payload was consumed.

Resolver scientific authority remains `0/64`.

This result does not authorize global Stokes/IBP, K5 periods, finite-part/joint selection, regulator independence, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

## Consequence

A minimal implementation-only repair is now justified: preserve the exact matching coefficients but push the matching-table **keys** into the target frame before the target route/covariance comparison. That repair must be prospectively frozen before code changes and must pass a dedicated preflight. Heavy resolver production remains forbidden until such a preflight is terminal and valid.
