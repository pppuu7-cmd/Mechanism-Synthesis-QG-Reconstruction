#!/usr/bin/env python3
"""Iter077A: exact true-source B-map transversality audit.

Frozen by prereg/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md.
No floating-point rank decisions are used.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = list(itertools.combinations(range(5), 2))
AXES = {
    "x": (Fraction(1), Fraction(0), Fraction(0)),
    "y": (Fraction(0), Fraction(1), Fraction(0)),
    "z": (Fraction(0), Fraction(0), Fraction(1)),
}
COL_LABELS = [f"v{v}{axis}" for v in range(1, 5) for axis in "xyz"]


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def rref(matrix):
    A = [[Fraction(x) for x in row] for row in matrix]
    m = len(A)
    n = len(A[0]) if m else 0
    pivots = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots


def rank_q(matrix) -> int:
    return len(rref(matrix)[1])


def nullspace(matrix):
    R, pivots = rref(matrix)
    n = len(R[0]) if R else 0
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0) for _ in range(n)]
        v[f] = Fraction(1)
        for row, p in enumerate(pivots):
            v[p] = -R[row][f]
        basis.append(v)
    return basis


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul_row(v, A):
    return [sum(v[i] * A[i][j] for i in range(len(v))) for j in range(len(A[0]))]


def determinant_fraction(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    sign = 1
    det = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            sign *= -1
        pivot = A[c][c]
        det *= pivot
        for j in range(c, n):
            A[c][j] /= pivot
        for r in range(c + 1, n):
            q = A[r][c]
            if q != 0:
                for j in range(c, n):
                    A[r][j] -= q * A[c][j]
    return det * sign


def bloch_from_spinor(a, b):
    """a,b are Gaussian integer pairs (re,im); return exact Pauli Bloch vector."""
    ar, ai = a
    br, bi = b
    norm = ar * ar + ai * ai + br * br + bi * bi
    re_ab = ar * br + ai * bi
    im_ab = ar * bi - ai * br
    return (
        Fraction(2 * re_ab, norm),
        Fraction(2 * im_ab, norm),
        Fraction(ar * ar + ai * ai - br * br - bi * bi, norm),
    )


def witness_directions():
    edge_sets = {
        "x": {(0, 1), (1, 2), (2, 3), (3, 4)},
        "y": {(0, 2), (0, 3), (1, 3), (1, 4)},
        "z": {(0, 4), (2, 4)},
    }
    out = {}
    for axis, es in edge_sets.items():
        for e in es:
            out[e] = AXES[axis]
    assert set(out) == set(EDGES)
    return out


def true_jacobian(directions):
    J = []
    for a, b in EDGES:
        n = directions[(a, b)]
        row = []
        for c in range(1, 5):
            s = (1 if a == c else 0) - (1 if b == c else 0)
            row.extend([Fraction(s) * x for x in n])
        J.append(row)
    return J


def scalar_incidence():
    I = []
    for a, b in EDGES:
        I.append([
            Fraction((1 if a == c else 0) - (1 if b == c else 0))
            for c in range(1, 5)
        ])
    return I


def lane_a():
    supplement = (ROOT / "sources" / "CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md").read_text(encoding="utf-8")
    source = (ROOT / "sources" / "CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY.md").read_text(encoding="utf-8")
    locks = {
        "source_eq17_spinor_restrictor": "theta(kappa_ab * B(z,g))" in source,
        "source_B_eq32": "B(z,g) = log(" in source,
        "ten_wedge_true_map": "ten-component source map" in prereg,
        "independent_wedge_spinors": "ten independent auxiliary spinors" in prereg,
        "derivative_frozen": "J_e,(c,i)" in prereg and "d B_ab = n_ab . (d x_a - d x_b)" in supplement,
        "scalar_surrogate_firewall": "scalar K5 incidence" in prereg,
        "epsilon_lock": "published spectral `i epsilon`" in prereg,
    }
    return {"iteration": "Iter077A", "lane": "A", "valid": all(locks.values()), "source_locks": locks}


def lane_b():
    expected = {
        "x": bloch_from_spinor((1, 0), (1, 0)),
        "y": bloch_from_spinor((1, 0), (0, 1)),
        "z": bloch_from_spinor((1, 0), (0, 0)),
    }
    bloch_ok = expected == AXES
    directions = witness_directions()
    J = true_jacobian(directions)
    rank = rank_q(J)
    minor = None
    for cols in itertools.combinations(range(12), 10):
        M = [[row[c] for c in cols] for row in J]
        det = determinant_fraction(M)
        if det != 0:
            minor = {"columns": list(cols), "column_labels": [COL_LABELS[c] for c in cols], "determinant": fstr(det)}
            break
    valid = bool(bloch_ok and rank == 10 and minor is not None)
    return {
        "iteration": "Iter077A",
        "lane": "B",
        "valid": valid,
        "bloch_vectors": {k: [fstr(x) for x in v] for k, v in expected.items()},
        "bloch_spinor_checks_exact": bloch_ok,
        "jacobian_shape": [10, 12],
        "rank_Q": rank,
        "left_nullity": 10 - rank,
        "nonzero_maximal_minor": minor,
        "witness_edge_directions": {f"{a}{b}": next(k for k, v in AXES.items() if directions[(a, b)] == v) for a, b in EDGES},
    }


def lane_c():
    I = scalar_incidence()
    J = true_jacobian(witness_directions())
    rank_I = rank_q(I)
    rank_J = rank_q(J)
    left_I = nullspace(transpose(I))
    left_J = nullspace(transpose(J))
    transfer = []
    for idx, v in enumerate(left_I):
        pushed = matmul_row(v, J)
        transfer.append({
            "basis_index": idx,
            "scalar_relation": [fstr(x) for x in v],
            "annihilates_true_J": all(x == 0 for x in pushed),
            "true_J_image": [fstr(x) for x in pushed],
        })
    valid = bool(rank_I == 4 and len(left_I) == 6 and rank_J == 10 and len(left_J) == 0 and all(not x["annihilates_true_J"] for x in transfer))
    return {
        "iteration": "Iter077A",
        "lane": "C",
        "valid": valid,
        "scalar_incidence_rank_Q": rank_I,
        "scalar_left_nullity": len(left_I),
        "true_witness_rank_Q": rank_J,
        "true_witness_left_nullity": len(left_J),
        "scalar_cycle_relations_transferring": sum(x["annihilates_true_J"] for x in transfer),
        "cycle_basis_checks": transfer,
    }


def component_count(edge_subset):
    parent = list(range(5))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    for a, b in edge_subset:
        union(a, b)
    return len({find(v) for v in range(5)})


def graph_rank_for_coloring(colors):
    total = 0
    for color in range(3):
        es = [EDGES[i] for i, c in enumerate(colors) if c == color]
        total += 5 - component_count(es)
    return total


def direct_matrix_for_coloring(colors):
    dirs = {e: AXES["xyz"[colors[i]]] for i, e in enumerate(EDGES)}
    return true_jacobian(dirs)


def lane_d():
    hist = Counter()
    full_rank = 0
    forest_full_rank = 0
    witness_dirs = witness_directions()
    witness_colors = tuple("xyz".index(next(k for k, v in AXES.items() if witness_dirs[e] == v)) for e in EDGES)
    sample = []
    deterministic_sample = []

    for idx, colors in enumerate(itertools.product(range(3), repeat=10)):
        rg = graph_rank_for_coloring(colors)
        hist[rg] += 1
        if rg == 10:
            full_rank += 1
        forest = True
        for color in range(3):
            es = [EDGES[i] for i, c in enumerate(colors) if c == color]
            if (5 - component_count(es)) != len(es):
                forest = False
                break
        if forest:
            forest_full_rank += 1
        if idx < 32:
            deterministic_sample.append(colors)

    controls = [witness_colors, (0,) * 10, (1,) * 10, (2,) * 10] + deterministic_sample
    seen = set()
    direct_ok = True
    for colors in controls:
        if colors in seen:
            continue
        seen.add(colors)
        rg = graph_rank_for_coloring(colors)
        rd = rank_q(direct_matrix_for_coloring(colors))
        ok = rg == rd
        direct_ok &= ok
        sample.append({"colors": "".join("xyz"[c] for c in colors), "graph_rank": rg, "direct_rank_Q": rd, "match": ok})

    monochrome_ranks = [graph_rank_for_coloring((c,) * 10) for c in range(3)]
    witness_rank = graph_rank_for_coloring(witness_colors)
    valid = bool(
        sum(hist.values()) == 3 ** 10
        and witness_rank == 10
        and monochrome_ranks == [4, 4, 4]
        and direct_ok
        and full_rank == forest_full_rank
    )
    return {
        "iteration": "Iter077A",
        "lane": "D",
        "valid": valid,
        "assignments_enumerated": sum(hist.values()),
        "rank_histogram": {str(k): hist[k] for k in sorted(hist)},
        "full_rank_assignments": full_rank,
        "all_color_classes_forests_assignments": forest_full_rank,
        "full_rank_iff_all_color_classes_forests_in_census": full_rank == forest_full_rank,
        "witness_rank": witness_rank,
        "monochromatic_control_ranks": monochrome_ranks,
        "direct_rank_crosschecks": sample,
    }


def aggregate(aggregate_dir: Path):
    lanes = {}
    for p in aggregate_dir.glob("**/iter077a_*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        lane = data.get("lane")
        if lane in {"A", "B", "C", "D"}:
            lanes[lane] = data
    required = {"A", "B", "C", "D"}
    all_present = set(lanes) == required
    all_valid = all_present and all(bool(lanes[k].get("valid")) for k in required)
    if all_valid:
        classification = "ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED"
        verdict = "PASS"
    elif all_present and lanes.get("A", {}).get("valid") and lanes.get("B", {}).get("rank_Q", 10) < 10:
        classification = "ITER077A_TRUE_SOURCE_B_MAP_FULL_RANK_WITNESS_FAILS_EXACT_SCOPED"
        verdict = "FAIL"
    else:
        classification = "ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_BLOCKED_OBJECT_OR_SOURCE_DEFINITION"
        verdict = "BLOCKED"
    return {
        "iteration": "Iter077A",
        "valid": all_valid,
        "verdict": verdict,
        "classification": classification,
        "lanes_found": sorted(lanes),
        "lane_valid": {k: bool(lanes[k].get("valid")) for k in sorted(lanes)},
        "rank_true_witness": lanes.get("B", {}).get("rank_Q"),
        "rank_scalar_incidence": lanes.get("C", {}).get("scalar_incidence_rank_Q"),
        "scalar_cycle_relations_transferring": lanes.get("C", {}).get("scalar_cycle_relations_transferring"),
        "full_rank_axis_assignments": lanes.get("D", {}).get("full_rank_assignments"),
        "next_admissible_gate": "Classify the first exceptional source strata Sigma={rank dB<10} using the true nonlinear B map, then test their distributional contribution before any reduced K4/Hodge coefficient is treated as physical.",
        "claim_lock": "No full causal-vertex finiteness/divergence theorem, regulator-independence theorem, physical source-to-K4 pushforward, nominal epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=["A", "B", "C", "D"])
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        out = aggregate(Path(args.aggregate_dir))
    else:
        if not args.lane:
            raise SystemExit("--lane required unless --aggregate-dir is used")
        out = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}[args.lane]()
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if args.aggregate_dir and out["verdict"] != "PASS":
        raise SystemExit(1)
    if not args.aggregate_dir and not out.get("valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
