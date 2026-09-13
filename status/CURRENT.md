# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_TO_K4_PUSHFORWARD / EPSILON_MINUS1_SOURCE_NUMERATOR_JACOBIAN_OBJECT / TRANSITIVE_FACE_COEFFICIENTS / CORRELATED_BOUNDARY_VALUE`

Durable result notes remain authoritative for all closed earlier iterations. The controlling frontier is the Iter076 chain below.

## Iter076 controlling chain

- Iter076A: `TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_EXACT_SCOPED`; authoritative retry run `34758521734`, job `103727049365`, artifact `10318116775`, digest `sha256:23edf7fc462f8b2e9cf82a2c1701b4fcde7c6bbd4ffcbd0e5f5f2011c7e07f31`.
- Iter076B: `TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_EXACT_COVARIANT_SCOPED`; run `34761228718`, aggregate job `103734341502`, artifact `10318722679`, digest `sha256:dc73bd0be09b53029160ae841189e315f21427b0d02508872079dd83d44fd005`. Degree-two data survive on some overlap strata; nominal `epsilon^-1` is therefore not automatically cancelled.
- Iter076C: `BLOCKED_SOURCE_TO_K4_PUSHFORWARD_OR_QUADRATIC_DENSITY_MISSING`; durable commit `b9f5875002695fdd1f7e164fdba66cfeaf16b406`. First missing object localized to P3, a source-to-K4 map/pushforward.
- Iter076D: `SOURCE_DOMAIN_HAAR_AND_RELATIVE_GROUP_QUADRATIC_JETS_EXACT_SCOPED`; run `34764323602`, aggregate artifact `10319059815`, digest `sha256:b38e6aa9f52a4fde2f924604303ff2971141398f7a30b91746a0f1e4c046d84b`. Source-domain Haar/BCH jets pinned; P3 not established.
- Iter076E: `SOURCE_RELATIVE_TANGENT_IS_CUT_SPACE_K4_CYCLE_IDENTIFICATION_REQUIRES_EXTRA_MAP_SCOPED`; run `34767157817`, aggregate artifact `10320284136`, digest `sha256:aaf2db22769c52dc25c57e21fb90697c1f22900e52d6abefab31edb9e4848ae4`. K4 cut and cycle spaces are both 3D but have trivial intersection.
- Iter076F: `K4_CUT_CYCLE_INTERTWINER_REQUIRES_ORIENTATION_SIGN_TWIST_EXACT_SCOPED`; run `34770168382`, aggregate artifact `10321462832`, digest `sha256:906db2edb7ca7e277e9f867c25559f94a0f85254570a78a0bab8376ecb83d5c8`. Untwisted Hom dimension `0`; sign-twisted Hom dimension exactly `1`.
- Iter076G: `EQUAL_SPIN_SOURCE_REVERSAL_CHARACTER_MATCHES_REQUIRED_S4_TWIST_EXACT_SCOPED`; run `34771963533`, aggregate artifact `10322715108`, digest `sha256:4c6166a16e2136a4d537798110645404814df7d2b244cbcdba045ec7a37ee6f6`. Source-backed equal-spin reversal parity equals `sgn(p)` on `24/24` S4 elements; character-level compatibility only.
- Iter076H: `CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED`; prereg `55414a04426227d1627220075c29f5ee50918319`, implementation `52740b63958af8515c913f45de2a49fe24c5cfab`, head `4d5fc2b259d05a08e5038a67f4cb933584359e1d`, run `34773167108`, aggregate job `103766397967`, artifact `10322961220`, digest `sha256:933ff2ef7836a8292229b5fe32d8b8e2c613543036afa0652ee1401e3687c94b`, durable result commit `0f3d872299874d6ddc14da8167a1f404ef07b6d6`. Canonical tetrahedral Hodge complement exactly realizes the unique twisted algebraic generator, but source selection is not established.
- Iter076I: `SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED`; prereg `f0b7aa3bd65c10b85daab85c92589986b845d132`, implementation `fff3b08f4740fa1aff8fc01965e6fd0d1d06beb4`, production head `4b05324531f982d93df3c0dd8b56b58668670bf0`, run `34776104982`, aggregate job `103774413741`, artifact `10324145415`, digest `sha256:5b1f3558947d8032bd920e4ad4cd87cf5eadf5896fa982d586fbe8a8ed1d4abe`, durable result commit `fd07f0c17df3f570d07a84e551e1ee00ddb62af9`. Source reversal preserves the same unordered edge in `6/6`; source-vs-Hodge support Hamming distance is `12`; magnetic swap has zero cross-edge support for tested `2j=1..4`; source parity still matches `sgn(p)` `24/24`. This is a provenance blocker, not a causal-vertex scientific FAIL.
- Iter076J ACTIVE: `GAUGE_FIXED_K5_COMPLEMENT_SUPPORT`. Prereg `c62d638c537de5f44590c8520242c82274cf84be`, implementation `1a73a4f6a221e8d9b635a90f55aba46e4df10d66`, production/workflow head `8a2526ab3cd9bb0ee5d53f2bf8673effa4a8c00f`, run `34776203868`. Frozen gate asks whether the source Eq.(4) K5 incidence plus gauge root canonically fixes the **unsigned** complement-edge support on the six internal K4 wedges. It cannot promote signed Hodge/P3 by itself.

## Exact blocker

The full-group source carrier and reduced K4 collision geometry are independently represented, but the connecting physical pushforward is not. Iter076E-F isolate the algebraic cut-to-cycle problem; Iter076G-H identify the required sign character and its canonical Hodge realization; Iter076I shows wedge reversal/magnetic transport alone does not generate complementary-edge support. Iter076J now tests whether that support instead follows canonically from the larger gauge-fixed K5 source incidence.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Next admissible steps

1. Consume all Iter076J raw lanes and aggregate without changing frozen criteria.
2. If Iter076J passes, the remaining P3 provenance question is the **signed/dynamical** lift: whether source orientation/contraction/intertwiner structure selects the Hodge sign and cut-to-cycle action, not merely whether complement support is combinatorially available.
3. Only after a provenance-linked P3 exists, derive the actual source-induced numerator and Haar/Jacobian through quadratic order and preregister the true degree-two / nominal `epsilon^-1` overlap-coefficient gate.
4. Establish the full source-backed correlated Toller/group boundary value and Eq.(5)/(6) compatibility before any K5 promotion.

Do not launch denominator-only density/quadrature, arbitrary quadratic coefficients, fitted cancellations, preferred trees/orders, or repetitive symmetry tests solely to keep runners busy.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no physical sector selection; no G3 PASS or F9/G8/K5 promotion; no arbitrary counterterm/fitted cancellation/preferred sequential order; retain published spectral `i epsilon`; do not replace it with `beta+i*epsilon`; keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
