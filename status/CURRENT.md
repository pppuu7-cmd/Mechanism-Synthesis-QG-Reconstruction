# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_TO_K4_PUSHFORWARD / EXACT_ORIENTATION_SELECTION_PROVENANCE / EPSILON_MINUS1_SOURCE_NUMERATOR_JACOBIAN_OBJECT / TRANSITIVE_FACE_COEFFICIENTS / CORRELATED_BOUNDARY_VALUE`

Durable result notes remain authoritative for all closed earlier iterations.

## Controlling Iter076 chain
- Iter076H: `CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED`; run `34773167108`, aggregate job `103766397967`, artifact `10322961220`, digest `sha256:933ff2ef7836a8292229b5fe32d8b8e2c613543036afa0652ee1401e3687c94b`.
- Iter076I: `SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`; run `34776104982`, aggregate job `103774413741`, artifact `10324145415`, digest `sha256:5b1f3558947d8032bd920e4ad4cd87cf5eadf5896fa982d586fbe8a8ed1d4abe`. Wedge reversal fixes the twist character, not complement support.
- Iter076J: `SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED`; run `34776203868`, aggregate job `103774690236`, artifact `10323372997`, digest `sha256:8b96d5e952a8804eaa5718a7b7c9e1bc57cccddee3e87922cc79eafaa3e4ea48`. Gauge-fixed K5 incidence fixes the unique unsigned complementary-edge support.
- Iter076K CLOSED: `SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`. Authoritative retry head `62000d2100e7d44b442f67b1e4118707bd1a9879`, run `34779234892`, aggregate job `103783117527`, artifact `10324660667`, digest `sha256:f4f51b24d519488580d06fc15ebf3c52cbe4f439a3abaae18ad79d34ba1c9dac`; A/B/C/D pass. Exactly two lifts `+H/-H` survive, while exhaustive `sigma/kappa` censuses supply no sign-equivariant selector.
- Iter076L CLOSED: `REGGE_4VOLUME_ORIENTATION_SELECTS_HODGE_SIGN_SEMICLASSICAL_EXACT_BRIDGE_STILL_BLOCKED_SCOPED`. Source supplement `91384368b80deb3e432a2f1a32ae4d030ae53fbb`; prereg `96782b4fbb81e36bf8129f2c29aed78447838a3d`; implementation `67d9c618945205de4ee836ea31ecaf1f08ddf487`; production head `7ac6470c9959de272c1b1efe0b7d5def7001443d`; run `34780504851`, aggregate job `103786559383`, artifact `10324722242`, digest `sha256:36795aa715631ea8f3eb99fc99bf19aff6b88e5c84eb0fdd91fa32db19a61673`; all A/B/C/D pass, `scope=SEMICLASSICAL_ONLY`. Regge 4-volume has exactly the needed pseudoscalar character but is not an exact Eq.(4) selector.
- Iter076M CLOSED: `SOURCE_GROUP_AND_CAUSAL_DATA_DEFINE_NONDEGENERATE_GLOBAL_ORIENTATION_PSEUDOSCALAR_REVIEW_P3_SCOPED`. Proper-vertex orientation snapshot `83339c7ff5ef46dd28f30edcc35ffa4278d0b518`; frozen candidate prereg `0ba0b8026f478ae8e4add2e2f0a9169db6a88afc`; implementation `e6a027fe8d2bae02e76ea82c5a39c65d58e7b9da`; production head `5989d115d27099e993fb8bfd4fed5f6e45cadafe`; run `34780608763`, aggregate job `103786841412`, artifact `10324832384`, digest `sha256:d3cf6d0fe82bcc78088d29048993c4414f971cae9ae295b4997e07efc2ea1720`; all A/B/C/D pass and aggregate is valid. On the non-degenerate locus the exact source-variable candidate `Omega_sigma(g)=sgn det([1; sigma_a ghat_a T])` is proper-Lorentz-gauge invariant, invariant under global causal reversal, S5 sign-equivariant, compatible with proper-vertex orientation products, and undefined rather than fitted at degeneracy.

## Exact blocker
Iter076L shows that Regge 4-volume has exactly the missing pseudoscalar character. Iter076M strengthens this: the exact causal-vertex variable set `(g_a,sigma_a)` itself admits a non-degenerate global pseudoscalar with the required covariance, so the blocker is no longer the mathematical availability of a sign.

The remaining blocker is **amplitude-selection provenance**. Physical signed `SOURCE_TO_K4_PUSHFORWARD` still requires evidence that the causal Eq.(4)/Eq.(7) Toller/intertwiner/contraction structure actually selects `Omega_sigma` (or an equivalent orientation-odd factor), rather than this sign merely being constructible from integration variables.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps
1. Preregister an exact amplitude-selection provenance gate: search/derive Eq.(4)/Eq.(7), magnetic contractions, intertwiners, and source orientation/order data for an occurrence of `Omega_sigma` or an equivalent orientation-odd factor. Mere constructibility from `(g_a,sigma_a)` is insufficient.
2. If such an exact selector is source-provenanced, test that coupling it to the unique Iter076H/K Hodge line yields a root/relabeling-covariant signed P3 before any promotion.
3. Only after a provenance-linked exact signed P3 exists, derive the actual source-induced numerator and Haar/Jacobian quadratic jet and preregister the true degree-two / nominal `epsilon^-1` coefficient gate.
4. Establish the full source-backed correlated Toller/group boundary value before any K5 promotion.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no physical sector selection; no G3 PASS or F9/G8/K5 promotion; no arbitrary counterterm/fitted cancellation/preferred sequential order; retain published spectral `i epsilon`; do not replace it with `beta+i*epsilon`; keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
