# K5 mask-511 structural divisibility — conditional timeout-only repair 2

Status: PROSPECTIVELY FROZEN, DORMANT UNLESS REPAIR-1 RUN TERMINATES BY EXECUTION TIMEOUT/CANCELLATION BEFORE COMPLETE SHARD AUTHORITY.
Date: 2026-09-17

## Parent authority

Scientific contract remains `prereg/K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS.md` at commit `bb2fc2636de21d8eed06e3694a128be34e5fede1`.
Repair-1 execution contract remains `prereg/K5_MASK511_STRUCTURAL_DIVISIBILITY_CONTROL_REPAIR_1.md`.
Current repaired production is run `35246991631`, head `ef5f365798ab6aa2b9cb53d6b091868d910c9b71`.

No partial substantive value from that non-terminal run is consumed by this fallback freeze.

## Activation condition

This repair is authorized **only if** run `35246991631` becomes terminal without a valid complete eight-shard aggregate because one or more exact shard jobs are cancelled/terminated by the existing 60-minute execution limit. If repair-1 reaches a valid terminal aggregate, this repair remains unused and must not be launched.

## Frozen execution-only change

If activated, preserve exactly the repair-1 scientific code, eight deterministic `global_matching_index mod 8` partitions, all source/input/blob locks, exact rational arithmetic, malformed control, aggregate coverage requirements, W1/W2 reproduction checks, scientific classifications and interpretation ceiling.

Change only the shard-job GitHub Actions execution budget from `timeout-minutes: 60` to `timeout-minutes: 180`. Keep the aggregate job and its scientific logic unchanged. Do not change shard count, matching assignment, polynomial truncation window, hypothesis, object, PASS/FAIL/BLOCKED/INVALID criteria, or any scientific threshold.

The activated retry must be a fresh workflow run from a commit changing only that workflow timeout (plus any provenance note needed to record the terminal timeout). Historical repair-1 remains preserved as infrastructure evidence and is never reclassified scientifically.

## Interpretation ceiling

Unchanged from the parent and repair-1 preregistrations. A completed repaired result can establish only the frozen labeled mask-511 exact lower-coefficient/structural-divisibility classification. No promotion to other masks, full K5 finiteness, global Stokes/IBP, period evaluation, finite-part selection, regulator independence, downstream QG closure, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
