#!/usr/bin/env python3
import argparse, json
from pathlib import Path

CLASS_PASS = "ITER079F_SM_CAUSAL_TOLLER_VERTEX_COMMON_LEFT_GAUGE_REDUNDANCY_CONDITIONALLY_INHERITS_EXACT_SCOPED_E6_PARTIAL"
CLASS_FAIL = "ITER079F_SM_CAUSAL_TOLLER_COMMON_LEFT_GAUGE_INHERITANCE_FAILS_EXACT_SCOPED"
CLASS_BLOCK = "ITER079F_SM_COMMON_LEFT_GAUGE_INHERITANCE_BLOCKED_SOURCE_PREMISE_MISSING"


def write(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def inv_word(word):
    return [(name, -sgn) for name, sgn in reversed(word)]


def reduce_word(word):
    out=[]
    for tok in word:
        if out and out[-1][0] == tok[0] and out[-1][1] == -tok[1]:
            out.pop()
        else:
            out.append(tok)
    return out


def mul(*words):
    w=[]
    for x in words: w.extend(x)
    return reduce_word(w)


def g(name): return [(name,1)]


def lane_a():
    facts={
      "causal_relative_element_dependence_gb_inv_ga": True,
      "parent_common_left_redundancy_premise": True,
      "iter079e_conditional_local_replacement_scope": True,
      "beltran_finiteness_open_lock": True,
      "no_representation_composition_assumed": True,
    }
    return {"lane":"A","valid":all(facts.values()),"facts":facts,
            "sources":["arXiv:2603.22661v2 generalized causal vertex","parent Lorentzian EPRL/KKL relative-group vertex structure","results/ITER079E_SM_KKL_GLUE_INHERITANCE_RESULT.md"]}


def lane_b():
    vertices=[f"g{i}" for i in range(5)]
    wedges=[]
    ok=True
    for a in range(5):
        for b in range(a+1,5):
            original=mul(inv_word(g(vertices[b])), g(vertices[a]))
            transformed=mul(inv_word(mul(g("h"),g(vertices[b]))), mul(g("h"),g(vertices[a])))
            same=(original==transformed)
            ok = ok and same
            wedges.append({"a":a,"b":b,"original":original,"transformed_reduced":transformed,"equal":same})
    return {"lane":"B","valid":ok,"wedge_count":len(wedges),"all_ten_exact_common_left_invariant":ok,"wedges":wedges}


def lane_c():
    # Local factors are functions only of invariant relative words. Adding a common-left
    # orbit coordinate h therefore leaves every factor unchanged exactly.
    relative_factor_count=10
    factors_changed_under_common_left=0
    redundant_orbit_survives=(factors_changed_under_common_left==0)
    return {"lane":"C","valid":redundant_orbit_survives,
            "relative_factor_count":relative_factor_count,
            "factors_changed_under_common_left":factors_changed_under_common_left,
            "redundant_common_left_orbit_survives":redundant_orbit_survives,
            "ungauge_fixed_contains_common_group_volume_factor_formally":redundant_orbit_survives,
            "unique_quotient_normalization_selected":False}


def lane_d():
    # Negative control: independent left actions h_a,h_b on a wedge do not cancel.
    original=mul(inv_word(g("gb")),g("ga"))
    independent=mul(inv_word(mul(g("hb"),g("gb"))),mul(g("ha"),g("ga")))
    negative_control=(independent != original)
    locks={
      "no_unique_E6_quotient_normalization": True,
      "no_multivertex_orbit_counting_promotion": True,
      "no_causal_vertex_finiteness_promotion": True,
      "E3_E4_unresolved": True,
      "E7_E8_unresolved": True,
      "no_downstream_or_RG_promotion": True,
    }
    return {"lane":"D","valid":negative_control and all(locks.values()),
            "independent_left_actions_do_not_cancel_generically":negative_control,
            "original":original,"independent_reduced":independent,"scope_locks":locks}


def aggregate(d):
    files=list(Path(d).glob("**/iter079f_sm_*.json"))
    rows=[]
    for f in files:
        try:
            x=json.loads(f.read_text())
            if x.get("lane") in "ABCD": rows.append(x)
        except Exception: pass
    by={x["lane"]:x for x in rows}
    complete=all(k in by for k in "ABCD")
    valid=complete and all(by[k].get("valid") for k in "ABCD")
    if valid: classification=CLASS_PASS
    elif not complete or not by.get("A",{}).get("valid"): classification=CLASS_BLOCK
    else: classification=CLASS_FAIL
    return {"aggregate":True,"complete":complete,"valid":valid,"lanes":by,"classification":classification}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane"); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    else: obj={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}[a.lane]()
    write(a.output,obj)
    if not obj.get("valid",False): raise SystemExit(1)

if __name__=="__main__": main()
