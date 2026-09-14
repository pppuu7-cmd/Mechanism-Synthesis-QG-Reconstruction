#!/usr/bin/env python3
import json, pathlib, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
MATRIX = ROOT / "data/iter081a_han_causal_bridge_source_matrix.json"
OUTDIR = ROOT / "results/raw"
OUTDIR.mkdir(parents=True, exist_ok=True)

m = json.loads(MATRIX.read_text())
p = m["frozen_predicates"]
n = m["negative_controls"]

invalid = []
if "arXiv:2603.17207" not in m.get("excluded_positive_authority", []):
    invalid.append("withdrawn_2603_17207_not_quarantined")
if n.get("su2_localization_is_selector") is not False:
    invalid.append("su2_localization_illegally_promoted")
if n.get("finite_boundary_block_scalars_select_W") is not False:
    invalid.append("finite_scalar_map_illegally_promoted")
if n.get("iter080d_applies_to_fixed_finite_scalar_linear_map") is not True:
    invalid.append("iter080d_negative_control_missing")

vals = [bool(p.get(k)) for k in [
    "B1_e3_bridge", "B2_e4_bridge", "B3_e6_bridge",
    "B4_source_order_and_toller_data_preserved_in_han_stack",
    "B5_explicit_full_W_map", "B6_full_W_selection_power"]]

if invalid:
    verdict = "INVALID_IMPLEMENTATION_OR_PROVENANCE"
    classification = verdict
elif all(vals):
    verdict = "PASS_EXACT_SCOPED"
    classification = "ITER081A_SM_HAN_CAUSAL_TOLLER_BRIDGE_WITH_FULL_W_SELECTION_POWER_SOURCE_EXPLICIT_SCOPED"
elif all(vals[:4]) and not all(vals[4:]):
    verdict = "BLOCKED_SELECTOR"
    classification = "ITER081A_SM_HAN_CAUSAL_TOLLER_BRIDGE_EXISTS_BUT_FULL_W_SELECTOR_NOT_ESTABLISHED_BLOCKED_SCOPED"
else:
    verdict = "BLOCKED_OBJECT_DEFINITION"
    classification = "ITER081A_SM_HAN_UV_STACK_CAUSAL_TOLLER_BRIDGE_NOT_SOURCE_DEFINED_OBJECT_DEFINITION_BLOCKED_SCOPED"

result = {
    "gate": m["gate"],
    "verdict": verdict,
    "classification": classification,
    "predicates": p,
    "negative_controls": n,
    "invalid_reasons": invalid,
    "matrix_sha256": hashlib.sha256(MATRIX.read_bytes()).hexdigest(),
    "claim_locks_preserved": True,
}
out = OUTDIR / "iter081a_sm_aggregate.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
if invalid:
    raise SystemExit(2)
