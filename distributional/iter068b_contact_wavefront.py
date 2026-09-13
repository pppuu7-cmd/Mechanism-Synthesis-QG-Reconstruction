#!/usr/bin/env python3
"""Iter068B: exact Appendix-D j=1/2 contact-layer wavefront audit.

Frozen by status/ITERATION_068B_PREREG.md.  This audits the naive product of
separately transformed contact distributions only; it is not a joint spectral
boundary-value construction.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def parse_sigma(s):
    if len(s)!=4 or s[0]!='+' or any(x not in '+-' for x in s):
        raise ValueError('sigma must be four signs with sigma_0=+')
    return tuple(1 if x=='+' else -1 for x in s)

def normal(a,b):
    v=[0,0,0,0]; v[a]=1; v[b]=-1; return tuple(v)

def add(*vs): return tuple(sum(x) for x in zip(*vs))
def scale(k,v): return tuple(k*x for x in v)
def fstr(q): return f'{q.numerator}/{q.denominator}' if q.denominator!=1 else str(q.numerator)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sigma',required=True)
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    sig=parse_sigma(a.sigma)
    gamma=Fraction(a.gamma); rho=gamma/2
    c2=Fraction(2,1)/(rho*rho+Fraction(1,4))
    kappas=[sig[u]*sig[v] for u,v in EDGES]
    coeffs=[-Fraction(k,1)*c2/2 for k in kappas]

    p1=(c2>0 and all(x!=0 for x in coeffs))
    # WF(delta') at x=0 contains both nonzero conormal orientations.  Record the
    # two representatives for every edge as an exact finite certificate.
    conormals={f'{u}{v}':[list(normal(u,v)),list(scale(-1,normal(u,v)))] for u,v in EDGES}
    p2=all(len(v)==2 and tuple(v[0])==tuple(-x for x in v[1]) for v in conormals.values())

    # Fixed exact K4 triangle identity n01+n12-n02=0.
    witness=add(normal(0,1),normal(1,2),scale(-1,normal(0,2)))
    p3=(witness==(0,0,0,0))

    # Independent branch sum on one edge: (-c2/2) + (+c2/2) = 0.
    branch_sum=-c2/2+c2/2
    p4=(branch_sum==0)
    valid=p1 and p2 and p3 and p4
    classification=('K4_SEPARATE_CONTACT_PRODUCT_HORMANDER_OBSTRUCTED_JHALF'
                    if valid else 'ITER068B_INVALID_OR_INCONSISTENT')
    out={
      'iteration':'Iter068B','sigma':a.sigma,'gamma':a.gamma,'rho':fstr(rho),'c2':fstr(c2),
      'kappa':kappas,'delta_prime_coefficients':[fstr(x) for x in coeffs],
      'contact_conormal_representatives':conormals,
      'triangle_collision_identity':'n01+n12-n02=0','triangle_sum':list(witness),
      'independent_branch_delta_prime_sum':fstr(branch_sum),
      'predicates':{'P1_CONTACT_NONZERO':p1,'P2_SYMMETRIC_CONORMAL':p2,
                    'P3_K4_CYCLE_COLLISION':p3,'P4_BRANCH_SUM_CONTROL':p4},
      'valid':valid,'classification':classification,
      'claim_lock':'Naive product of separately contact-expanded j=1/2 wedge distributions only; not a no-go for the source-defined joint spectral boundary value and not a vertex divergence theorem.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(9)
if __name__=='__main__': main()
