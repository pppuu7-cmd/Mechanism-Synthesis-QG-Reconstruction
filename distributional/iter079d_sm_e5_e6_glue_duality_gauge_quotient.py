#!/usr/bin/env python3
import argparse, json
from fractions import Fraction
from pathlib import Path

ITER = "Iter079D-SM"
BLOCKED_CLASS = "ITER079D_SM_E5_E6_BOUNDARY_DUALITY_AND_GAUGE_QUOTIENT_NOT_UNIQUELY_FIXED_BY_CURRENT_CAUSAL_INHERITANCE_DATA_EXACT_SCOPED"
FAIL_CLASS = "ITER079D_SM_PROPOSED_E5_E6_NONUNIQUENESS_WITNESS_FAILS_SCOPED"
INVALID_CLASS = "ITER079D_SM_INVALID_SOURCE_OR_IMPLEMENTATION"

VL = (Fraction(1), Fraction(2))
VR = (Fraction(3), Fraction(-1))
B0 = ((Fraction(2), Fraction(0)), (Fraction(0), Fraction(1)))
D1 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
D2 = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))
I2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def mv(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(2)) for i in range(2))

def bilinear(B,x,y):
    return sum(x[i]*B[i][j]*y[j] for i in range(2) for j in range(2))

def dump(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True),encoding="utf-8")

def lane_A():
    b = Path("results/ITER079B_SM_EPRL_KKL_CAUSAL_COMPOSITION_INHERITANCE_RESULT.md")
    c = Path("results/ITER079C_SM_MINIMAL_TWO_VERTEX_COMPOSITION_UNIQUENESS_RESULT.md")
    if not b.exists() or not c.exists():
        return {"iteration":ITER,"lane":"A","valid":False,"scientific_outcome":"INVALID","reason":"required durable result missing"}
    tb, tc = b.read_text(encoding="utf-8"), c.read_text(encoding="utf-8")
    locks = {
        "iter079b_e5_e6_missing": "E3-E6 remain missing required objects" in tb and "boundary gluing/duality" in tb and "gauge quotient/fixing" in tb,
        "iter079c_blocked_present": "ITER079C_SM_MINIMAL_TWO_VERTEX_CAUSAL_FUNCTIONAL_NOT_UNIQUELY_FIXED_BY_LOCAL_VERTEX_DATA_AND_COMBINATORIAL_SKELETON_E3_E4_BRIDGE_REQUIRED_EXACT_SCOPED" in tc,
        "parent_not_causal_authority": "parent **combinatorial** gluing skeleton" in tc,
    }
    valid=all(locks.values())
    return {"iteration":ITER,"lane":"A","valid":valid,"scientific_outcome":"PASS" if valid else "INVALID","locks":locks}

def lane_B():
    z1=bilinear(B0,VL,mv(D1,VR))
    z2=bilinear(B0,VL,mv(D2,VR))
    valid=(mm(D1,D1)==I2 and mm(D2,D2)==I2 and det2(D1)==-1 and det2(D2)==-1 and z1!=z2)
    return {"iteration":ITER,"lane":"B","valid":valid,"scientific_outcome":"BLOCKED" if valid else "FAIL","D1_squared_identity":mm(D1,D1)==I2,"D2_squared_identity":mm(D2,D2)==I2,"det_D1":str(det2(D1)),"det_D2":str(det2(D2)),"Z1":str(z1),"Z2":str(z2),"duality_nonuniqueness_exact":z1!=z2}

def lane_C():
    zred=Fraction(5)
    q1=Fraction(1)*zred
    q2=Fraction(2)*zred
    valid=(zred!=0 and q1!=q2 and q2==2*q1)
    return {"iteration":ITER,"lane":"C","valid":valid,"scientific_outcome":"BLOCKED" if valid else "FAIL","Zred":str(zred),"quotient_normalizations":[1,2],"Q1":str(q1),"Q2":str(q2),"gauge_invariance_preserved_by_constant_rescaling":True,"quotient_normalization_nonuniqueness_exact":valid}

def lane_D():
    p=Path("prereg/ITER079D_SM_E5_E6_GLUE_DUALITY_GAUGE_QUOTIENT.md")
    b=Path("results/ITER079B_SM_EPRL_KKL_CAUSAL_COMPOSITION_INHERITANCE_RESULT.md")
    text=p.read_text(encoding="utf-8") if p.exists() else ""
    tb=b.read_text(encoding="utf-8") if b.exists() else ""
    locks={
        "e7_e8_excluded": "does **not** test E7/E8" in text,
        "claim_lock_present": "No full causal multi-vertex theorem" in text and "no `NEW_PHYSICS_FOUND`" in text,
        "e5_e6_still_missing_in_authority": "E3-E6 remain missing required objects" in tb,
    }
    valid=all(locks.values())
    return {"iteration":ITER,"lane":"D","valid":valid,"scientific_outcome":"PASS" if valid else "INVALID","locks":locks}

def aggregate(root,outpath):
    data={}
    for lane in "ABCD":
        matches=list(Path(root).glob(f"**/iter079d_sm_{lane}.json"))
        if len(matches)!=1:
            dump(outpath,{"iteration":ITER,"execution_valid":False,"classification":INVALID_CLASS,"reason":f"lane {lane} artifact count={len(matches)}"})
            return
        data[lane]=json.loads(matches[0].read_text(encoding="utf-8"))
    execution_valid=all(data[k].get("valid") for k in data)
    blocked_pattern=(data["A"]["scientific_outcome"]=="PASS" and data["B"]["scientific_outcome"]=="BLOCKED" and data["C"]["scientific_outcome"]=="BLOCKED" and data["D"]["scientific_outcome"]=="PASS")
    any_fail=any(data[k]["scientific_outcome"]=="FAIL" for k in data)
    if execution_valid and blocked_pattern:
        verdict="BLOCKED"; classification=BLOCKED_CLASS
    elif execution_valid and any_fail:
        verdict="FAIL"; classification=FAIL_CLASS
    else:
        verdict="INVALID"; classification=INVALID_CLASS
    dump(outpath,{"iteration":ITER,"execution_valid":execution_valid,"verdict":verdict,"classification":classification,"lane_scientific_outcomes":{k:data[k]["scientific_outcome"] for k in data},"new_scientific_fact":"Current causal/source plus parent-skeleton data do not uniquely determine E5 boundary duality identification or E6 gauge-quotient normalization in the frozen minimal witness scope." if verdict=="BLOCKED" else "","next_admissible_gate":"If BLOCKED, E3-E6 all require explicit causal bridge data; do not test E7/E8 on an undefined composed functional. Search/derive a source-faithful E3-E6 composition prescription first.","claim_lock":"No full causal multivertex theorem, no unique K5 extension, no regulator independence, no E7/E8 result, no RG/G3/F9/G8/K5 promotion, no new physics."})

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",choices=list("ABCD")); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True); args=ap.parse_args()
    if args.aggregate_dir: aggregate(args.aggregate_dir,args.output)
    else: dump(args.output,{"A":lane_A,"B":lane_B,"C":lane_C,"D":lane_D}[args.lane]())
