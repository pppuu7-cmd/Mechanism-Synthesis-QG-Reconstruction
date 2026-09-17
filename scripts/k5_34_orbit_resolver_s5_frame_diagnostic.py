#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
PREREG = ROOT / 'prereg/K5_34_ORBIT_RESOLVER_REPAIR1_S5_FRAME_DIAGNOSTIC.md'
PREREG_COMMIT = 'fb648ab3b5c5430840c8025ceb31500252c080cc'
CONFIRMED = 'K5_34_ORBIT_RESOLVER_S5_LABEL_FRAME_MISMATCH_CONFIRMED_EXACT_CONTROL'
NOT_CONFIRMED = 'K5_34_ORBIT_RESOLVER_S5_LABEL_FRAME_HYPOTHESIS_NOT_CONFIRMED_EXACT_CONTROL'
INVALID = 'INVALID_IMPLEMENTATION'


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


c = load(CORE, 'k5_34_frame_diag_core')
s5 = c.s5
P = s5.C
PINV = s5.invperm(P)


def dictvec_equal(a, b):
    return len(a) == len(b) and all(x == y for x, y in zip(a, b))


def hash_dictvec(v):
    return s5.dictvec_hash(v)


def match_hash(mc):
    return c._match_coeff_hash(mc)


def explicit_target_key(types, p):
    out = [None] * 10
    for old in range(10):
        target = s5.ep(p, old)
        t = types[old]
        if s5.edge_sign(p, old) == -1:
            t = (t[1], t[0])
        out[target] = t
    assert all(x is not None for x in out)
    return tuple(out)


def explicit_target_dicts(base, p):
    g_source = s5.orientation_character(p)
    out = []
    for d in base:
        z = defaultdict(Fraction)
        for types, coeff in d.items():
            z[explicit_target_key(types, p)] += g_source * Fraction(coeff)
        out.append({k: v for k, v in z.items() if v})
    return out


def permute_matching(mt, p):
    pairs = []
    for i, j in mt:
        a = s5.ep(p, i)
        b = s5.ep(p, j)
        pairs.append((min(a, b), max(a, b)))
    return tuple(sorted(pairs))


def push_matching_coeff(mc, p):
    out = {}
    for mt, coeffs in mc.items():
        k = permute_matching(mt, p)
        assert k not in out
        out[k] = coeffs
    return out


def exact_rational_match_coeff(mc):
    return all(isinstance(x, Fraction) for coeffs in mc.values() for ch in coeffs for x in ch)


def same_poly(a, b):
    return a.d == b.d


def lane_equal(a, b):
    checks = {}
    for ch in (0, 1):
        checks[f'ch{ch+1}_N'] = same_poly(a['channels'][ch]['N'], b['channels'][ch]['N'])
        checks[f'ch{ch+1}_B'] = same_poly(a['channels'][ch]['B'], b['channels'][ch]['B'])
    return checks


def route_hashes(a):
    return {
        f'ch{ch+1}_{obj}': c.vector_hash(a['channels'][ch][obj], c.N_DEG if obj == 'N' else c.B_DEG)
        for ch in (0, 1) for obj in ('N', 'B')
    }


def mutate_one_matching(mc):
    out = dict(mc)
    k = sorted(out)[0]
    coeffs = [[list(ch) for ch in out[k]]][0]
    # Copy into mutable nested pairs: [[re,im],[re,im]].
    coeffs = [list(ch) for ch in out[k]]
    coeffs[0][0] = Fraction(coeffs[0][0]) + 1
    out[k] = (tuple(coeffs[0]), tuple(coeffs[1]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    prereg_text = PREREG.read_text(encoding='utf-8')
    base_patterns = c._BASE_PATTERNS
    assert c._SOURCE_TERM_COUNT == 100000

    current_pullback = s5.transported_pattern_dicts(
        base_patterns, P,
        transpose_reversed=True,
        source_reversal_sign=True,
        covariance_orientation_sign=False,
    )
    explicit_target = explicit_target_dicts(base_patterns, P)
    inverse_helper_target = s5.transported_pattern_dicts(
        base_patterns, PINV,
        transpose_reversed=True,
        source_reversal_sign=True,
        covariance_orientation_sign=False,
    )

    current_mc = c._project_pattern_dicts_to_match_coeff(current_pullback)
    target_mc = c._project_pattern_dicts_to_match_coeff(explicit_target)
    inverse_mc = c._project_pattern_dicts_to_match_coeff(inverse_helper_target)
    pushed_base_mc = push_matching_coeff(c.MATCH_COEFF, P)

    mask = 1
    mp = c.core.pmask(mask, P)
    original = c.route_a(mask, c.W1)
    target_route = c.route_a(mp, c.WP1, target_mc)
    current_route = c.route_a(mp, c.WP1, current_mc)
    source_fixed_route = c.route_a(mp, c.WP1, c.MATCH_COEFF)
    altered_route = c.route_a(mp, c.WP1, mutate_one_matching(target_mc))

    eq_target = lane_equal(original, target_route)
    eq_current = lane_equal(original, current_route)
    eq_fixed = lane_equal(original, source_fixed_route)
    eq_altered = lane_equal(original, altered_route)

    edge_bijection = sorted(s5.ep(P, i) for i in range(10)) == list(range(10))
    inverse_roundtrip = all(s5.ep(PINV, s5.ep(P, i)) == i for i in range(10))

    D = {
        'D1_edge_bijection_inverse_roundtrip': edge_bijection and inverse_roundtrip,
        'D2_full32_100000_exact_rational_constructions': (
            len(current_pullback) == len(explicit_target) == 32
            and c._SOURCE_TERM_COUNT == 100000
            and exact_rational_match_coeff(current_mc)
            and exact_rational_match_coeff(target_mc)
        ),
        'D3_explicit_target_equals_inverse_helper_target_full32': dictvec_equal(explicit_target, inverse_helper_target),
        'D4_target_matching_support945_equals_pushed_base': len(target_mc) == 945 and target_mc == pushed_base_mc,
        'D5_current_pullback_frame_distinct_from_explicit_target': (
            not dictvec_equal(current_pullback, explicit_target)
            or current_mc != target_mc
        ),
        'D6_target_frame_route_full_N_B_equality_mask1_W1': all(eq_target.values()),
        'D7_current_pullback_not_valid_as_target_route_mask1_W1': not all(eq_current.values()),
        'D8_source_fixed_rejected_mask1_W1': not all(eq_fixed.values()),
        'D9_altered_matching_rejected_mask1_W1': not all(eq_altered.values()),
    }

    validity = {
        'prereg_commit_locked': PREREG_COMMIT == 'fb648ab3b5c5430840c8025ceb31500252c080cc',
        'prereg_present': 'S5 label frame' in prereg_text,
        'parent_prereg_locked': c.PRE == 'd6b0e805101c8590eafac71398cc2b1466691752',
        'repair1_source_terms_100000': c._SOURCE_TERM_COUNT == 100000,
        'base_matching_support_945': len(c.MATCH_COEFF) == 945,
        'target_matching_support_945': len(target_mc) == 945,
        'current_matching_exact_rational': exact_rational_match_coeff(current_mc),
        'target_matching_exact_rational': exact_rational_match_coeff(target_mc),
        'inverse_matching_exact_rational': exact_rational_match_coeff(inverse_mc),
        'route_internal_checks_original': all(original['checks'].values()),
        'route_internal_checks_target': all(target_route['checks'].values()),
        'route_internal_checks_current': all(current_route['checks'].values()),
        'route_internal_checks_source_fixed': all(source_fixed_route['checks'].values()),
        'route_internal_checks_altered': all(altered_route['checks'].values()),
        'mandatory_source_fixed_discriminates': D['D8_source_fixed_rejected_mask1_W1'],
        'mandatory_altered_matching_discriminates': D['D9_altered_matching_rejected_mask1_W1'],
    }

    if not all(validity.values()):
        classification = INVALID
        status = INVALID
    elif all(D.values()):
        classification = CONFIRMED
        status = 'PASS_EXACT_CONTROL'
    else:
        classification = NOT_CONFIRMED
        status = 'PASS_EXACT_CONTROL_DIAGNOSTIC_NEGATIVE'

    out = {
        'gate': 'K5_34_ORBIT_RESOLVER_REPAIR1_S5_FRAME_DIAGNOSTIC',
        'prereg_commit': PREREG_COMMIT,
        'status': status,
        'classification': classification,
        'scientific_coefficient_verdict': None,
        'cycle': list(P),
        'cycle_inverse': list(PINV),
        'orientation_character_cycle': s5.orientation_character(P),
        'diagnostic_obligations': D,
        'validity': validity,
        'route_equality_booleans': {
            'target': eq_target,
            'current_pullback': eq_current,
            'source_fixed': eq_fixed,
            'altered_target': eq_altered,
        },
        'hashes_only': {
            'base_pattern_dictvec_sha256': hash_dictvec(base_patterns),
            'current_pullback_dictvec_sha256': hash_dictvec(current_pullback),
            'explicit_target_dictvec_sha256': hash_dictvec(explicit_target),
            'inverse_helper_target_dictvec_sha256': hash_dictvec(inverse_helper_target),
            'base_matching_sha256': match_hash(c.MATCH_COEFF),
            'current_pullback_matching_sha256': match_hash(current_mc),
            'explicit_target_matching_sha256': match_hash(target_mc),
            'inverse_helper_target_matching_sha256': match_hash(inverse_mc),
            'pushed_base_matching_sha256': match_hash(pushed_base_mc),
            'original_route': route_hashes(original),
            'target_route': route_hashes(target_route),
            'current_pullback_route': route_hashes(current_route),
            'source_fixed_route': route_hashes(source_fixed_route),
            'altered_target_route': route_hashes(altered_route),
        },
        'no_N_B_orders_or_coefficients_recorded': True,
        'interpretation_ceiling': 'implementation label-frame diagnosis only; no 64-component scientific authority',
    }

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('CLASSIFICATION=' + classification)
    print('STATUS=' + status)
    print('D=' + json.dumps(D, sort_keys=True))
    return 0 if classification != INVALID else 2


if __name__ == '__main__':
    raise SystemExit(main())
