# Iter083F-SM preregistration — common finite spectral epsilon does not regularize the K5 common collision

Date: 2026-09-15

## Status

Prospective exact scoped gate after Iter083E. The exploratory derivation has already identified the candidate finite-epsilon formulas; this preregistration freezes the source object, algebraic obligations, controls and interpretation ceiling before implementation/production promotion.

## Scientific question

A natural new construction after Iter083E is to *reverse the published source ordering*: keep the Feynman spectral regulator `epsilon>0` finite in all ten wedge Toller integrals, form the full K5 product/boundary contraction/group distribution first, and only then consider `epsilon -> 0+`.

Before asking whether that new common-epsilon limit selects an extension, the first question is more basic:

**Does a finite common spectral epsilon regularize the simultaneous K5 group collision at all?**

The candidate exact answer in the frozen all-`j=1/2` sector is no. The finite-epsilon contour shifts the spectral variable `rho`, but after the Toller kernel cancels the pole denominator the small-boost singularity of every elementary branch remains exactly `beta^-2` with the same leading coefficient as at `epsilon=0`. Hence the ten-wedge common-collision product retains the same nonzero `r^-20` leading tensor at every fixed sufficiently small `epsilon>0`.

## Frozen public source authority

### Toller companion `arXiv:2604.24945`

For fixed `beta>0`, Eq. (17) defines the finite-epsilon functional

`I_epsilon^(+-)[f] = integral d(rho_tilde)/(2 pi i) [+- P_jl(rho_tilde;rho)/(rho_tilde-rho -+ i epsilon)] f(rho_tilde)`.

The paper states that `P_jl` cancels all Toller poles. For the plus branch the only remaining pole is at `rho_tilde=rho+i epsilon` and the contour closes in the upper half-plane; for the minus branch the analogous pole is `rho-i epsilon` in the lower half-plane. The cross-branch contour has no enclosed pole.

Therefore, before taking the limit, the same contour argument gives for fixed positive epsilon in its admissible range

`I_epsilon^+[d] = P_jl(rho+i epsilon;rho) t^+(rho+i epsilon,beta)`,

`I_epsilon^-[d] = P_jl(rho-i epsilon;rho) t^-(rho-i epsilon,beta)`.

Eq. (16) gives the Toller kernel.

For `j=l=1/2`,

`P_(1/2,1/2)(rho_tilde;rho) = (rho_tilde^2+1/4)/(rho^2+1/4)`.

Table II gives explicit `j=l=k=1/2` Toller branches for both `m=+-1/2`. In every branch the denominator contains

`(rho+i/2)(rho-i/2)=rho^2+1/4`.

The physical gamma-simple specialization uses `rho=gamma j=gamma/2`.

### Causal vertex `arXiv:2601.23162v1`

The published source takes the one-wedge `epsilon->0+` limit in the definition of each Toller matrix before forming the product of ten Toller matrices. Hence the common finite-epsilon construction tested here is explicitly a **new candidate regulator**, not a claim about the published source definition.

## Frozen upstream repository authority

1. Iter077I establishes that at `epsilon=0` every all-`j=1/2` Toller branch has leading small-boost order `beta^-2`, with opposite branches differing only by a nonzero sign, and that the frozen ten-wedge boundary contraction has a nonzero `r^-20` leading tensor.
2. Iter077L/M establish the common-collision geometry `N subset M`, `codim_R N=12`, and source scaling degree `20`.
3. Iter083B classifies the resulting same-scaling-degree supported ambiguity as `F_8`, `dim_C F_8=377`.
4. Iter083E proves the source one-wedge epsilon prescription itself cannot select the joint extension and leaves a deliberately new common finite-epsilon construction as an open candidate.

## Frozen finite-epsilon object

For `epsilon>0`, define the exploratory finite-epsilon elementary branch

`T_epsilon^(+-)`

by replacing the source `lim_(epsilon->0+) I_epsilon^(+-)[d]` with `I_epsilon^(+-)[d]` at fixed epsilon.

Use the **same epsilon in all ten wedges** and form the source-ordered ten-factor K5 boundary-contracted function/distribution before taking any epsilon limit.

No extra damping in beta/group variables, no radial cutoff and no subtraction is added.

## Exact proof obligations

### P0 — finite-epsilon contour identity

Derive, without prematurely taking `epsilon->0`,

`I_epsilon^+[d] = P(rho+i epsilon;rho) t^+(rho+i epsilon,beta)`,

`I_epsilon^-[d] = P(rho-i epsilon;rho) t^-(rho-i epsilon,beta)`.

The proof must explicitly use cancellation of Toller poles and the empty cross-branch contour. It must state the finite-epsilon range needed for the contour/asymptotic argument, if any.

### P1 — exact j=1/2 kernel cancellation

For `j=l=1/2`, prove

`P(rho_tilde;rho)=(rho_tilde^2+1/4)/(rho^2+1/4)`.

Substituting `rho_tilde=rho+-i epsilon` into the Table-II Toller branches must cancel the complete shifted factor `rho_tilde^2+1/4` exactly. The surviving physical denominator must be `rho^2+1/4`, independent of epsilon.

### P2 — all four finite-epsilon reduced branches

For `m=+1/2`, require the exact forms

`I_epsilon^+[d] = - exp(+i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d] = + exp(-i rho beta) exp(-epsilon beta) [cosh(beta)+2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`.

For `m=-1/2`, require

`I_epsilon^+[d] = + exp(+i rho beta) exp(-epsilon beta) [cosh(beta)-2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d] = - exp(-i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`.

If an exact source-convention audit changes a subleading `epsilon sinh(beta)` sign, the preregistered scientific PASS may still hold only if the leading `beta^-2` coefficient and all source branch signs are unchanged; any such convention repair must be documented before production promotion. The leading coefficients themselves are frozen and may not be changed.

### P3 — epsilon-independent leading collision coefficient

For every fixed finite `epsilon>0`, prove as `beta->0+`

`I_epsilon^(+-)[d] = c_(+- ,m)(rho) beta^-2 + O(beta^-1)`

with

`c_(+, +1/2) = -1/[2(rho^2+1/4)]`,

`c_(+, -1/2) = +1/[2(rho^2+1/4)]`,

`c_(-, +1/2) = +1/[2(rho^2+1/4)]`,

`c_(-, -1/2) = -1/[2(rho^2+1/4)]`.

No leading coefficient may depend on epsilon.

At `rho=gamma/2`, the magnitude is exactly

`2/(1+gamma^2)`.

### P4 — full Toller matrix and angular tensor

Restore the SU(2) Cartan factors. Since the finite-epsilon modification acts only in the reduced boost factor, prove that the leading full `T_epsilon^(+-)(g)` angular matrix is exactly the same nonzero leading angular matrix as in Iter077I, multiplied by the same branch sign, with no epsilon-dependent leading deformation.

### P5 — ten-wedge K5 product

On the frozen nonzero angular witness used by Iter077I, show that the product of ten finite-epsilon branches retains

`C(kappa,gamma) r^-20 + O(r^-19)`

with the same nonzero leading coefficient/tensor `C` as at epsilon=0 (up to the already frozen branch-sign product).

Consequently the fixed-epsilon transverse scaling degree remains exactly `20`.

### P6 — no local-integrability regularization

Because `codim_R N=12`, a nonzero `r^-20` common-collision singularity is not locally integrable in the 12 normal variables. A finite common spectral epsilon therefore does **not** define the K5 distribution across `N` merely by making the ten spectral denominators finite.

Equivalently, keeping epsilon finite does not collapse the Iter083B extension problem before any additional joint prescription is supplied.

### P7 — regulator classification

Conclude only:

`COMMON_FINITE_ONE_WEDGE_SPECTRAL_EPSILON_IS_NOT_A_K5_COLLISION_REGULATOR_IN_THE_FROZEN_J_HALF_SECTOR`.

Do not conclude that every possible correlated multivariable regulator fails. A successful joint regulator must modify/control the collision-normal singularity or impose additional multivariable analytic information beyond holding the existing spectral epsilon finite.

## Mechanical validation

The implementation must use exact rational/algebraic checks where possible and must not infer the result from floating-point fits alone.

At minimum it must verify:

- the `j=1/2` kernel polynomial identity;
- exact cancellation of the shifted `rho_tilde^2+1/4` denominator;
- all four branch leading signs;
- epsilon independence of the leading coefficient symbolically/algebraically;
- gamma-simple substitution `rho=gamma/2 -> |c|=2/(1+gamma^2)`;
- tenfold order `2*10=20` versus codimension 12.

## Negative controls

The validator/review must reject:

1. replacing `exp(-epsilon beta)` by `exp(-epsilon/beta)` and calling it the source regulator;
2. replacing spectral `rho -> rho+-i epsilon` by a group-normal shift `beta -> beta+-i epsilon`;
3. dropping the Toller kernel `P_jl`, which would leave a spurious epsilon-dependent pole denominator;
4. claiming that a bounded spectral denominator implies local integrability in beta;
5. checking only the Barrett-Crane `j=0` example instead of the physical frozen `j=1/2` sector;
6. taking `epsilon->0` before the small-beta analysis and then claiming to have tested finite epsilon;
7. inferring that no genuinely joint K5 regulator can exist;
8. promoting this candidate common-epsilon construction to published source authority.

## PASS classification

If P0-P7 and all controls pass:

`ITER083F_SM_COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION_EXACT_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Interpretation ceiling

A PASS rules out only the simplest new construction obtained by holding the existing one-wedge spectral epsilon finite and common across the ten wedges. It does not rule out group-normal regularization, analytic regularization of scaling exponents, several-complex-variable boundary values, Epstein-Glaser/BPHZ-type subtraction with a source normalization, microlocal multiplication prescriptions, composition/gluing laws, or other joint conditions acting on `F_8`.

No generic-spin completeness, all-strata global patching, regulator independence, causal-vertex nonexistence/divergence theorem, multivertex E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG result follows.
