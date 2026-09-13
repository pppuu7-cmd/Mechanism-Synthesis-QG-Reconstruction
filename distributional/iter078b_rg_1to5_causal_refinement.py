#!/usr/bin/env python3
"""Iter078B-RG: exact 1->5 causal refinement orientation enumeration."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
from collections import Counter
from pathlib import Path

VERTICES = range(5)
EDGES = list(itertools.combinations(VERTICES, 2))
ALL_EDGE_MASK = (1 << len(EDGES)) - 1


def sigma_from_mask(mask: int):
    # bit=1 -> outgoing +1; bit=0 -> ingoing -1
    return tuple(1 if (mask >> a) & 1 else -1 for a in VERTICES)


def directed_edges(edge_mask: int):
    out = []
    for k, (a, b) in enumerate(EDGES):
        # bit=0: a -> b; bit=1: b -> a
        out.append((b, a) if ((edge_mask >> k) & 1) else (a, b))
    return out


def total_order_if_acyclic(edge_mask: int):
    """K5 tournament is acyclic iff outdegrees are exactly 4,3,2,1,0."""
    directed = directed_edges(edge_mask)
    outdeg = [0] * 5
    for u, v in directed:
        outdeg[u] += 1
    if sorted(outdeg) != [0, 1, 2, 3, 4]:
        return None
    order = tuple(sorted(VERTICES, key=lambda a: -outdeg[a]))
    pos = {a: i for i, a in enumerate(order)}
    if not all(pos[u] < pos[v] for u, v in directed):
        return None
    return order


def boundary_compatible(order, sigmas):
    pos = {a: i for i, a in enumerate(order)}
    incoming = [a for a, s in enumerate(sigmas) if s == -1]
    outgoing = [a for a, s in enumerate(sigmas) if s == +1]
    return all(pos[i] < pos[o] for i in incoming for o in outgoing)


def local_sign_tuple(a: int, edge_mask: int, external_sigma: int):
    signs = [external_sigma]
    directed = directed_edges(edge_mask)
    edge_dir = {frozenset((u, v)): (u, v) for u, v in directed}
    for b in VERTICES:
        if b == a:
            continue
        u, v = edge_dir[frozenset((a, b))]
        signs.append(+1 if u == a else -1)
    return tuple(signs)


def causal_class(signs):
    n_in = sum(1 for s in signs if s == -1)
    m = min(n_in, 5 - n_in)
    return {0: "0<->5", 1: "1<->4", 2: "2<->3"}[m]


def audit_pattern(boundary_mask: int):
    sigmas = sigma_from_mask(boundary_mask)
    p = sum(1 for s in sigmas if s == -1)
    q = 5 - p
    compatible = []
    local_classes = Counter()
    local_tuples = Counter()
    for edge_mask in range(1 << len(EDGES)):
        order = total_order_if_acyclic(edge_mask)
        if order is None or not boundary_compatible(order, sigmas):
            continue
        compatible.append(edge_mask)
        for a in VERTICES:
            tup = local_sign_tuple(a, edge_mask, sigmas[a])
            local_tuples[tup] += 1
            local_classes[causal_class(tup)] += 1
    expected = math.factorial(p) * math.factorial(q)
    return {
        "boundary_mask": boundary_mask,
        "sigma": list(sigmas),
        "p_in": p,
        "q_out": q,
        "compatible_count": len(compatible),
        "expected_p_factorial_q_factorial": expected,
        "count_matches_prediction": len(compatible) == expected,
        "nonempty": len(compatible) > 0,
        "compatible_edge_masks": compatible,
        "local_class_counts": dict(sorted(local_classes.items())),
        "all_local_classes_source_allowed": set(local_classes).issubset({"0<->5", "1<->4", "2<->3"}),
        "distinct_local_sign_tuples": len(local_tuples),
    }


def lane(chunk: int):
    start = 8 * chunk
    rows = [audit_pattern(m) for m in range(start, start + 8)]
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    valid = all(r["count_matches_prediction"] and r["nonempty"] and r["all_local_classes_source_allowed"] for r in rows)
    return {
        "iteration": "Iter078B-RG",
        "lane": chunk,
        "valid": valid,
        "scientific_outcome": "PASS" if valid else "FAIL",
        "boundary_masks": list(range(start, start + 8)),
        "sha256_rows": hashlib.sha256(canonical.encode()).hexdigest(),
        "rows": rows,
    }


def aggregate(root):
    lanes = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter078B-RG" and isinstance(obj.get("lane"), int):
                lanes[obj["lane"]] = obj
    complete = set(lanes) == {0, 1, 2, 3}
    rows = []
    if complete:
        for k in range(4):
            rows.extend(lanes[k]["rows"])
        rows.sort(key=lambda r: r["boundary_mask"])
    all_counts = complete and all(r["count_matches_prediction"] for r in rows)
    all_nonempty = complete and all(r["nonempty"] for r in rows)
    all_classes = complete and all(r["all_local_classes_source_allowed"] for r in rows)

    reversal_ok = bool(complete)
    if complete:
        by_mask = {r["boundary_mask"]: r for r in rows}
        for r in rows:
            complement = r["boundary_mask"] ^ 31
            target = set(by_mask[complement]["compatible_edge_masks"])
            mapped = {m ^ ALL_EDGE_MASK for m in r["compatible_edge_masks"]}
            if mapped != target:
                reversal_ok = False
                break

    valid = complete and all_counts and all_nonempty and all_classes and reversal_ok
    classification = (
        "ITER078B_RG_1TO5_CAUSAL_BOUNDARY_ORIENTATIONS_EXTEND_TO_FINE_ACYCLIC_K5_ALL32_EXACT_COMBINATORIAL_SCOPED"
        if valid else
        "ITER078B_RG_1TO5_CAUSAL_REFINEMENT_ORIENTATION_PREDICTION_FAILS_EXACT_SCOPED"
    )
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":")) if complete else ""
    counts_by_p = {}
    if complete:
        for p in range(6):
            vals = sorted({r["compatible_count"] for r in rows if r["p_in"] == p})
            counts_by_p[str(p)] = vals
    return {
        "iteration": "Iter078B-RG",
        "execution_valid": complete,
        "verdict": "PASS" if valid else ("FAIL" if complete else "INVALID_IMPLEMENTATION"),
        "classification": classification if complete else "ITER078B_RG_1TO5_CAUSAL_REFINEMENT_INCOMPLETE",
        "boundary_patterns_checked": len(rows),
        "all_32_nonempty": all_nonempty,
        "all_counts_match_p_factorial_q_factorial": all_counts,
        "all_local_classes_source_allowed": all_classes,
        "global_reversal_bijection": reversal_ok,
        "compatible_counts_by_p_in": counts_by_p,
        "sha256_all_rows": hashlib.sha256(canonical.encode()).hexdigest() if complete else None,
        "next_admissible_gate": "Freeze the 1->5 fine-complex amplitude/measure, boundary embedding and extension-coupling transport; then test closure of the causal refinement map before any RG fixed-point claim.",
        "claim_lock": "Causal-orientation PASS alone does not define the fine amplitude, RG map, continuum limit, regulator independence or G3.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", type=int, choices=(0, 1, 2, 3))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if (args.lane is None) == (args.aggregate_dir is None):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = lane(args.lane) if args.lane is not None else aggregate(args.aggregate_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
