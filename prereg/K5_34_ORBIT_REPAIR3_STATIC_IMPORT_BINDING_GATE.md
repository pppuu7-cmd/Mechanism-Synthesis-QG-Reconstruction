# K5 34-orbit repair3 static/import binding gate — prospective preregistration

Status: PROSPECTIVE IMPLEMENTATION-ONLY GATE. Frozen before implementation or production.

## Purpose
Before the single authorized repair3 heavy production, verify that the production resolver is actually bound to the repaired matching-key frame and that no stale direct-pullback lookup remains on the scientific path.

## Frozen scope
This gate is implementation/provenance only. It MUST NOT evaluate or expose any N/B coefficient, leading order, q18 value, local flux/action verdict, Stokes/IBP statement, period, selector, F9/G3/G8 promotion, NEW_PHYSICS_FOUND, or complete-QG claim.

The only authorized repair remains the already frozen repair3: target matching coefficients are reindexed by the forward matching map P into the target-label frame; coefficient values themselves are unchanged.

## Mandatory checks
1. Locate the exact heavy 34-orbit resolver implementation and its workflow/import entry point used for the next production.
2. Import/compile the resolver module without executing the heavy scientific computation.
3. Statically identify the matching-coefficient target lookup on the scientific S5-comparison path.
4. Require that the target lookup is keyed in the target-label frame via the forward map P (or an exactly equivalent helper whose implementation is inspected by this gate).
5. Reject any stale scientific-path lookup that indexes the pullback/old-label matching table directly as if already in target labels.
6. Require the canonical matching universe cardinality 945 and an exact bijective forward-map roundtrip over all 945 keys using the same helper imported by production.
7. Require exact preservation of the multiset of matching-coefficient values under reindexing.
8. Require unchanged frozen production constants: 32 orbit representatives, 64 channel-orbit rows, two invariant-dual channels, W1/W2, N degree ceiling 27, B degree ceiling 31, U authority 5, exact rational arithmetic, and the existing parent classifier meanings.
9. Require no import/reference to quarantined q18 partial outputs on the production path.
10. Negative controls: (a) deliberately substitute direct pullback lookup for one target key and require detection; (b) deliberately transpose/invert the matching map convention and require roundtrip or lookup failure.

## Frozen classifier
Only the following terminal classifications are allowed:

- `PASS_REPAIR3_STATIC_IMPORT_BINDING` — every mandatory check and both negative controls pass; this authorizes exactly one unchanged-parent heavy repair3 production run.
- `BLOCKED_REPAIR3_BINDING_NOT_PROVEN` — import/static binding cannot be established without changing scientific code or an expected binding is absent/ambiguous.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` — malformed gate, missing frozen authority, incomplete 945-key coverage, failed validity control, or provenance mismatch.

No scientific PASS/FAIL is permitted from this gate.

## Dependency
Requires terminal `PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT` authority from run 35414831103. Heavy repair3 production is forbidden until this gate is terminal PASS.
