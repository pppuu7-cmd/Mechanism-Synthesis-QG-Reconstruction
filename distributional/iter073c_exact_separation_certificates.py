#!/usr/bin/env python3
"""Iter073C: exact Stiemke/Gordan certificates for nontransitive source classes."""
from __future__ import annotations
import argparse,itertools,json,math
from collections import Counter
from pathlib import Path
from distributional.iter073a_k4_signed_cutspace_face_atlas import (
    EDGES,TREES,Lmat,source_signs,dag_feasible,weak_order_feasible,permuted
)

NONTRANS=['++-+','+-++','+-+-','+--+']
CAP=8

def primitive_candidates(cap=CAP):
    out=[]
    for y in itertools.product(range(-cap,cap+1),repeat=3):
        if y==(0,0,0): continue
        g=math.gcd(math.gcd(abs(y[0]),abs(y[1])),abs(y[2]))
        if g!=1: continue
        out.append(y)
    out.sort(key=lambda y:(sum(abs(v) for v in y),y))
    return out
CAND=primitive_candidates()

def Lrows(tree):
    L,_=Lmat(tree)
    return [tuple(int(L[e,j]) for j in range(3)) for e in range(6)]

def cert_for(S,signs,rows):
    for y in CAND:
        w=[]
        for e in S:
            r=rows[e]; w.append(int(signs[e])*(r[0]*y[0]+r[1]*y[1]+r[2]*y[2]))
        if all(v>=0 for v in w) and any(v>0 for v in w):
            pos=[v for v in w if v>0]
            return {'y':list(y),'w':w,'l1':sum(abs(v) for v in y),'positive_components':len(pos),'positive_margin':min(pos)}
    return None

def audit_signs(signs,tree,store=True):
    rows=Lrows(tree); cases=[]; ok=True
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            fa,_=weak_order_feasible(S,signs); fb=dag_feasible(S,signs)
            cert=cert_for(S,signs,rows)
            case_ok=(fa==fb and (cert is not None)==(not fb))
            ok &= case_ok
            if store:
                cases.append({'S':list(S),'m':m,'positive_feasible':bool(fb),'routes_agree':bool(fa==fb),'certificate':cert,'ok':bool(case_ok)})
    return ok,cases

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    allcases={}; p1=p2=p3=p4=True; global_l1=Counter(); global_pc=Counter(); margins=[]
    basis_summaries={}
    for lab in NONTRANS:
        signs=source_signs(lab); ref_status=None; basis_summaries[lab]={}
        for tr in TREES:
            ok,cases=audit_signs(signs,tr,store=True)
            p1 &= ok
            p2 &= all(c['certificate'] is not None and all(v>=0 for v in c['certificate']['w']) and any(v>0 for v in c['certificate']['w']) for c in cases)
            p3 &= all((not c['positive_feasible']) and c['routes_agree'] for c in cases)
            status=tuple((tuple(c['S']),c['positive_feasible'],c['certificate'] is not None) for c in cases)
            if ref_status is None: ref_status=status
            else: p4 &= (status==ref_status)
            l1=Counter(c['certificate']['l1'] for c in cases); pc=Counter(c['certificate']['positive_components'] for c in cases)
            for c in cases:
                global_l1[c['certificate']['l1']]+=1; global_pc[c['certificate']['positive_components']]+=1; margins.append(c['certificate']['positive_margin'])
            basis_summaries[lab][tr]={
                'cases':len(cases),'all_separated':all(c['certificate'] is not None for c in cases),
                'l1_histogram':{str(k):v for k,v in sorted(l1.items())},
                'positive_component_histogram':{str(k):v for k,v in sorted(pc.items())},
                'min_positive_margin':min(c['certificate']['positive_margin'] for c in cases)}
            allcases[f'{lab}:{tr}']=cases

    # S4 certificate-existence/subset-size census, recomputed on S0.
    p6=True; s4_census={}
    for lab in NONTRANS:
        base=source_signs(lab); seen=[]
        for perm in itertools.permutations(range(4)):
            sg=permuted(base,perm); ok,cases=audit_signs(sg,'S0',store=True)
            h=Counter(c['m'] for c in cases if c['certificate'] is not None)
            seen.append((ok,tuple(sorted(h.items()))))
        p6 &= all(v==seen[0] for v in seen)
        s4_census[lab]={'all_24_equal':all(v==seen[0] for v in seen),'signature':list(seen[0][1])}

    # Positive control: a ++++ positive-admissible face must not admit separation.
    pos=source_signs('++++'); prow=Lrows('S0'); control=None
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            if dag_feasible(S,pos):
                control={'S':list(S),'certificate':cert_for(S,pos,prow)}; break
        if control: break
    p7=bool(control and control['certificate'] is None)
    p5=bool(margins and min(margins)>=1)
    ok=bool(p1 and p2 and p3 and p4 and p5 and p6 and p7)
    out={
        'iteration':'Iter073C','nontransitive_classes':NONTRANS,'hard_cap':CAP,
        'cases_expected':4*4*63,'cases_audited':sum(len(v) for v in allcases.values()),
        'basis_summaries':basis_summaries,
        'global_l1_histogram':{str(k):v for k,v in sorted(global_l1.items())},
        'global_positive_component_histogram':{str(k):v for k,v in sorted(global_pc.items())},
        'global_min_positive_integer_margin':min(margins) if margins else None,
        's4_census':s4_census,'positive_control':control,
        'predicates':{
            'P1_ALL_1008_CERTIFICATES':bool(p1),'P2_CERTIFICATE_INEQUALITIES_EXACT':bool(p2),
            'P3_INDEPENDENT_POSITIVITY_RECOMPUTATION':bool(p3),'P4_BASIS_STATUS_INVARIANT':bool(p4),
            'P5_INTEGER_MARGIN_RECORDED':bool(p5),'P6_S4_CENSUS_INVARIANT':bool(p6),
            'P7_POSITIVE_CONTROL_REJECTS_UNIVERSAL_SEPARATION':bool(p7)},
        'classification':'ITER073C_NONTRANSITIVE_ALL_FACES_EXACT_STIEMKE_SEPARATED_SCOPED' if ok else 'ITER073C_EXACT_SEPARATION_CERTIFICATE_FAIL',
        'claim_lock':'Reduced positive-real cut-space separation only; no epsilon->0 boundedness/convergence or physical vertex finiteness theorem.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(9)
if __name__=='__main__': main()
