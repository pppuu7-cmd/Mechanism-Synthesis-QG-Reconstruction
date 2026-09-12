#!/usr/bin/env python3
"""Iteration 027A: full-sphere angular-mean test of leading causal collision residues.

This is independent of the antipodal test in Iter026.  It estimates whether the
leading homogeneous coefficient has a small *global* angular mean after the
full j=1/2 K5 boundary-intertwiner contraction and the Cboth32 causal+co-causal
sector sum.  A small mean can support a conditional/PV cancellation mechanism;
an O(1) mean/RMS ratio rules that mechanism out on the tested carrier.

Guardrail: this is a Monte-Carlo angular diagnostic, not the exact published
distributional i-epsilon integral and not a proof of convergence/divergence.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp
import numpy as np
from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import make_groups, random_su2
from vertex.multicollision_power_counting import rapidity_diagnostics, fmt
from vertex.regulated_haar_mc_vertex import directional_boost
from vertex.boundary_intertwiner_collision_power import BOUNDARY_STATES, edge_branch_matrices, contracted_modes

mp.mp.dps=60
KS=(3,4,5); R0=mp.mpf('0.003125'); ANGULAR_MIN=0.10; SAMPLES=64


def groups_from_omega(bg,hs,k,r,w):
    gs=[g.copy() for g in bg]; gs[0]=np.eye(2,dtype=complex)
    for i in range(1,k):
        v=np.asarray(w[3*(i-1):3*i],dtype=float); nv=float(np.linalg.norm(v))
        n=np.array([1.0,0.0,0.0]) if nv<1e-14 else v/nv
        gs[i]=directional_boost(float(r)*nv,n)@hs[i]
    return gs


def coeff(groups,gamma,bstate,k):
    ev,_=edge_branch_matrices(groups,gamma)
    z=contracted_modes(ev,bstate)['Cboth32']
    return complex(z)*(float(R0)**(k*(k-1)))


def mean(v): return sum(v,0j)/len(v)
def rms(v): return math.sqrt(sum(abs(z)**2 for z in v)/len(v))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gamma',required=True); ap.add_argument('--seed',type=int,required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); gamma=mp.mpf(a.gamma); ep.GAMMA=gamma; rng=np.random.default_rng(a.seed)
    rows=[]
    for k in KS:
        bg,_,_,_,_=make_groups(a.seed+91000+k,min_pair_beta=0.80)
        hs={i:random_su2(rng) for i in range(1,k)}
        dirs=[]; tries=0
        while len(dirs)<SAMPLES and tries<6000:
            tries+=1; w=rng.normal(size=3*(k-1)); w=w/np.linalg.norm(w)
            g=groups_from_omega(bg,hs,k,R0,w); mn,_,_,_=rapidity_diagnostics(g,k)
            if mn/float(R0) >= ANGULAR_MIN: dirs.append(w)
        if len(dirs)<SAMPLES: raise RuntimeError(f'angular sampling failed k={k}')
        for bname in ('i00000','i22222','i02020','i20202'):
            vals=[coeff(groups_from_omega(bg,hs,k,R0,w),gamma,BOUNDARY_STATES[bname],k) for w in dirs]
            rr=rms(vals); m=mean(vals); ratio=abs(m)/max(rr,1e-300)
            # Four disjoint batch means provide an elementary stability diagnostic.
            batch=[]
            q=SAMPLES//4
            for j in range(4): batch.append(abs(mean(vals[j*q:(j+1)*q]))/max(rms(vals[j*q:(j+1)*q]),1e-300))
            rows.append({'cluster_k':k,'boundary_state':bname,'samples':SAMPLES,'angular_mean_over_rms':ratio,'batch_mean_over_rms':batch,'max_batch_ratio':max(batch),'mean_coefficient':[m.real,m.imag],'rms_coefficient':rr})
    ratios=[r['angular_mean_over_rms'] for r in rows]
    # <0.15 is only a diagnostic support threshold, never a convergence proof.
    supported=sum(x<0.15 for x in ratios)
    out={'gamma':a.gamma,'seed':a.seed,'r0':fmt(R0),'samples_per_row':SAMPLES,'rows':rows,'ratio_range':[min(ratios),max(ratios)],'rows_below_0p15':supported,'rows_total':len(rows),'verdict':('GLOBAL_ANGULAR_MEAN_SMALL_ALL_ROWS' if supported==len(rows) else 'NO_UNIVERSAL_GLOBAL_ANGULAR_CANCELLATION'),'guardrail':'Monte-Carlo full-sphere mean of the leading homogeneous coefficient after boundary contraction and Cboth32 sector sum. It does not replace the exact distributional i-epsilon integral.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__': main()
