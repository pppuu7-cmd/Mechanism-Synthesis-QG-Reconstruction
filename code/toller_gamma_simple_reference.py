#!/usr/bin/env python3
"""High-precision reference for gamma-simple Wigner d and Toller t^± matrices.

Implements Eqs. (45)-(46) of Bianchi, Chen & Gamonal, Phys. Rev. D 114,
046014 (2026), specialized to rho=gamma*j and k=j.  This is intentionally a
slow Python/mpmath oracle for validating a later C implementation inside the
sl2cfoam dsmall/booster path.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
mp.mp.dps=70

def d_gamma(j,m,gamma,beta):
    rho=mp.mpf(gamma)*j;z=1-mp.e**(-2*beta)
    return mp.e**(-(j-1j*rho+m+1)*beta)*mp.hyp2f1(j+m+1,j+1-1j*rho,2*j+2,z)

def t_gamma(sign,j,m,gamma,beta):
    # sign=+1 for t^+, -1 for t^-.
    s=mp.mpf(sign);rho=mp.mpf(gamma)*j;z=mp.e**(-2*beta)
    pref=mp.e**(-(j-s*1j*rho+s*m+1)*beta)
    pref*=mp.gamma(2*j+2)*mp.gamma(s*1j*rho-s*m)/(mp.gamma(j-s*m+1)*mp.gamma(j+1+s*1j*rho))
    return pref*mp.hyp2f1(j+s*m+1,j+1-s*1j*rho,1+s*m-s*1j*rho,z)

def c(z):return [float(mp.re(z)),float(mp.im(z))]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/toller_gamma_simple_reference.json');args=ap.parse_args()
    cases=[];worst=mp.mpf('0')
    for j,mvals in [(mp.mpf('0.5'),[-mp.mpf('0.5'),mp.mpf('0.5')]),(mp.mpf('1'),[-1,0,1])]:
      for m in mvals:
       for gamma in (mp.mpf('0.4'),mp.mpf('1.2')):
        for beta in (mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('1.7'),mp.mpf('3.0')):
          d=d_gamma(j,m,gamma,beta);tp=t_gamma(1,j,m,gamma,beta);tm=t_gamma(-1,j,m,gamma,beta);r=abs(tp+tm-d)/max(abs(d),mp.mpf('1e-60'));worst=max(worst,r)
          cases.append({'j':float(j),'m':float(m),'gamma':float(gamma),'beta':float(beta),'d':c(d),'t_plus':c(tp),'t_minus':c(tm),'relative_sum_residual':float(r)})
    tol=mp.mpf('1e-40');passed=worst<tol
    out={'paper':'PhysRevD.114.046014 / arXiv:2604.24945','specialization':'k=j, rho=gamma*j','cases':cases,'worst_relative_sum_residual':float(worst),'tolerance':float(tol),'passed':passed,
         'verdict':'TOLLER_REFERENCE_SUM_RULE_VERIFIED' if passed else 'TOLLER_REFERENCE_FORMULA_MISMATCH',
         'integration_target':'replace/branch sl2cfoam reduced Wigner dsmall factors inside booster integration, not post-project a scalar vertex','scope':'formula/reference validation only; no physical coarse-graining or F9 credit'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'verdict':out['verdict'],'cases':len(cases),'worst_residual':out['worst_relative_sum_residual']},indent=2))
if __name__=='__main__':main()
