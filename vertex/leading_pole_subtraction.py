#!/usr/bin/env python3
"""Leading beta^-2 pole extraction and subtraction diagnostic.

Iteration 020 found |T^+/-| and a generic one-pair causal ten-wedge integrand
scaling as beta^-2.  Under the local Haar factor beta^2 d beta this gives a
finite first moment but an infinite ordinary-IID second moment.

This script asks the next numerical question: is the leading collision
singularity sufficiently universal that subtracting C/beta^2 leaves a local
remainder with power q > -3/2, i.e. finite second moment under Haar measure?

For each full Cartan-reconstructed j=1/2 magnetic component we fit

    beta^2 T^s(beta) = C_s + a_s beta + b_s beta^2 + ...

from the three smallest beta values.  We then test

    R_s(beta) = T^s(beta) - C_s/beta^2.

The same operation is repeated directly on the ten-wedge integrand along the
gauge-pair and internal-pair collision paths used in Iteration 020.  This is a
local subtraction diagnostic only; it is not yet a globally unbiased vertex
estimator because overlapping collision strata require inclusion-exclusion or
a partition of unity.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.collision_power_counting import (
    collision_groups_fixed, collision_groups_internal, unit_vector
)
from vertex.direct_causal_integrand_smoke import random_su2
from vertex.regulated_haar_mc_vertex import SIGMAS, directional_boost, full_branch, integrand

mp.mp.dps = 80
BETAS = [mp.mpf(x) for x in ('0.10','0.05','0.025','0.0125','0.00625','0.003125')]
CAUSAL_MODES = ('allplus','onefour','twothree')


def fmt(x,n=24):
    return mp.nstr(x,n)


def cfmt(z,n=24):
    return [fmt(mp.re(z),n),fmt(mp.im(z),n)]


def finite(z):
    return bool(mp.isfinite(mp.re(z)) and mp.isfinite(mp.im(z)))


def slope(xs,ys):
    pts=[(mp.log(x),mp.log(abs(y))) for x,y in zip(xs,ys) if finite(y) and abs(y)>mp.mpf('1e-70')]
    if len(pts)<3:
        return mp.nan
    pts=pts[-4:]
    xb=sum(x for x,_ in pts)/len(pts)
    yb=sum(y for _,y in pts)/len(pts)
    den=sum((x-xb)**2 for x,_ in pts)
    return sum((x-xb)*(y-yb) for x,y in pts)/den


def fit_leading_coefficient(betas,vals):
    """Fit beta^2 F = C + a beta + b beta^2 on the three smallest betas."""
    xs=betas[-3:]
    ys=[(b*b)*v for b,v in zip(betas[-3:],vals[-3:])]
    M=mp.matrix([[1,x,x*x] for x in xs])
    y=mp.matrix(ys)
    sol=mp.lu_solve(M,y)
    return sol[0],sol[1],sol[2]


def remainder_class(q):
    if not mp.isfinite(q):
        return {'slope':'nan','second_moment_finite_after_subtraction':False}
    return {
        'slope':fmt(q),
        'haar_second_moment_power':fmt(2+2*q),
        'second_moment_finite_after_subtraction':bool(q>mp.mpf('-1.5')),
    }


def edge_rows(gamma,seed):
    rng=np.random.default_rng(seed)
    n=unit_vector(rng)
    h=random_su2(rng)
    rows=[]
    for two_m in (-1,1):
        for two_n in (-1,1):
            vals={'+':[],'-':[]}
            for beta in BETAS:
                g=directional_boost(float(beta),n)@h
                tp,_,_=full_branch(+1,g,gamma,two_m,two_n)
                tm,_,_=full_branch(-1,g,gamma,two_m,two_n)
                vals['+'].append(tp)
                vals['-'].append(tm)
            fitted={}
            for branch in ('+','-'):
                C,a,b=fit_leading_coefficient(BETAS,vals[branch])
                rem=[v-C/(x*x) for x,v in zip(BETAS,vals[branch])]
                q=slope(BETAS,rem)
                fitted[branch]={'C':C,'a':a,'b':b,'remainder':rem,'q':q}
                rows.append({
                    'two_m':two_m,'two_n':two_n,'branch':branch,
                    'C':cfmt(C),'a':cfmt(a),'b':cfmt(b),
                    'raw_slope':fmt(slope(BETAS,vals[branch])),
                    **remainder_class(q),
                    'raw_magnitudes':[fmt(abs(z)) for z in vals[branch]],
                    'remainder_magnitudes':[fmt(abs(z)) for z in rem],
                })
            Cp=fitted['+']['C']; Cm=fitted['-']['C']
            denom=max(abs(Cp),abs(Cm),mp.mpf('1e-80'))
            cancellation=abs(Cp+Cm)/denom
            for row in rows[-2:]:
                row['leading_pole_plus_minus_cancellation_relative']=fmt(cancellation)
    return rows


def vertex_rows(gamma,seed):
    rows=[]
    for collision,fn in (
        ('gauge_pair_1_2',collision_groups_fixed),
        ('internal_pair_2_3',collision_groups_internal),
    ):
        for mode in CAUSAL_MODES:
            vals=[]
            sigma=SIGMAS[mode]
            for beta in BETAS:
                groups=fn(seed,beta)
                v,_,_,_=integrand(mode,sigma,groups,gamma)
                vals.append(v)
            C,a,b=fit_leading_coefficient(BETAS,vals)
            rem=[v-C/(x*x) for x,v in zip(BETAS,vals)]
            q=slope(BETAS,rem)
            rows.append({
                'collision':collision,'mode':mode,
                'C':cfmt(C),'a':cfmt(a),'b':cfmt(b),
                'raw_slope':fmt(slope(BETAS,vals)),
                **remainder_class(q),
                'raw_magnitudes':[fmt(abs(z)) for z in vals],
                'remainder_magnitudes':[fmt(abs(z)) for z in rem],
            })
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma)
    ep.GAMMA=gamma

    edges=edge_rows(gamma,args.seed)
    verts=vertex_rows(gamma,args.seed)
    edge_pass=sum(r['second_moment_finite_after_subtraction'] for r in edges)
    vert_pass=sum(r['second_moment_finite_after_subtraction'] for r in verts)
    cancels=[mp.mpf(r['leading_pole_plus_minus_cancellation_relative']) for r in edges]
    rem_edge=[float(r['slope']) for r in edges if r['slope']!='nan']
    rem_vert=[float(r['slope']) for r in verts if r['slope']!='nan']

    verdict=(
        'LEADING_POLE_SUBTRACTION_VARIANCE_CURE_LOCAL_PASS'
        if edge_pass==len(edges) and vert_pass==len(verts)
        else 'LEADING_POLE_SUBTRACTION_PARTIAL_OR_FAIL_OPEN'
    )
    out={
        'gamma':args.gamma,'seed':args.seed,'betas':[fmt(x) for x in BETAS],
        'edge_rows':len(edges),'edge_finite_variance_after_subtraction':edge_pass,
        'vertex_rows':len(verts),'vertex_finite_variance_after_subtraction':vert_pass,
        'max_leading_pole_plus_minus_cancellation_relative':fmt(max(cancels)),
        'edge_remainder_slope_range':[min(rem_edge),max(rem_edge)] if rem_edge else None,
        'vertex_remainder_slope_range':[min(rem_vert),max(rem_vert)] if rem_vert else None,
        'edge_details':edges,'vertex_details':verts,
        'verdict':verdict,
        'guardrail':(
            'Local single-collision subtraction only. C is fitted along a chosen approach to one collision stratum. '
            'This does not yet define a globally unbiased estimator on overlapping pair-collision strata, prove full vertex '
            'finiteness, or replace the distributional/Feynman prescription of the causal amplitude.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('edge_details','vertex_details')},indent=2))

if __name__=='__main__':
    main()
