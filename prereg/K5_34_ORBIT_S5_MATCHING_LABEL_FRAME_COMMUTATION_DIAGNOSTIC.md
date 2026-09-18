# K5 34-orbit S5 matching label-frame commutation diagnostic

**Date:** 2026-09-18
**Role:** AUTOMATION A — MSQGR Researcher / Constructor
**Type:** exact object-map / implementation theorem; no physical N/B coefficient consumption

## HYPOTHESIS

The systematic failure of `S5_full_coefficient_covariance_all` in resolver repair-1 is caused by a label-frame mismatch between:

1. the independently confirmed source-pattern transport map on the complete 32-component / 100000-term source object; and
2. the perfect-matching coefficient object consumed by a route evaluated in the permuted target edge frame.

More precisely, projection/collapse to the 945 retained perfect matchings must commute with S5 transport only after the matching keys are transported into the same edge-label frame as the covariance geometry.

## EXACT OBJECT

Let `D` be the exact complete source pattern dictionary vector, `T_p D` its independently confirmed simultaneous endpoint/orientation + boundary contragredient transport for the frozen cycle `p=C=(1,2,3,4,0)`, and `C_match` the exact invariant-dual projection plus compatible-Wick collapse to matching coefficients.

Construct and compare exactly:

`M_source = C_match(T_p D)`.

For the parent matching object `M=C_match(D)`, define exact matching-key transports for:
- forward target-frame edge relabeling `R_p M`;
- inverse relabeling `R_(p^-1) M`;
- identity/no relabeling.

No physical orbit polynomial, N coefficient, B coefficient, first-nonzero order or invalid-run coefficient payload may be used.

## DEPENDENCY

Independent Boundary-S5 Critic authority `CONFIRMED_EXACT_SCOPED`, run `35267432939`; terminal resolver repair-1 invalid ledger; canonical ten-edge source ordering.

## SOURCE AUTHORITY

- `scripts/k5_full_source_boundary_s5_transport_symbolic_theorem.py`;
- `scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py`;
- canonical all-32/100000-term source object;
- 945 exact retained matchings;
- exact invariant-dual projection;
- corrected Iter077 source ordering;
- published spectral `i epsilon` retained.

## FROZEN INPUTS

- generator `C=(1,2,3,4,0)`;
- exact edge permutation `ep(C,i)`;
- exact source-pattern transport with endpoint transpose and source reversal sign;
- covariance orientation sign excluded from the source coefficient object because it belongs to covariance-geometry pullback in the resolver route;
- exact rational/Gaussian-rational arithmetic;
- canonical matching normalization: unordered pair endpoints sorted internally and the five pairs sorted lexicographically.

## POSITIVE CONTROLS

1. Base `C_match(D)` reproduces parent `MATCH_COEFF` exactly.
2. `ep(C,·)` is a bijection of ten edge labels.
3. Forward then inverse matching-key transport returns the original matching object.
4. Both transported objects retain exact rational coefficients and 945 retained matchings.

## NEGATIVE CONTROLS

- identity/no matching relabel must be rejected if the frame-mismatch hypothesis is correct;
- inverse relabel must be rejected if forward target-frame relabel is correct;
- omitting source endpoint transpose or source reversal sign must remain rejected through the already-confirmed source transport controls.

## PASS

`PASS_EXACT_SCOPED` iff exactly one of {forward, inverse, identity} matches `M_source`, all controls pass, and the unique matching relation is compatible with the target covariance frame. Classification:

`K5_34_ORBIT_S5_MATCHING_LABEL_FRAME_COMMUTATION_IDENTIFIED_EXACT_SCOPED`.

## FAIL

`FAIL_EXACT_SCOPED` iff no allowed matching-key frame map makes the exact collapse commute, with all source locks and controls valid. This falsifies the simple label-frame-mismatch explanation and forces a deeper transport theorem before another resolver repair.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` iff more than one non-equivalent frame map survives or the canonical matching normalization cannot be defined from repository authority.

## INVALID

Any source/hash mismatch, non-bijective coverage, rationality defect, missing critic authority, or use of repair-1 physical N/B values is `INVALID_IMPLEMENTATION`.

## INTERPRETATION CEILING

This diagnostic cannot authorize any 34-orbit N/B coefficient/order, physical corner classification, local K5 finiteness/divergence statement, global Stokes/IBP relation, period, finite-part selector, reduction of `dim_C F_8=377`, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim. A PASS only identifies the exact object-map needed before a separately prospectively frozen control-only resolver repair.
