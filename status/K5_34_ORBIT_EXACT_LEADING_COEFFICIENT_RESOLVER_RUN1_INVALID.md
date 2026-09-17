# K5 34-orbit exact leading-coefficient resolver — run 1 invalid

Date: 2026-09-17

## Frozen scientific contract

Parent preregistration remains `prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`.

The scientific object, 32 proper S5 orbit representatives, two invariant-dual physical channels, frozen W1/W2 angular weights, degree ceilings `N<=27`, `B<=31`, 945 exact retained matchings, canonical all-32/100000-term source contraction, source ordering and published spectral `i epsilon` remain unchanged.

## Terminal production

Workflow `K5 34-orbit exact leading coefficient resolution`, run `35268238924`, head `25f646baa8b427d7f52ec3d1a5fadc31cd80fca1`.

All eight deterministic shard jobs completed successfully. Aggregate job `105366477161` also completed at the CI level and uploaded aggregate artifact `10517943520`, ZIP digest `sha256:dbae89ae18674cfe8d518e507e330b6b92b25c22325fe3b8a077955a6856863e`.

The aggregate classifier itself returned

`status = INVALID_IMPLEMENTATION`

`classification = INVALID_IMPLEMENTATION`.

Therefore **no N/B coefficient, first-nonzero order, zero/nonzero state or provisional 64-component classification from this run is scientific authority**.

## Exact implementation defects

Two frozen controls failed:

- `route_internal_exact_controls_all = false`;
- `S5_full_coefficient_covariance_all = false`.

The first is a pure control implementation defect: polynomial wrapper `P` has no structural `__eq__`, while route controls compare `P` objects directly in `psi.v == tree`, `Ds[0].v == psi.v` and `Ds[0].d == psi.d`. These comparisons test Python object identity rather than exact coefficient dictionaries.

The second is an object-transport defect, not a scientific covariance failure. The shard computes the S5 comparison by permuting only mask/weights and re-evaluating the fixed source coefficient object. The independently confirmed full-source boundary transport authority instead requires simultaneous endpoint/orientation transport of source data plus boundary contragredient transport. The parent prereg explicitly requires transport of the actual full coefficient object before comparison. A source-fixed mismatch is therefore `INVALID_IMPLEMENTATION`, not a physical obstruction.

## Firewall

No invalid-run substantive values may be used to tune masks, weights, channels, matchings, degree ceilings, source normalization, DAG construction, PASS/FAIL thresholds or a repair.

Any repair must be prospectively frozen before code changes and may alter only control/transport implementation. The parent scientific hypothesis and interpretation ceiling remain unchanged.
