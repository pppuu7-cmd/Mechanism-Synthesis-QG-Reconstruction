# Iter083C-SM adversarial review — Toller-additivity joint-K5 selector nullmode

Date: 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER083C_SM_TOLLER_ADDITIVITY_SELECTOR_NULLMODE_RESULT.md`, commit `4f7117408d10ef67279324cfffddb360fa256d51`.

Prospective preregistration: `e7938c383f445a1770c9473c72f65490cc8dd41b`.

Production run: `34910439308`, terminal `success`.

Production job: `104196500834`, terminal `success`.

Artifact: `10374621113`, digest `sha256:021a118ed6b77dbe679cb544c5c71db859872a86c43165bd878bbe774045c0b8`.

Production JSON SHA256: `3130a340c407c5d0bd7ef23007f3871bc8b4a2df0360a18aafd1cecbd4c3c901`.

## SOURCE_OBJECT_CHECK

The source identity tested is exact and upstream: `T^(+)+T^(-)=D` wedge by wedge. The causal-vertex construction contains ten Toller factors on K5. The unconstrained expansion of all ten sums ranges over `2^10` independent wedge-sign assignments, whereas causal sign patterns are restricted to `kappa_ab=sigma_a sigma_b`.

The theorem does not identify termwise spinor contact distributions with the source object. It acts at the already source-ordered ten-Toller product extension layer.

## SCALING_CHECK

Iter077I gives the crucial same-class premise: at all-`j=1/2`, the two Toller branches have identical leading `beta^-2` angular matrix up to an overall minus sign. Therefore an arbitrary independent ten-edge sign assignment changes the nonzero leading K5 contraction only by the product of ten signs and preserves radial degree `r^-20`.

Thus every sector used in the Boolean cube lies in the same frozen `sd_N=20` local extension problem. The nullmode is not manufactured by mixing extensions of different scaling degree.

## BOOLEAN_CHECK

The exact character

`chi_top(kappa)=product_e kappa_e`

is in the kernel of every nonempty partial sign-sum map. For a summed subset `S`, the marginal contains a factor

`product_(e in S) sum_(kappa_e=+-1) kappa_e = 0`.

This analytic proof is complete. Production independently exhausts the finite Boolean problem and reports:

- 1023 nonempty sign subsets;
- 58,025 conditional marginal sums;
- zero failures;
- full 1024-sector top-character sum equal to zero.

The controls correctly show that this is not generic behavior of arbitrary sign tables: the constant mode fails, every proper-subset Boolean character is exposed by a marginal over an edge outside its support, and a deliberately damaged table is rejected.

## CAUSAL_CHECK

For causal signs `kappa_ab=sigma_a sigma_b`,

`product_(a<b) kappa_ab = product_a sigma_a^4 = +1`

because K5 is 4-regular.

Global reversal of all five `sigma_a` is redundant, so the 32 node-sign assignments yield exactly 16 distinct causal wedge-sign patterns. Production enumerates exactly 16, and the top character is `+1` on all of them.

The all-minus ten-edge assignment is correctly absent from the causal image.

Therefore every causal sector receives the same supported shift `+a`; this is not a cancellation argument based on a special causal pattern.

## S5_CHECK

A K5 vertex permutation merely permutes the ten factors in `chi_top`, so the top character is S5 invariant. Relabeling a factorized causal assignment produces another factorized causal assignment. Hence the nullmode is compatible with upstream vertex-relabeling covariance whenever its coefficient ambiguity `a` is.

## DISTRIBUTIONAL_CHECK

The deformation changes only a distribution supported on the common-collision submanifold `N`. It therefore leaves all exact sign-sector Toller products unchanged off `N`, preserves support and same scaling degree, and does not modify any one-wedge Feynman prescription.

Iter077M already provides a nonzero source-compatible supported ambiguity. Therefore the qualitative no-go does not depend on the pending Iter083A boundary-covariant dimension calculation.

## STRONGEST_ADDITIVITY_CHECK

The result is genuinely stronger than a kernel of the total EPRL sum. Since the deformation vanishes under the sign sum over **any nonempty subset**, it remains invisible even if every mixed product with arbitrary combinations of `D`, `T+` and `T-` factors is imposed as an additive consistency equation.

Thus no additional identity obtainable solely by repeated linear use of `T+ + T- = D` can constrain the top Boolean coefficient.

This does not address a non-additive correlated K5 limiting prescription.

## REGULATOR_CHECK

No common regulator is inferred. The source one-wedge Feynman prescription remains one-wedge authority only. A genuinely joint multivariable boundary value/common regulator could correlate the 10 signs in a way not expressible as additive marginals and remains outside this theorem.

## DEPENDENCY_CHECK

The production artifact deliberately reports Iter083A as not yet authoritative and does not insert the exploratory number 377. This is correct dependency hygiene.

If later authoritative Iter083A/B prove a finite-dimensional frozen coefficient space `A`, linearity immediately embeds all of `A` into the top Boolean nullmode. That future numerical promotion requires the upstream result; it is not part of the present unconditional verdict.

## COUNTEREXAMPLE_ATTEMPTS

1. **Use the full EPRL identity to fix causal extensions.** Rejected: the top mode sums to zero over all 1024 independent signs while equaling `+a` on all causal patterns.
2. **Use one-edge Toller additivity.** Rejected: every one-edge marginal vanishes exactly.
3. **Use several `D` factors simultaneously.** Rejected: every nonempty multi-edge marginal vanishes exactly.
4. **Break the construction by S5 relabeling.** Rejected: the complete edge product is permutation invariant.
5. **Exclude the mode by scaling degree.** Rejected in the frozen sector: branch changes only flip the nonzero leading sign.
6. **Claim the all-minus wedge assignment is a causal sector and changes the parity argument.** Rejected by exact enumeration and by the factorized causal condition.
7. **Interpret the nullmode as a modification of one-wedge Toller functions.** Rejected: it is supported only at the final joint common-collision extension layer.
8. **Promote additivity failure to failure of every conceivable selector.** Rejected: non-additive common-regulator, analytic, differential, composition, positivity and RG conditions remain logically open.

## VERDICT

`CONFIRMED_SCOPED`

The authoritative scoped classification is

`ITER083C_SM_TOLLER_ADDITIVITY_HAS_EXACT_JOINT_K5_TOP_BOOLEAN_SELECTOR_NULLMODE`.

## UPDATED LOCAL CHAIN

`source one-wedge Toller branches` -> `exact T+ + T- = D additivity` -> `source-ordered K5 products` -> `common-collision same-scaling-degree supported ambiguity exists` -> `top Boolean sector Delta_kappa=(product_e kappa_e)a` -> `all 1023 nonempty additive marginal families annihilate Delta` -> `all 16 causal patterns retain +a` -> **`TOLLER ADDITIVITY CANNOT SELECT JOINT-K5 EXTENSION`** -> `genuinely non-additive joint selector still missing`.

## INTERPRETATION CEILING

No causal-vertex divergence/nonexistence theorem, no regulator-independence theorem, no generic-spin completeness, no all-strata global extension, no multivertex closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
