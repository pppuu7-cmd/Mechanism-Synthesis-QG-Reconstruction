# Iter077 numbering and scope correction

**Date:** 2026-09-14

## Canonical reservation

`Iter077A` was already prospectively frozen as:

`prereg/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md`

with source input commit `08499d9cb1bd786adfdd842364606b4517d1962d`.

This canonical reservation predates the later experimental files:

- `prereg/ITER077A_K5_TOLLER_FRONT_FACE_DATA_MODEL.md` at commit `0aa40cc290ec4c2d71e687d95c915f6f473a37cd`;
- `prereg/ITER077B_SOURCE_BCH_K4_CYCLE_CURVATURE.md` at commit `ee7338fc314847a2524544445baf01ea78e87994`;
- experimental workflow `iter077_parallel_frontier_ab.yml` at commit `339c71b2b5e211cbfa61d7613eeccdffe0c7d184`.

The experimental A/B workflow is therefore **non-authoritative for iteration numbering**. Any run from it may be used only as implementation smoke-test evidence and must not be cited as the canonical Iter077 scientific verdict.

## Scientific scope correction

The canonical true source differential is

`J_(ab),(c,i) = (delta_ac-delta_bc) n_ab^i`

with ten wedge-local Bloch directions `n_ab`. The ordinary scalar rooted K5 incidence matrix is recovered only on the special collinear slice where all `n_ab` are the same direction.

Therefore the scalar K5 cut/cycle relations in the experimental front-face preregistration are **not admissible as generic source identities** unless an additional source pushforward theorem is supplied. The experimental front-face gate is superseded rather than silently edited after preregistration.

The BCH relative-coordinate calculation remains mathematically admissible as an explicitly coordinate-scoped control, provided it is renumbered and continues to carry the firewall that it is not the physical Toller/front-face pushforward.

## Canonical ordering from this point

1. `Iter077A`: true source B-map transversality and scalar-surrogate non-transfer — canonical existing preregistration.
2. `Iter077B`: reserved for the next source-faithful object after the Iter077A verdict; if A passes, priority is the rank-deficient exceptional set `Sigma={rank dB<10}` and/or the fully contracted local-limit object required by the A preregistration.
3. `Iter077C`: source BCH quadratic K4 cycle-curvature coordinate control, renumbered without promoting it to a physical source-to-K4 map.

No prior Iter076 result is changed by this correction.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.