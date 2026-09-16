# K5 projective tangent normal-flux scaling — control repair 2 result

Date: 2026-09-16

## Status

Researcher production status: `PASS_EXACT_SCOPED`

Classification:

`K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`

Independent Critic review: **PENDING**. This Researcher result does not by itself authorize the 34-orbit physical corner classification.

## Frozen contract

Parent scientific preregistration:

`prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`, commit `bf6464e30893101a7bd6fd59b78b8b00dea14f61`.

Historical parent implementation was independently classified `INVALID_IMPLEMENTATION` by Critic commit `3335307be94fada4366f88565496f96b657e2c70`.

Control repair 1 preregistration:

`prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_1.md`, commit `68c14c6774d27388878c0f2fe6c3741eab828e87`.

Repair-1 production run `35124809996`, job `104891115629`, head `4481ad4c33e6b82ca48dec4da93bda1e78b271f3` failed before scientific classification because the exact-form comparator used polynomial `expand()` on rational expressions containing `1/s1`. That run has no substantive scientific authority.

Control repair 2 was prospectively frozen before implementation:

`prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_2.md`, commit `d482b58d8d2640752ea9840eecf05bf444ded4cc`.

Repair-2 implementation commit:

`1b59d5426e9eeec4e99f01510da7fe220d1640f3`.

Workflow/head:

`90dc54e8568b77675cd6dfee4e9d8dbcec645fef`.

## Authoritative Researcher production

- run `35146728850`, terminal success;
- job `104964596683`, terminal success;
- artifact `10466668706`, `k5-projective-tangent-normal-flux-exact-repair2`;
- artifact ZIP digest `sha256:3c6d2894b184bd8177a6d0c5eaced31c62c49b3b813710e9e9f118eeffd52b3e`;
- production result JSON SHA256 `017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3`.

All frozen implementation checks and all exact mathematical checks passed.

## Exact differential-form construction

The verifier constructs

`Vol = dalpha_0 wedge ... wedge dalpha_9`,

`Omega_9 = i_E Vol`, with `E=sum_i alpha_i partial_i`,

as exact antisymmetric differential-form data.

For a generic nonradial polynomial logarithmic field

`v_i = alpha_i q_i(alpha)`,

it constructs

`u = v - (S/s1) E`, `S=sum_i v_i`, `s1=sum_i alpha_i`,

and verifies exactly:

- `u(s1)=0`;
- `i_E Omega_9=0`;
- `i_v Omega_9 = i_u Omega_9`;
- `v -> v+f(alpha)E` leaves the contracted projective form invariant.

Rational differential-form coefficients are compared after exact `together/cancel` canonicalization, not polynomial expansion alone.

## Explicit blow-up pullbacks

For every proper-face size `k=1,...,9`, the verifier uses the proper subset `Z={0,...,k-1}` and performs explicit substitutions

`alpha_e=t beta_e` for `e in Z`

inside two genuinely distinct simplex/projective charts with different dependent beta and/or eliminated outside coordinate.

For each of the 18 `(k,chart)` witnesses it mechanically computes:

- the pulled-back scalar `Omega_9` coefficient;
- its lowest nonzero `t` valuation and exact leading coefficient;
- the pulled-back `i_u Omega_9` normal flux;
- its lowest nonzero `t` valuation and exact leading coefficient;
- the projective normal component `u(t)`;
- the exact chart identity

`PB(i_u Omega_9)|_{dt=0} = PB(Omega_9)_{dt wedge ...} * u(t)`.

The scalar valuation is derived mechanically as `k-1`; it is not inserted into the decision path.

For the generic frozen polynomial field the normal-flux valuation is mechanically finite for every `k=1,...,9`.

## Genuine chart-transition control

For every `k=1,...,9`, the verifier constructs the exact transition map between the two simplex charts and its determinant.

It verifies equality of the **full pulled-back scalar top form** and the **full pulled-back flux form** under the transition Jacobian. Thus chart equivalence is stronger than merely matching valuations.

All nine scalar and all nine flux chart-transition identities pass exactly.

## Separate K5/S5 permutation control

The verifier uses the nontrivial K5 vertex permutation

`(0,1,2,3,4) -> (1,2,3,4,0)`,

with induced edge permutation

`[4,5,6,0,7,8,1,9,2,3]`.

It pushes forward the generic field and independently checks the original and permuted proper subsets for every `k=1,...,9`.

All nine mechanically extracted scalar/flux valuation pairs agree. This is logically separate from the chart-equivalence test.

## Nontrivial exceptional leading-zero witness

The exceptional nonradial polynomial family is

`q_i = 1 + (i+1) alpha_0`, `i=0,...,9`,

at the proper face `Z={0}`.

It is not the identically radial Euler field. The normal flux is not identically zero.

For the generic field at the same face:

`flux valuation = 1`.

For the exceptional field:

`flux valuation = 2`.

The exact exceptional leading coefficient is

`-8*yexc_0 - 7*yexc_1 - 6*yexc_2 - 5*yexc_3 - 4*yexc_4 - 3*yexc_5 - 2*yexc_6 - yexc_7 + 9`.

Therefore the extractor demonstrably advances past a cancelled naive leading term to the next finite nonzero `t` order.

## Machine-readable coverage

Production emitted:

- 18 proper-face/chart witnesses;
- 9 full chart-transition witnesses;
- 9 K5/S5 permutation witnesses;
- one nontrivial exceptional-leading-zero witness;
- ambient `Omega_9`, `i_v Omega_9`, `i_u Omega_9`, `i_E Omega_9` form terms;
- empty/full-set control firewalls.

All repair-2 implementation obligations are represented in the production decision path.

## New scoped fact

At Researcher level, the corrected local projective tangent normal-flux/blow-up geometry survives the frozen exact differential-form, chart-transition, radial, permutation and exceptional-cancellation tests.

This repairs the implementation defects identified by the earlier independent Critic. It does **not** retroactively validate historical run `35104985610` or failed repair-1 run `35124809996`.

## Interpretation ceiling

Until a fresh independent Critic review confirms this repair-2 production, the 34-orbit physical numerator/action-flux audit remains blocked from substantive classification.

Even after such confirmation, this result alone does not establish:

- a 34-orbit physical numerator/action-flux classification;
- a global projective Stokes/IBP theorem;
- an integrated invariant-dual K5 period zero/nonzero theorem;
- any reduction of `dim_C F_8=377`;
- a physical finite-part selector;
- regulator independence;
- F9/G3/G8;
- `NEW_PHYSICS_FOUND` or complete quantum gravity.

## Authorized next state

Request/await a fresh independent Critic review of this exact repair-2 production. Only if that review is terminally confirming may the prospectively frozen 34-orbit physical numerator/action-flux gate be opened.
