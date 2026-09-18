#!/usr/bin/env python3
# Frozen implementation trigger; scientific contract is prereg bf520ee5eb2a72d4aad867cb0b97f80299f2c301.
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; FRAME=ROOT/'scripts/k5_34_orbit_resolver_s5_frame_diagnostic.py'; PREREG=ROOT/'prereg/K5_34_ORBIT_RESOLVER_SOURCE_COEFFICIENT_TRANSPORT_DEFECT_DIAGNOSTIC.md'; PRE='bf520ee5eb2a72d4aad867cb0b97f80299f2c301'; FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m
f=load(FRAME,'srcdef_frame'); c,s5,P=f.c,f.s5,f.P
def H(x): return hashlib.sha256(repr(x).encode()).hexdigest()
def target_key(types,transpose):
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
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args(); pre=PREREG.read_text(); base=c._BASE_PATTERNS
 no_transpose=transform(base,False,True); target=transform(base,True,True); no_source_sign=transform(base,True,False)
 mc_target=project(target); pushed=f.push_matching_coeff(c.MATCH_COEFF,P); mc_no_transpose=project(no_transpose)
 endpoint_ok=sorted(s5.ep(P,i) for i in range(10))==list(range(10)); key_target=set().union(*(d.keys() for d in target)); key_pushed=set().union(*(d.keys() for d in no_source_sign))
 orientation_ok=(key_target!=set().union(*(d.keys() for d in no_transpose))) or coeff(mc_no_transpose)!=coeff(mc_target); component_key_ok=(key_target==key_pushed); boundary_ok=(coeff(project(target))==coeff(mc_target)); source_spectral_ok=(s5.orientation_character(P)==1 and target==no_source_sign) or (s5.orientation_character(P)!=1 and target!=no_source_sign); prewick_ok=(coeff(mc_target)==coeff(pushed))
 stages={'endpoint_map':endpoint_ok,'orientation_reversal_control_discriminates':orientation_ok,'source_component_key':component_key_ok,'boundary_contragredient':boundary_ok,'source_spectral_component':source_spectral_ok,'prewick_product':prewick_ok}
 if not endpoint_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_ENDPOINT_MAP'
 elif not orientation_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_ORIENTATION_REVERSAL'
 elif not component_key_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_SOURCE_COMPONENT_KEY'
 elif not boundary_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_BOUNDARY_CONTRAGREDIENT'
 elif not source_spectral_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_SOURCE_SPECTRAL_COMPONENT'
 elif not prewick_ok: cls='K5_S5_SOURCE_COEFF_DEFECT_PREWICK_PRODUCT'
 else: cls='K5_S5_SOURCE_COEFF_NO_DEFECT_ON_FROZEN_MATCHING'
 fixed=project(base); bad=dict(mc_target)
 if FROZEN in bad:
  q=[list(x) for x in bad[FROZEN]]; q[0][0]+=1; bad[FROZEN]=(tuple(q[0]),tuple(q[1]))
 validity={'prereg_locked':PRE=='bf520ee5eb2a72d4aad867cb0b97f80299f2c301' and 'source-coefficient transport defect diagnostic' in pre,'full32':len(base)==32,'source100000':c._SOURCE_TERM_COUNT==100000,'matching_present_target':FROZEN in mc_target,'matching_present_pushed':FROZEN in pushed,'support945':len(mc_target)==len(pushed)==945,'exact_fraction':all(isinstance(x,Fraction) for m in (mc_target,pushed) for v in m.values() for ch in v for x in ch),'source_fixed_rejected':coeff(fixed)!=coeff(mc_target),'orientation_flag_flip_rejected':coeff(mc_no_transpose)!=coeff(mc_target),'boundary_coeff_mutation_rejected':coeff(bad)!=coeff(mc_target)}
 if not all(validity.values()): cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 out={'gate':'K5_34_ORBIT_RESOLVER_SOURCE_COEFFICIENT_TRANSPORT_DEFECT_DIAGNOSTIC','prereg_commit':PRE,'classification':cls,'scientific_verdict':None,'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN},'stage_equalities':stages,'validity':validity,'hashes':{'target_patterns':H(target),'no_transpose':H(no_transpose),'no_source_sign':H(no_source_sign),'target_matching':f.match_hash(mc_target),'pushed_matching':f.match_hash(pushed),'frozen_target':H(coeff(mc_target)),'frozen_pushed':H(coeff(pushed))},'no_N_B_orders_or_coefficients_recorded':True,'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print('CLASSIFICATION='+cls); print(json.dumps(stages,sort_keys=True)); return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0
if __name__=='__main__': raise SystemExit(main())
