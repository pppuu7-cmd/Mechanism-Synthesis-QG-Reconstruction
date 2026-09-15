#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MODULE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
GENERAL_ENGINE = ROOT / 'scripts/k5_order8_nonuniform_schwinger_sign_diagnostic.py'
RANKONE_ENGINE = ROOT / 'scripts/k5_order8_edge01_rankone_positivity.py'
DERIVATION = ROOT / 'sources/K5_ORDER8_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_DERIVATION.md'
PREREG_COMMIT = 'ef26d063354d0def5af3fdba4fe0d8b537a038d1'

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))

POSITIVE_CLASS = 'K5_EDGE01_EDGE02_RANKTWO_RADIAL_MOMENT_POSITIVE_ALL_TU_GT0_EXACT_SCOPED'
SIGN_CHANGE_CLASS = 'K5_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_EXACT_SCOPED'
ZERO_CLASS = 'K5_EDGE01_EDGE02_RANKTWO_ZERO_WITNESS_EXACT_SCOPED'
INCONCLUSIVE_CLASS = 'K5_EDGE01_EDGE02_RANKTWO_INCONCLUSIVE_SCOPED'
INVALID_CLASS = 'INVALID_IMPLEMENTATION'

PREREG_POINTS = (
    (Fraction(1), Fraction(1)),
    (Fraction(2), Fraction(1)),
    (Fraction(1), Fraction(2)),
    (Fraction(1, 2), Fraction(1)),
    (Fraction(1), Fraction(1, 2)),
    (Fraction(2), Fraction(3)),
    (Fraction(3), Fraction(2)),
    (Fraction(1, 2), Fraction(3, 2)),
    (Fraction(3, 2), Fraction(1, 2)),
)
POST_PREREG_NEGATIVE_WITNESS = (Fraction(1), Fraction(3))


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def fq(q: Fraction):
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def gz(z):
    return [fq(z[0]), fq(z[1])]


def point_key(t: Fraction, u: Fraction) -> str:
    return f'{fq(t)},{fq(u)}'


def classify(values, *, source_choice_count, prereg_complete, all_pd, exact_crosschecks,
             global_positive_certificate=False):
    if source_choice_count != 1024 or not prereg_complete or not all_pd or not exact_crosschecks:
        return INVALID_CLASS
    if any(z == ZERO for z in values):
        return ZERO_CLASS
    if any(z[1] != 0 for z in values):
        return INCONCLUSIVE_CLASS
    signs = {1 if z[0] > 0 else -1 for z in values if z[0] != 0}
    if signs == {1, -1}:
        return SIGN_CHANGE_CLASS
    if global_positive_certificate and signs == {1}:
        return POSITIVE_CLASS
    return INCONCLUSIVE_CLASS


def symbolic_det_ranktwo(general, rows):
    # Entries are bilinear polynomials in (t,u), encoded as dict[(i,j)] -> coeff.
    # L(t,u)=L0+(t-1)r01r01^T+(u-1)r02r02^T.
    L0 = general.build_L((Fraction(1),) * 10, rows)
    r0, r1 = rows[0], rows[1]

    def padd(a, b):
        out = dict(a)
        for k, v in b.items():
            out[k] = out.get(k, Fraction(0)) + v
            if out[k] == 0:
                del out[k]
        return out

    def pmul(a, b):
        out = {}
        for (i, j), x in a.items():
            for (k, l), y in b.items():
                key = (i + k, j + l)
                out[key] = out.get(key, Fraction(0)) + x * y
        return {k: v for k, v in out.items() if v}

    entries = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # constant after replacing alpha01=t, alpha02=u
            c = L0[i][j] - Fraction(r0[i] * r0[j]) - Fraction(r1[i] * r1[j])
            p = {(0, 0): c}
            if r0[i] * r0[j]:
                p = padd(p, {(1, 0): Fraction(r0[i] * r0[j])})
            if r1[i] * r1[j]:
                p = padd(p, {(0, 1): Fraction(r1[i] * r1[j])})
            entries[i][j] = p

    import itertools
    det = {}
    for p in itertools.permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        term = {(0, 0): Fraction(-1 if inv % 2 else 1)}
        for i in range(4):
            term = pmul(term, entries[i][p[i]])
        det = padd(det, term)
    return det


def full_source_F_target(rankone, mod, edges, rows, target_index: int):
    # Independent generalization of the rank-one source contraction to an arbitrary
    # target edge. This derives the t=1 / edge02 slice from all 1024 source terms.
    L0 = rankone.build_L((Fraction(1),) * 10, rows)
    B0 = rankone.mat_inv(L0)
    C0 = [[rankone.dot_mat(rows[i], B0, rows[j]) for j in range(10)] for i in range(10)]
    c = C0[target_index][target_index]
    v = [C0[i][target_index] for i in range(10)]
    entry = rankone.entry_coeff_from_source(mod)
    pats = rankone.selected_patterns(mod, edges)

    pair = {}
    for i in range(10):
        for j in range(i + 1, 10):
            cov = [C0[i][j], -v[i] * v[j]] + [Fraction(0)] * (rankone.UORD - 1)
            for ea in entry:
                for eb in entry:
                    gd = rankone.gdot(entry[ea], entry[eb])
                    pair[(i, j, ea, eb)] = [rankone.gscale(x, gd) for x in cov]

    cache = {}

    def wick(rem):
        if not rem:
            return [ONE] + [ZERO] * rankone.UORD
        if rem in cache:
            return cache[rem]
        i, ei = rem[0]
        total = [ZERO] * (rankone.UORD + 1)
        for pos in range(1, len(rem)):
            j, ej = rem[pos]
            rest = rem[1:pos] + rem[pos + 1:]
            total = rankone.pcs_add(
                total,
                rankone.pcs_mul(pair[(i, j, ei, ej)], wick(rest), rankone.UORD),
                rankone.UORD,
            )
        cache[rem] = total
        return total

    F = [ZERO] * (rankone.UORD + 1)
    for entries, coeff in pats:
        rem = tuple((i, entries[i]) for i in range(10))
        F = rankone.pcs_add(F, rankone.pcs_scale(wick(rem), Fraction(coeff)), rankone.UORD)
    return F, c, len(pats), len(cache)


def evaluate_full_point(general, t, u, rows, Q, pats):
    alphas = (Fraction(t), Fraction(u)) + (Fraction(1),) * 8
    return general.evaluate_point(alphas, rows, Q, pats)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    mod = load(SOURCE_MODULE, 'iter077i_source_ranktwo')
    general = load(GENERAL_ENGINE, 'general_ranktwo')
    rankone = load(RANKONE_ENGINE, 'rankone_parent')

    edges = tuple(mod.EDGES)
    expected_edges = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4))
    rows = tuple(general.incidence_row(e) for e in edges)
    pats = general.selected_patterns(mod, edges)
    Luni = general.build_L((Fraction(1),) * 10, rows)
    Q = general.mat_scale(Luni, Fraction(1, 5))

    # Exact rank-two determinant and uniform two-edge covariance Gram controls.
    det_poly = symbolic_det_ranktwo(general, rows)
    expected_det = {
        (0, 0): Fraction(40),
        (1, 0): Fraction(35),
        (0, 1): Fraction(35),
        (1, 1): Fraction(15),
    }
    B0 = general.mat_inv(Luni)
    gram = (
        (general.dot_mat(rows[0], B0, rows[0]), general.dot_mat(rows[0], B0, rows[1])),
        (general.dot_mat(rows[1], B0, rows[0]), general.dot_mat(rows[1], B0, rows[1])),
    )

    # Independently reconstruct the edge02 rank-one slice from all source terms.
    F02, c02, slice_choice_count, slice_cache_count = full_source_F_target(rankone, mod, edges, rows, 1)
    F02_expected_real = [
        Fraction(128, 625),
        Fraction(-1024, 3125),
        Fraction(1984, 15625),
        Fraction(-896, 78125),
        Fraction(0),
        Fraction(0),
    ]
    F02_real = [z[0] for z in F02]
    F02_imag_zero = all(z[1] == 0 for z in F02)

    # Reconstruct the exact t=1 radial numerator from source-derived F02.
    degree_bound = 7
    xs = list(range(1, degree_bound + 2))
    ys = [rankone.radial_from_F(x, F02_real, c02) * Fraction((2*x + 3)**degree_bound) for x in xs]
    qcoeff = rankone.solve_vandermonde(xs, ys, degree_bound)
    scalarP02, primitiveP02 = rankone.primitive_integer_polynomial(qcoeff)
    expected_scalarP02 = Fraction(1344, 78125)
    expected_primitiveP02 = [
        15347529,
        18446466,
        6476985,
        -1743180,
        -2084965,
        -625974,
        -66861,
        0,
    ]

    specialized_positive = rankone.radial_from_F(Fraction(2), F02_real, c02)
    specialized_negative = rankone.radial_from_F(Fraction(3), F02_real, c02)
    expected_positive = Fraction(1254383808, 9191328125)
    expected_negative = Fraction(-14327118848, 13839609375)

    # Full general-L exact engine: all nine prospectively frozen points plus the
    # post-prereg negative witness. These are independent of the specialized slice.
    all_points = tuple(PREREG_POINTS) + (POST_PREREG_NEGATIVE_WITNESS,)
    full = {}
    for t, u in all_points:
        full[(t, u)] = evaluate_full_point(general, t, u, rows, Q, pats)

    prereg_rows = []
    for t, u in PREREG_POINTS:
        r = full[(t, u)]
        prereg_rows.append({
            't': fq(t),
            'u': fq(u),
            'positive_definite': bool(r['positive_definite']),
            'det_L': fq(r['det_L']),
            'radial_probe': gz(r['radial_probe_fourth_derivative_zero_equivalent']),
        })

    pos_full = full[(Fraction(1), Fraction(2))]['radial_probe_fourth_derivative_zero_equivalent']
    neg_full = full[POST_PREREG_NEGATIVE_WITNESS]['radial_probe_fourth_derivative_zero_equivalent']

    all_pd = all(r['positive_definite'] for r in full.values())
    prereg_complete = len(prereg_rows) == 9
    exact_crosschecks = (
        pos_full == (expected_positive, Fraction(0))
        and neg_full == (expected_negative, Fraction(0))
        and specialized_positive == expected_positive
        and specialized_negative == expected_negative
    )

    actual_values = [r['radial_probe_fourth_derivative_zero_equivalent'] for r in full.values()]
    actual_classification = classify(
        actual_values,
        source_choice_count=len(pats),
        prereg_complete=prereg_complete,
        all_pd=all_pd,
        exact_crosschecks=exact_crosschecks,
        global_positive_certificate=False,
    )

    # Same-path positive fixture demonstrates that the positive branch is reachable
    # when an external exact positivity certificate is supplied.
    positive_fixture = classify(
        [(Fraction(1), Fraction(0)), (Fraction(2), Fraction(0))],
        source_choice_count=1024,
        prereg_complete=True,
        all_pd=True,
        exact_crosschecks=True,
        global_positive_certificate=True,
    ) == POSITIVE_CLASS

    # Malformed source-removal control: the same decision path must reject a 1023-term lane.
    removed_source_term_rejected = classify(
        [pos_full, neg_full],
        source_choice_count=1023,
        prereg_complete=True,
        all_pd=True,
        exact_crosschecks=True,
    ) == INVALID_CLASS

    # Malformed coefficient control: flip one exact F02 coefficient. Its specialized
    # witness must no longer agree with the independently computed full general engine,
    # and the same decision path rejects the failed exact-crosscheck candidate.
    bad_F02 = list(F02_real)
    bad_F02[1] = -bad_F02[1]
    bad_specialized_positive = rankone.radial_from_F(Fraction(2), bad_F02, c02)
    bad_exact_crosscheck = bad_specialized_positive == pos_full[0]
    flipped_coefficient_rejected = classify(
        [pos_full, neg_full],
        source_choice_count=1024,
        prereg_complete=True,
        all_pd=True,
        exact_crosschecks=bad_exact_crosscheck,
    ) == INVALID_CLASS

    derivation_text = DERIVATION.read_text(encoding='utf-8')
    locks = {
        'prereg_commit_locked': PREREG_COMMIT in derivation_text,
        'derivation_has_positive_witness': '1254383808/9191328125' in derivation_text,
        'derivation_has_negative_witness': '-14327118848/13839609375' in derivation_text,
        'derivation_keeps_full_period_open': 'does **not** imply that the 9-dimensional projective period vanishes' in derivation_text,
    }

    checks = {
        'authoritative_edge_order': edges == expected_edges,
        'all_1024_source_choices': len(pats) == 1024 and slice_choice_count == 1024,
        'uniform_two_edge_gram_exact': gram == ((Fraction(2,5), Fraction(1,5)), (Fraction(1,5), Fraction(2,5))),
        'ranktwo_determinant_polynomial_exact': det_poly == expected_det,
        'edge02_effective_covariance_2_over_5': c02 == Fraction(2,5),
        'edge02_source_F_imaginary_zero': F02_imag_zero,
        'edge02_source_F_exact': F02_real == F02_expected_real,
        'edge02_radial_scalar_exact': scalarP02 == expected_scalarP02,
        'edge02_radial_primitive_polynomial_exact': primitiveP02 == expected_primitiveP02,
        'all_nine_preregistered_points_evaluated': prereg_complete,
        'all_ten_full_engine_points_positive_definite': all_pd,
        'positive_witness_full_engine_exact': pos_full == (expected_positive, Fraction(0)),
        'negative_witness_full_engine_exact': neg_full == (expected_negative, Fraction(0)),
        'specialized_and_full_engine_witnesses_agree': exact_crosschecks,
        'actual_classification_is_frozen_sign_change': actual_classification == SIGN_CHANGE_CLASS,
        'derivation_locks_present': all(locks.values()),
        'no_parent_k5_zero_nonzero_verdict': True,
    }

    controls = {
        'synthetic_positive_fixture_passes_same_classifier': positive_fixture,
        'removed_source_term_rejected_same_classifier': removed_source_term_rejected,
        'flipped_F02_coefficient_changes_witness': bad_specialized_positive != pos_full[0],
        'flipped_coefficient_rejected_same_classifier': flipped_coefficient_rejected,
        'sign_change_not_promoted_to_full_period_zero': True,
    }

    implementation_valid = all(checks.values()) and all(controls.values())
    status = 'PASS_EXACT_SCOPED' if implementation_valid else 'INVALID_IMPLEMENTATION'
    classification = actual_classification if implementation_valid else INVALID_CLASS

    out = {
        'gate': 'K5_ORDER8_EDGE01_EDGE02_RANKTWO_POSITIVITY_LANE',
        'prereg_commit': PREREG_COMMIT,
        'status': status,
        'classification': classification,
        'checks': checks,
        'controls': controls,
        'source_choice_terms': len(pats),
        'edge02_slice_wick_cache_states': slice_cache_count,
        'uniform_two_edge_covariance_gram': [[fq(x) for x in row] for row in gram],
        'det_L_bivariate_polynomial': {
            'constant': 40,
            't': 35,
            'u': 35,
            't_u': 15,
            'factorized': '5*(3*t*u+7*t+7*u+8)',
        },
        'edge02_source_F_coefficients_z0_to_z5': [[fq(z[0]), fq(z[1])] for z in F02],
        'edge02_radial_scalar': fq(scalarP02),
        'edge02_radial_primitive_coefficients_u0_up': primitiveP02,
        'preregistered_full_engine_points': prereg_rows,
        'positive_witness': {
            'point': ['1', '2'],
            'value': gz(pos_full),
        },
        'negative_witness': {
            'point': ['1', '3'],
            'value': gz(neg_full),
        },
        'scientific_k5_zero_nonzero_verdict': None,
        'interpretation': {
            'pointwise_positive_ranktwo_certificate_falsified': classification == SIGN_CHANGE_CLASS,
            'sign_change_proves_full_projective_period_zero': False,
            'sign_change_proves_full_projective_period_nonzero': False,
            'next': 'exact invariant-dual projective integration/IBP or another genuine noncancellation certificate; do not continue mechanical higher-rank positivity lanes',
        },
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if implementation_valid else 2


if __name__ == '__main__':
    raise SystemExit(main())
