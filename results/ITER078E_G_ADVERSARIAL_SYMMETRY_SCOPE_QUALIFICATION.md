# Iter078E/G adversarial qualification — the 32-dimensional saturation theorem is for the labelled boundary dual before automorphism reduction

**Date:** 2026-09-14

## Reviewed results

- `results/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE_RESULT.md`, commit `f9a7e264a0747e3fbb809a2130b6729361b6ec31`;
- `results/ITER078G_RG_INTEGRATED_VERTEX_AMBIGUITY_SATURATION_RESULT.md`, commit `e7ac634faf24da7f005d38d685f15a0bb39c02fa`.

## Exact core retained

For the frozen **labelled** all-`j=1/2` boundary graph and one fixed labelled causal sector,

`H_B = tensor_a Inv[(1/2)^tensor4]`

has complex dimension 32, and componentwise finite-scaling-degree extension permits order-zero supported shifts

`Delta A_ell = ell(Psi) delta_N`

for `ell in H_B^*` before any additional boundary-automorphism selector is imposed. Integration of the normalized supported delta gives a nonzero common factor times `ell`, so the labelled integrated ambiguity fills the labelled dual space.

This is a valid affine-space statement in the frozen labelled coordinates.

## Qualification

A physical unlabelled or permutation-covariant 4-simplex amplitude may satisfy additional graph-automorphism / orientation / recoupling covariance conditions. In an equal-spin sector the stabilizer of a causal sign pattern can be nontrivial. Imposing such conditions can restrict `ell` to a proper symmetry-compatible subspace of `H_B^*`.

The exact dimension of that symmetry-compatible subspace has **not** been computed because it requires the correct action of 4-simplex vertex permutations on the chosen four-valent recoupling basis, including leg-order/orientation phases. It must not be guessed from simple permutation of the five `k_a` labels.

Therefore the number `32` must not be advertised as the proven number of **physical independent couplings** after all graph symmetries.

## What remains unaffected

This qualification does not restore uniqueness:

- Iter077M/N already exhibit an explicit source-structured compact spin-network supported direction that survives the integrated vertex;
- Iter078I/K/L show that EPRL recovery, large-spin asymptotics and the published source formulas do not select the finite-spin extension;
- a future permutation-symmetry reduction can lower the ambiguity dimension but must still be combined with refinement/RG or another selector to determine the remaining coefficients.

## Forward rule

Use the full 32-dimensional space in Iter078F/H/J/M only as a **labelled fixed-spin control theory space**. Any claim about the physical reduced coupling count requires a separate prospectively frozen automorphism/recoupling representation audit.

Verdict: `QUALIFIED_SCOPE`, not invalidation.