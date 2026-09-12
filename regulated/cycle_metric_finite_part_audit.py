#!/usr/bin/env python3
"""Iter031 — cycle-metric finite-part universality audit.

Purpose
-------
Iter030 showed that the eta^-q ambient divergence disappears when the joint
Gaussian object is treated as a density on its natural rank-r cut-space.
Iter031 asks a sharper question: after minimally removing eta^-q from an
ambient correlated regulator, is the remaining finite normalization unique?

For an m-edge complete graph with rank r and q=m-r, choose orthonormal bases
U_cut and U_cycle. Define

    Sigma_eta = U_cut A U_cut^T + eta^2 U_cycle K U_cycle^T,

with A,K positive definite. Then exactly

    rho_ambient(0) = rho_cut(0) * (2 pi)^(-q/2)
                     * eta^(-q) * det(K)^(-1/2).

Thus eta^q rho_ambient/rho_cut is universal only if the cycle-volume
normalization det(K) is fixed. A determinant-normalized cycle metric K0 with
det(K0)=1 should restore the universal factor (2 pi)^(-q/2).

This is a structural linearized audit, not a derivation of the physical
causal EPRL/Toller prescription.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def complete_edges(n: int):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def reduced_incidence(n: int, edge_signs: np.ndarray) -> np.ndarray:
    edges = complete_edges(n)
    B = np.zeros((len(edges), n - 1), dtype=float)
    for e, (i, j) in enumerate(edges):
        s = float(edge_signs[e])
        if i < n - 1:
            B[e, i] += s
        if j < n - 1:
            B[e, j] -= s
    return B


def vertex_signs_for_sector(n: int, sector: int) -> np.ndarray:
    # Global flip fixed by sigma_0=+1; sector encodes remaining n-1 signs.
    sig = np.ones(n, dtype=int)
    for k in range(1, n):
        sig[k] = 1 if ((sector >> (k - 1)) & 1) else -1
    return sig


def edge_signs_from_vertices(n: int, sig: np.ndarray) -> np.ndarray:
    return np.array([sig[i] * sig[j] for i, j in complete_edges(n)], dtype=int)


def random_spd(dim: int, rng: np.random.Generator, spread: float) -> np.ndarray:
    Q, _ = np.linalg.qr(rng.normal(size=(dim, dim)))
    exponents = rng.uniform(-spread, spread, size=dim)
    vals = np.exp(exponents)
    return Q @ np.diag(vals) @ Q.T


def density_from_cov(S: np.ndarray) -> float:
    sign, logdet = np.linalg.slogdet(S)
    if sign <= 0:
        raise RuntimeError("covariance is not positive definite")
    m = S.shape[0]
    return float(np.exp(-0.5 * (m * np.log(2.0 * np.pi) + logdet)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    n = args.n
    profile = args.profile
    edges = complete_edges(n)
    m = len(edges)
    sector_count = 2 ** (n - 1)
    sector = profile % sector_count

    sig = vertex_signs_for_sector(n, sector)
    edge_signs = edge_signs_from_vertices(n, sig)
    B = reduced_incidence(n, edge_signs)

    U, svals, _ = np.linalg.svd(B, full_matrices=True)
    tol = 1e-12
    r = int(np.sum(svals > tol))
    q = m - r
    Ucut = U[:, :r]
    Ucycle = U[:, r:]

    rng = np.random.default_rng(310000 + profile)
    A = random_spd(r, rng, spread=2.0)
    K = random_spd(q, rng, spread=3.0)

    detA = float(np.linalg.det(A))
    detK = float(np.linalg.det(K))
    support_density = float((2.0 * np.pi) ** (-r / 2.0) / np.sqrt(detA))
    predicted_factor = float((2.0 * np.pi) ** (-q / 2.0) / np.sqrt(detK))
    universal_unit_det_factor = float((2.0 * np.pi) ** (-q / 2.0))

    # Determinant-normalized cycle metric.
    K0 = K / (detK ** (1.0 / q))
    detK0 = float(np.linalg.det(K0))

    etas = np.logspace(-1.0, -4.0, 10)
    ambient = []
    renorm_ratio = []
    ambient_unit = []
    renorm_ratio_unit = []

    cut_cov = Ucut @ A @ Ucut.T
    cyc_cov = Ucycle @ K @ Ucycle.T
    cyc_cov_unit = Ucycle @ K0 @ Ucycle.T

    for eta in etas:
        rho = density_from_cov(cut_cov + (eta ** 2) * cyc_cov)
        rho0 = density_from_cov(cut_cov + (eta ** 2) * cyc_cov_unit)
        ambient.append(rho)
        ambient_unit.append(rho0)
        renorm_ratio.append(float((eta ** q) * rho / support_density))
        renorm_ratio_unit.append(float((eta ** q) * rho0 / support_density))

    # Fit log rho = c + p log eta.
    slope = float(np.polyfit(np.log(etas), np.log(np.array(ambient)), 1)[0])
    slope_unit = float(np.polyfit(np.log(etas), np.log(np.array(ambient_unit)), 1)[0])

    rr = np.array(renorm_ratio)
    rru = np.array(renorm_ratio_unit)
    rel_err_pred = float(np.max(np.abs(rr / predicted_factor - 1.0)))
    rel_err_unit = float(np.max(np.abs(rru / universal_unit_det_factor - 1.0)))

    # Direct 10x10 slogdet becomes mildly ill-conditioned at eta=1e-4 because
    # six eigenvalues scale as eta^2.  A 1e-6 relative gate is still far tighter
    # than needed to distinguish the O(1) finite-part changes induced by det(K),
    # while avoiding false numerical failures at condition numbers ~1e9-1e10.
    finite_part_rtol = 1e-6

    gates = {
        "rank_is_n_minus_1": bool(r == n - 1),
        "cycle_nullity_is_6_for_k5": bool(q == 6 if n == 5 else q == m - (n - 1)),
        "ambient_slope_matches_minus_q": bool(abs(slope + q) < 2e-5),
        "analytic_finite_factor_matches": bool(rel_err_pred < finite_part_rtol),
        "unit_det_cycle_metric_restores_universal_factor": bool(rel_err_unit < finite_part_rtol),
        "unit_det_is_one": bool(abs(detK0 - 1.0) < 2e-10),
    }
    all_pass = bool(all(gates.values()))

    out = {
        "iteration": "Iter031",
        "n": n,
        "profile": profile,
        "sector": sector,
        "vertex_signs": sig.tolist(),
        "edge_signs": edge_signs.tolist(),
        "edge_count": m,
        "rank": r,
        "cycle_nullity": q,
        "det_cut_metric_A": detA,
        "det_cycle_metric_K": detK,
        "det_cycle_metric_K_unit_normalized": detK0,
        "support_density_at_origin": support_density,
        "predicted_renormalized_factor": predicted_factor,
        "universal_unit_det_factor": universal_unit_det_factor,
        "finite_part_relative_tolerance": finite_part_rtol,
        "eta": etas.tolist(),
        "ambient_density": ambient,
        "renormalized_ambient_over_support": renorm_ratio,
        "renormalized_unitdet_ambient_over_support": renorm_ratio_unit,
        "ambient_power_slope": slope,
        "unitdet_ambient_power_slope": slope_unit,
        "max_relative_error_predicted_factor": rel_err_pred,
        "max_relative_error_unitdet_universal_factor": rel_err_unit,
        "gates": gates,
        "all_hard_pass": all_pass,
        "classification": (
            "CYCLE_METRIC_DETERMINANT_CONTROLS_FINITE_PART_AFTER_ETA_POWER_SUBTRACTION"
            if all_pass else "ITER031_GATE_FAILURE"
        ),
        "scope_note": (
            "Linearized structural result only. Dependence of the finite ambient normalization on det(K) "
            "shows that power subtraction alone does not select a unique physical extension. Unit-determinant "
            "normalization removes this one scalar ambiguity but is not derived here from causal EPRL/Toller data."
        ),
    }

    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile": profile,
        "sector": sector,
        "q": q,
        "slope": slope,
        "detK": detK,
        "factor": float(np.mean(rr)),
        "predicted": predicted_factor,
        "unit_factor": float(np.mean(rru)),
        "all_hard_pass": all_pass,
    }, indent=2))
    if not all_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
