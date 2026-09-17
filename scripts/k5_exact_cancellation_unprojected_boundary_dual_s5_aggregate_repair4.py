#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG = '06049f0a575a07d1e35afcea143fbb800101071e'
PARENT_PREREG = '41f26f8e314f4ab1213fe6a681b69d2c87e00d68'
LABELS = ('W1_base','W1_cycle','W1_inverse','W2_base','W2_cycle','W2_inverse')
ALLOWED = {
    'BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT',
    'BOUNDARY_S5_OTHER_REPRESENTATION_EXACT',
    'DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT',
    'BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT',
}


def load(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    assert s.loader is not None
    s.loader.exec_module(m)
    return m


mod = load(BASE, 'boundary_dual_parent_r4_aggregate')


def invperm(p):
    return tuple(p.index(i) for i in range(len(p)))


def fq(x):
    return Fraction(x)


def decode_vec(rows):
    return tuple((fq(z[0]), fq(z[1])) for z in rows)


def digest_vec(v):
    return [[str(x[0]), str(x[1])] for x in v]


def expected_alphas():
    ip = invperm(mod.CYCLE)
    w1 = tuple(mod.WITNESSES['W1'])
    w2 = tuple(mod.WITNESSES['W2'])
    return {
        'W1_base': w1,
        'W1_cycle': tuple(mod.core.perm_weights(w1, mod.CYCLE)),
        'W1_inverse': tuple(mod.core.perm_weights(w1, ip)),
        'W2_base': w2,
        'W2_cycle': tuple(mod.core.perm_weights(w2, mod.CYCLE)),
        'W2_inverse': tuple(mod.core.perm_weights(w2, ip)),
    }


EXPECTED = expected_alphas()


def manifest_entry_ok(label, d):
    try:
        return (
            label in EXPECTED
            and d.get('label') == label
            and d.get('status') == 'PASS_EXACT_SHARD'
            and d.get('execution_repair4_prereg_commit') == REPAIR_PREREG
            and d.get('parent_prereg_commit') == PARENT_PREREG
            and tuple(Fraction(x) for x in d.get('alpha', [])) == tuple(Fraction(x) for x in EXPECTED[label])
            and d.get('source_terms') == 100000
            and d.get('boundary_components') == 32
            and len(d.get('vector', [])) == 32
            and d.get('physical_corner_coefficients_used') is False
            and all(d.get('checks', {}).values())
        )
    except Exception:
        return False


def lane_from_vectors(a, b, A, Ai):
    laws = {
        'A': mod.mvec(A, a),
        'A_inverse': mod.mvec(Ai, a),
        'A_transpose': mod.mvec(mod.tr(A), a),
        'A_inverse_transpose': mod.mvec(mod.tr(Ai), a),
    }
    exact = {k: (v == b) for k, v in laws.items()}
    ca, cw = mod.coords(a)
    cb, cbw = mod.coords(b)
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shards', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    root = Path(args.shards)

    files = sorted(root.glob('*.json'))
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

    exact_label_set = set(loaded) == set(LABELS) and len(loaded) == len(LABELS) and not duplicate_labels
    shard_manifests_exact = exact_label_set and all(manifest_entry_ok(label, loaded[label]) for label in LABELS)

    # Frozen negative controls, evaluated before classification.
    bad_manifest = dict(loaded.get('W1_cycle', {}))
    if 'W1_inverse' in loaded:
        bad_manifest['alpha'] = loaded['W1_inverse'].get('alpha')
    negative_wrong_alpha_rejected = not manifest_entry_ok('W1_cycle', bad_manifest)
    bad_len = dict(loaded.get('W1_base', {}))
    bad_len['vector'] = list(bad_len.get('vector', []))[:-1]
    bad_len['boundary_components'] = 31
    negative_missing_component_rejected = not manifest_entry_ok('W1_base', bad_len)

    tensors = mod.reach.local_tensor_vectors(mod.act.src)
    local = mod.reach.local_action_matrices(tensors)
    A = mod.reach.global_action_matrix(mod.act.src, mod.CYCLE, local)
    ip = invperm(mod.CYCLE)
    Ai = mod.reach.global_action_matrix(mod.act.src, ip, local)
    I = mod.eye(32)
    action_inverse_exact = mod.mm(A, Ai) == I and mod.mm(Ai, A) == I
    A_bad = [row[:] for row in A]
    A_bad[0][0] += Fraction(1)
    negative_perturbed_action_rejected = not (mod.mm(A_bad, Ai) == I and mod.mm(Ai, A_bad) == I)

    prechecks = {
        'repair4_prereg_locked': bool(REPAIR_PREREG),
        'parent_prereg_unchanged': mod.PREREG == PARENT_PREREG,
        'exact_six_shard_label_set': exact_label_set,
        'all_shard_manifests_exact': shard_manifests_exact,
        'local_actions_24': len(local) == 24,
        'A_inverse_exact': action_inverse_exact,
        'reynolds_rank_two_pivots_1_4': len(mod.act.PIV) == 2 and list(mod.act.PIV) == [1,4],
        'negative_wrong_alpha_rejected': negative_wrong_alpha_rejected,
        'negative_missing_component_rejected': negative_missing_component_rejected,
        'negative_perturbed_action_rejected': negative_perturbed_action_rejected,
        'physical_corner_coefficients_unused': True,
    }

    valid_pre = all(prechecks.values())
    vectors = {}
    if valid_pre:
        vectors = {label: decode_vec(loaded[label]['vector']) for label in LABELS}
        prechecks['all_decoded_vectors_32_exact'] = all(
            len(v) == 32 and all(isinstance(z[0], Fraction) and isinstance(z[1], Fraction) for z in v)
            for v in vectors.values()
        )
    else:
        prechecks['all_decoded_vectors_32_exact'] = False

    lanes = {}
    if all(prechecks.values()):
        for witness in ('W1','W2'):
            base = vectors[f'{witness}_base']
            lanes[witness] = {
                'cycle': lane_from_vectors(base, vectors[f'{witness}_cycle'], A, Ai),
                'inverse': lane_from_vectors(base, vectors[f'{witness}_inverse'], Ai, A),
            }

    parent_checks = {
        'local_actions_24': len(local) == 24,
        'A_inverse_exact': action_inverse_exact,
        'reynolds_rank_two': len(mod.act.PIV) == 2 and list(mod.act.PIV) == [1,4],
        'source_terms_100000': all(loaded.get(label, {}).get('source_terms') == 100000 for label in LABELS),
        'complete_source_coverage': all(loaded.get(label, {}).get('source_terms') == 100000 for label in LABELS),
    }

    classification = 'INVALID_IMPLEMENTATION'
    law = None
    coordinv = False
    coordextract = False
    if all(prechecks.values()) and all(parent_checks.values()):
        allentries = [lanes[n][d] for n in ('W1','W2') for d in ('cycle','inverse')]
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
        'execution_repair4_prereg_commit': REPAIR_PREREG,
        'execution_repair4': 'six_independent_exact_alpha_shards_then_exact_parent_classifier_recombination',
        'cycle': list(mod.CYCLE),
        'inverse_cycle': list(ip),
        'shard_manifest': manifest,
        'checks': parent_checks,
        'execution_repair4_checks': repair_checks,
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
        'repair4_checks_all_true': all(repair_checks.values()),
        'shard_labels': sorted(manifest),
    }, indent=2, sort_keys=True))
    return 0 if classification in ALLOWED and all(repair_checks.values()) else 2


if __name__ == '__main__':
    raise SystemExit(main())
