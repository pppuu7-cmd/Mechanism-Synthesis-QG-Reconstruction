# Current MSQGR research state

**Date:** 2026-09-14

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_DEFINED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`
- **Authoritative active front:** `SOURCE_SELECTED_K5_EXTENSION_SELECTOR / TWO_VERTEX_GLUING_COMPOSITION / REGULATOR_INDEPENDENCE`
- Conditional companion fronts: `TOLLER_FRONT_FACE_ALGEBRA (-FF) / SOURCE_BCH_K4_COORDINATE_CONTROL (-BCH)`.

Durable results are authoritative only in their recorded scopes. Naming collisions and quarantined source locks are governed by `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

## Controlling true-source chain

### Iter077A-SM CLOSED — generic true-source transversality

Run `34784565177`.

At the common group collision the exact coherent-spinor Jacobian has a rank-10 witness. Rooted scalar K5 incidence has rank 4; none of its six cycle-nullspace basis relations survives as an identity of the true witness Jacobian. Scalar K5/K4 cycle algebra is therefore conditional until a source pushforward is derived.

### Iter077C-SM CLOSED — first rank-9 exceptional stratum

Run `34784868939`.

Frozen witness `xxxxxyyyzz` has rank 9 and self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`. The first tested full-span exceptional stratum is locally transverse codimension 3 in the 20-dimensional wedge-normal manifold.

### Iter077D-SM CLOSED — canonical mixed nonlinear normal form

Run `34785200044`; result `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`.

The full mixed six-dimensional second jet is nondegenerate with determinant `-1` and inertia `(3+,3-)`. The older fixed-normal/group-only D sibling is provenance-labelled `Iter077D-FN` and is not the full normal form.

### Contact-formula correction

Historical source-dependent `Iter077E-SM` microlocal and `Iter077F-SM` scaling runs are `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`: they transcribed Appendix-D Eq. (37) incorrectly. The controlling erratum is `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

Corrected primary-source `j=1/2` contact:

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

### Iter077G-SM CLOSED — corrected contact microlocal/scaling gate

Run `34785754577`; result commit `5c3af58f116d508a20ab7138d46862d954399ad4`.

Classification:
`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

At the frozen rank-9 source point the standard termwise Hörmander criterion collides. Exact self-stress contact order is `n_eff=3`; on the canonical six-dimensional quadratic normal form scaling degree is `8`, so scaling degree alone does not select a unique extension. This does not prove nonexistence of the source-selected correlated boundary value.

### Iter077H-SM CLOSED — finite spectral epsilon is not a termwise smoothing cure

Run `34785966710`; aggregate artifact `10326811897`, digest `sha256:e8dd522e9b5af081032bb6a4ee14ad6b1116c7fabf43a5f491e3909afdae4175`; result commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`.

Classification:
`ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`.

Finite spectral epsilon leaves the nonzero delta-prime contact and does not legalize the termwise spinor-contact K5 pullback.

### Iter077I-SM CLOSED — source-ordered Toller K5 is not locally L1 in the all-j=1/2 leading sector

Authoritative run `34786586785`, production head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`, aggregate artifact `10326812769`, digest `sha256:b9e7d617598acaeb60ee7018e3ee4f78a232b32be86b112da4713352d9797887`.

Durable result: `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.

Classification:
`ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`.

Raw artifacts establish:

- all `32/32` five-node boundary-intertwiner components have nonzero exact leading contractions on the frozen nondegenerate collision ray;
- all `512/512` factorized-causal leading contractions are nonzero and equal to the all-plus coefficient in the frozen convention;
- ten `j=1/2` wedges give homogeneous power `q=-20`;
- transverse boost dimension is `d=12`, so radial absolute-integrability exponent is `d-1+q=-9` and first-moment margin `q+d=-8`.

Therefore the source-ordered leading K5 object is not locally absolutely integrable on an open angular neighbourhood. This is only an `L1` obstruction: no full causal-vertex divergence/nonexistence theorem follows.

### Iter077J-SM — original terminal run requires exact-rank control repair

Original preregistration: `prereg/ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN.md`, commit `e5aae441c84a5d458e1d91dd1f64ab160043dd35`.

Original terminal run `34788323622` completed with green CI and aggregate artifact `10326974314`, digest `sha256:2ccd439510ff0f053861782424c8a384c64711bac94a64f76b26cae6b5c2f0b9`. Its aggregate reported scientific FAIL with modular ranks `main=9`, `combined=9`, `relabelled=30`.

That original FAIL is **not yet authoritative as an exact-rank statement**. Adversarial implementation audit found that the code computed rank over `F_p(i)` at `p=1000000007`. Full rank modulo an inert prime would certify characteristic-zero full rank, but rank deficiency modulo one prime does not prove rank deficiency over `Q(i)`. The original preregistration also required an explicit exact right-nullspace witness on FAIL, which the implementation did not emit.

A further exact structural fact was found before the repair calculation: the frozen main/held-out ray family is one-parameter affine in seed `s`; every edge matrix is affine in `s`; the ten-edge contraction is therefore polynomial in `s` of degree at most 10. Hence the frozen one-parameter family has exact characteristic-zero row-rank upper bound `<=11` and was structurally incapable of certifying full rank 32.

Prospective control-only repair:

- prereg: `prereg/ITER077J_SM_EXACT_RANK_CONTROL_ONLY_REPAIR.md`, final frozen commit `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`;
- implementation: `distributional/iter077j_sm_exact_rank_control_repair.py`, commit `d0dbde896462ffa897a918bc80995a7e463e753b`;
- workflow: `.github/workflows/iter077j_sm_exact_rank_control_repair.yml`, production commit `d9072a636db5ce0a9705f770c92a5876dfc74114`;
- run `34789579078` is active at the latest recovery read.

Repair lanes Bx/Cx compute exact `Q(i)` RREF and an exact verified nullspace witness. Four independent Dx lanes use inert primes only as lower-bound/full-rank certificates and explicitly forbid the invalid converse. No repair scientific verdict is authoritative until the aggregate is terminal.

### Iter077K-SM CLOSED — published source does not define the missing joint K5 boundary value

Preregistration: `prereg/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION.md`, commit `97f0114f80edee3a42f67490f81cb1eb8f497304`.

Durable result: `results/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION_RESULT.md`, commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Classification:
`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

The primary sources define every one-wedge Toller matrix by the spectral Feynman prescription and formally place ten resulting Toller functions under four gauge-fixed `SL(2,C)` integrations. They do not supply a joint K5 common regulator, correlated extension, Hadamard finite part, group-variable contour prescription, conditional-convergence theorem, or theorem commuting the one-wedge limits with K5 multiplication/integration after the Iter077I non-`L1` collision.

This is `BLOCKED`, not a theorem of nonexistence.

### Iter077L-SM CLOSED — standard extension theory gives existence but not uniqueness

Preregistration: `prereg/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM.md`, commit `565a36453cf781b1af366da6960ab7f55e6605f1`.

Source/theorem derivation: `sources/ITER077L_SM_TRANSVERSE_EXTENSION_THEOREM_DERIVATION.md`, commit `1a6cb5331098287823e55c7db5452a976b8501a5`.

Durable result: `results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md`, commit `2da1cce87fb102761d3e2cad83ec93f39ff0f144`.

Classification:
`ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`.

The simultaneous common-collision locus is locally the smooth embedded submanifold

`N = SU(2)^4 subset SL(2,C)^4`,

with real codimension 12. On a conic normal patch around an Iter077I nonzero witness, all additional partial-edge collisions are excluded for nonzero radius and the source-ordered K5 component has exact transverse scaling degree `sd_N=20`.

Brunetti-Fredenhagen submanifold extension theory is therefore in the finite but nonunique regime `12 <= 20 < infinity`: local same-scaling-degree extensions exist, but scaling degree alone leaves finite normal-jet freedom through order `20-12=8`. Thus mathematical extension existence is not the active obstruction; **physical/source selection is**.

This theorem does not prove that no stronger physical condition can fix the extension.

### Iter077M-SM CLOSED — published gauge/boundary/causal constraints still do not select the extension

Preregistration: `prereg/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR.md`, commit `b9af6704336a357dba0b2287b2d7d1320fc020a7`.

Source derivation: `sources/ITER077M_SM_SOURCE_SYMMETRY_SELECTOR_DERIVATION.md`, commit `3bd388c143030e8947ca1a206e907027e0dd2362`.

Durable result: `results/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR_RESULT.md`, commit `811c84ecdaecf46ba94fde89e8a8fa3a4fe5627e`.

Classification:
`ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`.

An explicit one-parameter local ambiguity survives every constraint actually frozen from the published single-vertex construction. If `A_ext` is one Iter077L same-scaling-degree extension, then

`A_ext,c(Psi) = A_ext(Psi) + c F_SU2(y;Psi) delta_N(x)`

has:

- identical off-`N` source-ordered ten-Toller object;
- the same maximal transverse scaling degree 20 because `sd_N(delta_N)=12`;
- the exact common global `SL(2,C)` gauge structure when written before gauge fixing on the invariant common-collision set;
- a coefficient `F_SU2` constructed from the same true ten spins and five SU(2)-invariant boundary intertwiners;
- unchanged fixed causal labels and no causal-sector sum.

The primary source explicitly states that causal-vertex finiteness still requires investigation and that many-vertex construction is future work. No published single-vertex subtraction/normalization, K5 finite part, common regulator, or gluing/composition identity fixes `c`.

Therefore the currently published constraints do not make the finite-spin local vertex unique. This does not preclude a future independently motivated selector.

## Exact blocker

The fully contracted fixed-causal K5 vertex is locally extendible but is not uniquely selected by the published source construction or its stated single-vertex symmetries.

The controlling missing object is now sharpened to:

`UNIQUE_SOURCE_OR_COMPOSITION_SELECTED_K5_EXTENSION_FIXING_ORDER8_LOCAL_NORMAL_JET_FREEDOM`.

Status:

`BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.

The physical nonlinear source-to-K4 curvature remains unselected. The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`. G3 remains downstream and cannot be promoted while the local amplitude carries an unfixed supported ambiguity.

## Next admissible steps

1. Consume Iter077J control-only repair only after run `34789579078` is terminal. If exact Bx/Cx confirm rank deficiency with a verified exact nullspace witness, preserve it only as a scoped property of the frozen one-parameter angular family; do not infer a universal boundary-state cancellation.
2. Do not run further leading-angle rank families merely to increase local evidence. Iter077L/M have opened the more fundamental selector problem.
3. **Highest-information next gate:** move one layer outward to the smallest source-faithful **two-vertex gluing/composition** problem. Prospectively freeze the internal boundary Hilbert-space contraction, measure, causal orientations and local extension parameterization; determine whether composition forces the supported coefficient(s) to zero, fixes a unique nonzero value, leaves residual freedom, or is itself undefined.
4. Only if a unique local extension is selected may regulator-independence and then G3 quantum dynamics be promoted.
5. A new common regulator, finite part, subtraction, or extension law may be studied only as a separately motivated new mechanism with prospective falsification criteria; it may not be introduced post hoc to rescue CRQN.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no unique source-selected K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; retain the published one-wedge spectral `i epsilon`; do not reinterpret it as a joint K5 regulator; do not treat the original Iter077J modular rank deficiency as an exact rank proof until the control-only repair is terminal.