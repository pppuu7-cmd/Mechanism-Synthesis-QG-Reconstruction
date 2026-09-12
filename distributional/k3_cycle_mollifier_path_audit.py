#!/usr/bin/env python3
"""Iter043C: exact path dependence of the simplest cyclic contact product.

The all-delta j=1/2 source sector already contains, on a K3 collision,
    delta(x) delta(y) delta(y-x)
with only two independent relative coordinates.  Standard products are
non-transverse (Iter028/029).  To quantify rather than merely state this, use
normalized Gaussian delta mollifiers of widths a*eta, b*eta, c*eta.

The leading action on a smooth test function with phi(0,0)=1 is

  I_eta ~ C(a,b,c)/eta,
  C = 1 / [sqrt(pi) a b c sqrt(det M)],
  M = [[a^-2+c^-2, -c^-2],[-c^-2,b^-2+c^-2]].

C depends on the width ratios.  By contrast the transverse/tree control
 delta_{a eta}(x) delta_{b eta}(y)
has leading coefficient 1 independently of a,b.  The script validates the
closed K3 coefficient by numerical quadrature in scaled variables and records
path spread.  This is a regulator-dependence diagnostic, not a physical choice
of mollifier and not a substitute for the published Feynman prescription.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

PATHS=[(1.0,1.0,1.0),(1.0,1.5,0.7),(1.0,2.0,3.0),(0.6,1.4,2.2),(2.0,0.8,1.3)]


def closed_coeff(a,b,c):
    M=np.array([[1/a**2+1/c**2,-1/c**2],[-1/c**2,1/b**2+1/c**2]],float)
    return 1.0/(math.sqrt(math.pi)*a*b*c*math.sqrt(np.linalg.det(M)))


def numerical_coeff(a,b,c,n=801,L=8.0):
    # eta-scaled variables.  The coefficient is the integral itself after the
    # universal 1/eta factor is stripped.
    u=np.linspace(-L,L,n); h=u[1]-u[0]; U,V=np.meshgrid(u,u,indexing='ij')
    norm=1.0/(math.pi**1.5*a*b*c)
    z=norm*np.exp(-(U/a)**2-(V/b)**2-((V-U)/c)**2)
    # trapezoidal rule in both variables
    return float(np.trapezoid(np.trapezoid(z,u,axis=1),u,axis=0))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--grid',type=int,default=801); ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); rows=[]; errs=[]; vals=[]
    for widths in PATHS:
        exact=closed_coeff(*widths); numeric=numerical_coeff(*widths,n=a.grid)
        rel=abs(numeric-exact)/abs(exact); errs.append(rel); vals.append(exact)
        rows.append({'width_ratios':list(widths),'closed_cycle_coefficient':exact,'numerical_cycle_coefficient':numeric,'relative_error':rel,
                     'tree_control_leading_coefficient':1.0})
    spread=max(vals)/min(vals)
    gates={'closed_vs_numeric':max(errs)<2e-5,'tree_control_path_independent_exactly':True,'cyclic_coefficient_path_dependent':spread>1.05}
    out={'iteration':'Iter043C','grid':a.grid,'rows':rows,'max_relative_quadrature_error':max(errs),
         'cycle_path_coefficient_max_over_min':spread,'gates':gates,
         'classification':('K3_CYCLIC_CONTACT_PRODUCT_MOLLIFIER_PATH_DEPENDENT' if all(gates.values()) else 'K3_MOLLIFIER_AUDIT_REVIEW'),
         'claim_lock':('This proves path dependence only for independent Gaussian mollification of the overconstrained all-delta K3 contact product. '
                       'It does not define the physical causal amplitude and does not rule out a correlated spectral/Feynman extension.')}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    if not all(gates.values()): raise SystemExit(7)

if __name__=='__main__': main()
