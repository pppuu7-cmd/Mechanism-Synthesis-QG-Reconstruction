# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / chain status

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- K5 local amplitude: `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`
- Causal multi-vertex/refinement map: `BLOCKED_MAP_DEFINITION`
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_DEFINED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- **Authoritative active front:** `SOURCE_FAITHFUL_CAUSAL_1TO5_REFINEMENT_MAP / MIXED_A0_L_CLOSURE / UNIQUE_K5_EXTENSION / REGULATOR_INDEPENDENCE`
- Conditional pure-supported control: `SU2_BF_15J_CHANNEL / BF_GAUGE_VOLUME_REGULARIZATION`.
- Conditional companions `TOLLER_FRONT_FACE_ALGEBRA (-FF)` and `SOURCE_BCH_K4_COORDINATE_CONTROL (-BCH)` remain non-authoritative for the physical source amplitude without a bridge theorem.

At the latest recovery read there are no queued or in-progress GitHub Actions. Durable results are authoritative only in their recorded scopes. Historical naming collisions and source-lock quarantines remain governed by `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md`. The latest independent critic handoff is `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`.

## Controlling source-map chain

### Iter077A-SM CLOSED — true-source transversality

Run `34784565177`: exact coherent-spinor source Jacobian has a rank-10 witness; scalar rooted K5 incidence has rank 4 and its six cycle relations do not transfer. Scalar K4/K5 reductions remain conditional without a source pushforward.

### Iter077C-SM CLOSED — rank-9 exceptional source stratum

Run `34784868939`: frozen witness `xxxxxyyyzz` has rank 9, self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`, and transverse codimension 3 in the 20-dimensional wedge-normal manifold.

### Iter077D-SM CLOSED — canonical mixed nonlinear normal form

Run `34785200044`; `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`. Mixed six-dimensional Hessian is nondegenerate, determinant `-1`, inertia `(3+,3-)`. Historical fixed-normal sibling remains `Iter077D-FN` only.

### Contact-formula erratum

Historical source-dependent Iter077E/F runs remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`. Correct source formula at `j=1/2` is

`delta^(rho,1/2)=-(2 i rho/D) delta-(1/D) delta'`, `D=rho^2+1/4`.

### Iter077G-SM CLOSED — corrected contact/scaling

Run `34785754577`, result commit `5c3af58f116d508a20ab7138d46862d954399ad4`.

Classification: `ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

The termwise standard pullback collides at the frozen rank-9 source point; `n_eff=3`; the canonical six-dimensional quadratic normal form has scaling degree 8. This is not a source-ordered vertex nonexistence theorem.

### Iter077H-SM CLOSED — finite one-wedge epsilon is not a termwise cure

Run `34785966710`, aggregate artifact `10326811897`, result commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`. The corrected delta-prime channel survives finite one-wedge spectral epsilon; all `1024/1024` frozen wedge-sign assignments retain the tested pure-contact self-stress contribution.

### Iter077I-SM CLOSED — source-ordered ordinary Toller K5 fails local L1

Run `34786586785`, aggregate artifact `10326812769`, durable result `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.

Classification: `ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`.

All `32/32` all-`j=1/2` boundary components have nonzero exact leading contraction at the frozen source-faithful collision ray; all `512/512` frozen factorized-causal leading contractions survive. Ten wedges give `q=-20` in transverse dimension `d=12`, radial absolute exponent `-9`. This is an exact local-L1 obstruction, not a full distributional divergence theorem.

### Iter077J-SM CLOSED after control-only exact-rank repair

Original run `34788323622` reported modular ranks `9/9/30`, but its exact-rank FAIL was non-authoritative because one-prime rank deficiency does not prove rank deficiency over `Q(i)` and the preregistered exact null witness was missing.

Control-only repair prereg final commit `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`; implementation `d0dbde896462ffa897a918bc80995a7e463e753b`; production head `d9072a636db5ce0a9705f770c92a5876dfc74114`; terminal run `34789579078`; aggregate artifact `10327871709`, digest `sha256:207ce920cb79136dc1f54bb56f8f934c9c1768093ca3e544ef5855b748a79e79`; durable result `results/ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_RESULT.md`, commit `034f14277e4df5589e3f8fa2995283ea4afe8cb9`.

Repaired classification: `ITER077J_SM_FROZEN_MAIN_FULL32_ANGULAR_SPAN_EXACTLY_FAILS_CONTROL_REPAIR_SCOPED`.

Exact main and main+held-out ranks are both `9` over `Q(i)`, nullity `23`, with a verified exact right-null witness. This FAIL applies only to the frozen one-parameter angular family, whose polynomial-degree structure implies rank `<=11`. It does not establish universal boundary-state cancellation and does not affect the Iter077I local-L1 witness.

### Iter077K-SM CLOSED — published source does not define the joint K5 boundary value

Prereg commit `97f0114f80edee3a42f67490f81cb1eb8f497304`; result commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Classification: `ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

The one-wedge spectral Feynman prescription selects individual Toller branches but supplies no joint K5 regulator, finite part, correlated extension, contour, conditional-convergence theorem, or limit/interchange theorem for the non-`L1` product.

### Iter077L-SM CLOSED — extensions exist but are not unique

Prereg `565a36453cf781b1af366da6960ab7f55e6605f1`; result `2da1cce87fb102761d3e2cad83ec93f39ff0f144`.

Classification: `ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`.

The common collision is locally `N=SU(2)^4 subset SL(2,C)^4`, codimension 12. On the source-ordered conic patch transverse scaling degree is 20. Standard submanifold extension theory gives same-scaling-degree local extensions but finite normal-jet freedom through order `8`. Existence is therefore not the blocker; physical/source selection is.

### Iter077M-SM CLOSED — published single-vertex constraints do not select the extension

Prereg `b9af6704336a357dba0b2287b2d7d1320fc020a7`; result `811c84ecdaecf46ba94fde89e8a8fa3a4fe5627e`.

Classification: `ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`.

A concrete family `A_ext,c=A_ext+c F_SU2 delta_N` preserves the off-collision source object, global gauge structure, true spin/intertwiner boundary data, fixed causal labels and maximal transverse scaling degree. The published single-vertex source contains no condition fixing `c`.

Independent critic control `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`, commit `ba2d013d5c0d3889e94b3f120cba031e2f8b4ce9`, verifies the compact coefficient is a nonzero functional on the complete frozen 32-dimensional boundary basis (`16/32` nonzero at the identity compact connection).

### Iter077N-SM CLOSED — ambiguity survives integrated vertex; ordinary gluing does not select it

Authoritative run `34789869127`, production head `7b12b0f8207d129ffd9b79bda158db77e265f8f6`, aggregate artifact `10328420436`, digest `sha256:04fecbabcdf0db984665da0220bf2e1499b9ccaf911e721e721471a4284bddd3`; result commit `03407a010f96e5d81af9813756d21fca6ffcda32`.

Classification: `ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`.

Exact all-32 compact K5 census gives `16/32` nonzero integrated boundary functionals. Ordinary two-vertex state-sum contraction propagates `A_c=A_0+cL` but supplies no independent equation selecting `c`.

Critic review commit `604ececa716c057e62ee325b7e80b7cf7bb9f591` confirmed this only in standard-gluing scope. Exact critic branch-cube control `64e364df099f879b876d10a2d4653c21ddf12d4d` shows `T^+ + T^- = D` and the full independent-sign EPRL sum can remain unchanged while every factorizable causal K5 sector retains the supported coefficient.

## Refinement / RG front

### Iter078A-RG CLOSED — general RG framework exists, causal-Toller map missing

Prereg `97257d6830f1a386f9df3a854391e4e86e340884`; source audit `377e78d6b954003354f2a73ecf95b34f70e97109`; result `728d6e3f40a1797247c2b32a652a2c2d67cb5310`.

Classification: `ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`.

Verdict: `BLOCKED_MAP_DEFINITION`. Background-independent spin-foam consistent-boundary/RG frameworks exist, but CRQN v0.2 / the causal-Toller source defines only a single causal vertex. The source does not supply the same-boundary coarse/fine complex pair, causal fine face/edge measure, boundary embedding/projection, fixed-point equation, or transport law for the Iter077 extension freedom.

This means no BF, EPRL, hypercuboidal, tensor-network or other external refinement measure may be silently treated as the already-defined CRQN RG map.

### Iter078B-RG CLOSED — causal 1-to-5 orientation combinatorics are not the blocker

Prereg `6f4360ca249c1b5ad9c6b1bd78c9be747be24acd`; implementation `a5d14bf75920c38a0c46106731c76ca65e2ebe07`; production head `047b19fe75630a88aac3f0b783e34198756e6f05`; terminal run `34790158373`; aggregate artifact `10328585276`, digest `sha256:db941e5cbf45e8f89012a8a7b0cef9568d3c289544c4b98a8027bb36f7d9a566`; result `4d4ae20ca3ace6ec37d176ebf1afbf97804513cb`.

Classification: `ITER078B_RG_1TO5_CAUSAL_BOUNDARY_ORIENTATIONS_EXTEND_TO_FINE_ACYCLIC_K5_ALL32_EXACT_COMBINATORIAL_SCOPED`.

All `32/32` coarse causal boundary sign patterns admit compatible acyclic internal K5 orientations. Counts are exactly `p!(5-p)!`. Therefore the minimal 1-to-5 refinement is not blocked by causal partial-order combinatorics. This does not define the refined amplitude/measure or RG map.

### Iter078C-RG CLOSED — local supported tensor is BF 15j; RG interpretation QUALIFIED

Prereg `bef22c39989905373c95bf49c666584dc898176e`; source/theorem derivation `b531e3d9a2f5e0c9422b170cc220ae9890c0f71e`; result `1eb593fdc97b46e3a2cc41e4ac568274e1c3b1c8`.

Research classification: `ITER078C_RG_SUPPORTED_K5_AMBIGUITY_IS_SU2_BF_15J_CHANNEL_REFINEMENT_STABLE_UP_TO_BF_GAUGE_NORMALIZATION_EXACT_THEOREM_SCOPED`.

Adversarial qualification: `results/ITER078C_ADVERSARIAL_QUALIFICATION.md`, commit `6206080d12a629bf9cca9b7084d8e8e03a843ecb`; critic handoff commit `d427f1777b0c90b2bc43e37b1796d81ee14b1604`; verdict `QUALIFIED`.

Accepted exact/scoped core: the compact supported K5 boundary tensor `F_SU2` is the SU(2) Ooguri/BF 15j vertex tensor up to nonzero basis normalization/sign conventions. Under **standard BF internal sums/weights**, the pure-`L` multi-vertex sector is the Ooguri BF state sum up to `c^V`, basis normalization and BF gauge-volume factors.

Critical scope lock: the BF weights are not the source-defined causal-Toller refinement map. Iter078A established that that map/measure is absent. Therefore `Fine[L^5]=K_BF L` and `c=K_BF c^5` are conditional pure-BF control equations, not yet CRQN RG equations. A non-BF causal face/edge measure need not preserve the BF Pachner identity. Mixed `A_0/L` sectors remain unresolved. The full Iter077L normal-jet ambiguity space is larger than one scalar `c`.

### Iter078D-RG PREREGISTERED — pure-BF c^5 gauge-volume control only

Prereg `prereg/ITER078D_RG_BF_CHANNEL_1TO5_GAUGE_VOLUME.md`, commit `71a8c52bbc2b46a83ebb3f57908e1a4e028261a8`.

This gate may be used as a **conditional BF regulator/control theorem**: under standard BF internal weights, isolate the formal `c^5` coefficient and audit the known 1-to-5 gauge-volume divergence. It is not authorized to relabel that BF-weighted coefficient as the actual causal-Toller refinement map, because the latter remains `BLOCKED_MAP_DEFINITION`.

A PASS can establish only that the BF-weighted pure-supported coefficient requires gauge fixing/regulation before a finite `K_BF` is assigned. It cannot select `c`, close mixed sectors, establish an RG fixed point, or repair the missing causal multi-vertex measure.

## Exact blocker

The fixed-causal K5 vertex is locally extendible but nonunique. At least one supported ambiguity direction survives the integrated boundary functional and is locally identifiable with an SU(2) BF 15j tensor. Ordinary gluing and the published single-vertex constraints do not select its coefficient.

The controlling missing object has moved to:

`SOURCE_FAITHFUL_CAUSAL_1TO5_AMPLITUDE_MEASURE_EMBEDDING_PROJECTION_AND_MIXED_EXTENSION_CLOSURE_MAP`.

Status remains `BLOCKED_MAP_DEFINITION / BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.

The order-8 Iter077L result denotes maximal normal-jet order, not eight scalar couplings. Any future RG truncation must justify how the full allowed supported jet/function freedom is projected into a finite coupling space.

## Exact next admissible gate

Highest-information physical gate: prospectively define one explicit causal 1-to-5 multi-vertex prescription, with:

1. fine face/edge weights and internal spin/intertwiner sums;
2. per-vertex gauge fixing and treatment of BF/redundant gauge volume where relevant;
3. causal orientation sum/selection using the Iter078B-compatible fine patterns;
4. same-boundary embedding map;
5. coarse projection/matching functional;
6. regulator path;
7. explicit transport/projection of the Iter077 extension ambiguity space.

If no source-backed prescription exists, any Lorentzian EPRL-like choice must be versioned as new independently motivated CRQN structure rather than attributed to the original causal source.

Once frozen, expand `A_c=A_0+cL` over the five fine vertices. A finite-spin mixed sector producing a coarse boundary tensor outside the proposed `{A_0,L}` span is a decisive FAIL of one-parameter closure and requires an enlarged coupling space before any fixed-point search.

Pure-BF gauge-volume calculations such as Iter078D are useful conditional controls but are not a substitute for this mixed source-faithful map/closure test.

Only after a unique local amplitude and a mathematically defined refinement map are established may regulator independence, G3 and continuum RG be promoted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no full-amplitude causal divergence/nonexistence theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no CRQN RG fixed point; no `K_BF=1`; no G3 PASS or F9/G8/K5 promotion. Retain the published one-wedge spectral `i epsilon`; do not reinterpret it as a joint K5 regulator.