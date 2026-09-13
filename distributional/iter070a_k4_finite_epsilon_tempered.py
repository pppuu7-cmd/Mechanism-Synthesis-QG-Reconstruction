#!/usr/bin/env python3
"""Iter070A: fixed-epsilon temperedness audit for the reduced K4 joint-spectral family.

Frozen by status/ITERATION_070A_PREREG.md.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp
from distributional.k4_forest_order_finite_part import constrained_edge_flows, TREES, EDGE_NAMES

CASES={
 'T1':(sp.Rational(37,100),sp.Rational(41,1000),(sp.Rational(17,100),sp.Rational(-29,100),sp.Rational(21,100),sp.Rational(-9,100))),
 'T2':(sp.Rational(173,100),sp.Rational(137,1000),(sp.Rational(-26,100),sp.Rational(34,100),sp.Rational(-11,100),sp.Rational(3,100))),
}
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']

def causal_signs(label):
    sg=[1 if c=='+' else -1 for c in label]
    return tuple(sg[a]*sg[b] for a,b in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--tree',required=True,choices=sorted(TREES)); ap.add_argument('--sigma',required=True,choices=SIGMAS); ap.add_argument('--output',required=True); a=ap.parse_args()
    signs=causal_signs(a.sigma); rows=[]; lane_valid=True
    for cname,(gamma,eps,k) in CASES.items():
        rho=gamma/2; c1=2*rho/(rho**2+sp.Rational(1,4)); c2=2/(rho**2+sp.Rational(1,4))
        y,x,tree,chords,det=constrained_edge_flows(a.tree,k)
        affine=[]; imag=[]; numer_deg=[]; slopes=[]
        lam=sp.symbols('lambda',real=True); v=(sp.Integer(1),sp.Integer(2),sp.Integer(3))
        src_num_deg=0; src_den_deg=0
        for i,xe in enumerate(x):
            p=sp.Poly(sp.expand(xe),*y,domain='QQ')
            affine.append(p.total_degree()<=1 and all(co.is_real is not False for co in p.coeffs()))
            im=-sp.Integer(signs[i])*eps; imag.append(str(im))
            num=1+c1*xe+(c2/2)*xe**2
            pn=sp.Poly(sp.expand(num.subs({y[j]:lam*v[j] for j in range(3)})),lam,domain='QQ')
            den=xe-sp.I*sp.Integer(signs[i])*eps
            pd=sp.Poly(sp.expand(den.subs({y[j]:lam*v[j] for j in range(3)})),lam,domain='EX')
            src_num_deg+=int(pn.degree()); src_den_deg+=int(pd.degree())
            slopes.append(str(sp.Poly(sp.expand(xe.subs({y[j]:lam*v[j] for j in range(3)})),lam,domain='QQ').coeff_monomial(lam)))
            numer_deg.append(int(sp.Poly(sp.expand(num),*y,domain='QQ').total_degree()))
        p1=all(affine)
        p2=all(sp.sympify(q)!=0 for q in imag)
        p3=p1 and p2
        radial=src_num_deg-src_den_deg
        p4=(radial==6)
        # Since |x-i s eps| >= eps on real cycle space and each numerator factor is quadratic
        # in affine x, a global polynomial bound of degree <=12 follows directly.
        global_bound_degree=sum(numer_deg)
        tempered=p3 and global_bound_degree<=12
        valid=p1 and p2 and p3 and p4 and tempered
        lane_valid=lane_valid and valid
        rows.append({'case':cname,'gamma':str(gamma),'epsilon':str(eps),'tree':a.tree,'sigma':a.sigma,
                     'denominator_imaginary_constants':imag,'edge_slopes_V1':slopes,
                     'radial_degree_V1':radial,'global_polynomial_bound_degree':global_bound_degree,
                     'predicates':{'P1_REAL_AFFINE_EDGE_FLOWS':p1,'P2_NONZERO_CONSTANT_IMAG_DENOMINATORS':p2,
                                   'P3_SMOOTH_ON_REAL_CYCLE_SPACE':p3,'P4_RADIAL_DEGREE_PLUS6':p4,
                                   'P5_GLOBAL_POLYNOMIAL_BOUND_IMPLIES_TEMPERED':tempered},'valid':valid})
    target='ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED'
    out={'iteration':'Iter070A','tree':a.tree,'sigma':a.sigma,'rows':rows,'valid':lane_valid,
         'classification':target if lane_valid else 'ITER070A_FINITE_EPSILON_TEMPEREDNESS_REVIEW',
         'claim_lock':'Fixed epsilon>0 reduced family only; no epsilon->0 boundary-value theorem or causal-vertex theorem.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2,sort_keys=True))
    if not lane_valid: raise SystemExit(9)
if __name__=='__main__': main()
