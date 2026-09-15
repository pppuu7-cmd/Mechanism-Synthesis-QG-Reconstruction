# K4 cubic-realization bridge independent Critic — implementation repair 1

Date: 2026-09-15
Role: control-only / implementation repair; no change to frozen scientific Critic contract

## Trigger

Independent Critic production run `34985145895` on head `26cb70250ce2ad3aae47dbad7262412de60721dd` terminated with process exit 2 and emitted `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_SCIENTIFIC_FAIL_SCOPED` only because check `no_k4_coefficient_claim` was false.

The audited Researcher result explicitly states both:

- `It does **not** compute the K4 polar coefficient itself.`
- under Interpretation ceiling: `This gate does **not** evaluate the K4 polar coefficient, classify it zero/nonzero, compute its annihilator...`

Therefore the failed boolean is caused by a brittle exact-phrase matcher requiring the literal string `No K4 polar coefficient`; it is not an independently demonstrated false source/mathematical claim. Under the already-frozen Critic taxonomy this historical production is `INVALID_IMPLEMENTATION`, not `SCIENTIFIC_FAIL_SCOPED`.

## Frozen repair scope

Repair only the independent Critic implementation. Do not change the parent Critic preregistration, Researcher derivation, Researcher raw result, Researcher result note, source authority, branch conventions, published spectral `i epsilon`, scientific ceiling, or terminal classification definitions.

The repaired Critic must:

1. verify the frozen durable Researcher SHA256 values already observed before this repair:
   - Researcher result `a5a48bc226847eb13526899867a32345ca54c9da3e4de6519fef3b70afc3ef4c`;
   - derivation `5587251463a7871c078eeba34aa6f37741e5cad030ca62ee3443a4114a86c686`;
   - Researcher raw `c3fd167e17b4f3cf10c69f481011d66844afd0958c6a376fb0aa8682a9fee6b7`;
   - Researcher implementation `517ca58bf73245d1105ac08fe560a3c56e7ec65c20d80f296c86428aa6a39938`.
2. parse the durable Researcher raw JSON and independently enforce its scientific ceiling: `k4_polar_coefficient_evaluated=false`, `k4_zero_or_nonzero_classified=false`, `k4_annihilator_computed=false`, `physical_finite_part_selected=false`, `k5_order8_authorized=false`, `regulator_independence_claimed=false`, `new_physics_found=false`.
3. independently re-check the exact full-matrix algebraic reconstruction in the formal `(S,N)` basis rather than accepting a Researcher verdict boolean.
4. independently re-check the exact cubic `q=2s-s^2/3+4s^3/45` by composition through order 3.
5. independently re-enumerate the five K4 blocks, six internal plus four external edges per block, 16 divergent K3/K4/K5 blocks and all 120 S5 transports.
6. verify all R1-R10 requirement states needed by the object-definition bridge from durable raw/source authority and verify all 12 malformed Researcher controls were rejected by the same Researcher validator path.
7. treat a failure of the repaired implementation itself as `INVALID_IMPLEMENTATION`; `SCIENTIFIC_FAIL_SCOPED` remains reserved for an independently false source/mathematical claim with valid implementation/provenance.

## Interpretation ceiling

This repair cannot confirm the bridge by itself, cannot compute or classify the actual K4 order-3 polar coefficient, cannot authorize K5 order 8, cannot choose a finite part, and cannot promote F9/G3 or any new-physics claim. Only a fresh terminal repaired Critic production may provide the parent Critic classification.
