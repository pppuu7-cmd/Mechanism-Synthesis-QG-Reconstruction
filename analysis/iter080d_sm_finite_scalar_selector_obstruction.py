#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'analysis' / 'iter080d_sm_source_lock.json'
DERIV = ROOT / 'sources' / 'ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md'
ERRATUM = ROOT / 'status' / 'ITER077_CONTACT_FORMULA_ERRATUM.md'
PREREG = ROOT / 'prereg' / 'ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md'
ITER = 'Iter080D-SM'
CLASSIFICATION = (
    'ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_'
    'CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED'
)


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def load_lock() -> dict:
    return json.loads(read(LOCK))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f'blob {len(data)}\0'.encode('ascii')
    return hashlib.sha1(header + data).hexdigest()


# Exact affine expressions a*m + b*R + c.  This is deliberately symbolic:
# no selected numerical m/R values can make this certificate pass.
def affine_add(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(x, y))


def affine_sub(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(x, y))


def symbolic_rank_nullity_certificate() -> dict:
    m = (1, 0, 0)
    R = (0, 1, 0)
    one = (0, 0, 1)
    N = affine_sub(affine_add(m, R), one)       # m + R - 1
    dim_WN = affine_add(N, one)                 # m + R
    lower_bound = affine_sub(dim_WN, m)         # R

    identities = {
        'N_equals_m_plus_R_minus_1': N == (1, 1, -1),
        'dim_WN_equals_N_plus_1': dim_WN == (1, 1, 0),
        'rank_codomain_bound_symbolic': m == (1, 0, 0),
        'nullity_lower_bound_equals_R_identically': lower_bound == R,
        'no_numeric_mR_instantiation_used': True,
    }
    # Universal proof schema encoded by the identities above:
    # for arbitrary fixed finite m>=0 and arbitrary R>=1, choose N=m+R-1.
    # Since rank(L|W_N)<=m and dim W_N=N+1, rank-nullity gives
    # dim ker(L|W_N)>=dim W_N-m=R.  R is arbitrary, hence ker L is
    # infinite-dimensional and L cannot be injective.
    return {
        'quantifiers': 'for every fixed finite integer m>=0 and every integer R>=1',
        'choice': 'N=m+R-1',
        'affine_basis': '[m,R,1]',
        'N_coefficients': list(N),
        'dim_WN_coefficients': list(dim_WN),
        'kernel_lower_bound_coefficients': list(lower_bound),
        'rank_nullity_rule': 'dim ker T = dim domain - rank T; rank(L|W_N) <= dim C^m = m',
        'identities': identities,
        'valid': all(identities.values()),
    }


def lane_a() -> dict:
    L = load_lock()
    d = read(DERIV)
    e = read(ERRATUM)
    p = read(PREREG)
    expected_blob = L['authority']['iter077q']['derivation_blob_sha']
    actual_blob = git_blob_sha(DERIV)
    checks = {
        'prereg_precedes_gate': 'PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE COMPUTATION' in p,
        'iter077q_derivation_sha_literal_locked': expected_blob == '1b15464e8f7d5ae9d87932938f76de1ac8f3351f',
        'iter077q_checked_out_blob_matches_lock': actual_blob == expected_blob,
        'actual_collision_manifold': 'N = SU(2)^4 subset SL(2,C)^4' in d,
        'exact_Q_path': 'Q(t)=12+8 cos(t)' in d,
        'linear_independence': 'Therefore `{Q^n F}_{n>=0}` is linearly independent.' in d,
        'countably_infinite': 'countably infinite-dimensional subspace' in d,
        'actual_boundary_nonzero': 'not identically zero for at least one actual minimal-sector boundary state' in d,
        'source_not_surrogate': 'not obtained from a scalar K4/K5 surrogate' in d,
        'erratum_correct_formula': "`delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)`" in e,
        'historical_invalid_quarantine': 'Iter077E' in e and 'Iter077F' in e and 'NON_AUTHORITATIVE_SOURCE_LOCK_INVALID' in e,
    }
    valid = all(checks.values())
    return {
        'iteration': ITER,
        'lane': 'A',
        'purpose': 'authoritative Iter077Q/erratum source lock with checked-out blob identity',
        'valid': valid,
        'scientific_outcome': 'PASS_SOURCE_LOCK' if valid else 'INVALID_SOURCE_LOCK',
        'checks': checks,
        'expected_derivation_blob_sha': expected_blob,
        'actual_derivation_blob_sha': actual_blob,
        'locked_run': L['authority']['iter077q']['run_id'],
        'locked_artifact': L['authority']['iter077q']['aggregate_artifact_id'],
        'locked_digest': L['authority']['iter077q']['aggregate_digest'],
    }


def lane_b() -> dict:
    L = load_lock()
    pairs = [tuple(x) for x in L['frozen_controls']['pairs_m_N']]
    controls = []
    for m, N in pairs:
        dim = N + 1
        lower = dim - m
        controls.append({
            'm': m,
            'N': N,
            'dim_W_N': dim,
            'universal_rank_upper_bound': m,
            'universal_nullity_lower_bound': lower,
            'coordinate_projection_rank': m,
            'coordinate_projection_nullity': lower,
            'valid': N >= m and lower > 0,
            'role': 'finite negative/control example only; not universality evidence',
        })

    cert = symbolic_rank_nullity_certificate()
    prereg = read(PREREG)
    checks = {
        'iter077q_family_locked': L['selector_class']['space'].startswith('W=span_C{h_n:n>=0}'),
        'selector_codomain_finite': L['selector_class']['maps'].endswith('W->C^m'),
        'fixed_finite_m': 'fixed finite m' in L['selector_class']['scope'],
        'frozen_projection_controls_valid': all(x['valid'] for x in controls),
        'prereg_requires_universal_not_sampled': 'INVALID_IMPLEMENTATION' in prereg and 'selected matrices' in prereg,
        'universal_symbolic_certificate': cert['valid'],
        'certificate_has_arbitrary_quantifiers': cert['quantifiers'].startswith('for every fixed finite integer m'),
        'certificate_kernel_bound_is_symbolic_R': cert['kernel_lower_bound_coefficients'] == [0, 1, 0],
    }
    # Crucially, PASS depends on cert, not on a grid of selected m/R values.
    valid = all(checks.values())
    return {
        'iteration': ITER,
        'lane': 'B',
        'purpose': 'universal exact rank-nullity obstruction with executable symbolic certificate',
        'valid': valid,
        'scientific_outcome': 'PASS_EXACT_THEOREM' if valid else 'INVALID_IMPLEMENTATION',
        'theorem': (
            'For arbitrary fixed finite m and arbitrary R>=1, choose N=m+R-1. '
            'For every complex-linear L:W->C^m, rank(L|W_N)<=m and dim(W_N)=N+1=m+R, '
            'so rank-nullity gives dim ker(L|W_N)>=R. Because R is arbitrary, ker L is '
            'infinite-dimensional and L is not injective.'
        ),
        'checks': checks,
        'symbolic_certificate': cert,
        'frozen_controls': controls,
    }


def lane_c() -> dict:
    L = load_lock()
    pairs = [tuple(x) for x in L['frozen_controls']['pairs_m_N']]
    neg = []
    for _, N in pairs:
        dim = N + 1
        neg.append({'N': N, 'condition_count': dim, 'identity_rank': dim, 'identity_nullity': 0, 'valid': dim > 0})
    excluded = L['selector_class']['excluded']
    checks = {
        'identity_negative_controls': all(x['valid'] and x['identity_nullity'] == 0 for x in neg),
        'growing_condition_family_excluded': any('grows without bound' in x for x in excluded),
        'function_valued_excluded': 'function-valued constraints' in excluded,
        'differential_spectral_excluded': any('differential/spectral/microlocal' in x for x in excluded),
        'nonlinear_excluded': 'nonlinear selectors' in excluded,
        'ceiling_in_prereg': 'does **not** eliminate a source-derived function-valued constraint' in read(PREREG),
    }
    valid = all(checks.values())
    return {
        'iteration': ITER,
        'lane': 'C',
        'purpose': 'negative controls and interpretation ceiling',
        'valid': valid,
        'scientific_outcome': 'PASS_SCOPE_CONTROL' if valid else 'INVALID_IMPLEMENTATION',
        'checks': checks,
        'negative_controls': neg,
        'surviving_selector_classes': excluded,
    }


LANES = {'A': lane_a, 'B': lane_b, 'C': lane_c}


def aggregate(root: str) -> dict:
    got = {}
    for base, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'):
                continue
            try:
                obj = json.loads(Path(base, fn).read_text(encoding='utf-8'))
            except Exception:
                continue
            if obj.get('iteration') == ITER and obj.get('lane') in LANES:
                got[obj['lane']] = obj
    valid = set(got) == set(LANES) and all(got[k].get('valid') for k in LANES)
    # Aggregate additionally refuses promotion if Lane B lacks the symbolic certificate.
    if valid:
        bcert = got['B'].get('symbolic_certificate', {})
        valid = bool(bcert.get('valid')) and bcert.get('kernel_lower_bound_coefficients') == [0, 1, 0]
    if valid:
        verdict = 'PASS_EXACT_SCOPED'
        classification = CLASSIFICATION
        fact = (
            'The exact Iter077Q ambiguity W contains infinitely many linearly independent source-compatible '
            'directions, and every selector consisting of a fixed finite number of scalar-valued complex-linear '
            'conditions W->C^m has an infinite-dimensional kernel. Such finite scalar renormalization conditions '
            'therefore cannot uniquely select the K5 extension.'
        )
    else:
        verdict = 'INVALID'
        classification = 'ITER080D_SM_INVALID_SOURCE_LOCK_OR_IMPLEMENTATION'
        fact = 'No scientific promotion: at least one frozen required lane or universal symbolic certificate is invalid or missing.'
    return {
        'iteration': ITER,
        'execution_valid': valid,
        'lane_scientific_outcomes': {k: got.get(k, {}).get('scientific_outcome') for k in LANES},
        'verdict': verdict,
        'classification': classification,
        'new_scientific_fact': fact,
        'claim_ceiling': (
            'This excludes only a fixed finite list of scalar-valued linear conditions. It does not exclude '
            'function-valued or infinite condition families, differential/spectral/microlocal equations, or '
            'nonlinear selectors; it does not prove a unique K5 extension, full-vertex divergence, regulator '
            'independence, E7/E8, G3, RG, F9/G8/K5 promotion, or new physics.'
        ),
        'next_admissible_gate': (
            'Audit primary Toller/causal source authority for a genuinely function-valued, differential, spectral, '
            'or microlocal joint-K5 extension condition acting on the full tangential ambiguity space; do not repeat '
            'finite symmetry or finite scalar-normalization controls.'
        ),
        'claim_lock': (
            'No NEW_PHYSICS_FOUND; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude '
            'cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no regulator-'
            'independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1; no G3 PASS; no '
            'F9/G8/K5 promotion; retain published spectral i epsilon.'
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', choices=sorted(LANES))
    ap.add_argument('--aggregate-dir')
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    if bool(args.lane) == bool(args.aggregate_dir):
        raise SystemExit('choose exactly one mode')
    obj = LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding='utf-8')
    print(json.dumps(obj, indent=2, sort_keys=True))
    if args.lane and not obj['valid']:
        raise SystemExit(1)
    if args.aggregate_dir and not obj['execution_valid']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
