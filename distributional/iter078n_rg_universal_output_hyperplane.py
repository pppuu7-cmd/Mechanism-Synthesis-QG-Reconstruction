#!/usr/bin/env python3
"""Iter078N-RG: exact universal output-hyperplane audit for Iter078H map."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H_PATH = ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py"
spec = importlib.util.spec_from_file_location("iter078h", H_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(h)

LANE_NAMES = ("A", "B", "C", "L")


def tensor_point(name):
    if name == "A": return [i + 1 for i in range(32)]
    if name == "B": return [((-1) ** i.bit_count()) * (i + 1) for i in range(32)]
    if name == "C": return [(i + 1) ** 2 for i in range(32)]
    if name == "L": return h.compact_tensor()
    raise ValueError(name)


def transpose(M):
    return [list(col) for col in zip(*M)]


def primitive_left_null(C, mode):
    J = h.jacobian_at(C, mode)
    rank, pivots, left = h.rref_rank_null(transpose(J))
    if left is None:
        return rank, None, False
    verified = all(sum(left[i] * J[i][j] for i in range(32)) == 0 for j in range(32))
    return rank, left, verified


def proportional(a, b):
    if a is None or b is None:
        return False, None
    r = None
    for x, y in zip(a, b):
        if y == 0:
            if x != 0: return False, None
            continue
        q = Fraction(x, y)
        if r is None: r = q
        elif q != r: return False, None
    if r is None: return all(x == 0 for x in a), Fraction(0)
    return True, r


def common_left_null(mode):
    rows = {}
    for name in LANE_NAMES:
        rank, w, ok = primitive_left_null(tensor_point(name), mode)
        rows[name] = {"rank": rank, "left_null": w, "verified": ok}
    base = rows["A"]["left_null"]
    if any(rows[n]["rank"] != 31 or not rows[n]["verified"] for n in LANE_NAMES):
        relation = "INVALID"
        common = None
    elif all(rows[n]["left_null"] == base for n in LANE_NAMES):
        relation = "COMMON_IDENTICAL"
        common = base
    else:
        props = [proportional(rows[n]["left_null"], base)[0] for n in LANE_NAMES]
        if all(props):
            relation = "COMMON_PROPORTIONAL"
            common = base
        else:
            relation = "DIFFERENT"
            common = None
    return rows, relation, common


def polynomial_coefficients(w, mode):
    coeff = defaultdict(int)
    raw = 0
    for external in h.TUPLES:
        out_idx = h.INDEX[external]
        ww = w[out_idx]
        for bits in itertools.product((0, 1), repeat=10):
            raw += 1
            kd = h.internal_dict(bits)
            local_indices = tuple(sorted(h.INDEX[h.local_tuple(a, external, kd)] for a in range(5)))
            c = ww * h.FACE_FACTOR * h.edge_measure(kd, mode)
            coeff[local_indices] += c
    distinct_before = len(coeff)
    nonzero = {k: v for k, v in coeff.items() if v != 0}
    serial = [([int(x) for x in k], int(v)) for k, v in sorted(nonzero.items())]
    digest = hashlib.sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()
    first = serial[0] if serial else None
    return {
        "raw_configurations": raw,
        "distinct_monomials_before_zero_drop": distinct_before,
        "nonzero_monomial_coefficients": len(nonzero),
        "polynomial_identically_zero": len(nonzero) == 0,
        "sha256_nonzero_coefficient_dictionary": digest,
        "first_nonzero_monomial": first,
    }


def lane_a():
    rows, relation, common = common_left_null("eprl")
    valid = relation != "INVALID"
    return {
        "iteration": "Iter078N-RG", "lane": "A", "valid": valid,
        "measure": "eprl_edge_weights", "relation": relation,
        "common_left_null": common, "points": rows,
    }


def lane_b():
    rows, relation, common = common_left_null("eprl")
    if common is None:
        return {
            "iteration": "Iter078N-RG", "lane": "B", "valid": relation != "INVALID",
            "measure": "eprl_edge_weights", "relation": relation,
            "status": "NO_COMMON_W", "polynomial": None,
        }
    poly = polynomial_coefficients(common, "eprl")
    return {
        "iteration": "Iter078N-RG", "lane": "B", "valid": True,
        "measure": "eprl_edge_weights", "relation": relation,
        "status": "COMMON_W_TESTED", "common_left_null": common,
        "polynomial": poly,
    }


def signum(x): return 0 if x == 0 else (1 if x > 0 else -1)


def catalogue(L):
    out = {
        "constant": [1] * 32,
        "hamming_weight": [sum(t) for t in h.TUPLES],
        "complement_hamming_weight": [5 - sum(t) for t in h.TUPLES],
        "compact_tensor_L": list(L),
        "support_nonzero": [1 if x != 0 else 0 for x in L],
        "support_zero": [1 if x == 0 else 0 for x in L],
        "signed_compact_support": [signum(x) for x in L],
    }
    for smask in range(32):
        s = tuple((smask >> i) & 1 for i in range(5))
        out[f"walsh_{smask:02d}"] = [(-1 if sum(si*ki for si, ki in zip(s,t)) % 2 else 1) for t in h.TUPLES]
    return out


def lane_c():
    _, relation, common = common_left_null("eprl")
    if common is None:
        return {"iteration":"Iter078N-RG","lane":"C","valid":relation!="INVALID","relation":relation,"matches":[]}
    matches = []
    for name, vec in catalogue(h.compact_tensor()).items():
        ok, r = proportional(common, vec)
        if ok: matches.append({"name":name,"factor":str(r)})
    return {
        "iteration":"Iter078N-RG","lane":"C","valid":True,
        "relation":relation,"catalogue_size":len(catalogue(h.compact_tensor())),
        "matches":matches,"match_status":"MATCH" if matches else "NO_MATCH",
    }


def lane_d():
    rows, relation, common = common_left_null("unit")
    poly = polynomial_coefficients(common, "unit") if common is not None else None
    return {
        "iteration":"Iter078N-RG","lane":"D","valid":relation!="INVALID",
        "measure":"unit_edge_weight_control","relation":relation,
        "common_left_null":common,"points":rows,"polynomial":poly,
    }

LANES = {"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"): continue
            try: obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception: continue
            if obj.get("iteration") == "Iter078N-RG" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    complete = set(got) == set(LANES)
    valid = complete and all(bool(got[k].get("valid")) for k in LANES)
    if not valid:
        return {"iteration":"Iter078N-RG","execution_valid":False,"verdict":"INVALID_IMPLEMENTATION","lanes_found":sorted(got)}
    rel = got["A"]["relation"]
    poly = got["B"].get("polynomial")
    if rel in ("COMMON_IDENTICAL","COMMON_PROPORTIONAL") and poly and poly.get("polynomial_identically_zero"):
        verdict = "PASS"
        classification = "ITER078N_RG_FIXED_JHALF_REFINEMENT_CONTROL_IMAGE_LIES_IN_EXACT_UNIVERSAL_31D_OUTPUT_HYPERPLANE_STRUCTURAL_RANK_CEILING_SCOPED"
    elif rel in ("COMMON_IDENTICAL","COMMON_PROPORTIONAL") and poly:
        verdict = "FAIL"
        classification = "ITER078N_RG_COMMON_LEFT_NULL_AT_FROZEN_POINTS_NOT_UNIVERSAL_POLYNOMIAL_IDENTITY"
    else:
        verdict = "INCONCLUSIVE_STRUCTURAL_RANK"
        classification = "ITER078N_RG_NO_COMMON_LEFT_NULL_ACROSS_FROZEN_RANK31_POINTS"
    unit_poly = got["D"].get("polynomial")
    return {
        "iteration":"Iter078N-RG","execution_valid":True,"verdict":verdict,"classification":classification,
        "eprl_left_null_relation":rel,
        "eprl_common_left_null":got["A"].get("common_left_null"),
        "eprl_polynomial_identically_zero":poly.get("polynomial_identically_zero") if poly else None,
        "eprl_nonzero_monomials":poly.get("nonzero_monomial_coefficients") if poly else None,
        "eprl_polynomial_digest":poly.get("sha256_nonzero_coefficient_dictionary") if poly else None,
        "catalogue_matches":got["C"].get("matches"),
        "unit_left_null_relation":got["D"].get("relation"),
        "unit_common_left_null":got["D"].get("common_left_null"),
        "unit_polynomial_identically_zero":unit_poly.get("polynomial_identically_zero") if unit_poly else None,
        "unit_nonzero_monomials":unit_poly.get("nonzero_monomial_coefficients") if unit_poly else None,
        "interpretation_ceiling":"Fixed labelled all-j=1/2 pure order-zero tensor-network control only; no physical causal-Toller constraint or gauge identity implied.",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane",choices=LANES); ap.add_argument("--aggregate-dir"); ap.add_argument("--output",required=True); args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit("choose lane or aggregate")
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding="utf-8"); print(json.dumps(obj,indent=2,sort_keys=True))
    if args.lane and not obj.get("valid",False): raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid",False): raise SystemExit(1)

if __name__=="__main__": main()
