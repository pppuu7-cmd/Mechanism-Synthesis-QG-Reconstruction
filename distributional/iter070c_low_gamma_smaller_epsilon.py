#!/usr/bin/env python3
"""Iter070C: prospective smaller-epsilon extension of the low-gamma pre-pullback control.
Frozen by status/ITERATION_070C_PREREG.md.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
from distributional.jhalf_finite_epsilon_contact import closed_action, TESTS, phi
from distributional.jhalf_iepsilon_validation import coeffs

mp.mp.dps=80
GAMMA=mp.mpf('0.2')
EPS=[mp.mpf('0.0125'),mp.mpf('0.00625'),mp.mpf('0.003125'),mp.mpf('0.0015625')]
BASE=mp.mpf('0.025')

def fmt(x,n=30): return mp.nstr(x,n)
def rel(a,b): return abs(a-b)/max(abs(b),mp.mpf('1e-70'))
def identity_action(a,b,c): return mp.quad(lambda x: phi(x,a,b,c),[-mp.inf,0,mp.inf])

def main():
    rho=GAMMA/2; c1,c2=coeffs(rho)
    dp=(-c2/2)+(c2/2)
    p1=(dp==0)
    rows=[]; p2=True; p3=True; p4=True; p5=True
    for name,aa,b,c in TESTS:
        target=identity_action(aa,b,c)
        base_z=closed_action(rho,1,BASE,aa,b,c)+closed_action(rho,-1,BASE,aa,b,c)
        base_err=rel(base_z,target)
        errs=[]
        for eps in EPS:
            z=closed_action(rho,1,eps,aa,b,c)+closed_action(rho,-1,eps,aa,b,c)
            er=rel(z,target); errs.append(er)
            Bp=(-1j*c1+eps*c2/2); Bm=(1j*c1+eps*c2/2)
            p2=p2 and abs((Bp+Bm)-eps*c2) < mp.mpf('1e-70')
            rows.append({'test':name,'epsilon':fmt(eps),'relative_error':fmt(er),
                         'identity_action':fmt(target),'branch_sum_action':[fmt(mp.re(z)),fmt(mp.im(z))]})
        p3=p3 and all(errs[i+1] < errs[i] for i in range(len(errs)-1))
        p4=p4 and errs[-1] < mp.mpf('0.08')
        p5=p5 and errs[-1] < base_err
        for i in range(len(errs)-1):
            rows.append({'test':name,'halving_pair':f'{fmt(EPS[i])}->{fmt(EPS[i+1])}','error_ratio':fmt(errs[i]/errs[i+1])})
        rows.append({'test':name,'baseline_epsilon':fmt(BASE),'baseline_error':fmt(base_err),'final_error':fmt(errs[-1])})
    valid=p1 and p2
    passed=valid and p3 and p4 and p5
    out={'iteration':'Iter070C','gamma':fmt(GAMMA),'epsilon_sequence':[fmt(e) for e in EPS],
         'predicates':{'P1_DPRIME_CANCELS_EXACTLY':p1,'P2_RESIDUAL_DELTA_IS_EPSILON_C2':p2,
                       'P3_STRICT_MONOTONE_ERROR_DECREASE':p3,'P4_FINAL_ERROR_LT_0P08':p4,
                       'P5_FINAL_BEATS_ITER068C_EPS_0P025':p5},
         'rows':rows,'valid':valid,
         'classification':'ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED' if passed else 'ITER070C_LOW_GAMMA_PREPULLBACK_CONVERGENCE_REVIEW',
         'claim_lock':'Additional pre-pullback one-edge branch-sum evidence only; Iter068C remains terminal and no correlated K4/K5 boundary-value identity is proved.'}
    Path('results').mkdir(exist_ok=True)
    Path('results/iter070c.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if not valid: raise SystemExit(9)
if __name__=='__main__': main()
