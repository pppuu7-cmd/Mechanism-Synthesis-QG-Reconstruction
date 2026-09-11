#!/usr/bin/env python3
"""High-precision endpoint diagnostics for branch-resolved Toller boosters.

Purpose
-------
The ordinary sl2cfoam B4 algorithm integrates each magnetic p-sector before
recoupling. Individual Toller branches can be singular at beta -> 0 even when
T+ + T- is finite. This script tests whether the relevant cancellation occurs
only after the magnetic/4j recoupling sum is formed *before* radial integration.

This is a regulator/ordering diagnostic, not an implementation of the full
Feynman i-epsilon causal vertex.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
from sympy import Rational
from sympy.physics.wigner import wigner_3j

mp.mp.dps = 80

BETAS = [mp.mpf(x) for x in ("0.2","0.1","0.05","0.02","0.01","0.005","0.002")]
CUTOFFS = [mp.mpf(x) for x in ("0.2","0.1","0.05","0.02","0.01")]
GAMMA = mp.mpf("1.2")


def facti(n: int):
    if n < 0:
        return mp.mpf("0")
    return mp.factorial(n)


def binomi(n: int, r: int):
    if r < 0 or r > n or n < 0:
        return mp.mpf("0")
    return mp.binomial(n, r)


def sign_int(n: int):
    return -1 if n & 1 else 1


def prefactor(tj: int, tl: int, tm: int, tk: int):
    jmk=(tj-tk)//2; jpk=(tj+tk)//2; lmk=(tl-tk)//2; lpk=(tl+tk)//2
    jmm=(tj-tm)//2; jpm=(tj+tm)//2; lmm=(tl-tm)//2; lpm=(tl+tm)//2
    num=facti(jmk)*facti(jpk)*facti(lmk)*facti(lpk)
    den=facti(jmm)*facti(jpm)*facti(lmm)*facti(lpm)
    return mp.sqrt((1+tj)*(1+tl))*mp.sqrt(num/den)


def toller_plus(tj:int, tl:int, tm:int, tk:int, rho, beta):
    z=mp.e**(-2*beta)
    P=prefactor(tj,tl,tm,tk)
    total=mp.mpc(0)
    mkp=(tm+tk)//2
    a1=max(0,mkp); b1=min((tj+tm)//2,(tj+tk)//2)
    a2=max(0,mkp); b2=min((tl+tm)//2,(tl+tk)//2)
    j=mp.mpf(tj)/2; l=mp.mpf(tl)/2
    Bgamma=(1+j)+1j*rho
    for n1 in range(a1,b1+1):
        for n2 in range(a2,b2+1):
            dgamma=(tk+tm)//2-n1-n2-1
            q=mp.gamma(Bgamma+dgamma)/mp.gamma(Bgamma)
            q*=facti(-(tk+tm)//2+n1+n2)
            q*=binomi((tj-tm)//2, -(tk+tm)//2+n1)
            q*=binomi((tl-tm)//2, -(tk+tm)//2+n2)
            q*=binomi((tj+tm)//2,n1)
            q*=binomi((tl+tm)//2,n2)
            q*=sign_int((tj-tl)//2+n1+n2)
            er=-1+mp.mpf(tk+tm)/2-2*n2
            q*=mp.e**(beta*(er+1j*rho))
            a=1-mp.mpf(tk+tm)/2+n1+n2
            b=(1+l)-1j*rho
            c=(1-mp.mpf(tj+tk+tm)/2+n1+n2)-1j*rho
            q*=mp.hyp2f1(a,b,c,z)
            total+=q
    return P*total


def toller_minus(tj:int, tl:int, tm:int, tk:int, rho, beta):
    z=mp.e**(-2*beta)
    P=prefactor(tj,tl,tm,tk)
    total=mp.mpc(0)
    mmk=(tm-tk)//2
    a1=max(0,mmk); b1=min((tl+tm)//2,(tl-tk)//2)
    a2=max(0,mmk); b2=min((tj+tm)//2,(tj-tk)//2)
    j=mp.mpf(tj)/2; l=mp.mpf(tl)/2
    Bgamma=(1+l)-1j*rho
    for n1 in range(a1,b1+1):
        for n2 in range(a2,b2+1):
            dgamma=(-tk+tm)//2-n1-n2-1
            q=mp.gamma(Bgamma+dgamma)/mp.gamma(Bgamma)
            q*=facti((tk-tm)//2+n1+n2)
            q*=binomi((tl-tm)//2,(tk-tm)//2+n1)
            q*=binomi((tj-tm)//2,(tk-tm)//2+n2)
            q*=binomi((tl+tm)//2,n1)
            q*=binomi((tj+tm)//2,n2)
            q*=sign_int(n1+n2)
            er=-1+mp.mpf(-tk+tm)/2-2*n2
            q*=mp.e**(beta*(er-1j*rho))
            a=1+mp.mpf(tk-tm)/2+n1+n2
            b=(1+j)+1j*rho
            c=(1-l+mp.mpf(tk-tm)/2+n1+n2)+1j*rho
            q*=mp.hyp2f1(a,b,c,z)
            total+=q
    return P*total


def tbranch(branch:int,tj:int,tl:int,tp:int,beta):
    # EPRL simple representation: boost magnetic k equals boundary j.
    rho=GAMMA*(mp.mpf(tj)/2)
    return toller_plus(tj,tl,tp,tj,rho,beta) if branch>0 else toller_minus(tj,tl,tp,tj,rho,beta)


def dsum(tj:int,tl:int,tp:int,beta):
    return tbranch(+1,tj,tl,tp,beta)+tbranch(-1,tj,tl,tp,beta)


def mpfloat_sympy(x):
    return mp.mpf(str(x.evalf(70)))


def w4jm(tj1,tj2,tj3,tj4,tm1,tm2,tm3,tm4,ti):
    # Exact copy of upstream sl2cfoam_w4jm convention.
    h=lambda n:Rational(n,2)
    w1=wigner_3j(h(tj1),h(tj2),h(ti),h(tm1),h(tm2),h(-tm1-tm2))
    w2=wigner_3j(h(ti),h(tj3),h(tj4),h(tm1+tm2),h(tm3),h(tm4))
    # upstream real_negpow(two_i + two_m1 + two_m2)
    n=ti+tm1+tm2
    if n%2: raise ValueError("non-integer phase")
    phase=1 if n%4==0 else -1
    return mp.mpf(phase)*mpfloat_sympy(w1)*mpfloat_sympy(w2)


def allowed_p(tj):
    vals=list(range(-tj,tj+1,2))
    return [p for p in itertools.product(vals, repeat=4) if sum(p)==0]


def recoupling_weight(tj,tl,p,ti,tk):
    pj=w4jm(tj,tj,tj,tj,*p,ti)
    pl=w4jm(tl,tl,tl,tl,*p,tk)
    return mp.sqrt((ti+1)*(tk+1))*pj*pl


def radial_measure(beta):
    # Exact beta-dependence of the SL(2,C) radial measure up to an irrelevant
    # beta-independent constant. Enough for endpoint powers and cutoff scaling.
    return mp.sinh(beta)**2


def branch_product(mask,tj,tl,p,beta):
    z=mp.mpc(1)
    for leg in range(4):
        branch=+1 if mask&(1<<leg) else -1
        z*=tbranch(branch,tj,tl,p[leg],beta)
    return z


def additive_product(tj,tl,p,beta):
    z=mp.mpc(1)
    for leg in range(4): z*=dsum(tj,tl,p[leg],beta)
    return z


def precontracted(mask,tj,tl,ti,tk,beta,additive=False):
    total=mp.mpc(0)
    for p in allowed_p(tj):
        w=recoupling_weight(tj,tl,p,ti,tk)
        prod=additive_product(tj,tl,p,beta) if additive else branch_product(mask,tj,tl,p,beta)
        total+=w*prod
    return radial_measure(beta)*total


def log_slope(xs,ys):
    pts=[(mp.log(x),mp.log(abs(y))) for x,y in zip(xs,ys) if mp.isfinite(abs(y)) and abs(y)>0]
    if len(pts)<3: return mp.nan
    xbar=sum(x for x,_ in pts)/len(pts); ybar=sum(y for _,y in pts)/len(pts)
    den=sum((x-xbar)**2 for x,_ in pts)
    return sum((x-xbar)*(y-ybar) for x,y in pts)/den


def recent_slope(vals):
    # Emphasize the asymptotic half of the grid.
    return log_slope(BETAS[-4:], vals[-4:])


def finite_complex(z):
    return bool(mp.isfinite(mp.re(z)) and mp.isfinite(mp.im(z)))


def s(x, n=18):
    if isinstance(x, complex): return [mp.nstr(x.real,n),mp.nstr(x.imag,n)]
    if hasattr(x,'imag') and not isinstance(x,(str,int,float)):
        try: return [mp.nstr(mp.re(x),n),mp.nstr(mp.im(x),n)]
        except Exception: pass
    return mp.nstr(x,n)


def single_leg_report():
    rows=[]
    for tl in (1,3):
        for tp in (-1,1):
            for branch in (-1,+1):
                vals=[tbranch(branch,1,tl,tp,b) for b in BETAS]
                rows.append({"two_l":tl,"two_p":tp,"branch":branch,
                             "slope":s(recent_slope(vals)),
                             "finite":all(finite_complex(v) for v in vals),
                             "magnitudes":[s(abs(v)) for v in vals]})
            vals=[dsum(1,tl,tp,b) for b in BETAS]
            rows.append({"two_l":tl,"two_p":tp,"branch":"sum",
                         "slope":s(recent_slope(vals)),"finite":all(finite_complex(v) for v in vals),
                         "magnitudes":[s(abs(v)) for v in vals]})
    return {"betas":[s(b) for b in BETAS],"rows":rows}


def uncontracted_report():
    rows=[]
    p0=allowed_p(1)[0]
    for tl in (1,3):
        for mask in range(16):
            vals=[radial_measure(b)*branch_product(mask,1,tl,p0,b) for b in BETAS]
            rows.append({"two_l":tl,"p":list(p0),"mask":mask,
                         "measure_product_slope":s(recent_slope(vals)),
                         "endpoint_integrable_by_power": bool(recent_slope(vals)>-1),
                         "finite":all(finite_complex(v) for v in vals)})
        vals=[radial_measure(b)*additive_product(1,tl,p0,b) for b in BETAS]
        rows.append({"two_l":tl,"p":list(p0),"mask":"additive",
                     "measure_product_slope":s(recent_slope(vals)),
                     "endpoint_integrable_by_power":bool(recent_slope(vals)>-1),
                     "finite":all(finite_complex(v) for v in vals)})
    return {"betas":[s(b) for b in BETAS],"rows":rows}


def precontracted_report():
    rows=[]
    for tl in (1,3):
        # small-spin intertwiner ranges: i=0,1 (two_i 0,2); k spans |l-l|..2l.
        for ti in (0,2):
            for tk in range(0,2*tl+1,2):
                for mask in range(16):
                    vals=[precontracted(mask,1,tl,ti,tk,b) for b in BETAS]
                    q=recent_slope(vals)
                    rows.append({"two_l":tl,"two_i":ti,"two_k":tk,"mask":mask,
                                 "slope":s(q),"endpoint_integrable_by_power":bool(q>-1),
                                 "finite":all(finite_complex(v) for v in vals),
                                 "magnitudes":[s(abs(v)) for v in vals]})
                vals=[precontracted(0,1,tl,ti,tk,b,additive=True) for b in BETAS]
                q=recent_slope(vals)
                rows.append({"two_l":tl,"two_i":ti,"two_k":tk,"mask":"additive",
                             "slope":s(q),"endpoint_integrable_by_power":bool(q>-1),
                             "finite":all(finite_complex(v) for v in vals),
                             "magnitudes":[s(abs(v)) for v in vals]})
    finite_branch=[r for r in rows if r["mask"]!="additive" and r["finite"]]
    integrable=[r for r in finite_branch if r["endpoint_integrable_by_power"]]
    return {"betas":[s(b) for b in BETAS],"branch_rows":len(finite_branch),
            "integrable_branch_rows":len(integrable),"rows":rows}


def cutoff_report():
    # Pure real-axis cutoff diagnostic. We deliberately do not call this an
    # i-epsilon prescription. Integrate only from beta_min to a finite beta=4.
    rows=[]
    tl=1
    for ti,tk in ((0,0),(2,2)):
        for mask in range(16):
            vals=[]
            for bmin in CUTOFFS:
                f=lambda b: precontracted(mask,1,tl,ti,tk,b)
                try:
                    val=mp.quad(f,[bmin,mp.mpf("0.5"),mp.mpf("1.5"),mp.mpf("4.0")])
                except Exception:
                    val=mp.mpc(mp.nan,mp.nan)
                vals.append(val)
            rows.append({"two_i":ti,"two_k":tk,"mask":mask,"finite":all(finite_complex(v) for v in vals),
                         "cutoff_values":[s(v) for v in vals],
                         "cutoff_magnitudes":[s(abs(v)) for v in vals]})
    return {"cutoffs":[s(x) for x in CUTOFFS],"beta_max":"4.0","rows":rows,
            "guardrail":"real-axis cutoff only; not equivalent to Feynman i-epsilon"}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["single-leg","uncontracted","precontracted","cutoff"],required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    fn={"single-leg":single_leg_report,"uncontracted":uncontracted_report,
        "precontracted":precontracted_report,"cutoff":cutoff_report}[args.mode]
    report=fn()
    report.update({"mode":args.mode,"gamma":"1.2","mp_dps":mp.mp.dps,
                   "interpretation_guardrail":"Endpoint/cutoff diagnostic only. A finite causal vertex requires the Feynman i-epsilon Toller prescription and vertex-level correlated kappa_ab=sigma_a sigma_b."})
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    summary={k:v for k,v in report.items() if k not in ("rows",)}
    if "rows" not in summary: pass
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
