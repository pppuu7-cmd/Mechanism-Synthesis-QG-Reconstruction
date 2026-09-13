#!/usr/bin/env python3
"""Iter076D: frozen source-domain local Haar/BCH prerequisite lanes."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp
import sympy as sp


def write(out, path):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True), encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not out['valid']:
        raise SystemExit(9)


def lane_a():
    b=sp.symbols('beta')
    s=sp.series(sp.sinh(b)**2/b**2,b,0,6).removeO().expand()
    coeff={n:sp.expand(s).coeff(b,n) for n in range(6)}
    pred={
      'constant_exact': coeff[0]==1,
      'quadratic_exact_one_third': coeff[2]==sp.Rational(1,3),
      'quartic_exact_two_fortyfive': coeff[4]==sp.Rational(2,45),
      'odd_terms_zero': coeff[1]==0 and coeff[3]==0 and coeff[5]==0,
    }
    ok=all(pred.values())
    return {'iteration':'Iter076D','lane':'A','series':str(s),'coefficients':{str(k):str(v) for k,v in coeff.items()},'predicates':pred,'valid':ok}


def lane_b():
    mp.mp.dps=80
    bs=[mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025'),mp.mpf('0.0125')]
    rows=[]; errs=[]
    for b in bs:
        r=(mp.sinh(b)/b)**2
        est=(r-1)/(b*b)
        er=abs(est-mp.mpf(1)/3)
        errs.append(er)
        rows.append({'beta':mp.nstr(b,20),'ratio':mp.nstr(r,40),'estimator':mp.nstr(est,40),'error_to_one_third':mp.nstr(er,30)})
    pred={
      'strict_error_convergence': all(errs[i+1] < errs[i] for i in range(len(errs)-1)),
      'final_error_lt_2e_5': errs[-1] < mp.mpf('2e-5'),
      'flat_density_control_rejected': abs((mp.sinh(bs[-1])/bs[-1])**2-1)/(bs[-1]**2) > mp.mpf('0.3'),
    }
    return {'iteration':'Iter076D','lane':'B','rows':rows,'predicates':pred,'valid':all(pred.values())}


def trunc_matrix(M,t,order=3):
    return M.applyfunc(lambda e: sp.series(sp.expand(e),t,0,order).removeO().expand())


def exp2(M,t):
    I=sp.eye(M.rows)
    return I+t*M+t**2*(M*M)/2


def log_near_I(P,t):
    I=sp.eye(P.rows); Z=trunc_matrix(P-I,t,3)
    return trunc_matrix(Z-Z*Z/2,t,3)


def generic_xy():
    x1,x2,x3,y1,y2,y3=sp.symbols('x1 x2 x3 y1 y2 y3')
    X=sp.Matrix([[x1,x2],[x3,-x1]])
    Y=sp.Matrix([[y1,y2],[y3,-y1]])
    return X,Y


def lane_c():
    t=sp.symbols('t'); X,Y=generic_xy(); I=sp.eye(2)
    P=trunc_matrix(exp2(-Y,t)*exp2(X,t),t,3)
    L=log_near_I(P,t)
    comm=X*Y-Y*X
    target=t*(X-Y)+t**2*comm/2
    revP=trunc_matrix(exp2(-X,t)*exp2(Y,t),t,3)
    revL=log_near_I(revP,t)
    p1=trunc_matrix(L-target,t,3)==sp.zeros(2)
    p2=trunc_matrix(revL+L,t,3)==sp.zeros(2)
    return {'iteration':'Iter076D','lane':'C','predicates':{'bch_quadratic_exact':bool(p1),'order_reversal_exact_through_t2':bool(p2)},'valid':bool(p1 and p2)}


def lane_d():
    t=sp.symbols('t'); X,Y=generic_xy()
    P=trunc_matrix(exp2(-Y,t)*exp2(X,t),t,3); L=log_near_I(P,t)
    comm=X*Y-Y*X
    wrong=t*(X-Y)-t**2*comm/2
    wrong_sign_rejected=trunc_matrix(L-wrong,t,3)!=sp.zeros(2)
    b=sp.symbols('beta')
    true_series=sp.series(sp.sinh(b)**2/b**2,b,0,4).removeO().expand()
    flat_rejected=sp.expand(true_series-1)!=0 and true_series.coeff(b,2)==sp.Rational(1,3)
    pred={'wrong_bch_sign_rejected':bool(wrong_sign_rejected),'flat_radial_density_rejected':bool(flat_rejected),'scope_guard_present':True}
    return {'iteration':'Iter076D','lane':'D','scope':'K4_PUSHFORWARD_NOT_ESTABLISHED','predicates':pred,'valid':all(pred.values())}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD'),required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    out={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    out['claim_lock']='Source-domain local prerequisite only; K4 pushforward and epsilon^-1 coefficient remain undefined.'
    write(out,a.output)

if __name__=='__main__': main()
