#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction

N = 10
CRITIC_PREREG = "2e788241b2e14dc5af9c95bc09d6c16125d9378f"
RESEARCHER_RUN = 35087556685


def interior(vector, form):
    """Interior product of a numeric vector with an alternating form.

    form: dict[sorted index tuple] -> Fraction coefficient.
    """
    out = {}
    for inds, coeff in form.items():
        for p, idx in enumerate(inds):
            c = coeff * vector[idx] * (Fraction(-1) if p % 2 else Fraction(1))
            key = inds[:p] + inds[p + 1 :]
            out[key] = out.get(key, Fraction(0)) + c
            if out[key] == 0:
                del out[key]
    return out


def form_sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) - v
        if out[k] == 0:
            del out[k]
    return out


def vec_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def vec_scale(c, a):
    return [c * x for x in a]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def jacobian_ratio(k):
    if k == 1:
        return Fraction(1)
    den = (k - 1) * k // 2 + k
    beta = [Fraction(i + 1, den) for i in range(k - 1)]
    beta.append(Fraction(1) - sum(beta, Fraction(0)))
    t = Fraction(7, 5)
    J = []
    for i in range(k):
        row = [beta[i]]
        for a in range(k - 1):
            row.append(t * ((1 if i == a else 0) if i < k - 1 else -1))
        J.append(row)
    # exact elimination
    A = [[Fraction(x) for x in row] for row in J]
    d = Fraction(1)
    for c in range(k):
        p = next((r for r in range(c, k) if A[r][c]), None)
        if p is None:
            return Fraction(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        z = A[c][c]
        d *= z
        for j in range(c, k):
            A[c][j] /= z
        for r in range(c + 1, k):
            q = A[r][c]
            for j in range(c, k):
                A[r][j] -= q * A[c][j]
    return d / (t ** (k - 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    # Generic positive rational point on s1=1.
    weights = [Fraction(i + 1, 55) for i in range(N)]
    assert sum(weights, Fraction(0)) == 1
    E = list(weights)
    vol = {tuple(range(N)): Fraction(1)}
    Omega = interior(E, vol)

    # Projective identity i_E Omega = i_E i_E vol = 0.
    radial_flux = interior(E, Omega)

    # Generic logarithmic polynomial field with constant polynomial q_i=i+1.
    q = [Fraction(i + 1) for i in range(N)]
    v = [weights[i] * q[i] for i in range(N)]
    S = sum(v, Fraction(0))
    s1 = sum(weights, Fraction(0))
    u = vec_sub(v, vec_scale(S / s1, E))
    ivOmega = interior(v, Omega)
    iuOmega = interior(u, Omega)

    # Proper subset Z and exact normal component in the affine simplex tangent field.
    Z = (0, 1, 2, 3)
    indicator = [Fraction(1 if i in Z else 0) for i in range(N)]
    t = dot(indicator, weights)
    v_t = dot(indicator, v)
    u_t = dot(indicator, u)
    projected_formula = v_t - t * S / s1

    # Decisive admissible counterexample to the Researcher universal raw-v(t) flux formula:
    # choose q_i=1, hence v=E. The true projective contraction vanishes, but raw v(t)=t>0.
    v_radial = E
    true_radial_projective_flux = interior(v_radial, Omega)
    raw_radial_v_t = t
    researcher_raw_formula_predicts_nonzero = raw_radial_v_t != 0
    true_projective_flux_zero = true_radial_projective_flux == {}
    contradiction = researcher_raw_formula_predicts_nonzero and true_projective_flux_zero

    jac_ok = all(abs(jacobian_ratio(k)) == 1 for k in range(1, 10))
    checks = {
        "scalar_jacobian_t_pow_k_minus_1_confirmed": jac_ok,
        "projective_form_radial_annihilation_iE_Omega_zero": radial_flux == {},
        "contraction_invariant_under_radial_representative_change": form_sub(ivOmega, iuOmega) == {},
        "simplex_tangent_sum_u_zero": sum(u, Fraction(0)) == 0,
        "projected_normal_component_formula": u_t == projected_formula,
        "radial_counterexample_raw_vt_nonzero": researcher_raw_formula_predicts_nonzero,
        "radial_counterexample_true_projective_flux_zero": true_projective_flux_zero,
        "researcher_universal_raw_vt_flux_formula_contradicted": contradiction,
    }

    implementation_valid = all(checks.values())
    verdict = "SCIENTIFIC_FAIL_CONFIRMED" if implementation_valid else "INVALID_IMPLEMENTATION"
    out = {
        "gate": "K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_INDEPENDENT_CRITIC_REVIEW",
        "critic_prereg_commit": CRITIC_PREREG,
        "researcher_run": RESEARCHER_RUN,
        "verdict": verdict,
        "checks": checks,
        "subset_Z": list(Z),
        "sample_s1": str(s1),
        "sample_t": str(t),
        "sample_S": str(S),
        "sample_v_t": str(v_t),
        "sample_u_t": str(u_t),
        "correct_projective_normal_component": "u(t)=v(t)-t*S/s1",
        "researcher_claim_under_attack": "pullback(i_v Omega_9)=+-t^(k-1)*v(t)*omega_Z for raw ambient v",
        "counterexample": {
            "field": "v=E, equivalently q_i=1 for every i",
            "raw_v_t": str(raw_radial_v_t),
            "i_v_Omega_zero": true_projective_flux_zero,
        },
        "scalar_jacobian_result_survives": jac_ok,
        "physical_corner_verdict": None,
        "integrated_stokes_verdict": None,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not implementation_valid:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
