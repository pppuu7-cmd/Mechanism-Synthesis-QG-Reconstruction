# Iter083A-SM adversarial review — boundary-covariant K5 normal-symbol character classification

Date: 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_RESULT.md`, commit `4a56e325dad2c42f5ab7566c0e2f91d585cf4c9e`.

Prospective preregistration: `38abc8bfbc78fe07e56a4f29a09733925e96d9b2`.

Authoritative production run: `34910602967`, terminal `success`.

Authoritative job: `104197010950`, terminal `success`.

Artifact: `10374461752`, digest `sha256:da52890c29d86fc5d246c074e26fd670b5a860a635bdbf654042690637bcd973`.

Production JSON SHA256: `65e99a1011723848f53451c967fbd1d1af8c77580da5fa562427c5695ec16394`.

The older run `34908559463` remained stale queued and is scientifically irrelevant. The successful rerun was triggered by a workflow-comment-only commit; no scientific code or frozen criterion changed.

## SOURCE_OBJECT_CHECK

The source causal vertex is a linear functional on the true spin-network boundary state. In the frozen all-`j=1/2` 4-simplex sector each of the five four-valent intertwiner spaces is two-dimensional, so the boundary intertwiner fiber is genuinely 32-dimensional. Treating extension differences as boundary-dual-valued distributions is therefore the natural finite-dimensional vector-valued extension problem, not an artificial enlargement by unrelated scalar fields.

Iter077Q/Iter081R already fix the exact compact node gauge symmetry and the normal representation. The current gate adds the missing S5 action on the 32-dimensional boundary fiber instead of replacing the physical boundary by a scalar representative.

## LOCAL SINGLET CHECK

The four-spin invariant space was not identified merely by representation-name lookup. The implementation constructs total `J^2`, forms the exact spectral projector

`P0=((J^2-2I)(J^2-6I))/12`,

and checks idempotence, rank two and commutation with all 24 leg permutations. It then computes local permutation traces from `P0` itself.

This rejects a key surrogate risk: an arbitrary two-dimensional subspace of `(C^2)^tensor4` would have the right dimension but the wrong leg-permutation action. The preregistered arbitrary-rank-two projector negative control is mechanically rejected.

## K5 RELABELING CHECK

A K5 vertex permutation does more than permute five tensor factors; it also permutes the four incident legs at each moved vertex. The implementation derives those incident-leg permutations from the K5 relabeling cycles for all 120 elements of S5.

The vertex-only negative control is rejected. Therefore the recovered character

`(32,0,8,2,0,0,2)`

is not the trace of the naive permutation action on five abstract two-dimensional factors.

All 120 traces are class-constant, and the identity trace is 32.

## IRREP CHECK

The boundary character decomposes exactly as

`2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]`.

Every multiplicity is a nonnegative integer and the irrep dimensions sum to 32. This independently certifies that the class row is an honest S5 character rather than an accidental integer trace table.

The character norm 18 is consistent with a reducible representation and supplies no contradiction.

## PAIRING CHECK

The target multiplicity is

`m_k = dim (H_boundary^* tensor M_k)^S5`,

where `M_k=(Sym^k V)^SO(3)` and Iter081R supplies its exact S5 class character.

Two independent exact routes agree for every degree:

1. direct weighted class inner product;
2. decompose both the boundary character and `M_k` into S5 irreducibles and pair multiplicities.

Both give

`(2,0,5,1,22,10,72,48,217)`.

The corrupted-row and unweighted-inner-product negative controls both fail, so the result is not insensitive to the frozen Iter081R data or conjugacy-class weights.

## ODD-ORDER CHECK

The new nonzero values at orders 3, 5 and 7 are genuine representation-valued channels, not a contradiction with Iter081R. Iter081R counted only scalar S5 invariants and correctly found odd scalar dimensions zero. Tensoring with the nontrivial boundary S5 representation can contain the trivial representation even when `M_k` itself does not.

The exact irrep decomposition confirms this mechanism degree by degree.

## ORIENTATION/SIGN CHECK

A possible global sign twist from a different but consistent epsilon/edge-dual convention was preregistered as a robustness concern. The boundary character vanishes on the odd S5 conjugacy classes, so multiplying by the sign character leaves the relevant pairing sequence unchanged. Production explicitly confirms the sign-twisted pairing equals the untwisted one.

This robustness does not license arbitrary local orientation conventions; it only removes the specific global sign-twist ambiguity tested.

## COMPLETENESS CHECK

The result is complete for the **graded principal normal-symbol space** under the frozen all-`j=1/2`, exact compact gauge and S5 covariance assumptions. It is stronger than the scalar lower bound 28 but is not by itself a theorem about a globally split coefficient bundle.

The possible nonlinear mixing of displayed lower-order delta coefficients under tubular-coordinate changes does not invalidate the graded character result; it is precisely why the separate Iter083B filtered exactness theorem is required before interpreting the sum 377 as the dimension of the full filtered supported ambiguity space.

## COUNTEREXAMPLE_ATTEMPTS

1. **Replace the singlet space by an arbitrary two-dimensional subspace.** Rejected by exact permutation-commutation tests and the negative control.
2. **Ignore incident-leg permutations.** Rejected by the vertex-only action negative control.
3. **Use scalar Iter081R dimensions directly.** Rejected; it misses the boundary representation and especially odd orders.
4. **Drop S5 conjugacy-class weights.** Rejected by the exact control.
5. **Explain odd channels as numerical error.** Rejected by exact rational/integer character decomposition and independent pairing lanes.
6. **Introduce an orientation sign that changes multiplicities.** The tested global sign twist leaves them unchanged.
7. **Promote the graded count directly to a physical selector.** Rejected; classification of ambiguity directions is not selection of coefficients.
8. **Promote the result to generic spins or every collision stratum.** Rejected by the frozen scope.

## VERDICT

`CONFIRMED_SCOPED`

Authoritative classification:

`K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED`

with

`m_0..m_8=(2,0,5,1,22,10,72,48,217)`

and cumulative graded dimension `377`.

## AUTHORIZED NEXT CONSEQUENCE

The preregistered Iter083B structural theorem may now consume this authoritative sequence. If its already-frozen short-exact-sequence and homogeneous-space arguments remain confirmed, it may promote `377` from a graded-symbol sum to the exact dimension of the full frozen filtered boundary-covariant supported ambiguity through normal order 8.

## INTERPRETATION CEILING

No canonical splitting, no finite-part selector, no global all-strata physical vertex, no causal-vertex divergence/nonexistence theorem, no regulator independence, no generic-spin completeness, no multivertex closure, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
