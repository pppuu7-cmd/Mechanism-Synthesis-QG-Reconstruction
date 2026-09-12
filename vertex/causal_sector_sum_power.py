#!/usr/bin/env python3
"""Collision scaling of summed causal and co-causal sectors.

The 2026 causal-vertex construction permits a sum over edge orientations
sigma_a.  With global sigma reversal identified, there are 16 inequivalent
factorized wedge-sign structures kappa_ab=sigma_a sigma_b.  The co-causal
sector reverses every wedge sign, -kappa_ab.

Iteration 022 showed that fixed causal classes have multi-collision powers
near the naive product of beta^-2 Toller poles.  Iteration 021 showed the
leading single-edge residues satisfy C_- ~= -C_+.  This predicts a parity
pattern for a k-group cluster: the leading sign of a causal term is

    prod_{a<b<=k} kappa_ab = prod_a sigma_a^(k-1).

Hence the leading pole is expected to add coherently inside the causal sum for
odd k, while leading cancellation is possible for even k.  This script tests
that prediction directly on the full ten-wedge magnetic-basis carrier.

For efficiency each edge's T+ and T- is evaluated once.  From those 20 edge
values we construct:
  Cplus16  : sum over 16 inequivalent factorized causal structures,
  Cminus16 : the same structures with every wedge sign reversed,
  Cboth32  : Cplus16 + Cminus16,
  EPRL     : product over edges of (T+ + T-),
  fixed    : all-plus fixed causal structure control.

The factor of two from global sigma reversal is irrelevant for power counting
and is omitted.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.multicollision_power_counting import (
    RS, CLUSTERS, cluster_setup, groups_at_r, rapidity_diagnostics, fmt, finite, slope, classify_margin
)
from vertex.direct_causal_integrand_smoke import PAIRS
from vertex.regulated_haar_mc_vertex import full_branch
from vertex.direct_causal_integrand_smoke import ordered_m

mp.mp.dps = 75


def edge_branches(groups,gamma):
    vals={}
    maxerr=0.0
    for a,b in PAIRS:
        rel=np.linalg.inv(groups[b])@groups[a]
        m_ab=ordered_m(a,b); m_ba=ordered_m(b,a)
        tp,beta,ke=full_branch(+1,rel,gamma,m_ba,m_ab)
        tm,_,ke2=full_branch(-1,rel,gamma,m_ba,m_ab)
        vals[(a,b)]=(tp,tm,beta)
        maxerr=max(maxerr,ke,ke2)
    return vals,maxerr


def term_for_sigma(edgevals,sigma,co=False):
    z=mp.mpc(1)
    for a,b in PAIRS:
        k=sigma[a]*sigma[b]
        if co: k=-k
        tp,tm,_=edgevals[(a,b)]
        z*=tp if k>0 else tm
    return z


def sector_values(edgevals):
    sigmas=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
    cp=mp.mpc(0); cm=mp.mpc(0)
    for s in sigmas:
        cp += term_for_sigma(edgevals,s,False)
        cm += term_for_sigma(edgevals,s,True)
    eprl=mp.mpc(1)
    fixed=mp.mpc(1)
    for a,b in PAIRS:
        tp,tm,_=edgevals[(a,b)]
        eprl*=tp+tm
        fixed*=tp
    return {'Cplus16':cp,'Cminus16':cm,'Cboth32':cp+cm,'EPRL':eprl,'fixed_allplus':fixed}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma

    rows=[]
    for k in CLUSTERS:
        bg,dirs,hs=cluster_setup(args.seed,k)
        d=3*(k-1)
        series={m:[] for m in ('Cplus16','Cminus16','Cboth32','EPRL','fixed_allplus')}
        mins=[]; maxs=[]; kerrs=[]
        for r in RS:
            groups=groups_at_r(bg,dirs,hs,k,r)
            mn,mx,_,ke0=rapidity_diagnostics(groups,k)
            ev,ke1=edge_branches(groups,gamma)
            sv=sector_values(ev)
            for m,v in sv.items(): series[m].append(v)
            mins.append(mn); maxs.append(mx); kerrs.append(max(ke0,ke1))
        for mode,vals in series.items():
            q=slope(RS,vals)
            m1=q+d if mp.isfinite(q) else mp.nan
            m2=q+mp.mpf(d)/2 if mp.isfinite(q) else mp.nan
            rows.append({
                'cluster_k':k,'mode':mode,'local_boost_dimension_d':d,
                'measured_slope':fmt(q),
                'first_moment_margin_q_plus_d':fmt(m1),
                'first_moment_class':classify_margin(m1),
                'second_moment_margin_q_plus_d_over_2':fmt(m2),
                'second_moment_class':classify_margin(m2),
                'magnitudes':[fmt(abs(v)) for v in vals],
                'min_intra_betas':[fmt(x) for x in mins],
                'max_intra_betas':[fmt(x) for x in maxs],
                'max_kak_reconstruction_error':max(kerrs),
            })

    summary={}
    for k in CLUSTERS:
        summary[str(k)]={}
        for mode in ('Cplus16','Cminus16','Cboth32','EPRL','fixed_allplus'):
            r=next(x for x in rows if x['cluster_k']==k and x['mode']==mode)
            summary[str(k)][mode]={
                'slope':r['measured_slope'],
                'first_moment_class':r['first_moment_class'],
                'second_moment_class':r['second_moment_class'],
            }

    out={
        'gamma':args.gamma,'seed':args.seed,'r_values':[fmt(x) for x in RS],
        'summary':summary,'rows':rows,
        'verdict':'CAUSAL_SECTOR_SUM_POWER_SCAN_COMPLETE',
        'guardrail':(
            'Power counting of the 16 inequivalent sigma-factorized sector sum and its co-causal partner on generic cluster rays. '
            'The omitted global-sigma duplication is a constant factor. This does not replace the exact distributional i-epsilon '
            'integration or boundary-intertwiner contraction.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__':
    main()
