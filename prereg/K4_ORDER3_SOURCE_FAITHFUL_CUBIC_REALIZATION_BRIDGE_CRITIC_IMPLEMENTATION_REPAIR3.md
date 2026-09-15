# K4 cubic-realization bridge independent Critic — implementation repair 3

Date: 2026-09-15
Role: control-only implementation repair; no scientific-contract change

## Trigger

Run `34993403191` passed C1, C2, C4-C10 and exact R1-R10 checks, but C3 remained false because the repaired code incorrectly conjoined the five repair-2 C3 facts with a broad `source_retention_ok` text bundle containing unrelated evidence. This violates the prospectively frozen repair-2 definition of C3.

Run `34993403191` is therefore `INVALID_IMPLEMENTATION`, not scientific authority.

## Frozen repair

Set C3 **exactly** to the conjunction prospectively frozen in repair 2 and nothing else:

1. R9 is `RETAINED_AUTHORITY`;
2. `beta_shift_i_epsilon.rejected == true`;
3. its forbidden list includes `beta_shift_epsilon`;
4. its missing list includes `source_spectral_i_epsilon`;
5. normalized Researcher result text states retention of source branch normalization and published one-wedge spectral i epsilon.

Do not alter C1, C2, C4-C10, expected durable hashes, negative-control inventory, terminal taxonomy, or interpretation ceiling.
