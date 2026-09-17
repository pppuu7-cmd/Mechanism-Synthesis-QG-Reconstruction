# Prospective implementation-only diagnostic — K5 34-orbit resolver repair-1 S5 label frame

Date: 2026-09-18 (Europe/Helsinki)

## Scope

This is an implementation diagnosis only. It does not reopen or modify the parent scientific contract, and it may not produce scientific N/B order authority.

Frozen parent scientific preregistration:

`d6b0e805101c8590eafac71398cc2b1466691752`

Frozen repair-1 preregistration:

`2193692c90d8ee1fa097200dbbac6ab70fd3a159`

Terminal invalid repair-1 production:

run `35271187040`, head `42daba28fd0c2545be386f63e89f6bcafdbed9a3`, aggregate artifact `10519073488`, classification `INVALID_IMPLEMENTATION`.

Durable invalid authority:

`results/raw/k5_34_orbit_exact_leading_coefficient_resolution_repair1_invalid_authoritative.json`.

## Observed implementation-only failure surface

The frozen aggregate has exactly one mandatory failed aggregate control:

`S5_full_coefficient_covariance_all = false`.

All 32 proper orbit rows fail all eight full-coefficient S5 equality booleans, while route-internal checks, full support, independent interpolation classes, projective-normal authority, W1/W2 state/order agreement and mask511 parent reproduction all pass.

No N/B coefficient or order value from the invalid production may be consumed by this diagnostic.

## Hypothesis

Repair-1 uses the independent Boundary-S5 theorem helper

`transported_pattern_dicts(base, p, ...)`

whose key map is explicitly `transport_target_key_to_old`: it expresses the transported source object in the **pulled-back old edge-label frame** used by the symbolic theorem comparison.

The resolver then supplies that object directly to `route_a(pmask(mask,p), perm_weights(weights,p), ...)`, whose incidence/covariance geometry is in the **permuted target edge-label frame**.

Hypothesis H_FRAME:

**the repaired source matching object is correct as a pullback theorem object but is passed into the wrong edge-label frame for the direct permuted route.**

This is an implementation-frame hypothesis, not a physics hypothesis.

## Frozen exact constructions

Use only exact rational arithmetic and the already locked source/theorem modules.

Permutation is the frozen resolver `CYCLE=(1,2,3,4,0)`.

Construct three source pattern objects without reading any scientific coefficient result:

1. `CURRENT_PULLBACK`: the exact repair-1 object using `transported_pattern_dicts(base,CYCLE,transpose_reversed=True,source_reversal_sign=True,covariance_orientation_sign=False)`.
2. `EXPLICIT_TARGET`: independently push each old source edge slot `i` to target slot `ep(CYCLE,i)`; transpose the source matrix type iff that old canonical edge reverses orientation; multiply by the source-reversal orientation character only. Do not include the covariance orientation character because the target-frame route supplies covariance geometry itself.
3. `INVERSE_HELPER_TARGET`: build using the theorem helper with `invperm(CYCLE)` and the same source-only sign convention, then compare exactly to `EXPLICIT_TARGET`.

Project each full 32-component dictionary through the same frozen invariant-dual weights and exact compatible-Wick collapse to a 945-matching coefficient object.

Also construct `PUSHED_BASE_MATCHINGS` by relabelling every matching edge index `i -> ep(CYCLE,i)` in the frozen base matching object, preserving exact channel coefficients. Because the frozen CYCLE has source orientation character +1, this is the direct target-frame matching-label expectation.

## Primary exact diagnostic obligations

D1. canonical ten-edge permutation is a bijection and inverse round-trips exactly.

D2. `CURRENT_PULLBACK` and `EXPLICIT_TARGET` are each 32-component, 100000-source-term, exact-rational constructions.

D3. `EXPLICIT_TARGET == INVERSE_HELPER_TARGET` at the complete full-32 source-pattern dictionary level.

D4. The projected `EXPLICIT_TARGET` matching object has exactly the frozen 945 matching support and equals `PUSHED_BASE_MATCHINGS` exactly.

D5. The projected `CURRENT_PULLBACK` object is not silently relabelled as `EXPLICIT_TARGET`; exact frame distinction must be visible either at source-dictionary or matching-key level.

D6. Control-only direct-route check on frozen diagnostic instance `mask=1`, `W1`: original `route_a(mask,W1,base MATCH_COEFF)` must equal target-frame `route_a(pmask(mask,CYCLE),WP1,EXPLICIT_TARGET_MATCH_COEFF)` for complete N and B coefficient polynomials in both physical channels. Do not record or interpret coefficient values/orders; record only exact equality booleans/hashes.

D7. The current repair-1 pullback object must remain distinguishable on the same diagnostic instance; if it unexpectedly gives the same direct target-frame route, H_FRAME is not established and no repair is authorized from this diagnostic.

D8. Source-fixed matching coefficients under the nontrivial target geometry remain a rejected malformed control.

D9. Alter one exact matching coefficient prospectively and require the direct-route equality control to fail.

## Classification

### `K5_34_ORBIT_RESOLVER_S5_LABEL_FRAME_MISMATCH_CONFIRMED_EXACT_CONTROL`

Only if D1-D9 all pass and the explicit target construction restores the diagnostic route equality while current pullback/source-fixed/altered controls are rejected.

### `K5_34_ORBIT_RESOLVER_S5_LABEL_FRAME_HYPOTHESIS_NOT_CONFIRMED_EXACT_CONTROL`

If exact tests show the current/predicted frame explanation is false while implementation itself is valid.

### `INVALID_IMPLEMENTATION`

If the diagnostic cannot construct the frozen objects exactly, source/matching support changes, exact rationality is lost, or a mandatory malformed control does not discriminate.

## Repair authorization

Only the first classification authorizes a prospective repair-2 whose sole substantive code change is to supply the independently confirmed source transport in the target edge-label frame expected by the permuted resolver route. Such repair must leave every scientific input, orbit/channel set, W1/W2, matchings, DAG, degree ceiling, U authority, classifier meaning and claim ceiling unchanged.

No resolver rerun is authorized before this diagnostic is terminal.

## Interpretation ceiling

This diagnostic can only identify an implementation label-frame defect. It cannot establish any N/B order, exact zero, local corner behavior, global Stokes/IBP, period, finite-part selector, reduction of `dim_C F_8=377`, regulator independence, predictive amplitude, new physics or quantum gravity.
