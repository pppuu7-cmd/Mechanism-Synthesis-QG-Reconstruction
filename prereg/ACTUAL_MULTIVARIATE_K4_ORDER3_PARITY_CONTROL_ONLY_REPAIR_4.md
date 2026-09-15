# Actual K4 order-3 parity gate — control-only repair 4

Date: 2026-09-15
Status: prospectively frozen after run `34994282499` returned `INVALID_IMPLEMENTATION`, before repair/retry.

## Trigger

Run `34994282499` mechanically returned **all P0-P8 true**, `degree_partition_count=364`, `edge_census_failures=0`, and the full 5 x 32 contraction census. Nevertheless `execution_valid=false` solely because the implementation used

`all(pos['candidate_validator'].values())`

on the dictionary

`{'valid': True, 'reasons': []}`.

The empty reasons list is correctly empty but is falsy in Python, so a successful validator was incorrectly converted into failure. This is a pure implementation/control bug. No scientific result from run `34994282499` is promoted.

## Frozen repair

Change only execution-validity evaluation from the erroneous all-values expression to the explicit predicate

`pos['candidate_validator']['valid'] is True`

while retaining the already-frozen positive controls and requirement that all malformed controls are rejected.

No scientific hypothesis, source object, source authority, parity argument, degree enumeration, boundary census, normal geometry, PASS/FAIL/BLOCKED criteria, or interpretation ceiling may change.

Historical runs `34993972013`, `34994071337`, `34994172757`, and `34994282499` remain permanently `INVALID_IMPLEMENTATION`.
