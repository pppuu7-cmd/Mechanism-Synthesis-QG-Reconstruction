# Provenance ledger — K5 mask-511 unscaled-edge leading-covariance zero theorem

Date: 2026-09-17

## Prospective scientific contract

`prereg/K5_MASK511_UNSCALED_EDGE_LEADING_COVARIANCE_ZERO.md`, commit `e2a9fa293e9d442c3261a816aaef1b4a6b4d5aef`.

The contract was frozen before implementation/result while q18 production `35259123078` was already non-terminal. It explicitly forbids consuming q18 shard/aggregate values, Boundary-S5 transport, numerical sampling or interpolation.

## Source/code locks

Implementation commit: `190e475905ed8252f7183b6856aa65c35fbe7a51`.

Workflow/head: `043a47adb4ada8baa31813b47a67266dff72c3b4`.

Locked inputs include the canonical degree-27 numerator DAG, corrected ten-edge ordering, mask `511`, edge index 9 as the unique unscaled edge `(3,4)`, exact reduced Laplacian/adjugate construction, source order four and the complete 945 perfect-matching census.

No partial output from q18 run `35259123078` was read or consumed by this theorem.

## Terminal production

- run `35265139804`, terminal `success`;
- job `105350321664`, terminal `success`;
- artifact `10515789933`, `k5-mask511-unscaled-edge-q18-zero-theorem`;
- artifact ZIP digest `sha256:2f04456141a58bcc5ca8e047a1f03ba225fca335b2e8b3b6a9c0f8acb2396f1a`;
- production JSON SHA256 `afd6d1f6c9bcd8a6fe2794fdfcad52e2cbc7b93123c934dc236f7e57ee77e23f`;
- all frozen provenance locks, theorem checks and malformed controls passed.

Durable machine summary: `results/raw/k5_mask511_unscaled_edge_leading_covariance_zero_authoritative.json`, commit `2ec32d64b9dc2d428b6c2773bc9406ecf82d72e1`.

Durable result note: `results/K5_MASK511_UNSCALED_EDGE_LEADING_COVARIANCE_ZERO_RESULT.md`, commit `0a5fdd2954be5dac2a79bd4fca4e653a95c507c8`.

## Exact terminal fact

For mask `511`, with scaled edge slots `0,...,8` and unique unscaled slot `9`, reduced incidence row `r_*=(0,0,-1,1)`, the degree-zero reduced Laplacian is exactly

`L_0 = alpha_9 r_*^T r_*`.

The Kirchhoff determinant begins at filtration degree 3 and `adj L` begins at degree 2. With `A_2=in_2(adj L)`, the exact checker verifies

`A_2 r_*^T=0`, `r_* A_2=0`.

For every source-series order `n=0,...,4`, every minimum-filtration covariance incident to source slot 9 therefore vanishes exactly. The hierarchy is nontrivial away from slot 9. All 945 perfect matchings pair slot 9 exactly once, so every naive-minimum five-pair Wick product contains a zero factor.

Thus, before any retained source/matching coefficient is used,

`N_{1,18}=N_{2,18}=0`

as exact angular-polynomial identities in this labeled mask-511 all-`j=1/2` scope.

Terminal classification:

`K5_MASK511_UNSCALED_EDGE_FORCES_Q18_ZERO_EXACT_SCOPED`

with status `PASS_EXACT_SCOPED`.

## Relation to active q18 production

The independently frozen direct q18 construction run `35259123078` remains non-terminal at this reconciliation cut. Its eight shard jobs are still executing exact q18 initial-form computation. It is not duplicated, cancelled or partially consumed. The present theorem is independent structural authority and does not rewrite that run's frozen classification contract.

## Claim ceiling

No theorem for another mask/orbit; no coefficient-level Boundary-S5 confirmation; no full K5 corner-integrability or causal-vertex finiteness/divergence theorem; no global Stokes/IBP; no invariant-dual K5 period; no reduction of `dim_C F_8=377`; no physical finite-part selector; no regulator-independence theorem; no F9/G3/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim. Published spectral `i epsilon` retained.
