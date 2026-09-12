#!/usr/bin/env python3
"""Iteration 027B: numerical weighted single-edge norm test.

Christensen-type graph bounds reduce to weighted single-edge integrals.  This
script independently checks the relevant local exponent for the full j=l=1/2
Toller matrix, not just one magnetic element.

For random compact factors U1,U2 and small beta, construct the 2x2 T^sigma(g)
matrix for g=U1 exp(beta sigma_z/2) U2.  Measure its spectral/operator norm and
fit p from ||T|| ~ beta^{-p}.  Then classify weighted radial integrals

  int sinh(beta)^2 ||T||^m d beta

for m=1, 1.49, 1.5, 2.0, 2.5 by the fitted local exponent.  The critical m is
3/p.  The K5 Christensen cover requires m>=2.5 on at least one tree edge.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import random_su2, boost
from vertex.regulated_haar_mc_vertex import full_branch

mp.mp.dps=60
BETAS=[mp.mpf(x) for x in ('0.10','0.05','0.025','0.0125','0.00625','0.003125')]
WEIGHTS=(1.0,1.49,1.5,2.0,2.5)


def fit_power(xs,ys):
    pts=[(mp.log(x),mp.log(mp.mpf(str(y)))) for x,y in zip(xs,ys) if y>0]
    pts=pts[-4:]
    xb=sum(x for x,_ in pts)/len(pts); yb=sum(y for _,y in pts)/len(pts)
    return -sum((x-xb)*(y-yb) for x,y in pts)/sum((x-xb)**2 for x,_ in pts)


def full_matrix(branch,g,gamma):
    M=np.zeros((2,2),dtype=np.complex128); maxke=0.0
    ms=(1,-1)
    for i,m in enumerate(ms):
        for j,n in enumerate(ms):
            z,_,ke=full_branch(branch,g,gamma,m,n)
            M[i,j]=complex(z); maxke=max(maxke,ke)
    return M,maxke


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma
    rng=np.random.default_rng(args.seed)
    U1=random_su2(rng); U2=random_su2(rng)
    rows=[]
    for branch in (+1,-1):
        norms=[]; maxke=0.0
        for b in BETAS:
            g=U1@boost(float(b))@U2
            M,ke=full_matrix(branch,g,gamma)
            maxke=max(maxke,ke)
            norms.append(float(np.linalg.svd(M,compute_uv=False)[0]))
        p=fit_power(BETAS,norms); mcrit=mp.mpf(3)/p
        tests=[]
        for m in WEIGHTS:
            radial_power=mp.mpf(2)-p*mp.mpf(str(m))
            tests.append({'m':m,'radial_power':mp.nstr(radial_power,20),
                          'locally_integrable':bool(radial_power>-1),
                          'log_borderline':bool(abs(radial_power+1)<mp.mpf('0.05'))})
        rows.append({'branch':branch,'operator_norms':norms,'fitted_p':mp.nstr(p,20),
                     'critical_m_3_over_p':mp.nstr(mcrit,20),'weighted_tests':tests,
                     'max_kak_reconstruction_error':maxke})
    ps=[mp.mpf(r['fitted_p']) for r in rows]
    crits=[mp.mpf(r['critical_m_3_over_p']) for r in rows]
    out={'gamma':args.gamma,'seed':args.seed,'betas':[mp.nstr(x,12) for x in BETAS],
         'rows':rows,'p_range':[mp.nstr(min(ps),20),mp.nstr(max(ps),20)],
         'critical_m_range':[mp.nstr(min(crits),20),mp.nstr(max(crits),20)],
         'K5_tree_required_M':2.5,
         'K5_weight_2p5_integrable_all':all(next(t for t in r['weighted_tests'] if t['m']==2.5)['locally_integrable'] for r in rows),
         'verdict':('NUMERIC_TOLLER_NORM_EXCLUDES_K5_TREE_WEIGHT_2P5'
                    if max(crits)<mp.mpf('2.5') else 'NUMERIC_TREE_WEIGHT_NOT_EXCLUDED'),
         'guardrail':'Local operator-norm scan for generic compact factors; confirms the input exponent used by the exact graph-bound no-go but is not itself a global vertex theorem.'}
    pth=Path(args.output);pth.parent.mkdir(parents=True,exist_ok=True)
    pth.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
