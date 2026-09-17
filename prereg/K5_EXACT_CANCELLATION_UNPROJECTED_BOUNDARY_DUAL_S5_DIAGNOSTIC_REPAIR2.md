# K5 exact cancellation unprojected boundary-dual S5 diagnostic — execution repair 2

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR-1 OR REPAIR-2 OUTPUT**.

Parent diagnostic preregistration: `41f26f8e314f4ab1213fe6a681b69d2c87e00d68`.
Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Cancelled original production: run `35175131496`, job `105055061459`.
Repair-1 preregistration: `fa0eb9027a7df8138a6cef734ef75fbf43200815` (alpha-tuple memoization only; outcome unseen when this repair was frozen).

## Concrete execution defect

The original exact diagnostic exceeded its 20-minute workflow budget. Static inspection of the already-frozen source implementation shows that its 100000 authoritative source terms are stored as `(types, coefficient)` pairs, while the exact Wick contraction depends on a term only through `types` and enters linearly in the coefficient.

Thus repeated identical `types` keys inside a fixed boundary-state index cause deterministic repeated exact arithmetic without adding information.

## Frozen repair

Repair 2 is execution-only and preserves the parent mathematical object exactly:

1. Before any alpha/witness evaluation, traverse every one of the original 100000 source terms exactly once.
2. Within each of the 32 boundary-state indices, group terms by the complete 10-edge `types` tuple and sum their coefficients in exact `Fraction` arithmetic.
3. Retain nonzero aggregated coefficients only; exact-zero grouped coefficients are removed only after exact rational summation.
4. Record both original source-term count and compressed key count. Require original count exactly `100000` and all 32 boundary-state indices preserved.
5. Evaluate the same Wick function on the compressed exact linear combination.
6. In addition, memoize complete `unprojected(alpha)` by exact alpha tuple as in repair 1, requiring exactly 6 unique evaluations for W1/W2 with cycle/inverse images.
7. No physical-corner coefficients are used.
8. Do not change W1/W2, S5 cycle/inverse, reduced-Laplacian authority, 32-state representation, local/global action matrices, Reynolds projector, pivot coordinates, weighted compressed coordinates, four predetermined representation laws, or classifier.

## Equivalence controls

The production payload must verify:

- original source count is exactly 100000;
- all 32 boundary-state indices occur before and after compression;
- every compressed coefficient is the exact sum of all original coefficients with the same `(boundary index, types)` key;
- no floating-point arithmetic or threshold is introduced;
- exactly 6 distinct alpha tuples are evaluated and two duplicate base calls are cache hits.

This repair does not authorize a new scientific classifier. Terminal interpretation remains exactly the parent diagnostic classifier. Green CI alone is not scientific PASS.
