# Iter077B-BCH result — source BCH second order selects a nonzero K4 cycle curvature in coordinate scope

**Date:** 2026-09-14

Stable alias: `Iter077B-BCH`.

## Authority

- preregistration: `prereg/ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md`
- prereg commit: `ee7338fc314847a2524544445baf01ea78e87994`
- implementation lineage: `8c43363781fdd450de8396ec2ede0a1602e680a1`
- pre-production predicate repair: `cdba02a770db55b4ff2c1bba5df0cdf49e257951`
- dedicated production workflow launch: `f5ac9f4c45c1460fe75329de244df5c65d406e6b`
- control-only aggregate dependency repair: `88fae05ac2656ece6c3c1529f0e94ce6bd7d296e`
- authoritative retry run: `34785018388`
- jobs: A `103798792269`, B `103798792241`, C `103798792267`, D `103798792182`, aggregate `103798840134`

Artifacts:

- A `10325634912`, `sha256:c89f255656b67998cff17b719c8ad83e68dac7556bbbcd49f549414a28b1936b`
- B `10326690526`, `sha256:14c07a394b1e5f98f2f169c5a629e75103a0e50e4e096e27060825a31f6d3616`
- C `10325689325`, `sha256:364735458b5855cd6eb6702bf8ed9c6568615b26b422b328e1dd6c08a6e49a8a`
- D `10325943462`, `sha256:1bcdb841acab30c38ec30fb05da37271c13297c492aa824dc1644c22cacc2449`
- aggregate `10325634934`, `sha256:c476bd2bd8229a3c4a5343fe09054a7eaad451e1fd968fbb0000c1499d41f3bd`

All frozen scientific lanes A/B/C/D and the aggregate completed successfully on the authoritative retry. The earlier run `34784966067` already had all four scientific lanes PASS; its aggregate failed solely because SymPy was not installed in the aggregate job. No scientific criterion or witness was changed.

## Frozen classification

`ITER077B_SOURCE_BCH_SECOND_ORDER_SELECTS_NONZERO_K4_CYCLE_CURVATURE_EXACT_COORDINATE_SCOPED`

## Exact coordinate result

For source group exponential coordinates

`g_a = exp(X_a)`

and relative variables

`Y_ab = log(g_b^-1 g_a)`,

the BCH expansion is

`Y_ab = X_a - X_b + (1/2)[X_a,X_b] + O(X^3)`.

The linear edge datum is an exact cut/coboundary datum. The second-order commutator term has coefficient `1/2` fixed by the group law, not by a fit.

Across the three frozen exact rational `su(2)` control families and all five K5 root choices:

- every linear datum lies exactly in the K4 cut space;
- the quadratic BCH datum has a nonzero K4 cycle projection for every generic control/root pair;
- the nonzero cycle term scales quadratically under a common rescaling of the node variables;
- it is linear in the symbolic BCH coefficient, fixing the normalization at `1/2` in these coordinates.

For the frozen commuting/collinear control, the quadratic cycle component vanishes exactly for all five roots, as required.

The S4/root covariance lane also passed: cycle membership is preserved under all 24 non-root relabelings, and the canonical tetrahedral Hodge map gives the expected sign-twisted representative.

## Scientific consequence

The symmetry-allowed quadratic-curvature channel found in Iter076R-S is not merely an abstract representation-theoretic possibility: the source group law itself supplies a concrete nonzero second-order cycle-curvature mechanism in exponential relative-coordinate scope.

However, this does **not** identify that coordinate curvature with the physical causal Toller/front-face numerator. The true coherent-spinor source differential from `Iter077A-SM` is rank 10 generically and does not obey the scalar K5 cycle relations. Therefore this BCH result remains a sibling coordinate control until an explicit source/Toller/front-face pushforward composes the two objects.

## Next admissible gate

Keep this result available as a frozen coordinate-side quadratic mechanism. On the source-map critical path, first classify the true nonlinear `B`-map jet at the frozen rank-9 exceptional stratum from `Iter077C-SM`. Only after a source-faithful front-face/full-amplitude pushforward exists may the BCH K4 cycle channel enter a physical reduced numerator or `epsilon^-1` analysis.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical Toller/front-face pushforward; no physical reduced K4 numerator coefficient; no nominal `epsilon^-1` coefficient; no correlated K5 boundary-value theorem; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.