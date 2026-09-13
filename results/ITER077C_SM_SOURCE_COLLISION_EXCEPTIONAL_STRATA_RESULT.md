# Iter077C-SM result — first true-source rank-9 exceptional stratum is transverse codimension 3

**Date:** 2026-09-14

## Authority

Stable alias: `Iter077C-SM`.

- dependency result: `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`
- prospective preregistration: `prereg/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA.md`
- initial production head: `9cd251318135274b4fd7824f22d95b1bd84869ac`
- control-only source-lock notation repair: `54fe49f1041ef28ac324e2a503196c9b6a6d7ed3`
- authoritative retry/workflow head: `287c22078d275085888c173adfe395fec32bfc98`
- authoritative run: `34784868939`
- jobs: A `103798381892`, B `103798381929`, C `103798381890`, D `103798381793`, aggregate `103798432861`

Artifacts:

- A `10326600574`, `sha256:bc924c635cfd65a4e63065fdcefda9e23247dd92ce67240aa9429b8d15ac2b2b`
- B `10326590624`, `sha256:0c0117280226abea51abb9fff0ee48cb9193f4efed1967f49b8fc0fb43b6e105`
- C `10326307295`, `sha256:4227d5240cc5588be1c8e1e68fae700ad1785c8d89ea2273e69b2f03b47d38ca`
- D `10326585602`, `sha256:ab6d85d16e3a6876fbf93692e7f258b8e3171e38ff8f0a5b2b49754a88490c6d`
- aggregate `10326003230`, `sha256:45179d09f3becdd4b8b385d6ce301eccd43ca7dbd05d9996d3e233c091b1b285`

All frozen lanes A/B/C/D and the aggregate completed successfully on the authoritative retry. The first run `34784819999` is retained as a control-history record: lanes B/C/D succeeded there, while lane A failed only because a machine-readable source-notation lock was absent; no scientific witness or PASS criterion was changed.

## Frozen classification

`ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED`

## Exact source-map result

For the true common-collision differential

`J_(ab),(c,i) = (delta_ac-delta_bc) n_ab^i`,

rank deficiency is equivalent to the existence of a nonzero vector self-stress `lambda_ab` satisfying vector equilibrium at all five K5 nodes. Root equilibrium is redundant after gauge fixing because the five node-equilibrium vectors sum to zero.

The frozen first full-span rank-9 axis witness, selected lexicographically before evaluating transversality, is

`xxxxxyyyzz`

in edge order `01,02,03,04,12,13,14,23,24,34`. It has:

- exact source rank `9`;
- left nullity `1`;
- right nullity `3`;
- exact self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)` satisfying all five vector equilibria;
- structured normal-variation map shape `3 x 20`;
- exact structured-normal rank `3`;
- an explicit nonzero `3 x 3` minor on tangent columns `01:y`, `01:z`, `02:z` with determinant `-1`.

Therefore, at this exact full-span witness, the structured source-normal manifold is transverse to the rank-`<=9` determinantal locus. Locally, the first rank-deficient stratum is a smooth codimension-3 subset of the 20-dimensional normal-direction manifold.

## Exact discrete stress taxonomy

The complete `3^10 = 59049` axis-direction census reproduces Iter077A-SM exactly and resolves it by normal-span dimension and self-stress dimension:

- span 1, rank 4, stress 6: `3`;
- span 2, rank 5, stress 5: `60`;
- span 2, rank 6, stress 4: `330`;
- span 3, rank 6, stress 4: `270`;
- span 2, rank 7, stress 3: `1380`;
- span 3, rank 7, stress 3: `3420`;
- span 2, rank 8, stress 2: `1296`;
- span 3, rank 8, stress 2: `16470`;
- span 3, rank 9, stress 1: `26100`;
- span 3, rank 10, stress 0: `9720`.

The marginal rank histogram is therefore exactly `4:3, 5:60, 6:600, 7:4800, 8:17766, 9:26100, 10:9720`.

This finite axis census is descriptive only; it is not a global continuum-measure theorem.

## Scientific consequence

The generic full-rank source region and the first exceptional source stratum are now sharply separated. The exact rank-9 witness is not a mysterious scalar K5-cycle singularity: it is a true vector self-stress locus and is crossed transversely in three independent normal directions.

This does **not** prove that the source contact-distribution product is harmless on the exceptional set. The next source-map gate must include the true nonlinear `B` jet normal to this frozen rank-9 stratum and test the local pullback/scaling of the source contact distributions. Only after that may a full contracted vertex/regulator-removal or physical source-to-K4 analysis be attempted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no global full-rank theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.