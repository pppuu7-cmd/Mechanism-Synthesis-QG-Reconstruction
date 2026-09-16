# K5 exact cancellation resolver — S5 source/channel transport diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE DIAGNOSTIC OUTPUT**.

Parent scientific gate: `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`, preregistration `d6b0e805101c8590eafac71398cc2b1466691752`.
Implementation freeze: `808492fe93369f27e7fcaee6a0f7af64583a35ae`.
Execution amendment: `cf944a8c246a0c5b9819967549c155a6ca5d1aaa`.
Current production head: `051659255b1b1e7a5315f2b8dc2ec485615a0cfd`.

## Triggering defect

Completed orbit payloads from the current production show a sharply localized pattern: exact primary interpolation agrees coefficient-by-coefficient with the independent denominator-cleared reconstruction, all frozen degree checks and negative controls pass, and the projective-normal `U_Z` S5 covariance passes, while the physical numerator/action `N_c,B_v[N_c]` S5 full-coefficient comparison fails. The current resolver compares each physical channel to the same channel after only edge-mask/asymmetric-weight transport.

This diagnostic is execution/control-only. It does **not** change any physical object, coefficient support, orbit representative, asymmetric witness, degree ceiling, exact-zero rule, scientific classifier, or interpretation ceiling.

## Frozen objective

Determine the exact S5 transport law of the two physical invariant-dual coordinate functionals directly from the already-authoritative 32-state source representation, not from physical corner production coefficients.

For the frozen vertex cycle

`CYCLE=(1,2,3,4,0)`,

construct exactly:

1. the two local source tensor vectors from `NODE_OPTIONS`;
2. all local leg-permutation action matrices;
3. the exact 32x32 global action matrix `A_cycle` using the established `global_action_matrix` construction;
4. the exact Reynolds projector `P=(1/120) sum_sigma A_sigma`;
5. the frozen rank-two pivots `[1,4]`;
6. the two coordinate functionals actually used by the physical contraction, `W[:,c]=P[:,pivot_c]`.

Then test both representation conventions mechanically, without fitting to `N/B` data:

- vector convention: `A_cycle W = W T_vec`;
- covector convention: `A_cycle^T W = W T_cov`;
- inverse-covector convention: `A_cycle^{-T} W = W T_invcov`.

For each convention solve for a constant rational 2x2 matrix only if exact column-space membership holds, and verify the solution on all 32 rows. Also test exact identity transport for each convention.

## Frozen classifier

`S5_SOURCE_TRANSPORT_IDENTITY_CONFIRMED` only if the representation-derived transport of the physical coordinate functionals is exactly identity under the convention appropriate to the source boundary object and all 32-row checks pass.

`S5_SOURCE_TRANSPORT_NONTRIVIAL_2X2_EXACT` if an exact non-identity rational 2x2 action is mechanically derived from the source representation and all 32-row checks pass.

`S5_SOURCE_TRANSPORT_CURRENT_LANE_INVALID` if the current same-channel comparison is not the representation-derived law.

`INVALID_IMPLEMENTATION` if Reynolds rank/pivots, group-action construction, invertibility, exact solves, or representation checks fail.

No physical `N/B/U` coefficient from run `35153228914` may be used to fit or choose a transport law. Production coefficients may be revisited only after this source-only diagnostic is terminal.

## Repair rule

If and only if the source-only diagnostic proves that the current S5 lane omits or misstates the exact source/channel transport, a subsequent prospective control repair may replace only the S5 comparison operator. It must retain full coefficient-by-coefficient covariance, all frozen degree supports, nodes, witnesses, 32 proper orbits, two channels, independent reconstruction route, and terminal scientific classifier.

No global Stokes/IBP or period claim is authorized by this diagnostic.