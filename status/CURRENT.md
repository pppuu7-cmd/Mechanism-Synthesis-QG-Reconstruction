# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9: `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_TO_K4_PUSHFORWARD / TOLLER_CONJUGATION_CAUSAL_FACTOR_OBSTRUCTION / EPSILON_MINUS1_SOURCE_NUMERATOR_JACOBIAN_OBJECT / TRANSITIVE_FACE_COEFFICIENTS / CORRELATED_BOUNDARY_VALUE`

Durable result notes remain authoritative for all closed earlier iterations.

## Controlling Iter076 chain
- Iter076H-J: canonical twisted Hodge generator, reversal twist character, and unique unsigned K4 complement support are closed exact scoped results.
- Iter076K CLOSED: the source causal data fix the signed Hodge line but not its global sign.
- Iter076L CLOSED: Regge 4-volume orientation has the correct selector character only in semiclassical scope.
- Iter076M CLOSED: the exact source variables admit the non-degenerate pseudoscalar `Omega_sigma(g)=sgn det([1; sigma_a ghat_a T])`.
- Iter076N CLOSED: `EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED`; run `34781543192`, aggregate artifact `10324993593`, digest `sha256:6fd653c302afc865c33296b1f540d3f9a7cc92ae48424f207ddb6a63ae22ef30`; durable result `5758d275163c5344d63fc7f59f75c85d9774cb1d`.
- Iter076O CLOSED: `EXACT_TOLLER_BULK_SUPPORT_CONTAINS_BOTH_OMEGA_SECTORS_OFF_SADDLE_NO_GLOBAL_FINITE_SPIN_SELECTOR_SCOPED`. Source `98fa54aab0876707bf4b6e902a7d2fc059cbe665`; prereg `735a0bf1d2a7f8b9c5a13404bb4cd9b12fd8547b`; implementation `e9ba9d9bcb1218e821657456fb2987a63532c4bd`; production head `164bb65fa8b120c6e6d697bb2f75b433ac5e92e9`; run `34781757359`, aggregate artifact `10324732666`, digest `sha256:e40cbcf8d6372c8718b388b6c078a9bb9b9c24fc7eec64789b0bc2e71b00a0f8`; durable result `eb1800ddaa27dd5026ffebbd11106dc0335a2546`. Exact open bulk support contains both nonzero `Omega_sigma` sectors for one fixed `1->4` causal assignment.
- Iter076P ACTIVE: `TOLLER_CONJUGATION_CAUSAL_FACTOR_OBSTRUCTION`. Companion-paper source snapshot `eb40c0a321dbaa7bd8a838bc7206a29eb22686f7`; prospective prereg `a0730079deede85153deebd4380b80c6a04bdf95`, both committed before implementation. The exact reduced Toller conjugation identity flips `kappa -> -kappa`; the frozen gate tests whether this all-wedge flip remains in the source image `kappa_ab=sigma_a sigma_b`.

## Exact blocker
Iter076O rules out exact Toller **support alone** as a generic finite-spin orientation projector. The companion Toller paper supplies an exact complex-conjugation identity that flips the reduced Toller branch. If applied to every wedge of a causal K5 vertex, it sends `kappa_ab` to `-kappa_ab`.

Iter076P tests whether that flipped ten-wedge pattern is realizable by any source edge-sign assignment. If not, the known conjugation identity cannot furnish a same-causal pairing/cancellation of opposite `Omega_sigma` sectors, and a different parity/boundary/interference mechanism would still be required.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`.

## Next admissible steps
1. Implement and run the frozen Iter076P causal-image and triangle-obstruction census.
2. If conjugation exits the causal K5 image, do not use it to infer same-causal amplitude cancellation; search separately for an exact parity or boundary-state transformation, or keep signed P3 `SADDLE_EFFECTIVE_ONLY`.
3. Only after P3 scope is settled, derive the source numerator/Haar-Jacobian quadratic jet for the nominal `epsilon^-1` gate.
4. Independently establish the correlated Toller/group boundary value before K5 promotion.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no full-amplitude cancellation/non-cancellation theorem; no G3 PASS or F9/G8/K5 promotion; retain the published spectral `i epsilon`.
