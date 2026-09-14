#!/usr/bin/env python3
import argparse, json
from fractions import Fraction
from pathlib import Path

ITER = "Iter079C-SM"
BLOCKED_CLASS = "ITER079C_SM_MINIMAL_TWO_VERTEX_CAUSAL_FUNCTIONAL_NOT_UNIQUELY_FIXED_BY_LOCAL_VERTEX_DATA_AND_COMBINATORIAL_SKELETON_E3_E4_BRIDGE_REQUIRED_EXACT_SCOPED"
PASS_CLASS = "ITER079C_SM_CAUSAL_COMPOSITION_UNIQUENESS_ESTABLISHED_SCOPED"
INVALID_CLASS = "ITER079C_SM_INVALID_SOURCE_OR_IMPLEMENTATION"

# Frozen exact witness in H = Q^2.
VL = (Fraction(1), Fraction(2))
VR = (Fraction(3), Fraction(-1))
B0 = ((Fraction(2), Fraction(0)), (Fraction(0), Fraction(1)))

def bilinear(B, x, y):
    return sum(x[i] * B[i][j] * y[j] for i in range(2) for j in range(2))

def det2(B):
    return B[0][0]*B[1][1] - B[0][1]*B[1][0]

def dump(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")

def lane_A():
    z0 = bilinear(B0, VL, VR)
    valid = det2(B0) != 0 and z0 != 0
    return {
        "iteration": ITER, "lane": "A", "valid": valid,
        "scientific_outcome": "PASS" if valid else "INVALID",
        "candidate_parent_bridge": {"det_B0": str(det2(B0)), "Z0": str(z0), "nonzero": z0 != 0},
        "scope": "candidate composition exists; no causal inheritance authority promoted"
    }

def lane_B():
    lam = Fraction(2)
    B2 = tuple(tuple(lam*a for a in row) for row in B0)
    z0 = bilinear(B0, VL, VR)
    z2 = bilinear(B2, VL, VR)
    valid = det2(B0) != 0 and det2(B2) != 0 and z2 == 2*z0 and z2 != z0
    return {
        "iteration": ITER, "lane": "B", "valid": valid,
        "scientific_outcome": "BLOCKED" if valid else "INVALID",
        "lambda": 2, "det_B0": str(det2(B0)), "det_B2": str(det2(B2)),
        "Z0": str(z0), "Zlambda": str(z2),
        "same_local_vertices": True, "bilinear_type_preserved": True,
        "normalization_nonuniqueness_exact": valid
    }

def lane_C():
    z0 = bilinear(B0, VL, VR)
    z1 = Fraction(1)*z0
    z3 = Fraction(3)*z0
    valid = z0 != 0 and z3 == 3*z1 and z3 != z1
    return {
        "iteration": ITER, "lane": "C", "valid": valid,
        "scientific_outcome": "BLOCKED" if valid else "INVALID",
        "weights": [1,3], "Zw1": str(z1), "Zw3": str(z3),
        "same_local_vertices_and_pairing": True,
        "internal_weight_nonuniqueness_exact": valid
    }

def lane_D():
    p = Path("results/ITER079B_SM_EPRL_KKL_CAUSAL_COMPOSITION_INHERITANCE_RESULT.md")
    if not p.exists():
        return {"iteration": ITER, "lane":"D", "valid":False, "scientific_outcome":"INVALID", "reason":"Iter079B durable result missing"}
    text = p.read_text(encoding="utf-8")
    locks = {
        "iter079b_classification_present": "ITER079B_SM_PARENT_COMPOSITION_SKELETON_EXISTS_BUT_CAUSAL_INHERITANCE_REQUIRES_NEW_BRIDGE_E3_E8_BLOCKED_EXACT_SOURCE_AUDIT" in text,
        "E3_E6_missing_recorded": all(k in text for k in ["E3", "E4", "E5", "E6"]),
        "parent_not_silent_causal_authority": "may not be silently" in Path("prereg/ITER079C_SM_MINIMAL_TWO_VERTEX_COMPOSITION_UNIQUENESS.md").read_text(encoding="utf-8")
    }
    valid = all(locks.values())
    return {"iteration":ITER, "lane":"D", "valid":valid, "scientific_outcome":"PASS" if valid else "INVALID", "locks":locks}

def aggregate(root):
    data = {}
    for lane in "ABCD":
        matches = list(Path(root).glob(f"**/iter079c_sm_{lane}.json"))
        if len(matches) != 1:
            dump(args.output, {"iteration":ITER,"execution_valid":False,"classification":INVALID_CLASS,"reason":f"lane {lane} artifact count={len(matches)}"})
            return
        data[lane] = json.loads(matches[0].read_text(encoding="utf-8"))
    execution_valid = all(data[k].get("valid") for k in data)
    blocked_pattern = data["A"]["scientific_outcome"] == "PASS" and data["B"]["scientific_outcome"] == "BLOCKED" and data["C"]["scientific_outcome"] == "BLOCKED" and data["D"]["scientific_outcome"] == "PASS"
    if execution_valid and blocked_pattern:
        classification = BLOCKED_CLASS
        verdict = "BLOCKED"
    elif execution_valid and data["B"]["scientific_outcome"] == "PASS" and data["C"]["scientific_outcome"] == "PASS":
        classification = PASS_CLASS
        verdict = "PASS"
    else:
        classification = INVALID_CLASS
        verdict = "INVALID"
    out = {
        "iteration":ITER, "execution_valid":execution_valid, "verdict":verdict, "classification":classification,
        "lane_scientific_outcomes":{k:data[k]["scientific_outcome"] for k in data},
        "new_scientific_fact":"Local causal one-vertex data plus combinatorial gluing do not uniquely fix minimal two-vertex normalization/pairing or internal weight: exact inequivalent compositions exist unless an E3/E4 inheritance rule is added." if verdict=="BLOCKED" else "",
        "next_admissible_gate":"If BLOCKED, isolate E5/E6 orientation-duality and gauge-quotient inheritance; keep E7/E8 separate until an E3-E6 composed object exists.",
        "claim_lock":"No full causal multivertex theorem, no unique K5 extension, no regulator independence, no RG/G3/F9/G8/K5 promotion, no new physics."
    }
    dump(args.output, out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=list("ABCD"))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        aggregate(args.aggregate_dir)
    else:
        fn = {"A":lane_A,"B":lane_B,"C":lane_C,"D":lane_D}[args.lane]
        dump(args.output, fn())
