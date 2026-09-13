#!/usr/bin/env python3
"""Iter077C-SM: exact first exceptional strata of the true source B-map.

Frozen by prereg/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA.md.
All rank/nullspace decisions use exact rational arithmetic.
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
AXES = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)
AXIS_NAMES = "xyz"


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


def transpose(A):
    return [list(row) for row in zip(*A)]


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
            if q:
                for j in range(c, n):
                    A[r][j] -= q * A[c][j]
    return det * sign


def directions_from_colors(colors):
    return {e: AXES[colors[i]] for i, e in enumerate(EDGES)}


def true_jacobian_from_colors(colors, include_root=False):
    directions = directions_from_colors(colors)
    cols = range(5) if include_root else range(1, 5)
    J = []
    for a, b in EDGES:
        n = directions[(a, b)]
        row = []
        for c in cols:
            s = (1 if a == c else 0) - (1 if b == c else 0)
            row.extend(Fraction(s) * x for x in n)
        J.append(row)
    return J


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


def graph_rank(colors):
    total = 0
    for color in range(3):
        es = [EDGES[i] for i, c in enumerate(colors) if c == color]
        total += 5 - component_count(es)
    return total


def vector_equilibrium(lam, colors):
    eq = [[Fraction(0), Fraction(0), Fraction(0)] for _ in range(5)]
    for eidx, (a, b) in enumerate(EDGES):
        n = AXES[colors[eidx]]
        for i in range(3):
            eq[a][i] += lam[eidx] * n[i]
            eq[b][i] -= lam[eidx] * n[i]
    return eq


def equilibrium_equivalence(colors):
    J = true_jacobian_from_colors(colors)
    Jfull = true_jacobian_from_colors(colors, include_root=True)
    left = nullspace(transpose(J))
    left_full = nullspace(transpose(Jfull))

    root_redundancy = True
    for axis in range(3):
        root_col = [Jfull[r][axis] for r in range(10)]
        sum_nonroot = [sum(Jfull[r][3 * c + axis] for c in range(1, 5)) for r in range(10)]
        root_redundancy &= all(root_col[r] == -sum_nonroot[r] for r in range(10))

    basis_equilibrium_ok = True
    for lam in left:
        eq = vector_equilibrium(lam, colors)
        basis_equilibrium_ok &= all(x == 0 for node in eq for x in node)

    return {
        "rank": rank_q(J),
        "left_nullity": len(left),
        "full_equilibrium_left_nullity": len(left_full),
        "root_columns_are_negative_nonroot_sum": bool(root_redundancy),
        "left_null_basis_satisfies_all_five_equilibria": bool(basis_equilibrium_ok),
        "nullspaces_same_dimension": len(left) == len(left_full),
    }


def first_planar_max_rank_control():
    best_rank = -1
    best = None
    for bits in itertools.product(range(2), repeat=10):
        r = graph_rank(bits)
        if r > best_rank:
            best_rank = r
            best = bits
    return best, best_rank


def first_full_span_rank9():
    for colors in itertools.product(range(3), repeat=10):
        if len(set(colors)) == 3 and graph_rank(colors) == 9:
            return colors
    return None


def tangent_vectors(axis):
    if axis == 0:
        return (AXES[1], AXES[2])
    if axis == 1:
        return (AXES[0], AXES[2])
    return (AXES[0], AXES[1])


def delta_row_dot_right(edge, tangent, right_vec):
    a, b = edge
    out = Fraction(0)
    for c in range(1, 5):
        s = (1 if a == c else 0) - (1 if b == c else 0)
        if not s:
            continue
        block = right_vec[3 * (c - 1):3 * c]
        out += Fraction(s) * sum(tangent[i] * block[i] for i in range(3))
    return out


def lane_a():
    result = (ROOT / "results" / "ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md").read_text(encoding="utf-8")
    ledger = (ROOT / "status" / "ITER077_PROVENANCE_LEDGER.md").read_text(encoding="utf-8")
    source = (ROOT / "sources" / "CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA.md").read_text(encoding="utf-8")
    locks = {
        "sm_rank10_authority": "rank_Q(J)=10" in result,
        "scalar_nontransfer_authority": "0/6" in result and "not identities of the true source differential" in result,
        "ledger_sm_alias": "Iter077A-SM" in ledger,
        "ledger_ff_alias": "Iter077A-FF" in ledger,
        "ledger_bch_alias": "Iter077B-BCH" in ledger,
        "ten_wedge_normals": "ten unit Bloch normals" in prereg,
        "source_jacobian": "J_(ab),(c,i)" in prereg and "dB_ab = n_ab . (dx_a-dx_b)" in source,
        "scalar_firewall": "must not replace it by scalar K5 cycle relations" in prereg,
        "epsilon_lock": "published spectral `i epsilon`" in prereg,
    }
    return {"iteration": "Iter077C-SM", "lane": "A", "valid": bool(all(locks.values())), "locks": locks}


def lane_b():
    controls = []
    valid = True
    for axis in range(3):
        colors = (axis,) * 10
        eq = equilibrium_equivalence(colors)
        ok = eq["rank"] == 4 and eq["left_nullity"] == 6 and eq["full_equilibrium_left_nullity"] == 6 and eq["root_columns_are_negative_nonroot_sum"] and eq["left_null_basis_satisfies_all_five_equilibria"] and eq["nullspaces_same_dimension"]
        valid &= ok
        controls.append({"name": f"monochromatic_{AXIS_NAMES[axis]}", "colors": AXIS_NAMES[axis] * 10, "ok": bool(ok), **eq})

    planar, max_rank = first_planar_max_rank_control()
    peq = equilibrium_equivalence(planar)
    planar_ok = max_rank == 8 and peq["rank"] == 8 and peq["left_nullity"] == 2 and peq["full_equilibrium_left_nullity"] == 2 and peq["root_columns_are_negative_nonroot_sum"] and peq["left_null_basis_satisfies_all_five_equilibria"] and peq["nullspaces_same_dimension"]
    valid &= planar_ok
    controls.append({"name": "lex_first_planar_max_rank", "colors": "".join(AXIS_NAMES[c] for c in planar), "ok": bool(planar_ok), **peq})

    return {
        "iteration": "Iter077C-SM",
        "lane": "B",
        "valid": bool(valid),
        "planar_max_rank": max_rank,
        "planar_selected_colors": "".join(AXIS_NAMES[c] for c in planar),
        "controls": controls,
        "exact_statement": "rank(J)<10 iff a nonzero vector self-stress satisfies vector equilibrium at all five K5 nodes; root equilibrium is redundant after gauge fixing.",
    }


def lane_c():
    colors = first_full_span_rank9()
    if colors is None:
        return {
            "iteration": "Iter077C-SM",
            "lane": "C",
            "valid": False,
            "scientific_outcome": "BLOCKED",
            "classification": "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATUM_BLOCKED_OBJECT_DEFINITION",
            "reason": "No full-span rank-9 axis witness exists under the frozen selection rule.",
        }

    J = true_jacobian_from_colors(colors)
    rank = rank_q(J)
    left = nullspace(transpose(J))
    right = nullspace(J)
    object_valid = rank == 9 and len(set(colors)) == 3 and len(left) == 1 and len(right) == 3
    if not object_valid:
        return {
            "iteration": "Iter077C-SM",
            "lane": "C",
            "valid": False,
            "scientific_outcome": "BLOCKED",
            "classification": "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATUM_BLOCKED_OBJECT_DEFINITION",
            "reason": "Frozen witness does not have the required exact rank/nullities.",
            "colors": "".join(AXIS_NAMES[c] for c in colors),
            "rank_Q": rank,
            "left_nullity": len(left),
            "right_nullity": len(right),
        }

    lam = left[0]
    L = [[Fraction(0) for _ in range(20)] for _ in range(3)]
    tangent_labels = []
    col = 0
    tangent_orthogonal = True
    for eidx, edge in enumerate(EDGES):
        normal = AXES[colors[eidx]]
        for t in tangent_vectors(colors[eidx]):
            tangent_orthogonal &= sum(normal[i] * t[i] for i in range(3)) == 0
            tangent_labels.append(f"{edge[0]}{edge[1]}:{AXIS_NAMES[AXES.index(t)]}")
            for k, rv in enumerate(right):
                L[k][col] = lam[eidx] * delta_row_dot_right(edge, t, rv)
            col += 1

    lrank = rank_q(L)
    minor = None
    if lrank == 3:
        for cols in itertools.combinations(range(20), 3):
            M = [[L[r][c] for c in cols] for r in range(3)]
            det = determinant_fraction(M)
            if det != 0:
                minor = {"columns": list(cols), "labels": [tangent_labels[c] for c in cols], "determinant": fstr(det)}
                break

    eq = vector_equilibrium(lam, colors)
    stress_ok = all(x == 0 for node in eq for x in node)
    valid = bool(object_valid and tangent_orthogonal and stress_ok)
    if not valid:
        outcome = "BLOCKED"
        classification = "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATUM_BLOCKED_OBJECT_DEFINITION"
    elif lrank == 3:
        outcome = "PASS"
        classification = "ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED"
    else:
        outcome = "FAIL"
        classification = "ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_NONTRANSVERSE_LOWER_CODIM_EXACT_SCOPED"

    return {
        "iteration": "Iter077C-SM",
        "lane": "C",
        "valid": valid,
        "scientific_outcome": outcome,
        "classification": classification,
        "colors": "".join(AXIS_NAMES[c] for c in colors),
        "normal_span_dimension": len(set(colors)),
        "rank_Q": rank,
        "left_nullity": len(left),
        "right_nullity": len(right),
        "self_stress_lambda": [fstr(x) for x in lam],
        "self_stress_equilibrium_exact": bool(stress_ok),
        "right_null_basis": [[fstr(x) for x in rv] for rv in right],
        "tangent_directions": tangent_labels,
        "all_tangents_orthogonal": bool(tangent_orthogonal),
        "structured_normal_map_shape": [3, 20],
        "structured_normal_map_rank_Q": lrank,
        "nonzero_rank3_minor": minor,
        "local_codimension_if_transverse": 3 if lrank == 3 else None,
    }


def lane_d():
    expected_hist = {4: 3, 5: 60, 6: 600, 7: 4800, 8: 17766, 9: 26100, 10: 9720}
    joint = Counter()
    rank_hist = Counter()
    selected = first_full_span_rank9()
    planar, _ = first_planar_max_rank_control()
    deterministic = []

    for idx, colors in enumerate(itertools.product(range(3), repeat=10)):
        rank = graph_rank(colors)
        span = len(set(colors))
        stress = 10 - rank
        joint[(rank, span, stress)] += 1
        rank_hist[rank] += 1
        if idx < 32:
            deterministic.append(colors)

    controls = []
    all_crosschecks = True
    candidates = [(0,) * 10, (1,) * 10, (2,) * 10, planar] + ([selected] if selected else []) + deterministic
    seen = set()
    for colors in candidates:
        if colors in seen:
            continue
        seen.add(colors)
        J = true_jacobian_from_colors(colors)
        direct_rank = rank_q(J)
        graph_r = graph_rank(colors)
        stress_dim = len(nullspace(transpose(J)))
        ok = direct_rank == graph_r and stress_dim == 10 - direct_rank
        all_crosschecks &= ok
        controls.append({
            "colors": "".join(AXIS_NAMES[c] for c in colors),
            "normal_span_dimension": len(set(colors)),
            "graph_rank": graph_r,
            "direct_rank_Q": direct_rank,
            "left_nullity": stress_dim,
            "match": bool(ok),
        })

    hist_ok = dict(rank_hist) == expected_hist
    selected_ok = selected is not None and len(set(selected)) == 3 and graph_rank(selected) == 9
    valid = bool(sum(rank_hist.values()) == 3 ** 10 and hist_ok and selected_ok and all_crosschecks)
    return {
        "iteration": "Iter077C-SM",
        "lane": "D",
        "valid": valid,
        "assignments_enumerated": sum(rank_hist.values()),
        "rank_histogram": {str(k): rank_hist[k] for k in sorted(rank_hist)},
        "joint_rank_span_stress_census": [
            {"rank": r, "normal_span_dimension": s, "self_stress_dimension": d, "count": joint[(r, s, d)]}
            for r, s, d in sorted(joint)
        ],
        "full_span_rank9_count": joint[(9, 3, 1)],
        "full_span_rank10_count": joint[(10, 3, 0)],
        "selected_rank9_colors": "".join(AXIS_NAMES[c] for c in selected) if selected else None,
        "rank_histogram_matches_iter077a_sm": bool(hist_ok),
        "direct_crosschecks": controls,
    }


def aggregate(aggregate_dir: Path):
    lanes = {}
    for p in aggregate_dir.glob("**/iter077c_sm_*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        lane = data.get("lane")
        if lane in {"A", "B", "C", "D"}:
            lanes[lane] = data
    required = {"A", "B", "C", "D"}
    all_present = set(lanes) == required
    abd_valid = all_present and all(bool(lanes[k].get("valid")) for k in ("A", "B", "D"))
    c_valid = all_present and bool(lanes["C"].get("valid"))
    c_outcome = lanes.get("C", {}).get("scientific_outcome", "BLOCKED")

    if abd_valid and c_valid and c_outcome in {"PASS", "FAIL"}:
        verdict = c_outcome
        classification = lanes["C"]["classification"]
        execution_valid = True
    else:
        verdict = "BLOCKED"
        classification = "ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATUM_BLOCKED_OBJECT_DEFINITION"
        execution_valid = False

    return {
        "iteration": "Iter077C-SM",
        "execution_valid": execution_valid,
        "verdict": verdict,
        "classification": classification,
        "lanes_found": sorted(lanes),
        "lane_valid": {k: bool(lanes[k].get("valid")) for k in sorted(lanes)},
        "selected_rank9_colors": lanes.get("C", {}).get("colors"),
        "structured_normal_map_rank_Q": lanes.get("C", {}).get("structured_normal_map_rank_Q"),
        "local_codimension_if_transverse": lanes.get("C", {}).get("local_codimension_if_transverse"),
        "full_span_rank9_count_axis_census": lanes.get("D", {}).get("full_span_rank9_count"),
        "next_admissible_gate": "At a frozen exact rank-9 source stratum, include the true nonlinear B jet normal to the stratum and test the local pullback/scaling of the source contact distributions before any full-vertex finiteness or epsilon^-1 claim.",
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

    if args.aggregate_dir:
        if not out.get("execution_valid", False):
            raise SystemExit(1)
    elif not out.get("valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
