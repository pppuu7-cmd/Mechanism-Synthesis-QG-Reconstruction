#!/usr/bin/env python3
"""Iter078M-RG: exact fixed-causal stabilizer restricted Jacobian gate.

Prospectively preregistered in
prereg/ITER078M_RG_CAUSAL_STABILIZER_RESTRICTED_JACOBIAN.md.
All arithmetic is exact over Q.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


h = load("iter078h", ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py")
stab = load("iter078e_stab", ROOT / "distributional" / "iter078e_critic_boundary_stabilizer.py")

N = 32


def as_q_matrix(a):
    return [[Fraction(x) for x in row] for row in a]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(a, b):
    if not a or not b:
        return []
    nr, nk, nc = len(a), len(b), len(b[0])
    assert len(a[0]) == nk
    return [[sum(a[i][k] * b[k][j] for k in range(nk)) for j in range(nc)] for i in range(nr)]


def matvec(a, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def stack(*mats):
    out = []
    for m in mats:
        out.extend([row[:] for row in m])
    return out


def rref(a):
    a = as_q_matrix(a)
    if not a:
        return a, []
    nr, nc = len(a), len(a[0])
    pivots = []
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if a[i][c] != 0), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(nr):
            if i == r or a[i][c] == 0:
                continue
            q = a[i][c]
            a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return a, pivots


def rank_q(a):
    return len(rref(a)[1]) if a else 0


def nullspace_basis(a, ncols=None):
    if not a:
        if ncols is None:
            raise ValueError("ncols required for empty constraint matrix")
        return [[Fraction(int(i == j)) for i in range(ncols)] for j in range(ncols)]
    rr, pivots = rref(a)
    nc = len(a[0])
    free = [c for c in range(nc) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0) for _ in range(nc)]
        v[f] = Fraction(1)
        for row, pc in enumerate(pivots):
            v[pc] = -rr[row][f]
        basis.append(v)
    return basis


def columns(vectors):
    if not vectors:
        return [[] for _ in range(N)]
    return [[vectors[j][i] for j in range(len(vectors))] for i in range(len(vectors[0]))]


def diff(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def is_zero_matrix(a):
    return all(x == 0 for row in a for x in row)


def analyze(p_count: int, mode: str):
    gens = stab.stabilizer_generators(p_count)
    eye = identity(N)
    actions = [as_q_matrix(stab.global_action(g)) for g in gens]
    constraints = []
    for p in actions:
        constraints.extend(diff(p, eye))

    inv_basis = nullspace_basis(constraints, ncols=N)
    inv_dim = len(inv_basis)
    V = columns(inv_basis)  # 32 x inv_dim

    invariant_basis_ok = all(matvec(p, v) == v for p in actions for v in inv_basis)
    constraint_rank = rank_q(constraints) if constraints else 0
    invariant_dimension_crosscheck = inv_dim == N - constraint_rank

    L = [Fraction(x) for x in h.compact_tensor()]
    l_invariant = all(matvec(p, L) == L for p in actions)

    J = as_q_matrix(h.jacobian_at(h.compact_tensor(), mode))
    full_rank = rank_q(J)
    full_nullity = N - full_rank

    restricted = matmul(J, V) if inv_dim else [[] for _ in range(N)]
    restricted_rank = rank_q(restricted) if inv_dim else 0
    restricted_nullity = inv_dim - restricted_rank

    direct_stack = stack(J, constraints)
    direct_intersection_dimension = N - rank_q(direct_stack)
    nullity_crosscheck = restricted_nullity == direct_intersection_dimension

    equivariance = all(matmul(J, p) == matmul(p, J) for p in actions)

    valid = (
        full_rank == 31
        and full_nullity == 1
        and invariant_basis_ok
        and invariant_dimension_crosscheck
        and nullity_crosscheck
        and l_invariant
        and equivariance
    )

    return {
        "iteration": "Iter078M-RG",
        "p_count": p_count,
        "measure": mode,
        "stabilizer": f"S_{p_count} x S_{5-p_count}",
        "generator_count": len(gens),
        "invariant_dimension": inv_dim,
        "stacked_constraint_rank": constraint_rank,
        "invariant_basis_verified": invariant_basis_ok,
        "invariant_dimension_crosscheck": invariant_dimension_crosscheck,
        "compact_tensor_L_invariant": l_invariant,
        "jacobian_equivariant": equivariance,
        "full_rank": full_rank,
        "full_nullity": full_nullity,
        "restricted_rank": restricted_rank,
        "restricted_nullity": restricted_nullity,
        "direct_kernel_intersection_dimension": direct_intersection_dimension,
        "restricted_vs_direct_nullity_crosscheck": nullity_crosscheck,
        "valid": valid,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, choices=range(6), required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    rows = [analyze(args.p, mode) for mode in ("eprl", "unit")]
    execution_valid = all(r["valid"] for r in rows)
    any_retained = any(r["restricted_nullity"] > 0 for r in rows)
    if not execution_valid:
        classification = "ITER078M_RG_INVALID_OR_SYMMETRY_INTERTWINING_NOT_ESTABLISHED"
    elif any_retained:
        classification = "ITER078M_RG_FIXED_CAUSAL_STABILIZER_RESTRICTION_RETAINS_LINEARIZED_NULL_SOME_CLASS_EXACT_CONTROL_SCOPED"
    else:
        classification = "ITER078M_RG_P_CLASS_RESTRICTED_INJECTIVE_EXACT_CONTROL_SCOPED"

    out = {
        "iteration": "Iter078M-RG",
        "p_count": args.p,
        "execution_valid": execution_valid,
        "classification": classification,
        "measures": rows,
        "interpretation_ceiling": (
            "Fixed all-j=1/2 pure order-zero tensor-network control only; no physical causal-Toller refinement, "
            "unique extension, generic-spin injectivity, RG fixed point, regulator independence, G3/F9/G8, continuum, or complete-QG claim."
        ),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not execution_valid:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
