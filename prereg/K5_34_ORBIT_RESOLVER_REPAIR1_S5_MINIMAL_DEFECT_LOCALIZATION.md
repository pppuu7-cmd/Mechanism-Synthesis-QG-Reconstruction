# K5 34-orbit resolver repair-1: minimal S5 defect localization

Status: PROSPECTIVE IMPLEMENTATION-ONLY DIAGNOSTIC. Frozen before implementation.

## Trigger

Repair-1 run 35271187040 is INVALID_IMPLEMENTATION solely because `S5_full_coefficient_covariance_all=false`. The prospective label-frame diagnostic run 35280836616 terminated `PASS_EXACT_CONTROL_DIAGNOSTIC_NEGATIVE` with classification `K5_34_ORBIT_RESOLVER_S5_LABEL_FRAME_HYPOTHESIS_NOT_CONFIRMED_EXACT_CONTROL`: D1,D2,D3,D5,D7,D8,D9 pass; D4 and D6 fail. Therefore repair-2 is NOT authorized from the label-frame hypothesis and the smallest remaining exact S5 comparison defect must be localized before any resolver rerun.

## Frozen question

For the single frozen diagnostic representative mask=1, ray=W1, cycle permutation (0 1 2 3 4), locate the earliest exact object at which the independently confirmed Boundary-S5 transport and the repair-1 resolver route cease to agree.

## Frozen stages

Compare exact rational objects, in this order, and stop classification at the first mismatch while still recording all stage booleans/hashes:

1. canonical edge permutation and inverse roundtrip;
2. 945 retained matching support as canonical labeled edge-pair tuples, not only aggregate matching hashes;
3. per-matching transported source coefficient dictionaries before Wick contraction;
4. per-matching Wick contribution dictionaries before summation;
5. summed physical numerator coefficient vectors N for both invariant-dual channels;
6. annihilator/flux vectors B derived from the same N route.

For stages 2-4 record a deterministic first mismatching key plus hashes/counts only; do not emit or inspect scientific leading orders. Exact `Fraction` arithmetic only.

## Mandatory controls

- Reconstruct the independent Boundary-S5 authority convention from source endpoint/orientation transport plus boundary contragredient action; do not fit a phase, character, 2x2 matrix, permutation, or relabeling after seeing output.
- Verify all 32 boundary components and 100000 source terms are present in the constructed source object before restricting to the frozen mask/ray diagnostic.
- Verify 945 retained matchings on both routes.
- Source-fixed negative control must be rejected.
- Deliberately altered one-matching transport must be rejected.
- No q18/q19/q21 values or historical resolver coefficient/order outputs may be used to choose conventions.

## Frozen classifications

- `K5_34_ORBIT_S5_DEFECT_LOCALIZED_MATCHING_SUPPORT`
- `K5_34_ORBIT_S5_DEFECT_LOCALIZED_SOURCE_COEFFICIENT_TRANSPORT`
- `K5_34_ORBIT_S5_DEFECT_LOCALIZED_WICK_CONTRIBUTION`
- `K5_34_ORBIT_S5_DEFECT_LOCALIZED_NUMERATOR_ASSEMBLY`
- `K5_34_ORBIT_S5_DEFECT_LOCALIZED_ANNIHILATOR_FLUX`
- `K5_34_ORBIT_S5_NO_DEFECT_ON_FROZEN_LANE`
- `INVALID_IMPLEMENTATION_OR_PROVENANCE`

No classification is a scientific N/B coefficient verdict. No repair-2 or heavy 34-orbit rerun is authorized until this diagnostic is terminal and its defect class is consumed.

## Interpretation ceiling

Implementation diagnosis only. `0/64` resolver components remain authoritative until a future valid run satisfies the unchanged parent preregistration. No Stokes/IBP, K5-period, finite-part selector, F9/G3/G8, regulator-independence, NEW_PHYSICS_FOUND, or complete-QG promotion follows from this diagnostic.
