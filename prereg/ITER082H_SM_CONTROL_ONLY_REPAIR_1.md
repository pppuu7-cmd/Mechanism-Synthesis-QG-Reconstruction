# Iter082H-SM control-only repair 1 preregistration

Date: 2026-09-15

The first green production run `34907033113` is quarantined as `INVALID_IMPLEMENTATION_NEGATIVE_CONTROL_WIRING` because two frozen P6 malformed controls were assigned `rejected=true` directly instead of being evaluated by the same validators as the positive gate.

This repair is strictly control-only. **No scientific predicate, representation, atlas map, invariant dimension criterion, Čech criterion, threshold, classification label, or claim ceiling is changed.**

Frozen repair:

1. Factor the transition-invertibility condition into a validator that inspects the linear coefficient / formal transition object used by the positive gate. Feed the synthetic singular transition (zero linear coefficient) through that validator and require rejection.
2. Factor the normal-order filtration condition into a validator `output_degree >= input_degree`. Feed the synthetic `8 -> 6` malformed transition through that validator and require rejection.
3. Preserve every other Iter082H frozen criterion exactly.
4. Re-run production from a new commit and consume the new terminal artifact before any scientific classification.

Allowed outcomes after repair:

- if all original P0–P6 predicates pass with mechanically wired controls: the original preregistered PASS label may be used;
- if a scientific predicate fails with valid controls: the original preregistered FAIL label applies;
- if another control/implementation defect is found: quarantine again as `INVALID_IMPLEMENTATION` before any further repair.
