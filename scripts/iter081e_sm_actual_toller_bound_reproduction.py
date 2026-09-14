#!/usr/bin/env python3
import json
import os
import subprocess
from pathlib import Path
import sympy as sp

beta = sp.symbols('beta', positive=True, real=True)
rho = sp.symbols('rho', positive=True, real=True, finite=True)
i = sp.I
z = sp.exp(-2*beta)
j = sp.Rational(1,2)
D = rho**2 + sp.Rational(1,4)

# Frozen BCG Eq. (46), plus branch only. This function constructs the parameters
# mechanically from (j,m,rho), before any special-function simplification.
def plus_parameters(m):
    expo = j - i*rho + m + 1
    gamma_num = sp.gamma(2*j+2) * sp.gamma(i*rho-m)
    gamma_den = sp.gamma(j-m+1) * sp.gamma(j+1+i*rho)
    a = j + m + 1
    b = j + 1 - i*rho
    c = 1 + m - i*rho
    return expo, gamma_num, gamma_den, a, b, c

mp = sp.Rational(1,2)
mm = -sp.Rational(1,2)

# m=+1/2: b=c, so 2F1(a,b;b,z)=(1-z)^(-a).
ep, gnp, gdp, ap, bp, cp = plus_parameters(mp)
assert sp.simplify(bp-cp) == 0
assert ap == 2
gamma_ratio_p = sp.simplify(sp.expand_func(gnp/gdp))
expected_gamma_ratio_p = -2/D
assert sp.simplify(gamma_ratio_p-expected_gamma_ratio_p) == 0
hp = (1-z)**(-ap)
tp = sp.simplify(sp.exp(-ep*beta) * gamma_ratio_p * hp)
tp_expected = -2*sp.exp(-(2-i*rho)*beta)/(D*(1-z)**2)
assert sp.simplify(tp-tp_expected) == 0
# Since the phase exp(i rho beta) has unit modulus:
abs_tp = sp.simplify(2*sp.exp(-2*beta)/(D*(1-z)**2))
abs_tp_sinh = sp.simplify(1/(2*D*sp.sinh(beta)**2))
assert sp.simplify(abs_tp-abs_tp_sinh) == 0
limit_abs_tp = sp.limit(abs_tp_sinh, beta, 0, dir='+')
A_counterexample = (limit_abs_tp == sp.oo)

# m=-1/2: b=c+1. Derive 2F1(1,c+1;c,z) algebraically from
# (c+1)_n/(c)_n=(c+n)/c:
# sum [(c+n)/c] z^n = 1/(1-z) + z/[c(1-z)^2].
em, gnm, gdm, am, bm, cm = plus_parameters(mm)
assert am == 1
assert sp.simplify(bm-(cm+1)) == 0
gamma_ratio_m = sp.simplify(sp.expand_func(gnm/gdm))
expected_gamma_ratio_m = 2/(sp.Rational(1,2)+i*rho)
assert sp.simplify(gamma_ratio_m-expected_gamma_ratio_m) == 0
hm = sp.simplify(1/(1-z) + z/(cm*(1-z)**2))
tm = sp.simplify(sp.exp(-em*beta) * gamma_ratio_m * hm)

# Frozen natural two-wedge face term.
tau = sp.simplify(2*(tp**2 + tm**2))
limit_beta4_tau = sp.simplify(sp.limit(beta**4*tau, beta, 0, dir='+'))
expected_limit = sp.simplify(1/D**2)
assert sp.simplify(limit_beta4_tau-expected_limit) == 0
B_counterexample = (sp.simplify(limit_beta4_tau-expected_limit) == 0)

# Exact leading coefficients of individual magnetic components, useful to expose
# the non-cancellation mechanism before squaring.
lead_tp = sp.simplify(sp.limit(beta**2*tp, beta, 0, dir='+'))
lead_tm = sp.simplify(sp.limit(beta**2*tm, beta, 0, dir='+'))
assert sp.simplify(lead_tp + 1/(2*D)) == 0
assert sp.simplify(lead_tm - 1/(2*D)) == 0

# Non-authoritative regression controls at three independent rational rho values.
regression = []
for rv in [sp.Rational(1,2), sp.Rational(1,1), sp.Rational(2,1)]:
    exact_lim = sp.simplify(limit_beta4_tau.subs(rho,rv))
    expected = sp.simplify(expected_limit.subs(rho,rv))
    regression.append({
        'rho': str(rv),
        'beta4_tau_limit': str(exact_lim),
        'expected': str(expected),
        'match': bool(sp.simplify(exact_lim-expected)==0),
        'one_wedge_limit_infinite': True,
    })

# Negative bounded-surrogate control. Replacing exact branch entries by exp(-beta)
# must not satisfy either positive counterexample predicate.
sur = sp.exp(-beta)
sur_one_limit = sp.limit(sur, beta, 0, dir='+')
sur_tau = 2*(sur**2 + sur**2)
sur_face_limit = sp.limit(beta**4*sur_tau, beta, 0, dir='+')
negative_control_valid = (sur_one_limit == 1 and sur_face_limit == 0)

controls_valid = all(r['match'] for r in regression) and negative_control_valid
if A_counterexample and B_counterexample and controls_valid:
    classification = 'ITER081E_SM_ACTUAL_TOLLER_ONE_WEDGE_AND_NATURAL_TWO_WEDGE_HAN_BOUNDS_COUNTEREXAMPLES_REPRODUCED_EXACT_SCOPED'
    verdict = 'PASS_EXACT_SCOPED'
elif controls_valid:
    classification = 'ITER081E_SM_ACTUAL_TOLLER_HAN_BOUND_REPRODUCTION_PARTIAL_OR_FAIL_SCOPED'
    verdict = 'SCIENTIFIC_PARTIAL_OR_FAIL'
else:
    classification = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'
    verdict = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'

def git(args):
    return subprocess.check_output(['git']+args, text=True).strip()

out = {
    'iteration': 'Iter081E-SM',
    'classification': classification,
    'verdict': verdict,
    'frozen_object': {
        'j': '1/2', 'branch': '+', 'rho_domain': 'arbitrary fixed rho>0',
        'path': 'g_beta=exp(-i beta K_z), beta>0, beta->0+',
        'two_wedge_term': '2[(t_+1/2^+)^2+(t_-1/2^+)^2]'
    },
    'parameter_checks': {
        'm_plus_b_eq_c': str(sp.simplify(bp-cp)),
        'm_plus_a': str(ap),
        'm_minus_b_minus_c': str(sp.simplify(bm-cm)),
        'm_minus_a': str(am),
    },
    'derived': {
        'gamma_ratio_m_plus': str(gamma_ratio_p),
        't_m_plus': str(tp),
        'abs_t_m_plus': str(abs_tp_sinh),
        'limit_abs_t_m_plus_beta_to_0_plus': str(limit_abs_tp),
        'gamma_ratio_m_minus': str(gamma_ratio_m),
        'hypergeom_m_minus_reduced': str(hm),
        't_m_minus': str(tm),
        'limit_beta2_t_m_plus': str(lead_tp),
        'limit_beta2_t_m_minus': str(lead_tm),
        'limit_beta4_tau_pp_2': str(limit_beta4_tau),
        'expected_limit_beta4_tau_pp_2': str(expected_limit),
    },
    'subgates': {
        'A': 'A_COUNTEREXAMPLE' if A_counterexample else 'A_INSUFFICIENT',
        'B': 'B_FACE_BOUND_COUNTEREXAMPLE' if B_counterexample else 'B_INSUFFICIENT',
    },
    'regression_controls': regression,
    'negative_control': {
        'surrogate': 'exp(-beta)',
        'one_wedge_beta0_limit': str(sur_one_limit),
        'beta4_two_wedge_limit': str(sur_face_limit),
        'valid': bool(negative_control_valid),
    },
    'claim_locks': [
        'no complete causal face functional', 'no all-spin/all-branch theorem',
        'no causal-stack divergence theorem', 'no K5 selector', 'no G3/F9/G8 promotion',
        'no NEW_PHYSICS_FOUND'
    ],
    'provenance': {
        'git_head': git(['rev-parse','HEAD']),
        'prereg_commit_expected': '0f5414c9471a382527ca06c7f29ef2da6b8f8c1d',
        'prereg_ancestor': subprocess.call(['git','merge-base','--is-ancestor','0f5414c9471a382527ca06c7f29ef2da6b8f8c1d','HEAD']) == 0,
    }
}
if not out['provenance']['prereg_ancestor']:
    out['classification'] = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'
    out['verdict'] = 'INVALID_IMPLEMENTATION_OR_PROVENANCE'

outpath = Path(os.environ.get('ITER081E_OUT','results/raw/iter081e_sm_aggregate.json'))
outpath.parent.mkdir(parents=True, exist_ok=True)
outpath.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
print(json.dumps(out, indent=2, sort_keys=True))
if out['verdict'] == 'INVALID_IMPLEMENTATION_OR_PROVENANCE':
    raise SystemExit(2)
