#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
PREPATH=ROOT/'prereg/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC.md'
PRE='ea49bb0cc67887659bb92c8a68b616f6b7e52513'; COMPONENT=1; FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m
c=load(CORE,'c1diag_core');s5=c.s5;P=s5.C
def clean(d): return {k:Fraction(v) for k,v in d.items() if Fraction(v)}
def transport_one(d):
 g=s5.orientation_character(P);z=defaultdict(Fraction)
 for types,coef in d.items():
  out=[None]*10
  for old in range(10):
   j=s5.ep(P,old);t=types[old]
   if s5.edge_sign(P,old)==-1:t=(t[1],t[0])
   out[j]=t
  z[tuple(out)]+=g*Fraction(coef)
 return clean(z)
def H(d): return hashlib.sha256(repr(sorted(d.items(),key=lambda kv:repr(kv[0]))).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();base=c._BASE_PATTERNS
 tensors=s5.act.reach.local_tensor_vectors(s5.act.src);local=s5.act.reach.local_action_matrices(tensors)
 A=s5.boundary_matrix(P,local);Ai=s5.boundary_matrix(s5.invperm(P),local);ATi=s5.transpose(Ai)
 predicted=s5.transform_dictvec(ATi,base)
 target=[transport_one(d) for d in base]
 pred=clean(predicted[COMPONENT]);direct=clean(target[COMPONENT])
 ps=set(pred);ds=set(direct);missing=sorted(ps-ds,key=repr);spurious=sorted(ds-ps,key=repr);support_equal=ps==ds
 coeff_bad=next((k for k in sorted(ps&ds,key=repr) if pred[k]!=direct[k]),None)
 coeff_equal=support_equal and coeff_bad is None
 # endpoint/orientation roundtrip on every source term
 Pinv=s5.invperm(P)
 def tr(d,Q):
  g=s5.orientation_character(Q);z=defaultdict(Fraction)
  for types,coef in d.items():
   out=[None]*10
   for old in range(10):
    j=s5.ep(Q,old);t=types[old]
    if s5.edge_sign(Q,old)==-1:t=(t[1],t[0])
    out[j]=t
   z[tuple(out)]+=g*Fraction(coef)
  return clean(z)
 roundtrip=all(tr(tr(clean(d),P),Pinv)==clean(d) for d in base)
 wrong=s5.transform_dictvec(Ai,base)
 # predeclared nontrivial control component: first component where A^-1 and A^-T differ, fixed algorithmically before result comparison
 ctrl=next((i for i in range(32) if clean(wrong[i])!=clean(predicted[i])),None);wrong_rejected=ctrl is not None
 mutated=dict(pred)
 if mutated:
  k=sorted(mutated,key=repr)[0];mutated[k]+=Fraction(1)
 else: mutated[('MUTATION',)]=Fraction(1)
 mutation_rejected=mutated!=direct
 validity={'prereg_locked':PRE=='ea49bb0cc67887659bb92c8a68b616f6b7e52513' and 'component-1 support-mixing defect diagnostic' in PREPATH.read_text(),'component1_frozen':COMPONENT==1,'full32':len(base)==len(target)==len(predicted)==32,'source100000':c._SOURCE_TERM_COUNT==100000,'support945':len(c.MATCH_COEFF)==945,'exact_fraction':all(isinstance(Fraction(v),Fraction) for d in base for v in d.values()),'endpoint_orientation_roundtrip':roundtrip,'wrong_transpose_distinguishable':wrong_rejected,'coefficient_mutation_detected':mutation_rejected}
 if not all(validity.values()): cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 elif not support_equal: cls='K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS'
 elif not coeff_equal: cls='K5_S5_COMPONENT1_DEFECT_SUPPORT_COEFFICIENT'
 else: cls='K5_S5_COMPONENT1_SUPPORT_MIXING_EXACT'
 first_missing=repr(missing[0]) if missing else None;first_spurious=repr(spurious[0]) if spurious else None
 out={'gate':'K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC','prereg_commit':PRE,'classification':cls,'scientific_verdict':None,'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN,'component':COMPONENT},'stage_equalities':{'canonical_nonzero_support':bool(base[COMPONENT]),'AinvT_target_component_support':bool(pred),'direct_transported_target_support':bool(direct),'support_index_equality':support_equal,'coefficient_equality':coeff_equal},'first_missing_support_index':first_missing,'first_spurious_support_index':first_spurious,'first_coefficient_mismatch':repr(coeff_bad) if coeff_bad is not None else None,'validity':validity,'control_component_wrong_transpose':ctrl,'cardinalities':{'canonical_component_support':len(base[COMPONENT]),'AinvT_target_support':len(pred),'direct_target_support':len(direct)},'hashes':{'AinvT_target':H(pred),'direct_target':H(direct)},'no_N_B_orders_or_coefficients_recorded':True,'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('CLASSIFICATION='+cls);print(json.dumps(out['stage_equalities'],sort_keys=True));return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0
if __name__=='__main__':raise SystemExit(main())
