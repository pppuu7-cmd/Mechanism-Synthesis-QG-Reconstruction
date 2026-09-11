#!/usr/bin/env python3
"""Fail-closed promotion gate for F9_CAUSAL_ANALYTICITY_RG_INVARIANT."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--evidence",default=str(ROOT/"data"/"f9_evidence_v0_1.json"));ap.add_argument("--output",default="results/f9_gate.json");args=ap.parse_args()
    e=json.loads(Path(args.evidence).read_text(encoding="utf-8"))
    checks={
      "same_realization":bool(e.get("same_realization")),
      "physical_boundary_projectors_defined":bool(e.get("physical_boundary_projectors_defined")),
      "dynamical_embedding_maps_defined":bool(e.get("dynamical_embedding_maps_defined")),
      "cylindrical_consistency_demonstrated":bool(e.get("cylindrical_consistency_demonstrated")),
      "cci_carc_residual_pass":e.get("cci_carc_residual") is not None and float(e["cci_carc_residual"]) <= float(e.get("cci_carc_tolerance",1e-8)),
      "toller_pole_class_closed_after_internal_sums":bool(e.get("toller_pole_class_closed_after_internal_sums")),
      "no_new_independent_cross_branch_data":bool(e.get("no_new_independent_cross_branch_data")),
      "multi_step_control":int(e.get("controlled_refinement_steps",0)) >= int(e.get("minimum_refinement_steps",2))
    }
    passed=all(checks.values());missing=[k for k,v in checks.items() if not v]
    out={"gate":e.get("gate"),"candidate":e.get("candidate"),"checks":checks,"missing":missing,"passed":passed,"verdict":"F9_PASS" if passed else "F9_BLOCKED","rule":"No partial credit promotes F9. External support for ingredients is not same-realization closure evidence."}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    # BLOCKED is a valid scientific result, so exit success unless the ledger itself is malformed.
if __name__=="__main__":main()
