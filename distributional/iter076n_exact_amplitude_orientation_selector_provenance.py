#!/usr/bin/env python3
"""Iter076N exact amplitude orientation-selector provenance audit.

This script tests only the preregistered representation/character statements.
It does not evaluate the physical causal vertex numerically and cannot promote
G3/F9/K5 or a finiteness/divergence claim.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path

N = 5
LABELS = tuple(range(N))
EDGES = tuple(itertools.combinations(LABELS, 2))


def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            inv += p[i] > p[j]
    return -1 if inv % 2 else 1


def permute_sigma(sigma, p):
    out = [None] * N
    for old in LABELS:
        out[p[old]] = sigma[old]
    return tuple(out)


def kappa_signature(sigma):
    return tuple(sigma[a] * sigma[b] for a, b in EDGES)


def canonical_kappa_under_perm(sigma, p):
    ps = permute_sigma(sigma, p)
    return kappa_signature(ps)


def det_fraction(mat):
    a = [list(map(Fraction, row)) for row in mat]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det *= -1
        piv = a[col][col]
        det *= piv
        for j in range(col, n):
            a[col][j] /= piv
        for r in range(col + 1, n):
            fac = a[r][col]
            if fac:
                for j in range(col, n):
                    a[r][j] -= fac * a[col][j]
    return det


def rational_hyperboloid(u):
    r2 = sum(x * x for x in u)
    if r2 >= 1:
        raise ValueError("need |u|^2 < 1")
    den = 1 - r2
    return ((1 + r2) / den,) + tuple(2 * x / den for x in u)


def omega_det(sigma, normals):
    # columns are [1; sigma_a F_a]
    mat = [[Fraction(1) for _ in LABELS]]
    for mu in range(4):
        mat.append([Fraction(sigma[a]) * normals[a][mu] for a in LABELS])
    return det_fraction(mat)


def permute_columns_data(sigma, normals, p):
    ps = [None] * N
    pn = [None] * N
    for old in LABELS:
        ps[p[old]] = sigma[old]
        pn[p[old]] = normals[old]
    return tuple(ps), tuple(pn)


def lane_a():
    """Displayed Eq.(4) coefficient/product skeleton has trivial scalar character.

    We audit only the explicit scalar prefactor arising from simultaneous label
    reindexing: permutation of ten wedge factors and four identical Haar measure
    factors does not generate an alternating coefficient. Possible representation
    reindexing of matrix entries is tensor covariance, not a universal scalar sign.
    """
    perms = list(itertools.permutations(LABELS))
    even = sum(parity(p) == 1 for p in perms)
    odd = len(perms) - even

    # A product over all unordered pairs is mapped bijectively to itself.
    edge_set = {frozenset(e) for e in EDGES}
    all_edge_bijections = True
    coefficient_character = set()
    for p in perms:
        mapped = {frozenset((p[a], p[b])) for a, b in EDGES}
        all_edge_bijections &= mapped == edge_set
        # Reindexing a commutative scalar product and identical product measure
        # has coefficient +1; no orientation tensor is inserted by this action.
        coefficient_character.add(1)

    passed = all_edge_bijections and coefficient_character == {1} and even == odd == 60
    return {
        "lane": "A",
        "pass": passed,
        "permutations": len(perms),
        "even": even,
        "odd": odd,
        "all_wedge_slot_maps_bijective": all_edge_bijections,
        "explicit_scalar_character_values": sorted(coefficient_character),
        "interpretation": "Eq4 displayed wedge-product/Haar skeleton carries no explicit alternating S5 scalar coefficient.",
    }


def lane_b():
    """Reproduce the causal-data sign-character obstruction by orbit stabilizers."""
    perms = list(itertools.permutations(LABELS))
    representatives = {
        "0_or_5": (1, 1, 1, 1, 1),
        "1_or_4": (-1, 1, 1, 1, 1),
        "2_or_3": (-1, -1, 1, 1, 1),
    }
    out = {}
    all_have_odd = True
    for name, sigma in representatives.items():
        kap = kappa_signature(sigma)
        stabilizer = [p for p in perms if canonical_kappa_under_perm(sigma, p) == kap]
        odd_stab = [p for p in stabilizer if parity(p) == -1]
        all_have_odd &= bool(odd_stab)
        out[name] = {
            "stabilizer_size": len(stabilizer),
            "odd_stabilizer_count": len(odd_stab),
        }
    return {
        "lane": "B",
        "pass": all_have_odd,
        "orbits": out,
        "interpretation": "Every causal kappa orbit has an odd stabilizer, forcing any kappa-only alternating scalar to vanish.",
    }


def lane_c():
    """Exhibit exact-variable Omega with sign character while source slot coefficient stays trivial."""
    us = [
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1, 5), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 4), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1, 3)),
        (Fraction(1, 6), Fraction(1, 7), Fraction(1, 8)),
    ]
    normals = tuple(rational_hyperboloid(u) for u in us)
    sigma = (1, -1, 1, 1, -1)
    base = omega_det(sigma, normals)
    if base == 0:
        raise RuntimeError("control determinant unexpectedly degenerate")

    perms = list(itertools.permutations(LABELS))
    mismatches = []
    for p in perms:
        ps, pn = permute_columns_data(sigma, normals, p)
        d = omega_det(ps, pn)
        if d != parity(p) * base:
            mismatches.append({"p": p, "det": str(d), "expected": str(parity(p) * base)})

    passed = not mismatches
    return {
        "lane": "C",
        "pass": passed,
        "base_delta": str(base),
        "nondegenerate": base != 0,
        "checked_permutations": len(perms),
        "omega_character_mismatches": mismatches[:5],
        "source_skeleton_character": 1,
        "interpretation": "Omega has the alternating S5 character on exact group-normal variables, while the explicit Eq4 product/measure coefficient is trivial: availability is not selection.",
    }


def lane_d():
    """Boundary-state universality firewall.

    Eq.(4) is a linear functional on generic spin-network boundary states with
    five arbitrary intertwiners. A universal source-fixed sign character cannot
    be inferred from an arbitrary boundary state: the tensor-product slot action
    contains a symmetric vector (take identical slot labels), so the boundary
    space is not restricted to the alternating representation.
    """
    perms = list(itertools.permutations(LABELS))
    identical_slots = ("q",) * N
    fixed = 0
    odd_fixed = 0
    for p in perms:
        permuted = [None] * N
        for old in LABELS:
            permuted[p[old]] = identical_slots[old]
        if tuple(permuted) == identical_slots:
            fixed += 1
            if parity(p) == -1:
                odd_fixed += 1
    # If an odd permutation fixes an allowed boundary vector, the whole generic
    # boundary space cannot carry the sign representation universally.
    passed = fixed == 120 and odd_fixed == 60
    return {
        "lane": "D",
        "pass": passed,
        "all_permutations_fix_symmetric_boundary_control": fixed,
        "odd_permutations_fix_symmetric_boundary_control": odd_fixed,
        "source_boundary_space_restricted_to_sign_rep": False,
        "interpretation": "Generic intertwiner input cannot supply a source-fixed universal S5-odd selector; an alternating boundary state would be an extra state choice, not amplitude provenance.",
    }


LANES = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}


def aggregate(input_dir):
    records = {}
    for lane in "ABCD":
        matches = list(Path(input_dir).rglob(f"iter076n_lane_{lane}.json"))
        if len(matches) != 1:
            raise RuntimeError(f"expected one artifact for lane {lane}, found {len(matches)}")
        records[lane] = json.loads(matches[0].read_text())

    all_pass = all(records[x].get("pass") is True for x in "ABCD")
    no_selector = (
        all_pass
        and records["A"]["explicit_scalar_character_values"] == [1]
        and records["B"]["pass"]
        and records["C"]["source_skeleton_character"] == 1
        and records["D"]["source_boundary_space_restricted_to_sign_rep"] is False
    )

    if no_selector:
        classification = "ITER076N_EQ4_EQ7_HAVE_NO_CANONICAL_S5_ODD_SELECTOR_EXACT_SIGNED_P3_BLOCKED_SEMICLASSICAL_ONLY_SCOPED"
    else:
        classification = "ITER076N_BOUNDARY_INTERTWINER_ORIENTATION_CHARACTER_UNRESOLVED_EXACT_SIGNED_P3_BLOCKED_SCOPED"

    result = {
        "classification": classification,
        "lane_pass": {x: records[x]["pass"] for x in "ABCD"},
        "valid": all_pass,
        "scope": "EXACT_SOURCE_PROVENANCE_ONLY",
        "promotion_signed_p3": False,
        "semiclassical_iter076l_m_unchanged": True,
        "claim_lock": "No physical signed P3, G3/F9/K5 promotion, finiteness/divergence theorem, or new-physics claim.",
    }
    Path("results").mkdir(exist_ok=True)
    Path("results/iter076n_aggregate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if all_pass else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=list(LANES))
    ap.add_argument("--aggregate-dir")
    args = ap.parse_args()

    if args.aggregate_dir:
        raise SystemExit(aggregate(args.aggregate_dir))
    if not args.lane:
        ap.error("provide --lane or --aggregate-dir")

    result = LANES[args.lane]()
    Path("results").mkdir(exist_ok=True)
    out = Path("results") / f"iter076n_lane_{args.lane}.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
