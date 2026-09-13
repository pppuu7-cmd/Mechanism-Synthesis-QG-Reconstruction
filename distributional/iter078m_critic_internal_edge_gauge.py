#!/usr/bin/env python3
"""Adversarial exact control for the structural internal-edge gauge null mode of Iter078M.

Prospectively frozen in prereg/ITER078M_CRITIC_INTERNAL_EDGE_GAUGE_SYMMETRY.md.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H_PATH = ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py"
spec = importlib.util.spec_from_file_location("iter078h", H_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(h)


def tensor(lane: str):
    if lane == "A":
        return [i + 1 for i in range(32)], "eprl"
    if lane == "B":
        return [((-1) ** (i.bit_count())) * (i + 1) for i in range(32)], "eprl"
    if lane == "C":
        return [(i + 1) ** 2 for i in range(32)], "eprl"
    if lane == "L":
        return h.compact_tensor(), "eprl"
    if lane == "W":
        return [(i + 1) ** 3 + 2 * (i + 1) + 7 for i in range(32)], "eprl"
    if lane == "U":
        return [(i + 1) ** 3 + 2 * (i + 1) + 7 for i in range(32)], "unit"
    raise ValueError(lane)


def generator(mode: str):
    # X^T D + D X = 0 with D=diag(1,3) or I.
    if mode == "eprl":
        return ((0, -3), (1, 0)), ((1, 0), (0, 3))
    return ((0, -1), (1, 0)), ((1, 0), (0, 1))


def gauge_tangent(C, mode: str):
    X, _D = generator(mode)
    out = [0] * 32
    for t in h.TUPLES:
        val = 0
        # t[0] is the external leg. Transform only the four internal legs.
        for r in range(1, 5):
            i = t[r]
            for s in (0, 1):
                tt = list(t)
                tt[r] = s
                val += X[i][s] * C[h.INDEX[tuple(tt)]]
        out[h.INDEX[t]] = val
    return out


def metric_generator_residual(mode: str):
    X, D = generator(mode)
    # Compute X^T D + D X exactly.
    XT_D = [[sum(X[k][i] * D[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    D_X = [[sum(D[i][k] * X[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return [[XT_D[i][j] + D_X[i][j] for j in range(2)] for i in range(2)]


def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def lane_result(lane: str):
    C, mode = tensor(lane)
    J = h.jacobian_at(C, mode)
    rank, pivots, null = h.rref_rank_null(J)
    v = gauge_tangent(C, mode)
    Jv = matvec(J, v)
    residual = metric_generator_residual(mode)
    valid = (
        any(x != 0 for x in v)
        and all(x == 0 for x in Jv)
        and all(x == 0 for row in residual for x in row)
    )
    proportional_to_reported_null = None
    if null is not None:
        # Exact projective comparison without division.
        nz = next((i for i, x in enumerate(null) if x != 0), None)
        if nz is not None and v[nz] != 0:
            proportional_to_reported_null = all(v[i] * null[nz] == null[i] * v[nz] for i in range(32))
        else:
            proportional_to_reported_null = False
    return {
        "iteration": "Iter078M critic internal-edge gauge",
        "lane": lane,
        "mode": mode,
        "valid": bool(valid),
        "jacobian_rank_Q": rank,
        "jacobian_nullity": 32 - rank,
        "gauge_tangent_nonzero": any(x != 0 for x in v),
        "gauge_tangent": v,
        "Jv_zero_exact": all(x == 0 for x in Jv),
        "Jv": Jv,
        "metric_generator_residual": residual,
        "rref_null_witness_verified": h.verify_null(J, null) if null is not None else None,
        "gauge_tangent_proportional_to_first_rref_null": proportional_to_reported_null,
        "pivot_columns": pivots,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("A", "B", "C", "L", "W", "U"), required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    obj = lane_result(args.lane)
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj["valid"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
