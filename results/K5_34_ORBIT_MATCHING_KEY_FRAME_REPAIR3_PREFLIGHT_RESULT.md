# K5 34-orbit matching-key frame repair3 preflight — terminal result

Date: 2026-09-19

Terminal classification: **`PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT`**.

This is an implementation-only preflight. `scientific_verdict=null`; resolver scientific authority remains `0/64`.

## Frozen authority

Parent preflight prereg: `4ee6c6f3056c5934a5209a4f05616b73354b4e6e`.

Control repair1 prereg: `a05e1e29d2f39b678b2cf5f6b187cc165c787f9d`.

Control repair2 namespace prereg: `e4ecce03cbe5df09afcb858480e582fa7b0c9b9e`.

Repair3 key-frame core: commit `6691528d556247f1e8f9cae41f5559993077e15e`, blob `180d2a0248b6473abd9489654abcea8777844894`.

## Terminal production

- run `35414831103`;
- job `105821292023`;
- head `44a1bbed625a3d5ce77ec4d1d57c2c6b35bebf44`;
- workflow conclusion `success`;
- artifact `10575263328`, `k5-34-orbit-matching-key-frame-repair3-preflight-control-repair2`;
- ZIP SHA256 `6220218a1a5e596a7c03a5cb0fe209f3eb814c30153c0a80d99394b78c1fe824`;
- repaired result SHA256 `50311f2588be4dc3eecd29114fe54940af8844f81a0e7093949e8b2b83f0c304`;
- immutable raw-base SHA256 `ac23e157e2c7cdd6b0f9f31233e033a9f2470279a9e484c19c8b292b8308431b`.

The raw base still carries the known pre-wrapper `INVALID_IMPLEMENTATION_OR_PROVENANCE` label because its direct G8 run lookup is deliberately repaired only by the prospectively frozen control wrapper. The repaired terminal classification is the preflight authority.

## Exact all-945 certificate

All frozen census/relation checks pass:

- canonical, pullback and target matching supports each contain exactly 945 perfect matchings;
- forward matching map is a bijection on all 945 and inverse roundtrip is exact;
- repair1 pullback table equals canonical coefficients on all 945 old-frame keys;
- pushed target table obeys `MC_target[P(mt)] = MC_pullback[mt] = MATCH_COEFF[mt]` on all 945;
- the exact coefficient-value multiset is unchanged;
- every coefficient scalar remains a `Fraction`.

Canonical/pullback table SHA256: `cee5a38677919965c66a785349286163b4ebd5dda8731bcdccdc71eec2543cbc`.

Pushed target table SHA256: `0fadf222c22368dfac0f0c1e2ea93774ad9c103ed1506685292152e49cbe182b`.

## Frozen G8 lane

For mask `1`, ray `W1`, cycle `C=(1,2,3,4,0)`, all H1-H6 controls remain exact and H7 becomes exact using only the pushed target-key lookup. Geometry/covariance base transport remains unchanged with common SHA256 `caecba00c3bfc406c3acc5f648e6360a7c2f2bb943e47508ee4fbefce771222a`.

Frozen old matching:
`((0,1),(2,3),(4,5),(6,7),(8,9))`.

Forward target matching:
`((0,6),(1,9),(2,3),(4,5),(7,8))`.

Correct old/repaired-target coefficients:
- channel 1 `(-96/5,0)`;
- channel 2 `(-4144/15,0)`.

Malformed direct pullback-as-target lookup remains:
- channel 1 `(32,0)`;
- channel 2 `(-272/3,0)`.

## Negative controls

All mandatory malformed controls reject independently: direct pullback-as-target lookup, inverse matching map, extra global minus, deterministic first-two target-key swap, and coefficient mutation with otherwise-correct keys.

## Firewalls and ceiling

`q18_values_used=false`, `N_B_orders_or_coefficients_used=false`, `heavy_resolver_launched=false`.

No N/B coefficient/order is promoted. No q18 verdict is created. No global Stokes/IBP, period, finite-part selector, regulator-independence, downstream CRQN, new-physics or complete-QG claim follows.

This terminal PASS authorizes only a separately frozen implementation-only heavy resolver repair3 that substitutes the pushed target-key matching table at the existing S5 target route while leaving the parent scientific contract unchanged.
