# Iter078E-RG result — the minimal integrated extension theory space already contains the full 32-dimensional boundary dual

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE.md`, commit `1a5cbc1704f3e9b28539d46f974f4aa815924d78`.
- Source/theorem derivation: `sources/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE_DERIVATION.md`, commit `d6e0b31d9bc32b4a04eb060d4f314de7a7780e92`.
- Upstream extension authority: Iter077L-SM.
- Boundary-space authority: complete all-`j=1/2` 32-component basis used in Iter077I/J/N.

## Classification

`ITER078E_RG_INTEGRATED_EXTENSION_THEORY_SPACE_HAS_AT_LEAST_FULL32_ORDERZERO_BOUNDARY_DUAL_DIRECTIONS_EXACT_THEOREM_SCOPED`

Scientific verdict: **PASS** for the preregistered lower-bound statement.

## Exact findings

The controlling boundary Hilbert space has exact dimension

`dim_C H_B = 2^5 = 32`.

After contraction with each genuine gauge-invariant boundary basis state, the source-ordered vertex is a scalar distribution off the smooth collision submanifold `N=SU(2)^4`. Iter077L's finite-scaling-degree extension theorem applies componentwise.

For any boundary-dual functional `ell in H_B^*`,

`Delta A_ell(Psi)=ell(Psi) delta_N`

is an admissible order-zero supported extension difference with transverse scaling degree 12, below the source object's maximal degree 20. Global source gauge invariance does not identify distinct `ell`, because the boundary states are already invariant and the pre-gauge collision set is invariant under common left `SL(2,C)` multiplication.

Integration over the supported set gives a common nonzero normalization times `ell(Psi)`, so the order-zero ambiguity survives as an injective copy of the full boundary dual.

Therefore

`dim_C ambiguity_image >= 32`

already in the all-`j=1/2` finite-spin sector.

## New scientific fact

The one-parameter witness family `A_0+cL` used in Iter077M-N and as a control in Iter078C-D samples only one direction of a much larger known extension space. It cannot be promoted to the CRQN RG theory space without a prospective reduction theorem.

This materially changes the next RG obligation: a source-faithful refinement map must either transport at least the full 32-dimensional order-zero ambiguity image in the controlling minimal sector or prove a physical/symmetry projection that reduces it before any beta function is computed.

## Scope / adversarial ceiling

- `32` is a **lower bound**, not the full ambiguity dimension.
- Normal derivatives through order 8 and nonconstant/distributional tangential coefficient data along `N` may enlarge the space substantially.
- The result does not claim 32 generic-spin couplings or a universal finite-dimensional truncation.
- It does not supply a unique extension, RG fixed point, regulator independence, G3, continuum or complete-QG result.

## Exact next admissible step

Do not search for a one-scalar `c` fixed point. First define a causal 1-to-5 refinement prescription and a prospective projection/transport law for the **full 32-dimensional order-zero boundary-dual sector**. Any lower-dimensional truncation must state and test the symmetry/dynamical reduction criterion before the RG calculation, not after observing the flow.