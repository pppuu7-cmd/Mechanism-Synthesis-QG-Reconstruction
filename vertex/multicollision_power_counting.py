#!/usr/bin/env python3
"""Multi-collision power counting for the direct causal ten-wedge carrier.

Iteration 020 established a generic single relative-pair singularity
|I| ~ beta_ab^-2.  A single collision surface has codimension three and is
locally first-moment integrable.  Intersections of several such surfaces are a
separate question because the pair distances are correlated.

Here k group variables (including the gauge-fixed g1=1) are placed in a common
boost cluster.  For i=2..k,

    g_i(r) = B(r n_i) h_i,

with fixed generic n_i and independent SU(2) h_i.  At r -> 0 every relative
element inside the cluster tends to SU(2), so all k(k-1)/2 intra-cluster Cartan
rapidities vanish together as O(r).  Non-cluster groups remain generic and
separated.

The independent local boost dimension of a k-cluster is d = 3(k-1).  If the
direct integrand scales as |I| ~ r^q, radial absolute integrability requires
q > -d, while a finite ordinary-Monte-Carlo second moment requires q > -d/2.
The naive independent-edge prediction is q_naive = -k(k-1), making k=3 the
logarithmic first-moment boundary.  The computation below tests the actual
full Cartan-reconstructed causal integrand rather than assuming that product
power.

This remains local power counting along generic cluster rays.  It does not by
itself prove global (non)finiteness, because angular cancellations,
distributional i-epsilon structure, and exceptional lower-dimensional rays may
modify an integrated result.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.collision_power_counting import unit_vector
from vertex.direct_causal_integrand_smoke import make_groups, random_su2, PAIRS, cartan_kak
from vertex.regulated_haar_mc_vertex import SIGMAS, directional_boost, integrand

mp.mp.dps = 70
RS = [mp.mpf(x) for x in ('0.20','0.10','0.05','0.025','0.0125','0.00625','0.003125')]
MODES = ('allplus','onefour','twothree','eprl')
CLUSTERS = (2,3,4,5)


def fmt(x,n=22):
    return mp.nstr(x,n)


def finite(z):
    return bool(mp.isfinite(mp.re(z)) and mp.isfinite(mp.im(z)))


def slope(xs,ys):
    pts=[(mp.log(x),mp.log(abs(y))) for x,y in zip(xs,ys) if finite(y) and abs(y)>mp.mpf('1e-90')]
    if len(pts)<4:
        return mp.nan
    pts=pts[-4:]
    xb=sum(x for x,_ in pts)/len(pts)
    yb=sum(y for _,y in pts)/len(pts)
    den=sum((x-xb)**2 for x,_ in pts)
    return sum((x-xb)*(y-yb) for x,y in pts)/den


def classify_margin(margin,tol=mp.mpf('0.15')):
    if not mp.isfinite(margin):
        return 'UNRESOLVED'
    if margin > tol:
        return 'PASS'
    if margin < -tol:
        return 'FAIL'
    return 'BORDERLINE_LOG'


def cluster_setup(seed,k):
    # Background has all relative beta separated from zero.  It supplies only
    # non-cluster groups; clustered groups are overwritten below.
    bg,_,_,_,_=make_groups(seed+30000+k,min_pair_beta=0.80)
    rng=np.random.default_rng(seed+1000*k)
    dirs={i:unit_vector(rng) for i in range(1,k)}
    hs={i:random_su2(rng) for i in range(1,k)}
    return bg,dirs,hs


def groups_at_r(bg,dirs,hs,k,r):
    gs=[g.copy() for g in bg]
    gs[0]=np.eye(2,dtype=complex)
    for i in range(1,k):
        gs[i]=directional_boost(float(r),dirs[i])@hs[i]
    return gs


def rapidity_diagnostics(gs,k):
    intra=[]; cross=[]; maxerr=0.0
    for a,b in PAIRS:
        rel=np.linalg.inv(gs[b])@gs[a]
        _,beta,_,err,_,_=cartan_kak(rel)
        maxerr=max(maxerr,err)
        if a<k and b<k:
            intra.append(beta)
        else:
            cross.append(beta)
    return min(intra),max(intra), (min(cross) if cross else None), maxerr


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma); ep.GAMMA=gamma

    rows=[]
    for k in CLUSTERS:
        bg,dirs,hs=cluster_setup(args.seed,k)
        d=3*(k-1)
        naive=-k*(k-1)
        for mode in MODES:
            sigma=SIGMAS.get(mode)
            vals=[]; mins=[]; maxs=[]; crossmins=[]; kerrs=[]
            for r in RS:
                gs=groups_at_r(bg,dirs,hs,k,r)
                mn,mx,cmn,ke0=rapidity_diagnostics(gs,k)
                v,_,_,ke1=integrand(mode,sigma,gs,gamma)
                vals.append(v); mins.append(mn); maxs.append(mx)
                crossmins.append(cmn); kerrs.append(max(ke0,ke1))
            q=slope(RS,vals)
            first_margin=q+d if mp.isfinite(q) else mp.nan
            second_margin=q+mp.mpf(d)/2 if mp.isfinite(q) else mp.nan
            rows.append({
                'cluster_k':k,'local_boost_dimension_d':d,'mode':mode,
                'intra_cluster_edges':k*(k-1)//2,
                'naive_independent_edge_slope':naive,
                'measured_slope':fmt(q),
                'delta_from_naive':fmt(q-naive) if mp.isfinite(q) else 'nan',
                'first_moment_margin_q_plus_d':fmt(first_margin),
                'first_moment_class':classify_margin(first_margin),
                'second_moment_margin_q_plus_d_over_2':fmt(second_margin),
                'second_moment_class':classify_margin(second_margin),
                'magnitudes':[fmt(abs(v)) for v in vals],
                'min_intra_betas':[fmt(x) for x in mins],
                'max_intra_betas':[fmt(x) for x in maxs],
                'min_cross_betas':[None if x is None else fmt(x) for x in crossmins],
                'max_kak_reconstruction_error':max(kerrs),
            })

    causal=[r for r in rows if r['mode']!='eprl']
    by_k={}
    for k in CLUSTERS:
        rr=[r for r in causal if r['cluster_k']==k]
        by_k[str(k)]={
            'rows':len(rr),
            'slope_range':[min(float(r['measured_slope']) for r in rr),max(float(r['measured_slope']) for r in rr)],
            'first_moment_classes':{c:sum(r['first_moment_class']==c for r in rr) for c in ('PASS','BORDERLINE_LOG','FAIL')},
            'second_moment_classes':{c:sum(r['second_moment_class']==c for r in rr) for c in ('PASS','BORDERLINE_LOG','FAIL')},
        }

    out={
        'gamma':args.gamma,'seed':args.seed,'r_values':[fmt(x) for x in RS],
        'cluster_summary':by_k,'rows':rows,
        'verdict':'MULTICOLLISION_POWER_SCAN_COMPLETE',
        'guardrail':(
            'Generic common-scale cluster rays only. A FAIL/BORDERLINE absolute-power result flags a real finiteness '
            'problem to analyze with the exact i-epsilon/distributional amplitude, but is not alone a proof of divergence; '
            'conversely a PASS along these rays is not a global proof because other collision geometries may exist.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__':
    main()
