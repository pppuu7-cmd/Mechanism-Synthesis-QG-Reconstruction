#!/usr/bin/env python3
"""Iteration 038: full j=1/2 K5 causal-carrier permutation covariance.

Inputs already established:
  * Iter036: full S5 source-orbit symmetry would remove the K5 cycle-metric
    finite-part shape ambiguity.
  * Iter037A: A5 alone leaves one residual shape parameter; one odd permutation
    is needed to recover the unique S5 metric line.
  * Iter037B/C: on generic j=1/2 gamma-simple blocks,
        T_s(g^{-1}) = eps T_s(g)^T eps^{-1}
    (equivalently T_s(g^{-1}) = T_{-s}(g)^dagger in the tested convention),
    while D(g^{-1})=D(g)^dagger.

This script propagates the *same-branch eps-transpose* reversal law through the
complete K5 spin-network contraction.  We do not merely transpose an edge
matrix: when a vertex permutation reverses the canonical orientation of a K5
edge, eps is applied to the corresponding half-edge index at BOTH endpoint
intertwiners.  The four-valent node tensor is also transported to the new node
and its slots are permuted to the new canonical neighbour ordering.

For each generic group configuration we compare the original amplitude against
12 relabelings (six even, six odd), after regauging the permuted configuration
so new g_0=1.  We test three actual source causal representatives 5+0,4+1,3+2,
four j=1/2 recoupling-basis boundary states, and EPRL controls.

A PASS is an integrand-level same-realization S5 covariance result for this
small-spin carrier.  It does not prove covariance of the singular distributional
extension, all spins/coherent states, or the integrated vertex.
"""
from __future__ import annotations

import argparse,itertools,json,math
from pathlib import Path
import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import PAIRS,make_groups
from vertex.boundary_intertwiner_collision_power import (
    NODE,BOUNDARY_STATES,MS,edge_branch_matrices,
)

mp.mp.dps=60
EPS=np.array([[0,1],[-1,0]],dtype=np.complex128)
CAUSAL={
  '5+0':(1,1,1,1,1),
  '4+1':(1,-1,-1,-1,-1),
  '3+2':(1,1,-1,-1,-1),
}

def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2

def apply_axis(M,T,axis):
    # T'_{...i'...}=sum_i M_{i'i} T_{...i...}
    X=np.tensordot(M,T,axes=(1,axis))
    return np.moveaxis(X,0,axis)

def edge_reversed(a,b,p):
    # old canonical orientation a<b maps to p[a] -> p[b]; compare with new sorted orientation
    return p[a]>p[b]

def transport_node_tensors(boundary_state,p):
    pinv=[0]*5
    for old,new in enumerate(p):pinv[new]=old
    out={}
    for old_a,two_i in enumerate(boundary_state):
        T=NODE[two_i].copy()
        old_nbr=[b for b in range(5) if b!=old_a]
        # Every reversed incident edge contributes the epsilon duality on this half-edge.
        for ax,b in enumerate(old_nbr):
            lo,hi=(old_a,b) if old_a<b else (b,old_a)
            if edge_reversed(lo,hi,p):T=apply_axis(EPS,T,ax)
        new_a=p[old_a]
        new_nbr=sorted(b for b in range(5) if b!=new_a)
        # new axis c corresponds to old neighbour pinv[c]
        axes=[old_nbr.index(pinv[c]) for c in new_nbr]
        out[new_a]=np.transpose(T,axes=axes)
    return out

def contract_custom(edge_mats,node_tensors):
    # einsum integer-subscript form; one index per unordered half-edge endpoint.
    half={};n=0
    for a in range(5):
        for b in range(5):
            if a==b:continue
            half[(a,b)]=n;n+=1
    args=[]
    for a in range(5):
        nbr=sorted(b for b in range(5) if b!=a)
        args.extend([node_tensors[a],[half[(a,b)] for b in nbr]])
    for a,b in PAIRS:
        args.extend([edge_mats[(a,b)],[half[(b,a)],half[(a,b)]]])
    args.append([])
    return complex(np.einsum(*args,optimize='greedy'))

def mats_for_sigma(edgevals,sigma):
    out={}
    for a,b in PAIRS:
        tp,tm,_=edgevals[(a,b)];out[(a,b)]=tp if sigma[a]*sigma[b]>0 else tm
    return out

def mats_eprl(edgevals):
    return {(a,b):edgevals[(a,b)][0]+edgevals[(a,b)][1] for a,b in PAIRS}

def permute_groups(groups,p,regauge=True):
    out=[None]*5
    for old,new in enumerate(p):out[new]=groups[old].copy()
    if regauge:
        h=np.linalg.inv(out[0])
        out=[h@g for g in out]
    return out

def permute_sigma(s,p):
    out=[0]*5
    for old,new in enumerate(p):out[new]=s[old]
    return tuple(out)

def relerr(a,b):return float(abs(a-b)/max(abs(a),abs(b),1e-25))

def select_perms(seed):
    rng=np.random.default_rng(seed+38123)
    even=[p for p in itertools.permutations(range(5)) if parity(p)==0]
    odd=[p for p in itertools.permutations(range(5)) if parity(p)==1]
    # include identity in even plus five random nonidentity; include a simple transposition in odd plus five random.
    ident=tuple(range(5));trans=(1,0,2,3,4)
    ev=[ident]+[even[i] for i in rng.choice([i for i,p in enumerate(even) if p!=ident],size=5,replace=False)]
    od=[trans]+[odd[i] for i in rng.choice([i for i,p in enumerate(odd) if p!=trans],size=5,replace=False)]
    return ev+od

def original_node_tensors(bstate):return {a:NODE[two_i] for a,two_i in enumerate(bstate)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--gamma',required=True);ap.add_argument('--seed',type=int,required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    gamma=mp.mpf(args.gamma);ep.GAMMA=gamma
    groups,_,_,_,_=make_groups(args.seed+38000,min_pair_beta=0.65)
    orig_edges,k0=edge_branch_matrices(groups,gamma)
    orig={}
    for bn,bs in BOUNDARY_STATES.items():
        nodes=original_node_tensors(bs)
        for ct,s in CAUSAL.items():orig[(bn,ct)]=contract_custom(mats_for_sigma(orig_edges,s),nodes)
        orig[(bn,'EPRL')]=contract_custom(mats_eprl(orig_edges),nodes)
    rows=[];max_kerr=k0
    for p in select_perms(args.seed):
        pg=permute_groups(groups,p,True);pev,ke=edge_branch_matrices(pg,gamma);max_kerr=max(max_kerr,ke)
        nrev=sum(edge_reversed(a,b,p) for a,b in PAIRS)
        for bn,bs in BOUNDARY_STATES.items():
            nodes=transport_node_tensors(bs,p)
            for ct,s in CAUSAL.items():
                ps=permute_sigma(s,p);z=contract_custom(mats_for_sigma(pev,ps),nodes);ref=orig[(bn,ct)]
                rows.append({'permutation':list(p),'parity':'even' if parity(p)==0 else 'odd','reversed_edges':nrev,
                             'boundary_state':bn,'mode':ct,'reference_abs':abs(ref),'permuted_abs':abs(z),'relative_error':relerr(z,ref)})
            z=contract_custom(mats_eprl(pev),nodes);ref=orig[(bn,'EPRL')]
            rows.append({'permutation':list(p),'parity':'even' if parity(p)==0 else 'odd','reversed_edges':nrev,
                         'boundary_state':bn,'mode':'EPRL','reference_abs':abs(ref),'permuted_abs':abs(z),'relative_error':relerr(z,ref)})
    causal=[r for r in rows if r['mode']!='EPRL'];eprl=[r for r in rows if r['mode']=='EPRL']
    odd=[r for r in causal if r['parity']=='odd'];even=[r for r in causal if r['parity']=='even']
    gates={
      'even_causal_covariance':max(r['relative_error'] for r in even)<2e-8,
      'odd_causal_covariance_with_eps_duality':max(r['relative_error'] for r in odd)<2e-8,
      'eprl_full_permutation_control':max(r['relative_error'] for r in eprl)<2e-8,
      'kak_reconstruction_stable':max_kerr<1e-10,
    }
    gates={k:bool(v) for k,v in gates.items()};passed=all(gates.values())
    out={
      'iteration':'Iter038','gamma':args.gamma,'seed':args.seed,
      'permutations_tested':12,'causal_rows':len(causal),'eprl_rows':len(eprl),
      'max_even_causal_relative_error':max(r['relative_error'] for r in even),
      'max_odd_causal_relative_error':max(r['relative_error'] for r in odd),
      'max_eprl_relative_error':max(r['relative_error'] for r in eprl),
      'max_kak_reconstruction_error':max_kerr,'gates':gates,'pass':passed,
      'verdict':'FULL_SMALL_SPIN_CAUSAL_CARRIER_S5_COVARIANT' if passed else 'FULL_SMALL_SPIN_CAUSAL_CARRIER_COVARIANCE_REVIEW',
      'rows':rows,
      'claim_lock':('Pointwise generic j=1/2 boundary-contracted integrand covariance after explicit epsilon dual transport. '
                    'Does not prove covariance of the singular multiwedge distributional extension, the integrated vertex, or arbitrary spins/coherent states.'),
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
