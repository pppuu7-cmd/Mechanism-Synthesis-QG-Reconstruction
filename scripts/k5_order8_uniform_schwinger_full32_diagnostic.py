#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MODULE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'


def load_source():
    spec = importlib.util.spec_from_file_location('iter077i_source', SOURCE_MODULE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def inv_fraction(A):
    n = len(A)
    a = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if a[i][c])
        a[c], a[p] = a[p], a[c]
        z = a[c][c]
        a[c] = [x / z for x in a[c]]
        for i in range(n):
            if i == c:
                continue
            z = a[i][c]
            if z:
                a[i] = [x - z*y for x, y in zip(a[i], a[c])]
    return [row[n:] for row in a]


def incidence_row(edge):
    a, b = edge
    row = [0, 0, 0, 0]
    if a != 0:
        row[a-1] -= 1
    if b != 0:
        row[b-1] += 1
    return tuple(row)


def dot_mat(r, M, s):
    return sum(Fraction(r[i]) * M[i][j] * Fraction(s[j]) for i in range(4) for j in range(4))


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gmul(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])


def gscale(q, z):
    return (q*z[0], q*z[1])


def gdot(a, b):
    # Complex bilinear dot product, not Hermitian: Wick contraction is algebraic.
    out = (Fraction(0), Fraction(0))
    for x, y in zip(a, b):
        out = gadd(out, gmul(x, y))
    return out


# Coefficient vectors of M(v) entries in (vx,vy,vz), Gaussian-integer exact.
ENTRY_COEFF = {
    (0,0): ((0,0),(0,0),(1,0)),
    (0,1): ((-1,0),(0,-1),(0,0)),
    (1,0): ((-1,0),(0,1),(0,0)),
    (1,1): ((0,0),(0,0),(-1,0)),
}


def all_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for tail in all_matchings(rest):
            yield ((a,b),) + tail


def frac_json(q):
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def gaussian_json(z):
    return [frac_json(z[0]), frac_json(z[1])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    mod = load_source()
    edges = tuple(mod.EDGES)
    rows = [incidence_row(e) for e in edges]

    L = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for r in rows:
        for i in range(4):
            for j in range(4):
                L[i][j] += r[i]*r[j]
    Linv = inv_fraction(L)
    edge_cov = [[dot_mat(rows[i], Linv, rows[j]) for j in range(10)] for i in range(10)]

    matchings = list(all_matchings(range(10)))
    surviving = [m for m in matchings if all(edge_cov[a][b] != 0 for a,b in m)]

    pair_tensor = {}
    for a in range(10):
        for b in range(a+1,10):
            c = edge_cov[a][b]
            for ea in ENTRY_COEFF:
                for eb in ENTRY_COEFF:
                    pair_tensor[(a,b,ea,eb)] = gscale(c, gdot(ENTRY_COEFF[ea], ENTRY_COEFF[eb]))

    wick_cache = {}
    def wick(entry_types):
        key = tuple(entry_types)
        if key in wick_cache:
            return wick_cache[key]
        total = (Fraction(0), Fraction(0))
        for matching in surviving:
            z = (Fraction(1), Fraction(0))
            for a,b in matching:
                z = gmul(z, pair_tensor[(a,b,entry_types[a],entry_types[b])])
                if z == (0,0):
                    break
            total = gadd(total, z)
        wick_cache[key] = total
        return total

    boundary = []
    total_choice_terms = 0
    for ks in itertools.product((0,1), repeat=5):
        total = (Fraction(0), Fraction(0))
        choices_count = 0
        opts = [mod.NODE_OPTIONS[k] for k in ks]
        for choices in itertools.product(*opts):
            choices_count += 1
            states = []
            coeff = 1
            for state, c in choices:
                states.append(state)
                coeff *= c
            entry_types = []
            for a,b in edges:
                row = states[b][mod.LEG_POS[(b,a)]]
                col = states[a][mod.LEG_POS[(a,b)]]
                entry_types.append((row,col))
            z = wick(entry_types)
            total = gadd(total, gscale(Fraction(coeff), z))
        total_choice_terms += choices_count
        boundary.append({
            'boundary_k': list(ks),
            'choice_terms': choices_count,
            'gaussian_N10_moment_zero_equivalent': gaussian_json(total),
            'nonzero': total != (0,0),
        })

    nonzero = sum(int(r['nonzero']) for r in boundary)

    # Source radial probe P8=(R_K5^2)^4.  At alpha_e=1,
    # S=sum_e |v_e|^2 = 5 R_K5^2.  For homogeneous N10 in d=12,
    # integral N10*S^4*exp(-S) = (11)_4 integral N10*exp(-S).
    radial_factor = Fraction(11*12*13*14, 5**4)
    radial_boundary = []
    for r in boundary:
        re, im = r['gaussian_N10_moment_zero_equivalent']
        def parse(v):
            if isinstance(v, int):
                return Fraction(v)
            n,d = v.split('/')
            return Fraction(int(n),int(d))
        z=(parse(re),parse(im))
        rz=gscale(radial_factor,z)
        radial_boundary.append({
            'boundary_k':r['boundary_k'],
            'radial_probe_moment_zero_equivalent':gaussian_json(rz),
            'nonzero':rz!=(0,0),
        })

    # Controls are derived from recomputed objects.
    disjoint_nonzero = []
    adjacent_values = set()
    diagonal_values = set()
    for i,e in enumerate(edges):
        diagonal_values.add(edge_cov[i][i])
        for j in range(i+1,10):
            if set(e).isdisjoint(edges[j]):
                if edge_cov[i][j] != 0:
                    disjoint_nonzero.append((i,j))
            else:
                adjacent_values.add(abs(edge_cov[i][j]))

    checks = {
        'full32_components': len(boundary)==32,
        'all_source_choice_terms_counted': total_choice_terms == 100000,
        'all_945_matchings_enumerated': len(matchings)==945,
        'sparse_surviving_matching_count_144': len(surviving)==144,
        'disjoint_edge_covariances_zero': not disjoint_nonzero,
        'single_adjacent_covariance_magnitude': len(adjacent_values)==1,
        'single_diagonal_covariance_value': len(diagonal_values)==1,
        'radial_factor_nonzero': radial_factor != 0,
        'no_scientific_period_verdict_from_point_diagnostic': True,
    }

    out = {
        'gate':'K5_ORDER8_UNIFORM_SCHWINGER_FULL32_DIAGNOSTIC',
        'parent_scientific_gate':'ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE',
        'status':'DIAGNOSTIC_EXACT' if all(checks.values()) else 'INVALID_IMPLEMENTATION',
        'checks':checks,
        'edge_covariance_matrix':[[frac_json(x) for x in row] for row in edge_cov],
        'perfect_matchings_total':len(matchings),
        'perfect_matchings_surviving':len(surviving),
        'wick_cache_size':len(wick_cache),
        'source_choice_terms_total':total_choice_terms,
        'boundary_components_nonzero_gaussian_N10_moment':nonzero,
        'boundary_components_zero_gaussian_N10_moment':32-nonzero,
        'radial_probe_factor_11_12_13_14_over_5pow4':frac_json(radial_factor),
        'boundary_gaussian_N10':boundary,
        'boundary_radial_probe':radial_boundary,
        'scientific_k5_zero_nonzero_verdict':None,
        'interpretation':{
            'uniform_projective_integrand_identically_zero_excluded_if_any_nonzero':nonzero>0,
            'uniform_point_nonzero_does_not_prove_projective_period_nonzero':True,
            'next_if_nonzero':'derive invariant-dual full projective integrand and seek exact sign/IBP certificate',
            'next_if_all_zero':'identify exact uniform-point cancellation and test nonuniform rational Schwinger points',
        },
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if all(checks.values()) else 2


if __name__=='__main__':
    raise SystemExit(main())
