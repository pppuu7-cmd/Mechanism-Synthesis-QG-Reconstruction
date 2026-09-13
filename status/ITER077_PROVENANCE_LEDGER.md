# Iter077 provenance ledger

**Date:** 2026-09-14

This ledger resolves naming collisions, source-formula corrections, control-only repairs, and authority scope created by parallel research lanes. Historical filenames, workflow names, JSON labels and run IDs are immutable provenance; the authority flags below control future recovery.

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
- result `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`, commit `5cdafc091295526f49323f38be13e01dcd553926`
- classification `ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED`

Frozen witness `xxxxxyyyzz` has rank 9, self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`, and transverse local codimension 3.

### Historical fixed-normal `Iter077D` sibling — AUTHORITATIVE ONLY IN FIXED-NORMAL SCOPE

- result `results/ITER077D_SM_NONLINEAR_EXCESS_B_JET_RESULT.md`, commit `c9174445f22e6df74a2c41c9cb812900f8fce5de`
- run `34785181275`

This older sibling studies the group-only/fixed-normal right-kernel germ. Its quadratic Hessian has rank 2 with one zero direction; it is not the full mixed normal form. Refer to it as `Iter077D-FN` in prose.

### `Iter077D-SM` — canonical mixed second jet — AUTHORITATIVE PASS

- prereg commit `3dbc24dd5c3dff17c832fe5cbc98d7b456157a27`
- implementation commit `29e3f7a6fe843779061e4431985f4960f7d7a9e2`
- run `34785200044`
- result `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`, commit `5e12303a074312078db22962dd6eadd288780d9e`
- classification `ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED`

The full mixed six-dimensional Hessian is nondegenerate, determinant `-1`, inertia `(3+,3-)`.

## Contact-formula source correction

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, commit `eba9976fb7cdc1f7f64852325a35f7c6829a6b0b`, is controlling.

Primary Appendix-D Eq. (37) uses `c_(n+1) (-i)^(n+1) delta^(n)/(n+1)!`, not the historical transcription `c_n (-1)^(n+1)`.

Therefore the historical source-dependent E/F gates are retained for provenance but are **NON_AUTHORITATIVE_SOURCE_LOCK_INVALID**.

### Historical `Iter077E-SM` microlocal run — QUARANTINED

- run `34785411389`
- historical result `results/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION_RESULT.md`

Its qualitative wavefront conclusion is re-tested correctly by Iter077G; do not cite its source lock as authority.

### Historical `Iter077F-SM` scaling run — QUARANTINED

- run `34785560537`
- historical result `results/ITER077F_SM_RANK9_CONTACT_SCALING_EXTENSION_RESULT.md`

Its source-dependent contact coefficients are invalid. Scaling-degree mathematics is re-tested correctly by Iter077G.

### Historical separate E scaling BLOCKED sibling

The earlier `Iter077E_SM_SOURCE_CONTACT_PULLBACK_SCALING_RESULT.md` remains valid only as frozen-snapshot acquisition history. Primary-source reinspection later acquired the missing formula.

### `Iter077G-SM` — corrected contact/microlocal/scaling gate — AUTHORITATIVE PASS

- corrected source snapshot commit `edc8bd718c5ac381e26b57636963cfb180f3ecd7`
- prereg `e2d3d99be0c2377690494a86556b51a85f106e9f`
- implementation `0091d3d730c2ac06fcdd2f82de69cbb212913b63`
- production head `7cdadc77c589fff56650d7bcbc8a6e7ebf9a04dd`
- run `34785754577`
- result `results/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md`, commit `5c3af58f116d508a20ab7138d46862d954399ad4`
- classification `ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`

Correct all-spin-half contact is `delta^(rho,1/2)=-(2 i rho/D)delta-(1/D)delta'`. Standard termwise pullback fails at the frozen rank-9 source point; source-selected correlated extension remains required.

### `Iter077H-SM` — finite spectral epsilon persistence — AUTHORITATIVE PASS

- source/derived supplement commit `b7abbd430313b0624e1b0dfeb12025f5e8753539`
- prereg `cf6620e91ae9ef24091594eed0c1fa81e8829fc8`
- implementation `b42272217c22001cbe6c486767e5f2ad5c21a812`
- production head `24cb5abef3bf0f425b9dcba6eca841cbc8182549`
- run `34785966710`
- aggregate artifact `10326811897`, digest `sha256:e8dd522e9b5af081032bb6a4ee14ad6b1116c7fabf43a5f491e3909afdae4175`
- result `results/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md`, commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`
- classification `ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`

Finite one-wedge spectral epsilon does not legalize the termwise K5 pullback.

## Source-ordered K5 continuation

### `Iter077I-SM` — source-ordered Toller K5 local L1 — AUTHORITATIVE PASS IN SCOPED NEGATIVE-INTEGRABILITY STATEMENT

- source freeze `f7f0a957e7a0379be39f164bd6903a6e78425f95`
- prereg `c30f1556ad5d0bc92fac3be91b31c052f789cb63`
- implementation `53beff1f12bd78921ecd8a203a8786982ad6f414`
- first workflow head `eadf5b51977a7b2e27c633cbc0658cf008d057d2`, run `34786550378`, execution-invalid aggregate because a machine-readable source-order string lock failed
- control-only source-order alias `102fc7268b732bead5dfcf6d61fe4479ae1d3030`, authoritative run `34786586785`
- aggregate artifact `10326812769`, digest `sha256:b9e7d617598acaeb60ee7018e3ee4f78a232b32be86b112da4713352d9797887`
- durable result `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`, commit `6e1dd1e6bb5e26d607e2c249ff6f8978f0df922a`
- classification `ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`

All 32 minimal-sector boundary components are nonzero at the frozen exact collision witness; the source-ordered leading K5 product has `q=-20` in `d=12` and is not locally absolutely integrable. This is not a distributional nonexistence theorem.

### `Iter077J-SM` — full-32 angular-span hypothesis — AUTHORITATIVE SCIENTIFIC FAIL AFTER CONTROL-ONLY REPAIR

Original line:
- prereg `e5aae441c84a5d458e1d91dd1f64ab160043dd35`
- implementation `df951850617eb9683a3a6b42fe6cdb4e1b3b1fd6`
- workflow head `47065cdf518c9984f01cd1ee7e43818ea4dc6ba9`
- run `34788323622`

The original aggregate reported modular ranks `9/9/30`, but its exact-rank FAIL was non-authoritative because rank deficiency modulo one prime does not prove characteristic-zero rank deficiency and the preregistered exact null witness was not emitted.

Control-only repair:
- prereg initial `cc4bde6751e5a353f55d4b04f8fbcea3dc5453a0`, final frozen correction `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`
- implementation `d0dbde896462ffa897a918bc80995a7e463e753b`
- production head `d9072a636db5ce0a9705f770c92a5876dfc74114`
- terminal run `34789579078`
- aggregate artifact `10327871709`, digest `sha256:207ce920cb79136dc1f54bb56f8f934c9c1768093ca3e544ef5855b748a79e79`
- durable result `results/ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_RESULT.md`, commit `034f14277e4df5589e3f8fa2995283ea4afe8cb9`
- repaired classification `ITER077J_SM_FROZEN_MAIN_FULL32_ANGULAR_SPAN_EXACTLY_FAILS_CONTROL_REPAIR_SCOPED`

Exact main and combined ranks are `9` over `Q(i)`, nullity `23`, with exact right-null witness verified. The FAIL is **only** for the frozen one-parameter angular family; no universal boundary-state cancellation is established. Lane-D modular rank 30 at four primes is not promoted to an exact deficiency claim.

### `Iter077K-SM` — joint K5 object definition — AUTHORITATIVE BLOCKED

- prereg `97f0114f80edee3a42f67490f81cb1eb8f497304`
- result `results/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION_RESULT.md`, commit `898355bea286d6a64934ea20c95711aa4e408b3d`
- classification `ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`

The source one-wedge Feynman prescription does not itself define a unique joint K5 boundary value after the non-L1 product is formed.

### `Iter077L-SM` — transverse extension theorem — AUTHORITATIVE PASS IN THEOREM SCOPE

- prereg `565a36453cf781b1af366da6960ab7f55e6605f1`
- source/theorem derivation `1a6cb5331098287823e55c7db5452a976b8501a5`
- result `results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md`, commit `2da1cce87fb102761d3e2cad83ec93f39ff0f144`
- classification `ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`

For `N=SU(2)^4 subset SL(2,C)^4`, codimension 12, the source-ordered component has transverse scaling degree 20 on the frozen conic patch. Same-scaling-degree extensions exist but are nonunique through normal-jet order 8.

### `Iter077M-SM` — published symmetry selector — AUTHORITATIVE PASS IN NON-SELECTION SCOPE

- prereg `b9af6704336a357dba0b2287b2d7d1320fc020a7`
- source derivation `3bd388c143030e8947ca1a206e907027e0dd2362`
- result `results/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR_RESULT.md`, commit `811c84ecdaecf46ba94fde89e8a8fa3a4fe5627e`
- classification `ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`

The explicit supported direction `F_SU2 delta_N` preserves the frozen published single-vertex constraints and leaves a free coefficient.

Independent critic compact-boundary control: `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`, commit `ba2d013d5c0d3889e94b3f120cba031e2f8b4ce9`, independently finds `16/32` nonzero complete-boundary values.

### `Iter077N-SM` — integrated ambiguity survival / ordinary gluing — AUTHORITATIVE PASS, CRITIC CONFIRMED_SCOPED

- prereg `ee08121c94fd802f9111313d6f089fbf2ab10181`
- source lock `3543b523595b9b4d239866423ff279ae28f7236c`
- implementation `aa7440a939941b5bdde4e6f5c07f8f63ddfe8562`
- production head `7b12b0f8207d129ffd9b79bda158db77e265f8f6`
- terminal run `34789869127`
- aggregate artifact `10328420436`, digest `sha256:04fecbabcdf0db984665da0220bf2e1499b9ccaf911e721e721471a4284bddd3`
- result `results/ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING_RESULT.md`, commit `03407a010f96e5d81af9813756d21fca6ffcda32`
- classification `ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`

Exact all-32 compact K5 census gives 16 nonzero integrated boundary functionals. Ordinary bilinear/multilinear state-sum contraction propagates `A_c=A_0+cL` and is not itself a c-independent selector.

Adversarial review: `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, commit `604ececa716c057e62ee325b7e80b7cf7bb9f591`, verdict `CONFIRMED_SCOPED`.

Exact critic branch-cube control: `results/ITER077N_ADVERSARIAL_BRANCH_CUBE_CONTROL.md`, commit `64e364df099f879b876d10a2d4653c21ddf12d4d`. The deformation `Delta A_kappa=C(prod_e kappa_e)F_SU2 delta_N` preserves every additive one-wedge `T^++T^-=D` control and the full independent-sign EPRL sum, while every source-factorizable causal K5 pattern has `prod_(a<b)kappa_ab=+1` and retains the same coefficient. Thus known source additive branch identities do not select the ambiguity.

Scope qualification: this excludes **ordinary state-sum contraction alone**, not every future causal refinement/composition/RG law.

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
- historical E/F source-dependent gates remain quarantined permanently;
- `Iter077J` original modular run and its exact-rank control repair must both be cited when discussing J;
- after Iter077N the next authoritative layer is no longer another local Iter077 collision lemma: the prospectively opened gate is `Iter078A-RG` refinement-map definition.

## Claim firewall

Parallel execution does not merge scopes. No Iter077 result establishes a unique full source vertex, a physical causal-vertex finiteness/divergence theorem, regulator independence, a physical source-to-K4 pushforward, nominal `epsilon^-1`, generic finite-spin signed P3, G3/F9/G8/K5 promotion, new physics, or complete QG. Standard state-sum gluing is not a selector of the supported extension coefficient; stronger future refinement/RG consistency remains open.