#!/usr/bin/env python3
"""Iteration 025A: validate the j=1/2 Toller Feynman-i-epsilon distribution.

For j=1/2 the polynomial entering Appendix-D of the causal-vertex paper is

  F_{1/2}(rho+sigma q,rho)
    = 1 + c1 (sigma q) + c2/2 (sigma q)^2,

with

  c1 = 2 rho/(rho^2+1/4),
  c2 = 2/(rho^2+1/4).

Hence

  delta^(rho,1/2)(x) = -i c1 delta(x) - (c2/2) delta'(x),
  Theta_sigma(x) = theta(sigma x) + sigma delta^(rho,1/2)(x).

The goal is not to sample these distributions pointwise.  We test their action
on smooth Schwartz functions against the original finite-epsilon spectral
integral.  This is the mathematically correct place for the i-epsilon limit.

We choose Gaussian-polynomial test functions phi(x).  Their Fourier transform
is evaluated by high-precision quadrature.  The finite-epsilon spectral action
is

  <Theta_{sigma,eps},phi>
   = int dq/(2 pi i) sigma/(q-i eps)
       F(rho+sigma q,rho) PhiHat(-sigma q),

where PhiHat(k)=int dx phi(x) exp(i k x).  The target distributional action is

  int_{sigma x>0} phi(x) dx
  + sigma[-i c1 phi(0) + (c2/2) phi'(0)].

The derivative sign follows <delta',phi>=-phi'(0).

This validates the boundary-supported piece independently of the ordinary
Toller-function residue implementation.  It is a one-wedge distributional
unit test, not yet a product-of-distributions definition at multi-collisions.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70

EPS = [mp.mpf(x) for x in ('0.5','0.2','0.1','0.05','0.02','0.01')]

# phi(x)=exp(-a x^2)*(1+b x+c x^2)
TESTS = [
    ('even', mp.mpf('0.7'), mp.mpf('0.0'), mp.mpf('0.3')),
    ('oddmix', mp.mpf('1.1'), mp.mpf('0.45'), mp.mpf('-0.2')),
    ('narrow', mp.mpf('2.3'), mp.mpf('-0.35'), mp.mpf('0.15')),
]


def fmt(x,n=22): return mp.nstr(x,n)
def cfmt(z,n=22): return [fmt(mp.re(z),n),fmt(mp.im(z),n)]


def coeffs(rho):
    den=rho*rho+mp.mpf('0.25')
    return 2*rho/den, 2/den


def F(q,rho,sigma):
    c1,c2=coeffs(rho)
    return 1+c1*sigma*q+(c2/2)*(sigma*q)**2


def phi(x,a,b,c):
    return mp.e**(-a*x*x)*(1+b*x+c*x*x)


def phi0_deriv(a,b,c):
    return mp.mpf(1), b


def phihat(k,a,b,c):
    # Convention: integral phi(x) exp(i k x) dx.
    G=mp.sqrt(mp.pi/a)*mp.e**(-k*k/(4*a))
    # int x e^-a x2 e^ikx = (1/i)dG/dk = i*k/(2a) G
    X=1j*k/(2*a)*G
    # int x^2 ... = -d2G/dk2 = (1/(2a)-k^2/(4a^2))G
    X2=(1/(2*a)-k*k/(4*a*a))*G
    return G+b*X+c*X2


def target_action(rho,sigma,a,b,c):
    c1,c2=coeffs(rho)
    if sigma>0:
        bulk=mp.quad(lambda x:phi(x,a,b,c),[0,mp.inf])
    else:
        bulk=mp.quad(lambda x:phi(x,a,b,c),[-mp.inf,0])
    p0,p1=phi0_deriv(a,b,c)
    boundary=sigma*(-1j*c1*p0+(c2/2)*p1)
    return bulk+boundary


def spectral_action(rho,sigma,eps,a,b,c):
    def integrand(q):
        return (sigma/(q-1j*eps))*F(q,rho,sigma)*phihat(-sigma*q,a,b,c)/(2*mp.pi*1j)
    # Gaussian Fourier transform makes this absolutely easy at finite epsilon.
    return mp.quad(integrand,[-mp.inf,0,mp.inf])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rho',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); rho=mp.mpf(args.rho)
    c1,c2=coeffs(rho)
    rows=[]; all_last=[]
    for sigma in (-1,1):
        for name,a,b,c in TESTS:
            target=target_action(rho,sigma,a,b,c)
            vals=[]; errs=[]
            for eps in EPS:
                z=spectral_action(rho,sigma,eps,a,b,c)
                vals.append(z); errs.append(abs(z-target))
            rows.append({
                'sigma':sigma,'test':name,'target':cfmt(target),
                'finite_epsilon':[{'eps':fmt(e),'value':cfmt(v),'abs_error':fmt(er)}
                                  for e,v,er in zip(EPS,vals,errs)],
                'smallest_epsilon_error':fmt(errs[-1]),
            })
            all_last.append(errs[-1])
    out={
        'rho':args.rho,'j':'1/2','c1':fmt(c1),'c2':fmt(c2),
        'delta_distribution':'-i*c1*delta - (c2/2)*delta_prime',
        'rows':rows,
        'max_smallest_epsilon_abs_error':fmt(max(all_last)),
        'verdict':'JHALF_DISTRIBUTIONAL_IEPSILON_SCAN_COMPLETE',
        'guardrail':(
            'One-wedge Schwartz-test validation of the Appendix-D distributional identity. '
            'Finite epsilon is integrated in spectral q, not inserted as beta+i epsilon. '
            'This does not yet define products of boundary-supported distributions on intersecting wedge strata.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__': main()
