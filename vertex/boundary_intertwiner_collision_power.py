#!/usr/bin/env python3
"""Iteration 024: gauge-invariant boundary-intertwiner collision power counting.

Iterations 022/023 measured strong multi-collision poles in individual magnetic
components and in causal-sector sums.  The physical boundary state, however,
contracts the twenty boundary magnetic indices with five 4-valent SU(2)
intertwiners.  This script performs that contraction *before* the asymptotic
power fit.

All ten boundary spins are j=1/2.  Each 4-valent node therefore has the two
standard recoupling intertwiners two_i=0,2.  We test four representative
five-node boundary states.  For every group configuration we build the full
2x2 T+ and T- matrix on every wedge, then tensor-contract the complete K5 spin
network for:

  Cplus16   sum over 16 inequivalent factorized causal structures,
  Cminus16  co-causal sign reversal,
  Cboth32   Cplus16 + Cminus16,
  EPRL      every edge replaced by T+ + T-,
  fixed     all-plus causal structure.

The contraction uses the same normalized 4j convention already used by the
repository endpoint diagnostics.  Any phase convention independent of the
collision scale cannot change a power by itself, but cancellations among
magnetic components are retained exactly in the network contraction.

This is still local collision power counting, not the four-group integral.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from regulated.endpoint_precontraction_scan import w4jm
from vertex.multicollision_power_counting import (
    RS, CLUSTERS, cluster_setup, groups_at_r, rapidity_diagnostics,
    fmt, slope, classify_margin,
)
from vertex.direct_causal_integrand_smoke import PAIRS
from vertex.regulated_haar_mc_vertex import full_branch

mp.mp.dps = 70
MS = (1, -1)  # matrix index order: +1/2, -1/2
BOUNDARY_STATES = {
    'i00000': (0,0,0,0,0),
    'i22222': (2,2,2,2,2),
    'i02020': (0,2,0,2,0),
    'i20202': (2,0,2,0,2),
}


def node_tensor(two_i):
    """Normalized 4-valent j=1/2 intertwiner in the repository 4jm convention."""
    out=np.zeros((2,2,2,2),dtype=np.complex128)
    for inds in itertools.product(range(2),repeat=4):
        ms=tuple(MS[i] for i in inds)
        if sum(ms)!=0:
            continue
        val=mp.sqrt(two_i+1)*w4jm(1,1,1,1,*ms,two_i)
        out[inds]=complex(float(mp.re(val)),float(mp.im(val)))
    n=np.linalg.norm(out.ravel())
    if not np.isfinite(n) or n==0:
        raise RuntimeError(f'bad intertwiner two_i={two_i}')
    return out/n


NODE={0:node_tensor(0),2:node_tensor(2)}

# One tensor index for every oriented half-edge (a,b), a != b.
HALF={}
_counter=0
for a in range(5):
    for b in range(5):
        if a==b: continue
        HALF[(a,b)]=_counter; _counter+=1


def contract_network(edge_mats,boundary_state):
    args=[]
    for a,two_i in enumerate(boundary_state):
        nbrs=[b for b in range(5) if b!=a]
        args.extend([NODE[two_i],[HALF[(a,b)] for b in nbrs]])
    for a,b in PAIRS:
        # Eq.(4) convention: row m_ba at target b, column m_ab at source a.
        args.extend([edge_mats[(a,b)],[HALF[(b,a)],HALF[(a,b)]]])
    args.append([])
    return complex(np.einsum(*args,optimize='greedy'))


def edge_branch_matrices(groups,gamma):
    out={}; maxerr=0.0
    for a,b in PAIRS:
        rel=np.linalg.inv(groups[b])@groups[a]
        mats={+1:np.zeros((2,2),dtype=np.complex128),
              -1:np.zeros((2,2),dtype=np.complex128)}
        beta_ref=None
        for im,m_ba in enumerate(MS):
            for jn,m_ab in enumerate(MS):
                tp,beta,ke=full_branch(+1,rel,gamma,m_ba,m_ab)
                tm,_,ke2=full_branch(-1,rel,gamma,m_ba,m_ab)
                mats[+1][im,jn]=complex(tp)
                mats[-1][im,jn]=complex(tm)
                beta_ref=beta; maxerr=max(maxerr,ke,ke2)
        out[(a,b)]=(mats[+1],mats[-1],beta_ref)
    return out,maxerr


def mats_for_sigma(edgevals,sigma,co=False):
    mats={}
    for a,b in PAIRS:
        k=sigma[a]*sigma[b]
        if co: k=-k
        tp,tm,_=edgevals[(a,b)]
        mats[(a,b)]=tp if k>0 else tm
    return mats


def contracted_modes(edgevals,bstate):
    sigmas=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
    cp=0j; cm=0j
    for s in sigmas:
        cp += contract_network(mats_for_sigma(edgevals,s,False),bstate)
        cm += contract_network(mats_for_sigma(edgevals,s,True),bstate)
    eprl={}; fixed={}
    for a,b in PAIRS:
        tp,tm,_=edgevals[(a,b)]
        eprl[(a,b)]=tp+tm
        fixed[(a,b)]=tp
    return {
        'Cplus16':cp,
        'Cminus16':cm,
        'Cboth32':cp+cm,
        'EPRL':contract_network(eprl,bstate),
        'fixed_allplus':contract_network(fixed,bstate),
    }


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
        series={(bn,m):[] for bn in BOUNDARY_STATES
                for m in ('Cplus16','Cminus16','Cboth32','EPRL','fixed_allplus')}
        kerrs=[]; mins=[]; maxs=[]
        for r in RS:
            groups=groups_at_r(bg,dirs,hs,k,r)
            mn,mx,_,ke0=rapidity_diagnostics(groups,k)
            ev,ke1=edge_branch_matrices(groups,gamma)
            kerrs.append(max(ke0,ke1)); mins.append(mn); maxs.append(mx)
            for bn,bstate in BOUNDARY_STATES.items():
                vals=contracted_modes(ev,bstate)
                for mode,v in vals.items(): series[(bn,mode)].append(v)
        for (bn,mode),vals in series.items():
            q=slope(RS,vals)
            m1=q+d if mp.isfinite(q) else mp.nan
            m2=q+mp.mpf(d)/2 if mp.isfinite(q) else mp.nan
            rows.append({
                'cluster_k':k,'boundary_state':bn,'two_intertwiners':list(BOUNDARY_STATES[bn]),
                'mode':mode,'local_boost_dimension_d':d,
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

    causal=[r for r in rows if r['mode'] in ('Cplus16','Cminus16','Cboth32')]
    by_k={}
    for k in CLUSTERS:
        rr=[r for r in causal if r['cluster_k']==k]
        qs=[float(r['measured_slope']) for r in rr if r['measured_slope']!='nan']
        by_k[str(k)]={
            'rows':len(rr),
            'slope_range':[min(qs),max(qs)] if qs else None,
            'first_moment_PASS':sum(r['first_moment_class']=='PASS' for r in rr),
            'first_moment_BORDERLINE_LOG':sum(r['first_moment_class']=='BORDERLINE_LOG' for r in rr),
            'first_moment_FAIL':sum(r['first_moment_class']=='FAIL' for r in rr),
            'second_moment_PASS':sum(r['second_moment_class']=='PASS' for r in rr),
        }
    eprl=[r for r in rows if r['mode']=='EPRL']
    out={
        'gamma':args.gamma,'seed':args.seed,'r_values':[fmt(x) for x in RS],
        'boundary_states':{k:list(v) for k,v in BOUNDARY_STATES.items()},
        'causal_summary_by_cluster':by_k,
        'eprl_all_first_moment_pass':all(r['first_moment_class']=='PASS' for r in eprl),
        'eprl_all_second_moment_pass':all(r['second_moment_class']=='PASS' for r in eprl),
        'rows':rows,
        'verdict':'BOUNDARY_INTERTWINER_COLLISION_POWER_SCAN_COMPLETE',
        'guardrail':(
            'j=1/2 recoupling-basis boundary contraction performed before power fitting. '
            'This tests magnetic-index cancellations in four representative gauge-invariant boundary states. '
            'It is not the Haar-integrated vertex, does not exhaust all spins/coherent boundary data, and does not '
            'replace the distributional Feynman-i-epsilon prescription.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__': main()
