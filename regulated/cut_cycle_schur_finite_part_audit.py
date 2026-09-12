#!/usr/bin/env python3
"""Iter032 — cut/cycle Schur-complement finite-part universality audit.

Iter031 established that, for block-diagonal cut/cycle covariance, removing the
eta^-q divergence leaves a finite factor controlled by det(K). Iter032 allows
generic O(eta) cut-cycle mixing:

    Sigma_eta = Q D_eta H D_eta Q^T,
    H = [[A, C], [C^T, K]],
    D_eta = diag(I_r, eta I_q).

For positive-definite H,

    det(Sigma_eta) = eta^(2q) det(H)
                   = eta^(2q) det(A) det(S),
    S = K - C^T A^-1 C.

Relative to the natural cut-space density using A, the minimally renormalized
ambient finite factor is therefore

    eta^q rho_ambient(0) / rho_cut(0)
      = (2 pi)^(-q/2) det(S)^(-1/2).

Thus generic cut-cycle mixing promotes the Iter031 cycle-metric determinant to
the determinant of the conditional/Schur cycle metric S. Merely imposing
det(K)=1 is not sufficient when C != 0. Determinant-normalizing S should
restore the universal factor (2 pi)^(-q/2).

This is a structural Gaussian audit, not a derivation of a physical causal
EPRL/Toller regulator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np


def complete_edges(n: int):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def reduced_incidence(n: int, edge_signs: np.ndarray) -> np.ndarray:
    B = np.zeros((len(complete_edges(n)), n - 1), dtype=float)
    for e, (i, j) in enumerate(complete_edges(n)):
        s = float(edge_signs[e])
        if i < n - 1:
            B[e, i] += s
        if j < n - 1:
            B[e, j] -= s
    return B


def vertex_signs_for_sector(n: int, sector: int) -> np.ndarray:
    sig = np.ones(n, dtype=int)
    for k in range(1, n):
        sig[k] = 1 if ((sector >> (k - 1)) & 1) else -1
    return sig


def edge_signs_from_vertices(n: int, sig: np.ndarray) -> np.ndarray:
    return np.array([sig[i] * sig[j] for i, j in complete_edges(n)], dtype=int)


def random_spd(dim: int, rng: np.random.Generator, spread: float) -> np.ndarray:
    Q, _ = np.linalg.qr(rng.normal(size=(dim, dim)))
    vals = np.exp(rng.uniform(-spread, spread, size=dim))
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

    n, profile = args.n, args.profile
    m = len(complete_edges(n))
    sector = profile % (2 ** (n - 1))
    sig = vertex_signs_for_sector(n, sector)
    B = reduced_incidence(n, edge_signs_from_vertices(n, sig))
    U, svals, _ = np.linalg.svd(B, full_matrices=True)
    r = int(np.sum(svals > 1e-12))
    q = m - r
    Qbasis = U[:, :m]

    rng = np.random.default_rng(320000 + profile)
    A = random_spd(r, rng, 1.8)
    # Build H through a Schur-positive parameterization so mixing can be strong
    # without accidental loss of positive definiteness.
    S = random_spd(q, rng, 2.6)
    mix_scale = [0.0, 0.15, 0.35, 0.65, 1.0, 1.5, 2.0, 3.0][profile % 8]
    C = mix_scale * rng.normal(size=(r, q)) / np.sqrt(max(r, q))
    AinvC = np.linalg.solve(A, C)
    K = S + C.T @ AinvC
    H = np.block([[A, C], [C.T, K]])

    eigH = np.linalg.eigvalsh(H)
    Schur = K - C.T @ np.linalg.solve(A, C)
    eigS = np.linalg.eigvalsh(Schur)
    detA = float(np.linalg.det(A))
    detK = float(np.linalg.det(K))
    detS = float(np.linalg.det(Schur))

    rho_cut = float((2.0 * np.pi) ** (-r / 2.0) / np.sqrt(detA))
    predicted = float((2.0 * np.pi) ** (-q / 2.0) / np.sqrt(detS))
    universal = float((2.0 * np.pi) ** (-q / 2.0))

    # A control that enforces det(K)=1 while retaining nonzero mixing. It is
    # deliberately not expected to restore universality in general.
    scaleK = detK ** (-1.0 / q)
    K_unit = scaleK * K
    # To preserve SPD after this rescaling we reduce C only if necessary.
    C_unit = C.copy()
    for _ in range(30):
        S_unitK = K_unit - C_unit.T @ np.linalg.solve(A, C_unit)
        if np.min(np.linalg.eigvalsh(S_unitK)) > 1e-10:
            break
        C_unit *= 0.8
    detS_unitK = float(np.linalg.det(S_unitK))
    unitK_factor = float((2.0 * np.pi) ** (-q / 2.0) / np.sqrt(detS_unitK))

    # Construct a comparison block with the same A,C but Schur determinant 1.
    S0 = Schur / (detS ** (1.0 / q))
    K0 = S0 + C.T @ np.linalg.solve(A, C)
    H0 = np.block([[A, C], [C.T, K0]])

    etas = np.logspace(-1.0, -4.0, 10)
    ambient, ratios, ambient0, ratios0 = [], [], [], []
    for eta in etas:
        D = np.diag(np.r_[np.ones(r), eta * np.ones(q)])
        Sigma = Qbasis @ (D @ H @ D) @ Qbasis.T
        Sigma0 = Qbasis @ (D @ H0 @ D) @ Qbasis.T
        rho = density_from_cov(Sigma)
        rho0 = density_from_cov(Sigma0)
        ambient.append(rho)
        ambient0.append(rho0)
        ratios.append(float((eta ** q) * rho / rho_cut))
        ratios0.append(float((eta ** q) * rho0 / rho_cut))

    slope = float(np.polyfit(np.log(etas), np.log(ambient), 1)[0])
    slope0 = float(np.polyfit(np.log(etas), np.log(ambient0), 1)[0])
    rr, rr0 = np.array(ratios), np.array(ratios0)
    err_pred = float(np.max(np.abs(rr / predicted - 1.0)))
    err_univ = float(np.max(np.abs(rr0 / universal - 1.0)))

    # Verify the determinant identity directly in the unscaled H block.
    signH, logdetH = np.linalg.slogdet(H)
    det_identity_rel = float(abs(np.exp(logdetH) / (detA * detS) - 1.0))

    gates = {
        "rank_is_n_minus_1": bool(r == n - 1),
        "cycle_nullity_expected": bool(q == m - (n - 1)),
        "H_positive_definite": bool(signH > 0 and np.min(eigH) > 0.0),
        "schur_positive_definite": bool(np.min(eigS) > 0.0),
        "ambient_slope_minus_q": bool(abs(slope + q) < 3e-5),
        "schur_prediction_matches": bool(err_pred < 2e-6),
        "schur_unitdet_restores_universal": bool(err_univ < 2e-6),
        "determinant_factorization": bool(det_identity_rel < 2e-10),
    }
    all_pass = bool(all(gates.values()))

    out = {
        "iteration": "Iter032",
        "profile": profile,
        "sector": sector,
        "n": n,
        "edge_count": m,
        "rank": r,
        "cycle_nullity": q,
        "mix_scale": mix_scale,
        "det_A": detA,
        "det_K": detK,
        "det_Schur": detS,
        "predicted_renormalized_factor": predicted,
        "universal_unit_schur_factor": universal,
        "detK_unit_control_detSchur": detS_unitK,
        "detK_unit_control_factor": unitK_factor,
        "eta": etas.tolist(),
        "ambient_density": ambient,
        "renormalized_over_cut": ratios,
        "schur_unitdet_renormalized_over_cut": ratios0,
        "ambient_power_slope": slope,
        "schur_unitdet_power_slope": slope0,
        "max_relative_error_schur_prediction": err_pred,
        "max_relative_error_schur_unitdet_universal": err_univ,
        "determinant_factorization_relative_error": det_identity_rel,
        "gates": gates,
        "all_hard_pass": all_pass,
        "classification": "SCHUR_CYCLE_VOLUME_CONTROLS_FINITE_PART" if all_pass else "ITER032_GATE_FAILURE",
        "scope_note": (
            "Structural Gaussian result only. With generic O(eta) cut-cycle mixing, the finite part after eta^-q subtraction is controlled by the determinant of the Schur complement K-C^T A^-1 C, not det(K) alone. A physical causal prescription must derive or cancel this conditional cycle-volume normalization."
        ),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile": profile, "sector": sector, "mix_scale": mix_scale,
        "q": q, "slope": slope, "detK": detK, "detSchur": detS,
        "factor": float(np.mean(rr)), "predicted": predicted,
        "unit_schur_factor": float(np.mean(rr0)), "universal": universal,
        "all_hard_pass": all_pass,
    }, indent=2))
    if not all_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
