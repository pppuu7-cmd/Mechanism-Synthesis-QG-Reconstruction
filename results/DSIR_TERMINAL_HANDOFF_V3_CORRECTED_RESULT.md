# DSIR terminal handoff V3 — corrected source-contact authoritative result

**Date:** 2026-09-14

## Authority

- prospective preregistration: `prereg/DSIR_TERMINAL_HANDOFF_V3_CONTACT_ERRATUM_CORRECTED.md`
- corrected funnel specification: `docs/DSIR_TO_POLYGON_FUNNEL_V0_3.md`
- source-contact erratum: `status/ITER077_CONTACT_FORMULA_ERRATUM.md`
- V2 supersession notice: `status/DSIR_V2_CONTACT_FORMULA_SUPERSESSION.md`
- corrected provenance ledger: `status/ITER077_PROVENANCE_LEDGER_V2.md`
- implementation: `analysis/dsir_terminal_handoff_v3_corrected_audit.py`
- production/workflow head: `84540a7e786664339b02f16c23325b9cff7ac60c`
- authoritative run: `34786009031`
- jobs: R3 `103801500758`, S3 `103801500674`, T3 `103801500808`, U3 `103801500827`, aggregate `103801524647`

Artifacts:

- R3 `10326388709`, `sha256:a5fd15c24149fc6be556ddcb0dc9317abe95031bd5060a48fac169ed81b371d0`
- S3 `10326272550`, `sha256:8433dc9307983ea0b75100c8b0a53a20d73b03e8dcb43d0717f158994f2c138e`
- T3 `10326154403`, `sha256:241c0a7cd3f30109421d5f2fb36114f2e76799cff4a602b098b062700edf71a9`
- U3 `10326856247`, `sha256:de43d5bab4bf19fcc1baea24ff7e8068b9133c4c37619fcaacbc6e6df44db351`
- aggregate `10326199488`, `sha256:13fbcfee0d8e2d3baed22d7933b162484bac73732ca08884ab03a832cbd25d8e`

All four frozen V3 lanes and the aggregate passed.

## Frozen classification

`DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V3_CONTACT_FORMULA_CORRECTED`

`contract_completeness_percent = 100`

Meaning: **100% handoff-contract/interface completeness only; no physical gate promotion.**

## Source-contact correction absorbed

Historical Iter077E-SM / Iter077F-SM source-dependent verdicts and the pre-erratum DSIR V2 handoff are retained only as quarantined provenance. They may not be used for current source-contact coefficients.

Current source-contact authority is the prospectively corrected `Iter077G-SM` result:

`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

For `j=1/2`:

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

For `rho=gamma/2`:

`A_gamma=-4 i gamma/(1+gamma^2)`,

`C_gamma=-4/(1+gamma^2)`.

Along the frozen rank-9 self-stress ray,

`P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2(gamma-t)`,

which is a nonzero cubic for finite real `gamma != 0`. Therefore the corrected highest conormal order remains `n_eff=3`. In the exact six-dimensional transverse quadratic normal form, its scaling degree is `8`, so scaling degree alone does not select a unique extension.

This result supersedes the incorrect historical E/F coefficients while preserving the independently re-tested qualitative blocker.

## V3 lane verdicts

- R3 — corrected distributional/K5 handoff: `PASS`
- S3 — finite-scale dynamics/G3 preservation: `PASS`
- T3 — RG/CCI/F9 preservation: `PASS`
- U3 — corrected provenance/no-hidden-choice audit: `PASS`

## Terminal polygon transfers

### K5 / distributional source amplitude

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

First corrected local missing object:

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL`

Broad missing object:

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION`

Polygon test:

1. derive the exceptional correlated extension from the original published spectral `i epsilon` prescription;
2. forbid arbitrary fitted finite parts/counterterms;
3. include exact smooth Toller factors/phases, CP1 measure, shared group variables and boundary intertwiners;
4. test whether the corrected `n_eff=3` channel survives, cancels, or is uniquely fixed after full correlated contraction;
5. cover the remaining rank-deficient source strata;
6. distinguish distributional existence, extension uniqueness, absolute integrability and regulator removal;
7. only after these tests classify physical K5 or any full-vertex finiteness/divergence statement.

### G3 / finite-scale quantum dynamics

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

Missing object:

`CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION`

### F9 / RG-CCI

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

Missing object:

`PHYSICAL_MULTISCALE_CCI_REALIZATION`

### G8

Status:

`CONVERGENCE_ONLY`

## Independent sibling exports

Iter076X-Y-Z front-face results remain exported as non-scalar Toller bundle/connection constraints.

`Iter077B-BCH` remains an independent coordinate-scoped derived control with exact second-order BCH coefficient `1/2`; it is not a physical coherent-spinor/Toller source-to-K4 pushforward theorem.

## DSIR -> Polygon decision

The DSIR funnel is now terminally complete at V3 under the frozen 100% interface-completeness definition. The corrected handoff contains no anonymous dependency and no hidden source-contact convention. Further work on the named K5, G3 and F9 objects belongs to the polygon as separate falsifiable workstreams rather than to an ever-expanding DSIR funnel.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no K5/G3/F9/G8 promotion; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no generic finite-spin signed P3; no arbitrary finite part/counterterm/fitted cancellation/preferred sequential order; retain the published spectral `i epsilon`.