# Iter077J-SM control-only repair — exact Gaussian-field rank / nullspace certification

**Date:** 2026-09-14

## Status

Prospective control-only repair. This does **not** change the scientific hypothesis, rays, boundary basis, PASS/FAIL criteria, interpretation ceiling, or source object frozen in `prereg/ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN.md`.

## Why repair is required

The original implementation reduced the frozen Gaussian-integer row matrix modulo the inert prime `p=1000000007` and reported the resulting rank as a Gaussian-field certificate. A full rank `32` modulo `p` would indeed certify rank `32` over `Q(i)`, because a nonzero determinant modulo `p` implies the corresponding Gaussian-integer determinant is nonzero in characteristic zero.

The converse is false: rank `<32` modulo one prime does **not** by itself prove rank `<32` over `Q(i)`, because a nonzero characteristic-zero minor may vanish modulo that prime. In addition, the original preregistration explicitly required an exact nonzero right-nullspace witness if the main rank is below 32, while the implementation did not emit one.

Therefore the original Iter077J FAIL classification is not authoritative until the frozen exact-rank requirement is repaired.

## Frozen object

Unchanged from Iter077J-SM:

- source ordering: `one-wedge source construction -> Toller function -> K5 product -> group integration`;
- all ten `j=1/2` wedges;
- all 32 five-node boundary-intertwiner basis components;
- exact stripped Gaussian-integer leading contraction vectors;
- main seeds `0,...,39`;
- held-out seeds `41,...,56`;
- the same 8 main rays and all 120 vertex relabelings for Lane D;
- no ray, basis state, ordering, threshold, or sign convention may change.

## Exact analytic control

For every frozen main/held-out seed `s`, every edge matrix entry is affine in `s` because every coordinate and every relative vector is affine in `s`. The stripped K5 boundary contraction is multilinear in the ten edge matrices. Hence each of the 32 row-vector components is a polynomial in `s` of degree at most 10.

Consequently all rows in the one-parameter main+held-out family lie in the span of at most 11 coefficient vectors over `Q(i)`. This gives an exact a-priori upper bound

`rank_Q(i)(main) <= 11`,

`rank_Q(i)(main + heldout) <= 11`.

This degree bound is admissible because the omitted physical edge factors are common nonzero row scalars for a fixed ray and therefore do not change row-space rank.

## Repair lanes

### Lane Bx — exact main rank and nullspace

Compute exact Gaussian-rational row reduction of the 40x32 main matrix without modular reduction.

Required output:

- exact `rank_Q(i)`;
- pivot columns;
- at least one explicit nonzero exact right-nullspace vector;
- exact verification that all 40 rows annihilate that witness;
- verify `rank_Q(i) <= 11` from the frozen polynomial-degree bound.

Original Iter077J Lane-B PASS iff exact rank is 32. Original Lane-B FAIL iff exact rank is `<32` and an exact nullspace witness is verified.

### Lane Cx — exact held-out combined rank

Compute exact Gaussian-rational rank of all 56 main+held-out rows and verify the same exact nullspace witness (or another exact witness) on all 56 rows.

PASS iff combined exact rank is 32. FAIL iff exact rank is `<32` with exact witness. Verify the exact upper bound `<=11`.

### Lane Dx — relabeling audit without invalid converse

Re-evaluate the 960 relabelled vectors using several fixed inert primes only as **lower-bound/full-rank certificates**.

Frozen primes:

`1000000007, 1000000087, 1000000103, 1000000123`.

All four are prime and `3 mod 4`, so `x^2+1` is irreducible and the Gaussian-pair arithmetic is over the field `F_p(i)`.

For any prime at which rank is 32, exact characteristic-zero rank 32 is certified and Lane D is PASS. If all modular ranks remain below 32, record only the lower bounds obtained; do **not** infer an exact rank deficiency from modular rank alone. Lane D then remains `UNRESOLVED_EXACT_RANK`, but this cannot rescue aggregate PASS if Bx/Cx have an exact FAIL.

## Aggregate repaired interpretation

- If Bx exact rank `<32` with a verified exact right-nullspace witness, the frozen full-span hypothesis is scientifically **FAIL** regardless of Lane D, because the preregistered primary main family fails its target exactly.
- If Bx exact rank is 32, the original modular FAIL is invalid and the remaining original lanes must be reinterpreted under their frozen rules.
- If exact arithmetic cannot complete or the witness does not verify, classification is `INVALID_IMPLEMENTATION` / `BLOCKED_EXECUTION`, not scientific FAIL.

## Interpretation ceiling

Even an exact main-family rank deficiency proves only that this prospectively frozen one-parameter angular family does not span the full 32-dimensional boundary space. It does **not** prove the existence of a universal angle-independent cancellation for arbitrary collision directions. The one-parameter family itself has an exact degree-10 rank ceiling and is therefore structurally incapable of certifying full rank 32.

No causal-vertex finiteness/divergence theorem; no source-selected extension theorem; no regulator-independence theorem; no generic-spin result; no G3/F9/G8/K5 promotion; no complete-QG claim.