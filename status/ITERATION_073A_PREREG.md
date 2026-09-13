# Iter073A preregistration — K4 signed cut-space proper-face atlas

Date: 2026-09-13

## Scientific objective
After terminal Iter072B, classify exactly which proper denominator subsets of the reduced K4 common-epsilon family admit a strict-positive Schwinger cut-space kernel. This gate targets the still-open subleading/proper-collision geometry for the four source classes whose full six-edge `epsilon^-3` coefficient is absent under Iter072B.

## Scope
Reduced K4 common-epsilon rational family only. This is an exact signed-cut-space/face-geometry audit. It does **not** establish a distributional boundary value, a complete causal-vertex asymptotic expansion, physical sector selection, K5 inheritance, G3, F9, G8, or new physics.

## Frozen panel
Source sigma labels exactly:
`++++`, `+++-`, `++-+`, `++--`, `+-++`, `+-+-`, `+--+`, `+---`.

Cycle bases exactly: `S0`, `S1`, `P0`, `P1`.

For every sigma and basis, enumerate every nonempty proper subset S of the six K4 edges (62 subsets). For S with m edges define
`A_S = L_S^T diag(s_S)` and exact nullity `nu_S = m - rank(A_S)`.
A face is positive-admissible iff `ker(A_S)` contains a vector with every t_e>0 on S.

## Two frozen exact feasibility routes
A. **Weak-order potential enumeration.** Enumerate all vertex potentials with values in `{0,1,2,3}`, quotient by additive shift/order compression, and require inactive edges to have zero potential difference while active edges have source-prescribed strict signs.

B. **Contraction/DAG criterion.** Contract every connected component of the inactive-edge graph. Reject if an active edge lies inside a contracted component. Orient each remaining active edge by the source sign and require the contracted directed graph to be acyclic. This criterion is checked independently from route A.

The two routes must agree on every subset.

## Frozen predicates
P1 exact ranks/nullities are basis-consistent for every subset.
P2 route-A and route-B positive-face feasibility agree for all 62 proper subsets.
P3 every feasible subset has `nu_S >= 1`; every infeasible subset is not promoted by nullity alone.
P4 the maximal feasible proper-face nullity and the full histogram by `(m,nu)` are identical across all four cycle bases for a fixed sigma.
P5 S4 edge-permutation canonical support counts are recomputed and invariant at the count/histogram level; no source sigma is interpreted as a physical sector.
P6 full-set cross-check reproduces Iter072B: full six-edge strict-positive kernel exists iff source tournament is transitive, with nullity 3.
P7 generic source numerator and three frozen Schwartz-test polynomial constant terms at the collision origin remain nonzero (=1), so this gate does not manufacture cancellations by coefficient fitting.
P8 negative control: replace source edge signs `z_a z_b` by tail-only signs `z_a`; the proper-face atlas must disagree with the source atlas for at least one sigma, while no source predicate is altered.

## Frozen classification rule
If all 8 lanes satisfy P1–P8 and aggregate consumes all lanes, output
`ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_EXACT_SCOPED`.
Otherwise output
`ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_FAIL`.

The aggregate must report, without post-hoc thresholding, each sigma's maximal feasible proper-face nullity, counts of feasible faces by subset size/nullity, and the full-set Iter072B cross-check.

## Interpretation lock
A PASS classifies exact positive Schwinger-face geometry only. `nu_S` is a collision-degree/geometric scaling indicator, not by itself a proof that the complete regulated integral contains a nonzero `epsilon^-nu_S` term; cancellations between strata, distributional finite parts, and Eq.(5)/(6) inheritance remain separate open questions.
