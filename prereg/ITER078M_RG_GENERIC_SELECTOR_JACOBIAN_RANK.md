# Iter078M-RG preregistration — does the fixed-j=1/2 full-32 refinement control have a generic full-rank Jacobian?

**Date:** 2026-09-14

## Scientific question

Iter078G shows the integrated order-zero extension ambiguity saturates the complete 32-dimensional all-`j=1/2` boundary dual. Iter078H/J show the exact fixed-spin 1-to-5 control map has Jacobian rank 31 at the compact BF-like tensor `L`, with the unique null direction lifted nonlinearly at order 2.

Is rank 31 a structural rank ceiling of the degree-5 map, or is `L` a special singular point while the map is generically locally full rank 32?

A single exact rank-32 Jacobian witness is sufficient to prove that the determinant polynomial is not identically zero and hence that rank 32 holds on a nonempty Zariski-open subset of the 32-dimensional control theory space.

## Frozen map

Use exactly the EPRL-edge-weight fixed-`j=1/2` map `R_EPRL:C^32->C^32` from Iter078H, with no changes to slot convention, face factor, internal edge weights or topology.

No Toller reference extension, causal-orientation sum or higher-spin data are imported.

## Prospectively frozen witness tensors

In the lexicographic basis index `i=0,...,31`, evaluate the exact Jacobian at:

1. `C^(A)_i = i+1`;
2. `C^(B)_i = (-1)^(popcount(i)) (i+1)`;
3. `C^(C)_i = (i+1)^2`;
4. control `C^(L)=L` from Iter077N/Iter078H.

No witness may be changed or added after ranks are observed in this gate.

## Parallel lanes

Run A/B/C independently. Each lane must:

- compute the exact integer `32x32` Jacobian;
- compute exact rank over `Q`;
- if rank 32, record an exact determinant or fraction-free nonzero full-rank certificate;
- if deficient, record nullity and exact null witness.

A separate control lane must reproduce rank 31 at `L`.

## PASS

PASS iff at least one of A/B/C has exact rank 32.

Classification:

`ITER078M_RG_FIXED_JHALF_FULL32_REFINEMENT_CONTROL_HAS_EXACT_FULL_RANK_JACOBIAN_WITNESS_GENERIC_LOCAL_RANK32_SCOPED`

Allowed conclusion:

- the Jacobian determinant of the frozen polynomial map is not identically zero;
- rank 32 is generic in the algebraic sense on a nonempty Zariski-open subset;
- the rank-31 point `L` is a special singular point, not a structural one-direction deficit of the fixed-spin control map.

## Non-PASS outcome

If all three frozen candidate points are rank-deficient, classify only

`ITER078M_RG_NO_FULL_RANK_WITNESS_IN_FROZEN_GENERIC_CONTROLS`

with verdict `INCONCLUSIVE_GENERIC_RANK`, unless an independent symbolic theorem proves a rank ceiling. Do not infer generic rank deficiency from three failed samples.

## Interpretation ceiling

Even PASS proves only generic local rank of the **fixed all-j=1/2 pure order-zero control map**. It does not prove that the physical causal-Toller coarse/fine matching equations exist, are finite, or uniquely select the K5 extension. It says only that the frozen 32D tensor-network contraction has enough local algebraic rank in principle.

No RG fixed point, regulator independence, generic-spin closure, G3 or complete-QG claim.