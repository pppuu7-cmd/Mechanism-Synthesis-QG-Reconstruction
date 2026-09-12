#!/usr/bin/env python3
"""Iter034: K5 cycle-space symmetry isotropization audit.

Question: can full vertex-permutation symmetry remove the leading Schur-shape
ambiguity identified in Iter031-033?  The six-dimensional cycle space of K5 is
constructed directly from the oriented incidence matrix.  Every S5 vertex
permutation induces an orthogonal representation on that cycle space.

For a generic SPD conditional cycle metric S, normalized to det(S)=1, we form
its group average

    S_G = |G|^{-1} sum_g R_g^T S R_g.

If the K5 cycle representation is irreducible over the tested commutant, full
S5 averaging should force S_G proportional to I; det normalization then fixes
it to I.  C5 and D5 subgroup averages are retained as preregistered controls:
they need not isotropize a generic S.

This is a symmetry-mechanism audit, not a derivation that the physical quantum-
gravity measure actually performs such an average.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

N = 5
EDGES = [(i, j) for i in range(N) for j in range(i + 1, N)]
EIDX = {e: k for k, e in enumerate(EDGES)}


def incidence() -> np.ndarray:
    b = np.zeros((N, len(EDGES)))
    for k, (i, j) in enumerate(EDGES):
        b[i, k] = -1.0
        b[j, k] = +1.0
    return b


def cycle_basis() -> np.ndarray:
    # Right nullspace of incidence; K5 rank(B)=4, hence dim cycle=10-4=6.
    _, s, vt = np.linalg.svd(incidence(), full_matrices=True)
    rank = int(np.sum(s > 1e-12))
    q = vt[rank:].T
    assert q.shape == (10, 6)
    assert np.linalg.norm(incidence() @ q) < 1e-12
    assert np.linalg.norm(q.T @ q - np.eye(6)) < 1e-12
    return q


def edge_rep(perm: tuple[int, ...]) -> np.ndarray:
    p = np.zeros((10, 10))
    for col, (i, j) in enumerate(EDGES):
        a, b = perm[i], perm[j]
        sign = 1.0
        if a > b:
            a, b = b, a
            sign = -1.0
        row = EIDX[(a, b)]
        p[row, col] = sign
    return p


def cycle_rep(perm: tuple[int, ...], q: np.ndarray) -> np.ndarray:
    r = q.T @ edge_rep(perm) @ q
    return r


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # p after q
    return tuple(p[q[i]] for i in range(N))


def power(p: tuple[int, ...], k: int) -> tuple[int, ...]:
    out = tuple(range(N))
    for _ in range(k):
        out = compose(p, out)
    return out


def groups() -> dict[str, list[tuple[int, ...]]]:
    s5 = list(itertools.permutations(range(N)))
    c = (1, 2, 3, 4, 0)
    c5 = [power(c, k) for k in range(5)]
    # Reflection i -> -i mod 5.
    f = (0, 4, 3, 2, 1)
    d5 = []
    for k in range(5):
        d5.append(power(c, k))
        d5.append(compose(f, power(c, k)))
    # remove any accidental duplicates while preserving order
    d5 = list(dict.fromkeys(d5))
    return {"C5": c5, "D5": d5, "S5": s5}


def det_normalize(s: np.ndarray) -> np.ndarray:
    sign, logdet = np.linalg.slogdet(s)
    if sign <= 0:
        raise ValueError("metric not SPD")
    return s / math.exp(logdet / s.shape[0])


def random_spd(rng: np.random.Generator, condition: float) -> np.ndarray:
    x = rng.normal(size=(6, 6))
    q, _ = np.linalg.qr(x)
    # log-spaced eigenvalues with shuffled axes; exact condition target.
    lam = np.geomspace(1.0 / math.sqrt(condition), math.sqrt(condition), 6)
    rng.shuffle(lam)
    s = q @ np.diag(lam) @ q.T
    return det_normalize((s + s.T) / 2.0)


def group_average(s: np.ndarray, reps: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(s)
    for r in reps:
        out += r.T @ s @ r
    return (out / len(reps) + (out / len(reps)).T) / 2.0


def rel_anisotropy(s: np.ndarray) -> float:
    ev = np.linalg.eigvalsh(s)
    return float(np.max(ev) / np.min(ev) - 1.0)


def max_commutator(s: np.ndarray, reps: list[np.ndarray]) -> float:
    scale = max(float(np.linalg.norm(s)), 1e-30)
    return float(max(np.linalg.norm(s @ r - r @ s) / scale for r in reps))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    profile = args.profile
    if not (0 <= profile < 32):
        raise SystemExit("profile must be in [0,31]")

    rng = np.random.default_rng(34000 + profile)
    q = cycle_basis()
    gs = groups()
    reps = {name: [cycle_rep(p, q) for p in perms] for name, perms in gs.items()}

    # Representation sanity checks.
    orth_err = max(
        float(np.linalg.norm(r.T @ r - np.eye(6)))
        for rs in reps.values() for r in rs
    )
    conditions = [3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 10000.0]
    condition = conditions[profile % len(conditions)]
    s0 = random_spd(rng, condition)

    metrics = {}
    for name in ("C5", "D5", "S5"):
        sg = group_average(s0, reps[name])
        sgn = det_normalize(sg)
        metrics[name] = {
            "group_order": len(reps[name]),
            "anisotropy_before_detnorm": rel_anisotropy(sg),
            "anisotropy_after_detnorm": rel_anisotropy(sgn),
            "identity_residual_after_detnorm": float(np.linalg.norm(sgn - np.eye(6)) / np.linalg.norm(np.eye(6))),
            "max_commutator": max_commutator(sg, reps[name]),
            "eigenvalues_after_detnorm": [float(x) for x in np.linalg.eigvalsh(sgn)],
        }

    # Genericity control: initial metric must actually be anisotropic.
    initial_anisotropy = rel_anisotropy(s0)
    full = metrics["S5"]
    c5 = metrics["C5"]
    d5 = metrics["D5"]

    gates = {
        "cycle_dimension_is_6": q.shape[1] == 6,
        "representation_orthogonal": orth_err < 2e-12,
        "generic_input_anisotropic": initial_anisotropy > 0.5,
        "s5_average_invariant": full["max_commutator"] < 2e-12,
        "s5_detnorm_is_identity": full["identity_residual_after_detnorm"] < 2e-12,
        "s5_anisotropy_collapses": full["anisotropy_after_detnorm"] < 2e-12,
        # Controls should usually retain shape freedom. We require at least one
        # proper subgroup to retain visible anisotropy for each random profile.
        "proper_subgroup_retains_shape": max(c5["anisotropy_after_detnorm"], d5["anisotropy_after_detnorm"]) > 1e-4,
    }
    passed = all(gates.values())

    result = {
        "iteration": "Iter034",
        "audit": "K5 cycle symmetry isotropization",
        "profile": profile,
        "seed": 34000 + profile,
        "condition_target": condition,
        "initial_anisotropy": initial_anisotropy,
        "orthogonality_error": orth_err,
        "metrics": metrics,
        "gates": gates,
        "pass": passed,
        "interpretation_if_pass": (
            "Full S5 vertex-permutation symmetry collapses a generic determinant-normalized "
            "K5 conditional cycle metric to the identity, while proper-subgroup controls retain "
            "shape freedom. Thus exact full K5 symmetry is a concrete candidate mechanism for "
            "removing leading Schur-shape ambiguity up to volume normalization."
        ),
        "claim_lock": (
            "This is a finite-dimensional K5 representation-theory mechanism audit. It does not "
            "show that a microscopic spin-foam/QG amplitude enforces or dynamically averages over S5."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
