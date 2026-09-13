# Iter078G-RG result — order-zero extension freedom saturates the entire integrated all-j=1/2 vertex space

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078G_RG_INTEGRATED_VERTEX_AMBIGUITY_SATURATION.md`, commit `1a92ae65b6efa1f3fc4409383108787d77aeb496`.
- Controlling upstream theorem: Iter078E-RG, which establishes an injective copy of the full 32-dimensional boundary dual in the integrated order-zero ambiguity.

## Classification

`ITER078G_RG_ORDERZERO_EXTENSION_AMBIGUITY_SATURATES_FULL32_INTEGRATED_JHALF_VERTEX_SPACE_EXACT_THEOREM_SCOPED`

Scientific verdict: **PASS**.

## Exact argument

For the frozen all-`j=1/2` boundary sector,

`dim_C H_B^* = 32`.

The integrated fixed-causal vertex is a linear functional on `H_B`, so every integrated extension difference is an element of the same 32-dimensional space `H_B^*`.

Iter078E constructs an injective linear map

`J: H_B^* -> Amb_integrated`

by

`J(ell)=C_N ell`,

where `C_N != 0` is the common normalization from integrating `ell(Psi) delta_N` over the supported collision submanifold.

Thus

`dim Amb_integrated >= 32`.

But also

`Amb_integrated subseteq H_B^*`

and therefore

`dim Amb_integrated <= 32`.

Hence exactly

`Amb_integrated = H_B^*`,

`dim_C Amb_integrated = 32`.

## New scientific fact

Within this fixed finite-spin causal sector, the off-collision Toller source object together with the presently established scaling-degree and gauge constraints does **not** determine an absolute integrated 32-component vertex vector.

Given any reference integrated extension `a_ref in C^32` and any target `a_target in C^32`, an admissible order-zero supported extension shift exists that maps

`a_ref -> a_target`.

Therefore the local finite-spin vertex is maximally underdetermined in this sector until additional selector conditions are imposed.

## Consequence for RG/refinement

A one-parameter extension coupling is not merely incomplete: before extra physics, the full integrated minimal-sector vertex itself is an affine 32-dimensional ambiguity space. The experimental CRQN v0.3-R0 refinement programme must therefore supply enough independent consistency/normalization information to select a point in this space or a theorem reducing it to a smaller physical subspace.

## Interpretation ceiling

This is a fixed all-`j=1/2`, fixed-causal-structure theorem. It does not prove arbitrary independent shifts across all spin sectors simultaneously and does not imply that semiclassical, refinement, covariance or continuum conditions cannot select a unique correlated family across spins.

It is not a generic-spin nonpredictivity theorem, not a no-go theorem for CRQN, and not a statement that any chosen extension is physically acceptable.

## Exact next admissible step

The next high-information gate is no longer another local singularity calculation. It is a **selector-rank gate**: determine whether the versioned causal 1-to-5 consistency framework can generate at least 32 independent constraints on the controlling integrated ambiguity space, or whether its matching equations are structurally rank-deficient even before numerical vertex evaluation.