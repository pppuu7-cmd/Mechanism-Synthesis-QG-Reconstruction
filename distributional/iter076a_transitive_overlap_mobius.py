#!/usr/bin/env python3
"""Iter076A: exact intersection-poset/Mobius bookkeeping for transitive K4 faces.

Scientific scope is frozen in status/ITERATION_076A_PREREG.md. This constructs
only the combinatorial overlap object; it does not choose a finite-part or
counterterm prescription and does not evaluate an epsilon^-1 coefficient.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path

from distributional.iter073d_transitive_face_cones import records_for, TRANS, TREES

TOP = frozenset(range(6))
NEG = "++-+"


def support_closure(faces):
    nodes = {frozenset(f) for f in faces}
    nodes.add(TOP)
    changed = True
    while changed:
        changed = False
        cur = list(nodes)
        for a, b in itertools.combinations(cur, 2):
            c = a & b
            if c and c not in nodes:
                nodes.add(c)
                changed = True
    return frozenset(nodes)


def mobius(nodes):
    ns = sorted(nodes, key=lambda s: (len(s), tuple(sorted(s))))
    mu = {}
    for a in ns:
        mu[(a, a)] = 1
        supers = [b for b in ns if a < b]
        supers.sort(key=lambda s: (len(s), tuple(sorted(s))))
        for b in supers:
            subtotal = 0
            for z in ns:
                if a <= z < b:
                    subtotal += mu[(a, z)]
            mu[(a, b)] = -subtotal
    return mu


def verify_mobius(nodes, mu):
    for a in nodes:
        for b in nodes:
            if not a <= b:
                continue
            s = sum(mu[(a, z)] for z in nodes if a <= z <= b)
            if s != (1 if a == b else 0):
                return False
    return True


def mask(s):
    return sum(1 << i for i in s)


def permute_support(s, p):
    return frozenset(p[i] for i in s)


def canonical_family_signature(nodes):
    # Small exact canonicalization under all 6! edge relabellings. Equality of
    # these signatures implies support-poset isomorphism without attaching any
    # physical meaning to the larger S6 relabelling set.
    best = None
    for p in itertools.permutations(range(6)):
        sig = tuple(sorted(mask(permute_support(s, p)) for s in nodes))
        if best is None or sig < best:
            best = sig
    return best


def node_profiles(nodes, mu):
    out = []
    for a in nodes:
        lower = sum(1 for z in nodes if z < a)
        upper = sum(1 for z in nodes if a < z)
        out.append((len(a), lower, upper, mu[(a, TOP)] if a <= TOP else 0))
    return tuple(sorted(out))


def audit_basis(label, tree):
    rows = records_for(label, tree)
    faces = [frozenset(r["S"]) for r in rows]
    hist = Counter((r["m"], r["nu"]) for r in rows)
    nodes = support_closure(faces)
    mu = mobius(nodes)
    top_coeffs = tuple(sorted((len(a), mu[(a, TOP)]) for a in nodes))
    comparable_chains = {
        tuple(sorted(f)): sum(1 for z in nodes if f <= z <= TOP)
        for f in faces
    }
    return {
        "face_count": len(faces),
        "face_histogram": sorted((list(k), v) for k, v in hist.items()),
        "faces": sorted([sorted(f) for f in faces]),
        "closure_supports": sorted([sorted(s) for s in nodes], key=lambda x: (len(x), x)),
        "closure_size": len(nodes),
        "closure_cardinality_histogram": sorted(Counter(len(s) for s in nodes).items()),
        "mobius_top": [[sorted(a), mu[(a, TOP)]] for a in sorted(nodes, key=lambda s: (len(s), tuple(sorted(s))))],
        "mobius_top_histogram": sorted(Counter(v for (a, b), v in mu.items() if b == TOP).items()),
        "top_coeffs_by_size": list(top_coeffs),
        "mobius_identity_ok": verify_mobius(nodes, mu),
        "canonical_family_signature": list(canonical_family_signature(nodes)),
        "node_profiles": [list(x) for x in node_profiles(nodes, mu)],
        "face_chain_counts": [[list(k), v] for k, v in sorted(comparable_chains.items())],
        "all_faces_in_closure": all(f in nodes for f in faces),
        "all_faces_chain_to_top": all(v >= 2 for v in comparable_chains.values()),
    }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    expected_hist = Counter({(3, 1): 2, (4, 1): 1, (5, 2): 3})
    source = {}
    p1 = p2 = p3 = p4 = p5 = p6 = True
    class_refs = []

    for label in TRANS:
        basis = {}
        ref = None
        for tree in TREES:
            rec = audit_basis(label, tree)
            basis[tree] = rec
            got_hist = Counter({tuple(k): v for k, v in rec["face_histogram"]})
            p1 &= rec["face_count"] == 6 and got_hist == expected_hist
            p2 &= rec["closure_size"] == len(set(rec["canonical_family_signature"]))
            p3 &= rec["mobius_identity_ok"]
            p6 &= rec["all_faces_in_closure"] and rec["all_faces_chain_to_top"]
            basis_key = (
                tuple(rec["canonical_family_signature"]),
                tuple(tuple(x) for x in rec["top_coeffs_by_size"]),
                tuple(tuple(x) for x in rec["node_profiles"]),
                tuple(tuple(x) for x in rec["closure_cardinality_histogram"]),
            )
            if ref is None:
                ref = basis_key
            else:
                p4 &= basis_key == ref
        class_refs.append(ref)
        source[label] = basis

    p5 &= all(r == class_refs[0] for r in class_refs)
    neg_counts = {tree: len(records_for(NEG, tree)) for tree in TREES}
    p7 = all(v == 0 for v in neg_counts.values())

    ok = bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out = {
        "iteration": "Iter076A",
        "predicates": {
            "P1_ITER073D_SIX_FACE_HISTOGRAM_RECOVERED": bool(p1),
            "P2_FINITE_DUPLICATE_FREE_INTERSECTION_POSET": bool(p2),
            "P3_EXACT_MOBIUS_INCIDENCE_IDENTITY": bool(p3),
            "P4_BASIS_INVARIANT_POSET_AND_TOP_COEFFICIENTS": bool(p4),
            "P5_TRANSITIVE_ORBIT_POSET_SIGNATURE_EQUAL": bool(p5),
            "P6_EVERY_ORIGINAL_FACE_IN_CLOSURE_AND_CHAIN_TO_TOP": bool(p6),
            "P7_NONTRANSITIVE_NEGATIVE_CONTROL_EMPTY": bool(p7),
        },
        "negative_control_face_counts": neg_counts,
        "classification": (
            "ITER076A_TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_EXACT_SCOPED"
            if ok else
            "ITER076A_TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_OBSTRUCTED_SCOPED"
        ),
        "source": source,
        "claim_lock": (
            "Exact overlap-poset/Mobius bookkeeping only; no finite-part prescription, "
            "epsilon^-1 coefficient, causal-vertex theorem, K5/G3/F9/G8 promotion, complete QG or new physics."
        ),
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(json.dumps({k: v for k, v in out.items() if k != "source"}, indent=2, sort_keys=True))
    if not ok:
        raise SystemExit(9)


if __name__ == "__main__":
    main()
