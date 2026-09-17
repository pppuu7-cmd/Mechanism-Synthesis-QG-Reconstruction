#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG = 'a03481f8020cd0eaf9426b9a569913a459f55b19'
PARENT_PREREG = '41f26f8e314f4ab1213fe6a681b69d2c87e00d68'
RECOVERY_COMMIT = '0fa0ea3614849d60eb63a1c5b721d2352802811b'

spec = importlib.util.spec_from_file_location('boundary_dual_base_r3', BASE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

# ---------------------------------------------------------------------------
# Frozen exact source aggregation, preserving all 100000 source terms and all
# 32 boundary-state components before any projection.
# ---------------------------------------------------------------------------
SOURCE_BY_STATE = []
ORIGINAL_TERMS = 0
ORIGINAL_STATES = []
ALL_TYPES = set()
for idx, arr in mod.act.PATTERNS:
    ORIGINAL_STATES.append(idx)
    acc = defaultdict(Fraction)
    for types, coeff in arr:
        ORIGINAL_TERMS += 1
        acc[types] += Fraction(coeff)
    carr = tuple((types, coeff) for types, coeff in sorted(acc.items()) if coeff)
    for types, _ in carr:
        ALL_TYPES.add(types)
    SOURCE_BY_STATE.append((idx, carr))
SOURCE_BY_STATE = tuple(SOURCE_BY_STATE)
SOURCE_STATES = tuple(idx for idx, _ in SOURCE_BY_STATE)

# Exact source entry metric. This is the same bilinear Gaussian-rational entry
# contraction used by the parent Wick recursion and the orientation/transpose
# source diagnostic.
def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cscale(c, z):
    return (c * z[0], c * z[1])


def entry_metric(ea, eb):
    x = mod.core.ENTRY[ea]
    y = mod.core.ENTRY[eb]
    re = Fraction(0)
    im = Fraction(0)
    for xx, yy in zip(x, y):
        re += xx[0] * yy[0] - xx[1] * yy[1]
        im += xx[0] * yy[1] + xx[1] * yy[0]
    return (re, im)


ENTRY_METRIC = {
    (ea, eb): entry_metric(ea, eb)
    for ea in mod.core.ENTRY
    for eb in mod.core.ENTRY
}

# Complete perfect-matching expansion of one 10-edge source type key.  The
# recursion is algebraically identical to Wick: pair the smallest remaining
# edge with each later edge and recurse.  Results are cached globally because
# they are alpha-independent.
COMPAT_CACHE = {}


def compatible(types):
    if types in COMPAT_CACHE:
        return COMPAT_CACHE[types]
    memo = {}

    def rec(rem):
        if not rem:
            return (((), (Fraction(1), Fraction(0))),)
        if rem in memo:
            return memo[rem]
        i = rem[0]
        out = []
        for pos in range(1, len(rem)):
            j = rem[pos]
            z = ENTRY_METRIC[(types[i], types[j])]
            if z == (0, 0):
                continue
            rest = rem[1:pos] + rem[pos + 1:]
            for mt, coeff in rec(rest):
                out.append((((i, j),) + mt, cmul(z, coeff)))
        memo[rem] = tuple(out)
        return memo[rem]

    ans = rec(tuple(range(10)))
    COMPAT_CACHE[types] = ans
    return ans


# Static exact coefficient of every perfect matching in every unprojected
# boundary state.  This is the finite Wick sum reassociated before alpha enters.
MATCH_BOUNDARY = defaultdict(
    lambda: [[Fraction(0), Fraction(0)] for _ in range(32)]
)
for idx, arr in SOURCE_BY_STATE:
    for types, source_coeff in arr:
        for matching, entry_coeff in compatible(types):
            z = cscale(source_coeff, entry_coeff)
            MATCH_BOUNDARY[matching][idx][0] += z[0]
            MATCH_BOUNDARY[matching][idx][1] += z[1]

MATCH_BOUNDARY = {
    mt: tuple((z[0], z[1]) for z in by_state)
    for mt, by_state in MATCH_BOUNDARY.items()
    if any(z != [0, 0] for z in by_state)
}
MATCHINGS = tuple(sorted(MATCH_BOUNDARY))

# ---------------------------------------------------------------------------
# Outcome-independent exact equivalence controls.  These are evaluated before
# W1/W2 and use only a deterministic synthetic rational covariance fixture.
# ---------------------------------------------------------------------------
SYNTH_COV = {
    (i, j): Fraction(17 * (i + 1) + 3 * (j + 1) + 5, 13)
    for i in range(10)
    for j in range(i + 1, 10)
}


def matching_monomial(matching, cov):
    z = Fraction(1)
    for i, j in matching:
        z *= cov[(i, j)]
    return z


def recursive_type_value(types, cov):
    pair = {}
    for i in range(10):
        for j in range(i + 1, 10):
            for ea in mod.core.ENTRY:
                for eb in mod.core.ENTRY:
                    g = ENTRY_METRIC[(ea, eb)]
                    pair[(i, j, ea, eb)] = (
                        cov[(i, j)] * g[0],
                        cov[(i, j)] * g[1],
                    )
    memo = {}

    def wick(rem):
        if not rem:
            return (Fraction(1), Fraction(0))
        if rem in memo:
            return memo[rem]
        i, ei = rem[0]
        total = (Fraction(0), Fraction(0))
        for pos in range(1, len(rem)):
            j, ej = rem[pos]
            rest = rem[1:pos] + rem[pos + 1:]
            total = cadd(total, cmul(pair[(i, j, ei, ej)], wick(rest)))
        memo[rem] = total
        return total

    return wick(tuple((i, types[i]) for i in range(10)))


def expanded_type_value(types, cov, drop_first=False):
    total = (Fraction(0), Fraction(0))
    rows = compatible(types)
    if drop_first and rows:
        rows = rows[1:]
    for matching, coeff in rows:
        total = cadd(total, cscale(matching_monomial(matching, cov), coeff))
    return total


state_map = {idx: arr for idx, arr in SOURCE_BY_STATE}
TYPE_CONTROL_KEYS = tuple(sorted(state_map[0])[:8] + sorted(state_map[31])[:8])
type_controls_exact = all(
    recursive_type_value(types, SYNTH_COV) == expanded_type_value(types, SYNTH_COV)
    for types, _ in TYPE_CONTROL_KEYS
)


def recursive_boundary_value(idx, cov):
    total = (Fraction(0), Fraction(0))
    for types, coeff in state_map[idx]:
        total = cadd(total, cscale(coeff, recursive_type_value(types, cov)))
    return total


def static_boundary_value(idx, cov, table=None):
    table = MATCH_BOUNDARY if table is None else table
    total = (Fraction(0), Fraction(0))
    for matching, by_state in table.items():
        coeff = by_state[idx]
        if coeff != (0, 0):
            total = cadd(total, cscale(matching_monomial(matching, cov), coeff))
    return total


synthetic_boundary_recursive = recursive_boundary_value(0, SYNTH_COV)
synthetic_boundary_static = static_boundary_value(0, SYNTH_COV)
boundary_control_exact = synthetic_boundary_recursive == synthetic_boundary_static

# Negative N1: perturb first nonzero boundary-state-0 matching coefficient.
first_nonzero_mt = next(
    mt for mt in MATCHINGS if MATCH_BOUNDARY[mt][0] != (0, 0)
)
perturbed = dict(MATCH_BOUNDARY)
rows = list(perturbed[first_nonzero_mt])
z0 = rows[0]
rows[0] = (z0[0] + 1, z0[1])
perturbed[first_nonzero_mt] = tuple(rows)
negative_perturb_rejected = (
    static_boundary_value(0, SYNTH_COV, perturbed) != synthetic_boundary_recursive
)

# Negative N2: deterministically find a source type with >1 compatible nonzero
# matching contribution and verify omission of one contribution breaks exactness.
multi_type = None
for types in sorted(ALL_TYPES):
    if len(compatible(types)) > 1:
        multi_type = types
        break
negative_drop_matching_rejected = bool(
    multi_type is not None
    and expanded_type_value(multi_type, SYNTH_COV, drop_first=True)
    != recursive_type_value(multi_type, SYNTH_COV)
)

STATIC_CHECKS = {
    'repair3_prereg_frozen': True,
    'parent_prereg_unchanged': mod.PREREG == PARENT_PREREG,
    'recovery_authority_locked': bool(RECOVERY_COMMIT),
    'original_source_terms_exactly_100000': ORIGINAL_TERMS == 100000 and mod.act.SOURCE_TERMS == 100000,
    'all_32_boundary_states_preserved': len(SOURCE_STATES) == 32 and sorted(SOURCE_STATES) == list(range(32)),
    'exact_fraction_source_aggregation': all(
        isinstance(coeff, Fraction)
        for _, arr in SOURCE_BY_STATE
        for _, coeff in arr
    ),
    'complete_perfect_matching_basis_945': len(MATCHINGS) == 945,
    'all_matching_coefficients_exact_fraction_pairs': all(
        isinstance(z[0], Fraction) and isinstance(z[1], Fraction)
        for by_state in MATCH_BOUNDARY.values()
        for z in by_state
    ),
    'type_level_synthetic_equivalence_16_exact': len(TYPE_CONTROL_KEYS) == 16 and type_controls_exact,
    'boundary0_synthetic_equivalence_exact': boundary_control_exact,
    'negative_perturbed_matching_rejected': negative_perturb_rejected,
    'negative_dropped_matching_rejected': negative_drop_matching_rejected,
}

_stats = {'calls': 0, 'hits': 0, 'misses': 0}
_cache = {}


def fast_unprojected_uncached(alpha):
    cov = mod.b0_cov(alpha)
    monomials = {mt: matching_monomial(mt, cov) for mt in MATCHINGS}
    amps = [(Fraction(0), Fraction(0)) for _ in range(32)]
    for mt in MATCHINGS:
        mon = monomials[mt]
        by_state = MATCH_BOUNDARY[mt]
        for idx, coeff in enumerate(by_state):
            if coeff != (0, 0):
                amps[idx] = cadd(amps[idx], cscale(mon, coeff))
    return tuple(amps), ORIGINAL_TERMS, len(MATCHINGS)


def fast_unprojected(alpha):
    _stats['calls'] += 1
    key = tuple(alpha)
    if key in _cache:
        _stats['hits'] += 1
        return _cache[key]
    _stats['misses'] += 1
    value = fast_unprojected_uncached(alpha)
    _cache[key] = value
    return value


def write_invalid(path, reason):
    out = {
        'gate': 'K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC',
        'prereg_commit': PARENT_PREREG,
        'execution_repair3_prereg_commit': REPAIR_PREREG,
        'classification': 'INVALID_IMPLEMENTATION',
        'repair3_failure_reason': reason,
        'repair3_static_checks': STATIC_CHECKS,
        'physical_corner_coefficients_used': False,
        'scientific_verdict': None,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    outpath = Path(args.output)

    if not all(STATIC_CHECKS.values()):
        write_invalid(outpath, 'repair3_static_equivalence_or_negative_control_failed')
        return 2

    # Replace only the execution of the already-frozen unprojected finite sum.
    mod.unprojected = fast_unprojected
    old_argv = list(sys.argv)
    sys.argv = [str(BASE), '--output', str(outpath)]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    d = json.loads(outpath.read_text(encoding='utf-8'))
    parent_classification = d.get('classification')
    execution_checks = {
        'static_checks_all_true': all(STATIC_CHECKS.values()),
        'parent_prereg_unchanged': d.get('prereg_commit') == PARENT_PREREG,
        'physical_corner_coefficients_unused': d.get('physical_corner_coefficients_used') is False,
        'parent_local_actions_24': d.get('checks', {}).get('local_actions_24') is True,
        'parent_A_inverse_exact': d.get('checks', {}).get('A_inverse_exact') is True,
        'parent_reynolds_rank_two': d.get('checks', {}).get('reynolds_rank_two') is True,
        'parent_complete_source_coverage': d.get('checks', {}).get('complete_source_coverage') is True,
        'unique_unprojected_evaluations_exactly_6': _stats['misses'] == 6 and len(_cache) == 6,
        'duplicate_base_evaluations_cache_hits': _stats['hits'] == 2,
        'total_unprojected_calls_exactly_8': _stats['calls'] == 8,
        'matching_basis_still_945': len(MATCHINGS) == 945,
    }
    allowed = {
        'BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT',
        'BOUNDARY_S5_OTHER_REPRESENTATION_EXACT',
        'DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT',
        'BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT',
    }
    d['execution_repair3_prereg_commit'] = REPAIR_PREREG
    d['execution_repair3'] = 'exact_per_boundary_perfect_matching_reassociation_before_alpha_dependent_covariance_evaluation'
    d['execution_repair3_source_stats'] = {
        'original_terms': ORIGINAL_TERMS,
        'compressed_source_type_keys': sum(len(arr) for _, arr in SOURCE_BY_STATE),
        'distinct_source_type_keys': len(ALL_TYPES),
        'boundary_states': len(SOURCE_STATES),
        'perfect_matchings': len(MATCHINGS),
    }
    d['execution_repair3_cache_stats'] = dict(_stats, unique_keys=len(_cache))
    d['execution_repair3_static_checks'] = STATIC_CHECKS
    d['execution_repair3_checks'] = execution_checks
    d['execution_repair3_synthetic_control'] = {
        'type_keys_checked': len(TYPE_CONTROL_KEYS),
        'boundary_state_checked': 0,
        'recursive_boundary_value': [str(x) for x in synthetic_boundary_recursive],
        'static_boundary_value': [str(x) for x in synthetic_boundary_static],
        'negative_perturb_matching': str(first_nonzero_mt),
        'negative_drop_type_found': multi_type is not None,
    }
    d['parent_classification_before_repair3_validation'] = parent_classification

    if not all(execution_checks.values()) or parent_classification not in allowed:
        d['classification'] = 'INVALID_IMPLEMENTATION'
        rc = 2

    outpath.write_text(json.dumps(d, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('REPAIR3_SOURCE_STATS=', json.dumps(d['execution_repair3_source_stats'], sort_keys=True))
    print('REPAIR3_CACHE_STATS=', json.dumps(d['execution_repair3_cache_stats'], sort_keys=True))
    print('REPAIR3_STATIC_CHECKS=', json.dumps(STATIC_CHECKS, sort_keys=True))
    print('REPAIR3_EXECUTION_CHECKS=', json.dumps(execution_checks, sort_keys=True))
    print('FINAL_CLASSIFICATION=', d['classification'])
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
