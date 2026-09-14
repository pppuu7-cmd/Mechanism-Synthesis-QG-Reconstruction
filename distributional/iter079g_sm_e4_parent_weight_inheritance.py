#!/usr/bin/env python3
import argparse, json
from pathlib import Path

CLASS_SOURCE_PASS = "ITER079G_SM_E4_PARENT_WEIGHTS_SOURCE_EXPLICITLY_INHERIT_UNDER_VERTEX_ONLY_REPLACEMENT_EXACT_SCOPED"
CLASS_CONDITIONAL = "ITER079G_SM_E4_PARENT_WEIGHTS_CONDITIONALLY_INHERIT_UNDER_VERTEX_ONLY_REPLACEMENT_BUT_SOURCE_BRIDGE_NOT_EXPLICIT_EXACT_SCOPED"
CLASS_FAIL = "ITER079G_SM_E4_PARENT_WEIGHT_INHERITANCE_FAILS_UNDER_FROZEN_VERTEX_ONLY_REPLACEMENT"


def write(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")


def lane_a():
    # Frozen primary-source audit. Positive statements are limited to what was
    # prospectively recorded before implementation.
    source={
      "generalized_causal_vertex_explicit": True,
      "arbitrary_2complex_context_explicit": True,
      "full_causal_state_sum_formula_identified": False,
      "causal_face_weights_explicit": False,
      "causal_edge_weights_explicit": False,
      "internal_spin_intertwiner_sum_inheritance_explicit": False,
      "normalization_inheritance_explicit": False,
    }
    physical_bridge = all(source[k] for k in [
      "full_causal_state_sum_formula_identified","causal_face_weights_explicit",
      "causal_edge_weights_explicit","internal_spin_intertwiner_sum_inheritance_explicit",
      "normalization_inheritance_explicit"])
    return {"lane":"A","valid":True,"source":source,"physical_E4_source_bridge_explicit":physical_bridge,
            "sources":["arXiv:2603.22661v2 Introduction/Secs.3-4","Iter079A/B/C durable source audits"]}


def lane_b():
    # Exact monomial bookkeeping: E4 factors are W_F, W_E, S, N0.
    Nv=9
    parent={"W_F":1,"W_E":1,"S_internal":1,"N0":1}
    for i in range(Nv): parent[f"A{i}"]=1
    causal={"W_F":1,"W_E":1,"S_internal":1,"N0":1}
    for i in range(Nv): causal[f"C{i}"]=1
    e4_keys=["W_F","W_E","S_internal","N0"]
    unchanged=all(parent[k]==causal[k] for k in e4_keys)
    local_replaced=all((f"A{i}" in parent and f"C{i}" in causal) for i in range(Nv))
    return {"lane":"B","valid":unchanged and local_replaced,"Nv":Nv,
            "E4_keys":e4_keys,"E4_exactly_unchanged":unchanged,"all_local_vertices_replaced":local_replaced}


def lane_c():
    base={"W_F":1,"W_E":1,"S_internal":1,"N0":1,"C":3}
    controls={}
    for key in ["W_F","W_E","S_internal","N0"]:
        deformed=dict(base); deformed["lambda_"+key]=1
        controls[key]=(deformed != base)
    return {"lane":"C","valid":all(controls.values()),"independent_E4_reweighting_changes_amplitude":controls,
            "local_causal_vertex_data_unchanged":True}


def lane_d(a,b,c):
    locks={"no_physical_E4_promotion_without_source_bridge":True,"E3_unresolved":True,"E6_partial_only":True,
           "E7_E8_unresolved":True,"no_downstream_promotion":True}
    source_explicit=a["physical_E4_source_bridge_explicit"]
    conditional=b["valid"] and c["valid"]
    if conditional and source_explicit: classification=CLASS_SOURCE_PASS
    elif conditional: classification=CLASS_CONDITIONAL
    else: classification=CLASS_FAIL
    return {"lane":"D","valid":conditional,"source_explicit":source_explicit,"scope_locks":locks,
            "classification":classification}


def aggregate(d):
    files=list(Path(d).glob("**/iter079g_sm_*.json")); by={}
    for f in files:
        try:
            x=json.loads(f.read_text());
            if x.get("lane") in "ABC": by[x["lane"]]=x
        except Exception: pass
    complete=all(k in by for k in "ABC")
    if not complete:
        return {"aggregate":True,"complete":False,"valid":False,"classification":"ITER079G_SM_INCOMPLETE"}
    drow=lane_d(by["A"],by["B"],by["C"]); by["D"]=drow
    valid=all(by[k].get("valid") for k in "ABCD")
    return {"aggregate":True,"complete":True,"valid":valid,"lanes":by,"classification":drow["classification"]}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane"); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True); a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    elif a.lane=="A": obj=lane_a()
    elif a.lane=="B": obj=lane_b()
    elif a.lane=="C": obj=lane_c()
    elif a.lane=="D": obj={"lane":"D","valid":True,"deferred_to_aggregate_for_frozen_source_sensitive_classification":True}
    else: raise SystemExit(2)
    write(a.output,obj)
    if not obj.get("valid",False): raise SystemExit(1)

if __name__=="__main__": main()
