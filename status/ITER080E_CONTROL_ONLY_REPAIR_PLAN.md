# Iter080E-SM control-only repair plan

**Date:** 2026-09-14

## Trigger

Initial production run `34831623440` at head `542d81dc53d4b9afae5bab3d08ad0d01da0727c2` terminated `failure` before aggregate authority because Lane D returned `INVALID_PROVENANCE`.

The failure is implementation-only. Lane D used two brittle natural-language substring tests against `status/CURRENT.md`:

- it searched for `finite K5 permutation covariance does not uniquely select`, while CURRENT states `finite K5 permutation covariance does not select a unique extension`;
- it searched for `fixed finite scalar-valued complex-linear selector`, while CURRENT records the repaired Iter080D result with different wording and the exact durable classification identifier.

The same Lane D run verified the Iter077Q derivation blob exactly and passed the Iter077K and active-front locks. Lanes A/B/C are not scientific authority because the required aggregate never ran.

## Frozen contract remains unchanged

Prospective scientific preregistration remains exactly commit `f1a465a059f7c4da8270bed8021f920013b7f5da` and is not edited.

No HYPOTHESIS, OBJECT, DEPENDENCY, SOURCE AUTHORITY, FROZEN INPUTS, PASS, FAIL, BLOCKED, INVALID, or INTERPRETATION CEILING criterion changes.

No source-matrix status, source evidence, selector predicate, positive control, negative control, or scientific classification rule changes.

## Authorized control-only repair

Replace only the two brittle CURRENT prose matches in Lane D with exact durable classification identifiers already present in CURRENT:

- `ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`;
- `ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`.

Then allow the unchanged workflow to run prospectively on the repaired implementation. The initial failed run remains permanently non-authoritative provenance and must not be overwritten.

## Ceiling

This repair has zero scientific content by itself. Scientific classification is permitted only after a new complete terminal run with all frozen lanes and aggregate valid.