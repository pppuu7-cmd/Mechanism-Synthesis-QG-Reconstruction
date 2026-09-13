#!/usr/bin/env python3
"""Iter075A: exact quantitative L1 coercivity for nontransitive K4 positive-real faces."""
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

CAND=primitive_candidates()


def rows_for(tree):
    L,_=Lmat(tree)
    return [tuple(int(L[e,j]) for j in range(3)) for e in range(6)]


def cert_for(S, signs, rows):
    for y in CAND:
        w=[]
        for e in S:
            r=rows[e]
            w.append(int(signs[e])*(r[0]*y[0]+r[1]*y[1]+r[2]*y[2]))
        if all(v>0 for v in w):
            norm_inf=max(abs(v) for v in y)
            return {
                'y':list(y), 'w':w,
                'min_margin':min(w),
                'norm_inf':norm_inf,
                'kappa1':str(Fraction(min(w),norm_inf)),
            }
    return None


def kernel_witness(S, signs):
    # dag_feasible is the exact positive/nonnegative-support feasibility primitive
    # used in the previous atlas. Return one nonempty feasible sub-support.
    for r in range(1,len(S)+1):
        for U in itertools.combinations(S,r):
            if dag_feasible(U, signs):
                return list(U)
    return None


def audit_one(signs, tree):
    rows=rows_for(tree)
    cases=[]
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            cert=cert_for(S,signs,rows)
            if cert is None:
                cases.append({'S':list(S),'m':m,'ok':False,'certificate':None})
                continue
            # Exact algebraic proof data. For z=sum t_e a_e, t_e>=0:
            # y.z=sum t_e w_e >= m0 ||t||1 and |y.z|<=||y||inf ||z||1.
            # Hence ||z||1 >= (m0/||y||inf)||t||1.
            m0=cert['min_margin']; ninf=cert['norm_inf']
            exact=(m0>=1 and ninf>=1 and Fraction(cert['kappa1'])==Fraction(m0,ninf))
            cases.append({'S':list(S),'m':m,'ok':bool(exact),'certificate':cert})
    return cases


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    all_cases={}; kappas=[]; hist=Counter(); P1=P2=P3=P4=P5=True
    basis_signatures={}

    for lab in NONTRANS:
        signs=source_signs(lab); ref=None; basis_signatures[lab]={}
        for tr in TREES:
            cases=audit_one(signs,tr)
            all_cases[f'{lab}:{tr}']=cases
            P1 &= (len(cases)==63 and all(c['certificate'] is not None for c in cases))
            P2 &= all(c['certificate'] is not None and Fraction(c['certificate']['kappa1'])>0 for c in cases)
            P4 &= all(c['ok'] for c in cases)
            sig=tuple((tuple(c['S']), c['certificate'] is not None) for c in cases)
            if ref is None: ref=sig
            else: P5 &= (sig==ref)
            ks=[Fraction(c['certificate']['kappa1']) for c in cases if c['certificate']]
            kappas.extend(ks)
            for k in ks: hist[str(k)]+=1
            basis_signatures[lab][tr]={'cases':len(cases),'min_kappa1':str(min(ks))}

    global_min=min(kappas) if kappas else Fraction(0,1)
    P3 &= (global_min >= Fraction(1,7))

    # S4 status census: every permutation of each nontransitive sign pattern must retain
    # all 63 strictly separated supports in a fixed coordinate basis.
    s4={}
    for lab in NONTRANS:
        base=source_signs(lab); counts=[]
        for perm in itertools.permutations(range(4)):
            sg=permuted(base,perm); cases=audit_one(sg,'S0')
            counts.append(sum(c['certificate'] is not None for c in cases))
        same=(all(v==63 for v in counts) and len(set(counts))==1)
        P5 &= same
        s4[lab]={'all_24_have_63_strict_faces':same,'counts':counts}

    # Transitive positive control: find first positive-admissible face; strict dual
    # must be absent and a nonnegative-kernel support must be present.
    psg=source_signs('++++'); prows=rows_for('S0'); control=None
    for m in range(1,7):
        for S in itertools.combinations(range(6),m):
            if dag_feasible(S,psg):
                control={
                    'S':list(S),
                    'strict_certificate':cert_for(S,psg,prows),
                    'kernel_witness_support':kernel_witness(S,psg),
                }
                break
        if control is not None: break
    P6=bool(control and control['strict_certificate'] is None and control['kernel_witness_support'])

    passed=bool(P1 and P2 and P3 and P4 and P5 and P6)
    out={
        'iteration':'Iter075A',
        'cases_expected':1008,
        'cases_audited':sum(len(v) for v in all_cases.values()),
        'hard_coordinate_cap':CAP,
        'global_exact_kappa1_min':str(global_min),
        'kappa1_histogram':dict(sorted(hist.items(), key=lambda kv: Fraction(kv[0]))),
        'basis_summaries':basis_signatures,
        's4_census':s4,
        'positive_control':control,
        'predicates':{
            'P1_ALL_1008_EXACT_STRICT_CERTIFICATES':bool(P1),
            'P2_ALL_DERIVED_KAPPA1_POSITIVE':bool(P2),
            'P3_GLOBAL_KAPPA1_AT_LEAST_ONE_SEVENTH':bool(P3),
            'P4_EXACT_COERCIVITY_COEFFICIENT_PROOF_DATA_VALID':bool(P4),
            'P5_BASIS_AND_S4_STATUS_INVARIANT':bool(P5),
            'P6_TRANSITIVE_POSITIVE_CONTROL_HAS_KERNEL_AND_NO_STRICT_DUAL':bool(P6),
        },
        'classification':('ITER075A_NONTRANSITIVE_POSITIVE_REAL_L1_COERCIVITY_EXACT_SCOPED'
                          if passed else 'ITER075A_COERCIVITY_GATE_FAIL'),
        'scientific_summary':('For every frozen nontransitive positive-real face, an exact strict dual certificate yields '
                              '||A_S t||_1 >= kappa ||t||_1 for all t>=0, with the reported exact kappa. '
                              'This is a reduced real-cone coercivity result only.'),
        'claim_lock':'No epsilon->0 convergence theorem, no complex/distributional boundary value, no physical causal-vertex finiteness, no K5/G3/F9/G8 promotion, no complete QG or new physics claim.'
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(9)

if __name__=='__main__':
    main()
