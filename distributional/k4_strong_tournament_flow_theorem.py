#!/usr/bin/env python3
"""Iter058: exact K4 tournament/positive-circulation equivalence audit.

Preregistered at commit 51c3e04da81652060a3bc76c2bad5c9825faecca
before implementation/output.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import EDGES, EDGE_NAMES, TREES, incidence
from distributional.k4_global_contour_compatibility import exact_cycle_matrix
from distributional.k4_signed_normal_positive_circuit_atlas import complete_minimal_positive_circuits

EDGE_TO_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
ALL_SIGNS = tuple(itertools.product((1, -1), repeat=6))
PERMS = tuple(itertools.permutations(range(4)))
VERTICES = tuple(range(4))


def sign_text(s):
    return "".join("+" if z > 0 else "-" for z in s)


def directed_edges(s):
    out = []
    for se, (a, b) in zip(s, EDGES):
        out.append((a, b) if se > 0 else (b, a))
    return tuple(out)


def adjacency(s):
    adj = {v: [] for v in VERTICES}
    for u, v in directed_edges(s):
        adj[u].append(v)
    for u in adj:
        adj[u].sort()
    return adj


def reachable(adj, start):
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return seen


def strongly_connected(s):
    adj = adjacency(s)
    return all(len(reachable(adj, v)) == 4 for v in VERTICES)


def shortest_lex_path(adj, start, goal):
    """Lexicographically first among shortest directed paths."""
    q = deque([[start]])
    best_depth = None
    candidates = []
    seen_depth = {start: 0}
    while q:
        path = q.popleft()
        d = len(path) - 1
        if best_depth is not None and d > best_depth:
            break
        u = path[-1]
        if u == goal:
            best_depth = d
            candidates.append(path)
            continue
        for v in adj[u]:
            nd = d + 1
            if best_depth is not None and nd > best_depth:
                continue
            if v in path:
                continue
            old = seen_depth.get(v)
            if old is None or nd <= old:
                seen_depth[v] = nd if old is None else min(old, nd)
                q.append(path + [v])
    if not candidates:
        return None
    return min(candidates)


def traversal_to_canonical_flow(path_edges):
    x = [0] * 6
    for u, v in path_edges:
        idx = EDGE_TO_INDEX[tuple(sorted((u, v)))]
        a, b = EDGES[idx]
        x[idx] += 1 if (u, v) == (a, b) else -1
    return tuple(x)


def constructive_positive_circulation(s):
    adj = adjacency(s)
    cycles = []
    total = [0] * 6
    for u, v in directed_edges(s):
        ret = shortest_lex_path(adj, v, u)
        if ret is None:
            return None, None
        traversals = [(u, v)] + list(zip(ret[:-1], ret[1:]))
        flow = traversal_to_canonical_flow(traversals)
        # Every traversal must agree with the tournament orientation.
        if any(flow[e] != 0 and flow[e] * s[e] <= 0 for e in range(6)):
            raise RuntimeError("constructed directed cycle disagrees with sign orientation")
        for e in range(6):
            total[e] += flow[e]
        cycles.append({
            "seed_edge": [u, v],
            "return_path": list(map(int, ret)),
            "cycle_vertices": [u, v] + list(map(int, ret[1:])),
            "canonical_flow": list(map(int, flow)),
        })
    return tuple(total), cycles


def find_one_way_cut(s):
    dedges = set(directed_edges(s))
    candidates = []
    for r in range(1, 4):
        for U in itertools.combinations(VERTICES, r):
            U = set(U)
            comp = set(VERTICES) - U
            crossing = []
            directions = []
            for a in sorted(U):
                for b in sorted(comp):
                    if (a, b) in dedges:
                        crossing.append((a, b))
                        directions.append("out")
                    elif (b, a) in dedges:
                        crossing.append((b, a))
                        directions.append("in")
                    else:
                        raise RuntimeError("missing tournament edge")
            if directions and (all(x == "out" for x in directions) or all(x == "in" for x in directions)):
                direction = directions[0]
                candidates.append((tuple(sorted(U)), direction, tuple(crossing)))
    if not candidates:
        return None
    return min(candidates, key=lambda z: (len(z[0]), z[0], z[1]))


def cut_certificate(s, cut):
    B = incidence()
    U, direction, crossing = cut
    cut_row = sp.zeros(1, 6)
    for u in U:
        cut_row += B[u, :]
    aligned_coeffs = [sp.simplify(cut_row[0, e] * s[e]) for e in range(6)]
    crossing_idx = [e for e, z in enumerate(aligned_coeffs) if z != 0]
    nonzero_coeffs = [aligned_coeffs[e] for e in crossing_idx]
    uniform_nonzero_sign = (
        len(nonzero_coeffs) > 0
        and (all(z == 1 for z in nonzero_coeffs) or all(z == -1 for z in nonzero_coeffs))
    )
    # Internal edges cancel from summed conservation equations exactly.
    expected_crossing = sorted(
        EDGE_TO_INDEX[tuple(sorted((u, v)))] for u, v in crossing
    )
    valid = sorted(crossing_idx) == expected_crossing and uniform_nonzero_sign
    return {
        "U": list(U),
        "direction": direction,
        "crossing_directed_edges": [list(e) for e in crossing],
        "crossing_edge_indices": crossing_idx,
        "cut_row_times_sign": list(map(str, aligned_coeffs)),
        "strict_flux_sign": int(nonzero_coeffs[0]) if uniform_nonzero_sign else None,
        "valid": bool(valid),
    }


def score_and_triangles(s):
    dedges = set(directed_edges(s))
    outdeg = [0] * 4
    for u, v in dedges:
        outdeg[u] += 1
    cyc = 0
    for tri in itertools.combinations(VERTICES, 3):
        deg = []
        for u in tri:
            deg.append(sum(1 for v in tri if v != u and (u, v) in dedges))
        if sorted(deg) == [1, 1, 1]:
            cyc += 1
    return sorted(outdeg, reverse=True), cyc


def orientation_action(s, perm):
    target = [None] * 6
    edge_map = [None] * 6
    q_target = [None] * 6
    for old_e, (a, b) in enumerate(EDGES):
        pa, pb = perm[a], perm[b]
        new_e = EDGE_TO_INDEX[tuple(sorted((pa, pb)))]
        q = 1 if pa < pb else -1
        edge_map[old_e] = new_e
        q_target[new_e] = q
        target[new_e] = q * s[old_e]
    valid = sorted(edge_map) == list(range(6)) and all(z in (-1, 1) for z in target)
    return tuple(target), tuple(edge_map), bool(valid)


def connected_orbits(adj):
    seen = set()
    orbits = []
    for node in sorted(adj):
        if node in seen:
            continue
        comp = set()
        stack = [node]
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adj[x] - comp)
        seen |= comp
        orbits.append(sorted(comp))
    return sorted(orbits, key=lambda o: (len(o), o))


def audit_one(s):
    txt = sign_text(s)
    strong = strongly_connected(s)
    score, triangles = score_and_triangles(s)
    B = incidence()

    constructive_x = None
    constructive_cycles = None
    cut = None
    graph_cert_valid = True
    basis_reconstruction = {}

    if strong:
        constructive_x, constructive_cycles = constructive_positive_circulation(s)
        if constructive_x is None:
            graph_cert_valid = False
        else:
            xv = sp.Matrix(constructive_x)
            conservation = sp.simplify(B * xv)
            sign_margins = [sp.simplify(s[e] * xv[e]) for e in range(6)]
            graph_cert_valid = graph_cert_valid and all(sp.simplify(z) == 0 for z in conservation)
            graph_cert_valid = graph_cert_valid and all(z.is_positive is True for z in sign_margins)
            for tree in sorted(TREES):
                _, _, A, _, _, chords, _ = exact_cycle_matrix(tree)
                v = sp.Matrix([xv[e] for e in chords])
                residual = sp.simplify(A * v - xv)
                margins = sp.simplify(sp.diag(*s) * A * v)
                ok = all(sp.simplify(z) == 0 for z in residual) and all(z.is_positive is True for z in margins)
                graph_cert_valid = graph_cert_valid and ok
                basis_reconstruction[tree] = {
                    "v": list(map(str, v)),
                    "exact": bool(ok),
                    "signed_margins": list(map(str, margins)),
                }
    else:
        raw_cut = find_one_way_cut(s)
        if raw_cut is None:
            graph_cert_valid = False
        else:
            cut = cut_certificate(s, raw_cut)
            graph_cert_valid = graph_cert_valid and cut["valid"]

    # Independent positive-circuit feasibility on every frozen basis.
    pc_by_tree = {}
    pc_feasible_values = []
    pc_valid = True
    for tree in sorted(TREES):
        _, _, A, _, _, _, _ = exact_cycle_matrix(tree)
        M = sp.diag(*s) * A
        circuits, meta = complete_minimal_positive_circuits(M)
        feasible = len(circuits) == 0
        pc_by_tree[tree] = {
            "feasible": bool(feasible),
            "circuit_count": len(circuits),
            "supports": [c["support"] for c in circuits],
        }
        pc_feasible_values.append(feasible)
        pc_valid = pc_valid and meta["tested_support_count"] == 56
        pc_valid = pc_valid and meta["minimality_valid"] and meta["reconstruction_valid"]
    pc_basis_consistent = all(v == pc_feasible_values[0] for v in pc_feasible_values)
    pc_feasible = pc_feasible_values[0]

    equivalence = strong == pc_feasible
    cert_matches = strong == (constructive_x is not None)
    valid = graph_cert_valid and pc_valid and pc_basis_consistent and cert_matches

    return {
        "sign_text": txt,
        "strongly_connected": bool(strong),
        "score_sequence_desc": score,
        "directed_triangle_count": triangles,
        "constructive_positive_circulation": list(map(int, constructive_x)) if constructive_x is not None else None,
        "constructive_cycles": constructive_cycles,
        "one_way_cut_certificate": cut,
        "basis_reconstruction": basis_reconstruction,
        "positive_circuit_by_tree": pc_by_tree,
        "positive_circuit_basis_consistent": bool(pc_basis_consistent),
        "strict_chamber_feasible": bool(pc_feasible),
        "strong_connectivity_equals_strict_chamber": bool(equivalence),
        "graph_certificate_valid": bool(graph_cert_valid),
        "valid": bool(valid),
    }


def run_audit():
    rows = [audit_one(s) for s in ALL_SIGNS]
    per = {r["sign_text"]: r for r in rows}
    all_valid = all(r["valid"] for r in rows)
    all_equiv = all(r["strong_connectivity_equals_strict_chamber"] for r in rows)

    adjacency_orbits = {sign_text(s): set() for s in ALL_SIGNS}
    action_valid = True
    for s in ALL_SIGNS:
        src = sign_text(s)
        for perm in PERMS:
            tgt_tuple, edge_map, ok = orientation_action(s, perm)
            tgt = sign_text(tgt_tuple)
            action_valid = action_valid and ok and tgt in per
            adjacency_orbits[src].add(tgt)
            adjacency_orbits[tgt].add(src)
    orbits = connected_orbits(adjacency_orbits)

    orbit_rows = []
    orbit_valid = True
    strong_orbits = []
    for idx, orbit in enumerate(orbits):
        strong_vals = {per[s]["strongly_connected"] for s in orbit}
        scores = {tuple(per[s]["score_sequence_desc"]) for s in orbit}
        tri = {per[s]["directed_triangle_count"] for s in orbit}
        feas = {per[s]["strict_chamber_feasible"] for s in orbit}
        consistent = len(strong_vals) == len(scores) == len(tri) == len(feas) == 1
        orbit_valid = orbit_valid and consistent
        is_strong = next(iter(strong_vals)) if len(strong_vals) == 1 else None
        if is_strong:
            strong_orbits.append(idx)
        orbit_rows.append({
            "orbit_index": idx,
            "size": len(orbit),
            "members": orbit,
            "strongly_connected": is_strong,
            "strict_chamber_feasible": next(iter(feas)) if len(feas) == 1 else None,
            "score_sequence_desc": list(next(iter(scores))) if len(scores) == 1 else None,
            "directed_triangle_count": next(iter(tri)) if len(tri) == 1 else None,
            "invariants_constant": bool(consistent),
        })

    unique_strong_orbit = len(strong_orbits) == 1
    all_valid = all_valid and action_valid and orbit_valid

    if not all_valid:
        classification = "ITER058_GRAPH_FLOW_AUDIT_INVALID"
    elif not all_equiv:
        classification = "K4_STRICT_CHAMBER_STRONG_TOURNAMENT_EQUIVALENCE_FAIL"
    else:
        classification = "K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT"

    return {
        "iteration": "Iter058",
        "classification": classification,
        "sign_vector_count": len(rows),
        "all_valid": bool(all_valid),
        "all_64_equivalence_pass": bool(all_equiv),
        "strongly_connected_count": sum(r["strongly_connected"] for r in rows),
        "strict_chamber_feasible_count": sum(r["strict_chamber_feasible"] for r in rows),
        "constructive_positive_circulation_count": sum(r["constructive_positive_circulation"] is not None for r in rows),
        "one_way_cut_certificate_count": sum(r["one_way_cut_certificate"] is not None for r in rows),
        "s4_orbit_count": len(orbits),
        "unique_strongly_connected_orbit": bool(unique_strong_orbit),
        "strongly_connected_orbit_indices": strong_orbits,
        "orbit_summaries": orbit_rows,
        "rows": rows,
        "claim_lock": (
            "Exact K4 graph-flow explanation of the frozen affine signed-normal surrogate only; no claim that the physical "
            "Toller vertex selects tournament strong connectivity, no K5/G3/F9/G8 or new-physics promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = run_audit()
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    keys = [
        "iteration", "classification", "sign_vector_count", "all_valid",
        "all_64_equivalence_pass", "strongly_connected_count",
        "strict_chamber_feasible_count", "constructive_positive_circulation_count",
        "one_way_cut_certificate_count", "s4_orbit_count",
        "unique_strongly_connected_orbit", "strongly_connected_orbit_indices",
        "orbit_summaries",
    ]
    print(json.dumps({k: out[k] for k in keys}, indent=2))


if __name__ == "__main__":
    main()
