# Prospective independent Critic preregistration — G8 matching-coefficient label-frame relation

Date: 2026-09-19
Role: AUTOMATION B / independent adversarial Critic
Status: **FROZEN BEFORE IMPLEMENTATION OR OUTPUT**

## Parent authorities

Current repository state supersedes the stale Boundary-S5 target prompt. Boundary-S5 is already independently closed and must not be reopened.

Frozen parent G8 diagnostic prereg:

`a9781b3c6b61ecaa1940ae796ae0a68b9b29c9b6`

Terminal parent G8 production:

- run `35411497229`;
- job `105811869437`;
- head `d87f8ed389f0cf418e1ec0abd49077604c73f853`;
- artifact `10573657808`;
- artifact ZIP SHA256 `168c0826839c7480dd6fb0df0e6bf7711361fdd7c46d9b75e396640f0075ae59`;
- raw `g8_diagnostic.json` SHA256 `a706245b311c9e8d4b573747724fd75cd0ccb7efc5e09a63485addafe1a72361`;
- classification `K5_G8_DEFECT_FINAL_MATCHING_CONTRIBUTION`.

The parent has H1-H6 exact and H7 false on the frozen lane `mask=1`, `W1`, cycle `C=(1,2,3,4,0)`, matching `((0,1),(2,3),(4,5),(6,7),(8,9))`. Geometry/covariance factor transport is therefore frozen as already localized upstream; this diagnostic must not alter it.

Corrected post-collapse parent authority remains commit

`3ec5862258da84c25309c8ee091e6b752a246f66`.

## Frozen question

Determine whether the H7 mismatch is specifically a **matching-table label-frame error**: the repair-1 source matching object is generated from `transport_target_key_to_old(...)` and is therefore keyed in the pullback/old-edge frame, but the G8 target comparison indexes it by the forward target matching `TMT` as though the table itself were target-frame keyed.

Do not infer the answer from comments or prior narrative. Decide from exact table identities and exact matching-map relations.

## Frozen objects

Use unchanged repository objects:

- canonical `MATCH_COEFF` from `scripts/k5_34_orbit_exact_leading_coefficient_core.py`;
- repair-1 `S5_MATCH_COEFF_CYCLE` from `scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py`;
- repair-2 `S5_MATCH_COEFF_CYCLE` only as a no-go consistency control, never as a scientific replacement;
- canonical cycle `C=(1,2,3,4,0)`;
- all 945 retained perfect matchings;
- frozen first G8 matching above.

No q18 value, N/B leading coefficient/order, heavy-resolver shard payload, or downstream physical result may be read or emitted.

## Exact constructions

Define the exact forward matching map

`P(mt) = sorted({ canonical unordered pair (ep_C(i),ep_C(j)) : (i,j) in mt })`.

Define a target-frame pushforward of the repair-1 pullback table by

`MC_push[P(mt)] = S5_MATCH_COEFF_CYCLE[mt]`

for all 945 matchings, rejecting any non-bijection or key collision.

Compare three relations exactly:

### L1 — pullback-frame identity

Check whether repair-1 `S5_MATCH_COEFF_CYCLE[mt] == MATCH_COEFF[mt]` for all 945 old-frame matchings. Record the deterministic lexicographically first mismatch if not exact.

### L2 — correct forward target covariance

Check whether

`MC_push[P(mt)] == MATCH_COEFF[mt]`

for all 945 matchings. This is the target-frame relation induced by a pullback-keyed table.

### L3 — direct-as-target relation used by parent H7

Check whether

`S5_MATCH_COEFF_CYCLE[P(mt)] == MATCH_COEFF[mt]`

for all 945 matchings, and separately on the frozen first matching. Record the deterministic first mismatch and exact channel coefficients.

### L4 — H7 contribution repair on frozen lane

Without changing geometry or covariance, reuse the parent exact old/target matching bases. Compare:

- parent direct lookup contribution using `S5_MATCH_COEFF_CYCLE[TMT]`;
- frame-corrected target lookup using `MC_push[TMT]`.

The corrected lookup may be accepted only if the parent geometry base transport remains exact and the corrected full frozen matching contribution equals the old contribution exactly.

### L5 — repair-2 no-go consistency

Check whether repair-2 collapsed `S5_MATCH_COEFF_CYCLE` equals repair-1 collapsed `S5_MATCH_COEFF_CYCLE`, as reported by the terminal source-collapse no-go. This is a provenance/consistency control only and cannot override L1-L4.

## Mandatory validity controls

- parent G8 run/classification/hash locks exact;
- parent H1-H6 all true and H7 false;
- parent q18 unused and N/B coefficients/orders unused;
- 10-edge ordering unchanged;
- 945 canonical matchings and 945 repair-1 transported matching keys;
- all matching keys are perfect matchings of edge slots `0..9`;
- forward matching map is a bijection on all 945 matchings;
- forward/inverse matching-map roundtrip exact on all 945;
- all matching coefficients exact `Fraction` values;
- repair-1 source term census remains exactly 100000;
- no numerical tolerance, interpolation, fitted phase/character, adaptive support, or post-output convention change.

## Mandatory malformed controls

1. Treat the pullback table directly as target-frame keyed; this malformed route must be rejected on at least one matching if label-frame correction is substantive.
2. Use the inverse edge permutation where forward `P` is required; this must be rejected.
3. Apply an extra global minus sign to the pushed table; this must be rejected.
4. Swap the target keys of the deterministic first two lexicographic matchings; this must be rejected.

## Frozen classifications

After all validity/malformed controls pass:

- `K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED` iff L1 and L2 are exact, L3 fails (including the frozen parent matching), and L4 is repaired exactly by the pushforward lookup.
- `K5_G8_MATCHING_COEFF_VALUE_RELATION_DEFECT` iff the exact pushforward table L2 still fails or L4 remains false, with machine-readable first exact coefficient mismatch.
- `K5_G8_MATCHING_COEFF_DIRECT_TARGET_RELATION_EXACT` iff L3 is exact, contradicting the proposed label-frame diagnosis; record the exact parent inconsistency rather than changing criteria.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` if any required authority, exact-census, bijection, arithmetic, or malformed control fails.

No other terminal class is allowed. Criteria may not change after output is visible.

## Interpretation ceiling

This is implementation-only localization of the already-frozen G8/H7 resolver control path. Even `K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED` does not authorize a heavy resolver run by itself. It may only authorize a separately prospectively frozen minimal implementation repair and a dedicated preflight.

Resolver scientific authority remains `0/64`. No N/B order, q18 verdict, global Stokes/IBP, K5 period, finite-part selector, regulator-independence theorem, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim is authorized.
