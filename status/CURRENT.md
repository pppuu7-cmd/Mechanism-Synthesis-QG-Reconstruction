# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / authoritative front

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`).
- Established/source-backed mechanism union: `F1-F8`.
- Physical F9: `BLOCKED`.
- K5 local amplitude: `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.
- Causal multi-vertex composition: `PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_BLOCKED`.
- RG/refinement map: `BLOCKED_E9_COARSE_FINE_MAP_MISSING`.
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_AND_COMPOSITION_ARE_DEFINED`.
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`.
- **Physical active front:** `CAUSAL_MULTIVERTEX_COMPOSITION_E3_E8 / FUNCTION_SPACE_K5_EXTENSION_SELECTOR / REGULATOR_INDEPENDENCE`.
- **Conditional/control front:** `FIXED_JHALF_ORDERZERO_1TO5_MAP / INTERNAL_EDGE_GAUGE_QUOTIENT / CAUSAL_STABILIZER_REDUCTION / INPUT_TORUS_SYMMETRY`.

`status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remain controlling. Historical Iter077E/F source-dependent gates remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

## Physical source-amplitude chain

### Iter077A/C/D/G/H — authoritative only in recorded scopes

Durable facts:

- true coherent-spinor source Jacobian has an exact rank-10 witness; scalar K5 cycle algebra does not automatically transfer;
- first tested rank-9 exceptional source stratum is transverse codimension 3;
- canonical mixed six-dimensional second jet is nondegenerate;
- corrected `j=1/2` contact is `delta^(rho,1/2)=-(2 i rho/D)delta-(1/D)delta'`, `D=rho^2+1/4`;
- finite spectral epsilon does not legalize the termwise contact K5 pullback.

### Iter077I-SM CLOSED — source-ordered local L1 obstruction

Run `34786586785`; durable result `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.

All 32 minimal all-`j=1/2` boundary components have nonzero leading contractions on the frozen source-faithful collision witness. Ten wedges give homogeneous power `q=-20` in transverse dimension `d=12`, radial absolute-integrability exponent `-9`; the source-ordered leading K5 product is not locally absolutely integrable.

Ceiling: no full distributional vertex nonexistence/divergence theorem.

### Iter077J-SM CLOSED SCOPED FAIL — exact repair

The original modular-rank inference was insufficient. Exact control-only repair established exact rank `9` over `Q(i)`, nullity `23`, with exact null witness for the prospectively frozen one-parameter angular family. Result `results/ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_RESULT.md`, commit `034f14277e4df5589e3f8fa2995283ea4afe8cb9`.

This is not a universal cancellation theorem.

### Iter077K-SM CLOSED BLOCKED — joint K5 boundary value absent from source

Result commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Published one-wedge spectral `i epsilon` selects individual Toller branches but does not define a joint K5 finite part, correlated extension, contour, conditional-convergence theorem, or interchange theorem for the one-wedge limits with K5 multiplication/integration.

### Iter077L-SM CLOSED — extension theorem

Result commit `2da1cce87fb102761d3e2cad83ec93f39ff0f144`.

Actual collision submanifold after source gauge fixing:

`N=SU(2)^4 subset SL(2,C)^4`.

Real codimension `12`, transverse scaling degree `20`. Same-scaling-degree extensions exist but have supported normal-jet ambiguity through order `8`, with smooth coefficient data along `N` subject to additional independently imposed conditions.

### Iter077M/N-SM CLOSED — nonzero ambiguity survives source symmetries/gluing

Iter077M exhibits

`A_ext,c = A_ext + c F_SU2(y;Psi) delta_N(x)`

preserving source ordering, common-left gauge symmetry, true boundary structure and fixed causal labels; independent compact-boundary control has `16/32` nonzero minimal-sector functionals.

Iter077N establishes that ordinary state-sum gluing propagates this supported ambiguity but does not select its coefficient.

### Iter077Q-SM CLOSED PASS — function-space ambiguity

Prospective preregistration `df7d9167067d21be7b5ff1fdafa5aa9cea7ac39d`; authoritative terminal run `34792482045`; aggregate artifact `10328598487`, digest `sha256:58e3cb389a985838942a4d0181e6e680cdd75480cfc24e0ec7bb07d73b199a96`; result `results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md`, commit `5941b3a064d93f2898d9e9a48545826e950455f1`.

Classification:
`ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED`.

On the common-collision set define

`Q(g)=sum_(a<b) tr_(1/2)(g_b^-1 g_a)`.

`Q` is common-left `SL(2,C)` invariant and fully `S5` relabeling invariant. On the frozen compact path,

`Q(t)=12+8 cos(t)`.

For any actual boundary state with nonzero `F_SU2`, the supported family

`{Q^n F_SU2 delta_N : n>=0}`

is linearly independent. Therefore the source-compatible K5 extension freedom already contains at least a countably infinite-dimensional smooth tangential subspace at normal-derivative order zero.

Scientific effect: the local ambiguity is a **function-space problem**, not a one-counterterm problem.

## Causal multi-vertex source inheritance

### Iter079A-SM CLOSED BLOCKED — partial source bridge

Prospective preregistration `d489fa78cf6ee87bd4b02b5a81dc4e131e6883a7`; source matrix `ec642f9d5ad919ae2d75c5d33f5da758621f898b`; implementation `19e00e7acbc7c6407b9841735f8f59404296ab04`; workflow head `7627cf8303c4184940962b260118e0cd5420f833`.

Authoritative terminal run `34793089002`; aggregate artifact `10328048914`, digest `sha256:5172301070c89bc01e16ecf34ff5ecb547e9e78a9e50f5f0c706fd277ee9bb2`; result `results/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_RESULT.md`, commit `646a447b6bb6a654cb3e17b3b759d0981636d8a8`.

Classification:
`ITER079A_SM_CAUSAL_MULTIVERTEX_PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_OBJECT_DEFINITION_BLOCKED_EXACT_SOURCE_AUDIT`.

Terminal frozen matrix:

- `E1 SOURCE_EXPLICIT`: causal orientation / consistency on arbitrary oriented 2-complex is supplied by Beltrán, arXiv:2603.22661v2 (3 Aug 2026).
- `E2 SOURCE_EXPLICIT`: generalized BCG/Toller causal vertex for arbitrary vertex boundary graph / valence is supplied by the same source.
- `E3 MISSING_REQUIRED_OBJECT`: complete multi-vertex causal product/contraction rule as a mathematically defined source-faithful functional.
- `E4 MISSING_REQUIRED_OBJECT`: causal face/edge weights, internal spin/intertwiner sums and normalization with explicit inheritance authority.
- `E5 MISSING_REQUIRED_OBJECT`: boundary gluing / dual-orientation convention with explicit causal bridge.
- `E6 MISSING_REQUIRED_OBJECT`: gauge fixing / redundant noncompact integration treatment for the composed causal object.
- `E7 MISSING_REQUIRED_OBJECT`: joint distributional/regulator prescription compatible with the Iter077 collision problem.
- `E8 MISSING_REQUIRED_OBJECT`: transport/projection/selection of the Iter077Q supported function-space ambiguity through composition.
- `E9 NOT_REQUIRED_AT_THIS_LAYER` for merely defining a fixed multi-vertex amplitude, but `MISSING_REQUIRED_OBJECT` for RG/refinement.

This supersedes the broad wording of Iter078A: **do not repeat E1/E2 orientation/valence work**. The unresolved multi-vertex blocker is now specifically E3-E8.

Adversarial source reread confirms the scope: Beltrán defines arbitrary-2-complex causality and a generalized causal *vertex*, but treats replacing the EPRL-KKL vertex in multi-vertex discretizations as a proposal/application direction and explicitly leaves finiteness of the generalized causal vertex open. Parent EPRL/EPRL-KKL state-sum machinery may not be silently promoted to CRQN causal-Toller authority without an explicit inheritance theorem.

## Conditional/control line — never promote without a bridge

### Iter078N control

`results/ITER078N_ADVERSARIAL_INTERNAL_EDGE_GAUGE_REVIEW.md`, commit `5ac896622ac48b9d4302882ebdcb1b38e83e0014`.

For the frozen all-`j=1/2` order-zero control, exact internal-edge `O(D)` gauge symmetry explains a structural rank ceiling `<=31`. This is not a physical CRQN gauge theorem.

### Iter078P control

Exact one-dimensional multiplicative input-torus redundancy in the fixed-spin control. Not a physical causal refinement theorem.

### Iter078O control

Run `34791393789`; aggregate artifact `10327823415`, digest `sha256:a79e55117f8b8347f65dd0e11693b182a260a8068c0c710e9786e5b125e51864`; result `results/ITER078O_RG_CAUSAL_STABILIZER_SYMMETRY_RESULT.md`, commit `ec06acb66d71bfd6d3dee19335ad78bd14db75b9`.

Exact fixed-subspace dimensions in the labelled 32D all-`j=1/2` control are `2`, `3`, `5` for causal classes `0<->5`, `1<->4`, `2<->3`. This does not cure the Iter077Q physical function-space ambiguity because its scalar `Q` is itself fully relabeling invariant.

## Exact blockers

1. `FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR`.
2. `CAUSAL_MULTIVERTEX_COMPOSITION_E3_E8`.
3. `RG_REFINEMENT_E9_COARSE_FINE_BOUNDARY_MAP_AND_MATCHING_FUNCTIONAL`.
4. `REGULATOR_INDEPENDENCE_AFTER_OBJECT_DEFINITION`.

A blocked local amplitude or composition arrow blocks downstream promotion even if controls are successful.

## Exact next admissible step

Highest-information physical successor:

`EPRL_KKL_TO_CAUSAL_TOLLER_COMPOSITION_INHERITANCE_THEOREM / EXTENSION_TRANSPORT_COMPATIBILITY`.

Prospectively test whether the standard parent EPRL-KKL state-sum composition (face/edge weights, internal sums, boundary contraction and gauge quotient) can be inherited **without adding a new physical choice** when each local vertex is replaced by the BCG/Beltrán causal Toller vertex. The theorem must specify orientation/duality and normalization and must be tested against the Iter077Q supported extension family.

- If exact inheritance fails or is not derivable from frozen source/model axioms: retain `BLOCKED_MULTI_VERTEX_CAUSAL_OBJECT_DEFINITION`.
- If inheritance is proved: immediately test whether composition reduces the infinite-dimensional Iter077Q ambiguity or merely transports it.
- Do not open RG/G3 until E3-E8 are defined; E9 is separately required before refinement/RG.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no full-amplitude causal divergence/nonexistence theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no physical CRQN RG fixed point; no physical CRQN internal-edge gauge theorem from controls; no G3 PASS or F9/G8/K5 promotion. Retain the published one-wedge spectral `i epsilon`; never reinterpret it as a joint K5 regulator without a theorem.