# Iter078J-RG preregistration — classify the unique linearized null direction of the fixed-j=1/2 1-to-5 control map

**Date:** 2026-09-14

## Scientific question

Iter078H found that the exact `32x32` Jacobian of the frozen fixed-`j=1/2` order-zero refinement control map at the compact tensor `L` has rank `31` and nullity `1` for both the EPRL-edge-weight measure and the unit-edge-weight control.

Is that one-dimensional null direction:

1. a genuine exact flat direction of the full degree-5 refinement map;
2. only a first-order degeneracy lifted at quadratic or higher order;
3. a recognizable discrete symmetry / Walsh-character direction;
4. measure-independent at the vector level, or only rank-independent?

No interpretation may be assigned before the exact null vector is consumed.

## Frozen upstream object

Use exactly the Iter078H tensor map implementation and slot convention:

`distributional/iter078h_rg_full32_orderzero_1to5.py`

with:

- local tensor space `C^32`, basis tuples `(k_0,...,k_4) in {0,1}^5` in lexicographic order;
- compact reference tensor `L` from Iter077N;
- EPRL-edge-weight map and unit-edge-weight control map;
- all internal/external spins frozen to `j=1/2`;
- no Toller reference extension and no causal-orientation sum.

## Lane A — exact null-vector extraction and cross-measure comparison

Recompute the exact Jacobians from source code, not by parsing historical prose.

For each measure:

- compute exact rank/nullity over `Q`;
- extract the deterministic primitive integer right-null vector `n` from exact RREF;
- verify `J(L)n=0` exactly;
- normalize the first nonzero component positive.

Compare the two primitive null vectors.

Record one of:

- `IDENTICAL`;
- `PROPORTIONAL` with exact rational factor before primitive normalization;
- `DIFFERENT`.

## Lane B — discrete-character / obvious-direction census

Without fitting after the fact, compare each primitive null vector against the frozen catalogue:

1. the compact tensor `L` itself;
2. the constant vector `1`;
3. all 32 Walsh-Hadamard characters
   `chi_s(k)=(-1)^(s dot k)`, `s in {0,1}^5`;
4. the support-indicator of `L != 0` and the zero-support indicator `L=0`;
5. the signed compact support vector `sign(L)` with zeros retained.

A match requires exact proportionality over `Q`; otherwise record `NO_MATCH`.

This catalogue is frozen before inspection of the null vector.

## Lane C — exact nonlinear line test, EPRL measure

Let `n` be the EPRL primitive null vector. Since `R` is degree 5, compute the vector polynomial exactly:

`R(L+t n)-R(L)=sum_(m=1)^5 t^m V_m`.

Recover the coefficient vectors exactly, either by direct combinatorial expansion or exact interpolation/evaluation. Verify `V_1=0` from the Jacobian result.

Record:

- first nonzero order `m_*` among `2,...,5`, or `EXACT_FLAT` if all vanish;
- number of nonzero output components in each `V_m`;
- exact checksum / deterministic serialization of all coefficient vectors;
- whether every nonzero `V_m` is proportional to `n`, to `L`, or neither.

## Lane D — exact nonlinear line test, unit-weight control

Repeat Lane C with the unit-edge-weight map and its own null vector.

Compare the first nonlinear order and proportionality pattern with Lane C.

## Scientific classifications

### Exact flat direction

If all `V_1,...,V_5` vanish for a measure:

`ITER078J_RG_LINEARIZED_NULL_IS_EXACT_FLAT_DIRECTION_OF_FIXED_JHALF_1TO5_CONTROL_MAP_EXACT_SCOPED`

### Nonlinear lifting

If `V_1=0` but some `V_m`, `m>=2`, is nonzero:

`ITER078J_RG_UNIQUE_LINEARIZED_NULL_IS_NONLINEARLY_LIFTED_AT_ORDER_M_EXACT_CONTROL_SCOPED`

with the exact first order `M=m_*` recorded in the result.

### Invalid

`INVALID_IMPLEMENTATION` if rank/nullity fail to reproduce Iter078H, the null witness does not verify, or polynomial reconstruction is inconsistent with degree 5.

## Interpretation ceiling

Even an exact flat direction is only a property of the frozen fixed-spin pure order-zero tensor-network control. It is not automatically a gauge symmetry of the physical causal-Toller theory.

A nonlinearly lifted null direction means the refinement map is locally singular at `L` but may still constrain that direction beyond linear order. It is not evidence that the full causal RG selector has rank 31 or 32.

No RG fixed point, regulator independence, unique K5 extension, G3, continuum or complete-QG claim follows.