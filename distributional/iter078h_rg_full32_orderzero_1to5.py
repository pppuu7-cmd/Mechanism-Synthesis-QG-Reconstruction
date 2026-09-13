#!/usr/bin/env python3
"""Iter078H-RG: exact full-32 j=1/2 order-zero 1->5 tensor-map control."""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
N_PATH = ROOT / "distributional" / "iter077n_sm_supported_ambiguity_gluing.py"
spec = importlib.util.spec_from_file_location("iter077n_base", N_PATH)
nbase = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(nbase)

TUPLES = list(itertools.product((0, 1), repeat=5))
INDEX = {t: i for i, t in enumerate(TUPLES)}
EDGES = list(itertools.combinations(range(5), 2))
NEIGHBORS = {a: [b for b in range(5) if b != a] for a in range(5)}
FACE_FACTOR = 2 ** 10


def compact_tensor():
    vals = []
    for ks in TUPLES:
        z = nbase.compact_eval(ks)
        if z[1] != 0:
            raise RuntimeError("compact tensor unexpectedly complex")
        vals.append(int(z[0]))
    return vals


def internal_dict(bits):
    return {e: bits[i] for i, e in enumerate(EDGES)}


def kval(kdict, a, b):
    return kdict[(a, b) if a < b else (b, a)]


def local_tuple(a, external, kdict):
    return (external[a],) + tuple(kval(kdict, a, b) for b in NEIGHBORS[a])


def edge_measure(kdict, mode):
    if mode == "unit":
        return 1
    w = 1
    for e in EDGES:
        k = kdict[e]
        w *= 2 * k + 1
    return w


def rg_map(C, mode="eprl"):
    out = [0] * 32
    for external in TUPLES:
        total = 0
        for bits in itertools.product((0, 1), repeat=10):
            kd = internal_dict(bits)
            term = edge_measure(kd, mode)
            for a in range(5):
                term *= C[INDEX[local_tuple(a, external, kd)]]
                if term == 0:
                    break
            total += term
        out[INDEX[external]] = FACE_FACTOR * total
    return out


def jacobian_at(C, mode="eprl"):
    J = [[0 for _ in range(32)] for _ in range(32)]
    for external in TUPLES:
        row = INDEX[external]
        for bits in itertools.product((0, 1), repeat=10):
            kd = internal_dict(bits)
            basew = FACE_FACTOR * edge_measure(kd, mode)
            idx = [INDEX[local_tuple(a, external, kd)] for a in range(5)]
            for v in range(5):
                term = basew
                for u in range(5):
                    if u != v:
                        term *= C[idx[u]]
                        if term == 0:
                            break
                if term:
                    J[row][idx[v]] += term
    return J


def proportional(a, b):
    ratio = None
    witness = None
    for i, (x, y) in enumerate(zip(a, b)):
        if y == 0:
            if x != 0:
                return False, None, {"index": i, "image": x, "base": y}
            continue
        r = Fraction(x, y)
        if ratio is None:
            ratio = r
        elif r != ratio:
            return False, None, {"index": i, "image": x, "base": y, "expected_ratio": str(ratio), "actual_ratio": str(r)}
    if ratio is None:
        return all(x == 0 for x in a), Fraction(0), None
    return True, ratio, None


def rref_rank_null(A):
    m = [[Fraction(x) for x in row] for row in A]
    rows, cols = len(m), len(m[0]) if m else 0
    pivots = []
    r = 0
    for c in range(cols):
        p = next((rr for rr in range(r, rows) if m[rr][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        q = m[r][c]
        m[r] = [x / q for x in m[r]]
        for rr in range(rows):
            if rr == r or m[rr][c] == 0:
                continue
            q = m[rr][c]
            m[rr] = [x - q * y for x, y in zip(m[rr], m[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    rank = len(pivots)
    free = [c for c in range(cols) if c not in pivots]
    witness = None
    if free:
        f = free[0]
        x = [Fraction(0) for _ in range(cols)]
        x[f] = Fraction(1)
        for rr, pc in enumerate(pivots):
            x[pc] = -m[rr][f]
        # clear denominators
        import math
        den = 1
        for z in x:
            den = math.lcm(den, z.denominator)
        ints = [int(z * den) for z in x]
        g = 0
        for z in ints:
            g = math.gcd(g, abs(z))
        if g > 1:
            ints = [z // g for z in ints]
        first = next((z for z in ints if z != 0), 1)
        if first < 0:
            ints = [-z for z in ints]
        witness = ints
    return rank, pivots, witness


def verify_null(A, x):
    if x is None:
        return None
    return all(sum(a * b for a, b in zip(row, x)) == 0 for row in A)


def lane_a():
    old = nbase.lane_a()
    L = compact_tensor()
    valid = (
        len(L) == 32
        and sum(v != 0 for v in L) == 16
        and old.get("sha256_exact_rows") == "8923ae7f43fa83b9da1e9095d3ef195e6d208031ff6824a6a1a15a2d9912b936"
        and len(EDGES) == 10
        and FACE_FACTOR == 1024
    )
    return {
        "iteration": "Iter078H-RG",
        "lane": "A",
        "valid": valid,
        "local_components": len(L),
        "output_components": 32,
        "internal_binary_assignments_per_output": 2 ** 10,
        "internal_edge_weights": {"0": 1, "1": 3},
        "common_internal_face_factor": FACE_FACTOR,
        "compact_nonzero": sum(v != 0 for v in L),
        "iter077n_checksum": old.get("sha256_exact_rows"),
        "compact_tensor": L,
    }


def image_diag(mode):
    L = compact_tensor()
    image = rg_map(L, mode)
    prop, K, witness = proportional(image, L)
    return L, image, prop, K, witness


def lane_b():
    L, image, prop, K, witness = image_diag("eprl")
    return {
        "iteration": "Iter078H-RG",
        "lane": "B",
        "valid": True,
        "measure": "eprl_edge_weights",
        "bf_tensor_is_eigenray": prop,
        "K": str(K) if K is not None else None,
        "nonproportionality_witness": witness,
        "image": image,
        "base": L,
    }


def lane_c():
    L = compact_tensor()
    J = jacobian_at(L, "eprl")
    rank, pivots, null = rref_rank_null(J)
    return {
        "iteration": "Iter078H-RG",
        "lane": "C",
        "valid": True,
        "measure": "eprl_edge_weights",
        "jacobian_rank_Q": rank,
        "jacobian_nullity": 32 - rank,
        "pivot_columns": pivots,
        "right_null_witness": null,
        "right_null_witness_verified": verify_null(J, null),
    }


def lane_d():
    L, image, prop, K, witness = image_diag("unit")
    J = jacobian_at(L, "unit")
    rank, pivots, null = rref_rank_null(J)
    return {
        "iteration": "Iter078H-RG",
        "lane": "D",
        "valid": True,
        "measure": "unit_edge_weight_control",
        "bf_tensor_is_eigenray": prop,
        "K": str(K) if K is not None else None,
        "nonproportionality_witness": witness,
        "jacobian_rank_Q": rank,
        "jacobian_nullity": 32 - rank,
        "right_null_witness": null,
        "right_null_witness_verified": verify_null(J, null),
        "image": image,
    }

LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root):
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter078H-RG" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    complete = set(got) == set(LANES)
    valid = complete and all(bool(got[k].get("valid")) for k in LANES)
    if not valid:
        return {"iteration": "Iter078H-RG", "execution_valid": False, "verdict": "INVALID_IMPLEMENTATION", "lanes_found": sorted(got)}
    eigen = bool(got["B"]["bf_tensor_is_eigenray"])
    classification = (
        "ITER078H_RG_FULL32_FIXED_JHALF_ORDERZERO_MAP_BF_TENSOR_EIGENRAY_EXACT_CONTROL_SCOPED"
        if eigen else
        "ITER078H_RG_FULL32_FIXED_JHALF_ORDERZERO_MAP_BF_TENSOR_NOT_CLOSED_EXACT_CONTROL_SCOPED"
    )
    measure_sensitive = (
        got["B"]["bf_tensor_is_eigenray"] != got["D"]["bf_tensor_is_eigenray"]
        or got["C"]["jacobian_rank_Q"] != got["D"]["jacobian_rank_Q"]
        or got["B"].get("K") != got["D"].get("K")
    )
    return {
        "iteration": "Iter078H-RG",
        "execution_valid": True,
        "verdict": "CONTROL_RESULT",
        "classification": classification,
        "eprl_bf_tensor_eigenray": got["B"]["bf_tensor_is_eigenray"],
        "eprl_K": got["B"].get("K"),
        "eprl_nonproportionality_witness": got["B"].get("nonproportionality_witness"),
        "eprl_jacobian_rank_Q": got["C"]["jacobian_rank_Q"],
        "eprl_jacobian_nullity": got["C"]["jacobian_nullity"],
        "eprl_null_witness_verified": got["C"].get("right_null_witness_verified"),
        "unit_bf_tensor_eigenray": got["D"]["bf_tensor_is_eigenray"],
        "unit_K": got["D"].get("K"),
        "unit_jacobian_rank_Q": got["D"]["jacobian_rank_Q"],
        "unit_jacobian_nullity": got["D"]["jacobian_nullity"],
        "measure_sensitive": measure_sensitive,
        "interpretation_ceiling": "Fixed all-j=1/2 pure order-zero ambiguity tensor-network control only; no source Toller reference extension, full spin sums, causal-orientation sum, RG fixed point or continuum claim.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one lane or aggregate")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
