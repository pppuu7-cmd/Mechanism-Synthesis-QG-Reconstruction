#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'scripts/k5_34_orbit_resolver_source_coefficient_transport_defect_diagnostic.py'
PREREG=ROOT/'prereg/K5_34_ORBIT_PREWICK_PRODUCT_COMPOSITION_DEFECT_DIAGNOSTIC.md'
PRE='796fc0321179ed71ed0e941607ae018bc904cdcd'
FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m
sd=load(SRC,'prewick_parent'); f,c,s5,P=sd.f,sd.c,sd.s5,sd.P
def H(x): return hashlib.sha256(repr(x).encode()).hexdigest()
def one_component(base,i):
 return [base[j] if j==i else {} for j in range(32)]
def cf(mc): return mc.get(FROZEN)
def project(v): return c._project_pattern_dicts_to_match_coeff(v)
def push(mc): return f.push_matching_coeff(mc,P)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 base=c._BASE_PATTERNS; target=sd.transform(base,True,True)
 tgt=project(target); pushed=push(c.MATCH_COEFF)
 # Decompose the exact projection before the 32-component sum.  Each lane is
 # independently projected, so this diagnoses whether transport commutes with
 # component contraction without reading any N/B data.
 can_parts=[project(one_component(base,i)) for i in range(32)]
 tgt_parts=[project(one_component(target,i)) for i in range(32)]
 push_parts=[push(x) for x in can_parts]
 tvals=[cf(x) for x in tgt_parts]; pvals=[cf(x) for x in push_parts]
 # Equality as ordered components and as a multiset distinguishes a boundary
 # component permutation from a deeper rational/sign/multiplicity mismatch.
 ordered=tvals==pvals
 multiset=sorted(map(repr,tvals))==sorted(map(repr,pvals))
 first=next((i for i,(x,y) in enumerate(zip(tvals,pvals)) if x!=y),None)
 def sigrel(x,y):
  if x is None or y is None: return 'support'
  if x==y: return 'equal'
  try:
   if all(a==-b for A,B in zip(x,y) for a,b in zip(A,B)): return 'pure_sign'
  except TypeError: pass
  return 'nontrivial_rational_or_component_mix'
 relation=sigrel(tvals[first],pvals[first]) if first is not None else 'equal'
 matching_preimage=sum(1 for mt in c.MATCH_COEFF if f.permute_matching(mt,P)==FROZEN)
 support_ok=len(tgt)==len(pushed)==945 and set(tgt)==set(pushed)
 eligibility_ok=(FROZEN in tgt)==(FROZEN in pushed)
 # Mandatory mutations are outcome-blind controls.
 source_fixed=project(base)
 flip=sd.transform(base,False,True)
 flip_mc=project(flip)
 bad_parts=list(tvals); bad_parts[0]=pvals[1]
 multiplicity_mut=list(tvals); multiplicity_mut[0]=None if tvals[0] is None else tuple(tuple(2*z for z in q) for q in tvals[0])
 validity={'prereg_locked':PRE=='796fc0321179ed71ed0e941607ae018bc904cdcd' and 'pre-Wick product composition defect diagnostic' in PREREG.read_text(),'full32':len(base)==32,'source100000':c._SOURCE_TERM_COUNT==100000,'support945':support_ok,'unique_matching_preimage':matching_preimage==1,'exact_fraction':all(isinstance(z,Fraction) for mc in (tgt,pushed) for v in mc.values() for q in v for z in q),'source_fixed_rejected':cf(source_fixed)!=cf(tgt),'reversal_flip_rejected':cf(flip_mc)!=cf(tgt),'boundary_component_mutation_rejected':bad_parts!=tvals,'multiplicity_mutation_rejected':multiplicity_mut!=tvals}
 if not all(validity.values()): cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 elif matching_preimage!=1: cls='K5_S5_PREWICK_DEFECT_MATCHING_PREIMAGE'
 elif not support_ok: cls='K5_S5_PREWICK_DEFECT_TYPE_TRANSPORT'
 elif not eligibility_ok: cls='K5_S5_PREWICK_DEFECT_MATCHING_ELIGIBILITY'
 elif not ordered: cls='K5_S5_PREWICK_DEFECT_BOUNDARY_COMPONENT_COMPOSITION'
 elif cf(tgt)!=cf(pushed): cls='K5_S5_PREWICK_DEFECT_CHANNEL_REIM_COMPOSITION'
 elif tgt!=pushed: cls='K5_S5_PREWICK_DEFECT_FINAL_COMPONENT_SUM'
 else: cls='K5_S5_PREWICK_NO_DEFECT_ON_FROZEN_MATCHING'
 out={'gate':'K5_34_ORBIT_PREWICK_PRODUCT_COMPOSITION_DEFECT_DIAGNOSTIC','prereg_commit':PRE,'classification':cls,'scientific_verdict':None,'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN},'stage_equalities':{'matching_preimage_unique':matching_preimage==1,'type_transport_support':support_ok,'matching_eligibility':eligibility_ok,'boundary_component_ordered':ordered,'boundary_component_multiset':multiset,'channel_reim_composition':cf(tgt)==cf(pushed),'final_component_sum_full_matching_dict':tgt==pushed},'first_mismatch':{'component_index':first,'relation':relation},'validity':validity,'hashes':{'target_parts':H(tvals),'pushed_parts':H(pvals),'target_matching':f.match_hash(tgt),'pushed_matching':f.match_hash(pushed)},'no_N_B_orders_or_coefficients_recorded':True,'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print('CLASSIFICATION='+cls); print(json.dumps(out['stage_equalities'],sort_keys=True)); return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0
if __name__=='__main__': raise SystemExit(main())
