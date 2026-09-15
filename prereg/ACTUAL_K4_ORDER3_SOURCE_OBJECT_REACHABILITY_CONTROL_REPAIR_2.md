# K4 order-3 source-object reachability — control-only repair 2

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / REPAIRED OUTPUT**

Parent scientific preregistration: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY.md`, commit `a6983a4d7379bf73f48752a4de357450996d8572`.
Control repair 1: `prereg/ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_CONTROL_REPAIR_1.md`, commit `24378e82fff8db81893f01248b1cac2c2d3ec660`.
Historical runs `34963831115` and `34963919913` remain `INVALID_IMPLEMENTATION` and have no scientific authority.

## Remaining implementation defect

Whitespace/case normalization fixed the prose anchor but the bridge source writes the exact ray formula as a two-line displayed equation:

`q_B = r^2 (...) + O(r^3)`

followed by the continuation

`= r^2 R_B^2 + O(r^3)`.

The frozen evidence anchor expresses the mathematically identical contracted statement `q_B = r^2 R_B^2 + O(r^3)`. Literal normalized substring matching cannot recognize a displayed-equation continuation and therefore still returns a provenance-control failure.

## Frozen repair

Change only the evidence verifier so a requested equality `lhs = rhs` may also be satisfied when:

1. the normalized source contains the same `lhs =` earlier in the same local displayed-equation paragraph; and
2. it contains a subsequent normalized continuation `= rhs`.

No requirement status, scientific evidence path/commit, hypothesis, object, frozen input, control, verdict taxonomy, interpretation ceiling, or K4 scientific value may change. The existing audit manifest remains byte-for-byte unchanged. A repaired run is authoritative only if evidence verification, complete synthetic positive control and all 12 malformed controls pass.