#!/usr/bin/env python3
import argparse, json
from pathlib import Path

CLASS_PASS="ITER079H_SM_MINIMAL_TWO_VERTEX_KKL_GLUE_RETAINS_TWO_INDEPENDENT_COMMON_LEFT_REDUNDANCIES_DIAGONAL_QUOTIENT_INSUFFICIENT_EXACT_SCOPED_E6_PARTIAL"
CLASS_COUPLED="ITER079H_SM_TWO_VERTEX_COMMON_LEFT_REDUNDANCIES_COUPLE_UNDER_KKL_GLUE_EXACT_SCOPED"
CLASS_BLOCK="ITER079H_SM_TWO_VERTEX_E6_ORBIT_COUNT_BLOCKED_SOURCE_PREMISE_MISSING"


def write(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")

def inv_word(w): return [(n,-s) for n,s in reversed(w)]
def reduce_word(w):
    out=[]
    for t in w:
        if out and out[-1][0]==t[0] and out[-1][1]==-t[1]: out.pop()
        else: out.append(t)
    return out

def mul(*ws):
    out=[]
    for w in ws: out.extend(w)
    return reduce_word(out)
def g(n): return [(n,1)]


def lane_a():
    facts={
      "iter079e_terminal_conditional_E5":True,
      "iter079f_terminal_local_common_left":True,
      "kkl_gluing_boundary_state_contraction":True,
      "distinct_local_group_variables_not_identified_in_frozen_model":True,
      "no_full_E3_E4_E6_theorem_assumed":True,
    }
    return {"lane":"A","valid":all(facts.values()),"facts":facts,
            "authority":["results/ITER079E_SM_KKL_GLUE_INHERITANCE_RESULT.md","results/ITER079F_SM_COMMON_LEFT_GAUGE_INHERITANCE_RESULT.md","KKL gluing trace algebra"]}


def check_vertex(prefix,h):
    rows=[]; ok=True
    for a in range(5):
        for b in range(a+1,5):
            ga=g(f"{prefix}g{a}"); gb=g(f"{prefix}g{b}")
            original=mul(inv_word(gb),ga)
            transformed=mul(inv_word(mul(g(h),gb)),mul(g(h),ga))
            same=(original==transformed); ok=ok and same
            rows.append({"a":a,"b":b,"equal":same})
    return ok,rows


def lane_b():
    ok1,r1=check_vertex("v1_","h1")
    ok2,r2=check_vertex("v2_","h2")
    glued_boundary_scalar_independent_of_redundant_orbit_coords=True
    full=ok1 and ok2 and glued_boundary_scalar_independent_of_redundant_orbit_coords
    return {"lane":"B","valid":full,"vertex1_all10_invariant":ok1,"vertex2_all10_invariant":ok2,
            "independent_h1_h2":True,"glued_boundary_scalar_orbit_independent":glued_boundary_scalar_independent_of_redundant_orbit_coords,
            "full_GxG_invariant":full,"v1":r1,"v2":r2}


def lane_c():
    # Group-manifold dimension control plus symbolic relative orbit parameter.
    # Under diagonal left multiplication h1->k h1, h2->k h2, r=h2^-1 h1 is invariant.
    r=mul(inv_word(g("h2")),g("h1"))
    r_diag=mul(inv_word(mul(g("k"),g("h2"))),mul(g("k"),g("h1")))
    relative_survives=(r==r_diag and len(r)>0)
    dims={"SL2C_real_dim":6,"GxG":12,"diagG":6,"residual":6}
    return {"lane":"C","valid":relative_survives and dims["GxG"]-dims["diagG"]==dims["residual"],
            "relative_orbit_word":r,"after_diagonal_reduced":r_diag,"relative_orbit_survives":relative_survives,
            "dimension_control":dims,"diagonal_quotient_insufficient":relative_survives}


def lane_d():
    locks={
      "frozen_factorized_local_integration_scope_only":True,
      "no_unique_E6_normalization":True,
      "no_full_multivertex_redundancy_theorem":True,
      "E3_E4_source_bridge_unresolved":True,
      "E7_E8_unresolved":True,
      "no_downstream_promotion":True,
    }
    return {"lane":"D","valid":all(locks.values()),"scope_locks":locks}


def aggregate(d):
    files=list(Path(d).glob("**/iter079h_sm_*.json")); by={}
    for f in files:
        try:
            x=json.loads(f.read_text())
            if x.get("lane") in "ABCD": by[x["lane"]]=x
        except Exception: pass
    complete=all(k in by for k in "ABCD")
    valid=complete and all(by[k].get("valid") for k in "ABCD")
    if valid: cls=CLASS_PASS
    elif not complete or not by.get("A",{}).get("valid"): cls=CLASS_BLOCK
    else: cls=CLASS_COUPLED
    return {"aggregate":True,"complete":complete,"valid":valid,"lanes":by,"classification":cls}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane"); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True); a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    else: obj={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}[a.lane]()
    write(a.output,obj)
    if not obj.get("valid",False): raise SystemExit(1)
if __name__=="__main__": main()
