# Iter078E-RG derivation — full 32-dimensional order-zero supported ambiguity lower bound

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE.md`, commit `1a5cbc1704f3e9b28539d46f974f4aa815924d78`.

## Finite-dimensional boundary object

In the controlling all-`j=1/2` sector each four-valent node has the two invariant recoupling channels `k=0,1`. The five-node boundary Hilbert space is therefore

`H_B = tensor_(a=0)^4 Inv[(1/2)^tensor4]`,

with

`dim_C H_B = 2^5 = 32`.

This is the same complete boundary basis used in Iter077I/J/N. It is an actual SU(2)-gauge-invariant spin-network boundary space, not a scalar graph surrogate.

Choose the frozen recoupling basis `|alpha>`, `alpha=1,...,32`. For the source-ordered fixed-causal vertex off the common-collision submanifold `N`, contraction with `|alpha>` gives a scalar distribution `u_alpha` on the punctured group-variable neighbourhood.

## Componentwise extension theorem

Iter077L establishes finite transverse scaling degree 20 at the smooth codimension-12 collision submanifold. The Brunetti-Fredenhagen extension theorem is linear and applies componentwise to a finite collection of scalar distributions. Thus choose one same-scaling-degree extension `bar u_alpha` for each of the 32 components.

The transverse delta distribution `delta_N` has scaling degree 12. Therefore for arbitrary complex constants `c_alpha`,

`bar u_alpha^(c) = bar u_alpha + c_alpha delta_N`

is still an extension with maximal transverse scaling degree at most 20. Since the 32 boundary components are linearly independent, the map

`c in C^32 -> (c_alpha delta_N)_alpha`

is injective before any extra selector is imposed.

Higher normal derivatives allowed by Iter077L are not needed for this lower bound.

## Boundary/gauge covariance

A general frozen boundary state is

`Psi = sum_alpha psi_alpha |alpha>`.

The supported order-zero ambiguity can be written basis-independently as

`Delta A_ell(Psi) = ell(Psi) delta_N`,

where `ell in H_B^*` is an arbitrary linear functional.

Because `H_B` is already the gauge-invariant spin-network boundary Hilbert space, every `ell` acts on genuine invariant boundary data. In a different boundary basis the coefficient vector simply transforms contragrediently; the construction is therefore not a post-hoc selection of a convenient component.

Before root gauge fixing, place the delta distribution on the invariant common-collision set

`S={g: g_b^-1 g_a in SU(2) for all a,b}`.

Common left `SL(2,C)` multiplication leaves every relative element and `S` unchanged. The boundary scalar `ell(Psi)` is independent of the group gauge variable. Thus global source gauge invariance does not identify distinct elements of `H_B^*`.

## Integrated survival

With the normalized compact/tubular measure convention, integration of the order-zero term over the group variables gives

`Integral Delta A_ell(Psi) = C_N ell(Psi)`,

where `C_N` is the common nonzero normalization/volume factor associated with the chosen delta convention. In normalized Haar convention one may take `C_N=1`; changing convention rescales all directions by the same nonzero number.

Therefore the integrated ambiguity map contains an injective copy of `H_B^*`: no nonzero `ell` is annihilated solely by integrating `delta_N`.

This is stronger than the specific Iter077M/N choice `ell(Psi)=Integral_N F_SU2(y;Psi)`: that choice exhibited one source-structured direction, while the extension theorem itself permits the full order-zero boundary dual unless additional source conditions are imposed.

## Source symmetry audit

The primary causal-vertex construction defines a labelled fixed-causal vertex as a linear functional on the spin-network boundary state. No local extension normalization, Hermiticity/reality condition, permutation-invariance equation at fixed labels, or other equation is stated that collapses all 32 boundary-dual coefficients to one scalar.

Simultaneous relabelling covariance of graph data, if imposed, would transform both the basis states and the coefficient functional; it is not an equation requiring the coefficient vector to be invariant while the labelled boundary data are held fixed.

## Exact lower bound

Hence in the frozen minimal boundary sector the order-zero supported ambiguity has

`dim_C >= dim_C H_B^* = 32`.

The full Iter077L ambiguity is potentially much larger because normal derivatives through order 8 and nonconstant/distributional coefficient data along `N` have not been classified.

## RG consequence

Any refinement/RG ansatz using only

`A_c=A_0+cL`

is a one-direction witness truncation, not a closed representation of the known local extension freedom. A physical RG map must either:

1. carry at least the full 32-dimensional order-zero image in this finite-spin sector; or
2. prove a symmetry/dynamical reduction theorem selecting a lower-dimensional subspace before projecting.