# Control-only provenance repair 1 — K4 order-3 reachability Critic

Date: 2026-09-15
Role: Researcher durable-provenance repair only

## Trigger

Independent Critic run `34971934034` on head `d308cf543b8bd1b6c6dae51aef743b6e5d44f0b6` terminated `failure` with verdict `K4_ORDER3_REACHABILITY_CRITIC_INVALID_PROVENANCE`.

The failure is isolated to C0 byte-level durable-raw provenance. The Critic recomputed

`sha256(results/raw/actual_k4_order3_source_object_reachability.json) = d89153fcfd54d7b2498ff4e3581170392f53de99f52473d4888393708d4e6bbe`,

while the authoritative production run `34964010302` recorded production JSON SHA256

`60a4787f73d1b0908222ba85ae11eb3f55434465f1d1d5dcc386a090ec22957c`.

The production artifact `10394990199` has ZIP digest

`sha256:22cc7680b651802c96f5ce4ca0de8d358df6d790f6b61deccf198510d01c6c47`

and contains the exact production JSON whose SHA256 is the expected `60a4787...` value. Inspection shows the durable repository JSON is scientifically equivalent but was reserialized after production: array whitespace/line formatting differs from the exact `json.dumps(..., indent=2, sort_keys=True)` production bytes. No scientific field/value mismatch was found.

## Frozen repair

This repair is limited to replacing `results/raw/actual_k4_order3_source_object_reachability.json` with the exact UTF-8 bytes recovered from authoritative artifact `10394990199`, so its SHA256 equals the already frozen production JSON digest `60a4787f73d1b0908222ba85ae11eb3f55434465f1d1d5dcc386a090ec22957c`.

No Researcher scientific contract, requirement status, result classification, Critic criterion, Critic implementation, source authority, claim ceiling, or downstream dependency may change.

The first failed Critic run remains historical `INVALID_PROVENANCE`; it is not reinterpreted as a scientific verdict.

## Retrigger rule

After the exact artifact bytes are restored, the Critic workflow may be retriggered only by a control-only workflow-trigger change or an equivalent fresh execution on the new head. The Critic script and frozen scientific criteria must remain unchanged.

No K4 cubic-realization bridge, actual K4 coefficient extraction, or K5 order-8 calculation is authorized until a fresh terminal valid Critic classification is obtained.
