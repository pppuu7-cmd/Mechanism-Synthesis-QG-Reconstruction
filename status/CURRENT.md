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

## Controlling source-map results

The exact coherent-spinor source map is

`B : SL(2,C)^4 x (CP^1)^10 -> R^10`,

with `B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`. It is not generically the scalar rooted K5 incidence surrogate.

### Iter077A-SM CLOSED — true source-map transversality

Authoritative run `34784565177`; durable result `results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md`.

A frozen exact wedge-spinor witness gives `rank_Q(J)=10` for the true boost Jacobian, while rooted scalar K5 incidence has rank `4`. The scalar cycle/Hodge picture is therefore only a special collinear slice and does not transfer to the source amplitude without an explicit pushforward theorem.

### Iter077C-SM CLOSED — first exceptional source stratum

Authoritative retry run `34784868939`; durable result `results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md`; result commit `5cdafc091295526f49323f38be13e01dcd553926`.

The frozen full-span rank-9 witness `xxxxxyyyzz` has a one-dimensional vector self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`, a three-dimensional right kernel, and a rank-3 structured normal-variation map. This first tested rank-9 exceptional source stratum is locally codimension `3` in the wedge-normal manifold.

### Iter077D-SM CLOSED — nonlinear excess normal form

Authoritative retry run `34785181275`; durable result `results/ITER077D_SM_NONLINEAR_EXCESS_B_JET_RESULT.md`; result commit `c9174445f22e6df74a2c41c9cb812900f8fce5de`; aggregate job `103799287885`; aggregate artifact `10326213053`; digest `sha256:5d74fbbe1fd149bf82780510161d65d435cf9f5f4afdaf547bf4ea79b995dd9c`.

The initial run `34785141237` is infrastructure-only/non-authoritative for terminal classification: all four scientific lanes completed successfully, but the aggregate lacked SymPy. Control-only repair commit `79fd7ccabd41adc0b039994855da919645881a40` changed no frozen science.

For `Phi=B_01-B_02+B_12` on the frozen right kernel:

- quadratic Hessian rank `2`;
- inertia `(1 positive, 1 negative, 1 zero)`;
- `a=c` is an exact flat plane, `Phi=0` identically;
- the distinct quadratic-isotropic branch `a=0` is generically lifted first at quartic order with coefficient `b^2 c^2/3`.

Frozen classification:

`ITER077D_SM_RANK9_EXCESS_CONSTRAINT_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_DIAGONAL_FLAT_PLANE_AND_QUARTIC_LIFTED_SECOND_ISOTROPIC_BRANCH_EXACT_SCOPED`.

### Iter077E-SM CLOSED — source contact pullback blocker

Authoritative run `34785349590`; production head `b8813c11db038f76cee2dac06dba9d2f5879e75b`; durable result `results/ITER077E_SM_SOURCE_CONTACT_PULLBACK_SCALING_RESULT.md`; result commit `4b7e5769bbbfb155f8fd9babac912a62d8925183`.

Jobs: A `103799700694`, B `103799700807`, C `103799700655`, D `103799700692`, aggregate `103799735958`.

Aggregate artifact `10326700973`, digest `sha256:3df533b54542563b4234f6415fbb7abbc6747f815edb652e250095b62b14a2db`.

Frozen classification:

`ITER077E_SM_SOURCE_CONTACT_PULLBACK_BLOCKED_EXPLICIT_LOCAL_DISTRIBUTION_FORM_REQUIRED_NONMORSE_SCOPED`.

Execution is valid; this is a substantive scientific `BLOCKED_OBJECT_DEFINITION`, not infrastructure failure.

The frozen source snapshots establish the exact restrictor `theta(kappa B)+kappa delta^(rho,j)(B)`, the source function `B`, the spectral Feynman `i epsilon` provenance, and support at `B=0`. They do not yet freeze an explicit local scalar identity such as `delta^(rho,j)(x)=C delta(x)` or a unique scalar mollifier prescription.

On the known non-Morse germ, the ordinary scalar Dirac pullback submersion criterion fails on the exact flat family. Auxiliary even-mollifier controls give localization exponents `epsilon^(1/2)` on a quadratic branch and `epsilon^(1/4)` on the quartically lifted branch, while the exact flat family generates no shrinking localization scale; these exponents are `REGULATOR_MODEL_CONTROL_ONLY`, not a physical causal-vertex regularization.

## Conditional parallel branches

`Iter077A-FF` remains a conditional front-face algebra branch. `Iter077B-BCH` remains a coordinate-scoped BCH/K4 control. Neither can replace the source-amplitude line without an explicit pushforward theorem.

## Exact blocker

A **fully contracted source causal K5 vertex as a unique local distributional functional has not been established**.

The exceptional geometry is now sharply characterized for the first frozen rank-9 source stratum, but the local source contact distribution needed for a physical pullback/scaling statement has not yet been frozen in an explicit form sufficient to make that pullback unique.

The physical nonlinear source-to-K4 curvature remains unselected. The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps

1. **Primary source gate:** acquire and freeze the exact primary-paper definition of `delta^(rho,j)(x)` from the 2026 causal-vertex source/appendices, including whether it has an explicit local distribution formula or is defined only as a spectral boundary-value distribution. Do not replace it by an arbitrary Dirac delta or fitted mollifier.
2. If an explicit source-local form is available, prospectively preregister a dedicated pullback/scaling gate using that exact object and the Iter077D-SM non-Morse normal form.
3. Only after source-defined local contact pullback control build the frozen all-`j=1/2` complete boundary sector through all ten auxiliary-spinor integrations and four group variables and test the first potentially divergent fully contracted coefficient/regulator dependence.
4. Continue `-FF` and `-BCH` only as independent conditional lanes and never merge their classifications into the source-amplitude line without an explicit theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; no arbitrary scalar flattening of the Toller front face; retain the published spectral `i epsilon`.