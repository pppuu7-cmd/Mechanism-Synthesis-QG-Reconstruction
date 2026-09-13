# Iter073B preregistration — complete K4 independent-wedge signed cut-space atlas

Date: 2026-09-13

## Objective

Classify the complete `2^6 = 64` independent K4 wedge-sign space required by the reduced Eq.(5)/(6)-control analogue, rather than restricting to the eight edge-factorized source sign classes of Iter072B/073A.

## Scope

Reduced K4 common-epsilon denominator/cut-space family only. This is an exact combinatorial and linear-algebraic prerequisite audit. It is **not** a proof of distributional Eq.(5)/(6), not the full Toller vertex, and not a physical causal-sector selector.

## Frozen objects

Canonical K4 edges `(01,02,03,12,13,23)`. Enumerate all 64 sign vectors `s_e in {+1,-1}`.

Cycle bases: exactly `S0,S1,P0,P1` from the existing K4 constrained-flow implementation.

For every sign vector and every nonempty edge subset `S`, define

`A_S = L_S^T diag(s_S)`, `nu_S = |S| - rank(A_S)`.

Positive admissibility means `ker(A_S)` contains a vector strictly positive on every active edge.

## Frozen predicates

P1. Exact ranks/nullities agree across all four cycle bases for all 64 sign vectors and all 63 nonempty subsets.

P2. Two independent positivity routes agree for every subset: weak-order potential enumeration and contraction/DAG criterion as frozen in Iter073A.

P3. Full-set positive admissibility is equivalent to transitivity of the oriented K4 tournament; report the exact count over all 64 sign vectors.

P4. For each sign vector, report the exact maximum positive-admissible proper-face nullity and histogram by `(m,nu)`.

P5. The histogram/census is invariant under all S4 vertex relabellings.

P6. Recover the eight edge-factorized source sign vectors `s_ab=z_a z_b` as an explicitly identified subset (modulo global `z -> -z`) and reproduce the Iter073A source-class histograms exactly.

P7. Negative control: scramble one canonical edge sign after source construction; at least one resulting vector must leave the source subset and change its exact source-orbit identity, without altering the 64-vector exhaustive census.

## Frozen outputs

Report:
- number of full-set positive-admissible sign vectors;
- number and histogram of cyclic/nontransitive sign vectors;
- distribution of maximal proper-face nullity over all 64 signs;
- S4 orbit signatures;
- exact source-subset cross-check.

PASS classification:

`ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_EXACT_SCOPED`

otherwise:

`ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_FAIL`

## Claim lock

This gate only classifies signed cut-space geometry. It does not establish cancellation in the independent-wedge sum, a source-defined epsilon->0 boundary value, the EPRL vertex distributionally, K5, G3, F9, G8, complete QG or new physics.
