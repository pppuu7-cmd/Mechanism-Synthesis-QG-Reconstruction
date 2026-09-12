#!/usr/bin/env python3
"""Stable residue-series realization of reduced Toller matrices for j=l.

For the gamma-simple sector j=l, Eq. (46) of Bianchi-Chen-Gamonal,
Phys. Rev. D 114, 046014 (2026), gives Toller t^+/- as a prefactor times
2F1(...; z=e^{-2 beta}). Expanding 2F1 in its defining power series produces
an exponentially weighted residue series with the same pole lattice that
appears in the boost-eigenvalue contour representation.

This script evaluates that series by a recurrence, without calling hyp2f1,
and compares it to the independently implemented general reduced-Toller
closed form already validated against sl2cfoam through t+ + t-.

Scope: j=l only. This is a numerical kernel validation, not yet the full
10-wedge direct relative-group causal vertex and not F9 closure.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from regulated import endpoint_precontraction_scan as ep

mp.mp.dps = 90
BETAS = [mp.mpf(x) for x in ('0.03','0.05','0.1','0.3','0.7','1.5')]


def fmt(x, n=24):
    return mp.nstr(x, n)


def cfmt(z, n=24):
    return [fmt(mp.re(z),n), fmt(mp.im(z),n)]


def relerr(a,b):
    return abs(a-b)/max(abs(b), mp.mpf('1e-70'))


def series_2f1(a,b,c,z,tol=mp.mpf('1e-65'),max_terms=200000):
    term=mp.mpc(1)
    total=mp.mpc(1)
    small=0
    for n in range(max_terms-1):
        term *= z*(a+n)*(b+n)/((c+n)*(n+1))
        total += term
        scale=max(abs(total),mp.mpf('1e-80'))
        if abs(term) < tol*scale:
            small += 1
            if small >= 5:
                return total,n+2,True,abs(term)/scale
        else:
            small=0
    return total,max_terms,False,abs(term)/max(abs(total),mp.mpf('1e-80'))


def t_j_equal_l_series(sign:int,two_j:int,two_m:int,rho,beta):
    j=mp.mpf(two_j)/2
    m=mp.mpf(two_m)/2
    z=mp.e**(-2*beta)
    if sign==1:
        exponent=-(j-1j*rho+m+1)*beta
        pref=(mp.gamma(2*j+2)*mp.gamma(1j*rho-m)
              /(mp.gamma(j-m+1)*mp.gamma(j+1+1j*rho)))
        a=j+m+1
        b=j+1-1j*rho
        c=1+m-1j*rho
    elif sign==-1:
        exponent=-(j+1j*rho-m+1)*beta
        pref=(mp.gamma(2*j+2)*mp.gamma(-1j*rho+m)
              /(mp.gamma(j+m+1)*mp.gamma(j+1-1j*rho)))
        a=j-m+1
        b=j+1+1j*rho
        c=1-m+1j*rho
    else:
        raise ValueError('sign must be +/-1')
    h,n,conv,last=series_2f1(a,b,c,z)
    return mp.e**(exponent)*pref*h,n,conv,last


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma)
    ep.GAMMA=gamma

    rows=[]
    worst=mp.mpf('0'); worst_case=None; max_terms=0; failures=0
    additive_worst=mp.mpf('0')
    for two_j in (1,2,3,4):
        rho=gamma*(mp.mpf(two_j)/2)
        for two_m in range(-two_j,two_j+1,2):
            for beta in BETAS:
                sp,np,cp,lp=t_j_equal_l_series(+1,two_j,two_m,rho,beta)
                sm,nm,cm,lm=t_j_equal_l_series(-1,two_j,two_m,rho,beta)
                # General closed-form implementation from the native-Toller validation path.
                tp=ep.toller_plus(two_j,two_j,two_m,two_j,rho,beta)
                tm=ep.toller_minus(two_j,two_j,two_m,two_j,rho,beta)
                epv=relerr(sp,tp); emv=relerr(sm,tm)
                ea=relerr(sp+sm,tp+tm)
                max_terms=max(max_terms,np,nm)
                additive_worst=max(additive_worst,ea)
                if not cp or not cm: failures+=1
                local=max(epv,emv)
                if local>worst:
                    worst=local
                    worst_case=(two_j,two_m,beta,epv,emv,np,nm)
                rows.append({
                    'two_j':two_j,'two_l':two_j,'two_m':two_m,
                    'rho':fmt(rho),'beta':fmt(beta),
                    'series_plus':cfmt(sp),'series_minus':cfmt(sm),
                    'target_plus':cfmt(tp),'target_minus':cfmt(tm),
                    'relative_error_plus':fmt(epv),'relative_error_minus':fmt(emv),
                    'additive_relative_error':fmt(ea),
                    'terms_plus':np,'terms_minus':nm,
                    'converged_plus':cp,'converged_minus':cm,
                    'last_term_ratio_plus':fmt(lp),'last_term_ratio_minus':fmt(lm),
                })

    out={
        'gamma':str(args.gamma),'mp_dps':mp.mp.dps,
        'betas':[fmt(x) for x in BETAS],
        'cases':len(rows),'series_nonconvergences':failures,
        'max_terms_used':max_terms,
        'worst_branch_relative_error':fmt(worst),
        'worst_additive_relative_error':fmt(additive_worst),
        'worst_case':None if worst_case is None else {
            'two_j':worst_case[0],'two_m':worst_case[1],'beta':fmt(worst_case[2]),
            'error_plus':fmt(worst_case[3]),'error_minus':fmt(worst_case[4]),
            'terms_plus':worst_case[5],'terms_minus':worst_case[6],
        },
        'rows':rows,
        'verdict':('J_EQUAL_L_RESIDUE_SERIES_MATCHES_GENERAL_TOLLER'
                   if failures==0 and worst < mp.mpf('1e-45') else
                   'J_EQUAL_L_RESIDUE_SERIES_NEEDS_REVIEW'),
        'interpretation_guardrail':(
            'The recurrence is the Eq.46 2F1 power/residue series for j=l. '
            'It supplies a stable beta>0 causal-branch kernel in this sector, '
            'but does not by itself implement the ten pairwise T(g_b^-1 g_a) '
            'factors or the four SL(2,C) integrations of the causal vertex.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if out['verdict']!='J_EQUAL_L_RESIDUE_SERIES_MATCHES_GENERAL_TOLLER':
        raise SystemExit(3)

if __name__=='__main__':
    main()
