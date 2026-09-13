# Iter077 numbering and scope correction

**Date:** 2026-09-14

## Authoritative rule

This note records the historical collision only. The authoritative forward naming/provenance map is now:

`status/ITER077_PROVENANCE_LEDGER.md`.

Do not infer a new scientific ordering from bare historical labels `Iter077A` or `Iter077B`.

## Historical collision

`prereg/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md` was prospectively frozen before the later experimental files

- `prereg/ITER077A_K5_TOLLER_FRONT_FACE_DATA_MODEL.md`;
- `prereg/ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md`;
- `.github/workflows/iter077_parallel_frontier_ab.yml`.

The initial combined A/B workflow is therefore non-authoritative for iteration numbering. Existing frozen filenames and JSON labels remain immutable provenance, but future prose must use stable suffix aliases.

## Stable aliases

- `Iter077A-SM`: true coherent-spinor source `B`-map transversality.
- `Iter077A-FF`: Toller front-face algebra/data-model sibling.
- `Iter077B-BCH`: source-relative BCH/K4 coordinate-curvature sibling.
- `Iter077C-SM`: first true-source exceptional-strata gate.
- `Iter077D-SM`: true-source rank-9 mixed second-jet gate.

The `-SM`, `-FF`, and `-BCH` scopes are independent unless an explicit pushforward theorem is constructed.

## Scientific scope correction retained

The true common-collision source differential is

`J_(ab),(c,i) = (delta_ac-delta_bc) n_ab^i`

with ten wedge-local Bloch directions `n_ab`. The ordinary scalar rooted K5 incidence matrix occurs only on a special collinear-normal slice. Therefore scalar K5 cut/cycle identities are not generic source identities.

`Iter077A-SM` is authoritative for this distinction. `Iter077B-BCH` remains a valid coordinate-scoped sibling because its preregistration explicitly forbids promoting the BCH K4 cycle to a physical Toller/front-face pushforward.

No prior Iter076 result is changed by this correction.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.