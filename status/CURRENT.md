# Current MSQGR research state

**Date:** 2026-09-14

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- DSIR handoff-contract completeness V1: `100%` (interface completeness only, not physical-gate completion)
- **Authoritative active front:** `FULL_SOURCE_CAUSAL_VERTEX_LOCAL_LIMIT / TRUE_SOURCE_B_MAP_EXCEPTIONAL_CONTACT_PULLBACK / FULL_BOUNDARY_CONTRACTION / REGULATOR_INDEPENDENCE`
- Conditional companion fronts: `TOLLER_FRONT_FACE_ALGEBRA (-FF) / SOURCE_BCH_K4_COORDINATE_CONTROL (-BCH)`.

Durable result notes remain authoritative for all closed earlier iterations. Naming/provenance collisions in the parallel Iter077 campaign are governed by `status/ITER077_PROVENANCE_LEDGER.md` and `status/ITER077_NUMBERING_AND_SCOPE_CORRECTION.md`.

## Controlling earlier results

The Iter076 H-Z chain remains closed in its recorded scopes. In particular:

- H-Q establish the exact/scoped Hodge-line, orientation and quadratic-transport algebra, but not a physical nonlinear source-to-K4 pushforward.
- R-S establish zero Haar one-jet but allow a nonlinear quadratic-curvature contamination channel.
- T-U establish that an individual causal Toller branch is singular at the identity and that a minimally stripped gamma-simple wedge germ generically has nonzero one-jet.
- V-W show that common-node pure boost and compact generator directions are killed by exact SU(2)-intertwiner closure.
- X-Y show that those pure-direction zeros do not imply a direction-independent zero source germ: a transverse matrix-valued angular connection survives generic frozen intertwiner controls and is fed by a concrete mixed compact/boost path.
- Z establishes that after scalar radial stripping the generic Toller front face remains direction-dependent and matrix/bundle-valued; no scalar normalization derivative flattens it in `5/7` frozen exact controls.

These are useful local ingredients, but they do not by themselves establish existence of the source causal vertex.

## Strategic source-map handoff

The 2026 causal-vertex source defines the coherent vertex using four gauge-fixed `SL(2,C)` group integrations and ten wedge Toller factors. In the exact coherent-spinor representation each wedge carries an independent auxiliary `CP^1` spinor and the contact/restrictor structure is supported on

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`.

Therefore the relevant local source map is

`B : SL(2,C)^4 x (CP^1)^10 -> R^10`,

not the scalar rooted K5 incidence surrogate. A scalar-incidence cycle/Hodge result is conditional algebra until an explicit source pushforward theorem is supplied.

### Iter077A-SM CLOSED — true source-map transversality

Authoritative run `34784565177`; durable result `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`.

At the common group collision, with root 0 gauge fixed and Hermitian boost coordinates,

`dB_ab = n_ab . (dx_a-dx_b)`,

so the exact boost Jacobian is

`J_(ab),(c,i)=(delta_ac-delta_bc)n_ab^i`.

A frozen exact wedge-spinor witness has `rank_Q(J)=10`, left nullity `0`, and an exact nonzero maximal minor `-1`. The rooted scalar K5 incidence matrix has rank `4`, left nullity `6`, and `0/6` of its cycle-nullspace basis relations annihilate the true witness Jacobian.

**Durable consequence:** the scalar K5 rank-4/cycle picture is a special collinear slice, not the generic first-order structure of the coherent-spinor source map. Reduced K4/Hodge cycle coefficients do not transfer to the source amplitude without an explicit pushforward derivation.

Exact axis-control census over `3^10=59049` normal assignments gives ranks

`4:3, 5:60, 6:600, 7:4800, 8:17766, 9:26100, 10:9720`.

No continuum measure statement follows from this finite census.

### Iter077C-SM CLOSED — first exceptional source stratum

Authoritative retry run `34784868939`; durable result `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`; result commit `5cdafc091295526f49323f38be13e01dcd553926`.

Rank deficiency of the true common-collision Jacobian is exactly equivalent to a nonzero **vector self-stress** satisfying five-node equilibrium. It is not generically the scalar K5 cycle nullspace.

The prospectively frozen first full-span rank-9 axis witness is

`xxxxxyyyzz`

in edge order `01,02,03,04,12,13,14,23,24,34`. It has:

- `rank_Q(J)=9`;
- one-dimensional left kernel with
  `lambda=(1,-1,0,0,1,0,0,0,0,0)`;
- three-dimensional right kernel;
- exact self-stress equilibrium;
- structured normal-variation map `L` of shape `3 x 20` and exact rank `3`;
- a nonzero `3 x 3` minor `-1` on tangent directions `01:y`, `01:z`, `02:z`.

Therefore this first tested genuinely three-dimensional rank-9 exceptional source stratum is crossed transversely and is locally codimension `3` in the 20-dimensional wedge-normal manifold.

This is **not** a theorem for every exceptional point and does **not** prove that contact-distribution pullback is harmless.

## Conditional parallel branches

### `Iter077A-FF`

The later bare-name front-face preregistration is provenance-disambiguated as `Iter077A-FF`. Its algebraic/covariant closure results, if validly aggregated, remain front-face conditional controls. They cannot replace `Iter077A-SM` or establish a full source-amplitude theorem. The initial combined A/B workflow is non-authoritative for iteration numbering.

### `Iter077B-BCH`

The BCH/K4 branch is provenance-disambiguated as `Iter077B-BCH` and may run independently as a coordinate-scoped quadratic-curvature control. Even a PASS does not establish the physical Toller/front-face pushforward or a physical K4 numerator. Independent lane relaunch began at commit `f5ac9f4c45c1460fe75329de244df5c65d406e6b`.

## Exact blocker

A **fully contracted source causal K5 vertex as a unique local distributional functional has not been established**.

Generic common-collision transversality is now demonstrated by an exact full-rank witness. The first tested full-span rank-9 exceptional stratum is locally codimension 3. The decisive unresolved question has therefore moved to the **true nonlinear source geometry on the exceptional set**:

1. for a frozen self-stress `lambda`, determine the first nonzero nonlinear term of
   `Phi=sum_e lambda_e B_e` along the right kernel of `dB`;
2. determine whether this excess constraint is quadratic/nondegenerate, higher-order, or has exact flat directions;
3. from that nonlinear normal form, test the local pullback/scaling of the source contact distributions;
4. only after exceptional-stratum control retain all boundary intertwiner components through the ten `CP^1` integrations and four group variables and test regulator removal/independence.

The physical nonlinear source-to-K4 curvature is still not selected. The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps

1. **Primary:** `Iter077D-SM` — at the frozen rank-9 witness `xxxxxyyyzz`, compute the source-faithful nonlinear Taylor jet of `Phi=sum lambda_e B_e` from the exact Eq.(32) matrix expression. Restrict the quadratic form to `ker dB`, determine exact rank/signature, and test any remaining flat kernel direction without changing the witness after inspection.
2. If the nonlinear normal form is determined, test the local scaling/pullback of the source contact terms on that exceptional stratum. A negative/non-unique result is a valid source-amplitude obstruction.
3. Only then build the frozen all-`j=1/2` complete boundary sector (32 intertwiner components) through all ten auxiliary-spinor integrations and test the first potentially divergent fully contracted coefficient/regulator dependence.
4. Continue `-FF` and `-BCH` only as independent conditional lanes; do not merge their PASS/FAIL with the source-amplitude line without an explicit pushforward theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; no arbitrary scalar flattening of the Toller front face; retain the published spectral `i epsilon`.