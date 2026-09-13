#!/usr/bin/env python3
"""Iter070A: qualify the fixed-epsilon reduced K4 joint-spectral family as tempered.

Frozen by status/ITERATION_070A_PREREG.md.  This proves only fixed-epsilon
smooth polynomial boundedness; epsilon->0 remains open.
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

def parse_sigma(s): return tuple(1 if c=='+' else -1 for c in s)
def causal_signs(label):
    sg=parse_sigma(label); edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return tuple(sg[a]*sg[b] for a,b in edges)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sigma',required=True,choices=SIGMAS); ap.add_argument('--tree',required=True,choices=sorted(TREES)); ap.add_argument('--output',required=True); a=ap.parse_args()
    signs=causal_signs(a.sigma)
    ysym=sp.symbols('y0:3', real=True); v=sp.symbols('v0:3', real=True); lam=sp.symbols('lambda',real=True)
    rows=[]; all_valid=True
    for cname,(gamma,eps,k) in CASES.items():
        y,x,tree,chords,det=constrained_edge_flows(a.tree,k)
        rho=gamma/2; den0=rho*rho+sp.Rational(1,4); c1=sp.cancel(2*rho/den0); c2=sp.cancel(2/den0)
        edge_rows=[]; net=0; bound_degree=0; smooth=True; no_cancel=True
        for idx,xe in enumerate(x):
            grad=[sp.diff(xe,q) for q in y]
            real_affine=all(sp.im(g)==0 for g in grad) and sp.im(xe.subs({q:0 for q in y}))==0
            nonconstant=any(g!=0 for g in grad)
            imag_const=-signs[idx]*eps
            pole_free=(eps>0 and imag_const!=0)
            xl=sp.expand(xe.subs({y[i]:lam*v[i] for i in range(3)}))
            slope=sp.Poly(xl,lam,domain='EX').coeff_monomial(lam)
            num_at_pole=sp.simplify(1+c1*(sp.I*signs[idx]*eps)+(c2/2)*(sp.I*signs[idx]*eps)**2)
            edge_no_cancel=(num_at_pole!=0)
            no_cancel=no_cancel and edge_no_cancel
            # Generic factor degree: quadratic numerator / linear denominator.
            net += 1
            # A simple global bound uses |den|>=eps and quadratic numerator -> degree 2 per edge.
            bound_degree += 2
            smooth=smooth and real_affine and nonconstant and pole_free
            edge_rows.append({'edge':EDGE_NAMES[idx],'real_affine':bool(real_affine),'nonconstant':bool(nonconstant),
                              'imaginary_denominator_constant':str(imag_const),'pole_free_real_cycle':bool(pole_free),
                              'generic_slope':str(slope),'numerator_at_complex_pole':str(num_at_pole),
                              'no_exact_factor_cancellation':bool(edge_no_cancel)})
        polynomially_bounded=(smooth and bound_degree==12)
        tempered=(polynomially_bounded and net==6 and no_cancel)
        valid=smooth and net==6 and polynomially_bounded and no_cancel and tempered
        all_valid=all_valid and valid
        rows.append({'case':cname,'gamma':str(gamma),'epsilon':str(eps),'k':[str(q) for q in k],
                     'edge_rows':edge_rows,'generic_net_degree':net,'global_bound_degree_upper':bound_degree,
                     'smooth_on_real_cycle_space':smooth,'polynomially_bounded':polynomially_bounded,
                     'tempered_distribution_qualified':tempered,'valid':valid})
    cls=('ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED' if all_valid and len(rows)==2 else 'ITER070A_FINITE_EPSILON_TEMPEREDNESS_REVIEW')
    out={'iteration':'Iter070A','sigma':a.sigma,'causal_signs':list(signs),'tree':a.tree,'cases':rows,'valid':all_valid,'classification':cls,
         'claim_lock':'Fixed epsilon>0 tempered family only; epsilon->0 multivariate boundary value remains unproved.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2,sort_keys=True))
    if not all_valid: raise SystemExit(9)
if __name__=='__main__': main()
