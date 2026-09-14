#!/usr/bin/env python3
import argparse, json
from pathlib import Path

CLASS_PASS="ITER079I_SM_E6_QUOTIENT_FIXING_NORMALIZATION_SOURCE_EXPLICIT_EXACT_SCOPED"
CLASS_BLOCK="ITER079I_SM_E6_ORBIT_STRUCTURE_KNOWN_BUT_QUOTIENT_FIXING_NORMALIZATION_SOURCE_BRIDGE_MISSING_OBJECT_DEFINITION_BLOCKED_EXACT_SCOPED"

def write(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")

def lane_a():
    facts={"iter079f_terminal":True,"iter079h_terminal":True,"orbit_count_distinct_from_normalization":True}
    return {"lane":"A","valid":all(facts.values()),"facts":facts}

def lane_b():
    m={
      "one_common_left_orbit_per_local_vertex_established":True,
      "explicit_which_local_group_integration_removed_or_fixed":False,
      "explicit_quotient_or_fixing_measure":False,
      "explicit_normalization_convention":False,
      "explicit_KKL_gluing_compatibility_proof_for_E6":False,
      "explicit_generalized_causal_Toller_validity_proof_for_E6":False,
      "causal_vertex_finiteness_theorem":False,
    }
    required=["explicit_which_local_group_integration_removed_or_fixed","explicit_quotient_or_fixing_measure","explicit_normalization_convention","explicit_KKL_gluing_compatibility_proof_for_E6","explicit_generalized_causal_Toller_validity_proof_for_E6"]
    bridge=all(m[k] for k in required)
    return {"lane":"B","valid":True,"source_matrix":m,"required_E6_source_bridge_complete":bridge,
            "authority":["Iter079A/B/D/F/H durable audits","Beltran arXiv:2603.22661v2 frozen source scope","parent EPRL-KKL source scope"]}

def lane_c():
    a=7
    A1=1*a; A2=2*a
    return {"lane":"C","valid":A1!=A2,"base_reduced_witness":a,"c1":1,"A1":A1,"c2":2,"A2":A2,
            "gauge_invariance_preserved_under_constant_measure_rescaling":True,"normalization_changes_amplitude":A1!=A2}

def lane_d():
    locks={"no_informal_group_volume_division":True,"no_arbitrary_Haar_or_FP_normalization":True,"E7_E8_unresolved":True,"no_finiteness_promotion":True,"no_downstream_promotion":True}
    return {"lane":"D","valid":all(locks.values()),"scope_locks":locks}

def aggregate(d):
    files=list(Path(d).glob("**/iter079i_sm_*.json")); by={}
    for f in files:
        try:
            x=json.loads(f.read_text())
            if x.get("lane") in "ABCD": by[x["lane"]]=x
        except Exception: pass
    complete=all(k in by for k in "ABCD")
    valid=complete and all(by[k].get("valid") for k in "ABCD")
    if not valid: cls="ITER079I_SM_INVALID_OR_INCOMPLETE"
    else: cls=CLASS_PASS if by["B"].get("required_E6_source_bridge_complete") else CLASS_BLOCK
    return {"aggregate":True,"complete":complete,"valid":valid,"lanes":by,"classification":cls}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane"); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True); a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    else: obj={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}[a.lane]()
    write(a.output,obj)
    if not obj.get("valid",False): raise SystemExit(1)
if __name__=="__main__": main()
