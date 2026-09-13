#!/usr/bin/env python3
"""Independent adversarial control for Iter078E-RG.

This is a retrospective deterministic reviewer control, not a competing
prospective scientific gate.  It computes the exact action of vertex-label
permutations on the frozen all-j=1/2 five-node boundary basis used by
Iter077I/J/N and the dimension of the subspace invariant under the stabilizer
S_p x S_(5-p) of a causal sign pattern with p nodes of one sign.

All arithmetic is exact over Q.  No scientific threshold is encoded in CI.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

STATES4 = list(itertools.product((0, 1), repeat=4))
KS = list(itertools.product((0, 1), repeat=5))
KINDEX = {k: i for i, k in enumerate(KS)}
NEIGHBORS = {a: [b for b in range(5) if b != a] for a in range(5)}

NODE_OPTIONS = {
    0: [
        ((0, 1, 0, 1), +1),
        ((0, 1, 1, 0), -1),
        ((1, 0, 0, 1), -1),
        ((1, 0, 1, 0), +1),
    ],
    1: [
        ((0, 0, 1, 1), +2),
        ((0, 1, 0, 1), -1),
        ((0, 1, 1, 0), -1),
        ((1, 0, 0, 1), -1),
        ((1, 0, 1, 0), -1),
        ((1, 1, 0, 0), +2),
    ],
}

BVEC = {
    k: [Fraction(dict(NODE_OPTIONS[k]).get(s, 0)) for s in STATES4]
    for k in (0, 1)
}
BNORM = {
    k: sum(x * x for x in BVEC[k])
    for k in (0, 1)
}
assert sum(BVEC[0][i] * BVEC[1][i] for i in range(16)) == 0


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def local_action(old_node: int, perm: tuple[int, ...]):
    """2x2 exact matrix: old intertwiner basis -> relabelled canonical basis."""
    new_node = perm[old_node]
    old_neigh = NEIGHBORS[old_node]
    new_neigh = NEIGHBORS[new_node]
    mat = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for old_k in (0, 1):
        old = dict(NODE_OPTIONS[old_k])
        transformed = []
        for bits_new in STATES4:
            bits_old = tuple(bits_new[new_neigh.index(perm[b])] for b in old_neigh)
            transformed.append(Fraction(old.get(bits_old, 0)))
        for new_k in (0, 1):
            mat[new_k][old_k] = dot(BVEC[new_k], transformed) / BNORM[new_k]
        reconstructed = [
            sum(mat[new_k][old_k] * BVEC[new_k][i] for new_k in (0, 1))
            for i in range(16)
        ]
        assert reconstructed == transformed
    return mat


def global_action(perm: tuple[int, ...]):
    """32x32 exact boundary-basis action for old-label -> new-label permutation."""
    local = [local_action(a, perm) for a in range(5)]
    out = [[Fraction(0) for _ in range(32)] for _ in range(32)]
    for old_ks in KS:
        col = KINDEX[old_ks]
        for local_new_ks in KS:
            coeff = Fraction(1)
            new_ks = [None] * 5
            for a in range(5):
                coeff *= local[a][local_new_ks[a]][old_ks[a]]
                new_ks[perm[a]] = local_new_ks[a]
            if coeff:
                out[KINDEX[tuple(new_ks)]][col] += coeff
    return out


def matmul(a, b):
    n, m, q = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(m)) for j in range(q)] for i in range(n)]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def rank_q(rows):
    a = [row[:] for row in rows]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if a[i][c] != 0), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = Fraction(1, 1) / a[r][c]
        a[r] = [x * inv for x in a[r]]
        for i in range(nr):
            if i == r or a[i][c] == 0:
                continue
            f = a[i][c]
            a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == nr:
            break
    return r


def transposition(i, j):
    p = list(range(5))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def stabilizer_generators(p_count: int):
    plus = list(range(p_count))
    minus = list(range(p_count, 5))
    gens = []
    for group in (plus, minus):
        for i in range(len(group) - 1):
            gens.append(transposition(group[i], group[i + 1]))
    return gens


def analyze(p_count: int):
    gens = stabilizer_generators(p_count)
    eye = identity(32)
    constraints = []
    gen_rows = []
    for perm in gens:
        m = global_action(perm)
        assert matmul(m, m) == eye  # adjacent transpositions square to identity
        diff = [[m[i][j] - eye[i][j] for j in range(32)] for i in range(32)]
        rr = rank_q(diff)
        constraints.extend(diff)
        gen_rows.append({
            "permutation_old_to_new": list(perm),
            "rank_P_minus_I": rr,
            "single_generator_invariant_dimension": 32 - rr,
        })
    rank_constraints = rank_q(constraints)
    inv_dim = 32 - rank_constraints
    return {
        "p_count": p_count,
        "causal_stabilizer": f"S_{p_count} x S_{5-p_count}",
        "boundary_dimension": 32,
        "generator_count": len(gens),
        "generators": gen_rows,
        "stacked_constraint_rank": rank_constraints,
        "stabilizer_invariant_dimension": inv_dim,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, choices=range(6))
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.p is None:
        result = {"classes": [analyze(p) for p in range(6)]}
    else:
        result = analyze(args.p)
    result["status"] = "RETROSPECTIVE_ADVERSARIAL_REPRODUCTION_CONTROL"
    result["scientific_note"] = (
        "CI success certifies only exact execution. Scientific interpretation is made in the critic review."
    )
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
