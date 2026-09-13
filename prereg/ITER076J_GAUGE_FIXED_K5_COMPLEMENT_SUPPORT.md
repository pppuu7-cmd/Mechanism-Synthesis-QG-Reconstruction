# Iter076J preregistration — gauge-fixed K5 incidence versus K4 complement support

Date: 2026-09-13

## Purpose
Iter076I establishes that wedge reversal itself fixes only the orientation/sign character and preserves unordered edge support, so it cannot by itself produce the tetrahedral Hodge complementary-edge map. The source Eq.(4), however, contains a larger combinatorial object: the complete ten-wedge K5 graph with one gauge-fixed group variable (`g_1=1`). This prospective gate asks a narrower question before any dynamical claim: does the source-defined gauge-fixed K5 incidence canonically determine the **support** of the K4 complementary-edge involution on the six wedges among the four unfixed vertices?

No production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Source authority
Use only the repository primary-source snapshot of Eq.(4): five labelled source nodes, ten pair wedges, and one gauge-fixed root. No fitted coefficient, Toller asymptotic, denominator result, candidate mechanism, or physical sector choice may enter.

## Frozen construction
For each possible gauge root `r` in the five source nodes:
- `U_r` is the four unfixed nodes;
- `E_int(r)` is the six source wedges with both endpoints in `U_r`;
- `E_spoke(r)` is the four wedges incident to `r`;
- for an internal edge `{i,j}`, define the incidence-complement support candidate `C_r({i,j}) = U_r \ {i,j}`.

The candidate is a support map only. No sign is attached and no physical source-to-K4 pushforward is assumed.

## Frozen independent lanes
### A — exact source graph decomposition
For all five roots, verify K5 splits exactly into six internal K4 edges plus four spokes, with no overlap and complete ten-edge coverage. Verify each internal edge has a unique disjoint internal partner.

### B — uniqueness of complement support
Enumerate all permutation matrices on the six internal edges for one canonical root. Among maps satisfying all frozen properties—fixed-point-free involution, every edge mapped to a disjoint internal edge, bijective—verify uniqueness and equality to `C_r`.

### C — stabilizer covariance
For all five roots and every permutation of the four unfixed nodes, verify `C_r R(p)=R(p) C_r` at the unsigned support level. This is ordinary support covariance; the orientation-sign twist of Iter076F/H is deliberately not inserted here.

### D — root-change covariance and negative controls
Across all source-node permutations mapping root `r` to root `r'`, verify the family `C_r` is transported to `C_r'`. Reject controls that map an edge to an adjacent edge, introduce a fixed point, or use one root's complement pairing without relabelling after a root change.

## Frozen interpretation
If A-D pass, classify:
`ITER076J_SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED`

This would close only the **unsigned support provenance** part of the Iter076I blocker. It would not establish the signed Hodge matrix, source-induced cut-to-cycle pushforward, numerator/Jacobian, or any distributional amplitude property.

If the complement support is nonunique or not covariant, classify:
`ITER076J_K5_INCIDENCE_DOES_NOT_CANONICALLY_FIX_COMPLEMENT_SUPPORT`

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks
No physical P3, no nominal `epsilon^-1` coefficient, no causal-vertex finiteness/divergence theorem, no K5 promotion, no G3/F9/G8, no physical sector selection, no complete-QG or new-physics claim follows from either outcome.
