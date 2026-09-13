#!/usr/bin/env python3
"""Iter069A: exact symbolic homogeneous asymptotics of the reduced K4 joint-spectral family.

Frozen by status/ITERATION_069A_PREREG.md.  No finite-part prescription is used.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp
from distributional.k4_forest_order_finite_part import constrained_edge_flows, TREES, EDGE_NAMES


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--tree',required=True,choices=sorted(TREES)); ap.add_argument('--output',required=True); a=ap.parse_args()
    k0,k1,k2=sp.symbols('k0 k1 k2', real=True); k3=-(k0+k1+k2)
    y,x,tree,chords,det=constrained_edge_flows(a.tree,(k0,k1,k2,k3))
    lam=sp.symbols('lambda', real=True); v=sp.symbols('v0:3', real=True)
    c2=sp.symbols('c2', nonzero=True, real=True)
    eps=sp.symbols('epsilon', positive=True, real=True)
    s=sp.symbols('s0:6', nonzero=True, real=True)

    slopes=[]; factor_rows=[]
    source_net=0; control_net=0
    src_lead=sp.Integer(1); ctl_lead=sp.Integer(1)
    for idx,xe in enumerate(x):
        xl=sp.expand(xe.subs({y[i]:lam*v[i] for i in range(3)}))
        P=sp.Poly(xl,lam,domain='EX')
        slope=sp.simplify(P.coeff_monomial(lam)); slopes.append(slope)
        num=1 + sp.symbols('c1', real=True)*xl + (c2/2)*xl**2
        den=xl-sp.I*s[idx]*eps
        Pn=sp.Poly(sp.expand(num),lam,domain='EX'); Pd=sp.Poly(sp.expand(den),lam,domain='EX')
        dn,dd=int(Pn.degree()),int(Pd.degree())
        source_net += dn-dd; control_net += -dd
        nlead=sp.simplify(Pn.LC()); dlead=sp.simplify(Pd.LC())
        src_lead=sp.simplify(src_lead*nlead/dlead)
        ctl_lead=sp.simplify(ctl_lead/dlead)
        factor_rows.append({'edge':EDGE_NAMES[idx],'slope':str(slope),'num_degree':dn,'den_degree':dd,
                            'numerator_leading':str(nlead),'denominator_leading':str(dlead)})

    slope_product=sp.factor(sp.prod(slopes))
    expected_src=sp.factor((c2/2)**6*slope_product)
    expected_ctl=sp.factor(1/slope_product)
    free_src=src_lead.free_symbols
    sign_symbols=set(s); k_symbols={k0,k1,k2}
    gates={
      'six_nonzero_slope_polynomials': len(slopes)==6 and all(q!=0 for q in slopes),
      'source_net_degree_plus6': source_net==6,
      'control_net_degree_minus6': control_net==-6,
      'source_leading_formula_exact': sp.simplify(src_lead-expected_src)==0,
      'control_leading_formula_exact': sp.simplify(ctl_lead-expected_ctl)==0,
      'source_lead_sign_independent': not bool(free_src & sign_symbols),
      'source_lead_epsilon_independent': eps not in free_src,
      'source_lead_external_flow_independent': not bool(free_src & k_symbols),
    }
    passed=all(gates.values())
    out={'iteration':'Iter069A','tree':a.tree,'tree_edges':[EDGE_NAMES[i] for i in tree],
         'chord_edges':[EDGE_NAMES[i] for i in chords],'tree_incidence_det':str(det),
         'factor_rows':factor_rows,'slope_product':str(slope_product),
         'source_net_degree':source_net,'control_net_degree':control_net,
         'source_leading_coefficient':str(sp.factor(src_lead)),
         'control_leading_coefficient':str(sp.factor(ctl_lead)),
         'gates':gates,'valid':passed,
         'classification':('ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT' if passed else 'ITER069A_SYMBOLIC_ASYMPTOTIC_REVIEW'),
         'claim_lock':'Reduced joint-spectral rational family only; generic growth is not a no-go for analytic/distributional boundary values and is not a causal-vertex divergence theorem.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(9)
if __name__=='__main__': main()
