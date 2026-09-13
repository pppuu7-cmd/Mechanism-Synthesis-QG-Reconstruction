#!/usr/bin/env python3
import argparse, glob, json, os, sys

ap=argparse.ArgumentParser(); ap.add_argument('--input-root',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
lanes={}
for path in glob.glob(os.path.join(args.input_root,'iter076f-*','*.json')):
    with open(path) as f: d=json.load(f)
    if d.get('lane') in 'ABCD': lanes[d['lane']]=d
found=sorted(lanes)
valid_all=(found==list('ABCD') and all(lanes[x].get('valid') is True for x in 'ABCD'))
primary=False
if valid_all:
    primary=(
        lanes['A']['predicates']['dimensions_exact'] and
        lanes['A']['predicates']['spaces_invariant'] and
        lanes['A']['predicates']['characters_standard_vs_sign_twist_exact'] and
        lanes['B']['predicates']['untwisted_hom_zero'] and
        lanes['B']['predicates']['sign_twisted_hom_one'] and
        lanes['C']['predicates']['generator_invertible'] and
        lanes['C']['predicates']['twisted_covariance_all_24'] and
        lanes['C']['predicates']['ordinary_covariance_rejected_on_odd'] and
        lanes['D']['predicates']['basis_covariant_dimensions'] and
        lanes['D']['predicates']['ordinary_intertwiner_control_rejected'] and
        lanes['D']['predicates']['drop_reorientation_sign_control_rejected']
    )
classification = ('ITER076F_K4_CUT_CYCLE_INTERTWINER_REQUIRES_ORIENTATION_SIGN_TWIST_EXACT_SCOPED' if primary else 'ITER076F_FROZEN_PREDICATE_FAIL')
out={'iteration':'Iter076F','lanes_found':found,'lane_valid':{k:lanes[k].get('valid',False) for k in found},'valid':bool(valid_all and primary),'scope_guard_ok':True,'classification':classification,'claim_lock':'No physical source-to-K4 pushforward is defined; no epsilon^-1 coefficient; no causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion.'}
os.makedirs(os.path.dirname(args.output),exist_ok=True)
with open(args.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if not out['valid']: sys.exit(2)
