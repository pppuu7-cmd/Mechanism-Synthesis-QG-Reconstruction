# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- First MSQGR-derived prospective selector: Causal Cylindrical Intertwining (CCI)
  - `P_b'^± iota_b'b = iota_b'b P_b^±`
  - common-space/linearized form: `P_± R - R P_± = 0`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY` until physical F9/F10 evidence exists
- Active programme front: `ITERATION_027 / CONDITIONAL_FINITE_CAUSAL_CARRIER_AUDIT`

## What is established

1. The repository has a source-backed Lorentzian EPRL/Toller computational carrier and explicit causal/co-causal branch machinery.
2. The gamma-simple single-mode blocking ansatz is excluded by the half-integer mismatch `N=n1+n2+1/2`; this does not exclude superposition embeddings or a full RG map.
3. Multi-collision radial power counting gives a serious finiteness warning:
   - k=3 is approximately logarithmically borderline;
   - k=4 and k=5 fail absolute first-moment power counting on tested generic collision rays;
   - the ordinary EPRL control remains regular on the same tests.
4. Summing the tested causal sectors and performing the tested j=1/2 K5 boundary-intertwiner contraction did not remove the naive radial multi-pole scaling.
5. The published Appendix-D j=1/2 boundary distribution has been implemented and validated as a distributional primitive; this does not yet define products of several boundary distributions at intersecting wedge singularities.

## Active parallel computations

### Iter026 — antipodal angular cancellation

Run `34666284649`, 6 gamma/seed lanes.

Tests whether the leading homogeneous coefficient cancels between `+Omega` and `-Omega` after full tested boundary contraction and `Cboth32` causal+co-causal summation.

### Iter027A — global full-sphere angular cancellation

Run launched from commit `2c54298ec327e807fc617fa3708159aff5fc18d0`, 6 gamma/seed lanes.

Tests the normalized full-sphere angular mean of the leading homogeneous coefficient.  This is independent of the antipodal test and can detect more complicated non-pairwise angular cancellation.

### Iter027B — general-j Appendix-D authority

Run launched from commit `08e7233498eca5ae7bb8dab33fd79a414d55d64f`, 6 rho/j lanes for `j=1` and `j=3/2`.

Tests exact product-polynomial identity, complementary distribution identity, and higher-delta-derivative mollifier convergence beyond the minimal `j=1/2` representation.

## Current decisive target

The causal carrier must survive a finite, dynamically justified same-realization refinement/coarse-graining construction.  The immediate blocker is now sharper:

`MULTI_COLLISION_FINITE_DISTRIBUTIONAL_COMPOSITION_NOT_YET_ESTABLISHED`

If the angular tests fail to provide a conditional-cancellation route, the next legitimate step is not to weaken the radial criterion.  It is to formulate the exact multi-wedge product/intersection problem under the published spectral `i epsilon` prescription (or an equivalent source-backed distributional construction) and determine whether the full boundary amplitude is a well-defined distribution.

Only after finiteness/distributional composition is controlled should the programme promote the physical CCI/F9 refinement test.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no claim that causal EPRL is finite nonperturbatively;
- no claim that the current radial warning is a universal no-go theorem;
- no F9 promotion from convergence-only evidence;
- no G8 novelty promotion before physical F9/F10 evidence;
- workflow success alone is not a scientific PASS; raw artifacts must be consumed.
