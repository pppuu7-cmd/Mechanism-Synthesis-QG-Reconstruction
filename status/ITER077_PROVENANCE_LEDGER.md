# Iter077 provenance ledger

**Date:** 2026-09-14

This ledger resolves naming collisions and source-formula corrections created by parallel research lanes. Historical filenames, workflow names, JSON labels and run IDs are immutable provenance; stable aliases and authority flags below control future recovery.

## Stable source-map line

### `Iter077A-SM` — true source `B`-map transversality — AUTHORITATIVE PASS

- prereg: `prereg/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md`, commit `f8dbe2d008b46369fb45ef6fc7c5ff887967f299`
- implementation: `distributional/iter077a_true_source_b_map_transversality.py`, commit `e8ddeb1acc6830e6620db02630088eae3b23b2d9`
- run `34784565177`
- result: `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`, commit `fda83125747f530faff264eb6eea3fe4cb4b2f55`
- classification: `ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED`

True coherent-spinor source Jacobian has an exact rank-10 witness; scalar rooted K5 incidence has rank 4 and its six cycle relations do not transfer.

### `Iter077C-SM` — first exceptional source stratum — AUTHORITATIVE PASS

- prereg commit `d2414780967cc36c4b2f31ba4fbcb8453e13f978`
- implementation commit `9c11041e3ce1bce8148452c14e05103e1bed02e0`
- authoritative retry run `34784868939`
- result: `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`, commit `5cdafc091295526f49323f38be13e01dcd553926`
- classification: `ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED`

Frozen witness `xxxxxyyyzz` has rank 9, self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`, and transverse local codimension 3.

### Historical fixed-normal `Iter077D` sibling — AUTHORITATIVE ONLY IN FIXED-NORMAL SCOPE

- result: `results/ITER077D_SM_NONLINEAR_EXCESS_B_JET_RESULT.md`, commit `c9174445f22e6df74a2c41c9cb812900f8fce5de`
- run `34785181275`

This older sibling studies the group-only/fixed-normal right-kernel germ. Its quadratic Hessian has rank 2 with one zero direction; it is not the full mixed normal form. Refer to it as `Iter077D-FN` in prose.

### `Iter077D-SM` — canonical mixed second jet — AUTHORITATIVE PASS

- prereg commit `3dbc24dd5c3dff17c832fe5cbc98d7b456157a27`
- implementation commit `29e3f7a6fe843779061e4431985f4960f7d7a9e2`
- run `34785200044`
- result: `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`, commit `5e12303a074312078db22962dd6eadd288780d9e`
- classification: `ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED`

The full mixed six-dimensional Hessian is nondegenerate, determinant `-1`, inertia `(3+,3-)`.

## Contact-formula source correction

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, commit `eba9976fb7cdc1f7f64852325a35f7c6829a6b0b`, is controlling.

Primary Appendix-D Eq. (37) uses

`c_(n+1) (-i)^(n+1) delta^(n)/(n+1)!`,

not the historical transcription `c_n (-1)^(n+1)`.

Therefore the historical source-dependent E/F gates below are retained for provenance but are **NON_AUTHORITATIVE_SOURCE_LOCK_INVALID**:

### Historical `Iter077E-SM` microlocal run — QUARANTINED

- run `34785411389`
- historical result `results/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION_RESULT.md`

Its qualitative wavefront conclusion is re-tested correctly by `Iter077G-SM`; do not cite the historical E source lock as authority.

### Historical `Iter077F-SM` scaling run — QUARANTINED

- run `34785560537`
- historical result `results/ITER077F_SM_RANK9_CONTACT_SCALING_EXTENSION_RESULT.md`

Its source-dependent contact coefficients are invalid. Scaling-degree mathematics is re-tested correctly by `Iter077G-SM`.

### Historical separate E scaling BLOCKED sibling — valid only as frozen-snapshot acquisition history

The earlier `Iter077E_SM_SOURCE_CONTACT_PULLBACK_SCALING_RESULT.md` correctly reported that its then-frozen repository snapshots lacked an explicit local formula. Primary-source reinspection later acquired Eq. (37)-(39), so this is not the active blocker.

### `Iter077G-SM` — corrected contact/microlocal/scaling gate — AUTHORITATIVE PASS

- corrected source snapshot: `sources/CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_EQ37_39_CORRECTED_SNAPSHOT.md`, commit `edc8bd718c5ac381e26b57636963cfb180f3ecd7`
- prereg commit `e2d3d99be0c2377690494a86556b51a85f106e9f`
- implementation commit `0091d3d730c2ac06fcdd2f82de69cbb212913b63`
- production head `7cdadc77c589fff56650d7bcbc8a6e7ebf9a04dd`
- run `34785754577`
- result: `results/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md`, commit `5c3af58f116d508a20ab7138d46862d954399ad4`
- classification: `ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`

Correct all-spin-half contact:
`delta^(rho,1/2)=-(2 i rho/D)delta-(1/D)delta'`, `D=rho^2+1/4`.
At rank 9 the corrected ten-contact Fourier polynomial has a nonzero degree-3 self-stress restriction. Standard Hörmander termwise pullback fails there; with the canonical six-dimensional quadratic normal form the `n_eff=3` channel has scaling degree 8. This requires a source-selected correlated extension, not an arbitrary finite part.

### `Iter077H-SM` — finite spectral epsilon persistence — AUTHORITATIVE PASS

- source/derived supplement commit `b7abbd430313b0624e1b0dfeb12025f5e8753539`
- prereg commit `cf6620e91ae9ef24091594eed0c1fa81e8829fc8`
- implementation commit `b42272217c22001cbe6c486767e5f2ad5c21a812`
- workflow/production head `24cb5abef3bf0f425b9dcba6eca841cbc8182549`
- run `34785966710`
- aggregate artifact `10326811897`, digest `sha256:e8dd522e9b5af081032bb6a4ee14ad6b1116c7fabf43a5f491e3909afdae4175`
- result: `results/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md`, commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`
- classification: `ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`

For finite spectral `epsilon>0`, the `j=1/2` kernel still contains an epsilon-independent `delta'` coefficient. Exact census over all `2^10=1024` wedge-sign assignments at the frozen control has a nonzero degree-3 rank-9 pure-contact self-stress term in every case. Thus finite epsilon is not a termwise coordinate-space smoothing cure.

## Conditional companion lines

### `Iter077A-FF`
Front-face algebra only; no source-amplitude existence theorem.

### `Iter077B-BCH`
Coordinate-scoped BCH/K4 control; authoritative PASS in its own scope, result commit `a37f21397e41399eddc238e89154aaa5c9b7c094`. No physical source-to-K4 pushforward follows.

## Forward naming rule

- suffix `-SM`: source-map/full-source-amplitude line;
- suffix `-FF`: Toller front-face algebra;
- suffix `-BCH`: source-relative BCH/K4 control;
- historical fixed-normal D sibling is `Iter077D-FN` in prose;
- historical E/F source-dependent gates are quarantined and never regain authority;
- next source-map gate after authoritative `Iter077H-SM` is `Iter077I-SM` unless already occupied.

## Claim firewall

Parallel execution does not merge scopes. No current Iter077 result establishes full source-vertex existence/nonexistence, physical causal-vertex finiteness/divergence, regulator independence, physical source-to-K4 pushforward, nominal `epsilon^-1`, generic finite-spin signed P3, G3/F9/G8/K5 promotion, new physics, or complete QG.