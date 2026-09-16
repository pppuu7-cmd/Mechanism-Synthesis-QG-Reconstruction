# Control-only repair 1 — independent Critic review of K5 projective tangent-flux repair2

Date: 2026-09-16
Status: **PROSPECTIVELY FROZEN BEFORE REPAIRED CRITIC IMPLEMENTATION / OUTPUT**

## Trigger

The original independent Critic preregistration `prereg/K5_PROJECTIVE_TANGENT_FLUX_REPAIR2_INDEPENDENT_CRITIC_REVIEW.md`, commit `0fe3f174adfc2937ca481bd6e007ae36adc2d3d5`, froze required check 4 as:

> construct the exact chart-transition map, scalar and flux transition determinants, and establish equality of the **full pulled-back coefficients after transport**, not merely valuation agreement.

Historical Critic implementation `04219154057e18ca9cd85df4634ebaf4ae1ccba5` and run `35148773201` did not execute that frozen obligation. Its `transition_det_at` and `numeric_witness` path substitutes one frozen angular point and `t=1/7`, then compares only those point values. Exact equality at one point is not equality of the full symbolic pulled-back coefficient functions.

Therefore historical Critic result commit `9c3100676e2975629921c05c66799b4d59a07a88` is quarantined as **`INVALID_IMPLEMENTATION`** for independent-authority purposes. This does not itself falsify the Researcher repair2 result.

## Unchanged scientific object

This is a control-only Critic implementation repair. The reviewed Researcher object, parent artifact, hypothesis, source ordering, q-families, faces, charts, verdict taxonomy, and interpretation ceiling remain exactly those frozen at `0fe3f174adfc2937ca481bd6e007ae36adc2d3d5`.

Reviewed Researcher authority remains:

- result `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_REPAIR2_RESULT.md`, commit `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`;
- Researcher repair2 prereg `d482b58d8d2640752ea9840eecf05bf444ded4cc`;
- run `35146728850`, job `104964596683`, head `90dc54e8568b77675cd6dfee4e9d8dbcec645fef`;
- artifact `10466668706`, ZIP SHA256 `3c6d2894b184bd8177a6d0c5eaced31c62c49b3b813710e9e9f118eeffd52b3e`;
- parent result JSON SHA256 `017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3`.

## Frozen repaired-Critic inputs

Retain without alteration:

1. generic field `q_i=(i+3)+2 alpha_{i+2 mod 10}-alpha_{i+5 mod 10}`;
2. exceptional field `q_i=2+(i+1)^2 alpha_0` at `Z={0}`;
3. proper-face representative `Z={0,...,k-1}` for every `k=1,...,9`;
4. two genuine projective/simplex charts per `k`, with the same dependent-coordinate rules frozen in the original Critic prereg;
5. K5 vertex-cycle permutation `(0,1,2,3,4)->(1,2,3,4,0)` and its induced ten-edge permutation;
6. exact parent artifact byte/hash locks above.

## Mandatory repair

The repaired Critic must independently reconstruct the differential-form/blow-up geometry without importing or executing Researcher code and must satisfy **all** original frozen checks. In particular:

1. For every `k=1,...,9`, retain angular/projective coordinates symbolically — do not substitute a numerical angular witness before chart comparison.
2. Compute the complete symbolic pulled-back scalar coefficient `PB(Omega_9)` and complete symbolic pulled-back flux coefficient `PB(i_u Omega_9)|dt=0` in both charts.
3. Construct the exact chart transition and its scalar/flux Jacobian determinants symbolically.
4. After substitution of the exact transition, require canonical symbolic identities
   `F0_scalar - F1_scalar*det(J9) == 0`
   and
   `F0_flux - F1_flux*det(J8) == 0`
   as rational functions of `t` and all independent angular/projective coordinates.
5. Record each symbolic difference after exact `together/cancel`; every one must be identically zero. A single-point or finite-grid equality is explicitly insufficient.
6. Retain the independent ambient identities, mechanical `t`-valuation extraction, S5 permutation controls, exceptional higher-order finite witness, source hard-code audit, parent artifact coverage, and provenance checks from the original preregistration.

## Frozen verdict rule

- `CONFIRMED_SCOPED` only if all original Critic checks plus the repaired full-symbolic chart relations pass exactly.
- `SCIENTIFIC_FAIL_CONFIRMED` if implementation/provenance are valid and an exact Researcher mathematical identity is independently false.
- `INVALID_IMPLEMENTATION` if any original frozen Critic obligation or this symbolic repair is absent/incomplete/hard-coded.
- `INVALID_PROVENANCE` if run/artifact/hash chronology or identity fails.
- `QUALIFIED` only for a precise surviving smaller scientific scope.

No criterion, field, face, chart, point, threshold, or interpretation ceiling may be changed after repaired output is seen.

## Interpretation ceiling

Even repaired `CONFIRMED_SCOPED` authorizes only prospective execution of the 34-orbit physical numerator/action-flux audit. It does not establish that audit, global Stokes/IBP, an integrated K5 period theorem, removal of `dim_C F_8=377`, a physical finite-part selector, regulator independence, F9/G3/G8, `NEW_PHYSICS_FOUND`, or complete QG.
