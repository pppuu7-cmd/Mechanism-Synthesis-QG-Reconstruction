# Iteration 068D result — S4 covariance of the Iter068A denominator skeleton

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `124274f910c1cec8fde810a5e96d96224b0e4d45`
- Implementation: `7ec6d117762f8ef41b8eb6e69a25dfffb30077da`
- Initial workflow commit: `84538fde505098ff2f759977df77252156fd4c99`
- Initial run `34740854819`: infrastructure-only Python import-path failure before covariance predicates.
- Minimal launcher-only repair: `17184c54e13dfaf3cf21d1864ea10cc3fbc0b8a9`
- Authoritative repaired run: `34740982202`
- Aggregate job: `103680604842`
- Aggregate artifact: `10312294509`
- Digest: `sha256:d40df4684ae15634d184c6ee291b0e67daf80edbb4e435605659f9152ba39ec0`

## Frozen result

All `16/16` lanes passed. Each lane evaluated all 24 permutations of the four K4 vertices, for `384/384` exact transformed cases.

Terminal classification:

`ITER068D_K4_MICROLOCAL_SKELETON_S4_COVARIANT`

The transformed physical `kappa` pattern reconstructed exactly, global sigma gauge recanonicalization preserved `kappa`, the Iter068A collision classification was invariant under every S4 permutation, and the inverse permutation recovered the original ordered-edge skeleton up to the already audited global convention reversal.

## Scientific interpretation

The 8/8 compatible/obstructed split found by the Iter068A denominator-incidence skeleton is not an artifact of K4 vertex numbering or edge presentation. It is S4-covariant at that skeleton level.

This does not make the compatible half physical: Iter068B shows that the source-backed `j=1/2` contact layer obstructs naive separate-contact multiplication for all frozen causal classes. Iter068D is therefore a covariance result for the denominator skeleton, not a full Toller wavefront theorem and not a physical sector selector.

No K5/G3/F9/G8 promotion is authorized.
