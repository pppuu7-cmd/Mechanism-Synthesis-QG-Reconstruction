# Iter082H-SM first green production — quarantine

Date: 2026-09-15

Run `34907033113` (production head `41d7ba64906dc4a5e03d25b618659e95a4fb9f63`) completed successfully and produced artifact `10372739062`, digest `sha256:d854e0e395d209a17bb61d18d5c8897e840e1f5bc2b33895f07645b19db83074`.

The artifact was downloaded and inspected before scientific classification.

## Implementation defect

The frozen P6 negative-control requirement says all negative controls must be rejected **by the same validators** used by the positive gate. In the first implementation, two controls were wired as unconditional booleans:

- `singular_transition`: `rejected: true` was written directly rather than evaluated by the transition-invertibility validator;
- `order_lowering`: `rejected: true` was written directly rather than evaluated by the filtration/order-lowering validator.

Therefore P6 could not falsify the implementation for these two malformed inputs. The green workflow status is not sufficient for an authoritative scientific classification.

## Quarantine classification

`INVALID_IMPLEMENTATION_NEGATIVE_CONTROL_WIRING`

This is an implementation/control failure, **not** a scientific FAIL or BLOCKED result. No frozen scientific predicate or threshold is changed.

The numerical/scientific-looking payload from this run must not be promoted until an independently preregistered control-only repair makes both malformed inputs pass through the same validators and a new terminal production artifact is consumed.

Claim locks remain unchanged.
