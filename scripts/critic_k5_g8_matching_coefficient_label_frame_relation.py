#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R1 = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
R2 = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair2.py'
PC = ROOT / 'scripts/k5_34_orbit_postcollapse_geometry_covariance_s5_transport_diagnostic.py'
PREREG = ROOT / 'prereg/K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_RELATION_INDEPENDENT_CRITIC_DIAGNOSTIC.md'
PARENT = ROOT / 'results/raw/k5_34_orbit_g8_matching_covariance_composition_diagnostic_terminal.json'

PREREG_COMMIT = 'e0b8432e71b97cd169a909c27d1a93b92d9f0ef5'
PARENT_PERSIST_COMMIT = '65095d15ddb94996d6e331fd9d032f7bd51c0745'
PARENT_RUN = 35411497229
PARENT_JOB = 105811869437
PARENT_HEAD = 'd87f8ed389f0cf418e1ec0abd49077604c73f853'
PARENT_ARTIFACT = 10573657808
PARENT_ZIP_SHA256 = '168c0826839c7480dd6fb0df0e6bf7711361fdd7c46d9b75e396640f0075ae59'
PARENT_JSON_SHA256 = 'a706245b311c9e8d4b573747724fd75cd0ccb7efc5e09a63485addafe1a72361'
PARENT_CLASS = 'K5_G8_DEFECT_FINAL_MATCHING_CONTRIBUTION'
MT = ((0,1),(2,3),(4,5),(6,7),(8,9))

LABEL_FRAME = 'K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED'
VALUE_REL = 'K5_G8_MATCHING_COEFF_VALUE_RELATION_DEFECT'
DIRECT_EXACT = 'K5_G8_MATCHING_COEFF_DIRECT_TARGET_RELATION_EXACT'
INVALID = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def coeff_json(c):
    return [[str(x) for x in ch] for ch in c]


def neg_coeff(c):
    return tuple(tuple(-Fraction(x) for x in ch) for ch in c)


def table_hash(table):
    h = hashlib.sha256()
    for mt, c in sorted(table.items()):
        h.update((repr(mt) + '|').encode())
        for ch in c:
            h.update((str(ch[0]) + ',' + str(ch[1]) + ';').encode())
        h.update(b'\n')
    return h.hexdigest()


def perfect_matching(mt):
    if len(mt) != 5:
        return False
    flat = []
    for pair in mt:
        if len(pair) != 2 or pair[0] >= pair[1]:
            return False
        flat.extend(pair)
    return sorted(flat) == list(range(10))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    prereg_text = PREREG.read_text(encoding='utf-8')
    parent = json.loads(PARENT.read_text(encoding='utf-8'))
    r1 = load(R1, 'critic_g8_label_r1')
    r2 = load(R2, 'critic_g8_label_r2')
    pc = load(PC, 'critic_g8_label_pc')

    C = tuple(r1.CYCLE)
    EDGES = tuple(r1.EDGES)
    EIDX = {e: i for i, e in enumerate(EDGES)}

    def ep_independent(p, i):
        a, b = EDGES[i]
        x, y = p[a], p[b]
        return EIDX[(min(x, y), max(x, y))]

    def invperm(p):
        return tuple(p.index(i) for i in range(len(p)))

    def forward_mt(mt, p=C):
        out = []
        for i, j in mt:
            a, b = ep_independent(p, i), ep_independent(p, j)
            out.append((min(a, b), max(a, b)))
        return tuple(sorted(out))

    canonical = dict(r1.MATCH_COEFF)
    pullback = dict(r1.S5_MATCH_COEFF_CYCLE)
    repair2 = dict(r2.S5_MATCH_COEFF_CYCLE)

    old_keys = sorted(canonical)
    mapping = {mt: forward_mt(mt) for mt in old_keys}
    target_keys = list(mapping.values())
    inverseC = invperm(C)

    push = {}
    collision = False
    for mt in old_keys:
        tmt = mapping[mt]
        if tmt in push:
            collision = True
        push[tmt] = pullback[mt]

    def first_relation_mismatch(left_fn, right_fn):
        for mt in old_keys:
            l = left_fn(mt)
            r = right_fn(mt)
            if l != r:
                return {
                    'old_matching': [list(x) for x in mt],
                    'target_matching': [list(x) for x in mapping[mt]],
                    'left': coeff_json(l),
                    'right': coeff_json(r),
                }
        return None

    l1_mismatch = first_relation_mismatch(lambda mt: pullback[mt], lambda mt: canonical[mt])
    l1 = l1_mismatch is None

    l2_mismatch = first_relation_mismatch(lambda mt: push[mapping[mt]], lambda mt: canonical[mt])
    l2 = l2_mismatch is None

    l3_mismatch = first_relation_mismatch(lambda mt: pullback[mapping[mt]], lambda mt: canonical[mt])
    l3 = l3_mismatch is None

    TMT = mapping[MT]
    frozen_direct_equal = pullback[TMT] == canonical[MT]
    frozen_push_equal = push[TMT] == canonical[MT]

    old = pc.geometry(pc.MASK, pc.WEIGHTS)
    target = pc.geometry(pc.TMASK, pc.TWEIGHTS)
    old_base = pc.matching_base(MT, old['cov'], old['F'])
    target_base = pc.matching_base(TMT, target['cov'], target['F'])
    geometry_base_exact = pc.deq(old_base, target_base)

    old_contrib = pc.weighted_contribution(MT, canonical[MT], old['cov'], old['F'])
    parent_direct_contrib = pc.weighted_contribution(TMT, pullback[TMT], target['cov'], target['F'])
    corrected_contrib = pc.weighted_contribution(TMT, push[TMT], target['cov'], target['F'])
    parent_direct_contrib_equal = pc.contrib_eq(old_contrib, parent_direct_contrib)
    corrected_contrib_equal = pc.contrib_eq(old_contrib, corrected_contrib)
    l4 = geometry_base_exact and (not parent_direct_contrib_equal) and corrected_contrib_equal

    l5 = repair2 == pullback

    parent_stages = parent.get('stages', {})
    validity = {
        'prereg_commit_locked': PREREG_COMMIT == 'e0b8432e71b97cd169a909c27d1a93b92d9f0ef5',
        'prereg_present': 'matching-coefficient label-frame relation' in prereg_text,
        'parent_persistence_commit_locked': PARENT_PERSIST_COMMIT == '65095d15ddb94996d6e331fd9d032f7bd51c0745',
        'parent_run_locked': parent.get('production', {}).get('run_id') == PARENT_RUN,
        'parent_job_locked': parent.get('production', {}).get('job_id') == PARENT_JOB,
        'parent_head_locked': parent.get('production', {}).get('head_sha') == PARENT_HEAD,
        'parent_artifact_locked': parent.get('production', {}).get('artifact_id') == PARENT_ARTIFACT,
        'parent_zip_hash_locked': parent.get('production', {}).get('artifact_zip_sha256') == PARENT_ZIP_SHA256,
        'parent_json_hash_locked': parent.get('production', {}).get('g8_diagnostic_json_sha256') == PARENT_JSON_SHA256,
        'parent_classification_locked': parent.get('classification') == PARENT_CLASS,
        'parent_H1_H6_true': all(parent_stages.get(k) is True for k in (
            'H1_edge_pair_permutation',
            'H2_orientation_cocycle_sign',
            'H3_covariance_index_convention',
            'H4_per_pair_covariance_factor',
            'H5_ordered_product_assembly',
            'H6_factor_multiset_assembly',
        )),
        'parent_H7_false': parent_stages.get('H7_final_matching_contribution') is False,
        'parent_q18_unused': parent.get('q18_values_used') is False,
        'parent_N_B_unused': parent.get('N_B_orders_or_coefficients_used') is False,
        'canonical_ten_edges': len(EDGES) == 10,
        'edge_map_agrees_with_authoritative_s5': all(ep_independent(C, i) == r1.s5.ep(C, i) for i in range(10)),
        'canonical_matching_count_945': len(canonical) == 945,
        'pullback_matching_count_945': len(pullback) == 945,
        'repair2_matching_count_945': len(repair2) == 945,
        'all_canonical_keys_perfect': all(perfect_matching(mt) for mt in canonical),
        'all_pullback_keys_perfect': all(perfect_matching(mt) for mt in pullback),
        'forward_map_bijection_all945': len(set(target_keys)) == 945 and not collision,
        'forward_map_hits_pullback_keyset': set(target_keys) == set(pullback),
        'forward_inverse_roundtrip_all945': all(forward_mt(mapping[mt], inverseC) == mt for mt in old_keys),
        'all_coefficients_exact_fraction': all(
            isinstance(x, Fraction)
            for table in (canonical, pullback, repair2)
            for coeffs in table.values()
            for ch in coeffs
            for x in ch
        ),
        'source_terms_exactly_100000': r1._SOURCE_TERM_COUNT == 100000,
        'frozen_matching_present': MT in canonical and TMT in pullback,
    }

    # Mandatory malformed controls.
    direct_as_target_rejected = not l3 and not frozen_direct_equal

    wrong_inverse_mismatch = None
    wrong_inverse_rejected = False
    for mt in old_keys:
        wrong_tmt = forward_mt(mt, inverseC)
        if pullback[wrong_tmt] != canonical[mt]:
            wrong_inverse_rejected = True
            wrong_inverse_mismatch = {
                'old_matching': [list(x) for x in mt],
                'wrong_target_matching': [list(x) for x in wrong_tmt],
                'wrong_lookup': coeff_json(pullback[wrong_tmt]),
                'canonical': coeff_json(canonical[mt]),
            }
            break

    extra_minus_rejected = any(neg_coeff(push[mapping[mt]]) != canonical[mt] for mt in old_keys)

    first_two = old_keys[:2]
    mutated = dict(push)
    k0, k1 = mapping[first_two[0]], mapping[first_two[1]]
    mutated[k0], mutated[k1] = mutated[k1], mutated[k0]
    swapped_first_two_rejected = (
        mutated[k0] != canonical[first_two[0]]
        or mutated[k1] != canonical[first_two[1]]
    )

    malformed = {
        'direct_pullback_as_target_rejected': direct_as_target_rejected,
        'inverse_edge_permutation_rejected': wrong_inverse_rejected,
        'extra_global_minus_rejected': extra_minus_rejected,
        'swap_first_two_target_keys_rejected': swapped_first_two_rejected,
    }

    if not all(validity.values()) or not all(malformed.values()):
        classification = INVALID
    elif l3:
        classification = DIRECT_EXACT
    elif l1 and l2 and (not l3) and (not frozen_direct_equal) and frozen_push_equal and l4:
        classification = LABEL_FRAME
    else:
        classification = VALUE_REL

    out = {
        'gate': 'K5_G8_MATCHING_COEFFICIENT_LABEL_FRAME_RELATION_INDEPENDENT_CRITIC_DIAGNOSTIC',
        'classification': classification,
        'scientific_verdict': None,
        'prereg_commit': PREREG_COMMIT,
        'parent_terminal_persistence_commit': PARENT_PERSIST_COMMIT,
        'parent_run': PARENT_RUN,
        'frozen': {
            'cycle': list(C),
            'old_matching': [list(x) for x in MT],
            'target_matching': [list(x) for x in TMT],
        },
        'validity': validity,
        'relations': {
            'L1_pullback_table_equals_canonical_all945': l1,
            'L2_pushforward_target_covariance_all945': l2,
            'L3_direct_pullback_as_target_all945': l3,
            'L3_frozen_direct_equal': frozen_direct_equal,
            'L3_frozen_pushforward_equal': frozen_push_equal,
            'L4_geometry_base_exact': geometry_base_exact,
            'L4_parent_direct_contribution_equal': parent_direct_contrib_equal,
            'L4_corrected_pushforward_contribution_equal': corrected_contrib_equal,
            'L4_repaired_exact': l4,
            'L5_repair2_collapsed_equals_repair1_pullback': l5,
        },
        'first_mismatches': {
            'L1': l1_mismatch,
            'L2': l2_mismatch,
            'L3': l3_mismatch,
            'wrong_inverse_control': wrong_inverse_mismatch,
        },
        'frozen_coefficients': {
            'canonical_old': coeff_json(canonical[MT]),
            'pullback_at_old_key': coeff_json(pullback[MT]),
            'malformed_direct_pullback_at_target_key': coeff_json(pullback[TMT]),
            'corrected_pushforward_at_target_key': coeff_json(push[TMT]),
        },
        'hashes': {
            'canonical_table_sha256': table_hash(canonical),
            'pullback_table_sha256': table_hash(pullback),
            'pushforward_table_sha256': table_hash(push),
            'repair2_collapsed_table_sha256': table_hash(repair2),
            'old_base_sha256': pc.seq_hash(old_base),
            'target_base_sha256': pc.seq_hash(target_base),
        },
        'malformed_controls': malformed,
        'q18_values_used': False,
        'N_B_orders_or_coefficients_used': False,
        'heavy_resolver_authorized': False,
        'global_stokes_authorized': False,
        'interpretation_ceiling': 'implementation-only G8/H7 matching-label localization; resolver authority remains 0/64',
    }

    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('CLASSIFICATION=' + classification)
    print('RELATIONS=' + json.dumps(out['relations'], sort_keys=True))
    print('MALFORMED=' + json.dumps(malformed, sort_keys=True))
    print('HASHES=' + json.dumps(out['hashes'], sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
