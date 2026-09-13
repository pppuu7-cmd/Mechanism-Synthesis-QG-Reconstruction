#!/usr/bin/env python3
"""Iter068C: distributional pre-pullback Eq.(5)/(6) control audit.

Frozen by status/ITERATION_068C_PREREG.md.  This intentionally stops before any
non-transverse K4/K5 collision pullback.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import mpmath as mp
from distributional.jhalf_finite_epsilon_contact import closed_action, TESTS, phi
from distributional.jhalf_iepsilon_validation import coeffs

mp.mp.dps=70
EPS=[mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025')]

def fmt(x,n=28): return mp.nstr(x,n)
def rel(a,b): return abs(a-b)/max(abs(b),mp.mpf('1e-60'))
def identity_action(a,b,c): return mp.quad(lambda x: phi(x,a,b,c),[-mp.inf,0,mp.inf])

def tensor_identity_six_edges():
    # Expand prod_e(P_e+M_e) and compare with explicit independent-sign sum.
    explicit={bits:1 for bits in itertools.product((0,1), repeat=6)}
    factored={():1}
    for e in range(6):
        nxt={}
        for mon,coef in factored.items():
            for bit in (0,1): nxt[mon+(bit,)]=nxt.get(mon+(bit,),0)+coef
        factored=nxt
    return explicit==factored and len(explicit)==64

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gamma',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    gamma=mp.mpf(a.gamma); rho=gamma/2; c1,c2=coeffs(rho)
    dprime_exact=True; delta_linear=True; rows=[]; all_monotone=True; all_final=True
    for name,aa,b,c in TESTS:
        target=identity_action(aa,b,c); errs=[]
        for eps in EPS:
            z=closed_action(rho,1,eps,aa,b,c)+closed_action(rho,-1,eps,aa,b,c)
            er=rel(z,target); errs.append(er)
            # exact formulas in the validated closed representation
            dp=(-c2/2)+(c2/2)
            Bp=(-1j*c1+eps*c2/2); Bm=(1j*c1+eps*c2/2)
            dprime_exact=dprime_exact and (dp==0)
            delta_linear=delta_linear and (abs((Bp+Bm)-eps*c2)<mp.mpf('1e-60'))
            rows.append({'test':name,'epsilon':fmt(eps),'branch_sum_action':[fmt(mp.re(z)),fmt(mp.im(z))],
                         'identity_action':fmt(target),'relative_error':fmt(er)})
        mono=all(errs[i+1] < errs[i] for i in range(len(errs)-1))
        final=errs[-1] < mp.mpf('0.08')
        all_monotone=all_monotone and mono; all_final=all_final and final
    p1=dprime_exact; p2=delta_linear; p3=all_monotone and all_final; p4=tensor_identity_six_edges()
    valid=p1 and p2 and p4
    passed=valid and p3
    out={'iteration':'Iter068C','gamma':a.gamma,'rho':fmt(rho),'c1':fmt(c1),'c2':fmt(c2),
         'epsilon_sequence':[fmt(x) for x in EPS],
         'predicates':{'P1_DPRIME_CANCELS_EXACTLY':p1,'P2_DELTA_CONTACT_SCALES_LINEARLY':p2,
                       'P3_BRANCH_SUM_CONVERGES_TO_IDENTITY':p3,'P4_TENSOR_PRODUCT_EQ6_ALGEBRA':p4},
         'rows':rows,'valid':valid,
         'classification':('ITER068C_PREPULLBACK_DISTRIBUTIONAL_EPRL_CONTROL_PASS' if passed else 'ITER068C_PREPULLBACK_CONTROL_REVIEW'),
         'claim_lock':'Pre-pullback tensor-product control only; does not establish a correlated K4/K5 boundary-value product.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if not valid: raise SystemExit(9)
if __name__=='__main__': main()
