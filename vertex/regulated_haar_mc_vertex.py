#!/usr/bin/env python3
"""Regulated Haar-matched Monte Carlo pilot for a direct causal vertex component.

We gauge-fix g1=1 and sample g2..g5 from a *truncated* polar decomposition
of SL(2,C),

    g = B(n,beta) h,
    beta in [0,R], n in S^2, h in SU(2),

with beta drawn from p(beta) proportional to sinh(beta)^2.  This matches the
radial dependence of the Lorentz Haar measure on the truncated domain.  The
cutoff R is an explicit regulator: this script does NOT call the result the
full non-compact vertex.

For speed the branch kernel uses the closed-form reduced Toller formula through
the repository's stable-hyp2f1 launcher. Iterations 016/017 independently
validated this evaluator against the residue/power-series representation to
~1e-61 on the relevant small-spin grid.

The pilot integrates one j=1/2 magnetic-basis component for either a fixed
causal class or the EPRL D-matrix control.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import (
    PAIRS, cartan_kak, spin_rep, midx, mpc, ordered_m, random_su2
)

mp.mp.dps = 60

SIGMAS = {
    'allplus': (1,1,1,1,1),
    'onefour': (1,-1,-1,-1,-1),
    'twothree': (1,1,-1,-1,-1),
}


def sfmt(x,n=20): return mp.nstr(x,n)
def cfmt(z,n=20): return [mp.nstr(mp.re(z),n),mp.nstr(mp.im(z),n)]


def radial_primitive(beta):
    # Integral_0^beta sinh(r)^2 dr
    b=float(beta)
    return 0.25*math.sinh(2*b)-0.5*b


def sample_beta(rng,R):
    target=float(rng.random())*radial_primitive(R)
    lo,hi=0.0,float(R)
    for _ in range(64):
        mid=0.5*(lo+hi)
        if radial_primitive(mid)<target: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)


def directional_boost(beta,n):
    nx,ny,nz=[float(x) for x in n]
    c=math.cosh(beta/2); s=math.sinh(beta/2)
    ns=np.array([[nz,nx-1j*ny],[nx+1j*ny,-nz]],dtype=complex)
    return c*np.eye(2,dtype=complex)+s*ns


def sample_group(rng,R):
    beta=sample_beta(rng,R)
    n=rng.normal(size=3); n=n/np.linalg.norm(n)
    h=random_su2(rng)
    return directional_boost(beta,n)@h,beta


def full_branch(branch,g,gamma,two_m,two_n):
    two_j=1
    U1,beta,U2,kerr,_,_=cartan_kak(g)
    D1=spin_rep(U1,two_j); D2=spin_rep(U2,two_j)
    rho=mp.mpf(str(gamma))/2
    total=mp.mpc(0)
    b=mp.mpf(str(beta))
    for two_p in (-1,1):
        if branch>0:
            t=ep.toller_plus(1,1,two_p,1,rho,b)
        else:
            t=ep.toller_minus(1,1,two_p,1,rho,b)
        total += mpc(D1[midx(1,two_m),midx(1,two_p)])*t*mpc(D2[midx(1,two_p),midx(1,two_n)])
    return total,beta,kerr


def edge_value(mode,sigma,a,b,rel,gamma):
    m_ab=ordered_m(a,b); m_ba=ordered_m(b,a)
    if mode=='eprl':
        tp,beta,kerr=full_branch(+1,rel,gamma,m_ba,m_ab)
        tm,_,_=full_branch(-1,rel,gamma,m_ba,m_ab)
        return tp+tm,beta,kerr
    k=sigma[a]*sigma[b]
    return full_branch(+1 if k>0 else -1,rel,gamma,m_ba,m_ab)


def integrand(mode,sigma,groups,gamma):
    z=mp.mpc(1); min_pair=1e300; max_pair=0.0; max_kerr=0.0
    for a,b in PAIRS:
        rel=np.linalg.inv(groups[b])@groups[a]
        v,beta,kerr=edge_value(mode,sigma,a,b,rel,gamma)
        z*=v; min_pair=min(min_pair,beta); max_pair=max(max_pair,beta); max_kerr=max(max_kerr,kerr)
    return z,min_pair,max_pair,max_kerr


def mean_complex(vals):
    return sum(vals,mp.mpc(0))/len(vals)


def stderr_component(vals,part):
    xs=[float(part(v)) for v in vals]
    if len(xs)<2:return float('nan')
    return float(np.std(xs,ddof=1)/math.sqrt(len(xs)))


def quantile(xs,q):
    return float(np.quantile(np.asarray(xs,dtype=float),q))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',default='1.2')
    ap.add_argument('--mode',choices=['allplus','onefour','twothree','eprl'],required=True)
    ap.add_argument('--cutoff',type=float,required=True)
    ap.add_argument('--samples',type=int,default=32)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma
    sigma=SIGMAS.get(args.mode)
    rng=np.random.default_rng(args.seed)

    vals=[]; min_pairs=[]; max_pairs=[]; kerrs=[]; group_betas=[]
    for _ in range(args.samples):
        groups=[np.eye(2,dtype=complex)]; bs=[]
        for _a in range(4):
            g,b=sample_group(rng,args.cutoff); groups.append(g); bs.append(b)
        v,mn,mx,ke=integrand(args.mode,sigma,groups,gamma)
        vals.append(v); min_pairs.append(mn); max_pairs.append(mx); kerrs.append(ke); group_betas.extend(bs)

    mu=mean_complex(vals)
    se_re=stderr_component(vals,lambda z: mp.re(z)); se_im=stderr_component(vals,lambda z: mp.im(z))
    mags=[float(abs(v)) for v in vals]
    # Omits the convention-dependent overall Haar constant and normalized angular
    # factors. This factor is sufficient for R-dependence of the regulated pilot.
    radial_volume=radial_primitive(args.cutoff)
    rel_volume4=radial_volume**4
    est=mu*rel_volume4
    out={
      'gamma':args.gamma,'mode':args.mode,'sigma':None if sigma is None else list(sigma),
      'cutoff_R':args.cutoff,'samples':args.samples,'seed':args.seed,
      'mean_integrand':cfmt(mu),'stderr_re':se_re,'stderr_im':se_im,
      'relative_haar_volume_factor_F_R_pow4':rel_volume4,
      'regulated_estimate_relative_normalization':cfmt(est),
      'mean_abs_integrand':float(np.mean(mags)),'median_abs_integrand':float(np.median(mags)),
      'q90_abs_integrand':quantile(mags,0.9),'max_abs_integrand':max(mags),
      'min_relative_pair_beta':min(min_pairs),'max_relative_pair_beta':max(max_pairs),
      'min_sampled_group_beta':min(group_betas),'max_sampled_group_beta':max(group_betas),
      'max_kak_reconstruction_error':max(kerrs),
      'finite_samples':sum(bool(mp.isfinite(mp.re(v)) and mp.isfinite(mp.im(v))) for v in vals),
      'verdict':'REGULATED_HAAR_MC_FINITE' if all(mp.isfinite(mp.re(v)) and mp.isfinite(mp.im(v)) for v in vals) else 'REGULATED_HAAR_MC_NONFINITE',
      'guardrail':('This is a finite-rapidity, finite-sample magnetic-basis pilot. R is an explicit noncompact-domain regulator; '
                   'the overall Haar normalization is suppressed; no convergence to the full causal vertex is claimed until '
                   'cutoff and sample-size stability are demonstrated and boundary intertwiners are contracted.')
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if out['verdict']!='REGULATED_HAAR_MC_FINITE': raise SystemExit(5)

if __name__=='__main__': main()
