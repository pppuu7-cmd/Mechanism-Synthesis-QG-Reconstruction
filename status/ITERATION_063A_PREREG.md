# Iteration 063A preregistration — K4 ordered-bridge tree/cycle prescription independence

Date: 2026-09-13

This preregistration is prospective and precedes implementation/production.

## Scientific question

Given terminal Iter062 bridge `s(a,b)=c eta(a,b) kappa_ab`, does the induced K4 analyticity bookkeeping remain exactly independent of the arbitrary spanning-tree/fundamental-cycle representation used to solve conservation constraints, for every physical sigma class, both unfixed global conventions, and every S4 relabeling?

This is a prerequisite for a direct-causal-vertex prescription. It is NOT a causal-vertex amplitude test, NOT an exact EPRL amplitude control, and cannot promote K5/G3/F9/G8.

## Frozen domain

- vertices: K4 = `{0,1,2,3}`
- physical sigma representatives: 8 classes with global sigma flip quotient, fixed representative `sigma_0=+1`
- global branch convention: `c in {-1,+1}`
- all 24 S4 relabelings
- all 16 labeled spanning trees of K4 (Cayley count `4^(4-2)=16`)
- both wedge order states checked by sign reversal
- ordered bridge exactly `s(a,b)=c eta(a,b) sigma_a sigma_b`

## Frozen exact tests

For every `(sigma_class,c,permutation,tree)` lane:

1. construct oriented incidence matrix B in canonical edge order `(01,02,03,12,13,23)`;
2. construct the fundamental-cycle basis induced by the chosen spanning tree with deterministic chord order;
3. verify exact integer cycle vectors lie in `ker(B)` and have rank 3;
4. solve the strict sign chamber criterion using an exhaustive positive integer coefficient witness search over coefficients `1..6` in the fundamental-cycle basis;
5. independently classify the same oriented sign vector by strong connectivity of the induced tournament;
6. require chamber feasibility iff strong connectivity;
7. require the result for a fixed `(sigma,c,permutation)` to be identical for all 16 spanning trees;
8. reverse wedge order (`s -> -s`) and require the corresponding tournament/chamber classification to transform covariantly and retain feasibility status;
9. require the global convention pair `c=±1` to have identical feasibility status for each physical sigma/permutation/tree.

The finite witness search is not allowed to define feasibility by failure: for strong tournaments the implementation must additionally construct a deterministic strictly-positive circulation as a sum of all directed simple cycles and reconstruct it exactly in each fundamental-cycle basis. Non-strong tournaments must produce a one-way directed-cut obstruction.

## Frozen outputs

- `ITER063A_SOURCE_OR_IMPLEMENTATION_INVALID`
- `K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_DEPENDENCE_FAIL`
- `K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENT`

## Interpretation rule

A PASS establishes only exact representation-independence of this K4 ordered-sign analyticity prerequisite across all spanning trees/fundamental-cycle bases/permutations/order reversal/global convention. It does not establish a source-defined causal vertex, absolute/conditional integrability, an EPRL amplitude equality, a physical sector, or K5 readiness. A subsequent independently preregistered source-backed exact-EPRL/direct-vertex gate remains mandatory.

No thresholds, domain, or interpretation may be changed after production output is inspected.