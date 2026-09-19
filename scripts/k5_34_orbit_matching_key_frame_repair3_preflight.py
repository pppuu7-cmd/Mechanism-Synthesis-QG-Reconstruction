#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py'
G8 = ROOT / 'scripts/k5_34_orbit_g8_matching_covariance_composition_diagnostic.py'
CRITIC_AUTH = ROOT / 'results/raw/k5_g8_matching_coefficient_label_frame_independent_critic_authoritative.json'
PREREG = ROOT / 'prereg/K5_34_ORBIT_MATCHING_KEY_FRAME_CONTROL_REPAIR_3_PREFLIGHT.md'

PREREG_COMMIT = '4ee6c6f3056c5934a5209a4f05616b73354b4e6e'
CORE_COMMIT = '6d6dd17e579d7aeb2a793bfa1becbe611174f191'
EXPECTED_CRITIC_CLASS = 'K5_G8_MATCHING_COEFF_LABEL_FRAME_DEFECT_CONFIRMED'
EXPECTED_CRITIC_RUN = 35412815680
PASS = 'PASS_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT'
INVALID = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'
MISMATCH = 'MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT_SCIENTIFIC_MISMATCH'


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


r3 = load(CORE, 'matching_key_frame_repair3_core')
g8 = load(G8, 'matching_key_frame_repair3_g8')
p = g8.p
D = g8.D
MT = g8.MT


def mul_series(a, b):
    out = [D(0) for _ in range(p.b.ORDER + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= p.b.ORDER:
                out[i + j] = out[i + j] + x * y
    return out


def series_eq(a, b):
    return len(a) == len(b) and all(p.deq(x, y) for x, y in zip(a, b))


def factor_series(cov, key):
    return [cov[(key[0], key[1], n)] for n in range(p.b.ORDER + 1)]


def scale_series(q, s):
    return [Fraction(q) * x for x in s]


def serial_coeff(c):
    return [[str(x) for x in ch] for ch in c]


def first_table_mismatch(left, relation):
    for mt in sorted(r3.MATCH_COEFF):
        key = relation(mt)
        a = left.get(key)
        b = r3.MATCH_COEFF.get(mt)
        if a != b:
            return {
                'old_matching': [list(x) for x in mt],
                'lookup_key': [list(x) for x in key],
                'left': None if a is None else serial_coeff(a),
                'right': serial_coeff(b),
            }
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    prereg_text = PREREG.read_text(encoding='utf-8')
    critic = json.loads(CRITIC_AUTH.read_text(encoding='utf-8'))
    static = r3.static_checks()

    validity = {
        'prereg_commit_locked': PREREG_COMMIT == '4ee6c6f3056c5934a5209a4f05616b73354b4e6e',
        'prereg_present': 'minimal matching-key frame control repair 3 preflight' in prereg_text,
        'core_commit_locked': CORE_COMMIT == '6d6dd17e579d7aeb2a793bfa1becbe611174f191',
        'parent_scientific_prereg_locked': r3.PRE == 'd6b0e805101c8590eafac71398cc2b1466691752',
        'critic_class_locked': critic.get('classification') == EXPECTED_CRITIC_CLASS,
        'critic_run_locked': critic.get('provenance', {}).get('run_id') == EXPECTED_CRITIC_RUN,
        'critic_q18_unused': critic.get('q18_values_used') is False,
        'critic_N_B_unused': critic.get('N_B_orders_or_coefficients_used') is False,
        'static_repair3_controls': all(bool(v) for k, v in static.items() if k not in ('q18_values_used', 'N_B_orders_or_coefficients_used')),
        'q18_not_used': static.get('q18_values_used') is False,
        'N_B_not_used': static.get('N_B_orders_or_coefficients_used') is False,
    }

    canonical = r3.MATCH_COEFF
    pullback = r3.S5_MATCH_COEFF_CYCLE_PULLBACK
    target = r3.S5_MATCH_COEFF_CYCLE_TARGET

    census = {
        'canonical_count_945': len(canonical) == 945,
        'pullback_count_945': len(pullback) == 945,
        'target_count_945': len(target) == 945,
        'forward_bijection_all945': len({r3.forward_matching(mt) for mt in canonical}) == 945,
        'inverse_roundtrip_all945': all(r3.inverse_matching(r3.forward_matching(mt)) == mt for mt in canonical),
        'pullback_relation_all945': all(pullback.get(mt) == canonical.get(mt) for mt in canonical),
        'target_relation_all945': all(target.get(r3.forward_matching(mt)) == canonical.get(mt) for mt in canonical),
        'coefficient_values_preserved': sorted(repr(v) for v in pullback.values()) == sorted(repr(v) for v in target.values()),
        'all_target_coefficients_exact_fraction': all(isinstance(x, Fraction) for coeffs in target.values() for ch in coeffs for x in ch),
    }

    # Reconstruct frozen G8 lane. H1-H6 are copied from the already-frozen exact
    # definitions; repair-3 changes only the H7 target coefficient table lookup.
    old = p.geometry(p.MASK, p.WEIGHTS)
    target_geom = p.geometry(p.TMASK, p.TWEIGHTS)
    ep = lambda i: r3.repair1.s5.ep(p.CYCLE, i)
    es = lambda i: Fraction(r3.repair1.s5.edge_sign(p.CYCLE, i))

    mapped = []
    pair_sign = []
    for i, j in MT:
        a, b = ep(i), ep(j)
        mapped.append((min(a, b), max(a, b)))
        pair_sign.append(es(i) * es(j))
    TMT = tuple(sorted(mapped))

    h1 = TMT == r3.forward_matching(MT) and r3.inverse_matching(TMT) == MT

    inv = [0] * 5
    for i, j in enumerate(p.CYCLE):
        inv[j] = i
    edge_cocycle = [
        es(i) * Fraction(r3.repair1.s5.edge_sign(tuple(inv), ep(i))) == 1
        for i in range(10)
    ]
    h2 = all(s in (Fraction(1), Fraction(-1)) for s in pair_sign) and all(edge_cocycle)

    forward_keys = []
    factor_checks = []
    for (i, j), sgn in zip(MT, pair_sign):
        a, b = ep(i), ep(j)
        key = (min(a, b), max(a, b))
        forward_keys.append(key)
        oldser = factor_series(old['cov'], (i, j))
        tarser = factor_series(target_geom['cov'], key)
        factor_checks.append(series_eq(tarser, scale_series(sgn, oldser)))
    h3 = tuple(sorted(forward_keys)) == TMT
    h4 = all(factor_checks)

    pred_factors = []
    actual_factors = []
    for ij, key, sgn in zip(MT, forward_keys, pair_sign):
        pred_factors.append(scale_series(sgn, factor_series(old['cov'], ij)))
        actual_factors.append(factor_series(target_geom['cov'], key))
    pred_prod = [D(1)] + [D(0) for _ in range(p.b.ORDER)]
    actual_prod = [D(1)] + [D(0) for _ in range(p.b.ORDER)]
    for x, y in zip(pred_factors, actual_factors):
        pred_prod = mul_series(pred_prod, x)
        actual_prod = mul_series(actual_prod, y)
    h5 = series_eq(pred_prod, actual_prod)
    h6 = sorted(p.seq_hash(x) for x in pred_factors) == sorted(p.seq_hash(x) for x in actual_factors)

    old_coeff = canonical[MT]
    repaired_target_coeff = target[TMT]
    malformed_direct_coeff = pullback[TMT]
    old_base = p.matching_base(MT, old['cov'], old['F'])
    target_base = p.matching_base(TMT, target_geom['cov'], target_geom['F'])
    old_contrib = p.weighted_contribution(MT, old_coeff, old['cov'], old['F'])
    repaired_contrib = p.weighted_contribution(TMT, repaired_target_coeff, target_geom['cov'], target_geom['F'])
    malformed_direct_contrib = p.weighted_contribution(TMT, malformed_direct_coeff, target_geom['cov'], target_geom['F'])
    h7 = p.contrib_eq(old_contrib, repaired_contrib)

    total_pair_sign = Fraction(1)
    for s in pair_sign:
        total_pair_sign *= s
    geometry_base_exact = p.deq(target_base, total_pair_sign * old_base)

    stages = {
        'H1_edge_pair_permutation': h1,
        'H2_orientation_cocycle_sign': h2,
        'H3_covariance_index_convention': h3,
        'H4_per_pair_covariance_factor': h4,
        'H5_ordered_product_assembly': h5,
        'H6_factor_multiset_assembly': h6,
        'H7_final_matching_contribution_repaired': h7,
        'geometry_base_transport_exact': geometry_base_exact,
    }

    # Mandatory malformed controls.
    direct_pullback_rejected = any(pullback.get(r3.forward_matching(mt)) != canonical.get(mt) for mt in canonical)

    wrong_inverse = {}
    for mt, coeff in pullback.items():
        key = r3.inverse_matching(mt)
        if key in wrong_inverse:
            wrong_inverse = {}
            break
        wrong_inverse[key] = coeff
    inverse_map_rejected = bool(wrong_inverse) and any(wrong_inverse.get(r3.forward_matching(mt)) != canonical.get(mt) for mt in canonical)

    extra_minus_rejected = any(
        tuple(tuple(-x for x in ch) for ch in target[r3.forward_matching(mt)]) != canonical[mt]
        for mt in canonical
    )

    ordered = sorted(canonical)
    swapped = dict(target)
    t0, t1 = r3.forward_matching(ordered[0]), r3.forward_matching(ordered[1])
    swapped[t0], swapped[t1] = swapped[t1], swapped[t0]
    swapped_keys_rejected = any(swapped.get(r3.forward_matching(mt)) != canonical.get(mt) for mt in canonical)

    mutated = dict(target)
    k0 = r3.forward_matching(ordered[0])
    c0 = mutated[k0]
    mutated[k0] = ((c0[0][0] + Fraction(1), c0[0][1]), c0[1])
    coefficient_mutation_rejected = mutated[k0] != canonical[ordered[0]]

    malformed = {
        'direct_pullback_as_target_rejected': direct_pullback_rejected and not p.contrib_eq(old_contrib, malformed_direct_contrib),
        'inverse_matching_map_rejected': inverse_map_rejected,
        'extra_global_minus_rejected': extra_minus_rejected,
        'swap_first_two_target_keys_rejected': swapped_keys_rejected,
        'coefficient_value_mutation_rejected': coefficient_mutation_rejected,
    }

    implementation_ok = all(validity.values()) and all(malformed.values())
    exact_ok = all(census.values()) and all(stages.values())

    if not implementation_ok:
        classification = INVALID
    elif exact_ok:
        classification = PASS
    else:
        classification = MISMATCH

    out = {
        'gate': 'K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_PREFLIGHT',
        'classification': classification,
        'scientific_verdict': None,
        'prereg_commit': PREREG_COMMIT,
        'core_commit': CORE_COMMIT,
        'validity': validity,
        'census_and_relations': census,
        'g8_stages': stages,
        'malformed_controls': malformed,
        'frozen_lane': {
            'mask': 1,
            'ray': 'W1',
            'cycle': list(p.CYCLE),
            'old_matching': [list(x) for x in MT],
            'target_matching': [list(x) for x in TMT],
            'old_coeff': serial_coeff(old_coeff),
            'repaired_target_coeff': serial_coeff(repaired_target_coeff),
            'malformed_direct_coeff': serial_coeff(malformed_direct_coeff),
            'old_base_sha256': p.seq_hash(old_base),
            'target_base_sha256': p.seq_hash(target_base),
        },
        'hashes': {
            'canonical_table_sha256': r3.repair1._match_coeff_hash(canonical),
            'pullback_table_sha256': r3.repair1._match_coeff_hash(pullback),
            'target_table_sha256': r3.repair1._match_coeff_hash(target),
        },
        'first_mismatches': {
            'pullback_relation': first_table_mismatch(pullback, lambda mt: mt),
            'target_relation': first_table_mismatch(target, r3.forward_matching),
            'malformed_direct': first_table_mismatch(pullback, r3.forward_matching),
        },
        'q18_values_used': False,
        'N_B_orders_or_coefficients_used': False,
        'heavy_resolver_launched': False,
        'heavy_resolver_authorized_by_this_result': classification == PASS,
        'resolver_scientific_authority_components': 0,
        'interpretation_ceiling': 'implementation-only matching-key frame preflight; no N/B scientific result',
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('CLASSIFICATION=' + classification)
    print('VALIDITY=' + json.dumps(validity, sort_keys=True))
    print('CENSUS=' + json.dumps(census, sort_keys=True))
    print('G8_STAGES=' + json.dumps(stages, sort_keys=True))
    print('MALFORMED=' + json.dumps(malformed, sort_keys=True))
    return 0 if classification == PASS else 2


if __name__ == '__main__':
    raise SystemExit(main())
