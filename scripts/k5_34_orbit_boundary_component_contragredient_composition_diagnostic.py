#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
PREPATH=ROOT/'prereg/K5_34_ORBIT_BOUNDARY_COMPONENT_CONTRAGREDIENT_COMPOSITION_DIAGNOSTIC.md'
PRE='bc263cc34fe38a68ef817b49a41b5ee7da7b9999'
FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m
c=load(CORE,'bcdiag_core');s5=c.s5;P=s5.C
def H(x):return hashlib.sha256(repr(x).encode()).hexdigest()
def one(v,i):return [v[j] if j==i else {} for j in range(32)]
def cf(mc):return mc.get(FROZEN)
def project(v):return c._project_pattern_dicts_to_match_coeff(v)
def eqv(a,b):return len(a)==len(b) and all(x==y for x,y in zip(a,b))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 base=c._BASE_PATTERNS;target=[]
 # Explicit target-label transport, independent of helper pullback convention.
 g=s5.orientation_character(P)
 from collections import defaultdict
 for d in base:
  z=defaultdict(Fraction)
  for types,coef in d.items():
   out=[None]*10
   for old in range(10):
    j=s5.ep(P,old);t=types[old]
    if s5.edge_sign(P,old)==-1:t=(t[1],t[0])
    out[j]=t
   z[tuple(out)]+=g*Fraction(coef)
  target.append({k:v for k,v in z.items() if v})
 tensors=s5.act.reach.local_tensor_vectors(s5.act.src);local=s5.act.reach.local_action_matrices(tensors)
 A=s5.boundary_matrix(P,local);Ai=s5.boundary_matrix(s5.invperm(P),local);ATi=s5.transpose(Ai)
 predicted=s5.transform_dictvec(ATi,base)
 # Stage 1: independent theorem-level component mixing before invariant-dual contraction.
 support_mix=eqv(target,predicted)
 # Deliberately wrong row/column convention: A^{-1}, not A^{-T}.
 wrong=s5.transform_dictvec(Ai,base);wrong_rejected=not eqv(target,wrong)
 index_ok=support_mix and wrong_rejected
 # Stage 2: compare invariant-dual projection component by component on frozen matching.
 tgt_parts=[cf(project(one(target,i))) for i in range(32)]
 pred_parts=[cf(project(one(predicted,i))) for i in range(32)]
 weight_ok=tgt_parts==pred_parts
 # Stage 3: source coefficient dictionaries themselves must agree under the established law.
 source_ok=eqv(target,predicted)
 per_component_ok=tgt_parts==pred_parts
 full_t=project(target);full_p=project(predicted);final_ok=cf(full_t)==cf(full_p)
 preimages=sum(1 for mt in c.MATCH_COEFF if c.s5.ep(P,0)>=0 and __import__('builtins')) # overwritten below
 # Unique frozen matching preimage under edge permutation.
 def pm(mt):
  q=[]
  for i,j in mt:
   x,y=s5.ep(P,i),s5.ep(P,j);q.append((min(x,y),max(x,y)))
  return tuple(sorted(q))
 preimages=sum(1 for mt in c.MATCH_COEFF if pm(mt)==FROZEN)
 # Mandatory component-coefficient mutation.
 mutated=list(pred_parts)
 if mutated[0] is None: mutated[0]=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(0)))
 else:
  q=[list(x) for x in mutated[0]];q[0][0]+=1;mutated[0]=(tuple(q[0]),tuple(q[1]))
 mutation_rejected=mutated!=tgt_parts
 validity={'prereg_locked':PRE=='bc263cc34fe38a68ef817b49a41b5ee7da7b9999' and 'boundary-component contragredient composition diagnostic' in PREPATH.read_text(),'full32':len(base)==len(target)==32,'source100000':c._SOURCE_TERM_COUNT==100000,'support945':len(full_t)==len(full_p)==945,'exact_fraction':all(isinstance(x,Fraction) for mc in (full_t,full_p) for v in mc.values() for ch in v for x in ch),'unique_matching_preimage':preimages==1,'wrong_contragredient_rejected':wrong_rejected,'component_mutation_rejected':mutation_rejected}
 if not all(validity.values()):cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 elif not support_mix:cls='K5_S5_BOUNDARY_DEFECT_COMPONENT_SUPPORT_MIXING'
 elif not index_ok:cls='K5_S5_BOUNDARY_DEFECT_CONTRAGREDIENT_INDEX_CONVENTION'
 elif not weight_ok:cls='K5_S5_BOUNDARY_DEFECT_INVARIANT_DUAL_WEIGHT'
 elif not source_ok:cls='K5_S5_BOUNDARY_DEFECT_TRANSPORTED_SOURCE_COEFFICIENT'
 elif not per_component_ok:cls='K5_S5_BOUNDARY_DEFECT_PER_COMPONENT_PREWICK'
 elif not final_ok:cls='K5_S5_BOUNDARY_DEFECT_FINAL_32_CONTRACTION'
 else:cls='K5_S5_BOUNDARY_COMPONENT_COMPOSITION_NO_DEFECT_ON_FROZEN_LANE'
 first=next((i for i,(x,y) in enumerate(zip(tgt_parts,pred_parts)) if x!=y),None)
 out={'gate':'K5_34_ORBIT_BOUNDARY_COMPONENT_CONTRAGREDIENT_COMPOSITION_DIAGNOSTIC','prereg_commit':PRE,'classification':cls,'scientific_verdict':None,'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN},'stage_equalities':{'component_support_mixing':support_mix,'contragredient_index_convention':index_ok,'invariant_dual_weight':weight_ok,'transported_source_coefficient':source_ok,'per_component_prewick':per_component_ok,'final_32_contraction':final_ok},'first_mismatch_component':first,'validity':validity,'hashes':{'target_dictvec':s5.dictvec_hash(target),'predicted_AinvT_dictvec':s5.dictvec_hash(predicted),'wrong_Ainv_dictvec':s5.dictvec_hash(wrong),'target_parts':H(tgt_parts),'predicted_parts':H(pred_parts)},'no_N_B_orders_or_coefficients_recorded':True,'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('CLASSIFICATION='+cls);print(json.dumps(out['stage_equalities'],sort_keys=True));return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0
if __name__=='__main__':raise SystemExit(main())
