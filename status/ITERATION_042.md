# Iteration 042 — Appendix-D source-supported primitive jets and S5 invariant-ring fingerprint

Status: **TERMINAL / SOURCE SUPPORT STRONGLY REDUCES BUT DOES NOT FIX EXTENSION AMBIGUITY**

Date: 2026-09-12

## Authoritative computations

- Iter042A source-span run: `34695777621`, merge commit `9e359c291ec4738420ad771ed2d0bd424ea56447`, **14/14 SUCCESS**.
- Iter042B Molien/plethystic run: `34695777605`, same merge commit, **3/3 SUCCESS**.

All numerical subspace-containment, character-dimension and integrality gates passed.

## Iter042A result — edge-local j=1/2 source span

For j=1/2, Appendix D permits at most one derivative from each wedge. S5 Reynolds averages of square-free products of the ten projected K5 edge derivative directions were compared with the exact S5 primitive quotient modulo descendants of the unique quadratic invariant.

Both independent evaluation seeds agree on the checked ranks; in particular seed 29 reproduces the strong-deficit cases d=8 and d=10.

| degree d | exact primitive quotient | edge-local source primitive rank | coverage |
|---:|---:|---:|---:|
| 2 | 0 | 0 | n/a |
| 4 | 3 | 3 | 100% |
| 6 | 5 | 3 | 60% |
| 7 | 2 | 0 | 0% |
| 8 | 11 | 1 | 9.09% |
| 9 | 7 | 0 | 0% |
| 10 | 18 | 0 | 0% |

Independent seed-29 raw examples:

- d6: source primitive rank `3/5`, artifact `10299151321`;
- d8: source primitive rank `1/11`, artifact `10298429884`;
- d10: source primitive rank `0/18`, artifact `10297838824`.

Therefore the simplest edge-local Appendix-D derivative budget removes most symmetry-allowed primitive ambiguities at higher degree. But source compatibility does not select the remaining coefficients, and correlated finite-epsilon/analytic information could in principle generate structures outside this square-free edge-local closure.

## Iter042B result — S5 invariant-ring fingerprint

Hilbert coefficients were computed consistently through truncations 24, 32 and 40. The degree-40 sequence begins

`[1,0,1,0,4,0,9,2,20,9,38,23,74,51,125,101,211,...]`

and agrees with Iter039/040 on all overlapping degrees.

The truncated plethystic logarithm has first positive coefficients

- d2 `+1`, d4 `+3`, d6 `+5`, d7 `+2`, d8 `+5`, d9 `+7`, d10 `+3`, d11 `+8`,

with the first negative/relation-like coefficient at d12 (`-4`). This is a generator/relation fingerprint only, not a proof of a minimal invariant-ring presentation.

## Scientific classification

`EDGE_LOCAL_APPENDIXD_SOURCE_REDUCES_PRIMITIVE_AMBIGUITY = TRUE`.

`EDGE_LOCAL_APPENDIXD_SOURCE_UNIQUELY_SELECTS_EXTENSION = FALSE`.

`S5_INVARIANT_RING_IS_QUADRATICALLY_GENERATED = FALSE`.

The next allowed gate is source-faithful Feynman selection on the reduced source-compatible space, beginning with finite-spectral-i-epsilon one-wedge identities and the simplest cyclic K3 joint/contact structure before attempting a K5 extension.

## Claim locks

- no multi-wedge product is defined by this iteration;
- no arbitrary finite part/counterterm is authorized;
- no causal-vertex finiteness/divergence theorem;
- no G3/F9/G8 promotion.
