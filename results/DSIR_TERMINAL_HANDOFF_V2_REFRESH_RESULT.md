# DSIR terminal handoff V2 refresh — authoritative result

**Date:** 2026-09-14

## Authority

- V2 preregistration: `prereg/DSIR_TERMINAL_HANDOFF_V2_REFRESH.md`
- preregistration commit: `bec11308edab83dbbf59e0d8a88197de791fca7c`
- frozen funnel specification: `docs/DSIR_TO_POLYGON_FUNNEL_V0_2.md`
- funnel specification commit: `7db97c279736120a99f707423e459a0f9550aa35`
- initial audit implementation commit: `006569494d3cc9c2d920c86afd8e1a1254aec4b6`
- production workflow commit: `aeecc6d59ec22047b3ac28b7afaca9cf613c227f`
- control-only semantic string-lock repair: `9431460a8e8d2006e6ca4a72b704a2b3d2bdbb46`
- authoritative retry run: `34785832747`
- jobs: R2 `103801021829`, S2 `103801021694`, T2 `103801021809`, U2 `103801021807`, aggregate `103801047583`

Artifacts:

- R2 `10327010027`, `sha256:58a1d905f47345e77eb4f5d56b0a0bd2ac17f3b81b5b0b0a5e5b6a18e6205c74`
- S2 `10325884875`, `sha256:f6975580a123a4d2b760fd99bdefd6d2f90239d936df1b6cef1b32b0e753253a`
- T2 `10326412081`, `sha256:26424c0e82a254c95913404cc3dda26b53c7da798b41a98edfbc896cea8f629f`
- U2 `10326283877`, `sha256:819bcf74804f790f11ea8cdbfb88e7f605aa063da1cb9b0c832a9ed7a6fe3fa8`
- aggregate `10326826447`, `sha256:d036e455a505bee6228e7c0f4dd103ac7ba28e172d430697b6b927a7612b019f`

The authoritative retry completed with all four frozen lanes and the aggregate successful.

The initial run `34785749455` is retained as control history. S2 and T2 passed there. R2 and U2 failed only brittle machine-readable text locks: three semantically equivalent phrasing matches in R2 and the phrase `authoritative retry run` rather than the exact substring `authoritative run` in the BCH result. Commit `9431460a...` repaired only these string recognizers. No scientific predicate, classification, missing object, witness, numerical result or PASS/FAIL expectation was changed after the first run.

## Frozen classification

`DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V2_SOURCE_MAP_REFINED`

`contract_completeness_percent = 100`

Meaning: **100% handoff-contract/interface completeness only; no physical gate promotion.**

## Lane verdicts

- R2 — refreshed distributional/K5 handoff: `PASS`
- S2 — finite-scale dynamics/G3 preservation: `PASS`
- T2 — RG/CCI/F9 preservation: `PASS`
- U2 — dependency/provenance/no-hidden-choice audit: `PASS`

## Refreshed distributional/K5 handoff

The V2 record preserves the complete source-map split now established by Iter076X-Y-Z and Iter077A-F:

1. the generic true coherent-spinor source map has an open rank-10 submersion region;
2. scalar K5 cycle identities do not transfer to that generic true source differential;
3. the first frozen full-span rank-9 exceptional point is a vector-self-stress locus transverse of local codimension 3;
4. its exact mixed six-dimensional second-jet normal form is nondegenerate with determinant `-1` and inertia `(3+,3-)`;
5. the ordinary termwise point-contact Hörmander criterion fails at that frozen rank-9 point;
6. the ordinary quadratic `n_eff=0` contact channel has a unique local scaling extension;
7. in the all-`j=1/2`, gamma-simple control with finite real `gamma != 0`, the highest frozen self-stress excess order is exactly `n_eff=3` with nonzero coefficient proportional to `-8 gamma^3/(1+gamma^2)^3`;
8. that channel has scaling degree `8` in transverse dimension `6`, so scaling degree alone does not select a unique extension.

This does not establish nonexistence of the full source-selected amplitude and does not establish a causal-vertex finiteness/divergence theorem.

## Terminal V2 transfer statuses

### K5 / distributional extension

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

Broad missing object:

`SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION`

First concrete local subobject:

`SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL`

Polygon falsification/assembly test:

1. derive the exceptional extension from the published spectral `i epsilon` prescription, not an arbitrary finite part;
2. include the exact smooth Toller phases, CP1 measure, shared group variables and boundary intertwiners;
3. test whether the frozen `n_eff=3` channel survives, cancels or is uniquely fixed after the full correlated contraction;
4. classify the other rank-deficient source strata rather than extrapolating from the first rank-9 witness;
5. distinguish distributional existence, extension uniqueness, absolute integrability and regulator removal;
6. only then classify physical K5 or any full-vertex finiteness/divergence statement.

### G3 / finite-scale quantum dynamics

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

Missing object:

`CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION`

The polygon must instantiate a normalized local amplitude/measure, physical boundary spaces and gluing/composition in one realization. Source/comparator evidence is not a synthesis-derived novelty kernel.

### F9 / RG-CCI

Status:

`BLOCKED_TRANSFER_TO_POLYGON`

Missing object:

`PHYSICAL_MULTISCALE_CCI_REALIZATION`

The polygon must instantiate physical boundary spaces/projectors, dynamically justified embeddings, multi-step cylindrical consistency/CCI and Toller analytic/pole-class closure without new independent cross-branch data.

### G8

Status:

`CONVERGENCE_ONLY`

No novelty promotion is authorized by the source-map refinements.

## Coordinate sibling retained separately

`Iter077B-BCH` is exported as a coordinate-scoped derived control: the exact BCH source group law supplies a nonzero K4 cycle-curvature mechanism with coefficient `1/2` on the frozen generic controls. It remains scientifically separate from the physical coherent-spinor/Toller source-amplitude lane until an explicit source/front-face pushforward theorem is constructed.

## DSIR -> Polygon decision

The DSIR funnel is now **terminally complete at V2 under the frozen 100% interface-completeness definition**. Continuing to refine DSIR by adding unbounded downstream physics would violate the purpose of the funnel. The next constructive work should consume this versioned packet in the polygon as independent workstreams, while DSIR definitions and claim locks remain frozen unless a downstream falsification forces a versioned correction.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no K5/G3/F9/G8 promotion; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no arbitrary finite part/counterterm/fitted cancellation/preferred sequential order; retain the published spectral `i epsilon`.