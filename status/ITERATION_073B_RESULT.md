# Iter073B result — complete K4 independent-wedge 64-sign atlas

Date: 2026-09-13

## Authority

- preregistration commit: `e89805765ba2c993ba5b1f082586675543cd9eba`
- implementation commit: `85800f38468a808f18ef6c64f0628a7497c8f6b2`
- authoritative workflow head: `dbd3fcf56a8060c508bf065e012961b99a7c366f`
- workflow run: `34748536488`
- job: `103700759855`
- artifact: `10315061564`
- digest: `sha256:b5d1638a7bada9ed6371d46bcee6526d9f61abd06668458370fe63e482cc96cd`

## Frozen classification

`ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_EXACT_SCOPED`

All seven preregistered predicates passed.

## Exact census

Across all `2^6 = 64` independent K4 wedge-sign vectors:

- `24` are transitive tournaments and have a positive-admissible full six-edge cut-space kernel;
- `40` are cyclic/nontransitive and have no positive-admissible full six-edge kernel.

The distribution of maximal positive-admissible **proper-face** nullity is

- `-1`: 24 sign vectors;
- `1`: 16 sign vectors;
- `2`: 24 sign vectors.

Thus the complete independent-wedge sign space is strictly richer than the eight edge-factorized source sign vectors used by the causal `kappa_ab=sigma_a sigma_b` construction.

## Source-subset cross-check

The eight source-factorized sign vectors were recovered exactly.  Within that subset:

- four transitive vectors have maximal proper-face nullity `2` and histogram `(3,1)x2`, `(4,1)x1`, `(5,2)x3`;
- four nontransitive vectors have no positive-admissible proper face.

This reproduces Iter073A exactly.

## Interpretation

This closes the signed cut-space **geometric census** required before studying an independent-wedge Eq.(5)/(6)-control analogue at K4.  It does not prove the distributional Eq.(5)/(6) identity after correlated pullback, because the boundary-value operation and the 64-sign sum still have to be shown to commute in the relevant non-transverse limit.

No K5, G3, F9, G8, physical causal-sector selection, complete-QG or new-physics promotion follows.
