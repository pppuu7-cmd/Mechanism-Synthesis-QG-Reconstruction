#!/usr/bin/env python3
"""Iter042B: Molien/plethystic fingerprint of S5 invariants on Cycle(K5).

This is a representation-theory compression of the extension ambiguity found
in Iter039/040.  It computes exact integer invariant multiplicities from the
same S5 cycle representation, then forms the truncated plethystic logarithm of
the Hilbert series.  Positive/negative coefficients are a generator/relation
*fingerprint* only; beyond the first uncancelled orders they are not asserted
to be a minimal presentation of the invariant ring.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

from distributional.k5_extension_invariant_jet_audit import cycle_basis, cycle_rep, inv_dim

N = 5


def conv(a, b, nmax):
    out = [Fraction(0) for _ in range(nmax + 1)]
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            if i + j > nmax:
                break
            if y:
                out[i + j] += x * y
    return out


def log_series(h, nmax):
    # log(1+u)=sum_{k>=1}(-1)^(k+1)u^k/k
    u = [Fraction(x) for x in h]
    u[0] -= 1
    power = [Fraction(0)] * (nmax + 1)
    power[0] = 1
    out = [Fraction(0)] * (nmax + 1)
    for k in range(1, nmax + 1):
        power = conv(power, u, nmax)
        sign = 1 if k % 2 else -1
        for n in range(1, nmax + 1):
            out[n] += sign * power[n] / k
    return out


def mobius(n):
    if n == 1:
        return 1
    x = n
    p = 2
    count = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-degree", type=int, default=32)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    nmax = a.max_degree
    if not 8 <= nmax <= 48:
        raise SystemExit("max-degree must be in [8,48]")

    q = cycle_basis()
    s5 = list(itertools.permutations(range(N)))
    reps = {p: cycle_rep(p, q) for p in s5}
    dims = []
    residuals = []
    for d in range(nmax + 1):
        dim, res = inv_dim(s5, reps, d)
        dims.append(dim)
        residuals.append(res)

    logh = log_series(dims, nmax)
    pl = [Fraction(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        pl[n] = sum(Fraction(mobius(k), k) * logh[n // k] for k in divisors(n))

    nonzero = []
    for n in range(1, nmax + 1):
        if pl[n]:
            nonzero.append({
                "degree": n,
                "coefficient": str(pl[n]),
                "sign": "positive" if pl[n] > 0 else "negative",
            })

    primitive_by_quadratic = [None, None]
    for d in range(2, nmax + 1):
        primitive_by_quadratic.append(dims[d] - dims[d - 2])

    gates = {
        "constant_term_is_one": dims[0] == 1,
        "quadratic_invariant_unique": dims[2] == 1,
        "integrality_residual_ok": max(residuals) < 2e-7,
        "all_dimensions_nonnegative": all(x >= 0 for x in dims),
    }

    out = {
        "iteration": "Iter042B",
        "max_degree": nmax,
        "s5_hilbert_coefficients": dims,
        "quadratic_quotient_dimensions": primitive_by_quadratic,
        "plethystic_log_nonzero_coefficients": nonzero,
        "max_character_integrality_residual": max(residuals),
        "numerical_gates": gates,
        "classification": "S5_INVARIANT_RING_PLETHYSTIC_FINGERPRINT_COMPUTED",
        "claim_lock": (
            "Representation-theory diagnostic only. The truncated plethystic logarithm is used to localize "
            "candidate generator/relation degrees; it is not by itself a proof of a minimal invariant-ring "
            "presentation and supplies no physical counterterm or Feynman-extension prescription."
        ),
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
