# Actual K4 order-3 parity gate — control-only repair 3

Date: 2026-09-15
Status: prospectively frozen after run `34994172757` returned `INVALID_IMPLEMENTATION`, before repair/retry.

## Trigger

Run `34994172757` again had P1-P8 true and P0 false. The exact cause is now identified: helper `require()` Markdown-normalized the file text by removing `_`, `*`, and backticks, but only lower-cased the needle strings. Therefore the required classification `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED` was transformed in the haystack to a string without underscores while the needle retained underscores.

This is a deterministic implementation defect in the authority matcher. Run `34994172757` is permanently `INVALID_IMPLEMENTATION`; no scientific values are promoted from it.

## Frozen repair

Change only helper `require()` so both haystack and each needle are processed by the same `norm()` function before comparison. No scientific object, parity computation, degree census, source authority, controls, PASS/FAIL/BLOCKED criteria, or interpretation ceiling may change.

Historical K4 parity runs `34993972013`, `34994071337`, and `34994172757` remain `INVALID_IMPLEMENTATION`.
