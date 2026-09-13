#!/usr/bin/env python3
"""Iter076U — j=1/2 intertwiner-contracted regularized K5 one-jet witness.

Prospectively frozen by prereg/ITER076U_JHALF_INTERTWINER_CONTRACTED_ONEJET.md.
This is a pre-group-integration existence/no-universal-cancellation diagnostic.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.boundary_intertwiner_collision_power import NODE, contract_network
from vertex.direct_causal_integrand_smoke import PAIRS
from vertex.regulated_haar_mc_vertex import full_branch

ROOT = Path(__file__).resolve().parents[1]
mp.mp.dps = 70
MS = (1, -1)
PATHS = {
    0: (0.0, 1.0, 2.0, 4.0, 7.0),
    1: (0.0, -1.0, 2.0, 5.0, 9.0),
    2: (0.0, 1.0, -3.0, 4.0, 8.0),
    3: (0.0, -2.0, 1.0, 6.0, 10.0),
}
RADII = np.asarray([0.020, 0.015, 0.010, 0.0075, 0.0050, 0.0035], dtype=float)
BOUNDARY_STATES = list(itertools.product((0, 2), repeat=5))
SIGMAS = [(1,) + tail for tail in itertools.product((-1, 1), repeat=4)]


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def boost_z(x):
    return np.asarray([[math.exp(x / 2), 0j], [0j, math.exp(-x / 2)]], dtype=complex)


def groups_for(path_id, r):
    return [boost_z(v * r) for v in PATHS[path_id]]


def edge_regularized_mats(groups, gamma):
    out = {}
    max_kerr = 0.0
    for a, b in PAIRS:
        rel = np.linalg.inv(groups[b]) @ groups[a]
        bmats = {+1: np.zeros((2, 2), dtype=np.complex128), -1: np.zeros((2, 2), dtype=np.complex128)}
        beta_ref = None
        for im, m_ba in enumerate(MS):
            for jn, m_ab in enumerate(MS):
                tp, beta, ke1 = full_branch(+1, rel, gamma, m_ba, m_ab)
                tm, beta2, ke2 = full_branch(-1, rel, gamma, m_ba, m_ab)
                if abs(beta - beta2) > 1e-12:
                    raise RuntimeError("branch beta mismatch")
                fac = mp.sinh(mp.mpf(str(beta))) ** 2
                bmats[+1][im, jn] = complex(fac * tp)
                bmats[-1][im, jn] = complex(fac * tm)
                beta_ref = beta
                max_kerr = max(max_kerr, float(ke1), float(ke2))
        out[(a, b)] = (bmats[+1], bmats[-1], beta_ref)
    return out, max_kerr


def mats_for_sigma(edgevals, sigma):
    out = {}
    for a, b in PAIRS:
        tp, tm, _ = edgevals[(a, b)]
        out[(a, b)] = tp if sigma[a] * sigma[b] > 0 else tm
    return out


def eprl_mats(edgevals):
    return {e: edgevals[e][0] + edgevals[e][1] for e in PAIRS}


def polyfit_complex(xs, ys):
    coeff = np.polyfit(np.asarray(xs, dtype=float), np.asarray(ys, dtype=np.complex128), 2)
    return complex(coeff[2]), complex(coeff[1]), complex(coeff[0])  # c0,c1,c2


def robust_witness(vals):
    c0f, c1f, _ = polyfit_complex(RADII, vals)
    c0s, c1s, _ = polyfit_complex(RADII[-4:], vals[-4:])
    finite = all(np.isfinite([c0f.real, c0f.imag, c1f.real, c1f.imag, c0s.real, c0s.imag, c1s.real, c1s.imag]))
    threshold = 1e-7 * max(1.0, abs(c0s))
    nonzero = abs(c1s) > threshold
    stable = abs(c1f - c1s) <= 0.15 * max(abs(c1s), 1e-30)
    return {
        "finite": bool(finite),
        "c0_small": [c0s.real, c0s.imag],
        "c1_full": [c1f.real, c1f.imag],
        "c1_small": [c1s.real, c1s.imag],
        "abs_c1_small": abs(c1s),
        "threshold": threshold,
        "relative_window_difference": abs(c1f - c1s) / max(abs(c1s), 1e-30),
        "robust_nonzero": bool(finite and nonzero and stable),
    }


def lane_a():
    betas = [mp.mpf(x) for x in ("0.02", "0.01", "0.005", "0.0025")]
    rows = []
    all_ok = True
    for gamma_s in ("0.4", "1.2"):
        rho = mp.mpf(gamma_s) / 2
        for branch in (+1, -1):
            for two_p in (+1, -1):
                vals = []
                for beta in betas:
                    raw = ep.toller_plus(1, 1, two_p, 1, rho, beta) if branch > 0 else ep.toller_minus(1, 1, two_p, 1, rho, beta)
                    vals.append(mp.sinh(beta) ** 2 * raw)
                mags = [abs(v) for v in vals]
                finite = all(mp.isfinite(mp.re(v)) and mp.isfinite(mp.im(v)) for v in vals)
                ratio = mags[-1] / max(mags[-2], mp.mpf("1e-80"))
                stable_no_blowup = finite and ratio < 4
                all_ok &= bool(stable_no_blowup)
                rows.append({
                    "gamma": gamma_s,
                    "branch": branch,
                    "two_p": two_p,
                    "magnitudes": [mp.nstr(x, 18) for x in mags],
                    "last_ratio": mp.nstr(ratio, 18),
                    "stable_no_blowup": bool(stable_no_blowup),
                })
    return {"iteration": "Iter076U", "lane": "A", "valid": bool(all_ok), "rows": rows}


def census(gamma_s, path_id):
    gamma = mp.mpf(gamma_s)
    ep.GAMMA = gamma
    series = {(si, bi): [] for si in range(len(SIGMAS)) for bi in range(len(BOUNDARY_STATES))}
    eprl_series = []
    max_kerr = 0.0
    min_beta = float("inf")
    for r in RADII:
        groups = groups_for(path_id, float(r))
        edgevals, ke = edge_regularized_mats(groups, gamma)
        max_kerr = max(max_kerr, ke)
        min_beta = min(min_beta, *(float(edgevals[e][2]) for e in PAIRS))
        for si, sigma in enumerate(SIGMAS):
            mats = mats_for_sigma(edgevals, sigma)
            for bi, bstate in enumerate(BOUNDARY_STATES):
                series[(si, bi)].append(contract_network(mats, bstate))
        eprl_series.append(contract_network(eprl_mats(edgevals), BOUNDARY_STATES[0]))

    witnesses = []
    robust_count = 0
    finite_count = 0
    for (si, bi), vals in series.items():
        fit = robust_witness(vals)
        finite_count += int(fit["finite"])
        if fit["robust_nonzero"]:
            robust_count += 1
            if len(witnesses) < 12:
                witnesses.append({
                    "sigma_index": si,
                    "sigma": list(SIGMAS[si]),
                    "boundary_index": bi,
                    "boundary_state": list(BOUNDARY_STATES[bi]),
                    **fit,
                })
    eprl_finite = all(np.isfinite([z.real, z.imag]).all() if isinstance(np.isfinite([z.real, z.imag]), np.ndarray) else True for z in eprl_series)
    valid = max_kerr < 1e-10 and finite_count == len(series) and eprl_finite
    return {
        "iteration": "Iter076U",
        "lane": "B_SHARD",
        "valid": bool(valid),
        "gamma": gamma_s,
        "path_id": path_id,
        "path": list(PATHS[path_id]),
        "cases": len(series),
        "finite_fit_cases": finite_count,
        "robust_nonzero_witness_count": robust_count,
        "sample_witnesses": witnesses,
        "max_kak_reconstruction_error": max_kerr,
        "min_pair_beta_sampled": min_beta,
        "eprl_control_finite": bool(eprl_finite),
        "radii": RADII.tolist(),
    }


def lane_c():
    node_norms = {str(k): float(np.linalg.norm(v.ravel())) for k, v in NODE.items()}
    nodes_ok = set(NODE) == {0, 2} and all(abs(x - 1.0) < 1e-12 for x in node_norms.values())
    factorization_ok = True
    triangle_checks = 0
    for sigma in SIGMAS:
        kap = {(a, b): sigma[a] * sigma[b] for a, b in PAIRS}
        for a, b, c in itertools.combinations(range(5), 3):
            factorization_ok &= kap[tuple(sorted((a, b)))] * kap[tuple(sorted((b, c)))] * kap[tuple(sorted((a, c)))] == 1
            triangle_checks += 1
    valid = nodes_ok and factorization_ok and len(BOUNDARY_STATES) == 32 and len(SIGMAS) == 16
    return {
        "iteration": "Iter076U",
        "lane": "C",
        "valid": bool(valid),
        "node_tensor_norms": node_norms,
        "boundary_state_count": len(BOUNDARY_STATES),
        "causal_sigma_count": len(SIGMAS),
        "triangle_factorization_checks": triangle_checks,
        "all_source_factorizable": bool(factorization_ok),
    }


def lane_d():
    locks = {
        "four_group_integrated_vertex_onejet_established": False,
        "general_spin_contracted_onejet_theorem": False,
        "physical_nonlinear_source_to_k4_curvature_selected": False,
        "epsilon_minus1_coefficient_established": False,
        "generic_finite_spin_signed_p3_promoted": False,
        "physical_finiteness_or_divergence_theorem": False,
        "G3_promoted": False,
        "F9_promoted": False,
        "G8_promoted": False,
        "K5_promoted": False,
    }
    current = (ROOT / "status/CURRENT.md").read_text(encoding="utf-8")
    t_result = (ROOT / "results/ITER076T_TOLLER_HAAR_REGULARIZED_WEDGE_ONEJET_RESULT.md").read_text(encoding="utf-8")
    evidence = {
        "current_epsilon_blocked": "nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`" in current,
        "iter076t_full_contracted_missing": "FULL_TOLLER_INTERTWINER_CONTRACTED_NUMERATOR_ONEJET" in t_result,
        "iter076t_local_only": "deliberately local/source-wedge scoped" in t_result,
    }
    valid = all(evidence.values()) and not any(locks.values())
    return {
        "iteration": "Iter076U",
        "lane": "D",
        "valid": bool(valid),
        "evidence": evidence,
        "scope_locks": locks,
        "next_missing_layer": "CORRELATED_GROUP_INTEGRATED_CONTRACTED_NUMERATOR_ONEJET",
    }


def aggregate(root):
    shard_rows = []
    fixed = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            lane = obj.get("lane")
            if lane == "B_SHARD":
                shard_rows.append(obj)
            elif lane in ("A", "C", "D"):
                fixed[lane] = obj
    shard_rows.sort(key=lambda x: (float(x["gamma"]), int(x["path_id"])))
    expected_shards = 8
    shards_valid = len(shard_rows) == expected_shards and all(x.get("valid") for x in shard_rows)
    gamma_witness = {}
    for g in ("0.4", "1.2"):
        total = sum(int(x["robust_nonzero_witness_count"]) for x in shard_rows if x["gamma"] == g)
        gamma_witness[g] = total
    witnesses_pass = all(gamma_witness[g] > 0 for g in gamma_witness)
    fixed_valid = set(fixed) == {"A", "C", "D"} and all(fixed[k].get("valid") for k in fixed)
    max_kerr = max((float(x["max_kak_reconstruction_error"]) for x in shard_rows), default=float("inf"))
    all_valid = shards_valid and witnesses_pass and fixed_valid and max_kerr < 1e-10
    classification = (
        "ITER076U_JHALF_INTERTWINER_CONTRACTED_REGULARIZED_K5_TENSOR_HAS_NONZERO_ONEJET_WITNESS_GROUP_INTEGRATED_ONEJET_STILL_REQUIRED_SCOPED"
        if all_valid
        else (
            "ITER076U_NO_INTERTWINER_CONTRACTED_ONEJET_WITNESS_ON_FROZEN_JHALF_PATHS_INCONCLUSIVE_SCOPED"
            if shards_valid and fixed_valid and not witnesses_pass
            else "ITER076U_JHALF_INTERTWINER_CONTRACTED_ONEJET_GATE_FAIL"
        )
    )
    return {
        "iteration": "Iter076U",
        "valid": bool(all_valid or (shards_valid and fixed_valid and not witnesses_pass)),
        "classification": classification,
        "shards_found": len(shard_rows),
        "total_census_cases": sum(int(x["cases"]) for x in shard_rows),
        "robust_witness_count_by_gamma": gamma_witness,
        "total_robust_witnesses": sum(gamma_witness.values()),
        "max_kak_reconstruction_error": max_kerr,
        "fixed_lane_valid": {k: bool(fixed.get(k, {}).get("valid")) for k in ("A", "C", "D")},
        "group_integrated_onejet_established": False,
        "general_spin_theorem_established": False,
        "epsilon_minus1_coefficient_established": False,
        "next_admissible_gate": "Move only to correlated group-integrated contracted numerator one-jet or derive the physical nonlinear source-to-K4 curvature; do not repeat local/intertwiner cancellation tests.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("A", "census", "C", "D"))
    ap.add_argument("--gamma")
    ap.add_argument("--path-id", type=int)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        obj = aggregate(args.aggregate_dir)
    elif args.mode == "A":
        obj = lane_a()
    elif args.mode == "C":
        obj = lane_c()
    elif args.mode == "D":
        obj = lane_d()
    elif args.mode == "census":
        if args.gamma is None or args.path_id not in PATHS:
            raise SystemExit("census requires --gamma and valid --path-id")
        obj = census(args.gamma, args.path_id)
    else:
        raise SystemExit("choose --mode or --aggregate-dir")
    write(obj, args.output)
    print(json.dumps(obj, indent=2, sort_keys=True))
    if not obj.get("valid"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
