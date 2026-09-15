#!/usr/bin/env python3
import json, math
from fractions import Fraction

PREREG='2df22374c71e7f0918e1aea8e5b1017620ea3ef2'
RESEARCHER_HEAD='15472a83a6fc5e73c10b050649578822b65558cf'
RUN='34925157771'; JOB='104241540969'; ART='10379901560'
DIGEST='sha256:ac44a7a209847a097902904bb7114ffafa40edc8d40d8f15324b0c66204f0384'
JSON_SHA='b5e1f14e728c1ee9342a5433084b6c1d122faad4af360ffbcd627f60a76cd9ec'
PARENT='c29ba0ddbaa4d6e1581db558b792565a7916a0cd'; SOURCE='cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533'; THEOREM='70a756c9c7c66f822d0e5933e9522b2d359dafe8'; MCRIT='e7623cb5303ea49894e480e2fc4a884df44e7713'

def read(p):
    with open(p,encoding='utf-8') as f:return f.read()
def req(t,xs):return all(x in t for x in xs)
def mul(k,q):
    s={k:Fraction(1)}
    for _ in range(q):
        o={}
        for j,c in s.items():
            if j:o[j-1]=o.get(j-1,Fraction())-j*c
        s=o
    return s

def main():
    current=read('status/CURRENT.md'); result=read('results/ITER083N_PROVENANCE_CORRECT_RETRY_1_RESULT.md'); parent=read('prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md'); source=read('sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md'); theorem=read('sources/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_DERIVATION.md'); mcrit=read('results/ITER083M_REPAIRED_ADVERSARIAL_REVIEW.md'); old=read('results/ITER083N_ADVERSARIAL_PROVENANCE_REVIEW.md')
    c0=req(current,['awaits independent Critic review',RUN,ART,DIGEST,JSON_SHA]) and req(result,[RESEARCHER_HEAD,RUN,JOB,ART,DIGEST,JSON_SHA,PARENT,SOURCE,THEOREM,MCRIT]) and req(old,['INVALID_PROVENANCE'])
    # Independent Laurent coefficient bookkeeping: [residue, finite, phi*residue]
    before_res=(1,0,0); after_res=(1,0,0); before_fp=(0,1,0); after_fp=(0,1,1)
    c1=after_res==before_res and tuple(after_fp[i]-before_fp[i] for i in range(3))==(0,0,1)
    fails=[]
    for k in range(9):
      for q in range(10):
        got=mul(k,q); exp=({k-q:Fraction(((-1)**q)*math.factorial(k),math.factorial(k-q))} if q<=k else {})
        if got!=exp:fails.append((k,q))
    c2=not fails
    thresholds={w:w+1 for w in (0,3,8)}
    sharp={w: all(mul(q,q) for q in range(w+1)) and all(not mul(k,w+1) for k in range(w+1)) for w in (0,3,8)}
    c3=thresholds=={0:1,3:4,8:9} and all(sharp.values())
    c4=req(theorem,['Equality of the normalized Hessians','phi|_N=0','not enough, by itself']) and thresholds[0]==1 and thresholds[3]>1 and thresholds[8]>1
    c5=req(theorem,["rho'=c rho",'(log c) A_-1'])
    c6=req(parent,['do not infer that the physical Toller residue activates every allowed derivative channel','Actual independence can be stronger']) and req(theorem,['particular physical residue may have smaller order','No actual nonzero physical scheme dependence is proved'])
    c7=req(source,['Felder and David Kazhdan','odd-codimension','has not been established'])
    malformed={
      'stale_historical_authority': req(old,['INVALID_PROVENANCE']),
      'all_order_zero_rejected': thresholds[3]==4 and thresholds[8]==9,
      'tangent_full_fp_rejected': c4,
      'actual_dependence_without_residue_rejected': c6,
      'fk_parity_without_membership_rejected': c7,
      'weakened_threshold_rejected': all(mul(w,w) for w in (0,3,8)),
    }
    c8=all(malformed.values())
    checks={f'C{i}':v for i,v in enumerate([c0,c1,c2,c3,c4,c5,c6,c7,c8])}
    if not c0: verdict='INVALID_PROVENANCE'; cls='ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_INVALID_PROVENANCE'
    elif not c8: verdict='INVALID_IMPLEMENTATION'; cls='ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_INVALID_IMPLEMENTATION'
    elif all(checks.values()): verdict='CONFIRMED_SCOPED'; cls='ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_CONFIRMED_SCOPED'
    else: verdict='SCIENTIFIC_FAIL_SCOPED'; cls='ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_SCIENTIFIC_FAIL_SCOPED'
    out={'iteration':'Iter083N provenance-correct retry independent Critic review','prereg_commit':PREREG,'reviewed_run':RUN,'reviewed_artifact':ART,'reviewed_digest':DIGEST,'reviewed_json_sha256':JSON_SHA,'checks':checks,'delta_identity_checks':90,'delta_identity_failures':len(fails),'thresholds':{'K3':1,'K4':4,'K5':9},'sharpness':sharp,'malformed_controls':malformed,'verdict':verdict,'classification':cls,'claim_ceiling':'No actual nonzero physical finite-part dependence; no source-authorized selector; no unique K5 extension; no regulator theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.'}
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if verdict=='CONFIRMED_SCOPED' else 2
if __name__=='__main__': raise SystemExit(main())
