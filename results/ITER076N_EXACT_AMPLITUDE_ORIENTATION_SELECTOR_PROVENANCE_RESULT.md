# Iter076N result — exact amplitude orientation-selector provenance

**Date:** 2026-09-13

## Authority

- source supplement: commit `798b11ff86a69a0a097ecaba5ba5d18c85ba9a03`
- preregistration: commit `acba023513c7002d96dc135b3066be69d85dd333`
- implementation: commit `cc178ea1b5285c4d288fa51689eb14f999b3e723`
- production head/workflow: commit `d91be903ded34b52d05ae6fbdfb3a78eea49604f`
- run: `34781560893`
- aggregate job: `103789422732`
- aggregate artifact: `10324448025`
- aggregate digest: `sha256:a9af4314e3bc2a6050c8505512a35ff1ea8dbf6b4f2848d2720d00b77f4f5bc2`

Raw lane artifacts:

- A: artifact `10325381723`, digest `sha256:dac35cecfdd09e537964a360d0b3f5013dd0ba62772da69f286ffd674caebf00`
- B: artifact `10324537721`, digest `sha256:e261d323639af9f8a253e1293bc69275364257f4768c5d900c8538e0806f8a04`
- C: artifact `10325547303`, digest `sha256:3c38dca4862204f1065bca2bc3a5e83dd2c30678c019914c444acb5fe47db082`
- D: artifact `10325577066`, digest `sha256:8f0c035407341c5c8e912b478075c7a1a0114b919df236577dfd5931e0cf6227`

## Frozen classification

`ITER076N_EQ4_EQ7_HAVE_NO_CANONICAL_S5_ODD_SELECTOR_EXACT_SIGNED_P3_BLOCKED_SEMICLASSICAL_ONLY_SCOPED`

All lanes A/B/C/D passed and aggregate `valid=true`.

## Lane A — exact Eq.(4) scalar character

All `120` permutations were enumerated (`60` even, `60` odd). The ten wedge slots map bijectively to themselves. Simultaneous reindexing of the displayed commutative wedge product and identical Haar product measure contributes only explicit scalar coefficient `+1`.

Therefore the displayed Eq.(4) product/measure skeleton contains no alternating `S5` scalar prefactor.

## Lane B — causal-data obstruction

For the three causal `kappa` orbit classes, odd stabilizers exist in every case:

- `0/5`: stabilizer `120`, odd `60`;
- `1/4`: stabilizer `24`, odd `12`;
- `2/3`: stabilizer `12`, odd `6`.

Hence any alternating scalar depending only on `sigma/kappa` is forced to vanish. This reproduces the Iter076K obstruction in the exact provenance setting.

## Lane C — availability is not selection

A rational non-degenerate exact-variable control gave

`Delta_sigma = -840/26423 != 0`.

Across all `120` permutations,

`Omega_sigma(pi.x) = sgn(pi) Omega_sigma(x)`

with zero mismatches, while the explicit Eq.(4) product/measure coefficient remains character `+1`.

Thus the exact integration-variable set admits the desired pseudoscalar, but the published source kernel does not select it merely by containing those variables.

## Lane D — generic boundary-state firewall

The source amplitude acts on generic spin-network boundary states with arbitrary intertwiner input. A symmetric boundary-slot control is fixed by all `120` label permutations, including all `60` odd permutations. Therefore the source boundary state space is not restricted to the alternating one-dimensional representation.

An alternating boundary state could be chosen, but that would be extra state selection, not a universal amplitude-level orientation selector.

## Scientific consequence

The source-native exact signed-P3 lane terminates here.

- Iter076H unique Hodge line remains valid.
- Iter076L semiclassical Regge orientation remains valid.
- Iter076M exact-variable `Omega_sigma(g)` availability remains valid.
- No physical exact signed `SOURCE_TO_K4_PUSHFORWARD` is promoted.
- Iter076O source-native signed-P3 assembly is `NOT_APPLICABLE_SOURCE_NATIVE` unless a new primary source changes the provenance record.
- Any proper-vertex-style orientation insertion belongs to an explicitly separate polygon extension branch.
- The signed-P3-dependent source numerator/Haar-Jacobian `epsilon^-1` coefficient remains undefined, not zero/nonzero/divergent.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no G3/F9/G8/K5 promotion; no physical finiteness/divergence theorem; no arbitrary orientation convention or counterterm; retain the published spectral `i epsilon` prescription.
