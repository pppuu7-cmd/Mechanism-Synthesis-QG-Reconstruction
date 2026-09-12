#!/usr/bin/env python3
"""Iteration 026: angular/antipodal cancellation of multi-collision residues.

Iterations 022-024 established radial causal powers close to the product of
beta^-2 Toller poles, even after causal-sector sums and gauge-invariant
boundary-intertwiner contraction.  Radial absolute power counting does not,
however, exclude a conditionally convergent principal-value integral if the
leading homogeneous coefficient has zero angular mean.

For a k-group collision the independent boost tangent space has dimension
  d = 3(k-1).
We sample a unit vector Omega uniformly on S^(d-1), split it into the local
boost vectors of groups 2..k, and compare the boundary-contracted leading
coefficients on antipodal directions +Omega and -Omega.

For the naive pole p=k(k-1),
  C_r(Omega) = r^p I(r,Omega).
We evaluate r and r/2, reject directions too close to nested sub-collision
strata, and report
  antipodal_ratio = |C(Omega)+C(-Omega)|/(|C(Omega)|+|C(-Omega)|).
A parity/principal-value cancellation would drive this ratio to zero.  An O(1)
ratio rules out simple antipodal cancellation on generic angular sectors.

The test uses the full j=1/2 K5 boundary-intertwiner contraction and the
Cboth32 causal+co-causal sector sum.  It is not a proof about all possible
angular cancellations or the exact i-epsilon distributional integral.
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
from vertex.multicollision_power_counting import rapidity_diagnostics, fmt
from vertex.regulated_haar_mc_vertex import directional_boost
from vertex.boundary_intertwiner_collision_power import (
    BOUNDARY_STATES, edge_branch_matrices, contracted_modes
)

mp.mp.dps = 60
KS=(3,4,5)
R0=mp.mpf('0.00625')
ANGULAR_MIN=0.10
SAMPLES=24


def groups_from_omega(bg,hs,k,r,omega):
    gs=[g.copy() for g in bg]
    gs[0]=np.eye(2,dtype=complex)
    for i in range(1,k):
        v=np.asarray(omega[3*(i-1):3*i],dtype=float)
        nv=float(np.linalg.norm(v))
        if nv<1e-14:
            n=np.array([1.0,0.0,0.0]); beta=0.0
        else:
            n=v/nv; beta=float(r)*nv
        gs[i]=directional_boost(beta,n)@hs[i]
    return gs


def coeff_for(groups,gamma,bstate,k,r):
    ev,_=edge_branch_matrices(groups,gamma)
    val=contracted_modes(ev,bstate)['Cboth32']
    p=k*(k-1)
    return complex(val)*(float(r)**p)


def rel_homog(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def mean_complex(vals):
    return sum(vals,0j)/len(vals)


def rms(vals):
    return math.sqrt(sum(abs(z)**2 for z in vals)/len(vals))


def quant(xs,q): return float(np.quantile(np.asarray(xs,dtype=float),q))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma
    rng=np.random.default_rng(args.seed)
    rows=[]

    for k in KS:
        bg,_,_,_,_=make_groups(args.seed+70000+k,min_pair_beta=0.80)
        hs={i:random_su2(rng) for i in range(1,k)}
        accepted=[]; attempts=0
        while len(accepted)<SAMPLES and attempts<2000:
            attempts+=1
            w=rng.normal(size=3*(k-1)); w=w/np.linalg.norm(w)
            gp=groups_from_omega(bg,hs,k,R0,w)
            gm=groups_from_omega(bg,hs,k,R0,-w)
            mnp,_,_,_=rapidity_diagnostics(gp,k)
            mnm,_,_,_=rapidity_diagnostics(gm,k)
            # Stay in a generic angular sector, away from nested collisions.
            if min(mnp,mnm)/float(R0) < ANGULAR_MIN:
                continue
            accepted.append(w)
        if len(accepted)<SAMPLES:
            raise RuntimeError(f'could not sample enough generic angular directions for k={k}')

        for bname in ('i00000','i22222','i02020','i20202'):
            bstate=BOUNDARY_STATES[bname]
            cplus=[]; cminus=[]; ratios=[]; hom=[]
            for w in accepted:
                gp=groups_from_omega(bg,hs,k,R0,w)
                gm=groups_from_omega(bg,hs,k,R0,-w)
                gp2=groups_from_omega(bg,hs,k,R0/2,w)
                gm2=groups_from_omega(bg,hs,k,R0/2,-w)
                cp=coeff_for(gp,gamma,bstate,k,R0)
                cm=coeff_for(gm,gamma,bstate,k,R0)
                cp2=coeff_for(gp2,gamma,bstate,k,R0/2)
                cm2=coeff_for(gm2,gamma,bstate,k,R0/2)
                cplus.append(cp2); cminus.append(cm2)
                ratios.append(abs(cp2+cm2)/max(abs(cp2)+abs(cm2),1e-300))
                hom.extend([rel_homog(cp,cp2),rel_homog(cm,cm2)])

            both=[z for pair in zip(cplus,cminus) for z in pair]
            m=mean_complex(both); rr=rms(both)
            rows.append({
                'cluster_k':k,'boundary_state':bname,'samples':SAMPLES,
                'antipodal_ratio_median':quant(ratios,0.5),
                'antipodal_ratio_q10':quant(ratios,0.1),
                'antipodal_ratio_q90':quant(ratios,0.9),
                'antipodal_ratio_min':min(ratios),'antipodal_ratio_max':max(ratios),
                'angular_mean_over_rms':abs(m)/max(rr,1e-300),
                'homogeneity_error_median':quant(hom,0.5),
                'homogeneity_error_q90':quant(hom,0.9),
                'mean_coefficient':[m.real,m.imag],
                'rms_coefficient':rr,
            })

    # Simple antipodal cancellation criterion is intentionally strict.
    medians=[r['antipodal_ratio_median'] for r in rows]
    near_zero=sum(x<0.05 for x in medians)
    out={
        'gamma':args.gamma,'seed':args.seed,'r0':fmt(R0),
        'angular_min_beta_over_r':ANGULAR_MIN,'samples_per_cluster':SAMPLES,
        'rows':rows,
        'median_antipodal_ratio_range':[min(medians),max(medians)],
        'rows_with_median_antipodal_ratio_lt_0p05':near_zero,
        'verdict':('GENERIC_ANTIPODAL_CANCELLATION_PRESENT' if near_zero==len(rows)
                   else 'NO_GENERIC_ANTIPODAL_CANCELLATION'),
        'guardrail':(
            'Uniform tangent-sphere directions with an explicit exclusion of nested sub-collision angular strata. '
            'Failure of antipodal cancellation rules out the simplest principal-value parity mechanism on generic sectors, '
            'but does not exclude more complicated full-sphere cancellations or the published distributional i-epsilon prescription.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__': main()
