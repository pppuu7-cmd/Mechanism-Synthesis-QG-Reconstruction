# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / authoritative front

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`).
- Established/source-backed mechanism union: `F1-F8`.
- Physical F9: `BLOCKED`.
- K5 local amplitude: `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.
- Causal multi-vertex/refinement map: `BLOCKED_MAP_DEFINITION`.
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_DEFINED`.
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`.
- **Authoritative active front:** `SOURCE_FAITHFUL_CAUSAL_1TO5_AMPLITUDE_MAP / MIXED_A0_L_CLOSURE / UNIQUE_K5_EXTENSION / REGULATOR_INDEPENDENCE`.
- **Conditional control front:** `SU2_BF_15J_PURE_SUPPORTED_CHANNEL / BF_1TO5_GAUGE_VOLUME_REGULARIZATION`.

At the latest recovery read there are no queued or in-progress GitHub Actions. `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remain controlling for historical naming/source-lock issues. Historical Iter077E/F source-dependent runs remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

Latest independent review: `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, verdict `QUALIFIED` on Iter078D-RG.

## Controlling source-amplitude chain

### Iter077A/C/D/G/H — CLOSED in recorded scopes

Authoritative source-map results remain as recorded in `status/ITER077_PROVENANCE_LEDGER.md`:

- Iter077A: true coherent-spinor source Jacobian has an exact rank-10 witness; scalar rooted K5 incidence rank 4 and its cycle relations do not transfer.
- Iter077C: first frozen rank-9 exceptional source stratum is transverse codimension 3.
- Iter077D-SM: canonical mixed six-dimensional second jet is nondegenerate, determinant `-1`, inertia `(3+,3-)`; fixed-normal sibling remains `Iter077D-FN` only.
- Correct `j=1/2` contact after erratum: `delta^(rho,1/2)=-(2 i rho/D)delta-(1/D)delta'`, `D=rho^2+1/4`.
- Iter077G/H: corrected contact channel survives the relevant frozen rank-9/scaling and finite-one-wedge-epsilon controls; none of this is a source-ordered full-vertex nonexistence theorem.

### Iter077I-SM — source-ordered K5 ordinary local L1 obstruction CLOSED

Authoritative run `34786586785`; aggregate artifact `10326812769`; durable result `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.

Classification:
`ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`.

All `32/32` all-`j=1/2` boundary components and all `512/512` frozen factorized-causal leading contractions survive at the frozen source-faithful collision witness. Ten wedges give homogeneous power `q=-20` in transverse dimension `d=12`, so the source-ordered leading product is not locally absolutely integrable. This is not a full distributional divergence/nonexistence theorem.

### Iter077J-SM — frozen angular-span hypothesis FAIL confirmed after control-only repair

Original modular run `34788323622` was insufficient for an exact rank-deficiency theorem. Control-only exact repair: prereg final commit `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`; implementation `d0dbde896462ffa897a918bc80995a7e463e753b`; terminal run `34789579078`; aggregate artifact `10327871709`, digest `sha256:207ce920cb79136dc1f54bb56f8f934c9c1768093ca3e544ef5855b748a79e79`; durable result `results/ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_RESULT.md`, commit `034f14277e4df5589e3f8fa2995283ea4afe8cb9`.

Exact main and main+held-out ranks are both `9` over `Q(i)`, nullity `23`, with a verified exact right-null witness. This FAIL is only for the prospectively frozen one-parameter angular family, whose polynomial structure gives rank `<=11`; it is not a universal boundary-state cancellation theorem and does not rescue the K5 local-L1 obstruction.

### Iter077K-SM — joint K5 boundary value not source-defined

Result commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Classification:
`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

The one-wedge spectral `i epsilon` selects individual Toller branches but does not provide a joint K5 finite part/correlated extension/contour/conditional-convergence theorem or a theorem commuting one-wedge limits with K5 multiplication/integration.

### Iter077L-SM — extensions exist but are nonunique

Result commit `2da1cce87fb102761d3e2cad83ec93f39ff0f144`.

Classification:
`ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`.

The common collision submanifold is locally `N=SU(2)^4 subset SL(2,C)^4`, codimension 12. Transverse scaling degree is 20 on the frozen conic patch. Same-scaling-degree extensions exist but have local normal-jet freedom through order 8. “Order 8” is a maximal normal-jet order, **not eight scalar couplings**.

### Iter077M/N — explicit supported ambiguity survives source constraints, integration and ordinary gluing

Iter077M result commit `811c84ecdaecf46ba94fde89e8a8fa3a4fe5627e` exhibits

`A_ext,c = A_ext + c F_SU2 delta_N`

as a nonzero supported extension direction preserving the frozen single-vertex source constraints.

Independent critic compact-boundary control `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`, commit `ba2d013d5c0d3889e94b3f120cba031e2f8b4ce9`, exhausts all 32 minimal-sector boundary basis states and finds `16/32` nonzero compact boundary functionals.

Iter077N authoritative run `34789869127`, aggregate artifact `10328420436`, digest `sha256:04fecbabcdf0db984665da0220bf2e1499b9ccaf911e721e721471a4284bddd3`; result commit `03407a010f96e5d81af9813756d21fca6ffcda32`.

Classification:
`ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`.

Ordinary state-sum contraction propagates the local ambiguity but does not independently select its coefficient. Exact critic branch-cube control `results/ITER077N_ADVERSARIAL_BRANCH_CUBE_CONTROL.md`, commit `64e364df099f879b876d10a2d4653c21ddf12d4d`, shows the source additive identities `T^+ + T^- = D` and the full independent-sign EPRL sum can remain unchanged while all factorizable causal K5 sectors retain the supported coefficient.

## Refinement / RG front

### Iter078A-RG CLOSED — physical causal-Toller refinement map is missing

Prereg `97257d6830f1a386f9df3a854391e4e86e340884`; source audit `377e78d6b954003354f2a73ecf95b34f70e97109`; result `728d6e3f40a1797247c2b32a652a2c2d67cb5310`.

Classification:
`ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`.

Verdict: `BLOCKED_MAP_DEFINITION`.

General background-independent spin-foam RG/consistent-boundary frameworks exist, but CRQN v0.2/the causal-Toller source defines only a single causal vertex. Missing for a physical 1-to-5 map: same-boundary coarse/fine amplitudes, fine face/edge measure, boundary embedding/projection, causal multi-vertex prescription, regulator/gauge fixing, fixed-point/matching equation and transport of the Iter077 extension freedom. External BF/EPRL/restricted RG measures are not source-faithful substitutes without an explicit bridge.

### Iter078B-RG CLOSED — causal-orientation combinatorics PASS

Prereg `6f4360ca249c1b5ad9c6b1bd78c9be747be24acd`; implementation `a5d14bf75920c38a0c46106731c76ca65e2ebe07`; production head `047b19fe75630a88aac3f0b783e34198756e6f05`; run `34790158373`; aggregate artifact `10328585276`, digest `sha256:db941e5cbf45e8f89012a8a7b0cef9568d3c289544c4b98a8027bb36f7d9a566`; result `4d4ae20ca3ace6ec37d176ebf1afbf97804513cb`.

Classification:
`ITER078B_RG_1TO5_CAUSAL_BOUNDARY_ORIENTATIONS_EXTEND_TO_FINE_ACYCLIC_K5_ALL32_EXACT_COMBINATORIAL_SCOPED`.

All `32/32` coarse causal boundary sign patterns admit compatible acyclic internal K5 orientations, with exact counts `p!(5-p)!`. Thus causal partial-order combinatorics do not block the minimal same-boundary 1-to-5 refinement. This does not define its amplitude/measure.

### Iter078C-RG CLOSED — supported local tensor = SU(2) BF 15j; refinement interpretation QUALIFIED

Prereg `bef22c39989905373c95bf49c666584dc898176e`; derivation `b531e3d9a2f5e0c9422b170cc220ae9890c0f71e`; result `1eb593fdc97b46e3a2cc41e4ac568274e1c3b1c8`.

Research classification:
`ITER078C_RG_SUPPORTED_K5_AMBIGUITY_IS_SU2_BF_15J_CHANNEL_REFINEMENT_STABLE_UP_TO_BF_GAUGE_NORMALIZATION_EXACT_THEOREM_SCOPED`.

Adversarial qualification `results/ITER078C_ADVERSARIAL_QUALIFICATION.md`, commit `6206080d12a629bf9cca9b7084d8e8e03a843ecb`: verdict `QUALIFIED`.

Accepted core: the compact supported K5 tensor is the SU(2) Ooguri/BF 15j vertex tensor up to nonzero basis normalization/sign. Under **standard Ooguri BF internal sums/weights**, a pure-`L` multi-vertex sector is the BF state sum up to `c^V`, basis normalization and BF gauge-volume factors.

Scope lock: BF weights are not the source-defined causal-Toller refinement measure. Therefore `Fine[L^5]=K_BF L` and `c=K_BF c^5` are conditional BF-control equations, not CRQN RG equations. Mixed `A_0/L` sectors and the full Iter077L ambiguity space remain unresolved.

### Iter078D-RG CLOSED — BF-weighted pure `c^5` gauge-volume theorem; CRQN interpretation QUALIFIED

Prereg `71a8c52bbc2b46a83ebb3f57908e1a4e028261a8`; derivation `2a3f4f05e04c27cad58e76d11460c7334e0d2d42`; result `2046e38df32431967b16297dbb3f33d2967bad19`.

Research classification:
`ITER078D_RG_PURE_C5_BF_CHANNEL_MAKES_NAIVE_1TO5_COEFFICIENTWISE_MAP_GAUGE_VOLUME_DIVERGENT_DELTAI4_REGULATOR_REQUIRED_THEOREM_SCOPED`.

Adversarial qualification `results/ITER078D_ADVERSARIAL_QUALIFICATION.md`, commit `e4e7eace43e736f4f39b86d7b16e8225ee3ffb51`; latest critic handoff `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, commit `26972798ef8c37700862f7f72e9e3ee294edb66a`; verdict `QUALIFIED`.

Accepted exact/theorem core:

- for any fixed multilinear five-vertex contraction of `A_c=A_0+cL`, the formal `c^5` coefficient is exactly `Contract[L^5]` and cannot receive mixed `A_0` contributions;
- **if** the internal sums/measure are the Ooguri BF ones, this coefficient is the BF 1-to-5 amplitude;
- in the cited non-q-deformed BF theorem scope, the unregularized 1-to-5 amplitude contains four redundant flatness constraints and a `delta(I)^4`-type gauge-volume factor, so a BF gauge fixing/regulator is required before assigning a finite BF Pachner coefficient.

Critical scope lock: the actual CRQN causal-Toller refinement map is still undefined by Iter078A. A non-BF causal fine-complex measure need not produce the Ooguri `delta(I)^4` coefficient. Thus Iter078D is authoritative as a **conditional BF-weighted pure-supported regulator control**, not as a theorem that the undefined CRQN 1-to-5 map diverges. BF gauge fixing is required if BF weights are adopted on this sector; it is not yet the source-selected CRQN regulator.

## Exact blocker

The local fixed-causal K5 object is extendible but nonunique. At least one supported ambiguity direction survives the integrated vertex and has a compact SU(2) BF 15j tensor. The published single-vertex source, ordinary gluing and source additive identities do not select its coefficient.

The next physical object is still missing:

`SOURCE_FAITHFUL_CAUSAL_1TO5_AMPLITUDE_MEASURE_EMBEDDING_PROJECTION_REGULATOR_AND_EXTENSION_TRANSPORT_MAP`.

Status:
`BLOCKED_MAP_DEFINITION / BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.

Pure BF results C/D constrain any future map that deliberately adopts BF weights on the supported sector, but they do not supply that map.

## Exact next admissible step

Highest-information gate: freeze one explicit **causal** 1-to-5 multi-vertex prescription prospectively, including:

1. fine face/edge weights and internal spin/intertwiner sums;
2. per-vertex gauge fixing and a treatment of any redundant BF-like gauge volume actually present;
3. causal-orientation sum/selection using the Iter078B-compatible fine patterns;
4. same-boundary embedding map;
5. coarse projection/matching functional;
6. regulator path;
7. explicit transport/projection of the Iter077 extension ambiguity space.

If no source-backed prescription exists, any Lorentzian EPRL-like/BF-like choice must be versioned as **new independently motivated CRQN structure**, not attributed retroactively to the 2026 single-vertex source.

Then test mixed-sector closure of `A_c=A_0+cL` under the same frozen prescription. A source-defined finite-spin mixed sector producing a coarse boundary tensor outside the proposed truncation is a decisive FAIL of one-parameter closure and requires an enlarged coupling space before any fixed-point search.

Do not start from the pure-BF equation `c=K_BF c^5` as a surrogate CRQN flow. If the multi-vertex measure/embedding/projection cannot be defined, the correct terminal result remains `BLOCKED_MAP_DEFINITION`.

Only after a unique local amplitude and mathematically defined refinement map are established may regulator independence, G3 and continuum RG be promoted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no full-amplitude causal divergence/nonexistence theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no CRQN RG fixed point; no `K_BF=1`; no unconditional CRQN `delta(I)^4` theorem before the causal refinement measure is defined; no G3 PASS or F9/G8/K5 promotion. Retain the published one-wedge spectral `i epsilon`; do not reinterpret it as a joint K5 regulator.