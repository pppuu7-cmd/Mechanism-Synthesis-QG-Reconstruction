#!/usr/bin/env python3
"""Iter068D: exact S4 covariance audit of the Iter068A K4 skeleton partition."""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
from distributional.iter068a_k4_microlocal_collision import EDGES, parse_sigma, oriented_normal, subset_zero_witness

EDGE_SET=set(EDGES)

def canon_edge(u,v): return (u,v,1) if u<v else (v,u,-1)
def classify(sign_by_edge):
    normals=[oriented_normal(e,sign_by_edge[e]) for e in EDGES]
    return subset_zero_witness(normals) is not None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--sigma',required=True); ap.add_argument('--convention',required=True,choices=['+1','-1']); ap.add_argument('--output',required=True); a=ap.parse_args()
    sigma=parse_sigma(a.sigma); c=int(a.convention)
    orig_kappa={e:sigma[e[0]]*sigma[e[1]] for e in EDGES}
    orig_sign={e:c*orig_kappa[e] for e in EDGES}
    orig_collision=classify(orig_sign)
    rows=[]; ok_all=True
    for p in itertools.permutations(range(4)):
        inv=[0]*4
        for old,new in enumerate(p): inv[new]=old
        trans_sign={}
        for e in EDGES:
            u,v=e; nu,nv=p[u],p[v]; a0,b0,orient=canon_edge(nu,nv)
            trans_sign[(a0,b0)]=orig_sign[e]*orient
        # transformed vertex sigma and global gauge recanonicalization
        ts=[sigma[inv[new]] for new in range(4)]
        if ts[0]<0: ts=[-x for x in ts]
        trans_kappa={e:ts[e[0]]*ts[e[1]] for e in EDGES}
        expected_kappa={}
        for e in EDGES:
            u,v=e; old_u,old_v=inv[u],inv[v]
            expected_kappa[e]=sigma[old_u]*sigma[old_v]
        kappa_ok=(trans_kappa==expected_kappa)
        collision_ok=(classify(trans_sign)==orig_collision)
        # Pull transformed covectors back with inverse permutation.
        recovered={}
        for e,s in trans_sign.items():
            u,v=e; ou,ov=inv[u],inv[v]; a0,b0,orient=canon_edge(ou,ov)
            recovered[(a0,b0)]=s*orient
        inverse_ok=(recovered==orig_sign)
        row_ok=kappa_ok and collision_ok and inverse_ok and set(trans_sign)==EDGE_SET
        ok_all=ok_all and row_ok
        rows.append({'permutation':list(p),'kappa_reconstruction':kappa_ok,'collision_invariant':collision_ok,
                     'inverse_recovery':inverse_ok,'valid':row_ok})
    classification=('ITER068D_K4_MICROLOCAL_SKELETON_S4_COVARIANT' if ok_all and len(rows)==24 else 'ITER068D_K4_MICROLOCAL_SKELETON_PERMUTATION_FAILURE')
    out={'iteration':'Iter068D','sigma':a.sigma,'convention':c,'original_collision_obstructed':orig_collision,
         'permutations':len(rows),'all_valid':ok_all,'rows':rows,'classification':classification,
         'claim_lock':'S4 covariance of denominator skeleton only; no full Toller wavefront theorem or physical sector selection.'}
    pth=Path(a.output); pth.parent.mkdir(parents=True,exist_ok=True); pth.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2,sort_keys=True))
    if classification.endswith('FAILURE'): raise SystemExit(9)
if __name__=='__main__': main()
