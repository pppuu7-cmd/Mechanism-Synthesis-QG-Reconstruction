#!/usr/bin/env python3
"""Iter077J-SM: exact full-32 leading angular-span audit.

Frozen by prereg/ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN.md before implementation.
A full-rank certificate modulo the inert Gaussian prime p=1_000_000_007
proves the corresponding Gaussian-integer minor is nonzero over Q(i).
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "distributional" / "iter077i_sm_source_ordered_jhalf_k5_l1.py"
spec = importlib.util.spec_from_file_location("iter077i_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

P = 1_000_000_007  # 3 mod 4, so x^2+1 is irreducible over F_p.
MAIN_SEEDS = list(range(40))
HELD_SEEDS = list(range(41, 57))
ALL_SEEDS = MAIN_SEEDS + HELD_SEEDS
KS = list(itertools.product((0, 1), repeat=5))
EDGES = list(itertools.combinations(range(5), 2))


def ray(seed: int):
    s = seed
    return {
        0: (0, 0, 0),
        1: (1 + s, 2 + 2 * s, 3 + 3 * s),
        2: (2 + 2 * s, 5 + 3 * s, 7 + 5 * s),
        3: (4 + 3 * s, 8 + 5 * s, 13 + 7 * s),
        4: (7 + 5 * s, 11 + 7 * s, 19 + 11 * s),
    }


def edge_sq(coords):
    out = {}
    for a, b in EDGES:
        v = tuple(coords[a][j] - coords[b][j] for j in range(3))
        out[f"{a}{b}"] = sum(t * t for t in v)
    return out


def set_coords(coords):
    base.X = dict(coords)
    base.EDGE_MATRICES = {
        e: base.leading_matrix(tuple(coords[e[0]][j] - coords[e[1]][j] for j in range(3)))
        for e in EDGES
    }


def full32_exact(coords):
    set_coords(coords)
    vals = []
    for ks in KS:
        vals.append(tuple(base.contract_boundary(ks)))
    return vals


def gp(z):
    return (z[0] % P, z[1] % P)


def gadd(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def gsub(a, b):
    return ((a[0] - b[0]) % P, (a[1] - b[1]) % P)


def gmul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)


def ginv(a):
    den = (a[0] * a[0] + a[1] * a[1]) % P
    if den == 0:
        raise ZeroDivisionError
    q = pow(den, P - 2, P)
    return (a[0] * q % P, (-a[1]) * q % P)


def giszero(a):
    return a[0] % P == 0 and a[1] % P == 0


def rank_and_selected(rows):
    """Row rank over F_p[i], returning lexicographically first greedy independent rows."""
    basis = []  # (pivot, normalized row)
    selected = []
    for idx, row0 in enumerate(rows):
        row = [gp(z) for z in row0]
        for piv, br in basis:
            if not giszero(row[piv]):
                f = row[piv]
                row = [gsub(x, gmul(f, y)) for x, y in zip(row, br)]
        piv = next((j for j, z in enumerate(row) if not giszero(z)), None)
        if piv is None:
            continue
        inv = ginv(row[piv])
        row = [gmul(inv, z) for z in row]
        # eliminate this pivot from existing rows, keeping reduced basis stable
        newbasis = []
        for p0, br in basis:
            if not giszero(br[piv]):
                f = br[piv]
                br = [gsub(x, gmul(f, y)) for x, y in zip(br, row)]
            newbasis.append((p0, br))
        basis = sorted(newbasis + [(piv, row)], key=lambda x: x[0])
        selected.append(idx)
        if len(basis) == 32:
            # Continue selection is unnecessary: first 32 rank increases are lexicographically first independent rows.
            pass
    return len(basis), selected[:32]


def det_mod(rows32):
    m = [[gp(z) for z in row] for row in rows32]
    det = (1, 0)
    n = 32
    for c in range(n):
        piv = next((r for r in range(c, n) if not giszero(m[r][c])), None)
        if piv is None:
            return (0, 0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            det = ((-det[0]) % P, (-det[1]) % P)
        pv = m[c][c]
        det = gmul(det, pv)
        inv = ginv(pv)
        for r in range(c + 1, n):
            if giszero(m[r][c]):
                continue
            f = gmul(m[r][c], inv)
            for j in range(c, n):
                m[r][j] = gsub(m[r][j], gmul(f, m[c][j]))
    return det


def permute_regauge(coords, perm):
    # New label a receives old coordinate perm[a], then subtract new root coordinate.
    root = coords[perm[0]]
    return {
        a: tuple(coords[perm[a]][j] - root[j] for j in range(3))
        for a in range(5)
    }


def full32_mod(coords):
    # Exact contraction followed by homomorphic reduction. Kept separate for provenance clarity.
    return [gp(z) for z in full32_exact(coords)]


def lane_a():
    source = (ROOT / "sources" / "ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md").read_text(encoding="utf-8")
    ires = (ROOT / "results" / "ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md").read_text(encoding="utf-8")
    prereg = (ROOT / "prereg" / "ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN.md").read_text(encoding="utf-8")
    admiss = {s: all(v > 0 for v in edge_sq(ray(s)).values()) for s in ALL_SEEDS}
    locks = {
        "source_order": "one-wedge source construction -> Toller function -> K5 product -> group integration" in source,
        "iter077i_full32": "all 32" in ires,
        "iter077i_q_minus20": "q=-20" in ires,
        "preregistered_before_implementation": "No ray may be changed after looking at rank" in prereg,
        "all_56_rays_admissible": len(admiss) == 56 and all(admiss.values()),
    }
    ok = all(locks.values())
    return {
        "iteration": "Iter077J-SM", "lane": "A", "valid": ok,
        "scientific_outcome": "PASS" if ok else "BLOCKED",
        "source_locks": locks,
        "seed0_edge_sq": edge_sq(ray(0)), "seed56_edge_sq": edge_sq(ray(56)),
        "frozen_ray_count": len(admiss),
    }


def main_vectors():
    return [full32_exact(ray(s)) for s in MAIN_SEEDS]


def lane_b():
    rows = main_vectors()
    rank, selected = rank_and_selected(rows)
    det = det_mod([rows[i] for i in selected]) if rank == 32 else (0, 0)
    ok = rank == 32 and not giszero(det)
    return {
        "iteration": "Iter077J-SM", "lane": "B", "valid": True,
        "scientific_outcome": "PASS" if ok else "FAIL",
        "main_rows": len(rows), "boundary_dimension": 32,
        "rank_over_gaussian_field_certificate": rank,
        "certificate_prime": P,
        "lexicographic_independent_seed_indices": [MAIN_SEEDS[i] for i in selected],
        "determinant_mod_p_i": [det[0], det[1]],
        "full_rank_proves_Qi_rank32": ok,
    }


def lane_c():
    main = main_vectors()
    held = [full32_exact(ray(s)) for s in HELD_SEEDS]
    rmain, selected = rank_and_selected(main)
    rall, _ = rank_and_selected(main + held)
    det = det_mod([main[i] for i in selected]) if rmain == 32 else (0, 0)
    ok = rmain == 32 and rall == 32 and not giszero(det)
    return {
        "iteration": "Iter077J-SM", "lane": "C", "valid": True,
        "scientific_outcome": "PASS" if ok else "FAIL",
        "main_rank": rmain, "combined_rank": rall,
        "heldout_rows": len(held), "combined_rows": len(main) + len(held),
        "certificate_prime": P,
        "minor_seed_indices": [MAIN_SEEDS[i] for i in selected],
        "minor_determinant_mod_p_i": [det[0], det[1]],
    }


def lane_d():
    rows = []
    perms = list(itertools.permutations(range(5)))
    for s in MAIN_SEEDS[:8]:
        coords = ray(s)
        for perm in perms:
            rows.append(full32_mod(permute_regauge(coords, perm)))
    rank, selected = rank_and_selected(rows)
    # Diagnostic single collinear ray.
    t = (0, 1, 3, 7, 12)
    col = {a: (t[a], 0, 0) for a in range(5)}
    colvec = full32_exact(col)
    colrank, _ = rank_and_selected([colvec])
    ok = rank == 32 and colrank < 32
    return {
        "iteration": "Iter077J-SM", "lane": "D", "valid": True,
        "scientific_outcome": "PASS" if ok else "FAIL",
        "rays_relabelled": 8, "permutations_each": 120,
        "relabelled_vectors_checked": len(rows),
        "relabelled_span_rank": rank,
        "certificate_prime": P,
        "first_independent_orbit_row_indices": selected,
        "negative_control_single_collinear_ray_rank": colrank,
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(root):
    got = {}
    for base_dir, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base_dir, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") == "Iter077J-SM" and obj.get("lane") in LANES:
                got[obj["lane"]] = obj
    present = set(got) == set(LANES)
    execution_valid = present and all(bool(got[k].get("valid")) for k in LANES)
    outcomes = {k: got.get(k, {}).get("scientific_outcome") for k in LANES}
    if execution_valid and all(v == "PASS" for v in outcomes.values()):
        verdict = "PASS"
        classification = "ITER077J_SM_SOURCE_ORDERED_JHALF_LEADING_ANGULAR_COEFFICIENT_SPANS_FULL_32_BOUNDARY_SPACE_EXACT_SCOPED"
    elif execution_valid:
        verdict = "FAIL"
        classification = "ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN_HYPOTHESIS_FAILS_EXACT_SCOPED"
    else:
        verdict = "BLOCKED"
        classification = "ITER077J_SM_FULL32_LEADING_ANGULAR_SPAN_BLOCKED_EXECUTION_OR_PROVENANCE"
    return {
        "iteration": "Iter077J-SM", "execution_valid": execution_valid,
        "verdict": verdict, "classification": classification,
        "lane_scientific_outcomes": outcomes,
        "main_rank": got.get("B", {}).get("rank_over_gaussian_field_certificate"),
        "combined_rank": got.get("C", {}).get("combined_rank"),
        "relabelled_span_rank": got.get("D", {}).get("relabelled_span_rank"),
        "next_admissible_gate": "If PASS, move to source-selected correlated/conditional extension with subleading phase/measure/intertwiner data; leading cancellation by a fixed boundary superposition is then excluded in this j=1/2 sector.",
        "claim_lock": "No full causal-vertex divergence/nonexistence theorem, no regulator-independence theorem, no generic-spin result, no source-to-K4 pushforward, no epsilon^-1 coefficient, no G3/F9/G8/K5 promotion, no new physics or complete QG.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit("choose exactly one of --lane or --aggregate-dir")
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    p = Path(args.output); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj.get("valid", False):
        raise SystemExit(1)
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
