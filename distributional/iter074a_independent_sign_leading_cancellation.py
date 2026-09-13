#!/usr/bin/env python3
"""Iter074A: exact leading-power cancellation after the 64 independent-sign sum.

Prospectively frozen by status/ITERATION_074A_PREREG.md.
Reduced K4 denominator skeleton only.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

from distributional.iter073a_k4_signed_cutspace_face_atlas import EDGES, TREES, Lmat

Z = sp.symbols('z0:3', real=True)
EPS = sp.symbols('eps', positive=True, real=True)
EDGE_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}


def parity(perm):
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
    return -1 if inv % 2 else 1


def signed_edge_permutation(perm):
    Q = sp.zeros(6, 6)
    orientation_product = 1
    for e, (a, b) in enumerate(EDGES):
        aa, bb = perm[a], perm[b]
        ee = EDGE_INDEX[tuple(sorted((aa, bb)))]
        orient = 1 if aa < bb else -1
        Q[ee, e] = orient
        orientation_product *= orient
    return Q, orientation_product


def independent_rows(L):
    for rows in itertools.combinations(range(6), 3):
        B = L[list(rows), :]
        if B.det() != 0:
            return rows
    raise RuntimeError('rank-three row minor not found')


def induced_matrix(L, Q):
    rows = independent_rows(L)
    B = L[list(rows), :]
    C = (Q * L)[list(rows), :]
    M = sp.simplify(B.inv() * C)
    if L * M != Q * L:
        raise AssertionError('signed edge relabelling does not close on cycle space')
    return M


def sample_factorization(L):
    # Frozen exact rational points, selected to avoid zero edge forms for all bases.
    candidates = [
        (sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(11, 13), sp.Rational(3, 5)),
        (sp.Rational(7, 5), sp.Rational(-4, 9), sp.Rational(13, 8), sp.Rational(2, 7)),
        (sp.Rational(-5, 6), sp.Rational(17, 10), sp.Rational(9, 4), sp.Rational(5, 11)),
        (sp.Rational(8, 7), sp.Rational(3, 11), sp.Rational(-14, 9), sp.Rational(4, 13)),
    ]
    rows = []
    for a, b, c, eps in candidates:
        zv = sp.Matrix([a, b, c])
        xv = list(L * zv)
        if any(x == 0 for x in xv):
            continue
        direct = sp.Integer(0)
        for signs in itertools.product((1, -1), repeat=6):
            term = sp.Integer(1)
            for x, s in zip(xv, signs):
                term *= 1 / (x - sp.I * eps * s)
            direct += term
        fact = sp.prod(2 * x / (x * x + eps * eps) for x in xv)
        rows.append({'z': [str(a), str(b), str(c)], 'epsilon': str(eps),
                     'difference': str(sp.simplify(direct - fact))})
    return rows, bool(rows) and all(r['difference'] == '0' for r in rows)


def all_flats(L):
    flats = []
    for r in range(7):
        for S in itertools.combinations(range(6), r):
            B = L[list(S), :] if S else sp.zeros(0, 3)
            rank = int(B.rank())
            closure = []
            for e in range(6):
                C = sp.Matrix.vstack(B, L[e, :])
                if int(C.rank()) == rank:
                    closure.append(e)
            if tuple(closure) != tuple(S):
                continue
            q = 3 - rank
            if q <= 0:
                continue
            flats.append({'zero_edges': list(S), 'rank': rank, 'dimension': q,
                          'n_grow': 6 - len(S)})
    return flats


def moment_integrability(flats, d):
    bad = [f for f in flats if not (f['n_grow'] > d + f['dimension'])]
    return len(bad) == 0, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    one_edge = sp.simplify(1/(sp.Symbol('x')-sp.I*EPS) + 1/(sp.Symbol('x')+sp.I*EPS)
                           - 2*sp.Symbol('x')/(sp.Symbol('x')**2+EPS**2)) == 0

    basis_out = {}
    P1 = bool(one_edge)
    P2 = P3 = P4 = P5 = P7 = True
    degree2_open_all = True

    for tr in TREES:
        L, det_tree = Lmat(tr)
        sample_rows, sample_ok = sample_factorization(L)
        P1 &= sample_ok

        transforms = []
        reynolds = {str(1): sp.Integer(0), str(Z[0]): sp.Integer(0),
                    str(Z[1]): sp.Integer(0), str(Z[2]): sp.Integer(0)}
        edge_poly = sp.expand(sp.prod((L * sp.Matrix(Z))[e] for e in range(6)))
        edge_proj = sp.Integer(0)

        for perm in itertools.permutations(range(4)):
            Q, chi = signed_edge_permutation(perm)
            M = induced_matrix(L, Q)
            p = parity(perm)
            integer_M = all(v.is_Integer for v in M)
            unimod = abs(int(M.det())) == 1
            P2 &= bool(integer_M and unimod and L*M == Q*L)
            P3 &= bool(chi == p)

            mz = M * sp.Matrix(Z)
            monoms = [sp.Integer(1), Z[0], Z[1], Z[2]]
            for q in monoms:
                q_sub = sp.expand(q.subs({Z[i]: mz[i] for i in range(3)}, simultaneous=True))
                reynolds[str(q)] += chi * q_sub
            p_sub = sp.expand(edge_poly.subs({Z[i]: mz[i] for i in range(3)}, simultaneous=True))
            edge_proj += chi * p_sub
            transforms.append({'perm': list(perm), 'parity': p, 'chi': chi,
                               'det_M': int(M.det()),
                               'M': [[int(M[i,j]) for j in range(3)] for i in range(3)]})

        reynolds = {k: sp.expand(v) for k, v in reynolds.items()}
        basis_p4 = all(v == 0 for v in reynolds.values())
        P4 &= basis_p4

        # QL=LM and chi=product orientation signs imply the full rational identity
        # F(Mz)=chi F(z) factor-by-factor, without unsafe rational expansion.
        basis_p3 = all(t['chi'] == t['parity'] for t in transforms)
        P3 &= basis_p3

        flats = all_flats(L)
        d0, bad0 = moment_integrability(flats, 0)
        d1, bad1 = moment_integrability(flats, 1)
        d2, bad2 = moment_integrability(flats, 2)
        P5 &= bool(d0 and d1)
        degree2_open_all &= bool((not d2) and len(bad2) > 0)

        edge_proj = sp.expand(edge_proj)
        basis_p7 = edge_proj != 0
        P7 &= basis_p7

        basis_out[tr] = {
            'tree_det': det_tree,
            'sample_64term_checks': sample_rows,
            'transforms': transforms,
            'degree0_1_reynolds': {k: str(v) for k, v in reynolds.items()},
            'flat_census': flats,
            'degree0_absolutely_integrable': d0,
            'degree1_absolutely_integrable': d1,
            'degree2_absolutely_integrable': d2,
            'degree2_obstructing_flats': bad2,
            'degree6_negative_control_projection': str(edge_proj),
            'degree6_negative_control_nonzero': basis_p7,
        }

    P6 = bool(degree2_open_all)
    passed = bool(P1 and P2 and P3 and P4 and P5 and P6 and P7)
    out = {
        'iteration': 'Iter074A',
        'frozen_prereg_commit': '419804b9f395ddc3181d3c8ecbc539830036c527',
        'predicates': {
            'P1_FIXED_EPSILON_64SIGN_FACTORIZATION_EXACT': P1,
            'P2_S4_CYCLESPACE_ACTION_UNIMODULAR_EXACT': P2,
            'P3_ALTERNATING_EDGE_CHARACTER_EXACT': P3,
            'P4_DEGREE0_1_ALTERNATING_REYNOLDS_ZERO': P4,
            'P5_DEGREE0_1_MOMENTS_ABSOLUTELY_INTEGRABLE': P5,
            'P6_DEGREE2_FIRST_OVERLAP_OPEN_BY_FLAT_POWERCOUNT': P6,
            'P7_ALTERNATING_PROJECTOR_NEGATIVE_CONTROL_NONZERO': P7,
        },
        'classification': ('ITER074A_64SIGN_EPSM3_EPSM2_CANCEL_EXACT_EPSM1_OVERLAP_OPEN_SCOPED'
                           if passed else 'ITER074A_64SIGN_LEADING_CANCELLATION_FAIL'),
        'scientific_summary': (
            'In the reduced independent-wedge common-epsilon denominator family, the full-collision '
            'epsilon^-3 constant and epsilon^-2 linear local coefficients vanish exactly after the 64-sign '
            'sum by S4 alternating symmetry, provided the exact flat power count certifies absolute moment '
            'integrability. The nominal epsilon^-1 quadratic moment is left overlap-open when degree-2 '
            'absolute integrability fails on arrangement flats.'
        ),
        'basis': basis_out,
        'claim_lock': ('Reduced denominator skeleton only. No distributional Eq.(5)/(6), full Toller vertex, '
                       'physical finiteness theorem, K5/G3/F9/G8 promotion, complete QG or new physics.'),
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True), encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k != 'basis'}, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(9)


if __name__ == '__main__':
    main()
