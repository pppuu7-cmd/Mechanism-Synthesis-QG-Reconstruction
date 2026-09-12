#!/usr/bin/env python3
"""General reduced-Toller residue/power-series validation for gamma-simple sectors.

The existing closed-form reduced Toller implementation evaluates a finite sum
of Gauss 2F1 functions. For beta>0 we can instead expand each 2F1 directly in
its defining z=e^{-2 beta} power series. In the boost-eigenvalue contour
picture this is the exponentially weighted residue series. This avoids the
integer-degenerate 1-z analytic-continuation path that caused numerical
failures in generic hypergeometric backends.

Scope: pure-boost reduced matrix elements, gamma-simple k=j, with l=j,j+1,j+2.
This validates a stable branch kernel; it is not yet the full ten-edge direct
relative-group causal vertex.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from regulated import endpoint_precontraction_scan as ep
from regulated.j_equal_l_residue_series import series_2f1

mp.mp.dps = 90
BETAS = [mp.mpf(x) for x in ('0.03','0.05','0.1','0.3','0.7','1.5')]


def fmt(x, n=24):
    return mp.nstr(x, n)


def cfmt(z, n=24):
    return [fmt(mp.re(z),n), fmt(mp.im(z),n)]


def relerr(a,b):
    return abs(a-b)/max(abs(b),mp.mpf('1e-70'))


def toller_plus_series(tj:int, tl:int, tm:int, tk:int, rho, beta):
    z=mp.e**(-2*beta)
    P=ep.prefactor(tj,tl,tm,tk)
    total=mp.mpc(0)
    max_terms=0; converged=True; worst_last=mp.mpf('0')
    mkp=(tm+tk)//2
    a1=max(0,mkp); b1=min((tj+tm)//2,(tj+tk)//2)
    a2=max(0,mkp); b2=min((tl+tm)//2,(tl+tk)//2)
    j=mp.mpf(tj)/2; l=mp.mpf(tl)/2
    Bgamma=(1+j)+1j*rho
    for n1 in range(a1,b1+1):
        for n2 in range(a2,b2+1):
            dgamma=(tk+tm)//2-n1-n2-1
            q=mp.gamma(Bgamma+dgamma)/mp.gamma(Bgamma)
            q*=ep.facti(-(tk+tm)//2+n1+n2)
            q*=ep.binomi((tj-tm)//2, -(tk+tm)//2+n1)
            q*=ep.binomi((tl-tm)//2, -(tk+tm)//2+n2)
            q*=ep.binomi((tj+tm)//2,n1)
            q*=ep.binomi((tl+tm)//2,n2)
            q*=ep.sign_int((tj-tl)//2+n1+n2)
            er=-1+mp.mpf(tk+tm)/2-2*n2
            q*=mp.e**(beta*(er+1j*rho))
            a=1-mp.mpf(tk+tm)/2+n1+n2
            b=(1+l)-1j*rho
            c=(1-mp.mpf(tj+tk+tm)/2+n1+n2)-1j*rho
            h,nt,cv,last=series_2f1(a,b,c,z,tol=mp.mpf('1e-62'))
            max_terms=max(max_terms,nt); converged=converged and cv
            worst_last=max(worst_last,last)
            total += q*h
    return P*total,max_terms,converged,worst_last


def toller_minus_series(tj:int, tl:int, tm:int, tk:int, rho, beta):
    z=mp.e**(-2*beta)
    P=ep.prefactor(tj,tl,tm,tk)
    total=mp.mpc(0)
    max_terms=0; converged=True; worst_last=mp.mpf('0')
    mmk=(tm-tk)//2
    a1=max(0,mmk); b1=min((tl+tm)//2,(tl-tk)//2)
    a2=max(0,mmk); b2=min((tj+tm)//2,(tj-tk)//2)
    j=mp.mpf(tj)/2; l=mp.mpf(tl)/2
    Bgamma=(1+l)-1j*rho
    for n1 in range(a1,b1+1):
        for n2 in range(a2,b2+1):
            dgamma=(-tk+tm)//2-n1-n2-1
            q=mp.gamma(Bgamma+dgamma)/mp.gamma(Bgamma)
            q*=ep.facti((tk-tm)//2+n1+n2)
            q*=ep.binomi((tl-tm)//2,(tk-tm)//2+n1)
            q*=ep.binomi((tj-tm)//2,(tk-tm)//2+n2)
            q*=ep.binomi((tl+tm)//2,n1)
            q*=ep.binomi((tj+tm)//2,n2)
            q*=ep.sign_int(n1+n2)
            er=-1+mp.mpf(-tk+tm)/2-2*n2
            q*=mp.e**(beta*(er-1j*rho))
            a=1+mp.mpf(tk-tm)/2+n1+n2
            b=(1+j)+1j*rho
            c=(1-l+mp.mpf(tk-tm)/2+n1+n2)+1j*rho
            h,nt,cv,last=series_2f1(a,b,c,z,tol=mp.mpf('1e-62'))
            max_terms=max(max_terms,nt); converged=converged and cv
            worst_last=max(worst_last,last)
            total += q*h
    return P*total,max_terms,converged,worst_last


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma)
    ep.GAMMA=gamma

    rows=[]; worst=mp.mpf('0'); additive_worst=mp.mpf('0')
    worst_case=None; max_terms=0; failures=0
    by_delta={0:{'worst':mp.mpf('0'),'max_terms':0},
              1:{'worst':mp.mpf('0'),'max_terms':0},
              2:{'worst':mp.mpf('0'),'max_terms':0}}

    for tj in (1,2,3,4):
        rho=gamma*(mp.mpf(tj)/2)
        for dl in (0,1,2):
            tl=tj+2*dl
            for tm in range(-tj,tj+1,2):
                for beta in BETAS:
                    sp,np,cp,lp=toller_plus_series(tj,tl,tm,tj,rho,beta)
                    sm,nm,cm,lm=toller_minus_series(tj,tl,tm,tj,rho,beta)
                    tp=ep.toller_plus(tj,tl,tm,tj,rho,beta)
                    tn=ep.toller_minus(tj,tl,tm,tj,rho,beta)
                    epv=relerr(sp,tp); emv=relerr(sm,tn)
                    ea=relerr(sp+sm,tp+tn)
                    local=max(epv,emv)
                    max_terms=max(max_terms,np,nm)
                    by_delta[dl]['worst']=max(by_delta[dl]['worst'],local)
                    by_delta[dl]['max_terms']=max(by_delta[dl]['max_terms'],np,nm)
                    additive_worst=max(additive_worst,ea)
                    if not cp or not cm: failures+=1
                    if local>worst:
                        worst=local; worst_case=(tj,tl,tm,beta,epv,emv,np,nm)
                    rows.append({
                        'two_j':tj,'two_l':tl,'delta_l':dl,'two_m':tm,
                        'rho':fmt(rho),'beta':fmt(beta),
                        'series_plus':cfmt(sp),'series_minus':cfmt(sm),
                        'target_plus':cfmt(tp),'target_minus':cfmt(tn),
                        'relative_error_plus':fmt(epv),'relative_error_minus':fmt(emv),
                        'additive_relative_error':fmt(ea),
                        'terms_plus':np,'terms_minus':nm,
                        'converged_plus':cp,'converged_minus':cm,
                        'last_term_ratio_plus':fmt(lp),'last_term_ratio_minus':fmt(lm),
                    })

    verdict=('GENERAL_RESIDUE_SERIES_MATCHES_TOLLER'
             if failures==0 and worst < mp.mpf('1e-40')
             else 'GENERAL_RESIDUE_SERIES_NEEDS_REVIEW')
    out={
        'gamma':str(args.gamma),'mp_dps':mp.mp.dps,
        'betas':[fmt(x) for x in BETAS],'cases':len(rows),
        'series_nonconvergences':failures,'max_terms_used':max_terms,
        'worst_branch_relative_error':fmt(worst),
        'worst_additive_relative_error':fmt(additive_worst),
        'by_delta_l':{str(k):{'worst_branch_relative_error':fmt(v['worst']),
                              'max_terms_used':v['max_terms']} for k,v in by_delta.items()},
        'worst_case':None if worst_case is None else {
            'two_j':worst_case[0],'two_l':worst_case[1],'two_m':worst_case[2],
            'beta':fmt(worst_case[3]),'error_plus':fmt(worst_case[4]),
            'error_minus':fmt(worst_case[5]),'terms_plus':worst_case[6],
            'terms_minus':worst_case[7]},
        'verdict':verdict,'rows':rows,
        'interpretation_guardrail':(
            'This is a stable beta>0 reduced pure-boost Toller branch kernel for '
            'gamma-simple k=j and l=j,j+1,j+2. Agreement with the existing closed '
            'form validates the residue-series evaluator only; the direct causal '
            'vertex still requires ten pairwise T(g_b^-1 g_a) factors, rotations, '
            'boundary contractions, and four SL(2,C) integrations.'),
    }
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if verdict!='GENERAL_RESIDUE_SERIES_MATCHES_TOLLER':
        raise SystemExit(3)

if __name__=='__main__':
    main()
