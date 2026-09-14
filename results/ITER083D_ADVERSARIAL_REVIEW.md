# Iter083D-SM adversarial review — repaired causal-sum persistence of exact 377-dimensional ambiguity

Date: 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY_RESULT.md`, commit `6632b65df27cf47d6b7445544ccc534e6902a74e`.

Prospective preregistration: `7656ae687ce16ad05bacfc34349c8206b583237e`.

Theorem derivation: `dff3407d3ffa86f5aa5c3b4e7550a15798d6ed7c`.

Authoritative production run: `34911072018`, terminal success.

Authoritative job: `104198440273`, terminal success.

Artifact: `10374652013`, digest `sha256:338697c0e56a857c407685befd5023706a3080f1629fccdd27feb5dd180af91b`.

Production JSON SHA256: `a95e47e8833142a49cc8d3b4455f272cfca632fb21d8da12db6dac2599b403b1`.

The earlier run `34910997659` was `INVALID_IMPLEMENTATION`, not a scientific failure: its only false predicate was a literal source-text lock for a phrase absent from Iter081H, while the actual frozen `r^-20`, combinatorial and dimensional checks passed. Commit `10e9fdd9ba4aeb2cda800af32c74eeebd137e48e` repairs only that text lock to the exact frozen `q=-20` wording.

## HISTORICAL_ERRATUM_CHECK

Historical Iter081I used the family

`Q(y)^n F(y) delta_N`

and claimed countably infinite-dimensional source-compatible tangential ambiguity after causal summation. That family relied on the pre-correction Iter077Q symmetry model and is not invariant under the exact transitive node-wise compact action on `N`.

Therefore its infinite-dimensional conclusion cannot remain authoritative.

The current result does not silently discard Iter081I. It explicitly preserves the independently valid parts — finite unit-weight causal summation, nonzero summed `r^-20` source behavior, and the observation that off-collision summation is not a supported-extension selector — while replacing the invalid tangential space by Iter083B's exact finite `F_8`.

Historical Iter081I status is correctly

`SUPERSEDED_INVALID_SOURCE_SYMMETRY_MODEL`.

## SOURCE_SUM_CHECK

The primary Bianchi--Chen--Gamonal paper defines five node orientation labels `sigma_a=+-1` and fixed-sector wedge signs `kappa_ab=sigma_a sigma_b`. It explicitly discusses the unweighted sum `sum_(sigma_a=+-1) A_v^(sigma_a sigma_b)`.

There are 32 node-sign assignments but global reversal leaves every wedge sign unchanged, hence exactly 16 distinct wedge-sign patterns, each with multiplicity two in the 32-label expression.

Beltran eta=+1, as frozen by Iter081H, sums the same 16 inequivalent factorized patterns once each with unit coefficient.

Thus for wedge-sign-defined amplitudes

`S_BCG=2 S_Beltran`.

Production independently reconstructs all 32 node assignments and obtains exactly 16 patterns with multiplicity two. The factors 16 and 32 are not inserted by hand as a substitute for this enumeration.

## TOP_MODE_CHECK

Iter083C's authoritative deformation is

`Delta_kappa=(product_e kappa_e)a`.

For causal K5 signs,

`product_(a<b) sigma_a sigma_b = product_a sigma_a^4=1`.

Therefore the deformation is exactly sector-independent on the causal subset:

`Delta_kappa=a`.

This is important adversarially. If causal summation introduced an extra requirement of orientation blindness, the surviving top-mode family already satisfies it on all causal sectors; no further quotient is needed.

The two source sums act by nonzero scalar multiplication:

`S_Beltran(Delta)=16a`,

`S_BCG(Delta)=32a`.

Over the complex coefficient space these maps are injective. Hence every independent vector in `F_8` survives.

## LOWER_BOUND_CHECK

Iter083B gives `dim_C F_8=377`. The injective maps above therefore produce 377 linearly independent ambiguity directions after either source-defined unit sum.

This lower bound does not depend on the historical invalid `Q^n` family and does not depend merely on scaling degree.

## UPPER_BOUND_CHECK

The exact claim requires more than persistence of 377 directions.

Iter081H establishes that the Beltran summed off-collision object has a nonzero `16 C_alpha r^-20` leading coefficient for every frozen boundary component. It therefore stays in the same common-collision scaling-degree-20 extension class.

The causal sum changes no support geometry, boundary-dual fiber, node-gauge group, S5 relabeling covariance or Haar/tubular density convention. Iter083B's theorem classifies all same-scaling-degree source-symmetry-compatible supported differences for exactly that frozen local geometry and coefficient representation. Therefore no admissible summed-object extension difference can lie outside `F_8` in the frozen class.

This yields the upper bound 377.

For the BCG sum, `S_BCG=2S_Beltran` on the same fixed-sector Toller family. A nonzero scalar multiple has the same local scaling degree and symmetry class, so the same upper bound applies.

Thus lower and upper bounds agree exactly.

## ADDITIVE_CONSISTENCY_CHECK

The family used here is not merely compatible with the causal sum. Iter083C already proves it is annihilated by every nonempty partial sign-sum map generated from `T+ + T-=D`.

Therefore imposing causal summation together with the full additive Toller/EPRL hierarchy cannot reduce the 377-dimensional surviving space.

This closes a possible loophole in which the causal sum alone preserves ambiguity but an EPRL consistency equation removes it.

## WEIGHTED_SUM_CHECK

The exact theorem is deliberately not generalized to arbitrary weights. For `S_w`, the top-mode image is `(sum w_C)a`; if the total weight is zero, this particular family can cancel.

Neither frozen source object tested here uses such a weighting. Alternating or fitted weights would define a different model/observable and need their own source authority.

The production negative control correctly rejects importing such weights into the unit-sum theorem.

## NORMALIZATION_CHECK

The factor 16 versus 32 is not physical dimension data. It reflects whether global node-sign reversal is quotiented before summation. Both factors are nonzero and therefore give the same surviving 377-dimensional image.

Any overall nonzero normalization of the entire causal sum would likewise preserve the dimension, but no normalization convention is used to manufacture a selector.

## DISTRIBUTIONAL_CHECK

The result concerns extension differences supported exactly on the common-collision submanifold. Finite summation acts linearly on the off-collision distributions but does not assign values to contact/support terms unless a further prescription is supplied.

The corrected finite symmetry theorem prevents arbitrary tangential functions, but it still permits the 377 intrinsic normal/boundary-covariant directions classified by Iter083B. Causal summation neither changes their support nor their normal-order filtration.

## COUNTEREXAMPLE_ATTEMPTS

1. **Global reversal makes only 16 source terms, so the BCG factor cannot be 32.** Rejected: the primary comparison literally sums over all 32 `sigma` assignments; global reversal duplicates wedge amplitudes, giving factor two, not deletion of labels.
2. **Beltran and BCG sums could use different causal wedge sets.** Rejected in the frozen all-j=1/2 source chain: Iter081H identifies Beltran eta=+1 assignments with the same factorized `sigma_a sigma_b` K5 patterns.
3. **Causal summation adds an orientation-blind symmetry that reduces F8.** Rejected for the constructed family: `Delta=a` is already identical on all causal sectors; direct summed-object Iter083B upper-bound classification uses the resulting orientation-free boundary object.
4. **The surviving space might be larger than 377 after summation.** Rejected within the frozen same-scaling-degree symmetry class by Iter083B's complete upper-bound theorem.
5. **The space might be smaller than 377.** Rejected by the explicit injective `a->16a` / `a->32a` top-mode maps.
6. **Toller additivity could remove the surviving causal-sum directions.** Rejected by authoritative Iter083C all-partial-sums nullity.
7. **Historical infinite-dimensionality should be retained in addition to 377.** Rejected: the old tangential family violates the corrected exact source symmetry and is superseded.
8. **Finite causal summation therefore produces a unique physical vertex.** Rejected: exact ambiguity dimension is nonzero and equals 377.
9. **No future selector can exist.** Rejected as overclaim: genuinely non-additive joint prescriptions remain logically open.

## VERDICT

`CONFIRMED_SCOPED`

Authoritative repaired classification:

`ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED`.

The source-defined unit-weight Beltran 16-pattern and Bianchi--Chen--Gamonal 32-label causal sums both retain an exact 377-dimensional local common-collision same-scaling-degree ambiguity in the frozen all-`j=1/2` boundary-linear compact-gauge/S5-covariant sector.

## UPDATED LOCAL CHAIN

`fixed causal Toller sectors` -> `common-collision sd=20` -> `Iter083B exact F8 dimension 377` -> `Iter083C top Boolean mode equals +a on all causal patterns and is invisible to all Toller additive marginals` -> `unit causal sum sends a to 16a or 32a` -> `injective 377D persistence` -> `Iter081I infinite tangential claim superseded` -> **`CAUSAL SUMMATION DOES NOT SELECT THE K5 EXTENSION`** -> `genuinely non-additive joint selector still missing`.

## INTERPRETATION CEILING

No distributional nonexistence theorem, no generic-spin completeness, no all-strata global extension, no regulator dependence/independence, no causal multivertex E3/E4/E6 closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
