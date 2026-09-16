# K5 exact cancellation S5 source-transport diagnostic — terminal result

Date: 2026-09-17

Classification: **`S5_SOURCE_TRANSPORT_IDENTITY_CONFIRMED`**.

This is a source/control result only. It is not a physical corner, Stokes/IBP, or period verdict.

## Prospective authority

Preregistration: `86438c789eac23eabcb68ff6984ccbcc6fc3853b`.
Implementation: `759a244ade832be747575b4e9311d150c36e8fa6`.
Workflow/head: `4c56fc7b80c0608bb91862c56ecb6778eb55b9eb`.
Production run: `35155718756`.
Job: `104994548020`.
Artifact: `10470923264`.
Artifact ZIP SHA256: `0faed05d1e62c3940e4c982765294d4f54dc7ea9fe788a1825cc76db5e38412a`.
Production JSON SHA256: `0a986887cb28f5d14484269fb1b599d297dfbaef4e1f93a8684caef857d978f9`.

## Exact result

The authoritative 32-state source representation was reconstructed without using any physical corner `N/B/U` coefficient. The local S4 actions are complete; the Reynolds projector has exact rank two and pivots `[1,4]`; the frozen cycle action and its inverse multiply exactly to identity; and `A_cycle P=P=P A_cycle`.

For the two physical Reynolds columns `W=(P[:,1],P[:,4])` the vector transport is exactly

`A_cycle W = W I_2`.

Thus the source-derived invariant-vector transport on these two columns is exactly identity; there is no admissible post-hoc nontrivial constant `2x2` channel-mixing repair for the current S5 failure.

The diagnostic also records that treating these same columns naively as ordinary Euclidean covectors is not valid in the non-orthonormal 32-state basis: neither `A_cycle^T W` nor `A_cycle^{-T} W` lies exactly in the span of `W` under the tested column convention. This does not contradict vector invariance; it shows that vector/covector identification cannot be made by a naive transpose in this basis.

## Consequence for the exact cancellation resolver

Completed current-production orbit payloads already show exact agreement between the primary interpolation route and the independent denominator-cleared route while `N/B` S5 full-coefficient covariance fails and purely geometric `U_Z` covariance passes. Since the source-derived rank-two vector transport is identity, the failure cannot be repaired by fitting or inserting a nontrivial two-channel matrix.

The next diagnostic target is therefore the compressed source/Wick S5 transport itself (matching-key / leg-order / orientation conventions), prospectively frozen separately. Until that control is closed, the current exact-cancellation production remains implementation-invalid rather than scientifically PARTIAL/FAIL.
