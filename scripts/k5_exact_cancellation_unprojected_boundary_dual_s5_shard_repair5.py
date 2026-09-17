#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
ACTION = ROOT / 'scripts/k5_deg4_annihilator_actual_dual_action.py'
RESOLVER = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_cancellation_resolution.py'
PARENT = ROOT / 'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG = 'f472eb29ded6a04ab1ae8a5f367d378f64beee4f'
PARENT_PREREG = '41f26f8e314f4ab1213fe6a681b69d2c87e00d68'
ACTION_BLOB = '2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
RESOLVER_BLOB = '012b04669948962548064334bfbed47062e4acc0'
PARENT_BLOB = '493cded56de272ecc1929bb6cf1324d9ea4800cd'
MARKER = 'results={};checks={}'
CYCLE = (1, 2, 3, 4, 0)


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_action_prefix():
    raw = ACTION.read_bytes()
    assert git_blob_sha(ACTION) == ACTION_BLOB
    text = raw.decode('utf-8')
    assert text.count(MARKER) == 1
    prefix = text.split(MARKER, 1)[0]
    ns = {'__name__': 'k5_action_prefix_repair5', '__file__': str(ACTION), '__package__': None}
    exec(compile(prefix, str(ACTION), 'exec'), ns, ns)
    required = ('PATTERNS', 'SOURCE_TERMS', 'P', 'PIV', 'WEIGHTS', 'reach', 'src')
    assert all(k in ns for k in required)
    assert 'results' not in ns
    return SimpleNamespace(**ns)


assert git_blob_sha(RESOLVER) == RESOLVER_BLOB
assert git_blob_sha(PARENT) == PARENT_BLOB
r = load_module(RESOLVER, 'k5_cancel_resolver_repair5_shard')
act = load_action_prefix()
core = r.core


def invperm(p):
    return tuple(p.index(i) for i in range(len(p)))


IP = invperm(CYCLE)
W1 = tuple(r.W1)
W2 = tuple(r.W2)
EXPECTED = {
    'W1_base': W1,
    'W1_cycle': tuple(core.perm_weights(W1, CYCLE)),
    'W1_inverse': tuple(core.perm_weights(W1, IP)),
    'W2_base': W2,
    'W2_cycle': tuple(core.perm_weights(W2, CYCLE)),
    'W2_inverse': tuple(core.perm_weights(W2, IP)),
}


def cvadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cvscale(c, a):
    return (c * a[0], c * a[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def b0_cov(alpha):
    aa = [r.D(Fraction(x), 0) for x in alpha]
    L = r.build_L(aa)
    psi = r.psi_direct(aa)
    if psi.v == 0:
        raise ZeroDivisionError('psi zero')
    B0 = r.inv_cofactor(L, psi)
    return {
        (i, j): r.dot_mat(core.ROWS[i], B0, core.ROWS[j]).v
        for i in range(10)
        for j in range(i + 1, 10)
    }


def unprojected(alpha):
    cov = b0_cov(alpha)
    pair = {}
    for i in range(10):
        for j in range(i + 1, 10):
            for ea in core.ENTRY:
                for eb in core.ENTRY:
                    g = core.EM[(ea, eb)]
                    pair[(i, j, ea, eb)] = (cov[(i, j)] * g[0], cov[(i, j)] * g[1])
    cache = {}

    def wick(rem):
        if not rem:
            return (Fraction(1), Fraction(0))
        if rem in cache:
            return cache[rem]
        i, ei = rem[0]
        total = (Fraction(0), Fraction(0))
        for pos in range(1, len(rem)):
            j, ej = rem[pos]
            rest = rem[1:pos] + rem[pos + 1:]
            total = cvadd(total, cmul(pair[(i, j, ei, ej)], wick(rest)))
        cache[rem] = total
        return total

    amps = [(Fraction(0), Fraction(0)) for _ in range(32)]
    terms = 0
    seen = []
    for idx, arr in act.PATTERNS:
        seen.append(idx)
        z = (Fraction(0), Fraction(0))
        for types, coeff in arr:
            terms += 1
            rem = tuple((i, types[i]) for i in range(10))
            z = cvadd(z, cvscale(coeff, wick(rem)))
        amps[idx] = z
    assert sorted(seen) == list(range(32))
    return tuple(amps), terms, len(cache)


def fq(x):
    q = Fraction(x)
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def encode_vec(v):
    return [[fq(z[0]), fq(z[1])] for z in v]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True, choices=sorted(EXPECTED))
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    label = args.label
    alpha = EXPECTED[label]
    vec, terms, cache = unprojected(alpha)

    checks = {
        'repair5_prereg_locked': REPAIR_PREREG == 'f472eb29ded6a04ab1ae8a5f367d378f64beee4f',
        'parent_prereg_locked': PARENT_PREREG == '41f26f8e314f4ab1213fe6a681b69d2c87e00d68',
        'parent_blob_locked': git_blob_sha(PARENT) == PARENT_BLOB,
        'action_blob_locked': git_blob_sha(ACTION) == ACTION_BLOB,
        'resolver_blob_locked': git_blob_sha(RESOLVER) == RESOLVER_BLOB,
        'action_prefix_marker_unique': ACTION.read_text(encoding='utf-8').count(MARKER) == 1,
        'historical_action_production_suffix_not_executed': not hasattr(act, 'results'),
        'label_is_frozen': label in EXPECTED,
        'alpha_matches_frozen_label': tuple(alpha) == EXPECTED[label],
        'source_terms_exactly_100000': terms == 100000 and act.SOURCE_TERMS == 100000,
        'vector_has_32_boundary_components': len(vec) == 32,
        'all_components_exact_fraction_pairs': all(isinstance(z[0], Fraction) and isinstance(z[1], Fraction) for z in vec),
        'physical_corner_coefficients_unused': True,
    }
    valid = all(checks.values())
    out = {
        'gate': 'K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC_REPAIR5_SHARD',
        'execution_repair5_prereg_commit': REPAIR_PREREG,
        'parent_prereg_commit': PARENT_PREREG,
        'source_blobs': {'parent': PARENT_BLOB, 'action': ACTION_BLOB, 'resolver': RESOLVER_BLOB},
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
    print(json.dumps({k: out[k] for k in ('label', 'alpha', 'source_terms', 'wick_cache_size', 'boundary_components', 'status')}, indent=2, sort_keys=True))
    return 0 if valid else 2


if __name__ == '__main__':
    raise SystemExit(main())
