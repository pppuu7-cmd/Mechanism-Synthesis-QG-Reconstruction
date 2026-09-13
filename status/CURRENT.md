# Current MSQGR research state

**Date:** 2026-09-14

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- **Authoritative active front:** `FULL_SOURCE_CAUSAL_VERTEX_LOCAL_LIMIT / SOURCE_ORDERING_OF_TOLLER_WEDGE_INTEGRATION_VS_K5_PRODUCT / FULL_BOUNDARY_CONTRACTION / REGULATOR_INDEPENDENCE`
- Conditional companion fronts: `TOLLER_FRONT_FACE_ALGEBRA (-FF) / SOURCE_BCH_K4_COORDINATE_CONTROL (-BCH)`.

Durable results are authoritative only in their recorded scopes. Naming collisions and quarantined source locks are governed by `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

## Controlling true-source chain

### Iter077A-SM CLOSED — generic true-source transversality

Run `34784565177`.

At the common group collision the exact coherent-spinor Jacobian has a rank-10 witness. Rooted scalar K5 incidence has rank 4; none of its six cycle-nullspace basis relations survives as an identity of the true witness Jacobian. Scalar K5/K4 cycle algebra is therefore conditional until a source pushforward is derived.

### Iter077C-SM CLOSED — first rank-9 exceptional stratum

Run `34784868939`.

Frozen witness `xxxxxyyyzz` has exact rank 9 and self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`.

The first tested full-span exceptional stratum is locally transverse codimension 3 in the 20-dimensional wedge-normal manifold.

### Iter077D-SM CLOSED — canonical mixed nonlinear normal form

Run `34785200044`; result `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`.

The full mixed six-dimensional second jet is nondegenerate with determinant `-1` and inertia `(3+,3-)`. The older fixed-normal/group-only D sibling is provenance-labelled `Iter077D-FN` and is not the full normal form.

### Contact-formula correction

Historical source-dependent `Iter077E-SM` microlocal and `Iter077F-SM` scaling runs are `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`: they transcribed Appendix-D Eq. (37) incorrectly. The controlling erratum is `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

The corrected primary-source `j=1/2` contact is

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`,

`D=rho^2+1/4`.

### Iter077G-SM CLOSED — corrected contact microlocal/scaling gate

Run `34785754577`; result commit `5c3af58f116d508a20ab7138d46862d954399ad4`.

Classification:
`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

For the corrected ten-contact tensor,

`P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2 (gamma-t)`

is a nonzero cubic for finite real `gamma != 0`. The generic rank-10 region admits the standard distributional pullback; at the frozen rank-9 source point the standard termwise Hörmander criterion collides. The exact self-stress contact order is `n_eff=3`. On the canonical six-dimensional quadratic normal form its scaling degree is `8`, so scaling degree alone does not select a unique extension.

This does **not** prove nonexistence of the source-selected correlated boundary value.

### Iter077H-SM CLOSED — finite spectral epsilon is not a termwise smoothing cure

Run `34785966710`; aggregate artifact `10326811897`, digest `sha256:e8dd522e9b5af081032bb6a4ee14ad6b1116c7fabf43a5f491e3909afdae4175`; result `results/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md`, commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`.

Classification:
`ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`.

For finite `epsilon>0`, exact `j=1/2` spectral division gives

`Theta_(sigma,rho,1/2;epsilon)`

`= [1+(2 i sigma rho epsilon-epsilon^2)/D] theta(sigma x)e^(-epsilon|x|)`

`  + [(epsilon-2 i sigma rho)/D] delta(x) - [sigma/D] delta'(x)`.

The delta-prime coefficient is epsilon-independent and nonzero. At frozen `gamma=6/5`, `epsilon=1/7`, all `1024/1024` wedge-sign assignments retain a nonzero degree-3 pure-contact self-stress coefficient. Therefore simply keeping spectral epsilon finite does not legalize the termwise spinor-contact K5 pullback.

## Important source-ordering fact

The primary causal-vertex construction defines each Toller matrix by the spectral Feynman prescription and uses the product of ten Toller matrices in the vertex. The primary papers also describe Toller matrices as polynomially bounded **functions** on `SL(2,C)` and give closed reduced hypergeometric forms after the wedge/spinor integration.

Therefore the next decisive question is whether the source order

`one-wedge spectral/spinor integration -> Toller function -> K5 product/group integration`

has a well-defined local distributional/improper-integral meaning at the common collision even though

`expand each wedge into theta/contact distributions -> multiply all ten termwise`

fails the standard rank-9 pullback criterion.

The two orderings may not be interchanged without a theorem.

## Exact blocker

A fully contracted causal K5 vertex as a unique local distributional functional is still unestablished. The active missing object is no longer an arbitrary local contact coefficient or a finite-epsilon mollifier. It is:

`SOURCE_ORDERED_TOLLER_FUNCTION_K5_COLLISION_BOUNDARY_VALUE_WITH_FULL_BOUNDARY_CONTRACTION`.

Earlier boundary-intertwiner power-counting already found severe ordinary Toller-function collision powers in the all-`j=1/2` sector, but correctly stopped short of a distributional nonexistence theorem because source boundary terms/orderings were not included.

The physical nonlinear source-to-K4 curvature remains unselected. The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`.

## Next admissible steps

1. **Primary:** `Iter077I-SM` — prospectively freeze the source ordering actually encoded by Eq. (3)/(4) and the closed Toller-function formulas. Determine whether one-wedge spectral/spinor integration yields an ordinary locally integrable Toller matrix near `beta=0` or a singular function requiring a boundary value, and classify its exact small-boost leading powers for the complete `j=1/2` matrix.
2. Combine that source-ordered one-wedge object with the already existing full K5 boundary-intertwiner collision-power infrastructure, keeping all 32 all-spin-half boundary intertwiner components rather than representative states.
3. Test local K5 integrability/distributional extension and then regulator independence. A source-defined divergence/nonuniqueness is a valid negative result.
4. Continue `-FF` and `-BCH` only as conditional parallel controls; never promote them into the source-amplitude line without an explicit theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; retain the published spectral `i epsilon`.