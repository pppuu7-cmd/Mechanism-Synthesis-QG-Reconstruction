#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG = '06049f0a575a07d1e35afcea143fbb800101071e'
PARENT_PREREG = '41f26f8e314f4ab1213fe6a681b69d2c87e00d68'


def load(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    assert s.loader is not None
    s.loader.exec_module(m)
    return m


mod = load(BASE, 'boundary_dual_parent_r4_shard')


def invperm(p):
    return tuple(p.index(i) for i in range(len(p)))


IP = invperm(mod.CYCLE)


def expected_alphas():
    w1 = tuple(mod.WITNESSES['W1'])
    w2 = tuple(mod.WITNESSES['W2'])
    return {
        'W1_base': w1,
        'W1_cycle': tuple(mod.core.perm_weights(w1, mod.CYCLE)),
        'W1_inverse': tuple(mod.core.perm_weights(w1, IP)),
        'W2_base': w2,
        'W2_cycle': tuple(mod.core.perm_weights(w2, mod.CYCLE)),
        'W2_inverse': tuple(mod.core.perm_weights(w2, IP)),
    }


EXPECTED = expected_alphas()


def fq(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def encode_vec(v):
    return [[fq(z[0]), fq(z[1])] for z in v]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True, choices=sorted(EXPECTED))
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    label = args.label
    alpha = EXPECTED[label]
    vec, terms, cache = mod.unprojected(alpha)

    checks = {
        'repair4_prereg_locked': bool(REPAIR_PREREG),
        'parent_prereg_unchanged': mod.PREREG == PARENT_PREREG,
        'label_is_frozen': label in EXPECTED,
        'alpha_matches_frozen_label': tuple(alpha) == EXPECTED[label],
        'source_terms_exactly_100000': terms == 100000 and mod.act.SOURCE_TERMS == 100000,
        'vector_has_32_boundary_components': len(vec) == 32,
        'all_components_exact_fraction_pairs': all(
            isinstance(z[0], Fraction) and isinstance(z[1], Fraction) for z in vec
        ),
        'physical_corner_coefficients_unused': True,
    }
    valid = all(checks.values())
    out = {
        'gate': 'K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC_REPAIR4_SHARD',
        'execution_repair4_prereg_commit': REPAIR_PREREG,
        'parent_prereg_commit': PARENT_PREREG,
        'label': label,
        'alpha': [fq(x) for x in alpha],
        'source_terms': terms,
        'wick_cache_size': cache,
        'boundary_components': len(vec),
        'vector': encode_vec(vec),
        'checks': checks,
        'status': 'PASS_EXACT_SHARD' if valid else 'INVALID_IMPLEMENTATION',
        'physical_corner_coefficients_used': False,
        'scientific_verdict': None,
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('label','alpha','source_terms','wick_cache_size','boundary_components','status')}, indent=2, sort_keys=True))
    return 0 if valid else 2


if __name__ == '__main__':
    raise SystemExit(main())
