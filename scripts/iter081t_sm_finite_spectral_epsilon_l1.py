#!/usr/bin/env python3
"""Iter081T-SM exact j=1/2 finite spectral-epsilon K5 L1 diagnostic.

Checks the finite-epsilon BCG contour residue prefactor against the exact
small-beta Toller coefficients.  The key result is exact epsilon cancellation
in the leading matrix, so authoritative Iter077I K5 contractions are reused
without numerical recomputation.
"""
import json
import os
import subprocess
from pathlib import Path
import sympy as sp

rho = sp.symbols('rho', real=True, nonzero=True)
eps = sp.symbols('eps', positive=True, real=True)
sigma = sp.symbols('sigma', integer=True, nonzero=True)
I = sp.I
D0 = rho**2 + sp.Rational(1,4)


def D(x):
    return sp.expand(x**2 + sp.Rational(1,4))


def P_half(rtilde):
    # Product n=0,1 of [i rtilde -(n-1/2)]/[i rho-(n-1/2)].
    return sp.simplify(
        ((I*rtilde + sp.Rational(1,2))*(I*rtilde - sp.Rational(1,2))) /
        ((I*rho + sp.Rational(1,2))*(I*rho - sp.Rational(1,2)))
    )

assert sp.simplify(P_half(sp.symbols('R')) - D(sp.symbols('R'))/D0) == 0

rows = []
for s in (+1, -1):
    R = rho + I*s*eps
    P = sp.simplify(P_half(R))
    # Exact Eq.(46) leading coefficients for j=l=k=1/2, analytically
    # continued to R. Ordering is m=(-1/2,+1/2).
    plus_lead = [sp.Rational(1,2)/D(R), -sp.Rational(1,2)/D(R)]
    branch_lead = plus_lead if s == +1 else [-c for c in plus_lead]
    projected = [sp.simplify(P*c) for c in branch_lead]
    expected = (
        [sp.Rational(1,2)/D0, -sp.Rational(1,2)/D0]
        if s == +1 else
        [-sp.Rational(1,2)/D0, sp.Rational(1,2)/D0]
    )
    assert all(sp.simplify(a-b) == 0 for a,b in zip(projected, expected))
    rows.append({
        'branch_sigma': s,
        'shifted_rho': str(R),
        'P_shifted': str(P),
        'projected_leading_m_minus_half': str(projected[0]),
        'projected_leading_m_plus_half': str(projected[1]),
        'epsilon_independent': True,
    })

# Every wedge therefore has exactly the authoritative Iter077I leading matrix,
# including its branch sign. The full ten-wedge leading tensor and every full
# boundary contraction are unchanged at fixed eps>0.
wedge_power = -2
num_wedges = 10
q = wedge_power*num_wedges
transverse_dimension = 12
radial_abs_exponent = transverse_dimension - 1 + q
l1_margin = q + transverse_dimension
assert q == -20
assert radial_abs_exponent == -9
assert l1_margin == -8

prereg = '52313c08f39855bf18e3b56fce268e9cd262a074'
prereg_ancestor = subprocess.call(['git','merge-base','--is-ancestor',prereg,'HEAD']) == 0

out = {
    'iteration':'Iter081T-SM',
    'classification':'FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED',
    'verdict':'PASS_EXACT_SCOPED',
    'domain':'j=l=k=1/2; real rho!=0; fixed positive spectral epsilons; Iter077I collision ray',
    'finite_epsilon_contour_identity':'I_eps^sigma[d] = P(rho+i sigma eps;rho) t^sigma(rho+i sigma eps) (diagnostic pre-limit projector)',
    'P_half_identity':'P_1/2,1/2(R;rho)=(R^2+1/4)/(rho^2+1/4)',
    'branch_rows':rows,
    'k5':{
        'wedge_power':wedge_power,
        'num_wedges':num_wedges,
        'total_q':q,
        'transverse_dimension':transverse_dimension,
        'radial_absolute_exponent':radial_abs_exponent,
        'l1_margin_q_plus_d':l1_margin,
        'all_32_iter077i_leading_contractions_unchanged':True,
        'local_L1':False,
    },
    'common_vs_independent_epsilon':'leading result is epsilon-independent wedge by wedge, so common and independent fixed positive epsilons give the same r^-20 leading tensor',
    'source_scope':'finite epsilon retained through K5 is NOT the published source ordering; this is only a regulator diagnostic',
    'controls':{
        'epsilon_to_zero_reproduces_source_leading_matrix':True,
        'spectral_prefactor_cancels_shifted_D_exactly':True,
        'no_contact_distribution_product_used':True,
        'rho_real_nonzero_avoids_shifted_Toller_pole_zero_denominator_coincidence':True,
    },
    'provenance':{
        'git_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        'prereg_commit_expected':prereg,
        'prereg_ancestor':prereg_ancestor,
    },
    'claim_locks':[
        'not source-authorized regulator ordering',
        'no theorem against other correlated group-variable regulators',
        'no regulator independence',
        'no distributional nonexistence/divergence theorem',
        'no NEW_PHYSICS_FOUND'
    ]
}
if not prereg_ancestor:
    out['classification']='INVALID_PROVENANCE'
    out['verdict']='INVALID_PROVENANCE'

p=Path(os.environ.get('ITER081T_OUT','results/raw/iter081t_sm_finite_spectral_epsilon.json'))
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if out['verdict']!='PASS_EXACT_SCOPED':
    raise SystemExit(2)
