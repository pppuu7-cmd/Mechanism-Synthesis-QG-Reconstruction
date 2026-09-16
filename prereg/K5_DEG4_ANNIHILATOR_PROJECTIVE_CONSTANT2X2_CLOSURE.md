# Prospective preregistration — K5 degree-4 annihilator projective constant-2x2 closure

Date: 2026-09-16

## Parent authority and Critic correction

Parent exact action authority is repaired production run `35130545821`, job `104910177408`, artifact `10461780450`, production JSON SHA256 `909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`, with durable result `results/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION_REPAIR1_RESULT.md`.

Controlling independent Critic is `results/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_ACTION_REPAIR1_ADVERSARIAL_REVIEW.md`, commit `dfaf9ca72f056d2bfcb4e8bbdff8b9301f54107e`, verdict `REQUIRES_NEW_PREREGISTERED_GATE`.

The Critic identified the raw-cone test `B_v[N]=M N` as the wrong closure object because `deg B=31` and `deg N=27`. The correct degree-matched projective numerator is

`P_v[N](alpha)=B_v[N](alpha)/s1(alpha)^4`,

where `s1=sum_e alpha_e`. Equivalently one may normalize every representative to `s1=1` before comparison.

This gate is frozen before inspecting the projective fit/validation outcome.

## Scientific question

Do the two actual full-all-32 invariant-dual degree-27 projective numerator channels close under the confirmed degree-four K5 Kirchhoff annihilator through one constant rational `2x2` matrix

`P(alpha)=M N(alpha)`

on the prospectively frozen four representatives inherited from the parent gate?

This tests only constant closure of the two-channel projective module. It is not an integrated-period theorem and not a test of all polynomial/rational coefficient modules.

## Frozen inputs

Use exactly the four parent representatives, in authoritative edge order `(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`:

- `fit_A=(2,1,1,1,1,1,1,1,1,1)`;
- `fit_B=(1,2,1,3,1,2,1,1,2,1)`;
- `validation_U=(1,1,1,1,1,1,1,1,1,1)`;
- `validation_G=(2,3,1,2,1,3,2,1,2,3)`.

Consume the exact parent values `N_c(alpha)` and `B_c(alpha)` only from the authoritative repaired result/raw authority tied to the parent production hash. Do not refit, resample, replace points, select a boundary component, or alter the two dual channels.

For each point compute exactly

`P_c=B_c/s1^4`.

Fit the unique constant rational matrix `M` from `fit_A` and `fit_B` iff the `2x2` numerator matrix there is invertible. Test the same `M` at both validation points.

## Mandatory scale/projective controls

Because `N` and `P` are both homogeneous degree 27, the validator must verify exact projective compatibility under `alpha -> 2 alpha`:

- `N(2alpha)=2^27 N(alpha)`;
- `B(2alpha)=2^31 B(alpha)`;
- `P(2alpha)=2^27 P(alpha)`;
- the closure residual scales by `2^27` and therefore cannot be created or removed by changing homogeneous representative.

The old raw test `B=M N` must be explicitly rejected as grading-incompatible whenever `B!=0`.

## Frozen outcomes

Return exactly one scientific classification:

- `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_CONFIRMED_ON_FROZEN_POINTS_EXACT_SCOPED` iff the fit matrix exists and both validation residual vectors are exactly zero;
- `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED` iff the fit matrix exists and at least one validation residual vector is exactly nonzero;
- `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_BLOCKED_FIT_DEGENERACY_SCOPED` iff the frozen fit numerator matrix is singular;
- `INVALID_IMPLEMENTATION` or `INVALID_PROVENANCE` for implementation/provenance failure.

## Controls

A valid implementation must:

1. lock the parent production JSON identity/hash or a repo-persisted authoritative exact summary traceable to it;
2. verify all four frozen representatives and their exact `s1` values;
3. verify the two channels are retained and no representative component replaces the invariant-dual projection;
4. compute `P=B/s1^4` with exact rational arithmetic;
5. verify degree matching `deg N=deg P=27` and raw `deg B=31`;
6. verify the scale controls above at at least one nonzero frozen point without re-running source contraction;
7. fit only on `fit_A/fit_B` and validate only on `validation_U/validation_G`;
8. reject a deliberately altered projective denominator power `s1^3` or `s1^5` through the same closure/scale logic;
9. reject promotion of finite-point agreement/failure to a global polynomial/rational-module theorem;
10. issue no integrated-period verdict.

## Interpretation ceiling

A CONFIRMED result establishes only that the corrected projective action is consistent with one constant `2x2` matrix on the four frozen representatives; without a global exact identity it is not global closure.

A FALSIFIED result exactly excludes this constant two-channel projective closure ansatz because the fit matrix fails on prospectively frozen validation representatives. It does not prove all IBP reduction fails; polynomial/rational coefficient modules or additional channels may remain.

No Stokes/integrated-period theorem, no full 217-dimensional tensor theorem, no reduction of `dim_C F_8=377`, no physical finite-part selector, no regulator independence, no F9/G3/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.