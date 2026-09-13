# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / chain status

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- K5 local amplitude: `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`
- G3 quantum dynamics: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_DEFINED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- **Authoritative active front:** `REFINEMENT_CYLINDRICAL_OR_RG_SELECTOR / UNIQUE_K5_EXTENSION / REGULATOR_INDEPENDENCE`
- Conditional companion fronts remain `TOLLER_FRONT_FACE_ALGEBRA (-FF)` and `SOURCE_BCH_K4_COORDINATE_CONTROL (-BCH)` only.

Durable results are authoritative only in their recorded scopes. Historical naming collisions and quarantined source locks are governed by `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

## Controlling source-map chain

### Iter077A-SM CLOSED — true-source transversality

Run `34784565177`. Exact coherent-spinor source Jacobian has a rank-10 witness; scalar rooted K5 incidence has rank 4 and its six cycle relations do not transfer. Scalar K4/K5 cycle algebra remains conditional without a source pushforward.

### Iter077C-SM CLOSED — rank-9 exceptional source stratum

Run `34784868939`. Frozen witness `xxxxxyyyzz` has rank 9, self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`, and locally transverse codimension 3 in the 20-dimensional wedge-normal manifold.

### Iter077D-SM CLOSED — canonical mixed nonlinear normal form

Run `34785200044`; `results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md`. Mixed six-dimensional Hessian is nondegenerate, determinant `-1`, inertia `(3+,3-)`. Historical fixed-normal sibling is `Iter077D-FN` only.

### Contact-formula erratum

Historical source-dependent Iter077E/F runs are `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`. Correct source formula at `j=1/2` is

`delta^(rho,1/2)=-(2 i rho/D) delta-(1/D) delta'`, `D=rho^2+1/4`.

### Iter077G-SM CLOSED — corrected contact/scaling

Run `34785754577`, result commit `5c3af58f116d508a20ab7138d46862d954399ad4`.

Classification:
`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`.

The termwise standard pullback collides on the frozen rank-9 source point; `n_eff=3`; the canonical six-dimensional quadratic normal form has scaling degree 8. This requires source-selected correlated extension but is not a nonexistence theorem.

### Iter077H-SM CLOSED — finite one-wedge spectral epsilon is not a termwise cure

Run `34785966710`, aggregate artifact `10326811897`, result commit `004af0e570b4999ec849d0b75ca44d2faf9b47c2`.

Finite spectral epsilon leaves an epsilon-independent delta-prime channel; all `1024/1024` wedge-sign assignments retain a nonzero frozen pure-contact self-stress contribution. No termwise K5 legalization follows.

### Iter077I-SM CLOSED — source-ordered ordinary Toller K5 fails local L1

Run `34786586785`, aggregate artifact `10326812769`, result `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.

Classification:
`ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`.

All `32/32` boundary components have nonzero exact leading contraction at the frozen source-faithful collision ray; all `512/512` fixed factorized-causal leading contractions survive. Ten wedges give transverse power `q=-20` in `d=12`, radial absolute exponent `-9`, so the source-ordered object is not locally absolutely integrable on an open angular patch. This is not a full distributional divergence theorem.

### Iter077J-SM — original modular FAIL under exact-rank repair

Original terminal run `34788323622` reported main/combined/relabelled modular ranks `9/9/30`. The original preregistration required exact `Q(i)` rank and an exact right-nullspace witness on FAIL, but the implementation used a single `F_p(i)` rank. Full modular rank would certify full characteristic-zero rank; modular rank deficiency does not prove exact deficiency.

A prospective control-only repair is running as `34789579078`:

- prereg final frozen commit `c94c8b77a0877d2bf56bbb89c309ae7a6ae4c9d6`;
- implementation commit `d0dbde896462ffa897a918bc80995a7e463e753b`;
- workflow head `d9072a636db5ce0a9705f770c92a5876dfc74114`.

Independent exact structural control already proves the frozen main+held-out one-parameter ray family has rank at most 11 because every 32-vector component is a polynomial of degree at most 10 in the frozen seed. Do not promote the original exact-rank FAIL until the repair aggregate is terminal.

### Iter077K-SM CLOSED — published source does not define the joint K5 boundary value

Prereg commit `97f0114f80edee3a42f67490f81cb1eb8f497304`; result commit `898355bea286d6a64934ea20c95711aa4e408b3d`.

Classification:
`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

The published Feynman `i epsilon` uniquely selects each one-wedge Toller branch but does not supply a joint K5 common regulator, finite part, correlated extension, contour, conditional-convergence theorem, or theorem commuting the one-wedge limits with the non-`L1` K5 product/integration.

### Iter077L-SM CLOSED — local extensions exist but are not unique

Prereg commit `565a36453cf781b1af366da6960ab7f55e6605f1`; result commit `2da1cce87fb102761d3e2cad83ec93f39ff0f144`.

Classification:
`ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`.

The common collision is locally the smooth submanifold `N=SU(2)^4 subset SL(2,C)^4`, codimension 12. On the Iter077I conic patch the exact transverse scaling degree is 20. Brunetti-Fredenhagen submanifold extension theory gives local same-scaling-degree extensions but leaves normal-jet freedom through order `20-12=8`. Extension existence is therefore not the blocker; physical/source selection is.

### Iter077M-SM CLOSED — published single-vertex symmetries do not select the extension

Prereg commit `b9af6704336a357dba0b2287b2d7d1320fc020a7`; result commit `811c84ecdaecf46ba94fde89e8a8fa3a4fe5627e`.

Classification:
`ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`.

A concrete family

`A_ext,c(Psi)=A_ext(Psi)+c F_SU2(y;Psi) delta_N(x)`

preserves the off-collision ten-Toller source object, common global gauge symmetry, true boundary spin/intertwiner structure, fixed causal labels, and maximal transverse scaling degree. The published single-vertex source contains no condition fixing `c`.

### Iter077N-SM CLOSED — the supported ambiguity survives the integrated vertex; ordinary gluing does not fix it

Authoritative run `34789869127`, production head `7b12b0f8207d129ffd9b79bda158db77e265f8f6`, aggregate artifact `10328420436`, digest `sha256:04fecbabcdf0db984665da0220bf2e1499b9ccaf911e721e721471a4284bddd3`.

Durable result: `results/ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING_RESULT.md`, commit `03407a010f96e5d81af9813756d21fca6ffcda32`.

Classification:
`ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`.

Exact all-32 compact K5 census gives `16/32` nonzero integrated boundary functionals for the `F_SU2 delta_N` ambiguity; exact-row checksum `8923ae7f43fa83b9da1e9095d3ef195e6d208031ff6824a6a1a15a2d9912b936`.

For `A_c=A_0+cL`, ordinary two-vertex state-sum contraction is identically

`G_c=G_00+c(G_L0+G_0L)+c^2 G_LL`.

This is composition of whatever vertex tensor is supplied, not an independent equation selecting `c`. The published causal source has no c-independent multi-vertex/refinement target. Hence the local ambiguity affects the integrated single-vertex amplitude and is propagated, not removed, by standard gluing.

## Exact blocker

The fixed-causal K5 vertex is locally extendible but the integrated boundary functional is not uniquely selected by the published source construction, its stated single-vertex symmetries, or ordinary spin-foam gluing.

The controlling missing object is now:

`REFINEMENT_CYLINDRICAL_OR_RG_CONSISTENCY_SELECTOR_FOR_K5_EXTENSION_FREEDOM`.

Status:

`BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.

The order-8 statement is a finite **normal-jet order**, not a claim of only eight scalar couplings: coefficient data may still live along the 12-dimensional compact collision submanifold and require symmetry/RG reduction.

## Exact next admissible steps

1. Consume Iter077J repair only after run `34789579078` is terminal; preserve any exact rank deficiency only in its frozen one-parameter-family scope.
2. Do not run more local leading-angle/contact lemmas without a new dependency.
3. Open the next layer: prospectively test whether the established **consistent-boundary / cylindrical-consistency / background-independent RG** framework provides a concrete refinement map for the causal-Toller vertex and whether an independent fixed-point/consistency equation can constrain the supported extension freedom.
4. If no causal refinement/coarse-graining map exists, classify the RG selector as `BLOCKED_MAP_DEFINITION` rather than inventing a fixed point.
5. A new refinement/RG prescription is scientifically admissible only if independently motivated as necessary for regulator independence/continuum physics even without the local ambiguity, versioned as a new CRQN mechanism, and prospectively falsifiable. It may not be introduced merely to rescue CRQN v0.2.
6. Only after a unique local amplitude is selected may regulator independence and G3 be promoted.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no full-amplitude causal divergence/nonexistence theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no G3 PASS or F9/G8/K5 promotion. Retain the published one-wedge spectral `i epsilon`; do not reinterpret it as a joint K5 regulator. Standard state-sum gluing is not a selector of the extension coefficient.