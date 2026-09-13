#!/usr/bin/env python3
"""Iter078M-RG: exact generic-rank witnesses for the Iter078H 32D control map."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H_PATH = ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py"
spec = importlib.util.spec_from_file_location("iter078h", H_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(h)


def tensor_for_lane(lane):
    if lane == "A":
        return [i + 1 for i in range(32)]
    if lane == "B":
        return [((-1) ** (i.bit_count())) * (i + 1) for i in range(32)]
    if lane == "C":
        return [(i + 1) ** 2 for i in range(32)]
    if lane == "L":
        return h.compact_tensor()
    raise ValueError(lane)


def bareiss_det(A):
    m = [list(map(int, row)) for row in A]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            p = next((r for r in range(k + 1, n) if m[r][k] != 0), None)
            if p is None:
                return 0
            m[k], m[p] = m[p], m[k]
            sign *= -1
        pivot = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = m[i][j] * pivot - m[i][k] * m[k][j]
                if k > 0:
                    if num % prev != 0:
                        raise ArithmeticError("Bareiss exact division failed")
                    num //= prev
                m[i][j] = num
        for i in range(k + 1, n):
            m[i][k] = 0
        prev = pivot
    return sign * m[n - 1][n - 1]


def lane_result(lane):
    C = tensor_for_lane(lane)
    J = h.jacobian_at(C, "eprl")
    rank, pivots, null = h.rref_rank_null(J)
    null_verified = h.verify_null(J, null) if null is not None else None
    det = bareiss_det(J) if rank == 32 else None
    valid = (lane != "L" and rank in range(33)) or (lane == "L" and rank == 31)
    if rank == 32:
        valid = valid and det is not None and det != 0
    if rank < 32:
        valid = valid and null is not None and bool(null_verified)
    matrix_serial = json.dumps(J, separators=(",", ":"))
    return {
        "iteration": "Iter078M-RG",
        "lane": lane,
        "valid": bool(valid),
        "tensor": C,
        "jacobian_rank_Q": rank,
        "jacobian_nullity": 32 - rank,
        "pivot_columns": pivots,
        "right_null_witness": null,
        "right_null_witness_verified": null_verified,
        "determinant": str(det) if det is not None else None,
        "determinant_nonzero": det != 0 if det is not None else None,
        "determinant_decimal_digits": len(str(abs(det))) if det is not None else None,
        "jacobian_sha256": hashlib.sha256(matrix_serial.encode()).hexdigest(),
    }


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
            if obj.get("iteration") == "Iter078M-RG" and obj.get("lane") in {"A", "B", "C", "L"}:
                got[obj["lane"]] = obj
    complete = set(got) == {"A", "B", "C", "L"}
    valid = complete and all(bool(got[k].get("valid")) for k in got) and got["L"].get("jacobian_rank_Q") == 31
    if not valid:
        return {"iteration": "Iter078M-RG", "execution_valid": False, "verdict": "INVALID_IMPLEMENTATION", "lanes_found": sorted(got)}
    full = [k for k in ("A", "B", "C") if got[k]["jacobian_rank_Q"] == 32 and got[k].get("determinant_nonzero")]
    if full:
        verdict = "PASS"
        classification = "ITER078M_RG_FIXED_JHALF_FULL32_REFINEMENT_CONTROL_HAS_EXACT_FULL_RANK_JACOBIAN_WITNESS_GENERIC_LOCAL_RANK32_SCOPED"
    else:
        verdict = "INCONCLUSIVE_GENERIC_RANK"
        classification = "ITER078M_RG_NO_FULL_RANK_WITNESS_IN_FROZEN_GENERIC_CONTROLS"
    return {
        "iteration": "Iter078M-RG",
        "execution_valid": True,
        "verdict": verdict,
        "classification": classification,
        "full_rank_witness_lanes": full,
        "ranks": {k: got[k]["jacobian_rank_Q"] for k in ("A", "B", "C", "L")},
        "nullities": {k: got[k]["jacobian_nullity"] for k in ("A", "B", "C", "L")},
        "determinant_nonzero": {k: got[k].get("determinant_nonzero") for k in ("A", "B", "C")},
        "determinant_digits": {k: got[k].get("determinant_decimal_digits") for k in ("A", "B", "C")},
        "jacobian_sha256": {k: got[k].get("jacobian_sha256") for k in ("A", "B", "C", "L")},
        "interpretation_ceiling": "Fixed all-j=1/2 pure order-zero refinement control only; generic full local rank here does not define the physical causal-Toller RG selector.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("A", "B", "C", "L"))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose lane or aggregate")
    obj = lane_result(args.lane) if args.lane else aggregate(args.aggregate_dir)
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
