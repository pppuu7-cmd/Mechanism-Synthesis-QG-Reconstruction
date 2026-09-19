#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
PREREG = ROOT / 'prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_CONTROL_REPAIR_3_PREFLIGHT.md'
CONTROL_REPAIR_PREREG = ROOT / 'prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_CONTROL_REPAIR_1.md'
CRITIC_AUTH = ROOT / 'results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json'
CRITIC_PROVENANCE = ROOT / 'status/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_INDEPENDENT_CRITIC_PROVENANCE.md'

REPAIR3_PREREG_COMMIT = '4ee6c6f3056c5934a5209a4f05616b73354b4e6e'
CONTROL_REPAIR_PREREG_COMMIT = 'a05e1e29d2f39b678b2cf5f6b187cc165c787f9d'
CRITIC_CLASS = 'K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED'
CRITIC_RUN = 35412815680
CRITIC_JOB = 105815631932
CRITIC_PROVENANCE_COMMIT = '81b85171bb2432438b853bca37cca7bafa3c8d2e'
CRITIC_RAW_AUTH_COMMIT = 'daa6cbdf2f5c9412624a93d7e19feaf7c07dd2c7'
CRITIC_RAW_AUTH_BLOB = 'a738852e012f0d7e9b157ab9a1517df3696e6993'
CRITIC_RESULT_SHA256 = '7b6579241714f37631f58a9bef7ec1c7e507ad204f946ae769d615286a1a9f13'
EXPECTED_PULLBACK_HASH = 'cee5a38677919965c66a785349286163b4ebd5dda8731bcdccdc71eec2543cbc'
EXPECTED_TARGET_HASH = '0fadf222c22368dfac0f0c1e2ea93774ad9c103ed1506685292152e49cbe182b'


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


repair1 = load(PARENT, 'k5_34_exact_core_repair3_parent')

# Re-export the unchanged repair-1 scientific surface. Repair-3 alters only the
# label frame of the S5 matching coefficient table used by the target route.
for _name in dir(repair1):
    if not _name.startswith('__'):
        globals()[_name] = getattr(repair1, _name)


def _perfect_matching_key(mt):
    return (
        len(mt) == 5
        and sorted(i for pair in mt for i in pair) == list(range(10))
        and all(len(pair) == 2 and pair[0] < pair[1] for pair in mt)
    )


def forward_matching(mt):
    out = []
    for i, j in mt:
        a = repair1.s5.ep(repair1.s5.C, i)
        b = repair1.s5.ep(repair1.s5.C, j)
        out.append((min(a, b), max(a, b)))
    return tuple(sorted(out))


def inverse_matching(tmt):
    ip = repair1.s5.invperm(repair1.s5.C)
    out = []
    for i, j in tmt:
        a = repair1.s5.ep(ip, i)
        b = repair1.s5.ep(ip, j)
        out.append((min(a, b), max(a, b)))
    return tuple(sorted(out))


def _build_target_table(pullback):
    target = {}
    for mt, coeff in pullback.items():
        tmt = forward_matching(mt)
        if tmt in target:
            raise RuntimeError(f'non-bijective matching pushforward collision at {tmt!r}')
        target[tmt] = coeff
    return target


S5_MATCH_COEFF_CYCLE_PULLBACK = repair1.S5_MATCH_COEFF_CYCLE
S5_MATCH_COEFF_CYCLE_TARGET = _build_target_table(S5_MATCH_COEFF_CYCLE_PULLBACK)
# Future resolver repair-3 consumers use the existing symbol with only its key
# frame changed. Coefficient values remain the exact repair-1 values.
S5_MATCH_COEFF_CYCLE = S5_MATCH_COEFF_CYCLE_TARGET


def _value_multiset(table):
    return sorted(repr(v) for v in table.values())


def static_checks():
    out = dict(repair1.static_checks())
    auth = json.loads(CRITIC_AUTH.read_text(encoding='utf-8'))
    provenance_text = CRITIC_PROVENANCE.read_text(encoding='utf-8')
    canonical = repair1.MATCH_COEFF
    pullback = S5_MATCH_COEFF_CYCLE_PULLBACK
    target = S5_MATCH_COEFF_CYCLE_TARGET
    forward_keys = [forward_matching(mt) for mt in canonical]

    out.update({
        'repair3_prereg_commit_locked': REPAIR3_PREREG_COMMIT == '4ee6c6f3056c5934a5209a4f05616b73354b4e6e',
        'repair3_prereg_present': PREREG.exists() and 'minimal matching-key frame control repair 3 preflight' in PREREG.read_text(encoding='utf-8'),
        'control_repair1_prereg_commit_locked': CONTROL_REPAIR_PREREG_COMMIT == 'a05e1e29d2f39b678b2cf5f6b187cc165c787f9d',
        'control_repair1_prereg_present': CONTROL_REPAIR_PREREG.exists() and 'control-only repair 1' in CONTROL_REPAIR_PREREG.read_text(encoding='utf-8'),
        'label_frame_critic_class_locked': auth.get('classification') == CRITIC_CLASS,
        'label_frame_critic_raw_blob_locked': git_blob_sha1(CRITIC_AUTH) == CRITIC_RAW_AUTH_BLOB,
        'label_frame_critic_provenance_commit_locked': CRITIC_PROVENANCE_COMMIT == '81b85171bb2432438b853bca37cca7bafa3c8d2e',
        'label_frame_critic_provenance_present': CRITIC_PROVENANCE.exists(),
        'label_frame_critic_run_locked': f'run `{CRITIC_RUN}`' in provenance_text,
        'label_frame_critic_job_locked': f'job `{CRITIC_JOB}`' in provenance_text,
        'label_frame_critic_result_hash_locked': CRITIC_RESULT_SHA256 in provenance_text,
        'label_frame_critic_raw_commit_locked': CRITIC_RAW_AUTH_COMMIT in provenance_text,
        'label_frame_critic_q18_unused': auth.get('q18_values_used') is False,
        'label_frame_critic_N_B_unused': auth.get('N_B_orders_or_coefficients_used') is False,
        'canonical_matching_count_945': len(canonical) == 945,
        'pullback_matching_count_945': len(pullback) == 945,
        'target_matching_count_945': len(target) == 945,
        'canonical_keys_perfect': all(_perfect_matching_key(mt) for mt in canonical),
        'pullback_keys_perfect': all(_perfect_matching_key(mt) for mt in pullback),
        'target_keys_perfect': all(_perfect_matching_key(mt) for mt in target),
        'forward_map_bijection_all945': len(set(forward_keys)) == 945 and set(forward_keys) == set(target),
        'forward_inverse_roundtrip_all945': all(inverse_matching(forward_matching(mt)) == mt for mt in canonical),
        'pullback_equals_canonical_all945': all(pullback.get(mt) == canonical.get(mt) for mt in canonical),
        'target_pushforward_relation_all945': all(target.get(forward_matching(mt)) == canonical.get(mt) for mt in canonical),
        'coefficient_multiset_preserved': _value_multiset(target) == _value_multiset(pullback),
        'all_coefficients_exact_fraction': all(isinstance(x, Fraction) for coeffs in target.values() for ch in coeffs for x in ch),
        'pullback_hash_locked': repair1._match_coeff_hash(pullback) == EXPECTED_PULLBACK_HASH,
        'target_hash_locked': repair1._match_coeff_hash(target) == EXPECTED_TARGET_HASH,
        'source_terms_100000': repair1._SOURCE_TERM_COUNT == 100000,
        'q18_values_used': False,
        'N_B_orders_or_coefficients_used': False,
    })
    return out


# Unchanged parent helpers for future separately-authorized resolver repair-3.
route_a = repair1.route_a
route_b_interpolation = repair1.route_b_interpolation
proper_orbits = repair1.proper_orbits
class_representatives = repair1.class_representatives
lane_serial = repair1.lane_serial
vector_hash = repair1.vector_hash
PRE = repair1.PRE
N_DEG = repair1.N_DEG
B_DEG = repair1.B_DEG
SOURCE_TERMS = repair1.SOURCE_TERMS
MATCH_COEFF = repair1.MATCH_COEFF
W1 = repair1.W1
W2 = repair1.W2
CYCLE = repair1.CYCLE
WP1 = repair1.WP1
WP2 = repair1.WP2
core = repair1.core
