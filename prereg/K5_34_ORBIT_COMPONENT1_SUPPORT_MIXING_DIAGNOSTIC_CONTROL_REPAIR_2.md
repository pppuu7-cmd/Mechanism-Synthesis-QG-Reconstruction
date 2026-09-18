# K5 component-1 support-mixing diagnostic — control repair 2

**Date:** 2026-09-18

Parent repair-1 prereg: `aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec`.
Parent repair-1 run: `35363408523`, head `ef82324d05e46f474cebd2a14ea089c801b24ab6`.

The terminal artifact classified `INVALID_IMPLEMENTATION_OR_PROVENANCE` for exactly one failed validity boolean:

`repair_prereg_locked = false`.

Every other frozen validity/mixing control was true. The cause is self-referential: repair-1 code required the repair preregistration file contents to contain the preregistration commit SHA, but that SHA does not exist until after the file has already been committed. This cannot be a valid content lock.

## Frozen repair

Change only the repair-prereg validity check.

The repaired implementation must lock:
- the hard-coded expected repair-1 commit SHA `aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec`;
- the exact repair-1 prereg file path;
- stable title/parent-authority text already present in that file.

Do not change target component construction, source transport, boundary matrices, contributor set, support/coefficient comparison, parent classifications, mask/ray/cycle/matching, or any source/physics input.

Do not consume the repair-1 support/coefficient mismatch as authority. A fresh terminal repair-2 production is required.

Interpretation ceiling remains implementation diagnosis only; heavy resolver stays 0/64 authoritative.
