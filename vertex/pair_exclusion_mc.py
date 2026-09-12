#!/usr/bin/env python3
"""Nested pair-exclusion Monte Carlo for the regulated direct vertex.

Use common random numbers to estimate the same truncated-Haar integral with
nested exclusions

    min_{a<b} beta_ab > epsilon.

The proposal is the same finite-R Haar-matched sampler as Iteration 019.  A
sample failing a given exclusion contributes zero, so the sample mean estimates
the integral over the allowed subdomain without a conditional-normalization
bias.  Using the same samples for every epsilon makes differences between
nested cutoffs much less noisy and directly exposes the contribution of each
collision shell.

This remains a finite-R regulated magnetic-basis pilot.  It does not implement
the full distributional i-epsilon prescription or boundary intertwiners.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import PAIRS, cartan_kak
from vertex.regulated_haar_mc_vertex import SIGMAS, sample_group, integrand, radial_primitive

mp.mp.dps = 60
EPSILONS = [0.20,0.10,0.05,0.025]


def cfmt(z,n=18): return [mp.nstr(mp.re(z),n),mp.nstr(mp.im(z),n)]

def cmean(vals): return sum(vals,mp.mpc(0))/len(vals)

def cstderr(vals):
    re=np.asarray([float(mp.re(z)) for z in vals]); im=np.asarray([float(mp.im(z)) for z in vals])
    if len(vals)<2:return float('nan'),float('nan')
    return float(np.std(re,ddof=1)/math.sqrt(len(vals))),float(np.std(im,ddof=1)/math.sqrt(len(vals)))


def relative_betas(groups):
    bs=[]; maxerr=0.0
    for a,b in PAIRS:
        rel=np.linalg.inv(groups[b])@groups[a]
        _,beta,_,err,_,_=cartan_kak(rel)
        bs.append(beta); maxerr=max(maxerr,err)
    return bs,maxerr


def stats(vals,vol4):
    mu=cmean(vals); sr,si=cstderr(vals)
    mags=np.asarray([float(abs(z)) for z in vals])
    return {'mean':cfmt(mu),'estimate_relative_norm':cfmt(mu*vol4),
            'stderr_re':sr,'stderr_im':si,
            'stderr_estimate_re':sr*vol4,'stderr_estimate_im':si*vol4,
            'mean_abs':float(mags.mean()),'median_abs':float(np.median(mags)),
            'q90_abs':float(np.quantile(mags,0.9)),'max_abs':float(mags.max())}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',default='1.2')
    ap.add_argument('--mode',choices=['allplus','onefour','twothree','eprl'],required=True)
    ap.add_argument('--cutoff',type=float,default=1.0)
    ap.add_argument('--samples',type=int,default=512)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma
    sigma=SIGMAS.get(args.mode); rng=np.random.default_rng(args.seed)
    vol4=radial_primitive(args.cutoff)**4

    # Each threshold receives N entries, zeros included for excluded samples.
    nested={eps:[] for eps in EPSILONS}
    shells={(EPSILONS[i],EPSILONS[i+1]):[] for i in range(len(EPSILONS)-1)}
    accept={eps:0 for eps in EPSILONS}; finite=0; min_seen=1e300; max_kerr=0.0

    for _ in range(args.samples):
        groups=[np.eye(2,dtype=complex)]
        for _a in range(4):
            g,_b=sample_group(rng,args.cutoff); groups.append(g)
        bs,ke=relative_betas(groups); bmin=min(bs); min_seen=min(min_seen,bmin); max_kerr=max(max_kerr,ke)

        # Only compute the expensive causal integrand if the point contributes to
        # the least restrictive epsilon.  Otherwise all nested estimators get 0.
        if bmin>min(EPSILONS):
            v,_,_,ke2=integrand(args.mode,sigma,groups,gamma); max_kerr=max(max_kerr,ke2)
            finite += int(mp.isfinite(mp.re(v)) and mp.isfinite(mp.im(v)))
        else:
            v=mp.mpc(0)

        for eps in EPSILONS:
            if bmin>eps:
                nested[eps].append(v); accept[eps]+=1
            else:nested[eps].append(mp.mpc(0))
        for hi,lo in shells:
            shells[(hi,lo)].append(v if (bmin>lo and bmin<=hi) else mp.mpc(0))

    nested_out={}
    for eps in EPSILONS:
        nested_out[str(eps)]={'acceptance':accept[eps]/args.samples,'accepted':accept[eps],
                              **stats(nested[eps],vol4)}
    shell_out={}
    for (hi,lo),vals in shells.items():
        shell_out[f'{lo}<min_beta<={hi}']=stats(vals,vol4)

    out={'gamma':args.gamma,'mode':args.mode,'cutoff_R':args.cutoff,'samples':args.samples,'seed':args.seed,
         'epsilons':EPSILONS,'relative_haar_volume_factor_F_R_pow4':vol4,
         'minimum_pair_beta_seen':min_seen,'max_kak_reconstruction_error':max_kerr,
         'finite_computed_samples':finite,'nested':nested_out,'shells':shell_out,
         'verdict':'PAIR_EXCLUSION_SCAN_COMPLETE',
         'guardrail':('Nested finite-epsilon estimates use common random numbers and include rejected proposals as zero. '
                      'A stable/linear epsilon->0 trend would support a finite first moment, but only a dedicated extrapolation '
                      'with controlled errors can be used as a vertex estimate. Overall Haar normalization is suppressed.')}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('nested','shells')},indent=2))

if __name__=='__main__':main()
