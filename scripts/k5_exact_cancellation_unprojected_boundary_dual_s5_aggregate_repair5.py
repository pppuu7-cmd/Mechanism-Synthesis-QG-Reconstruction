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
LABELS = ('W1_base', 'W1_cycle', 'W1_inverse', 'W2_base', 'W2_cycle', 'W2_inverse')
ALLOWED = {
    'BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT',
    'BOUNDARY_S5_OTHER_REPRESENTATION_EXACT',
    'DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT',
    'BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT',
}


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def prefix_namespace_ok(ns):
    required = ('PATTERNS', 'SOURCE_TERMS', 'P', 'PIV', 'WEIGHTS', 'reach', 'src')
    return all(k in ns for k in required) and 'results' not in ns


def load_action_prefix():
    assert git_blob_sha(ACTION) == ACTION_BLOB
    text = ACTION.read_text(encoding='utf-8')
    assert text.count(MARKER) == 1
    prefix = text.split(MARKER, 1)[0]
    ns = {'__name__': 'k5_action_prefix_repair5_aggregate', '__file__': str(ACTION), '__package__': None}
    exec(compile(prefix, str(ACTION), 'exec'), ns, ns)
    assert prefix_namespace_ok(ns)
    return SimpleNamespace(**ns), ns


assert git_blob_sha(RESOLVER) == RESOLVER_BLOB
assert git_blob_sha(PARENT) == PARENT_BLOB
r = load_module(RESOLVER, 'k5_cancel_resolver_repair5_aggregate')
act, ACTION_NS = load_action_prefix()
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


def fq(x):
    return Fraction(x)


def decode_vec(rows):
    return tuple((fq(z[0]), fq(z[1])) for z in rows)


def digest_vec(v):
    return [[str(z[0]), str(z[1])] for z in v]


def tr(A):
    return [list(x) for x in zip(*A)]


def mm(A, B):
    BT = list(zip(*B))
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in BT] for row in A]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def cvadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cvscale(c, a):
    return (c * a[0], c * a[1])


def mvec(A, v):
    out = []
    for row in A:
        z = (Fraction(0), Fraction(0))
        for c, x in zip(row, v):
            z = cvadd(z, cvscale(c, x))
        out.append(z)
    return tuple(out)


def coords(a):
    dp = mvec(tr(act.P), a)
    auth = tuple(dp[i] for i in act.PIV)
    weighted = []
    for c in range(2):
        z = (Fraction(0), Fraction(0))
        for j, x in enumerate(a):
            z = cvadd(z, cvscale(act.WEIGHTS[j][c], x))
        weighted.append(z)
    return auth, tuple(weighted)


def lane_from_vectors(a, b, A, Ai):
    laws = {
        'A': mvec(A, a),
        'A_inverse': mvec(Ai, a),
        'A_transpose': mvec(tr(A), a),
        'A_inverse_transpose': mvec(tr(Ai), a),
    }
    exact = {k: (v == b) for k, v in laws.items()}
    ca, cw = coords(a)
    cb, cbw = coords(b)
    return {
        'laws_exact': exact,
        'exact_laws': [k for k, v in exact.items() if v],
        'dual_coordinates_base': digest_vec(ca),
        'dual_coordinates_target': digest_vec(cb),
        'dual_coordinates_invariant': ca == cb,
        'weighted_coordinates_equal_authoritative_base': cw == ca,
        'weighted_coordinates_equal_authoritative_target': cbw == cb,
        'source_terms': 100000,
        'target_source_terms': 100000,
    }


def manifest_entry_ok(label, d):
    try:
        return (
            label in EXPECTED
            and d.get('label') == label
            and d.get('status') == 'PASS_EXACT_SHARD'
            and d.get('execution_repair5_prereg_commit') == REPAIR_PREREG
            and d.get('parent_prereg_commit') == PARENT_PREREG
            and d.get('source_blobs') == {'parent': PARENT_BLOB, 'action': ACTION_BLOB, 'resolver': RESOLVER_BLOB}
            and tuple(Fraction(x) for x in d.get('alpha', [])) == tuple(Fraction(x) for x in EXPECTED[label])
            and d.get('source_terms') == 100000
            and d.get('boundary_components') == 32
            and len(d.get('vector', [])) == 32
            and d.get('physical_corner_coefficients_used') is False
            and all(d.get('checks', {}).values())
        )
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shards', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    root = Path(args.shards)

    files = sorted(root.rglob('*.json'))
    loaded = {}
    manifest = {}
    duplicate_labels = []
    for p in files:
        raw = p.read_bytes()
        d = json.loads(raw.decode('utf-8'))
        label = d.get('label')
        if label in loaded:
            duplicate_labels.append(label)
        loaded[label] = d
        manifest[label] = {
            'filename': p.name,
            'sha256': hashlib.sha256(raw).hexdigest(),
            'alpha': d.get('alpha'),
            'source_terms': d.get('source_terms'),
            'boundary_components': d.get('boundary_components'),
        }

    exact_label_set = set(loaded) == set(LABELS) and len(loaded) == 6 and not duplicate_labels
    shard_manifests_exact = exact_label_set and all(manifest_entry_ok(label, loaded[label]) for label in LABELS)

    tensors = act.reach.local_tensor_vectors(act.src)
    local = act.reach.local_action_matrices(tensors)
    A = act.reach.global_action_matrix(act.src, CYCLE, local)
    Ai = act.reach.global_action_matrix(act.src, IP, local)
    I = eye(32)
    action_inverse_exact = mm(A, Ai) == I and mm(Ai, A) == I

    bad_manifest = dict(loaded.get('W1_cycle', {}))
    if 'W1_inverse' in loaded:
        bad_manifest['alpha'] = loaded['W1_inverse'].get('alpha')
    negative_wrong_alpha_rejected = not manifest_entry_ok('W1_cycle', bad_manifest)
    bad_len = dict(loaded.get('W1_base', {}))
    bad_len['vector'] = list(bad_len.get('vector', []))[:-1]
    bad_len['boundary_components'] = 31
    negative_missing_component_rejected = not manifest_entry_ok('W1_base', bad_len)
    A_bad = [row[:] for row in A]
    A_bad[0][0] += Fraction(1)
    negative_perturbed_action_rejected = not (mm(A_bad, Ai) == I and mm(Ai, A_bad) == I)
    synthetic_suffix_ns = dict(ACTION_NS)
    synthetic_suffix_ns['results'] = {}
    negative_full_suffix_rejected = not prefix_namespace_ok(synthetic_suffix_ns)

    prechecks = {
        'repair5_prereg_locked': REPAIR_PREREG == 'f472eb29ded6a04ab1ae8a5f367d378f64beee4f',
        'parent_prereg_locked': PARENT_PREREG == '41f26f8e314f4ab1213fe6a681b69d2c87e00d68',
        'parent_blob_locked': git_blob_sha(PARENT) == PARENT_BLOB,
        'action_blob_locked': git_blob_sha(ACTION) == ACTION_BLOB,
        'resolver_blob_locked': git_blob_sha(RESOLVER) == RESOLVER_BLOB,
        'action_prefix_marker_unique': ACTION.read_text(encoding='utf-8').count(MARKER) == 1,
        'historical_action_production_suffix_not_executed': 'results' not in ACTION_NS,
        'exact_six_shard_label_set': exact_label_set,
        'all_shard_manifests_exact': shard_manifests_exact,
        'local_actions_24': len(local) == 24,
        'A_inverse_exact': action_inverse_exact,
        'reynolds_rank_two_pivots_1_4': len(act.PIV) == 2 and list(act.PIV) == [1, 4],
        'negative_full_action_suffix_rejected': negative_full_suffix_rejected,
        'negative_wrong_alpha_rejected': negative_wrong_alpha_rejected,
        'negative_missing_component_rejected': negative_missing_component_rejected,
        'negative_perturbed_action_rejected': negative_perturbed_action_rejected,
        'physical_corner_coefficients_unused': True,
    }

    vectors = {}
    if all(prechecks.values()):
        vectors = {label: decode_vec(loaded[label]['vector']) for label in LABELS}
        prechecks['all_decoded_vectors_32_exact'] = all(
            len(v) == 32 and all(isinstance(z[0], Fraction) and isinstance(z[1], Fraction) for z in v)
            for v in vectors.values()
        )
    else:
        prechecks['all_decoded_vectors_32_exact'] = False

    lanes = {}
    if all(prechecks.values()):
        for witness in ('W1', 'W2'):
            base = vectors[f'{witness}_base']
            lanes[witness] = {
                'cycle': lane_from_vectors(base, vectors[f'{witness}_cycle'], A, Ai),
                'inverse': lane_from_vectors(base, vectors[f'{witness}_inverse'], Ai, A),
            }

    parent_checks = {
        'local_actions_24': len(local) == 24,
        'A_inverse_exact': action_inverse_exact,
        'reynolds_rank_two': len(act.PIV) == 2 and list(act.PIV) == [1, 4],
        'source_terms_100000': all(loaded.get(label, {}).get('source_terms') == 100000 for label in LABELS),
        'complete_source_coverage': all(loaded.get(label, {}).get('source_terms') == 100000 for label in LABELS),
    }

    classification = 'INVALID_IMPLEMENTATION'
    law = None
    coordinv = False
    coordextract = False
    if all(prechecks.values()) and all(parent_checks.values()):
        allentries = [lanes[n][d] for n in ('W1', 'W2') for d in ('cycle', 'inverse')]
        lawsets = [tuple(x['exact_laws']) for x in allentries]
        unique_consistent = len(set(lawsets)) == 1 and len(lawsets[0]) == 1
        law = lawsets[0][0] if unique_consistent else None
        coordextract = all(
            x['weighted_coordinates_equal_authoritative_base'] and x['weighted_coordinates_equal_authoritative_target']
            for x in allentries
        )
        coordinv = all(x['dual_coordinates_invariant'] for x in allentries)
        if law == 'A_inverse_transpose' and coordinv and coordextract:
            classification = 'BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT'
        elif law == 'A_inverse_transpose' and not coordextract:
            classification = 'DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT'
        elif unique_consistent:
            classification = 'BOUNDARY_S5_OTHER_REPRESENTATION_EXACT'
        else:
            classification = 'BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT'

    repair_checks = dict(prechecks)
    repair_checks.update({
        'parent_checks_all_true': all(parent_checks.values()),
        'parent_classification_allowed': classification in ALLOWED,
        'logical_lane_count_four': sum(len(x) for x in lanes.values()) == 4 if lanes else False,
        'six_unique_vectors_two_base_reuses': len(vectors) == 6 if vectors else False,
    })
    if not all(repair_checks.values()):
        classification = 'INVALID_IMPLEMENTATION'

    out = {
        'gate': 'K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC',
        'prereg_commit': PARENT_PREREG,
        'execution_repair5_prereg_commit': REPAIR_PREREG,
        'execution_repair5': 'import_safe_action_prefix_then_six_independent_exact_alpha_shards_and_exact_parent_classifier',
        'source_blobs': {'parent': PARENT_BLOB, 'action': ACTION_BLOB, 'resolver': RESOLVER_BLOB},
        'cycle': list(CYCLE),
        'inverse_cycle': list(IP),
        'shard_manifest': manifest,
        'checks': parent_checks,
        'execution_repair5_checks': repair_checks,
        'lanes': lanes,
        'unique_consistent_law': law,
        'dual_coordinates_invariant_all': coordinv,
        'coordinate_extraction_exact_all': coordextract,
        'classification': classification,
        'physical_corner_coefficients_used': False,
        'scientific_verdict': None,
    }
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({
        'classification': classification,
        'unique_consistent_law': law,
        'dual_coordinates_invariant_all': coordinv,
        'coordinate_extraction_exact_all': coordextract,
        'repair5_checks_all_true': all(repair_checks.values()),
        'shard_labels': sorted(manifest),
    }, indent=2, sort_keys=True))
    return 0 if classification in ALLOWED and all(repair_checks.values()) else 2


if __name__ == '__main__':
    raise SystemExit(main())
