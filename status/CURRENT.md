# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_TO_K4_PUSHFORWARD / FINITE_SPIN_OFF_SADDLE_ORIENTATION_SUPPORT / EPSILON_MINUS1_SOURCE_NUMERATOR_JACOBIAN_OBJECT / TRANSITIVE_FACE_COEFFICIENTS / CORRELATED_BOUNDARY_VALUE`

Durable result notes remain authoritative for all closed earlier iterations.

## Controlling Iter076 chain
- Iter076H: `CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED`; run `34773167108`, aggregate job `103766397967`, artifact `10322961220`, digest `sha256:933ff2ef7836a8292229b5fe32d8b8e2c613543036afa0652ee1401e3687c94b`.
- Iter076I: `SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`; run `34776104982`, aggregate job `103774413741`, artifact `10324145415`, digest `sha256:5b1f3558947d8032bd920e4ad4cd87cf5eadf5896fa982d586fbe8a8ed1d4abe`. Wedge reversal fixes the twist character, not complement support.
- Iter076J: `SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED`; run `34776203868`, aggregate job `103774690236`, artifact `10323372997`, digest `sha256:8b96d5e952a8804eaa5718a7b7c9e1bc57cccddee3e87922cc79eafaa3e4ea48`. Gauge-fixed K5 incidence fixes the unique unsigned complementary-edge support.
- Iter076K CLOSED: `SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`. Authoritative retry head `62000d2100e7d44b442f67b1e4118707bd1a9879`, run `34779234892`, aggregate job `103783117527`, artifact `10324660667`, digest `sha256:f4f51b24d519488580d06fc15ebf3c52cbe4f439a3abaae18ad79d34ba1c9dac`; A/B/C/D pass.
- Iter076L CLOSED: `REGGE_4VOLUME_ORIENTATION_SELECTS_HODGE_SIGN_SEMICLASSICAL_EXACT_BRIDGE_STILL_BLOCKED_SCOPED`. Source supplement `91384368b80deb3e432a2f1a32ae4d030ae53fbb`; prereg `96782b4fbb81e36bf8129f2c29aed78447838a3d`; run `34780504851`, aggregate artifact `10324722242`, digest `sha256:36795aa715631ea8f3eb99fc99bf19aff6b88e5c84eb0fdd91fa32db19a61673`.
- Iter076M CLOSED: `SOURCE_GROUP_AND_CAUSAL_DATA_DEFINE_NONDEGENERATE_GLOBAL_ORIENTATION_PSEUDOSCALAR_REVIEW_P3_SCOPED`. Source-variable `Omega_sigma(g)=sgn det([1; sigma_a ghat_a T])` has the required non-degenerate covariance; run `34780608763`, aggregate artifact `10324832384`, digest `sha256:d3cf6d0fe82bcc78088d29048993c4414f971cae9ae295b4997e07efc2ea1720`.
- Iter076N CLOSED: `EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED`. Source `cf9b1182a7f6f0b996b69aa78a0d58e7276eac96`; prereg `eb4f6f655b8bfeb872d6e5b945308d0c2887f9a9`; implementation `8e47c093ce54ea511f54bbd9b0864426508c0c42`; production head `b3dc5e64b5aa706c8c836d366859017d8a913c57`; run `34781543192`, aggregate job `103789370946`, artifact `10324993593`, digest `sha256:6fd653c302afc865c33296b1f540d3f9a7cc92ae48424f207ddb6a63ae22ef30`; durable result `5758d275163c5344d63fc7f59f75c85d9774cb1d`. Exact Toller restriction selects one parity/Omega sector on the non-degenerate Lorentzian Regge saddle locus only.
- Iter076O ACTIVE: `EXACT_TOLLER_OFF_SADDLE_OMEGA_SUPPORT`. Exact off-saddle spinor-support source snapshot `98fa54aab0876707bf4b6e902a7d2fc059cbe665`; prospective prereg `735a0bf1d2a7f8b9c5a13404bb4cd9b12fd8547b`, committed before implementation. Frozen test uses one fixed `1->4` causal assignment and opposite-Omega group controls to determine whether the exact Heaviside bulk support itself is a global orientation projector.

## Exact blocker
The global Hodge-sign ambiguity is resolved on the non-degenerate Lorentzian Regge saddle locus. A generic finite-spin signed source-to-K4 pushforward requires more.

Iter076O now tests the exact off-saddle support question. The source integrates an independent projective spinor `z_ab` for each wedge, and `exp(B(z,g))` is the Rayleigh quotient of `g g^dagger`. For every non-unitary relative `SL(2,C)` element, determinant one forces reciprocal positive eigenvalues above and below one, making both signs of `B` available at the single-wedge level. The prospective gate checks whether ten independent wedge choices simultaneously place opposite nonzero `Omega_sigma` group configurations in the same fixed-causal open bulk.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps
1. Implement and run the four frozen Iter076O lanes without changing criteria.
2. If both `Omega` sectors occur in exact bulk support, lock generic finite-spin signed P3 against promotion from support alone and search only for a stronger phase/contraction/interference selector.
3. If support itself fixes one sector, independently verify root/relabeling covariance before any finite-spin P3 promotion.
4. Only after the required P3 scope is settled, derive the source-induced numerator and Haar/Jacobian quadratic jet for the nominal `epsilon^-1` coefficient; independently establish the correlated Toller/group boundary value before K5 promotion.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no conclusion yet about full-amplitude survival of both off-saddle sectors; no physical causal-vertex finiteness/divergence theorem; no physical sector selection outside frozen scope; no G3 PASS or F9/G8/K5 promotion; retain the published spectral `i epsilon` and keep support, oscillatory finite part and source-defined distributional amplitude distinct.
