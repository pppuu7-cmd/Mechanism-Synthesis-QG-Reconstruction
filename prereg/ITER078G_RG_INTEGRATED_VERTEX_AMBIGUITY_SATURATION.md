# Iter078G-RG preregistration — does order-zero extension freedom saturate the entire integrated all-j=1/2 vertex space?

**Date:** 2026-09-14

## Scientific question

Iter078E proves an injective 32-dimensional order-zero supported ambiguity inside the integrated fixed-causal all-`j=1/2` boundary functional. Since that boundary functional itself lives in a 32-dimensional dual space, does the allowed ambiguity already saturate the entire integrated vertex space?

If yes, then before an external selector is supplied, the off-collision source object plus finite-scaling-degree/gauge constraints do not determine any absolute 32-component integrated vertex vector in this minimal sector.

## Frozen inputs

1. Exact boundary space:
   `dim_C H_B = 32`.
2. Integrated vertex at fixed spins and fixed causal structure is a linear functional in `H_B^*`, hence its component vector belongs to a complex vector space of dimension 32.
3. Iter078E establishes an injective linear map
   `J: H_B^* -> Amb_integrated`
   of the form
   `ell -> C_N ell`,
   with common nonzero `C_N` from integrating `ell(Psi) delta_N`.
4. `Amb_integrated` is a subspace of `H_B^*`, because any extension difference changes only the same integrated boundary linear functional.

## PASS

PASS iff finite-dimensional linear algebra gives

`Amb_integrated = H_B^*`

and therefore

`dim_C Amb_integrated = 32`.

Equivalent physical statement in the frozen sector:

for any reference integrated extension vector `a_ref in C^32` and any target vector `a_target in C^32`, there exists an admissible order-zero supported extension shift such that

`a_ref -> a_target`.

Classification:

`ITER078G_RG_ORDERZERO_EXTENSION_AMBIGUITY_SATURATES_FULL32_INTEGRATED_JHALF_VERTEX_SPACE_EXACT_THEOREM_SCOPED`

## FAIL

FAIL iff the integrated extension differences live in a proper subspace despite the Iter078E injection, which would require identifying an inconsistency in the frozen dimension or codomain assumptions.

## Interpretation ceiling

PASS concerns one fixed all-`j=1/2` boundary-spin sector and one fixed causal structure. It does not show arbitrary control over generic-spin amplitudes simultaneously, nor compatibility of independently chosen shifts across spins, causal sectors, refinements, semiclassical limits or gluing.

PASS also does not imply the programme is impossible: refinement/RG, semiclassical matching, covariance, normalization, or other independently derived conditions may select a unique point in this 32-dimensional affine space. It does imply those conditions are mathematically indispensable for predictivity.

No RG fixed point, no generic-spin theorem, no G3, no continuum or complete-QG claim.