# Iteration 069A preregistration — symbolic K4 joint-spectral homogeneous asymptotics

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

For the source-backed reduced `j=1/2` K4 joint-spectral rational family already used in Iter046–052, what is the exact highest homogeneous behavior when all three independent K4 cycle variables are scaled together?

This gate is deliberately upstream of any sequential finite part, counterterm, forest prescription, or collision pullback.

## Frozen family

Use the exact K4 incidence solve and the same six-edge rational kernel as `distributional/k4_forest_order_finite_part.py`:

`K_s(y) = prod_e [1 + c1*x_e + (c2/2)*x_e^2] / [x_e - i*s_e*epsilon]`,

where each constrained edge flow is affine in the three cycle variables,

`x_e(y,k) = b_e(k) + L_e(y)`,

and

`c1=2*rho/(rho^2+1/4)`, `c2=2/(rho^2+1/4)`, `rho=gamma/2`.

The frozen no-contact denominator control is

`C_s(y)=prod_e 1/[x_e-i*s_e*epsilon]`.

## Frozen scaling

Set `y = lambda*v`, with symbolic `v=(v0,v1,v2)`, and consider a generic direction where none of the six exact linear edge slopes `L_e(v)` vanishes.

Audit all four previously frozen K4 tree/cycle bases:

`S0, S1, P0, P1`.

Matrix: **4 exact symbolic lanes**.

## Frozen expected identities to prove, not assume

For every tree basis, derive the six exact slope forms from the incidence solve and test symbolically:

1. all six slope forms are nonzero polynomials in `(v0,v1,v2)`;
2. the source kernel has generic total radial degree `+6`;
3. the no-contact denominator control has generic total radial degree `-6`;
4. the exact source leading coefficient is

   `(c2/2)^6 * prod_e L_e(v)`;

5. the leading source homogeneous sector is independent of the six causal denominator signs `s_e`, of `epsilon`, and of the external flow `k`;
6. the control leading coefficient is `1/prod_e L_e(v)`.

The proof object must be generated from the exact incidence solve, not entered as a hand-written list of slopes.

## Frozen classification

All four tree lanes satisfy all symbolic identities:

`ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT`

Otherwise:

`ITER069A_SYMBOLIC_ASYMPTOTIC_REVIEW`.

## Scope locks

- This is an asymptotic theorem for the reduced joint-spectral rational family used in the K4 distributional program, not a full group-valued Toller theorem.
- Generic `lambda^6` growth obstructs a naive ordinary real-cycle improper integral at infinity; it does **not** rule out a source-defined analytic/distributional boundary value or correlated contour.
- Sign independence of the highest homogeneous sector is not a physical causal-sector equivalence.
- No preferred order, finite counterterm, K5/G3/F9/G8 promotion, or vertex finiteness/divergence theorem is authorized.
