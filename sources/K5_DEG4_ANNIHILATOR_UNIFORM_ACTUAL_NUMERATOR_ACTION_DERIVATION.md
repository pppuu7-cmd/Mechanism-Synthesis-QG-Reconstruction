# Exact uniform-point action of the confirmed K5 degree-four annihilator on the actual invariant-dual numerators

Date: 2026-09-16

Prospective action gate: `prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION.md`, commit `2111b42adc1ab79247c72d0043e5332b24eb7679`.

This derivation was made after the action gate was frozen and before its GitHub Actions production became terminal. It uses only already-terminal parent authorities and assigns no integrated-period value.

## Inputs

Confirmed unique non-radial degree-four annihilator:

`results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_RESULT.md`, independently confirmed by the Critic.

Its primitive 33-orbit coefficient vector is

`(0,0,0,0,3,3,0,0,0,0,0,3,0,3,-1,-1,0,-1,-3,-1,0,-3,0,5,-1,-1,0,-1,0,-1,0,0,0)`.

Terminal actual numerator values from

`results/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_RESULT.md`:

`N_1(1,...,1)=-7038281250000000000`,

`N_2(1,...,1)=-5474218750000000000`.

The projective-gauge action numerator is

`B_v[N]=s1 v(N)+{s1[div v +(1/2) sum_i q_i]-3S}N`,

with `v_i=alpha_i q_i`, `S=sum_i v_i`.

## Uniform-point annihilator data

At `alpha=(1,...,1)`, exact reconstruction of the 33 fixed-edge cubic orbit basis with the emitted primitive coefficients gives, for every edge `i`,

`q_i=0`,

`partial_i q_i=-15`.

This is also forced qualitatively by symmetry: at the uniform point an S5-equivariant edge vector is proportional to the Euler/radial direction. Since `v(Psi_K5)=0`, while `E(Psi_K5)=4 Psi_K5` and `Psi_K5(1,...,1)=125 !=0`, the proportionality coefficient must vanish. Thus `v_i=0` at the uniform point.

The explicit orbit derivative census gives

`div v = sum_i [q_i + alpha_i partial_i q_i] = 10*(-15) = -150`.

Hence

`sum_i q_i=0`, `S=0`, and `v(N_c)=0` pointwise because the tangent vector itself is zero there.

Therefore the exact physical action simplifies to

`B_v[N_c](1,...,1) = -150 N_c(1,...,1)`.

## Exact nonzero witnesses

Channel 1:

`B_v[N_1](1,...,1)=1055742187500000000000 != 0`.

Channel 2:

`B_v[N_2](1,...,1)=821132812500000000000 != 0`.

Thus the confirmed K5 degree-four Kirchhoff annihilator does **not** algebraically annihilate either actual invariant-dual numerator identically.

This is an exact nonzero point witness; no sampling inference is needed for this one-sided conclusion.

## What remains for the active action gate

The queued frozen production still has independent scientific value:

1. forward-mode automatic differentiation on the full all-32 numerator DAG must reproduce the uniform result and the Euler control `E(N_c)=27N_c`;
2. it evaluates the action at the two frozen fit points and an additional validation point;
3. it can exactly falsify the cheapest constant-`2x2` closure hypothesis by an out-of-sample rational residual.

Finite point agreement, if it occurs, will not be promoted to global closure.

## Interpretation ceiling

This proves only nonzero algebraic action of the structural annihilator on each physical numerator channel. It does not justify Stokes at higher-codimension Schwinger corners and does not imply any integrated-period zero/nonzero result.
