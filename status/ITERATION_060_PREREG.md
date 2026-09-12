# Iteration 060 preregistration — source-backed reversal covariance of K4 analyticity geometry

Preregistered prospectively after terminal Iter059 and before any Iter060 production result.

## Scientific object
Combine only already-derived ingredients:
1. Iter056/057 orientation-cocycle action on the six canonically oriented K4 edges;
2. Iter058 exact theorem: strict sign-compatible circulation iff the associated K4 tournament is strongly connected;
3. Iter059 source-backed equal-spin Toller inversion law: group inversion / wedge-order reversal swaps `T+ <-> T-` with transpose/conjugation.

No Toller representation composition rule is assumed. No physical sector selector is assumed.

## Frozen domain
- vertices: `{0,1,2,3}`;
- canonical edges: `(01,02,03,12,13,23)`;
- all `64` oriented pole-sign vectors;
- all `24` vertex permutations;
- two source operations: ordinary source relabeling and relabeling composed with full wedge-order reversal (`T+ <-> T-` on every equal-spin wedge);
- total transformation lanes: `64 * 24 * 2 = 3072`.

## Frozen transformation
For each canonical edge after vertex permutation, include the algebraically forced orientation cocycle from reordering its endpoints back to canonical order. Under the additional full wedge-order reversal operation, apply the Iter059 branch swap to every edge, i.e. global sign complement after the relabeling+cocycle map.

## Frozen tests
A lane is valid only if all hold exactly:
1. transformed vector remains in the complete 64-vector oriented sign space;
2. direct tournament construction from the transformed signs agrees edge-by-edge with relabeling/reversal of the source tournament;
3. strong connectivity is invariant under vertex relabeling and under full edge reversal;
4. Iter058 feasibility predicate is invariant under the source-backed transformation;
5. for every strong source tournament, a deterministic positive circulation certificate transforms to a strictly positive circulation certificate of the target orientation and satisfies exact vertex conservation;
6. for every non-strong source tournament, a one-way-cut obstruction exists after transformation;
7. the four orientation-aware S4 orbit sizes remain exactly `8,8,24,24`; full reversal maps each orbit to an orbit of the same feasibility status;
8. branch-additive control is structurally compatible: reversal swaps the two branch labels but leaves the unordered sum `{T+,T-}` unchanged. This is a symbolic source-law control, not a numerical amplitude claim.

## Frozen classifiers
- `ITER060_SOURCE_OR_IMPLEMENTATION_INVALID`
- `K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANCE_FAIL`
- `K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANT`

## Interpretation rule
A PASS means only that the exact K4 tournament/positive-circulation surrogate is covariant under the actual source-backed equal-spin wedge reversal law plus vertex relabeling. It authorizes a subsequent prospective gate testing whether a source-selected causal K4 branch assignment lands in the strong-tournament domain and satisfies tree/cycle-basis/permutation/order independence with exact EPRL control.

A PASS does **not** prove that any physical causal assignment is strong, does not choose a physical sector, and does not prove contour existence, absolute integrability, a source-defined distributional amplitude, vertex finiteness/divergence, K5 extension, G3, F9, G8, complete quantum gravity, or new physics.

Frozen claim locks from CURRENT remain in force; criteria may not be weakened after production inspection.
