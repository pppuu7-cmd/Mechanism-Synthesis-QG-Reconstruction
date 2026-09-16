# K5 Schwinger projective tangent normal-flux scaling — control repair 2 preregistration

Date: 2026-09-16
Status: PROSPECTIVELY FROZEN BEFORE REPAIR-2 IMPLEMENTATION / PRODUCTION OUTPUT
Parent scientific contract: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`
Control repair 1: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_1.md`, commit `68c14c6774d27388878c0f2fe6c3741eab828e87`.
Failed repair-1 production: run `35124809996`, job `104891115629`, head `4481ad4c33e6b82ca48dec4da93bda1e78b271f3`.

## Trigger and scope

Repair-1 failed before scientific classification at exact-form identity `i_v Omega_9 = i_u Omega_9`. Inspection shows the comparator used polynomial `expand()` on rational expressions containing `1/s1`, so algebraically equal rational forms were not canonically reduced. The same implementation also did not separately execute the frozen permutation-related-subset control or a nontrivial exceptional-leading-zero case whose extractor advances to the next nonzero `t` order.

This is a control-only implementation repair. It does **not** alter the parent hypothesis, projective tangent object, blow-up geometry, success/failure criteria, source ordering, or interpretation ceiling.

## Frozen repair-2 obligations

The executable must satisfy the full repair-1 contract and additionally:

1. Compare rational differential-form coefficients only after exact `together/cancel`-equivalent canonical reduction; polynomial `expand()` alone is forbidden as the equality oracle.
2. Build `Vol`, `Omega_9=i_E Vol`, generic polynomial logarithmic `v`, `u=v-(S/s1)E`, and compute `i_v Omega_9`, `i_u Omega_9`, `i_E Omega_9` as exact antisymmetric forms.
3. Make classification outcome-neutral. The success label may appear only if all mathematical identities and all implementation-coverage checks pass. A genuine exact disagreement in the frozen parent formula must emit a scientific-failure/counterexample classification, not crash into an implementation PASS. Missing coverage remains `INVALID_IMPLEMENTATION`.
4. For every `k=1,...,9`, execute explicit blow-up pullbacks for a proper subset `Z` in two genuinely distinct simplex/projective charts. The scalar valuation must be mechanically extracted from the pulled-back `Omega_9`; no hard-coded `k-1` assignment is allowed in the decision path.
5. Compare the two chart pullbacks by constructing the exact transition map and determinant. Require equality of the **full pulled-back scalar form and full pulled-back flux form** under the transition Jacobian; matching valuations alone is insufficient. Record transition determinant and leading coefficients.
6. Execute a separate K5/S5-induced permutation-related-subset control: use a fixed nontrivial vertex permutation, its induced permutation of the ten edges, push forward the generic field, and verify the mechanically extracted scalar/flux valuations for the permuted proper subset. This control is logically separate from chart equivalence.
7. Execute a nontrivial exceptional nonradial polynomial field, not the identically radial Euler field, for which the naive leading projective normal coefficient vanishes on a frozen proper face but the flux is not identically zero. Require the extractor to advance to a strictly higher finite `t` valuation and record that witness.
8. Retain exact radial controls `i_E Omega_9=0` and `v -> v+f(alpha)E` invariance at contracted-form level; retain `Z=empty` and `Z=E(K5)` only as nonphysical firewalls.
9. Emit machine-readable witnesses for every `k` and both charts: chart maps/coordinate identities, pulled scalar coefficient, pulled flux coefficient, valuations, leading coefficients, transition determinant, plus the permutation and exceptional witnesses.

## Frozen classification

- `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED` only if every frozen mathematical identity and every repair-2 implementation obligation passes exactly.
- `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_SCIENTIFIC_FAIL_EXACT_SCOPED` if the implementation coverage is complete but an exact parent mathematical identity/chart relation/scaling claim is false.
- `INVALID_IMPLEMENTATION` if any frozen implementation obligation, witness coverage, chart transition, permutation control, exceptional control, or machine-readable provenance is missing or cannot be executed.

## Interpretation ceiling

Even a terminal success closes only the corrected local projective blow-up/tangent-flux geometry sub-gate. It does not classify the 34 physical corner orbits, prove global Stokes/IBP, evaluate an invariant-dual K5 period, reduce the 377-dimensional supported-extension freedom, select a finite part, establish regulator independence, or authorize F9/G3/G8 / `NEW_PHYSICS_FOUND` / complete QG.
