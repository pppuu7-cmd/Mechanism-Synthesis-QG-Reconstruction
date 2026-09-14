# Iter080J-SM control-only repair preregistration — Iter029 Hörmander/Hormander lexical match

Date: 2026-09-14

## Historical run preserved

Historical production run `34859269730` is execution-invalid for aggregate scientific classification because Lane B failed before artifact upload while lanes A/C/D passed. This is **not** classified as a scientific failure.

## Exact implementation defect

The frozen scientific criterion in Lane B is: the pre-existing repository Iter029 must establish an independently motivated microlocal/wavefront audit using the standard Hörmander wavefront/transversality criterion.

The implementation tested the literal Unicode token `Hörmander`, but the authoritative Iter029 result file writes the same surname as ASCII `Hormander` in the phrase `standard transverse/Hormander product criterion`.

Therefore the failed predicate was a lexical spelling mismatch, not absence of the frozen scientific evidence.

## Frozen repair

Only Lane B's textual control is changed:

- accept the exact authoritative ASCII spelling `Hormander` (and optionally Unicode `Hörmander`) when verifying the already-frozen Iter029 motivation;
- keep the exact same file, exact same independent-motivation requirement, and exact same frozen Brunetti--Fredenhagen / Dang source locks;
- no scientific criterion, M_WF definition, theorem implication, classification, or interpretation ceiling may change.

All other lanes remain byte-for-byte logically unchanged except workflow rerun provenance.

## Frozen classification handling

- Historical run `34859269730`: `INVALID_IMPLEMENTATION_LEXICAL_CONTROL`, no scientific PASS/FAIL.
- Repaired production run may receive the original preregistered classification only if A/B/C/D and aggregate all satisfy the original frozen gate.
- Scientific FAIL/BLOCKED remains distinct from infrastructure/control failure.
