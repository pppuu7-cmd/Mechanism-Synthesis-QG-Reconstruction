# Iter077J-SM terminal control repair — exact Q(i) rank and nullspace

**Date:** 2026-09-14

## Provenance

- Original preregistration: `prereg/ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN.md`, commit `e5aae441c84a5d458e1d91dd1f64ab160043dd35`.
- Control-only repair preregistration: `prereg/ITER077J_SM_EXACT_RANK_CONTROL_ONLY_REPAIR.md`, final frozen commit `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`.
- Repair implementation: `distributional/iter077j_sm_exact_rank_control_repair.py`, commit `d0dbde896462ffa897a918bc80995a7e463e753b`.
- Workflow/production head: commit `d9072a636db5ce0a9705f770c92a5876dfc74114`.
- Authoritative repair run: `34789579078`, terminal `completed/success`.
- Bx artifact `10328030657`, digest `sha256:d6d0d8e2267604245e05fb57d640b2ed45aaf3406fa19263474a6cae6c565aae`.
- Cx artifact `10328215382`, digest `sha256:e0ccb7be065004da6a2e627f7462bf4e3b5a1bb4598632fca581d255bca64aef`.
- Dx modular artifacts: `10328075617`, `10328570127`, `10328350398`, `10327835957`.
- Aggregate artifact `10327871709`, digest `sha256:207ce920cb79136dc1f54bb56f8f934c9c1768093ca3e544ef5855b748a79e79`.

## Repaired classification

`ITER077J_SM_FROZEN_MAIN_FULL32_ANGULAR_SPAN_EXACTLY_FAILS_CONTROL_REPAIR_SCOPED`

Scientific verdict under the original frozen main-family hypothesis: **FAIL_CONFIRMED**.

## Exact findings

- Main 40-ray family: exact rank over `Q(i)` = `9`, nullity `23`.
- Main+held-out 56-ray family: exact rank over `Q(i)` = `9`, nullity `23`.
- The exact polynomial-family structural bound is respected: every row component is degree at most 10 in the frozen affine seed, so rank is at most 11.
- An exact nonzero right-null witness is verified on every main row and every combined main+held-out row.
- One especially simple verified witness is the boundary-coordinate difference with coefficients `+1` on lexicographic component index 1 and `-1` on index 2, all other coefficients zero. Thus the two corresponding frozen-family leading angular coefficient functions are exactly identical on all 56 frozen rays.
- The relabelled 960-vector control has modular rank `30` for each frozen inert prime `1000000007`, `1000000087`, `1000000103`, `1000000123`. Because rank deficiency modulo primes does not imply characteristic-zero rank deficiency, no exact rank-deficiency claim is made for Lane D.

## Interpretation ceiling

This exact FAIL is only a property of the prospectively frozen one-parameter angular family. That family was structurally incapable of certifying rank 32. The result does **not** establish a universal angle-independent boundary-state cancellation on arbitrary collision directions, does not define the K5 boundary value, and does not weaken Iter077I's exact nonzero witness/open-angular-patch local L1 obstruction.

It is therefore a closed negative result about the Iter077J test design/hypothesis, not a rescue of the causal vertex.

## Forward effect

Do not repeat neighboring angular-rank families merely to obtain full rank. The authoritative blocker has already moved outward through Iter077L-N to the nonunique integrated K5 extension and the missing refinement/cylindrical/RG selector.