# Current MSQGR research state

**Date:** 2026-09-14

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_DEFINED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_OBJECT_DEFINITION`
- **Authoritative active front:** `FULL_SOURCE_CAUSAL_VERTEX_LOCAL_LIMIT / SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION / FULL_BOUNDARY_CONTRACTION / REGULATOR_INDEPENDENCE`
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

Therefore the source-ordered leading K5 object is not locally absolutely integrable on an open angular neighborhood. This is only an `L1` obstruction: no full causal-vertex divergence/nonexistence theorem follows.

## ACTIVE Iter077J-SM — full-32 leading angular-span gate

Preregistration commit `e5aae441c84a5d458e1d91dd1f64ab160043dd35` precedes implementation commit `df951850617eb9683a3a6b42fe6cdb4e1b3b1fd6` and production/workflow commit `47065cdf518c9984f01cd1ee7e43818ea4dc6ba9`.

Authoritative run: `34788323622`.

Frozen question: do exact leading angular coefficient vectors sampled on prospectively fixed nondegenerate K5 collision directions span the complete 32-dimensional boundary space? A full-rank result would exclude any nonzero **angle-independent** boundary-state superposition from cancelling the leading `r^-20` coefficient identically.

At the last recovery read, lanes A/B/C were terminal-successful but lane D was still `in_progress`; therefore **no Iter077J scientific verdict is yet authoritative**. Partial Actions results are not evidence.

Frozen lanes:

- A: source/provenance locks and admissibility of all 56 fixed main+held-out rays;
- B: exact Gaussian-field rank of 40 main angular vectors, PASS target rank 32;
- C: held-out 16-ray validation plus an exact nonzero 32x32 minor certificate;
- D: all 120 vertex relabelings of the first eight rays plus a collinear diagnostic control.

The finite-field `F_p(i)` certificate with inert prime `p=1000000007` is only used as an exact nonzero-minor certificate: full rank modulo this prime proves the corresponding Gaussian-integer minor is nonzero over `Q(i)`.

### Iter077K-SM CLOSED — published source does not select the missing joint K5 boundary value

Preregistration: `prereg/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION.md`, commit `97f0114f80edee3a42f67490f81cb1eb8f497304`.

Durable result: `results/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION_RESULT.md`, commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Classification:
`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

The two frozen primary sources do define each one-wedge Toller matrix through the spectral Feynman prescription and formally define the fixed-causal vertex as the product of ten resulting Toller functions under four gauge-fixed `SL(2,C)` integrations. The companion source proves uniqueness of the **one-wedge Toller splitting**.

However, after Iter077I-SM establishes that the complete minimal-sector source-ordered product is not locally `L1` at the common collision, those sources do not supply a separate joint K5 prescription/theorem selecting a unique correlated/conditional boundary value: no common ten-wedge regulator retained through group integration, correlated extension, Hadamard finite part, group-variable contour prescription, conditional-convergence theorem, or theorem commuting the one-wedge limits with K5 multiplication/integration was found in the frozen source authority.

This is `BLOCKED`, not `FAIL`: no theorem of mathematical nonexistence has been established. But a new common-`epsilon` limit, finite part, correlated extension, subtraction, or contour deformation would now be a **new mechanism/definition**, not something already source-selected by the published one-wedge `i epsilon`.

## Exact blocker

A fully contracted fixed-causal K5 vertex as a unique finite-spin local distributional/conditional functional is still unestablished. The controlling missing object remains:

`SOURCE_SELECTED_CORRELATED_OR_CONDITIONAL_COMMON_COLLISION_BOUNDARY_VALUE_WITH_FULL_BOUNDARY_CONTRACTION_AND_SUBLEADING_SOURCE_DATA`.

Its status is sharpened to `BLOCKED_OBJECT_DEFINITION_IN_PUBLISHED_SOURCE`.

The physical nonlinear source-to-K4 curvature remains unselected. The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`.

## Next admissible steps

1. Consume every raw Iter077J-SM lane artifact and aggregate **only after the run is terminal**, and classify it scientifically rather than by green CI. Do not launch a duplicate J gate.
2. Regardless of J's outcome, do not continue accumulating leading-angle lemmas as a substitute for the missing amplitude definition.
3. Highest-information next physical/mathematical gate: prospectively identify and test an external theorem that makes the exact fixed-causal Eq. (4) a unique distributional/conditional functional under the published ordering and its actual hypotheses. If no such theorem applies, keep K5 at `BLOCKED_OBJECT_DEFINITION`.
4. A new common-regulator/correlated-extension mechanism is admissible only if independently motivated **before** testing, with source ordering, complete 32-component boundary contraction, regulator path, positive/negative controls and regulator-independence criteria frozen prospectively. It may not be introduced merely to rescue CRQN.
5. G3 quantum dynamics remains downstream and is not admissible for promotion until the local vertex/amplitude is mathematically defined.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no source-selected K5 correlated-extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; retain the published one-wedge spectral `i epsilon`; do not reinterpret it as a joint K5 regulator without a theorem.