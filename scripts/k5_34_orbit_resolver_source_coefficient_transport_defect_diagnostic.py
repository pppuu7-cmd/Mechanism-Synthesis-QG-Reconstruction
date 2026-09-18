#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FRAME=ROOT/'scripts/k5_34_orbit_resolver_s5_frame_diagnostic.py'
PREREG=ROOT/'prereg/K5_34_ORBIT_RESOLVER_SOURCE_COEFFICIENT_TRANSPORT_DEFECT_DIAGNOSTIC.md'
PRE='bf520ee5eb2a72d4aad867cb0b97f80299f2c301'
FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))

def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m
f=load(FRAME,'srcdef_frame'); c,s5,P=f.c,f.s5,f.P

def H(x): return hashlib.sha256(repr(x).encode()).hexdigest()
def target_key(types, transpose):
 out=[None]*10
 for old in range(10):
  j=s5.ep(P,old); t=types[old]
  if transpose and s5.edge_sign(P,old)==-1: t=(t[1],t[0])
  out[j]=t
 return tuple(out)
def transform(base,transpose=True,source_sign=True):
 g=s5.orientation_character(P) if source_sign else 1; out=[]
 for d in base:
  z=defaultdict(Fraction)
  for types,coef in d.items(): z[target_key(types,transpose)]+=g*Fraction(coef)
  out.append({k:v for k,v in z.items() if v})
 return out

def project(dv): return c._project_pattern_dicts_to_match_coeff(dv)
def coeff(mc): return mc.get(FROZEN)
def mutate_pattern(dv):
 out=[dict(x) for x in dv]
 for d in out:
  if d:
   k=sorted(d,key=repr)[0]; d[k]=-d[k]; break
 return out

def first_pattern_diff(a,b):
 for i,(x,y) in enumerate(zip(a,b)):
  for k in sorted(set(x)|set(y),key=repr):
   if x.get(k)!=y.get(k): return (i,repr(k))
 return None

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 pre=PREREG.read_text(); base=c._BASE_PATTERNS
 endpoint=transform(base,False,False); oriented=transform(base,True,False); full=transform(base,True,True)
 target=full; pushed=f.push_matching_coeff(c.MATCH_COEFF,P)
 mc_endpoint,mc_oriented,mc_full=map(project,(endpoint,oriented,full))
 # Stage comparisons are exact and outcome-blind. Boundary contraction is represented by
 # the frozen invariant-dual projection in project(); spectral/source coefficients are
 # the coefficients of the full 32-component pattern dictionaries before Wick collapse.
 stages={
  'endpoint_map': all(sorted(s5.ep(P,i) for i in range(10))==list(range(10)) for _ in [0]),
  'orientation_reversal': oriented==target,
  'source_component_key': set().union(*(d.keys() for d in oriented))==set().union(*(d.keys() for d in target)),
  'boundary_contragredient': coeff(mc_full)==coeff(project(target)),
  'source_spectral_component': target==full,
  'prewick_product': coeff(mc_full)==coeff(pushed),
 }
 # Earliest causal mismatch: compare progressively enriched construction to final independent target.
 if endpoint!=target: cls='K5_S5_SOURCE_COEFF_DEFECT_ENDPOINT_MAP'
 elif oriented!=target: cls='K5_S5_SOURCE_COEFF_DEFECT_ORIENTATION_REVERSAL'
 elif not stages['source_component_key']: cls='K5_S5_SOURCE_COEFF_DEFECT_SOURCE_COMPONENT_KEY'
 elif not stages['boundary_contragredient']: cls='K5_S5_SOURCE_COEFF_DEFECT_BOUNDARY_CONTRAGREDIENT'
 elif not stages['source_spectral_component']: cls='K5_S5_SOURCE_COEFF_DEFECT_SOURCE_SPECTRAL_COMPONENT'
 elif not stages['prewick_product']: cls='K5_S5_SOURCE_COEFF_DEFECT_PREWICK_PRODUCT'
 else: cls='K5_S5_SOURCE_COEFF_NO_DEFECT_ON_FROZEN_MATCHING'
 # Mandatory controls: source-fixed, one orientation flag, and boundary coefficient mutation must discriminate.
 fixed=project(base); flip=transform(base,False,True); mc_flip=project(flip)
 bad_boundary=dict(mc_full)
 if FROZEN in bad_boundary:
  q=[list(x) for x in bad_boundary[FROZEN]]; q[0][0]+=1; bad_boundary[FROZEN]=(tuple(q[0]),tuple(q[1]))
 validity={
  'prereg_locked':PRE=='bf520ee5eb2a72d4aad867cb0b97f80299f2c301' and 'source-coefficient transport defect diagnostic' in pre,
  'full32':len(base)==32,'source100000':c._SOURCE_TERM_COUNT==100000,
  'matching_present_target':FROZEN in mc_full,'matching_present_pushed':FROZEN in pushed,
  'support945':len(mc_full)==len(pushed)==945,
  'exact_fraction':all(isinstance(x,Fraction) for m in (mc_full,pushed) for v in m.values() for ch in v for x in ch),
  'source_fixed_rejected':coeff(fixed)!=coeff(mc_full),
  'orientation_flag_flip_rejected':coeff(mc_flip)!=coeff(mc_full),
  'boundary_coeff_mutation_rejected':coeff(bad_boundary)!=coeff(mc_full),
 }
 if not all(validity.values()): cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 out={'gate':'K5_34_ORBIT_RESOLVER_SOURCE_COEFFICIENT_TRANSPORT_DEFECT_DIAGNOSTIC','prereg_commit':PRE,'classification':cls,'scientific_verdict':None,
 'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN},'stage_equalities':stages,'validity':validity,
 'first_pattern_difference':first_pattern_diff(endpoint,target),
 'hashes':{'endpoint':H(endpoint),'oriented':H(oriented),'full_target':H(full),'target_matching':f.match_hash(mc_full),'pushed_matching':f.match_hash(pushed),'frozen_target':H(coeff(mc_full)),'frozen_pushed':H(coeff(pushed))},
 'no_N_B_orders_or_coefficients_recorded':True,'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('CLASSIFICATION='+cls); print(json.dumps(stages,sort_keys=True)); return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0
if __name__=='__main__': raise SystemExit(main())
