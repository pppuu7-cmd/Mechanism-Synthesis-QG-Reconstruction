#!/usr/bin/env python3
"""Iter073B: exact 64-sign K4 independent-wedge cut-space atlas."""
from __future__ import annotations
import itertools,json,argparse
from collections import Counter
from pathlib import Path
import sympy as sp
from distributional.iter073a_k4_signed_cutspace_face_atlas import (
    EDGES,TREES,Lmat,weak_order_feasible,dag_feasible,permuted
)


def bits_label(signs):
    return ''.join('+' if s>0 else '-' for s in signs)

def source_vector(z):
    return tuple(z[a]*z[b] for a,b in EDGES)

def source_subset():
    return {source_vector((1,z1,z2,z3)) for z1,z2,z3 in itertools.product((1,-1),repeat=3)}

def tournament_transitive(signs):
    score=[0]*4
    for (a,b),s in zip(EDGES,signs): score[a if s>0 else b]+=1
    return sorted(score,reverse=True)==[3,2,1,0]

def face_data(signs,L,proper=True):
    rows=[]
    stop=5 if proper else 6
    for m in range(1,stop+1):
        for S in itertools.combinations(range(6),m):
            A=L[list(S),:].T*sp.diag(*[signs[e] for e in S])
            rank=int(A.rank()); nu=m-rank
            fa,_=weak_order_feasible(S,signs); fb=dag_feasible(S,signs)
            rows.append((tuple(S),m,rank,nu,fa,fb))
    return rows

def proper_signature(rows):
    good=[r for r in rows if r[4]]
    h=Counter((r[1],r[3]) for r in good)
    return max((r[3] for r in good),default=-1),tuple(sorted((m,nu,n) for (m,nu),n in h.items()))

def sign_signature(signs):
    ref=None; basis_ok=True; route_ok=True
    for tr in TREES:
        L,det=Lmat(tr)
        rows=face_data(signs,L,proper=True)
        route_ok &= all(r[4]==r[5] for r in rows)
        exact=tuple((r[0],r[2],r[3],r[4]) for r in rows)
        sig=proper_signature(rows)
        if ref is None: ref=(exact,sig)
        else: basis_ok &= (exact==ref[0] and sig==ref[1])
    L0,_=Lmat('S0')
    Af=L0.T*sp.diag(*signs)
    full_nu=6-int(Af.rank())
    full_pos=dag_feasible(range(6),signs)
    trans=tournament_transitive(signs)
    return {
        'label':bits_label(signs),'signs':list(signs),'full_nullity':full_nu,
        'full_positive':bool(full_pos),'transitive':bool(trans),
        'max_proper_nullity':ref[1][0],
        'proper_histogram':[list(x) for x in ref[1][1]],
        'basis_ok':bool(basis_ok),'route_ok':bool(route_ok),
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    vectors=[tuple(v) for v in itertools.product((1,-1),repeat=6)]
    rows=[sign_signature(v) for v in vectors]
    p1=all(r['basis_ok'] for r in rows)
    p2=all(r['route_ok'] for r in rows)
    p3=all(r['full_nullity']==3 and r['full_positive']==r['transitive'] for r in rows)
    full_count=sum(r['full_positive'] for r in rows)

    # P5 exact S4 invariance of the reduced signature.
    by={tuple(r['signs']):r for r in rows}; p5=True
    for s,r in by.items():
        key=(r['full_positive'],r['transitive'],r['max_proper_nullity'],tuple(map(tuple,r['proper_histogram'])))
        for perm in itertools.permutations(range(4)):
            spm=tuple(permuted(list(s),perm)); rp=by[spm]
            kp=(rp['full_positive'],rp['transitive'],rp['max_proper_nullity'],tuple(map(tuple,rp['proper_histogram'])))
            if kp!=key: p5=False; break
        if not p5: break

    src=source_subset(); p6=(len(src)==8)
    source_cross={}
    for s in sorted(src):
        r=by[s]; source_cross[bits_label(s)]={
            'full_positive':r['full_positive'],'transitive':r['transitive'],
            'max_proper_nullity':r['max_proper_nullity'],'proper_histogram':r['proper_histogram']}
        expected_pos=r['transitive']
        if expected_pos:
            p6 &= (r['max_proper_nullity']==2 and r['proper_histogram']==[[3,1,2],[4,1,1],[5,2,3]])
        else:
            p6 &= (r['max_proper_nullity']==-1 and r['proper_histogram']==[])

    # P7: one-edge scramble genuinely exits source subset for at least one source vector.
    exits=[]
    for s in src:
        t=list(s); t[0]*=-1; t=tuple(t)
        if t not in src: exits.append((bits_label(s),bits_label(t)))
    p7=bool(exits)

    maxnull=Counter(r['max_proper_nullity'] for r in rows)
    fullsplit=Counter(('transitive' if r['transitive'] else 'cyclic') for r in rows)
    p4=(sum(maxnull.values())==64)
    ok=bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out={
        'iteration':'Iter073B','vectors':64,
        'full_positive_count':full_count,
        'tournament_split':dict(sorted(fullsplit.items())),
        'max_proper_nullity_distribution':{str(k):v for k,v in sorted(maxnull.items())},
        'source_subset_size':len(src),'source_crosscheck':source_cross,
        'negative_control_source_edge0_flip_exits':exits,
        'predicates':{
            'P1_BASIS_EXACT':bool(p1),'P2_TWO_POSITIVITY_ROUTES_AGREE':bool(p2),
            'P3_FULLSET_POSITIVE_IFF_TRANSITIVE':bool(p3),'P4_COMPLETE_64_CENSUS':bool(p4),
            'P5_S4_SIGNATURE_INVARIANT':bool(p5),'P6_ITER073A_SOURCE_SUBSET_RECOVERED':bool(p6),
            'P7_SCRAMBLE_NEGATIVE_CONTROL':bool(p7)},
        'classification':'ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_EXACT_SCOPED' if ok else 'ITER073B_K4_INDEPENDENT_WEDGE_64_SIGN_ATLAS_FAIL',
        'rows':rows,
        'claim_lock':'Exact reduced signed cut-space geometry only; no distributional Eq.(5)/(6), no full Toller vertex, no K5/G3/F9/G8 promotion.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
