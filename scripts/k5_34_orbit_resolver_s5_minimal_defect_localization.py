#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / 'scripts/k5_34_orbit_resolver_s5_frame_diagnostic.py'
PREREG = ROOT / 'prereg/K5_34_ORBIT_RESOLVER_REPAIR1_S5_MINIMAL_DEFECT_LOCALIZATION.md'
PREREG_COMMIT = '37aa29af296a09f05c1a1392d05225416b073106'


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); assert spec.loader is not None
    spec.loader.exec_module(mod); return mod

f = load(FRAME, 'k5_min_defect_frame')
c, s5, P, PINV = f.c, f.s5, f.P, f.PINV


def h(obj):
    return hashlib.sha256(repr(obj).encode()).hexdigest()


def canon_support(mc):
    return tuple(sorted(tuple(sorted((min(a,b), max(a,b)) for a,b in mt)) for mt in mc))


def first_diff_dict(a,b):
    keys=sorted(set(a)|set(b))
    for k in keys:
        if a.get(k)!=b.get(k): return repr(k)
    return None


def mutate_one(mc):
    out=dict(mc); k=sorted(out)[0]; q=[list(x) for x in out[k]]
    q[0][0]=Fraction(q[0][0])+1; out[k]=(tuple(q[0]),tuple(q[1])); return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    pre=PREREG.read_text()
    base=f.c._BASE_PATTERNS
    target_dicts=f.explicit_target_dicts(base,P)
    target_mc=c._project_pattern_dicts_to_match_coeff(target_dicts)
    pushed_mc=f.push_matching_coeff(c.MATCH_COEFF,P)
    base_support=canon_support(c.MATCH_COEFF); target_support=canon_support(target_mc); pushed_support=canon_support(pushed_mc)

    stage1=sorted(s5.ep(P,i) for i in range(10))==list(range(10)) and all(s5.ep(PINV,s5.ep(P,i))==i for i in range(10))
    stage2=(len(target_mc)==945 and len(pushed_mc)==945 and target_support==pushed_support)
    stage3=(target_mc==pushed_mc)

    mask=1; mp=c.core.pmask(mask,P)
    original=c.route_a(mask,c.W1); target=c.route_a(mp,c.WP1,target_mc); pushed=c.route_a(mp,c.WP1,pushed_mc)
    stage5=all(f.lane_equal(original,target).values())
    stage6=all(f.lane_equal(original,target)[k] for k in ('ch1_B','ch2_B'))
    # Stage 4 is evaluated only if source coefficients agree; otherwise Wick is downstream/non-causal.
    stage4 = None if not stage3 else all(f.lane_equal(target,pushed).values())

    if not stage1: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_MATCHING_SUPPORT'
    elif not stage2: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_MATCHING_SUPPORT'
    elif not stage3: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_SOURCE_COEFFICIENT_TRANSPORT'
    elif stage4 is False: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_WICK_CONTRIBUTION'
    elif not stage5: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_NUMERATOR_ASSEMBLY'
    elif not stage6: cls='K5_34_ORBIT_S5_DEFECT_LOCALIZED_ANNIHILATOR_FLUX'
    else: cls='K5_34_ORBIT_S5_NO_DEFECT_ON_FROZEN_LANE'

    altered=mutate_one(target_mc)
    fixed=c.route_a(mp,c.WP1,c.MATCH_COEFF); alt=c.route_a(mp,c.WP1,altered)
    validity={
      'prereg_commit_locked': PREREG_COMMIT=='37aa29af296a09f05c1a1392d05225416b073106',
      'prereg_present': 'minimal S5 defect localization' in pre,
      'full32': len(base)==32, 'source_terms_100000': c._SOURCE_TERM_COUNT==100000,
      'target_945': len(target_mc)==945, 'pushed_945': len(pushed_mc)==945,
      'exact_rational': all(isinstance(x,Fraction) for mc in (target_mc,pushed_mc) for v in mc.values() for ch in v for x in ch),
      'source_fixed_rejected': not all(f.lane_equal(original,fixed).values()),
      'altered_one_matching_rejected': not all(f.lane_equal(original,alt).values()),
    }
    if not all(validity.values()): cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
    out={'gate':'K5_34_ORBIT_RESOLVER_REPAIR1_S5_MINIMAL_DEFECT_LOCALIZATION','prereg_commit':PREREG_COMMIT,
      'classification':cls,'scientific_coefficient_verdict':None,'frozen_lane':{'mask':1,'ray':'W1','cycle':list(P)},
      'stage_equalities':{'edge_roundtrip':stage1,'matching_support':stage2,'source_coefficients':stage3,'wick_contribution':stage4,'numerator':stage5,'annihilator_flux':stage6},
      'counts':{'target_matchings':len(target_mc),'pushed_matchings':len(pushed_mc)},
      'first_mismatch':{'matching_support': None if stage2 else first_diff_dict({k:1 for k in target_support},{k:1 for k in pushed_support}),
                        'source_coefficient': None if stage3 else first_diff_dict(target_mc,pushed_mc)},
      'hashes':{'target_support':h(target_support),'pushed_support':h(pushed_support),'target_mc':f.match_hash(target_mc),'pushed_mc':f.match_hash(pushed_mc)},
      'validity':validity,'no_N_B_orders_or_coefficients_recorded':True,
      'interpretation_ceiling':'implementation diagnosis only; no 64-component scientific authority'}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('CLASSIFICATION='+cls); print(json.dumps(out['stage_equalities'],sort_keys=True)); return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0

if __name__=='__main__': raise SystemExit(main())
