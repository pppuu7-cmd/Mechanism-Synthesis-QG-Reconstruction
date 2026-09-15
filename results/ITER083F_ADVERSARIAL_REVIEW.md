# Iter083F-SM adversarial review — finite common spectral epsilon versus K5 collision

Date: 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_RESULT.md`, commit `950611372f7b5898d5822f3dafd5f875e6007183`.

Prospective preregistration: `18fbeca191aa05fe09e3e38ed60abec53e09a8c9`.

Public-source lock: `d69eb1b5c187be257c507cdc3527ec4f9e824c97`; machine-readable lock `66c9a80ca6cecc59131deccca5d6e37a7ef57011`.

Theorem derivation: `464e54abfb63aa123ff9a6614fc033d98274b733`.

Production run: `34912148095`, terminal success.

Production job: `104201783021`, terminal success.

Artifact: `10374589062`, digest `sha256:7f64b3a817ea89cdef21bf75ef001f8afc1699c77fdcb661164e889f0cca45e0`.

Production JSON SHA256: `9242bfeea498e8634bec469ca52907eb1852ec60d9e56c200af4dee2d6e55fa6`.

## FINITE_EPSILON_CONTOUR_CHECK

The most important source-level issue is whether the residue formula is valid only after taking `epsilon->0`, in which case it could not establish finite-epsilon collision scaling.

The contour argument is stronger. The Toller kernel `P_jl` cancels the finite set of Toller poles before the epsilon limit. For the plus branch, at fixed positive admissible epsilon the remaining Feynman pole is at `rho+i epsilon` and lies inside the upper contour; the opposite Toller branch closes in the lower half-plane and contains no such pole. The same statement holds with signs reversed for the minus functional.

Therefore the fixed-epsilon residue identity is an exact intermediate step of the source contour proof, not an exchange of the epsilon limit with another limit:

`I_epsilon^+[d]=P(rho+i epsilon;rho)t^+(rho+i epsilon,beta)`,

`I_epsilon^-[d]=P(rho-i epsilon;rho)t^-(rho-i epsilon,beta)`.

The no-go can thus analyze `beta->0` at fixed epsilon without taking epsilon to zero at all.

## KERNEL_CANCELLATION_CHECK

For `j=l=1/2`,

`P=(rho_tilde^2+1/4)/(rho^2+1/4)`.

The Table-II Toller branches contain the exact shifted denominator `rho_tilde^2+1/4`. It cancels algebraically. Production verifies this with exact Gaussian-rational polynomial arithmetic.

This cancellation matters physically: if the kernel were dropped, one would incorrectly retain an epsilon-dependent spectral denominator and might misdiagnose that as collision regularization. The negative control explicitly rejects that surrogate.

## FOUR_BRANCH_CHECK

All four combinations of branch sign and `m=+-1/2` were checked. The fixed-epsilon factors are combinations of

`exp(-epsilon beta)`, `cosh(beta)`, `sinh(beta)`

multiplying the same `1/sinh(beta)^2` denominator.

The constant numerator terms are exactly `+-1`, producing the frozen leading signs

`(-,+,+,-)`

in the preregistered branch ordering. No leading coefficient depends on epsilon.

At `rho=gamma/2` the exact magnitude is `2/(1+gamma^2)`, matching Iter077I.

## ORDER_OF_LIMITS_CHECK

Could a correlated limit `epsilon->0`, `beta->0` evade the fixed-epsilon conclusion?

No for this candidate. After exact kernel cancellation every epsilon-dependent correction near the collision is built from

`exp(-epsilon beta)=1-epsilon beta+O((epsilon beta)^2)`

and terms proportional to `epsilon sinh(beta)=epsilon beta+O(epsilon beta^3)`.

For any path with both `epsilon->0+` and `beta->0+`, necessarily

`epsilon beta ->0`.

Hence the leading `beta^-2` coefficient remains the same along every ordinary joint regulator-removal path. There is no `epsilon/beta`, `beta/epsilon`, or `exp(-epsilon/beta)` structure in the exact finite-epsilon formula.

A path requiring `epsilon` to grow like `1/beta` would not be an `epsilon->0` regulator-removal path and is a different construction.

## FULL_MATRIX_CHECK

Restoring the SU(2) Cartan factors cannot improve the radial order: they are finite angular matrices. The reduced leading matrices remain

plus: `diag(+1,-1)` in ascending `m=(-1/2,+1/2)`,

minus: `diag(-1,+1)`.

This is exactly the branch-sign relation used by Iter077I. Therefore the frozen nonzero ten-wedge angular contraction remains nonzero at finite epsilon.

## TEN_WEDGE_CHECK

Each of the ten wedges supplies order `r^-2`; their leading product is still `r^-20`. The product of all finite-epsilon damping factors is

`exp[-epsilon sum_e beta_e] = 1+O(r)`

for fixed epsilon on the common radial path, and tends to one as `(epsilon,r)->(0,0)` as well.

Thus the finite spectral parameter leaves the common-collision scaling degree 20 unchanged.

## LOCAL_INTEGRABILITY_CHECK

The collision normal codimension is 12. The radial measure is `r^11 dr`, so the fixed-epsilon leading radial integral behaves as

`integral r^-9 dr`.

It diverges at zero as an ordinary locally integrable function.

Therefore the common finite spectral epsilon does not turn the ten-factor object into a canonically defined product distribution on the collision neighborhood. One still needs an extension/renormalized multiplication prescription even before trying to remove epsilon.

## REGULATOR_DEFINITION_CHECK

A possible semantic objection is that a regulator need not make the integrand an ordinary function; perhaps it could define a distribution for every epsilon by some other mechanism.

That possibility is not ruled out, but then the **spectral epsilon alone** is not doing the regulating. Any definition of the fixed-epsilon non-integrable product would require an additional distributional multiplication/extension prescription, precisely the missing joint information under study.

Thus the scoped classification “not a K5 collision regulator” means: holding the existing one-wedge spectral pole shift finite does not by itself remove the common-collision extension problem.

## SOURCE_AUTHORITY_CHECK

The common finite-epsilon ten-wedge construction is not promoted to the published causal-vertex definition. The source takes the one-wedge epsilon limit first. Iter083F deliberately tests a new reversed-order candidate and finds that it fails at the first required property, local collision regularization.

## COUNTEREXAMPLE_ATTEMPTS

1. **Finite epsilon bounds the spectral denominator, so the K5 product is regulated.** Rejected: exact kernel cancellation leaves the same `beta^-2` collision singularity.
2. **Use `exp(-epsilon beta)` as UV damping.** Rejected: it tends to one, not zero, at `beta=0`.
3. **Take epsilon and beta to zero jointly.** Rejected for the simple candidate: all epsilon dependence is regular in the product `epsilon beta`, which tends to zero.
4. **Interpret epsilon as shifting beta.** Rejected: source epsilon shifts spectral `rho`, not group-normal rapidity.
5. **Use the Barrett-Crane j=0 example only.** Rejected: the exact proof and CI use the physical frozen j=1/2 Table-II formulas.
6. **Maybe SU(2) angular factors cancel the leading ten-wedge term at finite epsilon.** Rejected: the finite-epsilon leading reduced matrix is exactly the same as at epsilon zero; Iter077I's frozen angular witness remains nonzero.
7. **A non-locally-integrable product has no distributional extension.** Rejected as overclaim: renormalized extensions exist but are nonunique without a selector.
8. **Therefore every joint regulator fails.** Rejected: only the reuse of the existing spectral epsilon has been excluded.

## VERDICT

`CONFIRMED_SCOPED`

Authoritative classification:

`ITER083F_SM_COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION_EXACT_SCOPED`.

The simplest genuinely reordered candidate proposed after Iter083E fails: a common finite **spectral** epsilon retains the exact K5 common-collision scaling degree 20 and does not eliminate the 377-dimensional extension problem.

## UPDATED LOCAL FRONT

The next useful selector/regulator candidate must actually constrain the **joint collision variables or supported kernel**, for example:

- analytic regularization of collision-normal scaling powers;
- several-complex-variable boundary values tied to the ten dependent K5 arguments;
- a microlocal multiplication/extension theorem plus normalization;
- a composition/gluing law;
- another condition with a nontrivial map on `F_8`.

Simply reusing the one-wedge spectral Feynman epsilon, even with a common value and reversed product/limit order, is now closed.

## INTERPRETATION CEILING

No causal-vertex distributional nonexistence theorem, no generic-spin completeness, no all-strata global patching, no regulator dependence/independence, no multivertex E3/E4/E6 closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
