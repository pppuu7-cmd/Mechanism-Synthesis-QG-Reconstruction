# K5 34-orbit resolver — minimal matching-key frame control repair 3 preflight

Date: 2026-09-19
Role: AUTOMATION B / MSQGR Adversarial Critic
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION OR PREFLIGHT OUTPUT**

## Current authority

Current repository state supersedes the stale Boundary-S5 prompt. Boundary-S5 is independently closed and must not be reopened.

Parent 34-orbit scientific contract remains immutable:

`prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Repair-1 aggregate remains terminal `INVALID_IMPLEMENTATION` because `S5_full_coefficient_covariance_all=false`; resolver scientific authority remains `0/64`.

Source-support repair-2 remains a terminal preflight no-go: full32 target component reconstruction collapses to the same repair-1 matching coefficient object and therefore does not alter the physical matching values.

Corrected post-collapse diagnostic authority localizes the first downstream failure to G8. Parent G8 run `35411497229` has H1-H6 exact and H7 final matching contribution false on the frozen mask=1/W1/CYCLE lane.

Independent matching-label Critic authority:

- prereg `e0b8432e71b97cd169a909c27d1a93b92d9f0ef5`;
- run `35412815680`;
- job `105815631932`;
- artifact `10574960563`;
- result JSON SHA256 `7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13`;
- classification `K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED`.

It establishes exactly that repair-1 `S5_MATCH_COEFF_CYCLE` is an old/pullback-keyed matching table with correct coefficient values, while the failing target route indexes it by forward target matching keys without first pushing the keys into the target frame.

## Frozen repair

Change **only the key frame** of the S5 matching coefficient table used by the target S5 route.

Let `P(mt)` be the exact forward matching map induced by cycle `C=(1,2,3,4,0)` on canonical edge slots.

Construct

`S5_MATCH_COEFF_CYCLE_TARGET[P(mt)] = S5_MATCH_COEFF_CYCLE_PULLBACK[mt]`

for every one of the 945 perfect matchings.

The repair MUST NOT change any matching coefficient value, source term, endpoint/orientation convention, covariance factor, geometry, physical channel, orbit representative, W1/W2 ray, DAG coefficient, degree ceiling, projective-normal authority, exact arithmetic path, scientific classification rule, or interpretation ceiling.

No coefficient fitting, sign fitting, interpolation, tolerance, adaptive support, or post-output convention change is allowed.

## Dedicated preflight requirements

The repair may not be used by a heavy resolver until one dedicated preflight terminally satisfies all controls below.

### P1 — authority/provenance

- parent scientific prereg commit locked;
- repair-1 source module and matching table available;
- G8 parent and independent label-frame Critic authorities present and exact;
- no q18 partials and no historical invalid heavy-resolver N/B payload consumed.

### P2 — all-945 matching census

- canonical matching support has exactly 945 keys;
- repair-1 pullback table has exactly 945 keys;
- every key is a perfect matching of edge slots `0..9`;
- forward matching map is a bijection on all 945;
- exact inverse roundtrip holds for all 945;
- pushed target table has exactly 945 keys.

### P3 — coefficient-value preservation

For all 945 old-frame matchings:

`S5_MATCH_COEFF_CYCLE_PULLBACK[mt] == MATCH_COEFF[mt]`.

For all 945 target keys:

`S5_MATCH_COEFF_CYCLE_TARGET[P(mt)] == MATCH_COEFF[mt]`.

The multiset of exact channel coefficient values before and after re-keying must be identical. All scalar entries must remain exact `Fraction` objects.

### P4 — frozen G8 lane

Reconstruct the frozen first parent G8 matching

`((0,1),(2,3),(4,5),(6,7),(8,9))`

on mask=1 / W1 / cycle C without changing geometry or signs.

H1-H6 must remain exact under the already-frozen definitions. H7 must become exact **only** by replacing the malformed direct pullback-key lookup with the pushed target-key lookup.

The old and target geometry/covariance matching-base transport relation must remain exact.

### P5 — malformed controls

The following must separately reject:

1. direct use of the pullback table as target-frame keyed;
2. inverse matching-map pushforward instead of the frozen forward map;
3. extra global minus on all pushed coefficient values;
4. deterministic swap of the pushed target keys for the first two lexicographic matchings;
5. mutation of any coefficient value while keeping keys correct.

### P6 — firewalls

- `q18_values_used=false`;
- `N_B_orders_or_coefficients_used=false` for the preflight;
- no heavy resolver shard or aggregate is launched by this preflight workflow;
- no global Stokes/IBP, period, finite-part selector, regulator-independence, F9/G3/G8 scientific promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim.

## Frozen preflight classifications

- `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` iff P1-P6 all pass and the frozen G8 H1-H7 lane is exact with only target-key pushforward changed.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` if any authority/census/arithmetic/firewall/malformed control fails.
- `MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_SCIENTIFIC_MISMATCH` if implementation validity passes but the exact all-945 relation or frozen H7 contribution still fails; record the deterministic first machine-readable exact mismatch.

No other terminal class is allowed.

## Authorization ceiling

A terminal `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` authorizes only a prospective implementation-only resolver repair that substitutes the pushed target-key table at the existing target S5 route. It does not itself authorize any N/B order or coefficient.

A heavy resolver production remains forbidden until the preflight is terminal and its artifact/provenance is reviewed. After a valid terminal PASS, exactly one unchanged-contract heavy repair-3 production may be authorized separately.

Resolver scientific authority remains `0/64` until a valid terminal aggregate exists.
