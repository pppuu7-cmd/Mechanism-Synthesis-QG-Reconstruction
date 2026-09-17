# K5 mask-511 unscaled-edge leading-covariance zero theorem — terminal exact result

Date: 2026-09-17

## Authority

Prospective preregistration: `prereg/K5_MASK511_UNSCALED_EDGE_LEADING_COVARIANCE_ZERO.md`, commit `e2a9fa293e9d442c3261a816aaef1b4a6b4d5aef`.

Implementation commit: `190e475905ed8252f7183b6856aa65c35fbe7a51`.
Workflow/head: `043a47adb4ada8baa31813b47a67266dff72c3b4`.
Production run: `35265139804`, job `105350321664`, terminal success.
Artifact: `10515789933`, ZIP digest `sha256:2f04456141a58bcc5ca8e047a1f03ba225fca335b2e8b3b6a9c0f8acb2396f1a`.
Result JSON SHA256: `afd6d1f6c9bcd8a6fe2794fdfcad52e2cbc7b93123c934dc236f7e57ee77e23f`.
Durable machine authority: `results/raw/k5_mask511_unscaled_edge_leading_covariance_zero_authoritative.json`.

## Terminal classification

`PASS_EXACT_SCOPED`

`K5_MASK511_UNSCALED_EDGE_FORCES_Q18_ZERO_EXACT_SCOPED`

## Exact structural proof

For mask `511`, canonical edge slots `0,...,8` carry common filtration degree one and canonical edge slot `9`, edge `(3,4)`, is the unique unscaled edge. Its reduced incidence row is

`r_*=(0,0,-1,1)`.

The reduced Laplacian has exact filtration-degree-zero part

`L_0 = alpha_9 r_*^T r_*`.

The exact Kirchhoff determinant begins at filtration degree three while the adjugate begins at degree two. Let

`A_2 = in_2(adj L)`.

Taking filtration degree two in the exact identity

`adj(L)L = det(L) I`

gives

`A_2 alpha_9 r_*^T r_* = 0`.

The executed exact checker independently verified both

`A_2 r_*^T = 0`

and

`r_* A_2 = 0`.

For all source-series orders `n=0,...,4`, the exact minimum-filtration covariance hierarchy therefore has zero covariance whenever one source slot is the unique unscaled edge. The hierarchy is not globally zero: minimum covariances away from edge slot 9 are nonzero.

There are exactly 945 perfect matchings of the ten edge-source slots, and every one pairs slot 9 exactly once. Hence every naive-minimum five-pair Wick product contains one exact zero covariance factor. Therefore the complete physical numerator degree-18 slice vanishes before any use of the retained source/matching coefficients:

`N_{1,18}=0`,

`N_{2,18}=0`

as exact angular-polynomial identities in the frozen mask-511 all-`j=1/2` scope.

## Controls

The malformed control that perturbs the leading adjugate in the `r_*` direction breaks the kernel exactly. The unique unscaled incidence row is nonzero; the leading adjugate is not a trivial all-row kernel; all 945 matchings are exhaustively checked. No q18 production shard value, incomplete q18 aggregate, Boundary-S5 theorem, numerical sampling, tolerance, or interpolation was consumed.

## Relation to active q18 production

Authoritative q18 polynomial production run `35259123078` was already non-terminal when this independent analytic companion gate was prospectively frozen. This theorem neither reads its partial values nor rewrites its frozen contract. The q18 run remains an independent direct construction/aggregate check until terminal.

The new theorem provides a source-independent explanation for the exact q18 cancellation and may be used as an additional terminal structural authority after provenance reconciliation. Combined with the already established structural lower bound, locked nonzero q19 ray coefficients, and terminal annihilator theorem `B_v(F^r) subset F^(r+2)` plus locked nonzero q21 rays, it supports exact mask-511 orders `r_N=19`, `r_B=21` within the frozen scope. This logical combination does not establish another mask or orbit.

## Interpretation ceiling

This result does not establish Boundary-S5 transport, all-orbit cancellation, boundary-flux cancellation, full K5 corner integrability, a global Stokes/IBP relation, invariant-dual K5 periods, a physical finite-part selector, regulator independence, predictive local K5 amplitude, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
