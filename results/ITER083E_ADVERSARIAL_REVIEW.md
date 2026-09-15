# Iter083E-SM adversarial review — Ruhl/Toller one-wedge uniqueness versus joint K5 extension

Date: 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NONIMPLICATION_RESULT.md`, commit `90f307f4e4a8dc99945bed4fdd84b632442d8d0d`.

Prospective preregistration: `6aedbc1075f1ca9d2dd71e22a21172f74e914322`.

Public-source lock: `fadc43d4107b687352520afc98952c5a22dac6cb`; machine-readable mirror `94df21f665e4b038b3919b8d444a397764b5ef17`.

Theorem derivation: `577759d30131e99e26092889cde0b893dab606db`.

Production run: `34911549126`, terminal success.

Production job: `104199927491`, terminal success.

Artifact: `10374825487`, digest `sha256:9e33393b72e166dcb92b49a7b524acf2fca33074ca1897d96a6e5de9e67bdcb0`.

Production JSON SHA256: `3f3c3dca902ff6fabdcf2dff8d8f447ac14677ab13ea6b4ff9dc06a1a7087ead`.

## SOURCE_UNIQUENESS_SCOPE_CHECK

The companion paper's uniqueness theorem is genuinely one-wedge. Its trial objects are `u_+(rho,beta),u_-(rho,beta)` meromorphic in one complex `rho` variable. The analytic hypotheses are one-rho-plane asymptotic decay, matching, finite simple poles and the one-wedge sum rule. The Feynman projector integrates the single variable `tilde rho`.

No common-collision normal coordinate appears in that theorem. Identifying the K5 transverse extension variables with `rho` would conflate representation spectral data with group-space collision geometry and is rejected.

## SOURCE_ORDER_CHECK

The causal paper defines an elementary Toller matrix first:

`T^(+/-)(g) = lim_(epsilon->0+) integral d tilde-rho (...) D^(tilde-rho)(g)`.

Only after this limit-defined elementary object is introduced does the fixed-causal vertex formula multiply ten Toller matrices and integrate the remaining four group variables.

Therefore the published formula has the order

`one-wedge epsilon limit -> elementary T -> ten-factor product -> K5 group integration`.

There is no outer `lim_(epsilon->0+)` surrounding the ten-factor product and group integral in the source vertex definition.

### Common-epsilon loophole

A possible objection is that the same symbol `epsilon` occurs in every Toller formula, so perhaps the source secretly intends one common epsilon to be held finite across all ten wedges, with the product/group integral formed first and only then a correlated epsilon limit taken.

That is **not** the displayed source definition. Eq. (3) defines each `T` by an already-taken one-wedge limit; Eq. (4) is written in terms of those `T` matrices. Reversing these operations would define a new correlated K5 regulator prescription. Such a prescription might be scientifically interesting and is explicitly left open, but it is not implied by the published one-wedge formula.

Hence the current theorem correctly treats a common ten-wedge epsilon limit as a falsifier/new selector candidate rather than as existing source authority.

## SUPPORTED_COUNTERDEFORMATION_CHECK

Iter083B proves that the restriction map from frozen same-scaling-degree joint extensions to the off-collision K5 distribution has a 377-dimensional translation kernel `F_8`.

For every nonzero `a in F_8`,

`U' = U+a`

is a distinct joint extension but has the same restriction to `M\N`.

All elementary Toller matrices are defined before this extension choice and are unchanged. Therefore all one-wedge spectral data used by the Ruhl uniqueness theorem are literally identical for `U` and `U'`.

This is stronger than an argument from absence of a source sentence: it is a constructive pair of distinct extensions satisfying exactly the same one-wedge constraints.

## HARMONIC_ANALYSIS_LOOPHOLE_CHECK

The companion notes that Toller matrices are useful in inverse Fourier transforms of distributions on `SL(2,C)`. Could this linear harmonic-analysis role make the ten-factor distribution unique automatically?

No. A linear transform/basis statement for an individual distribution does not supply a multiplication theorem for several singular distributions sharing a singular locus. The K5 ambiguity is not ambiguity in the representation of an elementary Toller function; it is the kernel of extending the already-fixed product from `M\N` across `N`.

The decisive evidence is internal to the frozen problem: `U` and `U+a` have identical off-collision product and hence identical elementary harmonic data, while Iter083B proves both are admissible same-scaling-degree extensions. Any harmonic criterion depending only on the already-fixed elementary Toller factors is therefore constant on `F_8`.

A genuinely joint harmonic multiplication/boundary-value theorem acting on the product would be new information and remains a valid falsifier.

## REPRESENTATION_COMPOSITION_CHECK

The companion explicitly states that Toller matrices do not provide an `SL(2,C)` representation and writes the failure of the usual composition law. Therefore the Wigner-D representation law cannot be imported to propagate one-factor uniqueness to the dependent K5 product arguments.

This fact is used only to block an unsupported proof route; ambiguity existence/dimension comes independently from Iter083B.

## LOCALLY_INTEGRABLE_FACTOR_VERSUS_PRODUCT_CHECK

Another objection is that each elementary Toller matrix is a well-defined polynomially bounded function, so perhaps its product needs no new prescription.

Individual definability does not imply local integrability of the product at the shared K5 collision. The authoritative source-ordered all-`j=1/2` analysis gives a ten-factor leading common-collision scaling degree 20 at codimension 12. That is exactly the regime in which same-scaling-degree extension freedom through normal order 8 exists.

Thus there is no contradiction between unique elementary factors and a nonunique distributional extension of their joint singular product.

## ADDITIVE_AND_CAUSAL_ESCAPE_CHECK

The companion's surviving explicit inter-branch identity is `T+ + T-=D`. Iter083C proves the complete additive hierarchy has an exact top-Boolean supported nullmode for every `a in F_8`.

Iter083D proves the source-defined unit causal orientation sums retain the exact 377-dimensional ambiguity.

Therefore adding the two obvious source consistency structures to one-wedge analytic uniqueness still does not distinguish the joint extensions.

## POSSIBLE_MULTIVARIABLE_SELECTOR_CHECK

The result correctly leaves open conditions that depend on the joint extension itself, including:

- taking a finite **common** epsilon/regulator across all ten wedges and proving a unique distributional limit after product/integration;
- a several-complex-variable boundary-value/edge-of-the-wedge theorem for the correlated K5 object;
- a rigorous multiplication theorem with extra microlocal hypotheses;
- composition/gluing normalization;
- differential, positivity or RG constraints acting nontrivially on `F_8`.

If primary authority supplies one of these, it must be tested directly against the 377-dimensional supported kernel. Iter083E does not prejudge the answer.

## COUNTEREXAMPLE_ATTEMPTS

1. **Use the same epsilon symbol as a common K5 regulator.** Rejected as a reading of the published formula: the epsilon limit is inside the definition of each elementary T before the vertex product. A reversed common-limit order is a new prescription.
2. **One-wedge uniqueness automatically implies product uniqueness.** Rejected by the explicit `U` versus `U+a` pair with identical elementary data.
3. **Inverse Fourier transform uniqueness fixes the product.** Rejected: linear harmonic representation does not define singular multiplication/extension; the supported kernel is invisible to elementary off-collision data.
4. **Use the Wigner representation composition law.** Rejected by the source's explicit Toller non-representation equation.
5. **Use `T+ + T-=D`.** Rejected by Iter083C's all-partial-sums nullmode.
6. **Use the causal orientation sum.** Rejected by Iter083D's exact 377-dimensional persistence theorem.
7. **Unique elementary functions imply local integrability of their tenfold product.** Rejected by the frozen `sd_N=20 > codim N=12` result and Iter083B extension theorem.
8. **Conclude no joint analytic selector can ever exist.** Rejected as overclaim; correlated multivariable prescriptions remain open.

## VERDICT

`CONFIRMED_SCOPED`

Authoritative classification:

`ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_ANALYTIC_UNIQUENESS_DOES_NOT_LIFT_TO_JOINT_K5_EXTENSION_SELECTOR_SCOPED`.

The current source-defined one-wedge analytic uniqueness/Feynman prescription has zero discriminating power on the 377-dimensional translation kernel of the frozen joint K5 extension problem. Known Toller additivity and unit causal summation do not restore that power.

## UPDATED LOCAL FRONT

The obvious selector candidates now excluded in the frozen sector are:

- scalar/atlas/Cech consistency;
- ordinary conormal wavefront admissibility;
- Toller additive identities;
- finite source causal summation;
- one-wedge Ruhl/Toller analytic uniqueness and its already-taken Feynman `i epsilon` prescription.

The highest-value local question is now whether a **genuinely correlated joint K5 prescription** exists: common regulator/limit, several-variable analytic boundary value, multiplication theorem, composition/gluing normalization, or another condition acting nontrivially on `F_8`.

## INTERPRETATION CEILING

No distributional nonexistence theorem, no generic-spin completeness, no all-strata global patching, no regulator dependence/independence, no multivertex E3/E4/E6 closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
