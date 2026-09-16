#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / 'results/raw/k5_deg4_annihilator_actual_dual_action_authoritative.json'
PREREG = ROOT / 'prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION.md'
DERIV = ROOT / 'sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md'
CRITIC_PREREG = ROOT / 'prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_ACTION_REPAIR1_INDEPENDENT_CRITIC_REVIEW.md'
OUT = ROOT / 'results/raw/critic_k5_deg4_constant_closure_object_audit.json'

s = json.loads(SUMMARY.read_text(encoding='utf-8'))
p = PREREG.read_text(encoding='utf-8')
d = DERIV.read_text(encoding='utf-8')
c = CRITIC_PREREG.read_text(encoding='utf-8')

N = tuple(Fraction(x) for x in s['uniform_control']['numerators'])
B = tuple(Fraction(x) for x in s['uniform_control']['actions'])
lam = Fraction(2)

# Independent grading counterexample. If a single constant M satisfied B(alpha)=M N(alpha)
# as a homogeneous-cone identity, then scaling alpha -> lam*alpha would require both
# B(lam alpha)=lam^31 B(alpha) and M N(lam alpha)=lam^27 B(alpha).
actual_scaled_B = tuple((lam ** 31) * x for x in B)
constant_M_scaled_prediction = tuple((lam ** 27) * x for x in B)
scaling_residual = tuple(a-b for a,b in zip(actual_scaled_B, constant_M_scaled_prediction))

checks = {
    'critic_prereg_present': 'REQUIRES_NEW_PREREGISTERED_GATE' in c,
    'researcher_classification_locked': s['classification'] == 'K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED',
    'researcher_reports_degree27_N': s['checks']['euler_degree_N'] == 27,
    'researcher_reports_degree31_B': s['checks']['action_homogeneous_degree'] == 31,
    'uniform_action_nonzero': all(x != 0 for x in B),
    'uniform_relation_minus1500': all(B[i] == -1500*N[i] for i in range(2)),
    'parent_prereg_explicit_B_degree31': 'homogeneous degree 31' in p,
    'parent_prereg_tests_raw_B_equals_MN': 'B_v[N](alpha) = M N(alpha)' in p,
    'derivation_defines_projective_P_degree27': 'P_v[N] = B_v[N]/s1^4' in d and 'degree-27 projective numerator' in d,
    'derivation_lists_projective_closure_after_P': 'whether the resulting projective numerators close in a finite module containing `N_1,N_2`' in d,
    'scaling_counterexample_nonzero_both_channels': all(x != 0 for x in scaling_residual),
    'scaling_ratio_mismatch_exact': lam**31 != lam**27,
}

controls = {
    'lambda_one_has_no_scaling_mismatch': all(((Fraction(1)**31)-(Fraction(1)**27))*x == 0 for x in B),
    'zero_action_would_not_supply_counterexample': all(((lam**31)-(lam**27))*Fraction(0) == 0 for _ in B),
    'degree_matched_fixture_has_no_mismatch': all(((lam**27)-(lam**27))*x == 0 for x in B),
}

valid = all(checks.values()) and all(controls.values())
verdict = 'REQUIRES_NEW_PREREGISTERED_GATE' if valid else 'INVALID_IMPLEMENTATION'

out = {
    'gate': 'K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_ACTION_REPAIR1_INDEPENDENT_CRITIC_REVIEW',
    'verdict': verdict,
    'checks': checks,
    'controls': controls,
    'uniform_N': [str(x) for x in N],
    'uniform_B': [str(x) for x in B],
    'lambda': str(lam),
    'actual_B_lambda_alpha': [str(x) for x in actual_scaled_B],
    'constant_M_prediction_if_fit_at_alpha': [str(x) for x in constant_M_scaled_prediction],
    'scaling_residual': [str(x) for x in scaling_residual],
    'scientific_scope': {
        'nonzero_action_survives': True,
        'raw_homogeneous_constant_M_closure_is_exactly_impossible': True,
        'projective_degree27_constant_M_closure_tested': False,
        'integrated_period_verdict': None,
    },
    'authorized_successor_object': 'P_v[N]=B_v[N]/s1^4 (or equivalently simplex-normalized A_v/B_v on s1=1), prospectively preregistered before testing constant closure',
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if valid else 2)
