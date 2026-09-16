# Prospective preregistration — confirmed degree-four annihilator acting on actual invariant-dual numerator DAGs

Date: 2026-09-16

Parent terminal numerator authority:

`results/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_RESULT.md`, commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`.

Parent structural annihilator authority:

`results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_RESULT.md`, commit `686268eddb3f0e2aece5857ef75cec52716eccc6`, independently confirmed by Critic result commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`.

Exact projective-gauge action derivation:

`sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`, commit `97e71f0c20173b0c387461ff7f860baa12897fcd`.

This gate is frozen before implementation or action-output inspection.

## Scientific question

For the two actual full-all-32 invariant-dual degree-27 numerator channels `N_1,N_2`, does the confirmed unique S5-equivariant non-radial degree-four Kirchhoff annihilator act nontrivially? If it acts nontrivially, can exact rational point witnesses already falsify the cheapest finite-closure hypothesis

`B_v[N](alpha) = M N(alpha)`

with one constant rational `2x2` matrix `M` over the two physical channels?

This is an **algebraic pointwise action** gate. It does not yet use Stokes and cannot by itself give an integrated-period identity.

## Frozen exact action

Let the confirmed annihilator be

`v=sum_i v_i d/dalpha_i`, `v_i=alpha_i q_i`, `v(Psi_K5)=0`.

Set

`s1=sum_i alpha_i`, `S=sum_i v_i`.

For either exact degree-27 numerator channel define the homogeneous polynomial action numerator

`B_v[N] = s1 v(N) + { s1[div v +(1/2)sum_i q_i] - 3S } N`.

This is the exact numerator from the previously derived affine/projective gauge representative. It is polynomial homogeneous degree 31.

No integrated boundary term is dropped in this gate.

## Required derivative implementation

The directional derivative `v(N)` must be computed by exact forward-mode differentiation of the same canonical source/Wick numerator construction used by the terminal numerator-DAG authority, or by an exactly equivalent differentiated DAG.

Finite differences and floating-point differentiation are forbidden.

The implementation must reconstruct the Researcher-emitted 33-coefficient annihilator from the durable production summary and independently verify `v(Psi_K5)=0` at every frozen point before using it.

## Frozen points

Use exactly:

- `fit_A = edge01_2 = (2,1,1,1,1,1,1,1,1,1)`;
- `fit_B = mixed_small = (1,2,1,3,1,2,1,1,2,1)`;
- `validation_U = uniform = (1,1,1,1,1,1,1,1,1,1)`;
- `validation_G = (2,3,1,2,1,3,2,1,2,3)`.

No point may be changed after production output.

## Exact constant-closure test

At the two fit points form the `2x2` matrix whose columns are the physical numerator vectors `N(fit_A),N(fit_B)`.

If this matrix is singular, classify closure testing as `BLOCKED_FIT_DEGENERACY` without changing points.

If it is invertible, solve the unique rational constant matrix

`M = [B(fit_A) B(fit_B)] [N(fit_A) N(fit_B)]^(-1)`.

Then evaluate the exact residuals

`R_U=B(validation_U)-M N(validation_U)`,

`R_G=B(validation_G)-M N(validation_G)`.

A single nonzero rational residual is an exact counterexample to constant-`2x2` closure.

If both frozen validation residuals vanish, the outcome is only `NOT_FALSIFIED_ON_FROZEN_POINTS`; finite agreement may not be promoted to a polynomial identity.

## Mandatory acceptance controls

1. Reconstruct the exact K5 annihilator coefficients from `results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`.
2. Reconstruct the same exact physical numerator object as the terminal canonical-DAG gate: all 32 boundary components, 100000 source terms, dual/covector projection, order-four source-radius derivative, `N=Psi^9 J_4`.
3. At `validation_U`, reproduce the terminal numerator values exactly:
   `(-7038281250000000000,-5474218750000000000)`.
4. At `fit_A`, reproduce exactly:
   `(-59622158569312500000,-71069744360125000000)`.
5. At `fit_B`, reproduce exactly:
   `(-98730229673044210483200,-611255260651417598361600)`.
6. Exact forward-mode Euler control: replacing the annihilator direction by `E=sum alpha_i d_i` must give `E(N_c)=27 N_c` for both channels at all four frozen points.
7. The actual annihilator direction must give `v(Psi_K5)=0` exactly at all four frozen points.
8. Direct and independently organized differentiated evaluation paths must agree for `v(N_c)` at least at `validation_U` and `fit_A`.
9. No floating-point arithmetic may enter scientific values.
10. No integrated-period verdict may be emitted.

## Malformed controls

The same validator must detect/reject:

- vector Reynolds projection substituted for dual projection;
- one altered annihilator coefficient;
- direction replaced by a field that does not annihilate `Psi`;
- derivative order of the source radius changed from four;
- `Psi^9` numerator clearing changed;
- a fabricated constant-closure matrix not obtained from the two frozen fit points;
- finite validation agreement promoted to global closure.

## Frozen outcomes

Return exactly one scientific classification:

- `K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED` if at least one actual channel has an exact nonzero `B_v[N_c]` witness and at least one frozen validation residual for the fitted constant matrix is exactly nonzero;
- `K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_NOT_FALSIFIED_ON_FROZEN_POINTS_SCOPED` if at least one exact nonzero action witness exists but both frozen constant-closure validation residuals vanish;
- `K5_DEG4_ANNIHILATOR_ACTION_ZERO_ON_FROZEN_POINTS_INCONCLUSIVE_SCOPED` if both action channels vanish at all four frozen points; this is **not** a global zero theorem;
- `K5_DEG4_ANNIHILATOR_ACTION_BLOCKED_FIT_DEGENERACY_SCOPED` if the frozen fit numerator matrix is singular;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

## Interpretation ceiling

Exact nonzero point action proves only that the confirmed annihilator does not algebraically annihilate the physical numerator channel identically. Exact failure of constant `2x2` closure proves only that a two-channel constant-coefficient IBP module is insufficient.

No finite set of point evaluations can prove global closure. No Stokes identity, integrated-period zero/nonzero theorem, full 217-dimensional tensor result, reduction of the 377-dimensional supported ambiguity, physical finite-part selector, regulator independence, G3/F9/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
