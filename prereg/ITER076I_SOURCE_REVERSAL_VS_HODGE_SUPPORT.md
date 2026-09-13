# Iter076I preregistration — source wedge reversal versus tetrahedral Hodge support

Date: 2026-09-13

## Purpose
Iter076F-G-H establish, respectively, that the algebraically allowed K4 cut-to-cycle intertwiner is one-dimensional only after the S4 orientation-sign twist, that the source-backed equal-spin wedge-reversal character matches that twist, and that the canonical tetrahedral Hodge complement realizes the unique twisted generator. This gate asks the still-open provenance question: does the actually established source reversal/magnetic-index transport itself determine the matrix-valued complementary-edge Hodge map, or only its one-dimensional parity character?

This gate is prospective. No production outputs exist at preregistration time. Frozen scientific criteria below must not be weakened after viewing results.

## Source authority and scope
Use only:
1. `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md` Eq. (4)/(7) conventions: ordered wedge argument `g_b^-1 g_a` and magnetic-index placement;
2. terminal Iter059 equal-spin law `T^(+)_{jm,jn}(g^-1)=conjugate(T^(-)_{jn,jm}(g))` and branch-swapped companion;
3. Iter076F/G/H exact algebraic objects, only as comparison targets.

No unequal-spin branch law, no fitted source-to-K4 map, no arbitrary complement pairing, and no denominator-only construction may be imported.

## Frozen objects
Let the six unoriented K4 wedge carriers be `E={(i,j):0<=i<j<=3}`.

- `R_src`: edge-support action induced by source wedge order reversal. Reversing `(i,j)` to `(j,i)` keeps the same unordered wedge support `{i,j}`; branch and magnetic indices may swap/conjugate, but no distinct unordered edge is introduced by Iter059.
- `H`: canonical Iter076H tetrahedral complement operator, `H e_ij = epsilon(i,j,k,l) e_kl`, with `{k,l}` the disjoint complementary edge.
- `M_j`: exact equal-spin magnetic-index swap/conjugation support for representative `2j in {1,2,3,4}`. It acts inside each wedge's magnetic fiber and therefore cannot by itself alter the unordered edge support.

## Independent frozen lanes
### Lane A — source edge-support audit
For every one of six K4 wedges, encode the Iter059/source reversal support before and after order reversal. PASS iff all six remain on the same unordered edge and no complementary-edge transport is present.

### Lane B — exact support mismatch with Hodge complement
Compare the 6x6 support matrices of `R_src` and `H`. PASS iff `R_src` is edge-diagonal in unordered-edge support, `H` has exactly one off-diagonal complementary-edge target per source edge, and their support Hamming distance is nonzero for all six source edges. Also verify that inserting the Hodge complement by hand makes the support agree; this is a missing-object control, not an authorization.

### Lane C — magnetic-fiber factorization
For `2j in {1,2,3,4}`, construct the source-backed magnetic index-swap support and the product support `R_src ⊗ M_j`. PASS iff every nonzero entry remains within the same unordered edge block for every tested j. A deliberately wrong control that inserts complementary-edge transport must be distinguishable exactly.

### Lane D — S4 covariance/provenance diagnostic
Recompute the Iter076G parity character and Iter076H twisted covariance, then test whether the source-established data determine a unique 6x6 edge map without adding a complement identification. PASS iff the source data fix the sign character but leave at least the matrix support underdetermined; the canonical Hodge operator becomes available only after an explicit complementary-edge/orientation structure is supplied. No coefficient fitting is allowed.

## Frozen interpretation
If A-D pass, classify:
`ITER076I_SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`

Meaning: current source-backed equal-spin reversal plus magnetic-index transport is insufficient to derive the matrix-valued physical P3 map. The missing object is narrowed to provenance for the complementary-edge/orientation identification (or an alternative source-derived map with the same algebraic role).

If source reversal itself generates complementary-edge support under the frozen construction, classify:
`ITER076I_SOURCE_REVERSAL_GENERATES_HODGE_SUPPORT_REVIEW`
and require independent manual/source review before any P3 promotion.

If a lane cannot be evaluated because a required source law is absent, classify `BLOCKED_SOURCE_LAW_NOT_ESTABLISHED`, not scientific FAIL.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL` and do not change the frozen science.

## Claim locks
Even a full PASS does not establish physical P3, the nominal `epsilon^-1` coefficient, causal-vertex finiteness/divergence, sector selection, K5, G3/F9/G8, complete QG, or new physics. It is a provenance/support diagnostic only.
