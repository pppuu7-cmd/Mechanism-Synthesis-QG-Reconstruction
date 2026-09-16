# K5 degree-four annihilator — projective/affine-gauge action derivation and boundary caveat

Date: 2026-09-16

Status: exact outcome-independent derivation. This note does not use or assign any invariant-dual period value.

Parent structural theorem: `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_RESULT.md`, commit `686268eddb3f0e2aece5857ef75cec52716eccc6`, independently confirmed by `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC_RESULT.md`.

## 1. Frozen integrand class

For either invariant-dual numerator channel let

`F_N(alpha)=W(alpha) N(alpha) / Psi(alpha)^(21/2)`,

where

- `W=prod_i alpha_i^(1/2)` has degree 5;
- `N` has degree 27;
- `Psi=Psi_K5` has degree 4.

Hence `F_N` is homogeneous of degree `-10`, matching the ten Schwinger variables.

Let the confirmed degree-four annihilator be

`v=sum_i v_i d/dalpha_i`,

with `v_i=alpha_i q_i`, `deg v_i=4`, `deg q_i=3`, and

`v(Psi)=0`.

The Researcher/Critic theorem does **not** imply `sum_i v_i=0`, so affine-simplex tangency may not be assumed.

## 2. Exact tangent representative on the standard simplex

Write

`s1=sum_i alpha_i`, `S=sum_i v_i`, `c=S/s1`.

Because `S` has degree four, `c` is a regular homogeneous rational function of degree three on the positive projective domain `s1>0`.

Define

`u_i = v_i - c alpha_i`.

Then identically in the ambient positive cone

`sum_i u_i = S-c s1 = 0`.

Therefore `u` is tangent to every affine slice `s1=constant`, in particular to the standard simplex `s1=1`.

Since both terms in `u_i` contain `alpha_i`, every component remains face-tangent:

`u_i = alpha_i (q_i-c)`.

No physical regulator, new metric, or subtraction datum has been introduced; this is only the radial/projective representative of the same projective vector-field class.

## 3. Exact divergence identity

In ten variables,

`div(c E)=E(c)+10c`.

Since `c` is homogeneous degree three,

`E(c)=3c`,

so

`div u = div v - 13 c`.

Because `F_N` has homogeneous degree `-10`,

`E(F_N)=-10 F_N`.

Furthermore `v(Psi)=0` and

`v(W)/W = (1/2) sum_i v_i/alpha_i = (1/2) sum_i q_i`.

Hence

`u(F_N)=v(F_N)-c E(F_N)`

and exact simplification gives

`div(u F_N)`

`= W/Psi^(21/2) * { v(N) + [div v + (1/2) sum_i q_i - 3c] N }`.

Thus the affine-simplex IBP numerator operator is

`A_v[N] = v(N) + [div v + (1/2) sum_i q_i - 3 S/s1] N`.

This formula is exact and source-normalization independent.

## 4. Homogeneous projective representation

`A_v[N]` is homogeneous degree 30 as a rational function. To write a degree-27 projective numerator define

`P_v[N] = A_v[N]/s1^3`

or, equivalently,

`P_v[N] = B_v[N]/s1^4`,

where the polynomial numerator

`B_v[N] = s1 v(N) + { s1[div v + (1/2) sum_i q_i] - 3S } N`

is homogeneous degree 31.

On the standard simplex `s1=1`, `P_v[N]`, `A_v[N]`, and `B_v[N]` have the same numerical value. The explicit powers of `s1` only restore projective homogeneity; they introduce no singularity on the positive projective domain because `s1>0` there.

If Stokes is justified globally, the induced relation would be

`integral_Delta W * B_v[N] / [s1^4 Psi^(21/2)] = 0`.

No claim that `B_v[N]` is divisible by `s1^4`, closes on the two physical numerator channels, or is nonzero is made here.

## 5. Open-face flux vanishing

On an open codimension-one Schwinger face `alpha_i=0`,

`u_i = alpha_i(q_i-c)`

while

`W ~ alpha_i^(1/2)`.

The normal flux therefore carries at least

`alpha_i^(3/2)`.

The already validated K5 tree count gives 75 spanning-tree monomials on every single-edge face, so `Psi|_(alpha_i=0)` is nonzero in the **interior** of that face. Therefore the regular face flux vanishes pointwise on every open codimension-one face.

## 6. Higher-codimension corner firewall

The previous paragraph is **not** a global Stokes theorem.

At boundaries of a codimension-one face, several Schwinger parameters may vanish simultaneously. Then `Psi_K5` can itself vanish when the remaining positive-edge graph disconnects. The factor `Psi^(-21/2)` can therefore compete with the explicit alpha powers, and the integral of the boundary flux near such corners is not decided by the open-face `alpha_i^(3/2)` factor alone.

Consequently a future projective-IBP action gate must prospectively audit every relevant Schwinger boundary scaling stratum, or provide an equivalent sector-decomposition/analytic-continuation theorem, before dropping the total boundary integral.

The exact-zero K3/K4 **collision** residues do not automatically equal Schwinger-simplex corner terms; no such identification is authorized.

## 7. Authorized use

Once the two invariant-dual degree-27 numerator objects are materialized, the confirmed annihilator can be applied algebraically through `B_v[N]` without ambiguity. Before integrating the resulting total derivative, however, a complete Schwinger-corner boundary audit is mandatory.

Useful exact questions for that successor include:

1. whether `B_v[N_c]` is identically zero or nonzero for either channel;
2. whether it is divisible by `s1^4`, giving a polynomial degree-27 projective representative;
3. whether the resulting projective numerators close in a finite module containing `N_1,N_2`;
4. whether all boundary scaling strata make the Stokes flux integrable/zero.

No integrated-period theorem follows from the present derivation alone.
