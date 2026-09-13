# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_TO_K4_PUSHFORWARD / EPSILON_MINUS1_SOURCE_NUMERATOR_JACOBIAN_OBJECT / TRANSITIVE_FACE_COEFFICIENTS / CORRELATED_BOUNDARY_VALUE`

Durable result notes remain authoritative for all closed earlier iterations.

## Controlling Iter076 chain
- Iter076H: `CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED`; run `34773167108`, aggregate job `103766397967`, artifact `10322961220`, digest `sha256:933ff2ef7836a8292229b5fe32d8b8e2c613543036afa0652ee1401e3687c94b`, durable result `0f3d872299874d6ddc14da8167a1f404ef07b6d6`.
- Iter076I: `SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`; run `34776104982`, aggregate job `103774413741`, artifact `10324145415`, digest `sha256:5b1f3558947d8032bd920e4ad4cd87cf5eadf5896fa982d586fbe8a8ed1d4abe`, durable result `fd07f0c17df3f570d07a84e551e1ee00ddb62af9`. Wedge reversal preserves the same unordered edge `6/6`; it fixes the twist character, not complement support.
- Iter076J: `SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED`; prereg `c62d638c537de5f44590c8520242c82274cf84be`, implementation `1a73a4f6a221e8d9b635a90f55aba46e4df10d66`, head `8a2526ab3cd9bb0ee5d53f2bf8673effa4a8c00f`, run `34776203868`, aggregate job `103774690236`, artifact `10323372997`, digest `sha256:8b96d5e952a8804eaa5718a7b7c9e1bc57cccddee3e87922cc79eafaa3e4ea48`, durable result `efdc7f011072d6aaa5901eb7587ca6f79a4dc3ec`. The source K5 incidence canonically fixes the unsigned complementary-edge support: unique disjoint-edge involution, S4 `720/720`, root-change `3600/3600`.
- Iter076K ACTIVE: `SOURCE_CAUSAL_DATA_HODGE_SIGN_LIFT`. Prereg `afcbd9d13833c7e4a2ff997ad49f3959726ad236` before implementation `3a6099e30c0d1760b0d09c925c4b9dfb3c444a35`. Initial production head `70ca50aecee1be7ebf911d434dbc262112f64716`, run `34776382876`, is NON-AUTHORITATIVE FOR SCIENTIFIC CLASSIFICATION because Lane A accidentally used an orientation-blind edge permutation action instead of the frozen oriented edge representation already fixed in Iter076H. The computation itself ran and returned zero signed lifts, while B/C/D passed; this is an implementation/convention regression, not a frozen scientific FAIL. Frozen criteria were not changed. Minimal control-only repair commit `62000d2100e7d44b442f67b1e4118707bd1a9879` restores the exact Iter076H oriented edge action. Authoritative retry run `34779234892` is queued. Maximum frozen PASS remains `ITER076K_SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`.

## Exact blocker
The unsigned support part of P3 is source-provenanced by Iter076J. What remains is the signed/dynamical lift. The source defines `sigma_a=±1` as ingoing/outgoing causal edge data and `kappa_ab=sigma_a sigma_b`; these must not be silently reinterpreted as a Levi-Civita orientation of the 4-simplex. Iter076K is prospectively testing whether those actual source data can supply the missing global pseudoscalar sign. Until the authoritative retry is terminal and its raw artifacts are consumed, signed Hodge/P3 remains unestablished.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps
1. Consume Iter076K authoritative retry `34779234892` raw lanes and aggregate under the unchanged frozen criteria.
2. If source causal data cannot fix the global sign, locate an explicit source contraction/orientation object before any P3 promotion; do not use raw label order as physics.
3. Only after provenance-linked signed P3 exists, derive the actual source-induced numerator and Haar/Jacobian quadratic jet and preregister the true degree-two / nominal `epsilon^-1` coefficient gate.
4. Establish the full source-backed correlated Toller/group boundary value before any K5 promotion.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no physical sector selection; no G3 PASS or F9/G8/K5 promotion; no arbitrary counterterm/fitted cancellation/preferred sequential order; retain published spectral `i epsilon`; do not replace it with `beta+i*epsilon`; keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
