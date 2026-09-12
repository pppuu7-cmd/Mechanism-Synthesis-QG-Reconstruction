# Iteration 041 — source delta/delta-prime collision forest census

Status: **PREREGISTERED / RUNNABLE**

Date: 2026-09-12

## Closed prerequisite

Iter040 run `34695321410` showed that S5 symmetry plus the unique quadratic invariant does not generate all local invariant jets: primitive S5 quotient dimensions are already 3 at degree 4 and grow to 86 at degree 16.

The next route must therefore use source structure rather than another generic symmetry assumption.

## Source-tied question

For the published j=1/2 Appendix-D boundary primitive, every singular wedge contributes either a `delta` or `delta_prime` term. Before attempting a correlated Feynman extension, census all complete K_k collision subgraphs (k=2..5) by the number `m` of delta-prime edges.

For K_k with `E=k(k-1)/2` edges and common-spectral relative-coordinate dimension `n=k-1`, a mixed pattern with m derivative edges has nominal homogeneous scaling degree

`sd = (E-m)*1 + m*2 = E+m`

and superficial extension degree

`omega = sd - n = E + m - (k-1)`.

This is only a scaling-degree/power-counting diagnostic. It does not assert that the naive product exists. Wavefront/transversality remains a separate gate: complete K_k has cycle rank `E-(k-1)`, so K3/K4/K5 are precisely the cyclic cases already implicated by Iter028/029; K2 is retained as the single-wedge control.

## Exact combinatorial layer

For each `(k,m)` lane:

1. enumerate all `C(E,m)` delta-prime edge assignments;
2. quotient them under exact S_k vertex relabeling;
3. record the number and sizes of source-pattern orbits;
4. record cycle rank, nominal scaling degree and omega;
5. record whether the graph is acyclic/transverse-control (`cycle_rank=0`) or cyclic (`cycle_rank>0`).

Matrix: every m=0..E for k=2,3,4,5, totaling 24 independent lanes.

## Frozen discriminators

- numerical/combinatorial consistency: orbit sizes sum to `C(E,m)` and every orbit is closed under S_k;
- `SOURCE_MIXED_TERMS_REQUIRE_ONLY_QUADRATIC_EXTENSION_DATA` is true only if every cyclic source lane has `omega<=2`;
- `HIGHER_ORDER_SOURCE_EXTENSION_BUDGET_PRESENT` is true if any cyclic source lane has `omega>=4`;
- no scientific conclusion is based on CI color alone.

No threshold, k-range, or m-range may be changed after results are seen.

## Interpretation lock

A positive higher-order budget does not prove divergence, nonexistence, or that all mathematically allowed invariant jets occur physically. It only identifies which extension orders are source-compatible at superficial scaling level and prepares the forest/inclusion-exclusion and correlated i-epsilon gates. K2 remains a control because its single distribution is already well defined.
