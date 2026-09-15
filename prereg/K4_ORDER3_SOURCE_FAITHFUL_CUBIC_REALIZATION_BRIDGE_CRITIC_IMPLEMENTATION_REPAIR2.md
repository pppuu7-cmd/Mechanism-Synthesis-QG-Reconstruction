# K4 cubic-realization bridge independent Critic — implementation repair 2

Date: 2026-09-15
Role: control-only / implementation repair; parent Critic scientific contract unchanged

## Trigger

Fresh repair-1 run `34993299842` was execution-valid and passed C1, C2, C4-C10 plus exact R1-R10 state checks, but failed C3 only because the Critic searched the Researcher result for the literal substring `beta+i epsilon`.

That literal occurs in the Researcher result solely as a malformed construction explicitly rejected by the frozen negative controls. The durable Researcher raw separately records `beta_shift_i_epsilon.rejected=true`, requires `source_spectral_i_epsilon`, and retains `R9_BRANCH_NORMALIZATION=RETAINED_AUTHORITY`. Therefore substring presence is not evidence that the bridge replaced the published spectral `i epsilon`.

Historical runs `34985145895` and `34993299842` are `INVALID_IMPLEMENTATION`; neither has scientific-fail authority.

## Frozen repair

Change only C3 implementation. C3 must pass iff all of the following durable facts hold:

1. `R9_BRANCH_NORMALIZATION == RETAINED_AUTHORITY`;
2. malformed control `beta_shift_i_epsilon` exists and is rejected by the Researcher validator;
3. that malformed control records `beta_shift_epsilon` as forbidden and `source_spectral_i_epsilon` as missing;
4. the durable Researcher result explicitly states retention of `source branch normalization and published one-wedge spectral i epsilon` (Markdown formatting differences may be normalized);
5. no repaired Critic code treats mention of a forbidden surrogate in a negative-control description as use of that surrogate by the positive bridge.

No other check, source, expected digest, scientific classification, or interpretation ceiling may change.
