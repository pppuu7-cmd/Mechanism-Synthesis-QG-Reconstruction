# Iter083A control-only repair 1

Status: **PROSPECTIVELY FROZEN BEFORE TERMINAL OUTPUT INSPECTION / BEFORE REPAIR IMPLEMENTATION**
Date: 2026-09-15

Parent scientific preregistration: `prereg/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_VALIDATION.md`, commit `38abc8bfbc78fe07e56a4f29a09733925e96d9b2`.
Current production head under execution: `fb98eb35ffd0a51cdefde53e3f03c57f3145bbb2`, run `34908559463`.

## Reason for prospective repair freeze

A pre-terminal code audit found two outcome-classification defects in `scripts/iter083a_boundary_covariant_jet_character_validation.py`. No production substantive values were inspected.

### R1 — P6 is a reporting predicate, not a positive-outcome requirement

The parent preregistration freezes P6 as:

> The calculation explicitly reports whether representation-valued boundary covariance opens normal orders absent in the scalar invariant sector; no parity conclusion may be assumed in advance.

The current implementation instead sets

`p6 = len(odd_open) > 0`.

That makes one substantive outcome mandatory. If the exact calculation validly finds `odd_open=[]`, the implementation would reject the result even though the frozen P6 requirement is satisfied by explicitly reporting that no additional order opens. This is outcome bias and is an implementation defect.

Control-only repair: P6 must validate that the comparison is actually computed and reported for every degree `0..8`, while the list of opened orders is allowed to be empty or nonempty. No expected parity pattern or exploratory value may be encoded in the predicate.

### R2 — valid scientific mismatches must be scientific FAIL, not implementation INVALID

The parent preregistration explicitly freezes three distinct terminal classes:

- all P0-P7 pass -> `PASS_EXACT_SCOPED`;
- canonical boundary action not source-definable -> `BLOCKED_OBJECT_DEFINITION`;
- valid first-principles reconstruction disagrees with the exploratory values or fails an exact representation-theory predicate -> `FAIL_EXACT_SCOPED`;
- implementation defects -> `INVALID_IMPLEMENTATION`.

The current script maps every non-PASS predicate state to `INVALID_IMPLEMENTATION`. This erases the frozen scientific FAIL/implementation distinction.

Control-only repair: the implementation must separate execution/provenance/control validity from scientific predicates. After execution validity is established, exact P1-P6 scientific mismatches must map to the frozen `FAIL_EXACT_SCOPED` classification, not to `INVALID_IMPLEMENTATION`. `INVALID_IMPLEMENTATION` remains reserved for broken controls, missing inputs, malformed computations, or provenance defects. `BLOCKED_OBJECT_DEFINITION` remains reserved for a demonstrated source-definition failure of the canonical boundary action.

## Scientific contract lock

No scientific object, source authority, boundary Hilbert space, normal representation, degree bound, character formula, exploratory replication target, positive/negative control, PASS label, FAIL label, BLOCKED label, or interpretation ceiling from the parent preregistration may change.

In particular, this repair does **not** alter P4 or any substantive expected character/multiplicity value. It only restores outcome-neutral execution of already-frozen P6 and the already-frozen verdict taxonomy.

## Production discipline

Do not cancel or duplicate the already queued/running parent production merely because of this audit. Its output, once terminal, may be used only to diagnose implementation/control behavior under the parent code. A repaired production may be launched only after the parent run is terminal, and only under this prospectively frozen control-only repair with the scientific contract unchanged.
