#!/usr/bin/env python3
"""Enumerate causal 4-simplex sign classes and map them to sl2cfoam booster legs.

For a causal vertex the ten wedge signs are not independent:
    kappa_ab = sigma_a sigma_b,  sigma_a in {+1,-1}.
A global flip of all five sigma leaves every kappa invariant, so there are 16
unique classes rather than 2^10 arbitrary wedge patterns.

The booster leg orders below are taken directly from upstream sl2cfoam-next
`src/boosters.c` MAP_SPINS_2 ... MAP_SPINS_5 macros.  Bit=1 selects T^(+),
bit=0 selects T^(-) in the branch adapter.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

NODES = (1,2,3,4,5)
FACES = tuple((a,b) for a in NODES for b in NODES if a<b)
BOOSTER_LEGS = {
    2: ((2,3),(2,4),(2,5),(1,2)),
    3: ((3,4),(3,5),(1,3),(2,3)),
    4: ((4,5),(1,4),(2,4),(3,4)),
    5: ((1,5),(2,5),(3,5),(4,5)),
}
BOOSTER_GF = {2:4,3:3,4:2,5:1}


def canon_face(a,b): return (a,b) if a<b else (b,a)

def kappas(sig): return {f:sig[f[0]]*sig[f[1]] for f in FACES}

def mask_for_booster(kappa, node):
    mask=0
    bits=[]
    for leg,f in enumerate(BOOSTER_LEGS[node]):
        k=kappa[canon_face(*f)]
        bits.append(k)
        if k>0: mask |= 1<<leg
    return mask,bits

def transition(sig):
    nplus=sum(v>0 for v in sig.values()); nminus=5-nplus
    small=min(nplus,nminus); large=max(nplus,nminus)
    return f"{small}<->{large}"

def cycle_ok(k):
    for a,b,c in itertools.combinations(NODES,3):
        if k[canon_face(a,b)]*k[canon_face(b,c)]*k[canon_face(a,c)] != 1:
            return False
    return True

def enumerate_classes():
    classes=[]
    # Gauge the global sign flip by fixing sigma_1=+1.
    for tail in itertools.product((-1,+1), repeat=4):
        sig={1:+1,2:tail[0],3:tail[1],4:tail[2],5:tail[3]}
        kap=kappas(sig)
        booster={}
        for node in (2,3,4,5):
            mask,bits=mask_for_booster(kap,node)
            booster[str(node)]={
                "gauge_fixed_leg_index":BOOSTER_GF[node],
                "faces":[list(f) for f in BOOSTER_LEGS[node]],
                "kappa_by_leg":bits,
                "mask_decimal":mask,
                "mask_binary":format(mask,"04b"),
            }
        classes.append({
            "class_id":len(classes),
            "sigma":{str(k):v for k,v in sig.items()},
            "transition":transition(sig),
            "semiclassical_nondegenerate_lorentzian_geometry_allowed":transition(sig)!="0<->5",
            "kappa":{f"{a}{b}":kap[(a,b)] for a,b in FACES},
            "cycle_constraints_pass":cycle_ok(kap),
            "sl2cfoam_boosters":booster,
            "booster_mask_tuple_2_3_4_5":[booster[str(n)]["mask_decimal"] for n in (2,3,4,5)],
        })
    return classes

def brute_factorizable_count():
    good=[]
    for signs in itertools.product((-1,+1), repeat=len(FACES)):
        k=dict(zip(FACES,signs))
        if cycle_ok(k): good.append(k)
    return good

def consistency_report(classes):
    # Faces joining two non-gauge-fixed nodes appear in two boosters and must
    # carry the same causal branch at both locations.
    shared={(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)}
    bad=[]
    for c in classes:
        for f in shared:
            seen=[]
            for node in f:
                legs=BOOSTER_LEGS[node]
                idx=next(i for i,x in enumerate(legs) if canon_face(*x)==f)
                seen.append(c["sl2cfoam_boosters"][str(node)]["kappa_by_leg"][idx])
            if seen[0]!=seen[1]: bad.append((c["class_id"],f,seen))
    return bad

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/causal_vertex_sigma_booster_map.json");args=ap.parse_args()
    classes=enumerate_classes(); good=brute_factorizable_count(); bad=consistency_report(classes)
    unique_kappa={tuple(c["kappa"][f"{a}{b}"] for a,b in FACES) for c in classes}
    unique_masks={tuple(c["booster_mask_tuple_2_3_4_5"]) for c in classes}
    counts=Counter(c["transition"] for c in classes)
    passed=(len(classes)==16 and len(unique_kappa)==16 and len(good)==16 and len(unique_masks)==16 and not bad and all(c["cycle_constraints_pass"] for c in classes))
    out={
        "passed":passed,
        "sigma_classes_mod_global_flip":len(classes),
        "all_wedge_sign_patterns":2**10,
        "factorizable_kappa_patterns":len(good),
        "factorizable_fraction":len(good)/(2**10),
        "transition_class_counts":dict(sorted(counts.items())),
        "unique_sl2cfoam_booster_mask_tuples":len(unique_masks),
        "shared_face_consistency_failures":bad,
        "upstream_mapping":{
            "booster_2":["j23","j24","j25","j12"],
            "booster_3":["j34","j35","j13","j23"],
            "booster_4":["j45","j14","j24","j34"],
            "booster_5":["j15","j25","j35","j45"],
            "gauge_fixed_indices":{"2":4,"3":3,"4":2,"5":1},
        },
        "classes":classes,
        "verdict":"CAUSAL_SIGMA_CLASSES_MAPPED_TO_SL2CFOAM_BOOSTER_MASKS" if passed else "CAUSAL_VERTEX_SIGN_MAP_FAILED",
        "next_action":"After complex branch-resolved B4 validation, use these four correlated booster masks per sigma class in a controlled causal-vertex contraction. Do not sample arbitrary independent wedge signs.",
        "scientific_guardrail":"The 0<->5 combinatorial class exists algebraically but a nondegenerate Lorentzian 4-simplex does not realize that geometric orientation class; keep combinatorial and Regge causal data distinct."
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k!="classes"},indent=2))
    if not passed: raise SystemExit(6)

if __name__=="__main__": main()
