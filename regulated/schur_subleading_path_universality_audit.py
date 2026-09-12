#!/usr/bin/env python3
"""Iter033: test whether the renormalized finite part is controlled only by
leading Schur geometry under analytic eta-dependent regulator deformations.

Claim scope: finite-dimensional Gaussian K5 surrogate only.
"""
import argparse, json, math
from pathlib import Path
import numpy as np

TWOPI = 2.0 * math.pi


def k5_basis():
    # oriented incidence, one row removed -> rank 4 cut map in R^10
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    B = np.zeros((5, 10))
    for e, (i, j) in enumerate(edges):
        B[i, e] = 1.0
        B[j, e] = -1.0
    _, _, vh = np.linalg.svd(B[:4, :], full_matrices=True)
    qcut = vh[:4].T
    qcyc = vh[4:].T
    Q = np.column_stack([qcut, qcyc])
    return Q


def spd(rng, n, condition):
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    vals = np.geomspace(1.0, condition, n)
    return q @ np.diag(vals) @ q.T


def build_h0(rng, profile):
    cond_a = [1.5, 3.0, 10.0, 30.0][profile % 4]
    cond_s = [1.2, 2.5, 8.0, 20.0][(profile // 4) % 4]
    mix = [0.0, 0.15, 0.5, 1.0, 2.0, 3.0][profile % 6]
    A = spd(rng, 4, cond_a)
    S = spd(rng, 6, cond_s)
    C0 = rng.normal(size=(4, 6))
    C0 /= max(np.linalg.norm(C0, 2), 1e-15)
    C = mix * C0
    K = S + C.T @ np.linalg.solve(A, C)
    H0 = np.block([[A, C], [C.T, K]])
    return H0, A, S, dict(cond_a=cond_a, cond_s=cond_s, mix=mix)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--profile', type=int, required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    p = args.profile
    rng = np.random.default_rng(33000 + p)
    Q = k5_basis()
    H0, A0, S0, meta = build_h0(rng, p)

    # Analytic path H(eta)=L[I + eta*a R1 + eta^2*b R2]L^T.
    # This guarantees H(0)=H0 while probing nontrivial subleading path data.
    L = np.linalg.cholesky(H0)
    R1 = rng.normal(size=(10, 10)); R1 = (R1 + R1.T) / 2
    R2 = rng.normal(size=(10, 10)); R2 = (R2 + R2.T) / 2
    R1 /= max(np.linalg.norm(R1, 2), 1e-15)
    R2 /= max(np.linalg.norm(R2, 2), 1e-15)
    alpha = [0.0, 0.25, 0.75, 1.5, 3.0, 5.0][p % 6]
    beta = [0.0, 0.5, 2.0, 5.0][(p // 6) % 4]

    etas = np.array([2e-2, 1.4e-2, 1e-2, 7e-3, 5e-3, 3e-3, 2e-3, 1e-3, 5e-4])
    finite = []
    slopesafe = []
    min_eigs = []
    density_logs = []
    for eta in etas:
        M = np.eye(10) + eta * alpha * R1 + eta**2 * beta * R2
        H = L @ M @ L.T
        min_eigs.append(float(np.linalg.eigvalsh(H).min()))
        D = np.diag([1.0]*4 + [eta]*6)
        Sigma = Q @ D @ H @ D @ Q.T
        sign, logdet_sigma = np.linalg.slogdet(Sigma)
        Aeta = H[:4, :4]
        signa, logdet_a = np.linalg.slogdet(Aeta)
        if sign <= 0 or signa <= 0:
            raise RuntimeError('non-positive determinant')
        log_rho_ambient = -5.0*math.log(TWOPI) - 0.5*logdet_sigma
        log_rho_cut = -2.0*math.log(TWOPI) - 0.5*logdet_a
        f = math.exp(6.0*math.log(eta) + log_rho_ambient - log_rho_cut)
        finite.append(f)
        density_logs.append(log_rho_ambient - log_rho_cut)

    finite = np.array(finite)
    predicted = TWOPI**(-3.0) / math.sqrt(np.linalg.det(S0))
    # Fit subleading analytic corrections; intercept is the eta->0 finite part.
    coeff = np.polyfit(etas, finite, deg=3)
    intercept = float(coeff[-1])
    rel_intercept = abs(intercept/predicted - 1.0)
    smallest_rel = abs(float(finite[-1])/predicted - 1.0)
    # Independent exponent fit: raw ratio should scale eta^-6 asymptotically.
    tail = slice(-5, None)
    slope = float(np.polyfit(np.log(etas[tail]), np.array(density_logs)[tail], 1)[0])
    slope_err = abs(slope + 6.0)
    spd_ok = min(min_eigs) > 1e-10
    # Preregistered hard gates chosen above numerical floor but tighter than O(eta) bias.
    passed = bool(spd_ok and rel_intercept < 2e-5 and slope_err < 3e-2 and smallest_rel < 2e-2)

    out = {
        'iteration': 33,
        'profile': p,
        'claim_scope': 'Gaussian K5 surrogate; no microscopic spin-foam claim',
        'question': 'Is the renormalized finite part insensitive to analytic subleading regulator-path deformations at fixed leading Schur geometry?',
        'meta': {**meta, 'alpha': alpha, 'beta': beta},
        'predicted_leading_schur_factor': predicted,
        'extrapolated_finite_factor': intercept,
        'relative_intercept_error': rel_intercept,
        'smallest_eta_relative_error': smallest_rel,
        'raw_log_slope': slope,
        'slope_error_from_minus6': slope_err,
        'minimum_H_eigenvalue': min(min_eigs),
        'etas': etas.tolist(),
        'finite_factors': finite.tolist(),
        'hard_gates': {
            'spd_all_eta': spd_ok,
            'relative_intercept_error_lt_2e-5': rel_intercept < 2e-5,
            'slope_error_lt_3e-2': slope_err < 3e-2,
            'smallest_eta_relative_error_lt_2e-2': smallest_rel < 2e-2,
        },
        'pass': passed,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out, indent=2))
    if not passed:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
