# Iter076D result — source-domain Haar and relative-group quadratic jets

Date: 2026-09-13

## Classification

`ITER076D_SOURCE_DOMAIN_HAAR_AND_RELATIVE_GROUP_QUADRATIC_JETS_EXACT_SCOPED`

This is a scoped scientific PASS for source-domain local prerequisites only. It does **not** establish the source-to-K4 pushforward, the induced K4 numerator/Jacobian, the nominal `epsilon^-1` coefficient, or any physical causal-vertex finiteness/divergence theorem.

## Authority

- Prospective preregistration: `9fd96d9274b3b787364ae8aed97c1b4ae31bb017`
- Implementation: `ccf7e572658e6b43da513820266ac79c72f7e9da`
- Frozen aggregate implementation: `f0f5adfd9081160db5c6dbcb15ca85386476dd63`
- Production head: `53102a0044c776f3a9e9a5861cf619e6cc45d06b`
- Run: `34764323602`
- Jobs: A `103742482686`, B `103742482592`, C `103742482745`, D `103742482721`, aggregate `103742528015`
- Artifacts: A `10320185467` (`sha256:70d975b568f0727fb1053f8a73a7ce8a9abbaeebefa06a9f902b5fe7a5480fa8`), B `10319434790` (`sha256:f702be8f5d47a7baaeaa531627a072c75c9ed43d1e98bc85559b6ab355e4f7e7`), C `10319788790` (`sha256:0134a98dca89277e8ed672fc56e0a304879e328591cf09a44e576dfe66ab0af1`), D `10319594278` (`sha256:625b65cb18b56bf2c1fcae16825e61841581ce6524736490a1a0bf5f5f8bff04`), aggregate `10319059815` (`sha256:b38e6aa9f52a4fde2f924604303ff2971141398f7a30b91746a0f1e4c046d84b`).

## Raw-lane classification

- **Lane A PASS:** exact local radial Haar/KAK factor has series `1 + beta^2/3 + 2 beta^4/45 + O(beta^6)`; constant and quadratic/quartic coefficients are exact and odd terms vanish.
- **Lane B PASS:** independent high-precision finite-beta estimator converges strictly to the quadratic coefficient `1/3`; final error is below frozen `2e-5`; flat-density control is rejected.
- **Lane C PASS:** BCH expansion for the relative argument is exact through quadratic order, with the frozen order-reversal relation also exact through `t^2`.
- **Lane D PASS:** deliberately wrong BCH sign and flat radial-density controls are rejected; scope guard explicitly keeps `K4_PUSHFORWARD_NOT_ESTABLISHED`.
- **Aggregate PASS:** all A/B/C/D valid; frozen classification emitted exactly `ITER076D_SOURCE_DOMAIN_HAAR_AND_RELATIVE_GROUP_QUADRATIC_JETS_EXACT_SCOPED`.

## Scientific meaning

The source-domain local geometry needed for any later pushforward is now pinned at two independent levels: the local Haar/KAK radial density and the local relative-group BCH jet. These are genuine prerequisites for an induced quadratic density, but they do not choose or derive the reduced three-dimensional K4 collision/cycle coordinates.

Therefore Iter076C's P3 blocker is narrowed but not removed: the missing object is now specifically a provenance-preserving map/projection/pushforward from the full relative-group tangent data to the reduced K4 collision variables. No arbitrary Euclidean metric, fitted quadratic coefficient, preferred tree/order, or denominator-only substitution is authorized.

## Next admissible gate

Audit the exact linearized source relative-coordinate complex induced by `g_b^-1 g_a` and compare its rank/kernel/cut-vs-cycle structure with the reduced K4 cycle-space object. This comparison must be preregistered before implementation. A PASS may establish only whether a nontrivial projection/dualization is mathematically required; it cannot itself define the physical pushforward or coefficient.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no physical sector selection; no G3/F9/G8/K5 promotion; retain source spectral `i epsilon`; distinguish source-domain local jets, source-to-K4 pushforward, induced numerator/Jacobian, overlap coefficient and correlated boundary value.
