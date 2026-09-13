# Iteration 070A preregistration — finite-epsilon K4 joint-spectral tempered-family qualification

Date: 2026-09-13

This gate is frozen **before implementation and production**.

## Question

For the reduced source-backed K4 joint-spectral rational family used in Iter046–069, does every fixed finite `epsilon>0` causal-sign member define a smooth polynomially bounded function on real cycle space, and hence a tempered distribution, even though Iter069 proves generic `+6` growth and rules out a naive ordinary improper real-cycle integral?

## Frozen family

For every K4 tree/cycle basis and physical causal sign class,

`K_s(y) = prod_e [1 + c1*x_e + (c2/2)*x_e^2] / [x_e - i*s_e*epsilon]`,

with real affine edge flows `x_e(y,k)`, real finite gamma, `rho=gamma/2`,

`c1=2*rho/(rho^2+1/4)`, `c2=2/(rho^2+1/4)`,

and fixed `epsilon>0`.

## Frozen lanes

Physical sigma classes:

`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

Tree/cycle bases:

`S0, S1, P0, P1`.

Use two exact source points internally in every lane:

- `T1`: gamma=`37/100`, epsilon=`41/1000`, k=`(17,-29,21,-9)/100`;
- `T2`: gamma=`173/100`, epsilon=`137/1000`, k=`(-26,34,-11,3)/100`.

Matrix: `8 sign classes x 4 trees = 32 jobs`; each job evaluates both T1 and T2.

## Frozen predicates

For every case in every job:

1. all six edge flows are real affine functions of the real cycle variables;
2. for each denominator `d_e=x_e-i*s_e*epsilon`, `Im(d_e)=-s_e*epsilon` is a nonzero constant, so no denominator vanishes on real cycle space;
3. the source rational function is therefore smooth on all real cycle space;
4. exact generic radial degree is `+6`, consistent with Iter069;
5. a smooth locally integrable function with a global polynomial bound of finite degree defines a tempered distribution by integration against Schwartz test functions.

The implementation must record the exact denominator imaginary constants and derive the radial degree from the exact K4 incidence solve. The temperedness inference is allowed only if predicates 1–4 pass.

## Frozen classification

All 64 exact case evaluations pass:

`ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED`

otherwise:

`ITER070A_FINITE_EPSILON_TEMPEREDNESS_REVIEW`.

## Scope locks

- This qualifies only each fixed `epsilon>0` member as a tempered distribution.
- It does **not** prove that the family has a unique or finite `epsilon->0+` limit in `S'`.
- It does not reconstruct a common tube contour, does not authorize separate contact multiplication, and does not prove a physical causal vertex exists/fails.
- No preferred order, arbitrary counterterm, K5/G3/F9/G8 promotion, or vertex finiteness/divergence theorem follows.
