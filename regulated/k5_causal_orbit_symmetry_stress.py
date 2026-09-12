#!/usr/bin/env python3
"""Iter036B: numerical stress test of source-causal orbit isotropization.

For each of the three causal sign partition types 5+0, 4+1, 3+2, build the
stabilizer H inside S5.  A random determinant-normalized SPD cycle metric is
first H-averaged, representing the most general tested sector tensor compatible
with that fixed causal type.  We then average its S5 transforms.  If Iter036A's
exact theorem is realized numerically, the determinant-normalized orbit average
is the identity for every profile, even when the three causal orbit types are
assigned arbitrary positive relative weights.

A control weakly biases one member within the nontrivial 4+1 and 3+2 orbits;
this should restore anisotropy, showing that equality/covariance *within* each
source orbit is the essential condition rather than equality between orbit
types.

This is a K5 symmetry/covariance stress test.  It does not derive physical
sector weights from the Toller amplitude.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
EIDX={e:k for k,e in enumerate(EDGES)}
PERMS=list(itertools.permutations(range(N)))
TYPES={'5+0':(1,1,1,1,1),'4+1':(1,-1,-1,-1,-1),'3+2':(1,1,-1,-1,-1)}


def incidence():
    b=np.zeros((N,10))
    for k,(i,j) in enumerate(EDGES):b[i,k]=-1;b[j,k]=1
    return b

def cycle_basis():
    _,s,vt=np.linalg.svd(incidence(),full_matrices=True);r=int(np.sum(s>1e-12));q=vt[r:].T
    assert q.shape==(10,6);return q

def edge_rep(p):
    P=np.zeros((10,10))
    for col,(i,j) in enumerate(EDGES):
        a,b=p[i],p[j];sgn=1.0
        if a>b:a,b=b,a;sgn=-1.0
        P[EIDX[(a,b)],col]=sgn
    return P

def cycle_rep(p,q):return q.T@edge_rep(p)@q

def transform_sigma(sig,p):
    out=[0]*N
    for i in range(N):out[p[i]]=sig[i]
    return tuple(out)
def canon(sig):return sig if sig[0]==1 else tuple(-x for x in sig)
def stabilizer(sig):return [i for i,p in enumerate(PERMS) if canon(transform_sigma(sig,p))==canon(sig)]
def orbit(sig):return {canon(transform_sigma(sig,p)) for p in PERMS}

def detnorm(s):
    sign,ld=np.linalg.slogdet(s)
    if sign<=0:raise ValueError('not SPD')
    return s/math.exp(ld/6)
def anis(s):
    e=np.linalg.eigvalsh(s);return float(e[-1]/e[0]-1)
def random_spd(rng,cond):
    x=rng.normal(size=(6,6));q,_=np.linalg.qr(x);lam=np.geomspace(1/math.sqrt(cond),math.sqrt(cond),6);rng.shuffle(lam)
    return detnorm((q@np.diag(lam)@q.T + (q@np.diag(lam)@q.T).T)/2)
def avg(s,reps,weights=None):
    if weights is None:weights=np.ones(len(reps))
    z=float(np.sum(weights));out=np.zeros_like(s)
    for w,r in zip(weights,reps):out+=float(w)*(r.T@s@r)
    return (out/z+(out/z).T)/2
def identity_residual(s):return float(np.linalg.norm(detnorm(s)-np.eye(6))/np.linalg.norm(np.eye(6)))
def max_comm(s,reps):
    sc=max(float(np.linalg.norm(s)),1e-30);return float(max(np.linalg.norm(s@r-r@s)/sc for r in reps))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profile',type=int,required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    if not 0<=args.profile<32:raise SystemExit('profile 0..31')
    rng=np.random.default_rng(36000+args.profile);q=cycle_basis();reps=[cycle_rep(p,q) for p in PERMS]
    conds=[3.,10.,30.,100.,300.,1000.,3000.,10000.];cond=conds[args.profile%8]
    rows=[];orbit_avgs=[]
    for name,sig in TYPES.items():
        Hidx=stabilizer(sig);H=[reps[i] for i in Hidx]
        s0=random_spd(rng,cond);sh=avg(s0,H);sg=avg(sh,reps);orbit_avgs.append(sg)
        row={
          'type':name,'orbit_size':len(orbit(sig)),'stabilizer_order':len(H),
          'sector_metric_anisotropy':anis(detnorm(sh)),
          'stabilizer_commutator':max_comm(sh,H),
          'S5_orbit_average_identity_residual':identity_residual(sg),
        }
        if len(orbit(sig))>1:
            target=canon(sig)
            weights=[]
            for p in PERMS:
                sector=canon(transform_sigma(sig,p))
                weights.append(math.exp(0.2 if sector==target else 0.0))
            biased=avg(sh,reps,np.asarray(weights))
            row['within_orbit_bias_0p2_anisotropy']=anis(detnorm(biased))
        else: row['within_orbit_bias_0p2_anisotropy']=0.0
        rows.append(row)

    # Relative weights between the three complete causal orbit sums are arbitrary.
    logw=rng.uniform(-4,4,size=3);w=np.exp(logw);combined=sum(float(a)*b for a,b in zip(w,orbit_avgs))/float(np.sum(w))
    gates={
      'orbit_sizes_1_5_10':[r['orbit_size'] for r in rows]==[1,5,10],
      'stabilizer_orders_120_24_12':[r['stabilizer_order'] for r in rows]==[120,24,12],
      'fixed_sector_stabilizers_respected':max(r['stabilizer_commutator'] for r in rows)<3e-12,
      'each_complete_orbit_isotropic':max(r['S5_orbit_average_identity_residual'] for r in rows)<3e-12,
      'arbitrary_interorbit_weights_still_isotropic':identity_residual(combined)<3e-12,
      'nontrivial_fixed_sectors_retain_shape':min(r['sector_metric_anisotropy'] for r in rows if r['type']!='5+0')>1e-5,
      'within_orbit_bias_restores_shape':min(r['within_orbit_bias_0p2_anisotropy'] for r in rows if r['type']!='5+0')>1e-6,
    }
    gates={k:bool(v) for k,v in gates.items()};passed=all(gates.values())
    out={
      'iteration':'Iter036B','profile':args.profile,'seed':36000+args.profile,'condition_target':cond,
      'rows':rows,'interorbit_weights':[float(x) for x in w],
      'combined_identity_residual':identity_residual(combined),'gates':gates,'pass':passed,
      'interpretation_if_pass':('A fixed nontrivial causal sector permits stabilizer-compatible cycle shape, but an equal-within-orbit '
                                'S5-covariant sum removes that shape for each source orbit separately. Relative weights between 5+0, 4+1 '
                                'and 3+2 types do not reintroduce shape; breaking equality inside an orbit does.'),
      'claim_lock':('The tested tensors are symmetry-compatible surrogates. Physical Toller/Feynman sector covariance and orbit weights '
                    'must be checked on the source amplitude before using this as a finite-part prescription.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
