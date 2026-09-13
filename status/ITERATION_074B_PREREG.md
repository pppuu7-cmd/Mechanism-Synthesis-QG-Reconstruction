# Iter074B preregistration — strict dual separation for nontransitive source classes

Date: 2026-09-13

This gate is frozen before production.

## Objective
Strengthen Iter073C from a nonnegative Stiemke certificate with at least one positive component to an exact strict dual separation certificate on every active edge. This is the finite-dimensional prerequisite for a uniform positive-real nonpinch estimate.

## Scope
Reduced K4 common-epsilon signed cut-space only. A strict dual certificate is not by itself a theorem of epsilon-to-zero convergence, complex contour admissibility or physical vertex finiteness.

## Frozen panel
Source classes exactly `++-+`, `+-++`, `+-+-`, `+--+`; cycle bases exactly `S0,S1,P0,P1`; all 63 nonempty subsets of the six K4 edges. Total `1008` cases. For each subset S form `A_S=L_S^T diag(s_S)`.

## Frozen certificate
Search deterministic primitive integer `y in Z^3` in increasing `(L1, lexicographic)` order, with hard coordinate cap `12`, such that `w=A_S^T y > 0` strictly on every active component. Record `y`, `w`, primitive `L1`, minimum positive integer margin, and normalized margin `delta_1=min(w)/||y||_1`.

## Frozen predicates
P1. All `1008/1008` cases admit a strict certificate within the frozen cap.
P2. Every stored certificate verifies exactly `A_S^T y=w` and `min(w)>=1`.
P3. Independent positivity recomputation confirms there is no nonzero nonnegative kernel on S: enumerate every nonempty support U contained in S and require no strict-positive kernel on U.
P4. Feasibility/status is basis-independent; report primitive-L1 and normalized-margin distributions but do not require coordinates to match across bases.
P5. Report a global exact lower bound `delta_1_min` across the frozen 1008 cases.
P6. S4 relabelling preserves existence and subset-size distribution of strict certificates.
P7. Positive control: on a known positive-admissible `++++` face no strict dual certificate may exist.

## Classification
PASS: `ITER074B_NONTRANSITIVE_ALL_FACES_STRICT_DUAL_SEPARATION_EXACT_SCOPED`

otherwise: `ITER074B_STRICT_DUAL_SEPARATION_FAIL`

## Claim lock
A PASS supplies exact positive-real separation directions for the reduced Schwinger cut-space. It does not authorize an epsilon-to-zero boundary-value theorem without a separate analytic estimate controlling the complex/distributional kernel and full numerator/group dependence. No physical sector selection, causal-vertex finiteness theorem, K5/G3/F9/G8 promotion, complete QG or new physics follows.
