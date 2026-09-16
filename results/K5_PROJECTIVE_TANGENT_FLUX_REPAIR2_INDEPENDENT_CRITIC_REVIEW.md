# Independent Critic review — K5 projective tangent-flux repair2

Date: 2026-09-16

## RESULT_REVIEWED

Researcher classification: `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.
Researcher result commit: `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`.
Researcher repair2 prereg: `d482b58d8d2640752ea9840eecf05bf444ded4cc`.
Researcher production: run `35146728850`, job `104964596683`, artifact `10466668706`, ZIP SHA256 `3c6d2894b184bd8177a6d0c5eaced31c62c49b3b813710e9e9f118eeffd52b3e`, result JSON SHA256 `017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3`.

Critic prereg: `prereg/K5_PROJECTIVE_TANGENT_FLUX_REPAIR2_INDEPENDENT_CRITIC_REVIEW.md`, commit `0fe3f174adfc2937ca481bd6e007ae36adc2d3d5`.
Critic implementation: `04219154057e18ca9cd85df4634ebaf4ae1ccba5`.
Critic workflow/head: `20ab932f5838847d2f694261472a865176942107`.
Critic production: run `35148773201`, job `104971456723`, terminal success.
Critic artifact: `10468526345`, ZIP SHA256 `68ee3e2c4e228eb0a5b96242b0ccef1fe140a88920b9e0622b1f279a5659a1d6`.
Critic result JSON SHA256: `cad71019f224bdab0b59598081ba73d08117dbed285f8a865d2b86a29683fbee`.

## SOURCE_OBJECT_CHECK

This review stays entirely within the corrected projective Schwinger boundary geometry sub-gate. It does not replace the full all-32/source-ordered K5 object, change the Toller source ordering, change the published spectral `i epsilon`, or consume a representative boundary state as a physical amplitude verdict.

## SOURCE_ORDERING_CHECK

No reordering of one-wedge spectral/spinor integration, Toller function construction, ten-wedge product, full boundary contraction, or K5 group/distributional integration is introduced.

## PROVENANCE_CHECK

The Critic workflow independently downloaded parent artifact `10466668706` from GitHub Actions, reproduced ZIP SHA256 `3c6d2894...`, unpacked it, and reproduced parent `result.json` SHA256 `017f25d4...` before the scientific reconstruction. The downloaded Critic artifact was subsequently re-downloaded and independently rechecked byte-for-byte; its ZIP and JSON hashes reproduce the values above.

## ERRATUM_CHECK

Historical source-lock-invalid Iter077E/F remain quarantined. The prior corrected tangent-flux run `35104985610` remains `INVALID_IMPLEMENTATION`; failed repair1 run `35124809996` remains non-authoritative. This review applies only to repair2.

## BOUNDARY_COMPLETENESS_CHECK

Parent artifact coverage is exact: 18 `(k,chart)` witnesses for `k=1..9`, 9 chart-transition witnesses, 9 S5/K5 permutation witnesses, one nontrivial exceptional-leading-zero witness, and explicit empty/full-set nonphysical firewalls.

The Critic independently reconstructed 18 explicit differential-form witnesses, both genuine charts for every `k=1..9`, 9 orientation/Jacobian relations, and 9 S5-induced permutation controls.

## DISTRIBUTIONAL_CHECK

No new distributional product/pullback theorem is asserted. This is local projective differential-form/blow-up geometry only.

## REGULATOR_CHECK

No regulator removal or regulator-independence claim is made. Published one-wedge spectral `i epsilon` remains retained.

## COUNTEREXAMPLE_ATTEMPTS

The Critic used a different frozen nonradial polynomial family

`q_i=(i+3)+2 alpha_{i+2 mod 10}-alpha_{i+5 mod 10}`

and independently verified exact ambient identities, mechanically extracted scalar orders `0,1,...,8` in both charts, all chart orientation/Jacobian relations, and all S5 permutation valuations.

A separate exceptional family

`q_i=2+(i+1)^2 alpha_0`

gives generic flux order `1` and exceptional flux order `2`, with exact nonzero leading coefficient `736/9`. Thus the independent extractor also advances through a cancelled leading order rather than reporting a hard-coded exponent.

The Researcher source audit found no forbidden `jac_exp=k-1`, `scalar_valuation=k-1`, `sv=k-1`, or equivalent scalar-valuation assignment shortcut. Mechanical pullback/valuation machinery is present in the decision path.

## SURROGATE_CHECK

No scalar K4/K5 surrogate is promoted to the physical K5 amplitude. The result is only a geometry prerequisite for the subsequently frozen physical numerator/action-flux audit.

## OVERCLAIM_CHECK

This confirmation does not classify the 34 physical corner orbits, establish global Stokes/IBP, evaluate an invariant-dual K5 period, reduce `dim_C F_8=377`, select a finite part, establish regulator independence, authorize F9/G3/G8, or imply `NEW_PHYSICS_FOUND` / complete QG.

## VERDICT

**`CONFIRMED_SCOPED`**

The corrected local projective tangent normal-flux/blow-up geometry survives an independent exact Critic reconstruction in the frozen scope.

## QUALIFICATIONS

The Critic reconstruction is an independent exact witness family over all `k=1..9` and both chart types, not a second full symbolic reproduction of every angular polynomial coefficient in the Researcher artifact. The parent full symbolic artifact provenance and coverage were independently verified before these controls.

## UPDATED_CRQN_CHAIN

`... -> scalar corner Jacobian k-1 retained -> obsolete raw-v projective flux SCIENTIFIC_FAIL_CONFIRMED -> corrected projective-tangent flux geometry CONFIRMED_SCOPED -> 34-orbit physical numerator/action-flux audit AUTHORIZED -> global projective Stokes/IBP ? -> invariant-dual K5 periods ? -> ...`

## AUTHORIZED_NEXT_GATE

Prospectively freeze and execute the **34-orbit physical numerator/action-flux audit**, using the confirmed projective tangent representative/geometry, canonical degree-27 numerator DAG, both physical invariant-dual channels, exact corner/orbit representatives, S5 covariance, and independent reconstruction of key valuations. Keep geometric Jacobian order, numerator/action zero-or-pole order, and final integrability exponent separate. No global Stokes or integrated-period conclusion is authorized from local corner data alone.
