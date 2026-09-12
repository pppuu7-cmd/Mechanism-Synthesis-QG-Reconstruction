#!/usr/bin/env python3
"""Iteration 025A: convention-safe j=1/2 Appendix-D distribution tests.

The causal-vertex paper gives, distributionally,

  Theta_{sigma,rho,j}(x) = theta(sigma x) + sigma delta^(rho,j)(x),

with

  delta^(rho,j)(x)
    = sum_{n=0}^{2j} c_{n+1}/(n+1)! * (-i)^(n+1) * delta^(n)(x),

and a polynomial

  F_j(rho+sigma q,rho)
    = 1 + sum_{n=1}^{2j+1} c_n/n! * (sigma q)^n.

For j=1/2 this can be derived algebraically from the product formula:

  F = [(i(rho+sigma q)+1/2)(i(rho+sigma q)-1/2)]
      /[(i rho+1/2)(i rho-1/2)]
    = 1 + c1 sigma q + (c2/2)(sigma q)^2,

  c1 = 2 rho/(rho^2+1/4),   c2 = 2/(rho^2+1/4),

so

  delta^(rho,1/2) = -i c1 delta - (c2/2) delta'.

This script validates three things without making a sign/orientation assumption
about an intermediate finite-epsilon change of spectral variable:

1. the closed c1,c2 reproduce the exact product polynomial;
2. a Gaussian mollifier implementation converges to the analytic action of
   theta(sigma x)+sigma delta^(rho,1/2) on several Schwartz test functions;
3. the causal/complementary distributions obey Theta_+ + Theta_- = 1 on every
   test function, including their boundary-supported delta and delta' pieces.

The finite epsilon in the underlying theory lives in the spectral variable.
This is a distributional unit test of the paper's already-derived epsilon->0
identity, not a replacement derivation of that identity and not yet a product
of distributions at multi-wedge intersections.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70
ETAS = [mp.mpf(x) for x in ('0.5','0.25','0.125','0.0625','0.03125')]
QTEST = [mp.mpf(x) for x in ('-3.1','-1.0','-0.2','0','0.37','1.4','2.8')]
TESTS = [
    ('even', mp.mpf('0.7'), mp.mpf('0.0'), mp.mpf('0.3')),
    ('oddmix', mp.mpf('1.1'), mp.mpf('0.45'), mp.mpf('-0.2')),
    ('narrow', mp.mpf('2.3'), mp.mpf('-0.35'), mp.mpf('0.15')),
]


def fmt(x,n=24): return mp.nstr(x,n)
def cfmt(z,n=24): return [fmt(mp.re(z),n),fmt(mp.im(z),n)]


def coeffs(rho):
    den=rho*rho+mp.mpf('0.25')
    return 2*rho/den, 2/den


def F_product(q,rho,sigma):
    x=1j*rho
    num=(x+1j*sigma*q+mp.mpf('0.5'))*(x+1j*sigma*q-mp.mpf('0.5'))
    den=(x+mp.mpf('0.5'))*(x-mp.mpf('0.5'))
    return num/den


def F_expanded(q,rho,sigma):
    c1,c2=coeffs(rho)
    return 1+c1*sigma*q+(c2/2)*(sigma*q)**2


def phi(x,a,b,c):
    return mp.e**(-a*x*x)*(1+b*x+c*x*x)


def total_phi(a,b,c):
    return mp.quad(lambda x:phi(x,a,b,c),[-mp.inf,0,mp.inf])


def target_action(rho,sigma,a,b,c):
    c1,c2=coeffs(rho)
    bulk=(mp.quad(lambda x:phi(x,a,b,c),[0,mp.inf]) if sigma>0
          else mp.quad(lambda x:phi(x,a,b,c),[-mp.inf,0]))
    # <delta,phi>=phi(0)=1; <delta',phi>=-phi'(0)=-b.
    # delta^(rho,1/2)=-i c1 delta-(c2/2)delta', hence its action is
    # -i c1 + (c2/2)b.
    boundary=sigma*(-1j*c1+(c2/2)*b)
    return bulk+boundary


def delta_eta(x,eta):
    return mp.e**(-(x/eta)**2)/(mp.sqrt(mp.pi)*eta)


def delta_prime_eta(x,eta):
    return -2*x/(eta*eta)*delta_eta(x,eta)


def H_eta(x,eta):
    return (1+mp.erf(x/eta))/2


def mollified_action(rho,sigma,eta,a,b,c):
    c1,c2=coeffs(rho)
    def integrand(x):
        theta=H_eta(sigma*x,eta)
        boundary=sigma*(-1j*c1*delta_eta(x,eta)-(c2/2)*delta_prime_eta(x,eta))
        return (theta+boundary)*phi(x,a,b,c)
    # Split around the shrinking mollifier support for stable quadrature.
    L=8*eta
    return mp.quad(integrand,[-mp.inf,-L,0,L,mp.inf])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rho',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); rho=mp.mpf(args.rho)
    c1,c2=coeffs(rho)

    poly_errors=[]
    for sigma in (-1,1):
        for q in QTEST:
            poly_errors.append(abs(F_product(q,rho,sigma)-F_expanded(q,rho,sigma)))

    rows=[]; last_errors=[]; complement_errors=[]
    for name,a,b,c in TESTS:
        targets={s:target_action(rho,s,a,b,c) for s in (-1,1)}
        exact_total=total_phi(a,b,c)
        complement_errors.append(abs(targets[1]+targets[-1]-exact_total))
        for sigma in (-1,1):
            vals=[]; errs=[]
            for eta in ETAS:
                z=mollified_action(rho,sigma,eta,a,b,c)
                vals.append(z); errs.append(abs(z-targets[sigma]))
            rows.append({
                'test':name,'sigma':sigma,'target':cfmt(targets[sigma]),
                'mollifier':[{'eta':fmt(e),'value':cfmt(v),'abs_error':fmt(er)}
                             for e,v,er in zip(ETAS,vals,errs)],
                'smallest_eta_error':fmt(errs[-1]),
            })
            last_errors.append(errs[-1])

    # Require algebra/complement identities at high precision and numerical
    # mollifier convergence to be visibly small at the final eta.
    pass_poly=max(poly_errors)<mp.mpf('1e-60')
    pass_comp=max(complement_errors)<mp.mpf('1e-60')
    pass_moll=max(last_errors)<mp.mpf('5e-3')
    out={
        'rho':args.rho,'j':'1/2','c1':fmt(c1),'c2':fmt(c2),
        'distribution':'delta_rho_jhalf = -i*c1*delta - (c2/2)*delta_prime',
        'max_polynomial_identity_error':fmt(max(poly_errors)),
        'max_exact_complement_action_error':fmt(max(complement_errors)),
        'max_smallest_eta_mollifier_error':fmt(max(last_errors)),
        'rows':rows,
        'verdict':('JHALF_APPENDIX_D_DISTRIBUTION_PASS'
                   if pass_poly and pass_comp and pass_moll
                   else 'JHALF_APPENDIX_D_DISTRIBUTION_REVIEW'),
        'guardrail':(
            'Validates the j=1/2 Appendix-D polynomial and distribution action using smooth test functions. '
            'It deliberately does not invent beta+i*epsilon and does not yet define products of delta-supported '
            'wedge distributions on multi-collision intersections.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if out['verdict']!='JHALF_APPENDIX_D_DISTRIBUTION_PASS': raise SystemExit(7)

if __name__=='__main__': main()
