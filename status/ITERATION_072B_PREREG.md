# Iteration 072B preregistration — K4 Schwinger signed-cut-space leading coefficient

Date frozen: 2026-09-13

## Purpose

Iter072A terminally failed because its preregistered theorem route confused the circulation space `ker(B)` with the Schwinger delta space `ker(L^T)`. Iter072B freezes the corrected dual-space question before implementation.

For zero external flow, `x=L y` with columns of `L` spanning the K4 cycle space. The common-epsilon Schwinger/Fourier representation imposes

`L^T diag(s) t = 0`, `t_e >= 0`.

Thus `diag(s)t` lies in the K4 cut space. The candidate full-collision `epsilon^-3` coefficient is nonzero only if this three-dimensional kernel has nonempty relative interior inside the positive orthant.

## Frozen hypothesis

For K4 tournament sign vector `s`,

`exists t_e > 0 with L^T diag(s)t=0`

iff the tournament is acyclic, equivalently transitive.

This is distinct from Iter058's strong-tournament / positive-circulation theorem and from Iter068A's denominator-wavefront collision test.

## Frozen lanes

Eight source factorized sigma classes:
`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

Each lane is tested in all four cycle bases `S0,S1,P0,P1`.

## Frozen predicates

P1. Exact rank: `rank(L)=3`, `rank(L^T diag(s))=3`, kernel dimension 3, tree minor unimodular.

P2. Independent tournament acyclicity: compute topological order directly. Require acyclic iff the tournament score sequence is `[3,2,1,0]`.

P3. Constructive cut-space witness for acyclic lanes: from the topological order assign strictly ordered integer vertex potentials and form canonical edge cut flow `x=B^T u`; require `sign(x_e)=s_e`; set `t_e=s_e*x_e`; require all `t_e>0` and exact `L^T diag(s)t=0` in all four bases.

P4. Obstruction for cyclic lanes: solve the exact strict-sign feasibility combinatorially by enumerating all vertex-potential orders; require no potential order realizes `s`. This is independent of P3's chosen witness.

P5. Relative-interior criterion: acyclic lanes must have a strict witness and kernel dimension 3; cyclic lanes must have no strict witness. This freezes whether the Schwinger delta-cone has positive 3D relative measure.

P6. Proper-stratum power separation: all nonempty proper denominator subsets must have `#factors-rank < 3`, independently recomputed in every basis.

P7. Source numerator and Iter071A frozen test functions `G0,G1,G2` must each have full-collision constant term exactly 1.

P8. Basis covariance: all classifications and P1-P7 outcomes identical in `S0,S1,P0,P1`.

P9. Negative control: replace source pair sign `sigma_a sigma_b` by the deliberately wrong single-vertex sign map `sigma_a`; it must change the acyclic/strict-cut classification for at least one source lane.

## Frozen outputs

If all predicates pass:
`ITER072B_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_TRANSITIVE_TOURNAMENT_SCOPED`.

If any mathematical predicate fails:
`ITER072B_SIGNED_CUTSPACE_THEOREM_FAIL` with exact counterexample preserved.

Implementation/parser failures are `ITER072B_INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL` and do not count scientifically.

## Interpretation lock

A PASS permits only the reduced K4 common-epsilon statement that the full-collision candidate `epsilon^-3` Schwinger coefficient is nonzero exactly for source sign classes whose tournament is transitive, assuming the frozen Schwinger/Fourier derivation. For other classes only this leading full-collision coefficient vanishes; subleading/proper-collision behavior remains open.

No physical causal-sector selection, complete causal-vertex divergence theorem, K5 extension, G3/F9/G8 promotion, NEW_PHYSICS_FOUND or complete-QG claim is authorized.
