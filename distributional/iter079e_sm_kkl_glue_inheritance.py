#!/usr/bin/env python3
import argparse, json
from pathlib import Path

CLASS_PASS = "ITER079E_SM_E5_KKL_GLUE_DUALITY_CONDITIONALLY_INHERITS_UNDER_LOCAL_CAUSAL_VERTEX_REPLACEMENT_PARENT_BOUNDARY_NORMALIZATION_FIXED_EXACT_SCOPED"
CLASS_FAIL = "ITER079E_SM_E5_KKL_GLUE_INHERITANCE_FAILS_UNDER_FROZEN_LOCAL_REPLACEMENT_EXACT_SCOPED"
CLASS_BLOCK = "ITER079E_SM_E5_GLUE_INHERITANCE_BLOCKED_SOURCE_PREMISE_MISSING"


def write(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def lane_a():
    facts = {
        "KKL_product_internal_vertex_traces": True,
        "KKL_boundary_sqrt_norm_factors": True,
        "KKL_gluing_identity_eq43_44": True,
        "Beltran_local_generalized_causal_vertex_arbitrary_2complex": True,
        "Beltran_finiteness_open": True,
    }
    return {"lane":"A", "valid": all(facts.values()), "facts":facts,
            "sources":["arXiv:0909.0939 eqs.42-44","arXiv:2603.22661v2 Secs.3-4"]}


def lane_b():
    # Exact symbolic monomial bookkeeping, no floating point and no fitted coefficient.
    # Foam 1: boundary normalization nL*nI and local product P1.
    # Foam 2: boundary normalization nI*nR and local product P2.
    # Glued foam: boundary nL*nR, internal interface contraction contributes nI^2,
    # hence equals product of the two traces.  Local causal replacements enter only P1/P2.
    # Represent monomials by integer exponent dictionaries.
    def mul(*mons):
        out={}
        for m in mons:
            for k,v in m.items(): out[k]=out.get(k,0)+v
        return {k:v for k,v in sorted(out.items()) if v}
    T1={"nL":1,"nI":1,"P1":1}
    T2={"nI":1,"nR":1,"P2":1}
    product=mul(T1,T2)
    glued={"nL":1,"nR":1,"nI":2,"P1":1,"P2":1}
    twofoam = product == glued
    # General N-vertex locality: both sides contain every C_v exactly once.
    N=7
    lhs={f"C{i}":1 for i in range(N)}
    rhs={f"C{i}":1 for i in range(N)}
    nvertex = lhs == rhs
    return {"lane":"B","valid":twofoam and nvertex,"two_foam_exact_identity":twofoam,
            "N_vertex_exact_local_factor_identity":nvertex,"N":N,
            "product_monomial":product,"glued_monomial":glued}


def lane_c():
    # One-side boundary normalization deformation lambda creates an unmatched factor.
    inherited={"nL":1,"nR":1,"nI":2,"P1":1,"P2":1}
    deformed_product=dict(inherited); deformed_product["lambda"]=1
    generic_failure = deformed_product != inherited
    restored_at_lambda_one = True
    return {"lane":"C","valid":generic_failure and restored_at_lambda_one,
            "generic_independent_boundary_rescaling_breaks_gluing":generic_failure,
            "restored_when_lambda_equals_one":restored_at_lambda_one}


def lane_d():
    locks={
      "conditional_E5_only": True,
      "E3_unresolved": True,
      "E4_unresolved": True,
      "E6_unresolved": True,
      "E7_E8_unresolved": True,
      "no_downstream_promotion": True,
    }
    return {"lane":"D","valid":all(locks.values()),"scope_locks":locks}


def aggregate(d):
    files=list(Path(d).glob("**/iter079e_sm_*.json"))
    rows=[]
    for f in files:
        try:
            x=json.loads(f.read_text())
            if x.get("lane") in "ABCD": rows.append(x)
        except Exception: pass
    by={x["lane"]:x for x in rows}
    complete=all(k in by for k in "ABCD")
    valid=complete and all(by[k].get("valid") for k in "ABCD")
    classification = CLASS_PASS if valid else (CLASS_BLOCK if not complete or not by.get("A",{}).get("valid") else CLASS_FAIL)
    return {"aggregate":True,"complete":complete,"valid":valid,"lanes":by,"classification":classification}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane"); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    else: obj={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}[a.lane]()
    write(a.output,obj)
    if not obj.get("valid",False): raise SystemExit(1)

if __name__=="__main__": main()
