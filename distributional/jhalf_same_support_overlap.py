#!/usr/bin/env python3
"""Iteration 028C: same-support overlap test for the published j=1/2 boundary primitive.

Iteration 025A validated
  D_rho = -i c1 delta - (c2/2) delta'
with c1=2rho/(rho^2+1/4), c2=2/(rho^2+1/4).

Here delta and delta' are represented by normalized Gaussian mollifiers.  We
compare two situations:
  (1) independent variables: D(x)D(y), which is a standard tensor product and
      must have a regulator-independent finite test-function limit;
  (2) the same scalar support: D_eta(x) D_{r eta}(x), which tests what happens
      if two pulled-back boundary terms become dependent on the same local
      normal coordinate.

The shared-support integral is analytic because the mollified distributions
and the test function are Gaussian times polynomials.  A divergence or width-
ratio-dependent leading coefficient is evidence that the naive same-support
product requires an extension.  It is NOT evidence that the exact causal
vertex necessarily identifies two Appendix-D spectral variables this way;
that pullback geometry is the next physical question.
"""
from __future__ import annotations

import argparse, cmath, json, math
from pathlib import Path
import numpy as np

ETAS=np.array([0.5,0.25,0.125,0.0625,0.03125,0.015625],dtype=float)
# phi(x)=exp(-a x^2)*(1+b x+c x^2)
A_TEST=0.7; B_TEST=0.31; C_TEST=0.22


def coeffs(rho):
    den=rho*rho+0.25
    return 2*rho/den,2/den


def gaussian_even_moment(n,alpha):
    # int x^(2n) exp(-alpha x^2) dx
    if n==0:return math.sqrt(math.pi)/math.sqrt(alpha)
    odd=1
    for q in range(1,2*n,2): odd*=q
    return odd*math.sqrt(math.pi)/(2**n*alpha**(n+0.5))


def poly_gaussian_integral(coeff,alpha):
    z=0j
    for power,c in enumerate(coeff):
        if power%2: continue
        z+=c*gaussian_even_moment(power//2,alpha)
    return z


def shared_action(rho,ratio,eta):
    c1,c2=coeffs(rho); e1=eta; e2=ratio*eta
    aa=-1j*c1
    b1=c2/(2*e1*e1); b2=c2/(2*e2*e2)
    # (aa+b1*x)(aa+b2*x) * (1+B*x+C*x^2)
    p12=[aa*aa,aa*(b1+b2),b1*b2]
    test=[1.0,B_TEST,C_TEST]
    poly=[0j]*(len(p12)+len(test)-1)
    for i,u in enumerate(p12):
        for j,v in enumerate(test): poly[i+j]+=u*v
    alpha=A_TEST+0.5/(e1*e1)+0.5/(e2*e2)
    pref=1.0/(2*math.pi*e1*e2)
    return pref*poly_gaussian_integral(poly,alpha)


def single_action_mollified(rho,eta):
    c1,c2=coeffs(rho); aa=-1j*c1; bb=c2/(2*eta*eta)
    # D_eta = delta_eta*(aa+bb*x), multiply by test polynomial.
    p=[aa,bb]; test=[1.0,B_TEST,C_TEST]
    poly=[0j]*(len(p)+len(test)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(test): poly[i+j]+=u*v
    alpha=A_TEST+0.5/(eta*eta)
    pref=1.0/(math.sqrt(2*math.pi)*eta)
    return pref*poly_gaussian_integral(poly,alpha)


def fit_power(vals):
    x=np.log(ETAS[-4:]); y=np.log(np.abs(np.asarray(vals[-4:],dtype=complex)))
    return float(np.polyfit(x,y,1)[0])


def cf(z):return [float(z.real),float(z.imag)]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rho',type=float,required=True);ap.add_argument('--ratio',type=float,required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    rho=args.rho;ratio=args.ratio;c1,c2=coeffs(rho)
    shared=[shared_action(rho,ratio,e) for e in ETAS]
    p=fit_power(shared)
    scaled=[z*(e**3) for z,e in zip(shared,ETAS)]
    single=[single_action_mollified(rho,e) for e in ETAS]
    exact_single=-1j*c1+(c2/2)*B_TEST
    independent=[z*z for z in single]
    exact_independent=exact_single*exact_single
    out={
      'rho':rho,'width_ratio':ratio,'c1':c1,'c2':c2,'eta_values':ETAS.tolist(),
      'shared_support_values':[cf(z) for z in shared],
      'shared_support_fitted_eta_power':p,'shared_support_expected_leading_power':-3.0,
      'shared_support_scaled_eta3_tail':[cf(z) for z in scaled[-3:]],
      'shared_support_scaled_tail_relative_change':abs(scaled[-1]-scaled[-2])/max(abs(scaled[-1]),1e-300),
      'independent_tensor_product_last':cf(independent[-1]),
      'independent_tensor_product_exact':cf(exact_independent),
      'independent_tensor_product_abs_error':abs(independent[-1]-exact_independent),
      'verdict':'JHALF_SAME_SUPPORT_OVERLAP_REQUIRES_EXTENSION' if p < -2.5 else 'JHALF_SAME_SUPPORT_OVERLAP_REVIEW',
      'guardrail':('Directly tests only a hypothetical dependent pullback onto one scalar normal coordinate. '
                   'The exact causal vertex may involve distinct spectral variables/conormals; no full-vertex divergence is inferred.'),
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
