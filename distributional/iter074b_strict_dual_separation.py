#!/usr/bin/env python3
"""Iter074B: exact strict dual separation on all nontransitive K4 source faces."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

from distributional.iter073a_k4_signed_cutspace_face_atlas import (
    TREES, Lmat, source_signs, dag_feasible, permuted
)

NONTRANS = ['++-+','+-++','+-+-','+--+']
CAP = 12


def primitive_candidates():
    out=[]
    for y in itertools.product(range(-CAP,CAP+1), repeat=3):
        if y==(0,0,0):
            continue
        g=0
        for v in y:
            g=math.gcd(g,abs(v))
        if g!=1:
            continue
        out.append(y)
    out.sort(key=lambda y:(sum(abs(v) for v in y),y))
    return out

CAND = primitive_candidates()


def rows_for(tree):
    L,_=Lmat(tree)
    return [tuple(int(L[e,j]) for j in range(3)) for e in range(6)]


def strict_cert(S, signs, rows):
    for y in CAND:
        w=[]
        for e in S:
            r=rows[e]
            w.append(int(signs[e])*(r[0]*y[0]+r[1]*y[1]+r[2]*y[2]))
        if all(v>0 for v in w):
            l1=sum(abs(v) for v in y)
            return {
                'y':list(y),'w':w,'l1':l1,
                'min_margin':min(w),
                'delta1':str(Fraction(min(w),l1)),
            }
    return None


def no_nonnegative_kernel_on_S(S,signs):
    S=tuple(S)
    for r in range(1,len(S)+1):
        for U in itertools.combinations(S,r):
            if dag_feasible(U,signs):
                return False,list(U)
    return True,None


def audit(signs,tree,store=True):
    rows=rows_for(tree)
    cases=[]; all_ok=True
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            cert=strict_cert(S,signs,rows)
            no_kernel,wit=no_nonnegative_kernel_on_S(S,signs)
            exact=False
            if cert is not None:
                y=cert['y']
                check=[]
                for e in S:
                    r=rows[e]
                    check.append(int(signs[e])*(r[0]*y[0]+r[1]*y[1]+r[2]*y[2]))
                exact=(check==cert['w'] and min(check)>=1)
            ok=(cert is not None and exact and no_kernel)
            all_ok &= ok
            if store:
                cases.append({'S':list(S),'m':m,'certificate':cert,
                              'no_nonnegative_kernel':no_kernel,
                              'kernel_counterexample_support':wit,'ok':ok})
    return all_ok,cases


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    summaries={}; all_cases={}
    P1=P2=P3=P4=True
    l1_hist=Counter(); margin_hist=Counter(); delta_hist=Counter(); deltas=[]
    for lab in NONTRANS:
        signs=source_signs(lab); summaries[lab]={}; ref_status=None
        for tr in TREES:
            ok,cases=audit(signs,tr,store=True)
            P1 &= ok
            P2 &= all(c['certificate'] is not None and min(c['certificate']['w'])>=1 for c in cases)
            P3 &= all(c['no_nonnegative_kernel'] for c in cases)
            status=tuple((tuple(c['S']),c['certificate'] is not None,c['no_nonnegative_kernel']) for c in cases)
            if ref_status is None: ref_status=status
            else: P4 &= (status==ref_status)
            for c in cases:
                cert=c['certificate']; l1_hist[cert['l1']]+=1; margin_hist[cert['min_margin']]+=1
                delta_hist[cert['delta1']]+=1; deltas.append(Fraction(cert['delta1']))
            summaries[lab][tr]={
                'cases':len(cases),'all_strict':all(c['certificate'] is not None for c in cases),
                'max_primitive_l1':max(c['certificate']['l1'] for c in cases),
                'min_delta1':str(min(Fraction(c['certificate']['delta1']) for c in cases)),
            }
            all_cases[f'{lab}:{tr}']=cases

    P5=bool(deltas); delta_min=min(deltas) if deltas else Fraction(0,1)

    # S4 invariance of strict-certificate existence census by subset size, recomputed in S0 coordinates.
    P6=True; s4={}
    for lab in NONTRANS:
        base=source_signs(lab); sigs=[]
        for perm in itertools.permutations(range(4)):
            sg=permuted(base,perm); ok,cases=audit(sg,'S0',store=True)
            h=Counter(c['m'] for c in cases if c['certificate'] is not None)
            sig=(ok,tuple(sorted(h.items())))
            sigs.append(sig)
        same=all(v==sigs[0] for v in sigs)
        P6 &= same
        s4[lab]={'all_24_equal':same,'signature':list(sigs[0][1])}

    # Positive control: first ++++ positive face must forbid strict dual separation.
    psg=source_signs('++++'); prows=rows_for('S0'); pos_control=None
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            if dag_feasible(S,psg):
                pos_control={'S':list(S),'certificate':strict_cert(S,psg,prows)}
                break
        if pos_control is not None:
            break
    P7=bool(pos_control is not None and pos_control['certificate'] is None)

    passed=bool(P1 and P2 and P3 and P4 and P5 and P6 and P7)
    out={
        'iteration':'Iter074B',
        'hard_coordinate_cap':CAP,
        'cases_expected':4*4*63,
        'cases_audited':sum(len(v) for v in all_cases.values()),
        'global_delta1_min':str(delta_min),
        'primitive_l1_histogram':{str(k):v for k,v in sorted(l1_hist.items())},
        'integer_margin_histogram':{str(k):v for k,v in sorted(margin_hist.items())},
        'normalized_margin_histogram':dict(sorted(delta_hist.items(), key=lambda kv: Fraction(kv[0]))),
        'summaries':summaries,
        's4_census':s4,
        'positive_control':pos_control,
        'predicates':{
            'P1_ALL_1008_STRICT_CERTIFICATES':bool(P1),
            'P2_EXACT_STRICT_COMPONENTWISE_VERIFICATION':bool(P2),
            'P3_NO_NONZERO_NONNEGATIVE_KERNEL_BY_SUPPORT_RECOMPUTATION':bool(P3),
            'P4_BASIS_STATUS_INVARIANT':bool(P4),
            'P5_GLOBAL_EXACT_DELTA1_BOUND_RECORDED':bool(P5),
            'P6_S4_EXISTENCE_CENSUS_INVARIANT':bool(P6),
            'P7_POSITIVE_CONTROL_FORBIDS_STRICT_DUAL':bool(P7),
        },
        'classification':('ITER074B_NONTRANSITIVE_ALL_FACES_STRICT_DUAL_SEPARATION_EXACT_SCOPED'
                          if passed else 'ITER074B_STRICT_DUAL_SEPARATION_FAIL'),
        'claim_lock':'Exact positive-real strict dual separation in the reduced cut-space only; no epsilon->0 convergence, complex boundary-value, physical vertex finiteness, K5/G3/F9/G8, complete QG or new physics claim.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(9)

if __name__=='__main__':
    main()
