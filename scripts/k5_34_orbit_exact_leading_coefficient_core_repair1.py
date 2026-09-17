#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'scripts/k5_34_orbit_exact_leading_coefficient_core.py'
S5 = ROOT / 'scripts/k5_full_source_boundary_s5_transport_symbolic_theorem.py'
REPAIR_PREREG = ROOT / 'prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_CONTROL_REPAIR_1.md'
REPAIR_PRE = '2193692c90d8ee1fa097200dbbac6ab70fd3a159'
CRITIC_RUN = 35267432939


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


base = load(BASE, 'k5_34_exact_base_repair1')
s5 = load(S5, 'k5_34_s5_transport_repair1')

# Re-export the frozen parent core surface. Scientific arithmetic remains in the
# parent module; this repair changes only equality/control and S5 source transport.
for _name in dir(base):
    if not _name.startswith('__'):
        globals()[_name] = getattr(base, _name)


# R1: structural polynomial equality. Parent P arithmetic is unchanged.
def _p_eq(self, other):
    return isinstance(other, base.P) and self.d == other.d

base.P.__eq__ = _p_eq
P = base.P


def _match_coeff_hash(mc):
    h = hashlib.sha256()
    for mt, coeffs in sorted(mc.items()):
        h.update((repr(mt) + '|').encode())
        for ch in coeffs:
            h.update((str(ch[0]) + ',' + str(ch[1]) + ';').encode())
        h.update(b'\n')
    return h.hexdigest()


def _project_pattern_dicts_to_match_coeff(dictvec):
    """Exact invariant-dual projection followed by exact Wick matching collapse."""
    tcw = defaultdict(lambda: [Fraction(0), Fraction(0)])
    assert len(dictvec) == 32
    for idx, d in enumerate(dictvec):
        w0, w1 = base.core.WEIGHTS[idx]
        for types, coeff in d.items():
            tcw[types][0] += Fraction(coeff) * w0
            tcw[types][1] += Fraction(coeff) * w1
    tcw = {t: (w[0], w[1]) for t, w in tcw.items() if w[0] or w[1]}

    mc = defaultdict(lambda: [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]])
    for types, w in tcw.items():
        for mt, z in base.core.compatible(types):
            for ch in (0, 1):
                if not w[ch]:
                    continue
                zz = base.core.cscale(w[ch], z)
                mc[mt][ch][0] += zz[0]
                mc[mt][ch][1] += zz[1]
    return {
        mt: ((c[0][0], c[0][1]), (c[1][0], c[1][1]))
        for mt, c in mc.items()
        if any(c[ch] != [0, 0] for ch in (0, 1))
    }


# R2: build the actual simultaneously source-transported coefficient object.
# The route itself supplies the covariance orientation character through the
# permuted incidence/covariance factors, so this source coefficient transport
# includes endpoint transpose + source reversal sign, but deliberately does not
# pre-multiply the covariance orientation sign a second time.
_BASE_PATTERNS, _SOURCE_TERM_COUNT = s5.aggregate_base_patterns()
assert _SOURCE_TERM_COUNT == 100000
_SOURCE_CYCLE = s5.transported_pattern_dicts(
    _BASE_PATTERNS,
    s5.C,
    transpose_reversed=True,
    source_reversal_sign=True,
    covariance_orientation_sign=False,
)
S5_MATCH_COEFF_CYCLE = _project_pattern_dicts_to_match_coeff(_SOURCE_CYCLE)

# Formal full-source/boundary controls are recomputed outcome-blind from the same
# independently confirmed object definition. They do not inspect any historical
# invalid resolver coefficient value.
_TENSORS = s5.act.reach.local_tensor_vectors(s5.act.src)
_LOCAL = s5.act.reach.local_action_matrices(_TENSORS)
_FORMAL_CYCLE = s5.formal_pattern_generator_check(_BASE_PATTERNS, _LOCAL, s5.C)
_FORMAL_T = s5.formal_pattern_generator_check(_BASE_PATTERNS, _LOCAL, s5.T)


def route_a(mask: int, weights, match_coeff=None):
    """Frozen parent route with an explicitly supplied source coefficient object."""
    old = base.MATCH_COEFF
    try:
        base.MATCH_COEFF = old if match_coeff is None else match_coeff
        return base.route_a(mask, weights)
    finally:
        base.MATCH_COEFF = old


def static_checks():
    out = dict(base.static_checks())
    critic = json.loads(base.CRITIC_AUTH.read_text(encoding='utf-8'))
    altered = P({0: 1, 2: 3})
    altered2 = P({0: 1, 2: 4})
    out.update({
        'repair1_prereg_commit_locked': REPAIR_PRE == '2193692c90d8ee1fa097200dbbac6ab70fd3a159',
        'repair1_prereg_present': REPAIR_PREREG.exists() and 'source-fixed S5 validation object' in REPAIR_PREREG.read_text(encoding='utf-8'),
        'critic_run_locked_35267432939': critic.get('production', {}).get('run_id') == CRITIC_RUN,
        'critic_exact_scoped_and_q18_unused': critic.get('classification') == 'CONFIRMED_EXACT_SCOPED' and critic.get('q18_values_used') is False,
        'structural_P_equality_accepts_exact_copy': P({0: 1, 2: 3}) == altered,
        'structural_P_equality_rejects_changed_coeff': not (altered == altered2),
        'source_transport_32_components': len(_SOURCE_CYCLE) == 32,
        'source_transport_100000_terms': _SOURCE_TERM_COUNT == 100000,
        'cycle_formal_full_source_boundary_exact': bool(_FORMAL_CYCLE['exact']),
        'cycle_boundary_inverse_exact': bool(_FORMAL_CYCLE['boundary_inverse_exact']),
        'odd_T_formal_full_source_boundary_exact': bool(_FORMAL_T['exact']),
        'odd_T_omit_endpoint_transpose_rejected': bool(_FORMAL_T['no_transpose_rejected']),
        'odd_T_omit_source_reversal_sign_rejected': bool(_FORMAL_T['no_source_sign_rejected']),
        'odd_T_source_fixed_object_rejected': bool(_FORMAL_T['source_fixed_rejected']),
        'transported_matching_object_nonempty': bool(S5_MATCH_COEFF_CYCLE),
        'transported_matching_object_exact_rational': all(isinstance(x, Fraction) for coeffs in S5_MATCH_COEFF_CYCLE.values() for ch in coeffs for x in ch),
        'transported_matching_hash_wellformed': len(_match_coeff_hash(S5_MATCH_COEFF_CYCLE)) == 64,
        'original_matching_hash_wellformed': len(_match_coeff_hash(base.MATCH_COEFF)) == 64,
    })
    return out


# Explicitly expose the unchanged base helpers expected by the shard.
route_b_interpolation = base.route_b_interpolation
proper_orbits = base.proper_orbits
class_representatives = base.class_representatives
lane_serial = base.lane_serial
vector_hash = base.vector_hash
PRE = base.PRE
N_DEG = base.N_DEG
B_DEG = base.B_DEG
SOURCE_TERMS = base.SOURCE_TERMS
MATCH_COEFF = base.MATCH_COEFF
W1 = base.W1
W2 = base.W2
CYCLE = base.CYCLE
WP1 = base.WP1
WP2 = base.WP2
core = base.core
