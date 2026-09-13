# Iter077 provenance ledger V2 — post-contact-formula erratum

**Date:** 2026-09-14

This ledger supersedes the source-contact authority assignments in `status/ITER077_PROVENANCE_LEDGER.md`. Historical files remain immutable provenance.

## Authoritative source-map chain

- `Iter077A-SM` — true source B-map transversality: PASS, run `34784565177`.
- `Iter077C-SM` — first full-span rank-9 exceptional stratum: PASS, run `34784868939`.
- canonical mixed rank-9 second-jet result used by the corrected G-SM scaling gate: PASS; six-dimensional transverse quadratic normal form nondegenerate.
- `Iter077G-SM` — **authoritative corrected contact/microlocal/scaling gate**: PASS, run `34785754577`, aggregate artifact `10326159080`, digest `sha256:a3eba270742cd17070c2b6b11f5aff064981412a92f4d3c96d55194c6ea84991`.

## Quarantined historical contact gates

The following source-dependent results are retained only as history and may not be promoted:

- historical `Iter077E-SM` wavefront sibling run `34785411389` using the incorrect Appendix-D transcription;
- historical `Iter077F-SM` scaling sibling run `34785560537` using the same incorrect transcription;
- DSIR V2 handoff run `34785832747` insofar as it depends on those E/F source coefficients.

Their qualitative n=3/scaling conclusion was independently re-tested and recovered by `Iter077G-SM`; their explicit source coefficients are not authoritative.

## Corrected contact authority

Appendix D Eqs. (37)-(39) give, for `j=1/2`,

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

For `rho=gamma/2`:

`A_gamma=-4 i gamma/(1+gamma^2)`,

`C_gamma=-4/(1+gamma^2)`.

The corrected ten-contact Fourier restriction along the frozen rank-9 self-stress is a nonzero cubic for finite real `gamma != 0`, hence `n_eff=3`. The six-dimensional scaling degree is `8`, so scaling alone does not uniquely select the local extension.

Corrected local missing object:

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL`.

## Independent sibling scopes

- `Iter077A-FF`: Toller front-face algebra/data-model sibling.
- `Iter077B-BCH`: source-relative BCH/K4 coordinate sibling, PASS run `34785018388`.

Neither sibling is a physical source-amplitude/K4 pushforward theorem.

## Forward rule

Future handoff/status documents must cite `Iter077G-SM` for the corrected contact formula, wavefront collision and n=3 scaling threshold. Historical E/F may be cited only with `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

No source-map result establishes full correlated K5 boundary value, full-vertex finiteness/divergence, regulator independence, physical source-to-K4 pushforward, nominal epsilon^-1 coefficient, or G3/F9/G8/K5 promotion.