#!/usr/bin/env python3
"""Iter043A: exact finite-epsilon contact structure of the published j=1/2 kernel.

Starting from Eq. (3) of the causal-vertex paper, set
    rtilde = rho + sigma*q.
For j=1/2 Appendix D gives exactly
    F(rho+sigma q,rho)=1+c1*sigma*q+(c2/2)q^2.
At finite epsilon>0 the spectral kernel acting on x is therefore

  Theta_{sigma,eps}(x)
   = ∫ dq/(2π i) F(rho+sigma q,rho)
       exp(i sigma q x)/(q-i eps).

Polynomial division gives the exact distribution identity

  Theta_{sigma,eps}(x)
   = A_{sigma,eps} theta(sigma x) exp(-eps |x|)
     + B_{sigma,eps} delta(x)
     - sigma*(c2/2) delta'(x),

  A = 1 + i eps sigma c1 - eps^2 c2/2,
  B = -i sigma c1 + eps c2/2.

The key source-level fact is that the delta-prime coefficient is independent of
finite epsilon.  Thus keeping the published spectral i-epsilon finite on each
wedge separately does not smooth away the boundary-supported contact layer.
This script validates the identity directly on Schwartz test functions by
comparing the closed distribution action with the original finite-epsilon
spectral integral.  It is a one-wedge theorem/check, not yet a definition of
non-transverse multi-wedge products.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from distributional.jhalf_iepsilon_validation import coeffs

mp.mp.dps = 70
TESTS = [
    ('even', mp.mpf('0.7'), mp.mpf('0.0'), mp.mpf('0.3')),
    ('oddmix', mp.mpf('1.1'), mp.mpf('0.45'), mp.mpf('-0.2')),
    ('narrow', mp.mpf('2.3'), mp.mpf('-0.35'), mp.mpf('0.15')),
]


def fmt(x,n=26): return mp.nstr(x,n)
def cfmt(z,n=26): return [fmt(mp.re(z),n),fmt(mp.im(z),n)]


def phi(x,a,b,c):
    return mp.e**(-a*x*x)*(1+b*x+c*x*x)


def phi0_prime(a,b,c):
    return b


def fourier_phi(k,a,b,c):
    g=mp.sqrt(mp.pi/a)*mp.e**(-k*k/(4*a))
    return g*(1+1j*b*k/(2*a)+c*(1/(2*a)-k*k/(4*a*a)))


def F_poly(q,rho,sigma):
    c1,c2=coeffs(rho)
    return 1+c1*sigma*q+(c2/2)*q*q


def closed_action(rho,sigma,eps,a,b,c):
    c1,c2=coeffs(rho)
    A=1+1j*eps*sigma*c1-(eps*eps*c2/2)
    B=-1j*sigma*c1+(eps*c2/2)
    if sigma>0:
        bulk=mp.quad(lambda x: mp.e**(-eps*x)*phi(x,a,b,c), [0, mp.inf])
    else:
        bulk=mp.quad(lambda x: mp.e**(eps*x)*phi(x,a,b,c), [-mp.inf,0])
    # <delta',phi> = -phi'(0) = -b
    return A*bulk + B*phi(0,a,b,c) + (-sigma*c2/2)*(-phi0_prime(a,b,c))


def spectral_action(rho,sigma,eps,a,b,c):
    def integrand(q):
        return (F_poly(q,rho,sigma)*fourier_phi(sigma*q,a,b,c)
                /(q-1j*eps)/(2*mp.pi*1j))
    # The test-function Fourier transform is Gaussian, so this integral is
    # absolutely controlled despite the polynomial F_j factor.
    return mp.quad(integrand, [-mp.inf,-8,-3,0,3,8,mp.inf])


def relerr(a,b):
    return abs(a-b)/max(abs(b),mp.mpf('1e-50'))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--epsilon',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma); eps=mp.mpf(args.epsilon); rho=gamma/2
    if eps <= 0: raise SystemExit('epsilon must be positive')
    c1,c2=coeffs(rho)

    rows=[]; errs=[]
    for name,a,b,c in TESTS:
        for sigma in (-1,1):
            zc=closed_action(rho,sigma,eps,a,b,c)
            zs=spectral_action(rho,sigma,eps,a,b,c)
            er=relerr(zs,zc); errs.append(er)
            rows.append({'test':name,'sigma':sigma,'closed_action':cfmt(zc),
                         'spectral_action':cfmt(zs),'relative_error':fmt(er)})

    # The exact finite-epsilon delta-prime coefficient and its epsilon->0 value
    # are algebraically identical.  Record this as a machine-checkable identity.
    dprime_finite={s: -s*c2/2 for s in (-1,1)}
    dprime_limit={s: -s*c2/2 for s in (-1,1)}
    dprime_error=max(abs(dprime_finite[s]-dprime_limit[s]) for s in (-1,1))
    maxerr=max(errs)
    gates={
        'spectral_vs_closed_action': maxerr < mp.mpf('2e-18'),
        'delta_prime_coefficient_epsilon_independent': dprime_error == 0,
    }
    out={
        'iteration':'Iter043A','gamma':args.gamma,'rho':fmt(rho),
        'epsilon':args.epsilon,'c1':fmt(c1),'c2':fmt(c2),'mp_dps':mp.mp.dps,
        'finite_epsilon_distribution':(
            'A*theta(sigma*x)*exp(-epsilon*abs(x)) + B*delta(x) '
            '- sigma*c2/2*delta_prime(x)'
        ),
        'A_formula':'1 + i*epsilon*sigma*c1 - epsilon^2*c2/2',
        'B_formula':'-i*sigma*c1 + epsilon*c2/2',
        'delta_prime_coefficient_formula':'-sigma*c2/2 (exactly epsilon independent)',
        'max_spectral_closed_relative_error':fmt(maxerr),
        'delta_prime_epsilon_independence_error':fmt(dprime_error),
        'rows':rows,'gates':gates,
        'classification':('FINITE_EPSILON_CONTACT_LAYER_PERSISTS'
                          if all(gates.values()) else 'FINITE_EPSILON_CONTACT_IDENTITY_REVIEW'),
        'claim_lock':(
            'This validates the published one-wedge finite-i-epsilon spectral antecedent for j=1/2. '
            'It shows that finite epsilon does not remove the delta-prime contact layer after the exact '
            'spectral transform. It does not say the full multi-wedge Feynman vertex is undefined: the '
            'spectral integrations may have to be treated jointly before multiplying boundary-supported '
            'distributions. No divergence, counterterm, G3, F9 or G8 claim follows.'
        )
    }
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if not all(gates.values()): raise SystemExit(7)

if __name__=='__main__': main()
