# Current MSQGR research state

**Date:** 2026-09-18

## Scientific ceiling and source locks

`CRQN v0.2` remains `CARRIER_SELECTED` only for established source-backed F1-F8 structure. Predictive local K5 amplitude remains `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`. Frozen all-`j=1/2` supported-extension freedom remains `dim_C F_8=377`; no physical finite-part/joint-K5 selector is known. No regulator-independence theorem, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND` or complete-QG claim is authorized.

Retain canonical ten-edge ordering, corrected Iter077 source ordering, all-32/100000-term physical source contraction, 945 exact retained matchings, exact rational arithmetic, both invariant-dual physical channels and published one-wedge spectral `i epsilon`. Iter077E/F remain quarantined. Iter077I authority remains corrected run `34786586785` from alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; historical run `34786550378` is failure/non-authority.

Source ordering remains:

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

## Established authority

K3 simple residue ZERO exact confirmed; K4 simple order-3 residue ZERO exact confirmed. Full all-32 invariant-dual K5 projective object is defined. Reusable degree-27 physical numerator DAG: commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`, production `35044686796`, canonical DAG SHA256 `f8eaaa5c7923497a67f0354a2d59475f4b6d82022e032fc005c1d9d2add69992`.

Unique degree-four non-radial S5-equivariant Kirchhoff annihilator with `v(Psi_K5)=0` is independently confirmed. Corrected projective-tangent normal-flux geometry is independently confirmed. Constant-`2x2` action closure is exactly falsified and independently confirmed.

Projective-normal 32-orbit frozen-path orders are resolved: `r_U=1` on 28 proper orbit types, `r_U=2` on masks `127,255,495`, `r_U=3` on mask `511`.

Labeled mask `511`: exact structural theorem gives `N_{1,18}=N_{2,18}=0`; with `q>=18`, exact nonzero q19 ray authority, `B_v(F^r) subset F^(r+2)` and exact nonzero q21 ray authority, frozen labeled-mask orders are `r_N=19`, `r_B=21`. This is not an all-orbit theorem. Historical direct q18 run `35259123078` is terminal cancelled with aggregate skipped and no scientific authority; do not rerun it.

## Boundary-S5 transport — independently closed

Independent Critic authority is terminal:

`results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json`

classification `CONFIRMED_EXACT_SCOPED`, run `35267432939`, job `105357990301`, head `992a5889656b2cf5925caf1c770824ab557e5833`, artifact `10516529280`, ZIP SHA256 `087ee496daf8a9aafa255d908c062fb8bba2a5481addef10da6d7b4b170cc479`, repaired result SHA256 `b0a0b94e22d76600c27c148c0072741b5e04a8652939ed58a228b9fbebda70ee`, `q18_values_used=false`.

It independently reconstructs all 32 boundary components, 100000 source terms, 945 matchings, all 120 S5 elements, exact source endpoint/orientation transport and boundary contragredient law. Boundary-S5 is no longer the current blocker.

## Frozen 34-orbit resolver — repair-1 terminal INVALID_IMPLEMENTATION

Parent scientific prereg remains immutable:

`prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Historical run `35268238924` remains `INVALID_IMPLEMENTATION`; no historical N/B coefficient/order is authority.

Prospective control-only repair-1 was frozen at commit `2193692c90d8ee1fa097200dbbac6ab70fd3a159`. Repaired production run `35271187040`, attempt 1, head `42daba28fd0c2545be386f63e89f6bcafdbed9a3`, is terminal `completed/success` at the workflow level. All eight deterministic shard jobs and aggregate job `105376689955` completed successfully.

Immutable aggregate artifact `10519073488`, ZIP SHA256 `6de47e29303091d4cabf48c59591d56634a5817be344e701b3dc435ddb1770db`. Raw `result.json` SHA256 `7c14d5746cf287d9d66872daec6334f2b8c7bb9c9f1430f6456ea3e1a3f1866e`; canonical decompressed coefficient payload SHA256 `1ebd19078b33cf6936d37d0223f2d58bbfe47d0c4866bdb6c2d7f33a06471c4d`.

The frozen aggregate classifier returns exactly:

`INVALID_IMPLEMENTATION`.

The mandatory failed control is:

`S5_full_coefficient_covariance_all = false`.

Every other aggregate control passes, including exact 32-orbit coverage, complete `N[0..27]` / `B[0..31]` vectors for all 64 channel-orbit rows and both W1/W2, route-internal exact controls, second-path class coverage, W1/W2 state/order agreement, projective-normal authority, mask511 parent reproduction and independent Boundary-S5 Critic lock.

The S5 failure is systematic: all 32 proper orbit rows fail all eight full-coefficient S5 comparison booleans (2 channels x W1/W2 x N/B). Because S5 covariance is mandatory under the frozen repair contract, no N/B coefficient/order/zero state from run `35271187040` is scientific authority despite its internal `certified_components=64` field.

Durable authority:

- `results/raw/k5_34_orbit_exact_leading_coefficient_resolution_repair1_invalid_authoritative.json`, commit `a987e7095fcb95830c917d4936cbac6d1c3bb7fc`;
- `status/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_RESOLVER_REPAIR1_INVALID.md`, commit `42c9927fca50d6d93df6b6dc962ef83c55dba2d3`.

Scientific resolver state after repair-1: `0/64` components authoritative, `64/64` unresolved.

## Active implementation-only S5 label-frame diagnostic

The common failure surface points to a possible label-frame mismatch rather than an orbit-specific arithmetic defect. This is a hypothesis only, not authority.

Prospective diagnostic contract:

`prereg/K5_34_ORBIT_RESOLVER_REPAIR1_S5_FRAME_DIAGNOSTIC.md`, commit `fb648ab3b5c5430840c8025ceb31500252c080cc`.

Implementation:

`scripts/k5_34_orbit_resolver_s5_frame_diagnostic.py`, commit `58c076610ffb8f6c495cc6de143d587324262367`.

Workflow/head commit `180d7c9e0b7990d5e150d5b2e34378e8d728aa02`; run `35280836616` is currently queued at this recovery cut.

The diagnostic records only exact equality booleans and hashes; it does not consume or emit scientific N/B orders. It tests whether repair-1 supplied a pullback-to-old-label source matching object to a route evaluated in the permuted target edge frame. No resolver repair-2 or rerun is authorized before this diagnostic is terminal.

If the frozen frame-mismatch classification is confirmed, only an implementation-only prospective repair-2 may be frozen; all physics inputs, 32 representatives, two channels, W1/W2, 945 matchings, DAG, degree ceilings, U authority, exact arithmetic, classifier meanings and interpretation ceiling must remain unchanged.

## Orthogonal graph-filtration run

Run `35268738542`, head `7ff709ee3360e5e8fa4213e293f7142e979b1c56`, failed before scientific computation with missing `EDGES` attribute. Classification: `INVALID_IMPLEMENTATION_OR_PROVENANCE_NO_SCIENTIFIC_VERDICT`. It remains quarantined and lower priority; do not repair it while the resolver S5 implementation chain is active.

## Survival chain

`F1-F8 carrier -> source-ordered K5 object -> F_8 ambiguity dim=377 -> K3 ZERO -> K4 ZERO -> K5 projective object DEFINED -> degree-4 annihilator CONFIRMED -> physical N1,N2 DAG MATERIALIZED -> tangent-flux geometry CONFIRMED -> Boundary-S5 coefficient transport INDEPENDENTLY CONFIRMED -> mask511 r_N=19,r_B=21 EXACT -> 34-orbit resolver run1 INVALID -> repair1 INVALID (systematic S5 coefficient covariance control) -> S5 label-frame diagnostic ACTIVE -> 64-component exact N/B authority ? -> local 34-orbit physical N/action/flux classification ? -> global Stokes/IBP ? -> K5 periods ? -> physical finite-part/joint selector ? -> regulator independence ? -> composition/G3 ? -> RG ? -> continuum ? -> spin-2 ? -> Einstein/GR ? -> matter/QFT ? -> normalized prediction ?`.

## Highest-information next work

1. Inspect only terminal output of run `35280836616`; do not use partial diagnostic output.
2. If exact label-frame mismatch is confirmed, freeze implementation-only repair-2 before code changes and rerun the unchanged parent resolver contract.
3. If the frame hypothesis is not confirmed, do not rerun the heavy resolver; localize the smallest remaining S5 comparison defect with a new prospective diagnostic.
4. Only a valid terminal resolver may create 64-component N/B order authority and unlock the local physical N/action/flux classifier.
5. Only after valid local classification may global projective Stokes/IBP become admissible.

Global Stokes/IBP, K5 periods, the physical finite-part/joint selector, the `377 -> ?` extension-selection problem and regulator independence remain separate downstream gates. Any mandatory blocked arrow prevents a predictive/complete-QG claim.
