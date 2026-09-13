# Iter076I terminal result — source reversal versus tetrahedral Hodge support

Date: 2026-09-13

## Authority
- preregistration: `f0b7aa3bd65c10b85daab85c92589986b845d132`
- implementation: `fff3b08f4740fa1aff8fc01965e6fd0d1d06beb4`
- production/workflow head: `4b05324531f982d93df3c0dd8b56b58668670bf0`
- run: `34776104982`
- aggregate job: `103774413741`
- aggregate artifact: `10324145415`
- aggregate digest: `sha256:5b1f3558947d8032bd920e4ad4cd87cf5eadf5896fa982d586fbe8a8ed1d4abe`

Raw lane artifacts consumed:
- A: job `103774386230`, artifact `10323159437`, digest `sha256:fde097d1a7a235b0c4446fc0130011af4a112f3b26a9b8bc3c107c67fb528c57`
- B: job `103774386114`, artifact `10323881109`, digest `sha256:956ca35815d5fff788746c00098af826ff7356edaefd855b4d6f17a79d890835`
- C: job `103774386205`, artifact `10323881108`, digest `sha256:543deef7867c8f57c6129793257e45cd848d14bf19ecd3b377f4baa48f375008`
- D: job `103774386191`, artifact `10323174373`, digest `sha256:9b86cae42427a8cbaf2410b7107b8ab7e27cb070359142547e1e3e32801ef3f6`

## Frozen scientific classification
`ITER076I_SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`

## Terminal facts
All four prospectively frozen lanes pass.

1. Source-backed equal-spin wedge order reversal preserves the same unordered wedge support in all `6/6` K4 edge cases; complementary-edge transports are `0/6`.
2. The source reversal support and the canonical Hodge support differ on every source edge. Their exact 6x6 support Hamming distance is `12`. The Hodge operator has one complementary-edge target per edge, whereas the established source reversal is edge-diagonal at the unordered-wedge level.
3. For representative `2j = 1,2,3,4`, magnetic-index swap/conjugation remains internal to each wedge block: cross-unordered-edge support is exactly zero in every lane. Deliberately inserting complementary-edge transport is exactly distinguishable.
4. The source reversal parity character still matches `sgn(p)` for all `24/24` S4 elements, consistent with Iter076G. Thus the one-dimensional twist character is source-compatible while the matrix-valued complement pairing is not supplied by the established reversal law itself.

## Interpretation
This is a scoped source-provenance blocker, not a scientific failure of the causal vertex and not a no-go theorem. Iter076F-H show that the canonical tetrahedral Hodge complement is the unique algebraically allowed sign-twisted cut-to-cycle generator, but Iter076I shows that the currently established source reversal/magnetic-index law does not select that matrix support.

The missing object is now narrowed to a source-derived complementary-edge/dualization prescription (or another source-derived matrix map with the same algebraic role), potentially from the full Eq.(4)/Eq.(7) contraction/intertwiner/orientation structure rather than wedge reversal alone.

`SOURCE_TO_K4_PUSHFORWARD` and the nominal `epsilon^-1` numerator/Jacobian coefficient remain `BLOCKED_OBJECT_DEFINITION`. No G3/F9/G8/K5 promotion, causal-vertex finiteness/divergence theorem, physical sector selection, complete-QG claim, or new-physics claim follows.
