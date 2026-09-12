#!/usr/bin/env python3
"""Iter035: K5 symmetry-breaking response audit.

Iter034 established that an exactly uniform S5 average isotropizes the six-
dimensional K5 cycle metric. Iter035 asks whether that mechanism is robust and
quantifies how shape ambiguity re-enters when the averaging measure weakly
selects one microscopic vertex.

For a generic determinant-normalized SPD cycle metric S, define

    S(eps) = sum_g w_eps(g) R_g^T S R_g / sum_g w_eps(g),
    w_eps(g) = exp(eps * 1[g(0)=0]).

At eps=0 the measure is uniform on S5 and S(eps) is isotropic. For eps>0 the
measure preserves only the stabilizer H = {g in S5 : g(0)=0} ~= S4. We test:
(1) exact recovery of isotropy at eps=0; (2) H-invariance for all eps; (3) a
linear small-eps response of determinant-normalized anisotropy; and (4) visible
return of shape freedom at finite eps.

This is a finite K5 mechanism-stability audit, not a derivation that a physical
QG amplitude has this weighting law.
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
        b[j, k] = 1.0
    return b


def cycle_basis() -> np.ndarray:
    _, s, vt = np.linalg.svd(incidence(), full_matrices=True)
    rank = int(np.sum(s > 1e-12))
    q = vt[rank:].T
    assert q.shape == (10, 6)
    return q


def edge_rep(perm: tuple[int, ...]) -> np.ndarray:
    p = np.zeros((10, 10))
    for col, (i, j) in enumerate(EDGES):
        a, b = perm[i], perm[j]
        sign = 1.0
        if a > b:
            a, b = b, a
            sign = -1.0
        p[EIDX[(a, b)], col] = sign
    return p


def cycle_rep(perm: tuple[int, ...], q: np.ndarray) -> np.ndarray:
    return q.T @ edge_rep(perm) @ q


def det_normalize(s: np.ndarray) -> np.ndarray:
    sign, logdet = np.linalg.slogdet(s)
    if sign <= 0:
        raise ValueError("metric not SPD")
    return s / math.exp(logdet / s.shape[0])


def random_spd(rng: np.random.Generator, condition: float) -> np.ndarray:
    x = rng.normal(size=(6, 6))
    q, _ = np.linalg.qr(x)
    lam = np.geomspace(1.0 / math.sqrt(condition), math.sqrt(condition), 6)
    rng.shuffle(lam)
    s = q @ np.diag(lam) @ q.T
    return det_normalize((s + s.T) / 2.0)


def anisotropy(s: np.ndarray) -> float:
    ev = np.linalg.eigvalsh(s)
    return float(np.max(ev) / np.min(ev) - 1.0)


def weighted_average(s: np.ndarray, perms, reps, eps: float) -> np.ndarray:
    out = np.zeros_like(s)
    z = 0.0
    for p, r in zip(perms, reps):
        w = math.exp(eps if p[0] == 0 else 0.0)
        out += w * (r.T @ s @ r)
        z += w
    out /= z
    return (out + out.T) / 2.0


def max_commutator(s: np.ndarray, reps: list[np.ndarray]) -> float:
    scale = max(float(np.linalg.norm(s)), 1e-30)
    return float(max(np.linalg.norm(s @ r - r @ s) / scale for r in reps))


def fit_log_slope(xs: np.ndarray, ys: np.ndarray) -> tuple[float, float]:
    lx = np.log(xs)
    ly = np.log(ys)
    a, b = np.polyfit(lx, ly, 1)
    pred = a * lx + b
    ss_res = float(np.sum((ly - pred) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    r2 = 1.0 - ss_res / max(ss_tot, 1e-30)
    return float(a), float(r2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if not (0 <= args.profile < 32):
        raise SystemExit("profile must be in [0,31]")

    rng = np.random.default_rng(35000 + args.profile)
    q = cycle_basis()
    perms = list(itertools.permutations(range(N)))
    reps = [cycle_rep(p, q) for p in perms]
    h_reps = [r for p, r in zip(perms, reps) if p[0] == 0]
    orth_err = max(float(np.linalg.norm(r.T @ r - np.eye(6))) for r in reps)

    conditions = [3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 10000.0]
    condition = conditions[args.profile % len(conditions)]
    s0 = random_spd(rng, condition)

    eps_grid = np.array([0.0, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 2.0])
    rows = []
    for eps in eps_grid:
        raw = weighted_average(s0, perms, reps, float(eps))
        sn = det_normalize(raw)
        rows.append({
            "epsilon": float(eps),
            "anisotropy": anisotropy(sn),
            "identity_residual": float(np.linalg.norm(sn - np.eye(6)) / np.linalg.norm(np.eye(6))),
            "stabilizer_commutator": max_commutator(raw, h_reps),
            "eigenvalues": [float(x) for x in np.linalg.eigvalsh(sn)],
        })

    small = [r for r in rows if 1e-5 <= r["epsilon"] <= 1e-2]
    x = np.array([r["epsilon"] for r in small])
    y = np.array([r["anisotropy"] for r in small])
    slope, r2 = fit_log_slope(x, y)
    base = rows[0]
    finite = next(r for r in rows if r["epsilon"] == 1.0)
    strong = rows[-1]

    gates = {
        "cycle_dimension_is_6": q.shape[1] == 6,
        "representation_orthogonal": orth_err < 2e-12,
        "uniform_limit_isotropic": base["identity_residual"] < 2e-12 and base["anisotropy"] < 2e-12,
        "residual_S4_invariance": max(r["stabilizer_commutator"] for r in rows) < 3e-12,
        "small_breaking_response_positive": min(y) > 1e-12,
        "small_breaking_is_linear": 0.80 <= slope <= 1.20 and r2 >= 0.995,
        "finite_breaking_restores_shape": finite["anisotropy"] > 1e-4,
        "strong_breaking_not_less_than_finite": strong["anisotropy"] >= 0.95 * finite["anisotropy"],
    }
    # NumPy comparisons can return np.bool_, which the stdlib JSON encoder does
    # not serialize. Normalize gate values without changing any preregistered
    # criterion or threshold.
    gates = {name: bool(value) for name, value in gates.items()}
    passed = all(gates.values())
    result = {
        "iteration": "Iter035",
        "audit": "K5 symmetry-breaking response",
        "profile": args.profile,
        "seed": 35000 + args.profile,
        "condition_target": condition,
        "stabilizer_order": len(h_reps),
        "orthogonality_error": orth_err,
        "small_epsilon_loglog_slope": slope,
        "small_epsilon_loglog_r2": r2,
        "rows": rows,
        "gates": gates,
        "pass": passed,
        "interpretation_if_pass": (
            "Exact S5 isotropization is stable in the symmetric limit but generic vertex-selecting "
            "symmetry breaking reintroduces cycle-metric shape at first order in the breaking strength, "
            "while preserving the expected S4 stabilizer. Thus the Iter034 ambiguity-removal mechanism "
            "is quantitatively symmetry-protected rather than automatically robust to microscopic bias."
        ),
        "claim_lock": (
            "The epsilon weighting is a controlled K5 surrogate for explicit microscopic symmetry breaking. "
            "It does not establish the symmetry content or breaking pattern of a physical spin-foam/QG measure."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
