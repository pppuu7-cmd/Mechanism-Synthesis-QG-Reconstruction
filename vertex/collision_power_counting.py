#!/usr/bin/env python3
"""Local beta_ab -> 0 power counting for the direct causal carrier.

The regulated IID Haar pilot developed enormous heavy tails.  This script tests
whether they are explained by the zero-boost stratum of a *relative* Lorentz
element.  It uses the full Cartan-reconstructed T(g), not an isolated reduced
boost function and not B4 factorization.

Two diagnostics are run:

1. General full-T edge approach to the SU(2) stratum
       g(beta) = B(n,beta) h, beta -> 0,
   for every j=l=1/2 magnetic component and both Toller branches.

2. Ten-wedge direct integrand collision, both for a gauge-fixed pair (g1,g2)
   and an internal pair (g2,g3), with the remaining group elements generic.

If |F| ~ beta^q, Haar radial measure is locally beta^2 d beta.  Therefore
absolute first-moment power is 2+q (integrable if q>-3) and second-moment
power is 2+2q (finite ordinary-MC variance if q>-3/2).

Power counting is diagnostic only: failure of absolute/variance criteria does
not by itself decide distributional/Feynman-i-epsilon finiteness of the causal
vertex.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import make_groups, random_su2
from vertex.regulated_haar_mc_vertex import (
    SIGMAS, directional_boost, full_branch, integrand
)

mp.mp.dps = 70
BETAS = [mp.mpf(x) for x in ('0.20','0.10','0.05','0.02','0.01','0.005','0.002')]
MODES = ('allplus','onefour','twothree','eprl')


def fmt(x,n=20): return mp.nstr(x,n)

def finite(z): return bool(mp.isfinite(mp.re(z)) and mp.isfinite(mp.im(z)))

def slope(xs,ys):
    pts=[(mp.log(x),mp.log(abs(y))) for x,y in zip(xs,ys) if finite(y) and abs(y)>0]
    if len(pts)<3: return mp.nan
    pts=pts[-4:]
    xb=sum(x for x,_ in pts)/len(pts); yb=sum(y for _,y in pts)/len(pts)
    den=sum((x-xb)**2 for x,_ in pts)
    return sum((x-xb)*(y-yb) for x,y in pts)/den


def classify(q):
    if not mp.isfinite(q):
        return {'slope':'nan','pole_power':'nan','first_moment_integrable':False,
                'second_moment_finite':False}
    return {
      'slope':fmt(q),'pole_power':fmt(-q),
      'haar_first_moment_power':fmt(2+q),
      'haar_second_moment_power':fmt(2+2*q),
      'first_moment_integrable':bool(q>-3),
      'second_moment_finite':bool(q>mp.mpf('-1.5')),
    }


def unit_vector(rng):
    x=rng.normal(size=3); return x/np.linalg.norm(x)


def edge_scan(gamma,seed):
    rng=np.random.default_rng(seed)
    n=unit_vector(rng); h=random_su2(rng)
    rows=[]
    for tm in (-1,1):
      for tn in (-1,1):
        vals={'+':[],'-':[],'sum':[]}
        for beta in BETAS:
            g=directional_boost(float(beta),n)@h
            tp,_,_=full_branch(+1,g,gamma,tm,tn)
            tmn,_,_=full_branch(-1,g,gamma,tm,tn)
            vals['+'].append(tp); vals['-'].append(tmn); vals['sum'].append(tp+tmn)
        for branch in ('+','-','sum'):
            q=slope(BETAS,vals[branch]); c=classify(q)
            rows.append({'two_m':tm,'two_n':tn,'branch':branch,**c,
                         'magnitudes':[fmt(abs(z)) for z in vals[branch]]})
    return rows


def collision_groups_fixed(seed,beta):
    # Generic background is kept away from the zero-boost strata before the
    # deliberate collision is introduced.
    bg,_,_,_,_=make_groups(seed+10000,min_pair_beta=0.45)
    rng=np.random.default_rng(seed+77)
    h=random_su2(rng); n=unit_vector(rng)
    gs=[g.copy() for g in bg]
    gs[1]=directional_boost(float(beta),n)@h
    return gs


def collision_groups_internal(seed,beta):
    bg,_,_,_,_=make_groups(seed+20000,min_pair_beta=0.45)
    rng=np.random.default_rng(seed+177)
    h=random_su2(rng); n=unit_vector(rng)
    gs=[g.copy() for g in bg]
    rel=directional_boost(float(beta),n)@h
    gs[2]=gs[1]@rel
    return gs


def integrand_scan(gamma,seed):
    rows=[]
    for collision,fn in (('gauge_pair_1_2',collision_groups_fixed),
                         ('internal_pair_2_3',collision_groups_internal)):
      for mode in MODES:
        sigma=SIGMAS.get(mode)
        vals=[]; target_betas=[]; min_all=[]
        for beta in BETAS:
            gs=fn(seed,beta)
            v,mn,mx,ke=integrand(mode,sigma,gs,gamma)
            vals.append(v); min_all.append(mn)
            # By construction one relative Cartan boost tends to zero with beta.
            target_betas.append(beta)
        q=slope(target_betas,vals); c=classify(q)
        rows.append({'collision':collision,'mode':mode,**c,
                     'magnitudes':[fmt(abs(z)) for z in vals],
                     'min_pair_betas':[fmt(x) for x in min_all]})
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma

    edges=edge_scan(gamma,args.seed)
    vertex=integrand_scan(gamma,args.seed)
    causal_edges=[r for r in edges if r['branch'] in ('+','-')]
    causal_vertex=[r for r in vertex if r['mode']!='eprl']

    edge_first=sum(r['first_moment_integrable'] for r in causal_edges)
    edge_second=sum(r['second_moment_finite'] for r in causal_edges)
    vert_first=sum(r['first_moment_integrable'] for r in causal_vertex)
    vert_second=sum(r['second_moment_finite'] for r in causal_vertex)

    slopes_edge=[float(r['slope']) for r in causal_edges]
    slopes_vertex=[float(r['slope']) for r in causal_vertex]
    out={
      'gamma':args.gamma,'seed':args.seed,'betas':[fmt(x) for x in BETAS],
      'edge_branch_rows':len(causal_edges),'edge_first_moment_integrable_rows':edge_first,
      'edge_second_moment_finite_rows':edge_second,
      'edge_slope_range':[min(slopes_edge),max(slopes_edge)],
      'vertex_causal_rows':len(causal_vertex),'vertex_first_moment_integrable_rows':vert_first,
      'vertex_second_moment_finite_rows':vert_second,
      'vertex_slope_range':[min(slopes_vertex),max(slopes_vertex)],
      'edge_rows':edges,'vertex_rows':vertex,
      'verdict':('FINITE_MEAN_INFINITE_VARIANCE_SIGNATURE'
                 if edge_first==len(causal_edges) and edge_second==0
                    and vert_first==len(causal_vertex) and vert_second==0
                 else 'COLLISION_SCALING_MIXED_REVIEW_REQUIRED'),
      'guardrail':('Local one-stratum power counting only. It classifies absolute first/second-moment behavior along '
                   'generic beta_ab->0 approaches; it does not prove or disprove the full distributional causal vertex, '
                   'multi-collision intersections, or the Feynman i-epsilon prescription.')
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('edge_rows','vertex_rows')},indent=2))

if __name__=='__main__': main()
