#!/usr/bin/env python3
"""Iter077J-SM control-only repair.

Repairs the frozen exact-Q(i)-rank/nullspace requirement without changing any
Iter077J scientific object, ray, boundary state, or PASS/FAIL criterion.
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
J_PATH = ROOT / "distributional" / "iter077j_sm_full32_leading_angular_span.py"
spec = importlib.util.spec_from_file_location("iter077j_base", J_PATH)
jbase = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(jbase)

FROZEN_PRIMES = (1_000_000_007, 1_000_000_087, 1_000_000_103, 1_000_000_123)
ZEROQ = (Fraction(0), Fraction(0))
ONEQ = (Fraction(1), Fraction(0))


def q(z):
    return (Fraction(z[0]), Fraction(z[1]))


def qzero(z):
    return z[0] == 0 and z[1] == 0


def qadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def qsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def qmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def qinv(a):
    den = a[0] * a[0] + a[1] * a[1]
    if den == 0:
        raise ZeroDivisionError
    return (a[0] / den, -a[1] / den)


def qscale_inv_row(row, pivot):
    inv = qinv(pivot)
    return [qmul(inv, z) for z in row]


def exact_rref(rows):
    """Reduced row echelon form over Q(i). Returns (matrix,pivot_columns)."""
    m = [[q(z) for z in row] for row in rows]
    if not m:
        return m, []
    nrow, ncol = len(m), len(m[0])
    pivots = []
    r = 0
    for c in range(ncol):
        p = next((rr for rr in range(r, nrow) if not qzero(m[rr][c])), None)
        if p is None:
            continue
        if p != r:
            m[r], m[p] = m[p], m[r]
        m[r] = qscale_inv_row(m[r], m[r][c])
        for rr in range(nrow):
            if rr == r or qzero(m[rr][c]):
                continue
            f = m[rr][c]
            m[rr] = [qsub(x, qmul(f, y)) for x, y in zip(m[rr], m[r])]
        pivots.append(c)
        r += 1
        if r == nrow:
            break
    return m, pivots


def null_witness_from_rref(rref, pivots, ncol=32):
    free = [c for c in range(ncol) if c not in pivots]
    if not free:
        return None
    f = free[0]
    x = [ZEROQ for _ in range(ncol)]
    x[f] = ONEQ
    for rr, pc in enumerate(pivots):
        x[pc] = (-rref[rr][f][0], -rref[rr][f][1])
    return x


def integerize(witness):
    den = 1
    for a, b in witness:
        den = math.lcm(den, a.denominator, b.denominator)
    vals = [(int(a * den), int(b * den)) for a, b in witness]
    g = 0
    for a, b in vals:
        g = math.gcd(g, abs(a))
        g = math.gcd(g, abs(b))
    if g > 1:
        vals = [(a // g, b // g) for a, b in vals]
    # deterministic phase/sign normalization: first nonzero Gaussian pair has
    # positive real part, or positive imaginary part if real part is zero.
    first = next(z for z in vals if z != (0, 0))
    if first[0] < 0 or (first[0] == 0 and first[1] < 0):
        vals = [(-a, -b) for a, b in vals]
    return vals


def verify_integer_null(rows, witness):
    for row in rows:
        acc = (0, 0)
        for z, x in zip(row, witness):
            acc = jbase.base.gadd(acc, jbase.base.gmul(z, x))
        if acc != (0, 0):
            return False
    return True


def finite_difference_degree10_control(rows):
    """For consecutive main seeds, all 11th finite differences must vanish."""
    seq = [[tuple(z) for z in row] for row in rows]
    for _ in range(11):
        nxt = []
        for a, b in zip(seq[:-1], seq[1:]):
            nxt.append([(b[j][0] - a[j][0], b[j][1] - a[j][1]) for j in range(32)])
        seq = nxt
    return all(z == (0, 0) for row in seq for z in row)


def exact_lane(rows, lane, degree_control=False):
    rref, pivots = exact_rref(rows)
    rank = len(pivots)
    witness_q = null_witness_from_rref(rref, pivots, 32)
    witness = integerize(witness_q) if witness_q is not None else None
    verified = bool(witness is not None and verify_integer_null(rows, witness))
    degree_ok = finite_difference_degree10_control(rows) if degree_control else True
    scientific = "PASS" if rank == 32 else ("FAIL" if verified else "INVALID")
    return {
        "iteration": "Iter077J-SM",
        "repair": "exact-rank-control-only",
        "lane": lane,
        "execution_valid": bool(rank == 32 or verified),
        "scientific_outcome_under_original_contract": scientific,
        "rows": len(rows),
        "columns": 32,
        "exact_rank_Q_i": rank,
        "pivot_columns": pivots,
        "nullity": 32 - rank,
        "exact_right_null_witness_gaussian_integer": [[a, b] for a, b in witness] if witness else None,
        "witness_nonzero": bool(witness and any(z != (0, 0) for z in witness)),
        "witness_annihilates_all_rows_exactly": verified,
        "polynomial_degree_bound": 10,
        "polynomial_rank_upper_bound": 11,
        "rank_respects_polynomial_bound": rank <= 11,
        "eleventh_finite_difference_zero_on_main_family": degree_ok if degree_control else None,
    }


def lane_bx():
    rows = jbase.main_vectors()
    return exact_lane(rows, "Bx", degree_control=True)


def lane_cx():
    rows = jbase.main_vectors() + [jbase.full32_exact(jbase.ray(s)) for s in jbase.HELD_SEEDS]
    return exact_lane(rows, "Cx", degree_control=False)


def mod_ops(p):
    def gp(z): return (z[0] % p, z[1] % p)
    def zero(z): return z[0] % p == 0 and z[1] % p == 0
    def sub(a, b): return ((a[0] - b[0]) % p, (a[1] - b[1]) % p)
    def mul(a, b): return ((a[0] * b[0] - a[1] * b[1]) % p, (a[0] * b[1] + a[1] * b[0]) % p)
    def inv(a):
        den = (a[0] * a[0] + a[1] * a[1]) % p
        if den == 0:
            raise ZeroDivisionError
        qv = pow(den, p - 2, p)
        return (a[0] * qv % p, -a[1] * qv % p)
    return gp, zero, sub, mul, inv


def rank_mod(rows, p):
    gp, zero, sub, mul, inv = mod_ops(p)
    basis = []
    for row0 in rows:
        row = [gp(z) for z in row0]
        for piv, br in basis:
            if not zero(row[piv]):
                f = row[piv]
                row = [sub(x, mul(f, y)) for x, y in zip(row, br)]
        piv = next((j for j, z in enumerate(row) if not zero(z)), None)
        if piv is None:
            continue
        iv = inv(row[piv])
        row = [mul(iv, z) for z in row]
        newbasis = []
        for p0, br in basis:
            if not zero(br[piv]):
                f = br[piv]
                br = [sub(x, mul(f, y)) for x, y in zip(br, row)]
            newbasis.append((p0, br))
        basis = sorted(newbasis + [(piv, row)], key=lambda x: x[0])
        if len(basis) == 32:
            return 32
    return len(basis)


def relabelled_rows_exact():
    rows = []
    perms = list(itertools.permutations(range(5)))
    for s in jbase.MAIN_SEEDS[:8]:
        coords = jbase.ray(s)
        for perm in perms:
            rows.append(jbase.full32_exact(jbase.permute_regauge(coords, perm)))
    return rows


def lane_dx(prime):
    if prime not in FROZEN_PRIMES:
        raise SystemExit("prime not frozen")
    rows = relabelled_rows_exact()
    rank = rank_mod(rows, prime)
    return {
        "iteration": "Iter077J-SM",
        "repair": "exact-rank-control-only",
        "lane": "Dx",
        "prime": prime,
        "prime_mod_4": prime % 4,
        "vectors_checked": len(rows),
        "rank_Fp_i": rank,
        "interpretation": "EXACT_FULL_RANK_CERTIFICATE" if rank == 32 else "LOWER_BOUND_ONLY_NO_EXACT_DEFICIENCY_INFERENCE",
        "certifies_exact_Q_i_rank_32": rank == 32,
    }


def aggregate(root):
    bx = cx = None
    dx = {}
    for base_dir, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                obj = json.loads(Path(base_dir, fn).read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("iteration") != "Iter077J-SM" or obj.get("repair") != "exact-rank-control-only":
                continue
            if obj.get("lane") == "Bx": bx = obj
            elif obj.get("lane") == "Cx": cx = obj
            elif obj.get("lane") == "Dx": dx[str(obj.get("prime"))] = obj
    complete = bx is not None and cx is not None and set(map(int, dx.keys())) == set(FROZEN_PRIMES)
    if not complete:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_INCOMPLETE"
    elif not bx.get("execution_valid") or not cx.get("execution_valid"):
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_FAILED_EXACT_WITNESS"
    elif bx.get("exact_rank_Q_i") < 32 and bx.get("witness_annihilates_all_rows_exactly"):
        verdict = "FAIL_CONFIRMED"
        classification = "ITER077J_SM_FROZEN_MAIN_FULL32_ANGULAR_SPAN_EXACTLY_FAILS_CONTROL_REPAIR_SCOPED"
    elif bx.get("exact_rank_Q_i") == 32:
        verdict = "ORIGINAL_FAIL_INVALID"
        classification = "ITER077J_SM_ORIGINAL_MODULAR_FAIL_INVALIDATED_BY_EXACT_FULL_RANK"
    else:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ITER077J_SM_EXACT_RANK_CONTROL_REPAIR_UNRESOLVED"
    d_full = [int(p) for p, obj in dx.items() if obj.get("certifies_exact_Q_i_rank_32")]
    return {
        "iteration": "Iter077J-SM",
        "repair": "exact-rank-control-only",
        "execution_valid": complete and verdict != "INVALID_IMPLEMENTATION",
        "verdict": verdict,
        "classification": classification,
        "main_exact_rank_Q_i": bx.get("exact_rank_Q_i") if bx else None,
        "main_nullity": bx.get("nullity") if bx else None,
        "main_exact_null_witness_verified": bx.get("witness_annihilates_all_rows_exactly") if bx else None,
        "combined_exact_rank_Q_i": cx.get("exact_rank_Q_i") if cx else None,
        "combined_nullity": cx.get("nullity") if cx else None,
        "combined_exact_null_witness_verified": cx.get("witness_annihilates_all_rows_exactly") if cx else None,
        "frozen_polynomial_rank_upper_bound": 11,
        "d_modular_ranks": {p: obj.get("rank_Fp_i") for p, obj in sorted(dx.items())},
        "d_primes_certifying_exact_full_rank": d_full,
        "d_exact_deficiency_claim_allowed": False if not d_full else None,
        "interpretation_ceiling": "FAIL, if confirmed, is only for the frozen one-parameter main angular family. It does not establish a universal boundary-state cancellation over arbitrary collision directions or define the K5 boundary value.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("Bx", "Cx", "Dx"))
    ap.add_argument("--prime", type=int)
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        obj = aggregate(args.aggregate_dir)
    elif args.lane == "Bx":
        obj = lane_bx()
    elif args.lane == "Cx":
        obj = lane_cx()
    elif args.lane == "Dx":
        if args.prime is None:
            raise SystemExit("Dx requires --prime")
        obj = lane_dx(args.prime)
    else:
        raise SystemExit("choose lane or aggregate")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.aggregate_dir and not obj.get("execution_valid", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
