# Iter077L-SM source/theorem derivation — transverse K5 common-collision extension

**Date:** 2026-09-14

## Frozen external theorem authority

This derivation follows the prospective contract in
`prereg/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM.md`.

Primary mathematical authority:

- R. Brunetti, K. Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000) 623-661, arXiv:math-ph/9903028. Section 5 treats extension to a point by scaling degree; Section 6 generalizes to smooth submanifolds. Theorem 6.9 states, in particular, that for a distribution defined off a smooth submanifold `N`, scaling degree below `codim(N)` gives a unique same-scaling-degree extension, while finite scaling degree at or above `codim(N)` admits same-scaling-degree extensions but requires additional data on a complementary finite-jet space.
- N. V. Dang, *Extension of distributions, scalings and renormalization of QFT on Riemannian manifolds*, arXiv:1411.3670, and the companion microlocal treatment arXiv:1412.2808, for the general extension-along-submanifolds / moderate-growth framework.

The theorem is used only as an extension/uniqueness statement. No QFT counterterm interpretation is imported as a physical CRQN mechanism.

## Actual CRQN singular submanifold

After gauge fixing node 0, the fixed-causal K5 group integrand is locally a function/distribution on

`M = SL(2,C)^4`.

A Lorentz element has Cartan boost parameter `beta=0` iff it lies in the compact subgroup `SU(2)`. Therefore simultaneous vanishing of all ten relative boost parameters in a neighbourhood of the common compact collision is equivalent to

`g_1,...,g_4 in SU(2)`

after the root is gauge fixed in `SU(2)`.

Thus the common-collision locus is locally

`N = SU(2)^4 subset SL(2,C)^4`.

Dimensions:

- `dim_R SL(2,C)^4 = 4*6 = 24`;
- `dim_R SU(2)^4 = 4*3 = 12`;
- `codim_R N = 12`.

This is a smooth embedded submanifold. The twelve compact directions are tangent to `N`; the twelve boost directions form the normal bundle relevant to transverse scaling.

This independently justifies the transverse dimension `d=12` already used in authoritative Iter077I-SM.

## Local patch excluding other collision surfaces

Iter077I froze an exact normal collision ray with four non-root boost vectors and all ten relative differences nonzero. The exact full boundary leading contraction is nonzero there for every one of the 32 all-`j=1/2` boundary components.

Choose a sufficiently small conic angular neighbourhood of that normal direction. Continuity gives:

1. every relative boost-direction difference remains nonzero on the angular closure;
2. for `r>0` sufficiently small no individual wedge has `beta_ab=0` in that punctured conic patch;
3. the only singular set reached as `r -> 0` inside the patch is the smooth common submanifold `N`;
4. the leading contracted angular coefficient remains nonzero for the chosen boundary component on a smaller open angular patch.

Hence the submanifold extension theorem can be applied locally without conflating the full collision with additional partial-edge collision strata.

## Exact transverse scaling degree

Authoritative Iter077I-SM established in the source ordering

`one-wedge Toller construction -> ten-wedge K5 product -> boundary contraction -> group integration`

that each `j=1/2` wedge contributes leading transverse boost degree `-2` and the complete leading contraction is nonzero on an open angular patch for each of the 32 basis components.

Therefore, on such a localized patch, one component has

`u(r,omega,y) = r^(-20) a(omega,y) + O(r^(-19))`,

where `y` denotes compact/tangential coordinates and `a` is smooth with `a(omega_0,y_0) != 0` at the frozen witness.

Under normal scaling `r -> lambda r`, the nonzero homogeneous leading term proves

`sd_N(u) = 20`.

The smooth Haar-density factor and smooth nonzero normalization/intertwiner factors do not increase or lower this local scaling degree; multiplication by a smooth factor nonzero at the witness preserves it.

Thus

`sd_N(u) = 20`,

`codim(N) = 12`,

and the transverse superficial degree is

`omega = 20 - 12 = 8`.

## Application of the extension theorem

Brunetti-Fredenhagen Theorem 6.9 is therefore in its second regime:

`codim(N) <= sd_N(u) < infinity`.

Consequences in the theorem's scope:

1. same-scaling-degree extensions across `N` exist locally;
2. scaling degree alone does not select one uniquely;
3. the missing extension data live in the finite normal jet through degree `8`;
4. equivalently, differences between admissible local extensions are distributions supported on `N` with normal derivative order at most `8` (with coefficients/distributional data along `N`, subject to any additional wavefront/symmetry requirements imposed separately).

This is not a statement that every such local term is physically admissible. Additional covariance, gluing, Ward-like identities, normalization conditions, analyticity, or a source-prescribed regulator may reduce the freedom. Iter077K-SM, however, established that the frozen published causal-Toller sources do not themselves supply the missing joint K5 prescription.

## Frozen controls

### Positive control below threshold

Replacing the radial degree by `-11` in the same twelve normal variables gives `sd=11<12`, which is the unique-extension regime of the theorem.

### Threshold control

Degree `-12` gives `sd=12=codim(N)`. A delta distribution supported on `N` has the same transverse scaling degree and therefore supplies the expected first nonuniqueness channel.

### Invalid ambient-dimension control

Using the full ambient dimension `24` as the uniqueness threshold would incorrectly count the twelve compact directions tangent to the singular locus as regularizing directions. Theorem 6.9 uses `codim(N)`, so the correct threshold here is `12`.

## Scientific consequence

Standard distribution-extension theory answers a key part of the Iter077K object-definition blocker:

- the local singular source-ordered K5 object is not blocked because extension is mathematically impossible;
- finite-scaling-degree theory supplies local extensions;
- but it does **not** make the published CRQN vertex unique because an order-8 finite normal-jet ambiguity remains before additional physical/source conditions are imposed.

No conclusion about a unique global vertex, regulator independence, gluing/composition, generic spins, causal-sector sums, or G3 follows from this theorem alone.