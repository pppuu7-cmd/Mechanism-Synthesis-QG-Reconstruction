#!/usr/bin/env python3
"""Iter036C: exact covariance audit of the 16 source causal sign sectors.

The causal vertex uses factorized wedge signs kappa_ab=sigma_a sigma_b with five
sigma_a signs modulo the global reversal sigma->-sigma.  This script verifies
purely combinatorially that the 16 canonical sectors carry the expected S5
action, split into orbits 1+5+10, and that the ten-edge branch-sign vector is
covariant under every one of the 120 vertex permutations.

It also verifies that any scalar sector weight depending only on causal orbit
type (5+0,4+1,3+2) is exactly S5-invariant.  This is a prerequisite for using
the Iter036A/B orbit-isotropization mechanism.  It does not check the numerical
Toller matrix values, boundary states, or the full integrated amplitude.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
PERMS=list(itertools.permutations(range(N)))

def canon(s):return s if s[0]==1 else tuple(-x for x in s)
def transform(s,p):
    out=[0]*N
    for i in range(N):out[p[i]]=s[i]
    return canon(tuple(out))
def kappa(s):return tuple(s[i]*s[j] for i,j in EDGES)
def permute_edge_values(vals,p):
    out={}
    for v,(i,j) in zip(vals,EDGES):
        a,b=p[i],p[j]
        if a>b:a,b=b,a
        out[(a,b)]=v
    return tuple(out[e] for e in EDGES)
def ptype(s):
    n=sum(x>0 for x in s);m=N-n;a=max(n,m);b=min(n,m);return f'{a}+{b}'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    sectors=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
    assert len(sectors)==16
    cov_fail=[]
    for s in sectors:
        ks=kappa(s)
        for p in PERMS:
            st=transform(s,p)
            if permute_edge_values(ks,p)!=kappa(st):cov_fail.append({'sigma':s,'perm':p});break
    orbits=[];remaining=set(sectors)
    while remaining:
        s=next(iter(remaining));O={transform(s,p) for p in PERMS};orbits.append(O);remaining-=O
    rows=[]
    for O in sorted(orbits,key=len):
        rep=sorted(O)[0];H=[p for p in PERMS if transform(rep,p)==rep]
        rows.append({'type':ptype(rep),'orbit_size':len(O),'stabilizer_order':len(H),'representative':list(rep)})
    # Three arbitrary distinct class weights remain invariant under every permutation.
    wtype={'5+0':2,'4+1':7,'3+2':11}
    invariant=True
    for s in sectors:
        for p in PERMS:
            if wtype[ptype(s)]!=wtype[ptype(transform(s,p))]:invariant=False
    passed=(not cov_fail and [r['orbit_size'] for r in rows]==[1,5,10]
            and [r['stabilizer_order'] for r in rows]==[120,24,12] and invariant)
    out={
      'iteration':'Iter036C','sector_count':16,'permutation_count':120,'edge_count':10,
      'orbit_rows':rows,'checked_sector_permutation_pairs':16*120,
      'branch_sign_covariance_failures':cov_fail,'class_weight_example':wtype,
      'class_weight_is_S5_invariant':invariant,'pass':passed,
      'verdict':'SOURCE_FACTORIZED_CAUSAL_SIGN_DATA_ARE_EXACTLY_S5_COVARIANT' if passed else 'SOURCE_CAUSAL_SIGN_COVARIANCE_REVIEW',
      'claim_lock':('Combinatorial causal-sign covariance only. Full Toller matrix elements and boundary/intertwiner data still require '
                    'a same-realization permutation-covariance test before the symmetry mechanism can constrain a physical finite part.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
