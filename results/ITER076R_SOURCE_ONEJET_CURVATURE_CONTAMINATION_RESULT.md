# Iter076R result — Haar one-jet zero, quadratic-curvature contamination channel allowed

**Date:** 2026-09-13

## Authority

- prospective preregistration: `3c6c179aeea5bafa02c986b0cd6a197b65f4e24e`
- implementation: `7df31825ebef196d18d88b9aa91889fa7dc4c699`
- initial workflow: `0d9be99d2cee722302afbec15e9a0fe5cdbe5b2a`
- control/provenance-only repair: `1f7971e547f04fbe95809f356b0a6e4a7fa50dd0`
- authoritative retry run: `34782351018`
- aggregate job: `103791710390`

Artifacts:

- A: `10325462428`, digest `sha256:0302ce05178f88f6ab259dcaa16621ee72850fcd6a003835a1a87ff7792638c2`
- B: `10325437544`, digest `sha256:c194bc747a2d17d0b04903d8193d328beefa5508a3d3420ee0cabe9d169c7793`
- C: `10325128017`, digest `sha256:630c534b562382ffe58814e74ed000e0d08d5230c96200f2fd824eda0abe8c9b`
- D: `10324429196`, digest `sha256:8bf3bfc0af857147f4487f16695f3f3f9ab8fa0968ee4c055d55e4edcf6ebcbb`
- aggregate: `10325685566`, digest `sha256:10707a2a9207e20488644bce0ba3861c8db8216cc2f9ffc2dc51b3f151e1c3c6`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER076R_HAAR_ONEJET_ZERO_BUT_SYMMETRY_ALLOWS_NONLINEAR_QUADRATIC_CURVATURE_SOURCE_NUMERATOR_ONEJET_STILL_REQUIRED_EXACT_SCOPED`

## Exact content

1. The source-domain local Haar/KAK radial factor has vanishing one-jet exactly at the identity. This is the already source-backed evenness of `(sinh beta / beta)^2` and does not extend automatically to the full Toller/intertwiner numerator.
2. The exact twisted quadratic-curvature Hom space compatible with the K4 cut/cycle representations has dimension exactly `1`.
3. A nonzero exact contamination witness exists for a generic one-jet. Therefore S4/twisted-Hodge symmetry does not force nonlinear-map one-jet contamination to vanish.
4. The known exact Toller conjugation mechanism from Iter076P cannot be used to impose same-causal numerator evenness, because its all-wedge branch flip exits the source causal K5 image.

## Scientific consequence

The Haar contribution to the source one-jet is closed: it is zero in the frozen local radial coordinate. The full Toller/intertwiner numerator one-jet is not closed. Since symmetry permits a nonlinear quadratic curvature channel, a nonzero full source one-jet could feed the degree-two coefficient.

This gate does not prove that the physical source-to-K4 map realizes nonzero curvature. It establishes only that symmetry cannot be used to bypass the missing source numerator one-jet.

## Relation to the later face-survival follow-up

A later, more restrictive confirmatory gate was accidentally preregistered under the same iteration letter after this R preregistration already existed. That follow-up tests whether the allowed contamination survives the exact Iter073/076B transitive proper-face complex. It must be treated as the next iteration and is being administratively renumbered without changing its frozen scientific predictions.

## Next admissible gate

Test the symmetry-allowed contamination against the exact transitive proper-face restriction complex. If it survives, derive or source-audit the full Toller/intertwiner numerator one-jet and actual nonlinear source-to-K4 curvature before forming any physical degree-two coefficient.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical nonlinear source-to-K4 map; no physical full numerator one-jet; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` prescription.