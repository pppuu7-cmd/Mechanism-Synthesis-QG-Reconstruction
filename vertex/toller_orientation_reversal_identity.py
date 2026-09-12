#!/usr/bin/env python3
"""Iter037B/C: discover and hold out the j=1/2 Toller orientation-reversal law.

The published causal vertex uses one Toller matrix per oriented wedge with
argument g_b^{-1}g_a.  Iter036's S5 finite-part mechanism is physically useful
only if odd vertex relabelings/orientation reversal act covariantly on the
actual Toller carrier.

For generic separated Lorentz elements we compute the full 2x2 j=l=k=1/2
blocks T_+(g), T_-(g), T_+(g^{-1}), T_-(g^{-1}).  A finite preregistered family
of possible universal reversal transforms is tested:

  source branch: same or swapped;
  matrix operation: transpose, conjugate, adjoint,
                    epsilon-sandwiched transpose/conjugate/adjoint;
  fixed phase: 1,-1,+i,-i.

The candidate with smallest *training* max relative Frobenius error is frozen,
then evaluated on disjoint holdout edges.  No candidate is invented after the
holdout is seen.  In parallel the EPRL control D=T_++T_- must obey the unitary
block identity D(g^{-1})=D(g)^dagger.

A universal branch-swapping reversal law would mean odd edge-orientation
changes cannot be treated as the same fixed causal branch without the induced
branch/boundary duality.  This is an integrand-carrier statement, not yet a
proof of the fully contracted/integrated simplex symmetry.
"""
from __future__ import annotations

import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from vertex.direct_causal_integrand_smoke import PAIRS,make_groups
from vertex.regulated_haar_mc_vertex import full_branch

mp.mp.dps=60
MS=(1,-1)
EPS=np.array([[0,1],[-1,0]],dtype=np.complex128)
EPSI=np.linalg.inv(EPS)
PHASES={'1':1+0j,'-1':-1+0j,'i':1j,'-i':-1j}


def matrix_for(branch,g,gamma):
    M=np.zeros((2,2),dtype=np.complex128);ke=0.0
    for i,m in enumerate(MS):
        for j,n in enumerate(MS):
            z,_,e=full_branch(branch,g,gamma,m,n);M[i,j]=complex(z);ke=max(ke,e)
    return M,ke

def relerr(A,B):return float(np.linalg.norm(A-B)/max(np.linalg.norm(B),1e-30))
def ops(M):
    return {
      'transpose':M.T,
      'conjugate':M.conj(),
      'adjoint':M.conj().T,
      'eps_transpose':EPS@M.T@EPSI,
      'eps_conjugate':EPS@M.conj()@EPSI,
      'eps_adjoint':EPS@M.conj().T@EPSI,
    }

def candidates():
    return [(src,op,ph) for src in ('same','swap') for op in ops(np.eye(2)).keys() for ph in PHASES]

def predict(cand,branch,Mp,Mm):
    src,op,ph=cand
    B=(Mp if (branch>0 and src=='same') or (branch<0 and src=='swap') else Mm)
    # explicit branch map: for target +, same=>Mp swap=>Mm; for target -, same=>Mm swap=>Mp
    if branch<0:
        B=(Mm if src=='same' else Mp)
    return PHASES[ph]*ops(B)[op]

def eval_candidate(cand,samples):
    errs=[]
    for Mp,Mm,Ip,Im in samples:
        errs.append(relerr(predict(cand,+1,Mp,Mm),Ip))
        errs.append(relerr(predict(cand,-1,Mp,Mm),Im))
    return max(errs),float(np.median(errs))

def cf(z):return [float(np.real(z)),float(np.imag(z))]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--gamma',required=True);ap.add_argument('--seed',type=int,required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    gamma=mp.mpf(args.gamma);ep.GAMMA=gamma
    gs,_,_,_,_=make_groups(args.seed+37000,min_pair_beta=0.55)
    samples=[];eprl=[];kerrs=[]
    for a,b in PAIRS:
        g=np.linalg.inv(gs[b])@gs[a];gi=np.linalg.inv(g)
        Mp,e1=matrix_for(+1,g,gamma);Mm,e2=matrix_for(-1,g,gamma)
        Ip,e3=matrix_for(+1,gi,gamma);Im,e4=matrix_for(-1,gi,gamma)
        samples.append((Mp,Mm,Ip,Im));kerrs.append(max(e1,e2,e3,e4))
        D=Mp+Mm;Di=Ip+Im;eprl.append(relerr(Di,D.conj().T))
    train=samples[:5];hold=samples[5:]
    scored=[]
    for c in candidates():
        mx,med=eval_candidate(c,train);scored.append((mx,med,c))
    scored.sort(key=lambda x:(x[0],x[1],x[2]))
    best=scored[0][2];train_max,train_med=eval_candidate(best,train);hold_max,hold_med=eval_candidate(best,hold)
    runner_up=scored[1]
    gates={
      'eprl_inverse_adjoint_control':max(eprl)<2e-10,
      'universal_toller_reversal_candidate_train':train_max<2e-8,
      'frozen_candidate_holds_out':hold_max<2e-8,
      'kak_reconstruction_stable':max(kerrs)<1e-10,
    }
    gates={k:bool(v) for k,v in gates.items()};passed=all(gates.values())
    out={
      'iteration':'Iter037B/C','gamma':args.gamma,'seed':args.seed,
      'sample_edges':len(samples),'training_edges':5,'holdout_edges':5,
      'best_frozen_candidate':{'source_branch':best[0],'matrix_operation':best[1],'phase':best[2]},
      'training_max_relative_error':train_max,'training_median_relative_error':train_med,
      'holdout_max_relative_error':hold_max,'holdout_median_relative_error':hold_med,
      'runner_up_training':{'max_error':runner_up[0],'median_error':runner_up[1],
                            'source_branch':runner_up[2][0],'matrix_operation':runner_up[2][1],'phase':runner_up[2][2]},
      'eprl_inverse_adjoint_max_error':max(eprl),'max_kak_reconstruction_error':max(kerrs),
      'gates':gates,'pass':passed,
      'verdict':'TOLLER_ORIENTATION_REVERSAL_IDENTITY_RESOLVED' if passed else 'TOLLER_ORIENTATION_REVERSAL_IDENTITY_UNRESOLVED',
      'claim_lock':('j=1/2 gamma-simple block on generic separated group elements. A successful local reversal identity still '
                    'must be propagated through transported boundary intertwiners and the full simplex contraction.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
