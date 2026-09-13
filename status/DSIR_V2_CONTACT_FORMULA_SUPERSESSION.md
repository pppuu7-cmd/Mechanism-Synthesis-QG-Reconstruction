# DSIR V2 contact-formula supersession

**Date:** 2026-09-14

## Status

`DSIR_TERMINAL_HANDOFF_V2_REFRESH_RESULT` is retained for provenance but is **SUPERSEDED_PRE_ERRATUM / NON_AUTHORITATIVE_FOR_CURRENT_SOURCE_CONTACT**.

## Reason

The V2 audit at run `34785832747` used historical Iter077E-SM / Iter077F-SM source-dependent results that were later quarantined by `status/ITER077_CONTACT_FORMULA_ERRATUM.md` because Appendix D Eqs. (37)-(39) had been transcribed incorrectly.

The invalid historical transcription used `c_n (-1)^(n+1)`. The primary source instead uses `c_(n+1) (-i)^(n+1)`.

Therefore V2's interface logic and G3/F9 preservation audit remain useful control evidence, but its source-contact coefficient and any dependency on the quarantined E/F verdicts may not be promoted.

## Corrected replacement

`Iter077G-SM` prospectively re-ran the corrected source contact and passed:

`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

The corrected local missing object is

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL`.

A V3 terminal handoff must use the corrected G-SM result and must not depend on the quarantined E/F coefficients.

## Claim locks

No K5/G3/F9/G8 promotion; no vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no arbitrary finite part or counterterm.