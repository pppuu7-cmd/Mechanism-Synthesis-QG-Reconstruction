#!/usr/bin/env python3
"""Iter069B: held-out exact K4 joint-spectral radial asymptotics.

Frozen by status/ITERATION_069B_PREREG.md.  One job handles one (case,tree)
and evaluates the frozen 8 sigma classes x 3 primitive directions = 24 cases.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp
from distributional.k4_forest_order_finite_part import build_kernel, constrained_edge_flows, TREES, EDGE_NAMES

CASES={
 'H6':(sp.Rational(37,100),sp.Rational(41,1000),(sp.Rational(17,100),sp.Rational(-29,100),sp.Rational(21,100),sp.Rational(-9,100))),
 'H7':(sp.Rational(173,100),sp.Rational(137,1000),(sp.Rational(-26,100),sp.Rational(34,100),sp.Rational(-11,100),sp.Rational(3,100))),
}
SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']
DIRS={'V1':(1,2,3),'V2':(2,-1,3),'V3':(3,1,-2)}

def causal_signs(label):
    sg=[1 if c=='+' else -1 for c in label]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return tuple(sg[a]*sg[b] for a,b in edges)

def sign_text(signs): return ''.join('+' if x>0 else '-' for x in signs)

def radial(expr,y,v):
    lam=sp.symbols('lambda', real=True)
    z=sp.cancel(expr.subs({y[i]:lam*v[i] for i in range(3)}))
    num,den=sp.fraction(z)
    pn=sp.Poly(sp.expand(num),lam,domain='EX'); pd=sp.Poly(sp.expand(den),lam,domain='EX')
    dn,dd=int(pn.degree()),int(pd.degree())
    lead=sp.cancel(pn.LC()/pd.LC())
    return dn,dd,dn-dd,sp.factor(lead)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',required=True,choices=sorted(CASES)); ap.add_argument('--tree',required=True,choices=sorted(TREES)); ap.add_argument('--output',required=True); a=ap.parse_args()
    gamma,eps,k=CASES[a.case]
    y0,x0,tree,chords,det=constrained_edge_flows(a.tree,k)
    rows=[]; all_valid=True
    for sigma in SIGMAS:
        signs=causal_signs(sigma)
        y,src,_=build_kernel(gamma,eps,signs,k,a.tree,control=False)
        yc,ctl,_=build_kernel(gamma,eps,signs,k,a.tree,control=True)
        if tuple(map(str,y))!=tuple(map(str,yc)): raise RuntimeError('source/control cycle coordinates disagree')
        for dname,v in DIRS.items():
            slopes=[]
            lam=sp.symbols('lambda',real=True)
            for xe in x0:
                p=sp.Poly(sp.expand(xe.subs({y0[i]:lam*v[i] for i in range(3)})),lam,domain='EX')
                slopes.append(sp.simplify(p.coeff_monomial(lam)))
            src_dn,src_dd,src_deg,src_lead=radial(src,y,v)
            ctl_dn,ctl_dd,ctl_deg,ctl_lead=radial(ctl,y,v)
            gates={'six_slopes_nonzero':all(q!=0 for q in slopes),'source_degree_plus6':src_deg==6,
                   'control_degree_minus6':ctl_deg==-6,'source_lead_nonzero':src_lead!=0,'control_lead_nonzero':ctl_lead!=0}
            valid=all(gates.values()); all_valid=all_valid and valid
            rows.append({'case':a.case,'tree':a.tree,'sigma':sigma,'causal_signs':sign_text(signs),'direction':dname,'v':list(v),
                         'edge_slopes':[str(q) for q in slopes],
                         'source_num_degree':src_dn,'source_den_degree':src_dd,'source_net_degree':src_deg,'source_leading':str(src_lead),
                         'control_num_degree':ctl_dn,'control_den_degree':ctl_dd,'control_net_degree':ctl_deg,'control_leading':str(ctl_lead),
                         'gates':gates,'valid':valid})
    # Within this lane, each direction must have exactly one source-leading value across all eight causal classes.
    local_sign_independent=True
    for d in DIRS:
        vals={r['source_leading'] for r in rows if r['direction']==d}
        local_sign_independent=local_sign_independent and len(vals)==1
    all_valid=all_valid and local_sign_independent and len(rows)==24
    out={'iteration':'Iter069B','case':a.case,'tree':a.tree,'gamma':str(gamma),'epsilon':str(eps),'k':[str(q) for q in k],
         'rows':rows,'local_causal_sign_leading_independence':local_sign_independent,'valid':all_valid,
         'classification':('ITER069B_LANE_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT' if all_valid else 'ITER069B_LANE_REVIEW'),
         'claim_lock':'Held-out generic radial asymptotics of reduced joint-spectral rational family only; no boundary-value or vertex divergence theorem.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2,sort_keys=True))
    if not all_valid: raise SystemExit(9)
if __name__=='__main__': main()
