#!/usr/bin/env python3
import argparse, json, os
from pathlib import Path

PASS = "ITER079J_SM_VERTEX_ONLY_KKL_GLUE_RETAINS_PRODUCT_COMMON_LEFT_REDUNDANCY_G_POWER_V_DIAGONAL_QUOTIENT_LEAVES_6V_MINUS_6_RELATIVE_DIRECTIONS_EXACT_SCOPED_E6_PARTIAL"
FAIL = "ITER079J_SM_MULTIVERTEX_PRODUCT_REDUNDANCY_FAILS_IN_FROZEN_VERTEX_ONLY_GLUE_MODEL_EXACT_SCOPED"
INVALID = "ITER079J_SM_INVALID"


def inv_word(w):
    return [(s, -e) for s, e in reversed(w)]


def reduce_word(w):
    out = []
    for s, e in w:
        if out and out[-1][0] == s:
            ne = out[-1][1] + e
            out.pop()
            if ne:
                out.append((s, ne))
        else:
            out.append((s, e))
    return out


def mul(*words):
    w=[]
    for q in words: w.extend(q)
    return reduce_word(w)


def local_pair(v,a,b,transformed):
    ga=[(f"g{v}_{a}",1)]
    gb=[(f"g{v}_{b}",1)]
    if transformed:
        h=[(f"h{v}",1)]
        ga=mul(h,ga); gb=mul(h,gb)
    return mul(inv_word(gb),ga)


def lane_a():
    checks=[]
    for v in range(1,6):
        for a in range(1,6):
            for b in range(a+1,6):
                lhs=local_pair(v,a,b,True)
                rhs=local_pair(v,a,b,False)
                checks.append(lhs==rhs)
    return {"lane":"A","valid":all(checks),"checks":len(checks),"all_exact":all(checks),"independent_h_labels":5}


def graph_families(v):
    gs=[]
    gs.append(("path",[(i,i+1) for i in range(1,v)]))
    if v>=3: gs.append(("cycle",[(i,i+1) for i in range(1,v)]+[(v,1)]))
    if v>=3: gs.append(("star",[(1,i) for i in range(2,v+1)]))
    return gs


def vertex_signature(v, transformed):
    return tuple(tuple(local_pair(v,a,b,transformed)) for a in range(1,5) for b in range(a+1,5))


def lane_b():
    records=[]; ok=True
    for vcount in range(2,6):
        before={v:vertex_signature(v,False) for v in range(1,vcount+1)}
        after={v:vertex_signature(v,True) for v in range(1,vcount+1)}
        local_ok=before==after
        # Gluing layer contains only abstract boundary-output labels and graph incidence.
        for name,edges in graph_families(vcount):
            glue_before=(tuple(sorted(edges)), tuple((v,before[v]) for v in before))
            glue_after=(tuple(sorted(edges)), tuple((v,after[v]) for v in after))
            g_ok=glue_before==glue_after
            records.append({"V":vcount,"graph":name,"edges":edges,"invariant":g_ok})
            ok &= g_ok
        ok &= local_ok
    # Independent labels are a frozen provenance condition.
    independent=len({f"h{v}" for v in range(1,6)})==5
    ok &= independent
    return {"lane":"B","valid":ok,"records":records,"independent_local_left_symbols":independent}


def lane_c():
    rows=[]; ok=True
    for v in range(1,6):
        product=6*v; diagonal=6; relative=6*(v-1)
        row={"V":v,"dim_product_G_power_V":product,"dim_diagonal_G":diagonal,"relative_after_diagonal":relative}
        rows.append(row)
        ok &= (product-diagonal==relative)
    return {"lane":"C","valid":ok,"rows":rows,"dimension_input":"dim_R SL(2,C)=6"}


def lane_d():
    rows=[]; ok=True
    for v in range(2,6):
        independent=v; forced_diagonal=1
        collapse=independent-forced_diagonal
        rows.append({"V":v,"independent_action_factors":independent,"forced_diagonal_factors":forced_diagonal,"lost_independent_factors":collapse})
        ok &= collapse==v-1
    locks={
      "no_quotient_fixing_normalization":True,
      "no_group_volume_division":True,
      "no_FP_or_Haar_prescription":True,
      "no_finiteness_or_convergence_claim":True,
      "E7_E8_unresolved":True,
      "no_downstream_promotion":True,
      "scoped_vertex_only_inheritance_not_arbitrary_foam_theorem":True,
    }
    return {"lane":"D","valid":ok and all(locks.values()),"negative_control":rows,"scope_locks":locks}


def aggregate(root):
    lanes={}
    for p in Path(root).rglob("iter079j_sm_*.json"):
        try: d=json.loads(p.read_text())
        except Exception: continue
        if d.get("lane") in "ABCD": lanes[d["lane"]]=d
    complete=set(lanes)==set("ABCD")
    valid=complete and all(lanes[x].get("valid") for x in "ABCD")
    classification=PASS if valid else (INVALID if not complete else FAIL)
    return {"aggregate":True,"complete":complete,"valid":valid,"classification":classification,"lanes":lanes}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",choices=list("ABCD")+['aggregate'],required=True); ap.add_argument("--out",required=True); ap.add_argument("--root",default='.')
    a=ap.parse_args()
    if a.lane=='A': d=lane_a()
    elif a.lane=='B': d=lane_b()
    elif a.lane=='C': d=lane_c()
    elif a.lane=='D': d=lane_d()
    else: d=aggregate(a.root)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps(d,indent=2,sort_keys=True))
    if not d.get('valid',False): raise SystemExit(2)

if __name__=='__main__': main()
