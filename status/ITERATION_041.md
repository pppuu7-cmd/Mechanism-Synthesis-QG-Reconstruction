# Iteration 041 — source delta/delta-prime collision forest census

Status: **TERMINAL / HIGHER-ORDER SOURCE EXTENSION BUDGET PRESENT**

Date: 2026-09-12

## Closed prerequisite

Iter040 run `34695321410` showed that S5 symmetry plus the unique quadratic invariant does not generate all local invariant jets: primitive S5 quotient dimensions are already 3 at degree 4 and grow to 86 at degree 16.

The next route therefore has to use source/Feynman structure rather than another generic symmetry assumption.

## Preregistered source question

For the published j=1/2 Appendix-D boundary primitive, every singular wedge contributes either `delta` or `delta_prime`. For complete K_k collision subgraphs (k=2..5), let E=k(k-1)/2 be the number of wedges and m the number of delta-prime wedges. The frozen superficial source budget is

`sd = E+m`,  `omega = sd-(k-1) = E+m-(k-1)`.

This is only a scaling-degree/combinatorial diagnostic. It does not assert that the naive product exists; Iter028/029 non-transversality remains binding.

## Authoritative computation

Preregister commit `7d880f96a96a92ca089cff68ea102e7f98e4bcf8`; computation commit `db715ad25a2c1d4e21ad711a6cf6224b867a5113`; workflow commit `c843ba032a65bb7d28de33e7e5be89b89d67f6c6`; run `34695499357`.

All **24/24 lanes completed SUCCESS** and produced one raw JSON artifact per `(k,m)` source sector. Orbit-partition, binomial-count, action-closure and cycle-rank gates passed in every lane.

Exact superficial extension degrees:

- K2, E=1, cycle rank 0: `omega = 0,1` for m=0,1. This is the acyclic single-wedge control.
- K3, E=3, cycle rank 1: `omega = 1,2,3,4` for m=0..3. Higher-order (`omega>=4`) first appears at the all-delta-prime lane m=3.
- K4, E=6, cycle rank 3: `omega = 3,4,5,6,7,8,9` for m=0..6. Higher-order appears for every m>=1.
- K5, E=10, cycle rank 6: `omega = 6,7,8,9,10,11,12,13,14,15,16` for m=0..10. Thus even the all-delta complete-collision sector already lies beyond the quadratic local budget.

Selected exact S_k source-pattern orbit counts:

- K3: one orbit for every m.
- K4: orbit counts `[1,1,2,3,2,1,1]` for m=0..6.
- K5: orbit counts `[1,1,2,4,6,6,6,4,2,1,1]` for m=0..10.

Selected artifact provenance from run `34695499357`: K2 m0 artifact `10298700753`; K3 m0 `10298985317`; K3 m3 `10298625938`; K4 m6 `10298840367`; K5 m3 `10298990288`; K5 m7 `10299045242`; K5 m9 `10298850519`; K5 m10 `10298611020`. The run contains all 24 artifacts.

## Frozen scientific discriminators

`SOURCE_MIXED_TERMS_REQUIRE_ONLY_QUADRATIC_EXTENSION_DATA = FALSE`.

`HIGHER_ORDER_SOURCE_EXTENSION_BUDGET_PRESENT = TRUE`.

This materially strengthens the Iter040 localization: higher-order local-extension orders are not merely abstract S5 possibilities. They are reached already by the superficial scaling budget of the actual Appendix-D delta/delta-prime source sectors, with K5 requiring omega>=6 even at m=0.

It still does **not** determine which primitive S5 directions receive nonzero coefficients, nor does it define the non-transverse multi-wedge distribution product. The next independent diagnostic is to intersect the source derivative-direction span with the Iter040 primitive quotient, followed by a source-faithful correlated finite-epsilon/Feynman extension test.

## Interpretation lock

- no divergence/nonexistence theorem;
- no arbitrary counterterm authorization;
- no physical F9/G3/G8 promotion;
- `T+ + T- = D` cancellation cannot be borrowed by a fixed causal sector without proof.
