#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def t(p): return (R/p).read_text(encoding='utf-8')
def r4():
 g=t('results/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md'); h=t('results/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md'); f=t('docs/DSIR_TO_POLYGON_FUNNEL_V0_4.md')
 c={'G_correct':'ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED' in g,
    'H_pass':'ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED' in h,
    'epsilon_independent':'delta-prime coefficient is independent of finite `epsilon>0`' in h,
    'census':'1024/1024' in h and 'nonzero leading coefficient' in h,
    'not_mollifier':'does not act as a coordinate-space mollifier' in h,
    'K5_blocked':'Status: `BLOCKED_TRANSFER_TO_POLYGON`' in f,
    'missing':'SOURCE_ORDERED_TOLLER_FUNCTION_K5_COLLISION_BOUNDARY_VALUE_WITH_FULL_BOUNDARY_CONTRACTION' in f,
    'ordering':'one-wedge spectral/spinor integration -> Toller function -> K5 product/group integration' in f,
    'no_interchange':'do not interchange the source order' in f}
 return {'audit':'DSIR-V4','lane':'R4','valid':all(c.values()),'checks':c}
def s4():
 f=t('docs/DSIR_TO_POLYGON_FUNNEL_V0_4.md'); c={'g3':'CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION' in f,'blocked':'## G3 handoff\n\nStatus: `BLOCKED_TRANSFER_TO_POLYGON`.' in f}; return {'audit':'DSIR-V4','lane':'S4','valid':all(c.values()),'checks':c}
def t4():
 f=t('docs/DSIR_TO_POLYGON_FUNNEL_V0_4.md'); c={'f9':'PHYSICAL_MULTISCALE_CCI_REALIZATION' in f,'blocked':'## F9/RG handoff\n\nStatus: `BLOCKED_TRANSFER_TO_POLYGON`.' in f,'downstream':'G4-G7 remain downstream' in f and 'G8 remains `CONVERGENCE_ONLY`' in f}; return {'audit':'DSIR-V4','lane':'T4','valid':all(c.values()),'checks':c}
def u4():
 h=t('results/ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE_RESULT.md'); v3=t('results/DSIR_TERMINAL_HANDOFF_V3_CORRECTED_RESULT.md'); sup=t('status/DSIR_V2_CONTACT_FORMULA_SUPERSESSION.md'); f=t('docs/DSIR_TO_POLYGON_FUNNEL_V0_4.md'); pre=t('prereg/DSIR_TERMINAL_HANDOFF_V4_SOURCE_ORDERING_REFRESH.md')
 c={'v2_quarantine':'SUPERSEDED_PRE_ERRATUM' in sup,'v3_correct':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V3_CONTACT_FORMULA_CORRECTED' in v3,'H_authority':'prospective preregistration' in h and 'authoritative run' in h and 'All frozen lanes A/B/C/D and aggregate passed.' in h,'siblings':'Neither is a physical source-amplitude pushforward theorem.' in f,'iepsilon':'published spectral `i epsilon`' in f,'locks':'no physical source-to-K4 pushforward' in f.lower() and 'no nominal epsilon^-1 coefficient' in f.lower(),'frozen':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V4_SOURCE_ORDERING_REFINED' in pre}
 return {'audit':'DSIR-V4','lane':'U4','valid':all(c.values()),'checks':c}
L={'R4':r4,'S4':s4,'T4':t4,'U4':u4}
def w(o,p): q=Path(p);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(o,indent=2,sort_keys=True),encoding='utf-8')
def agg(root):
 d={}
 for b,_,fs in os.walk(root):
  for fn in fs:
   if fn.endswith('.json'):
    try:o=json.loads(Path(b,fn).read_text())
    except:continue
    if o.get('audit')=='DSIR-V4' and o.get('lane') in L:d[o['lane']]=o
 v=set(d)==set(L) and all(d[k].get('valid') for k in L)
 return {'audit':'DSIR-V4','valid':bool(v),'classification':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V4_SOURCE_ORDERING_REFINED' if v else 'DSIR_TERMINAL_HANDOFF_V4_SOURCE_ORDERING_REFRESH_INCOMPLETE','contract_completeness_percent':100 if v else None,'meaning':'100% handoff-contract/interface completeness only; no physical gate promotion.' if v else 'Inspect failed frozen predicate.','lane_valid':{k:bool(d.get(k,{}).get('valid')) for k in L},'K5_status':'BLOCKED_TRANSFER_TO_POLYGON' if v else None,'K5_missing_object':'SOURCE_ORDERED_TOLLER_FUNCTION_K5_COLLISION_BOUNDARY_VALUE_WITH_FULL_BOUNDARY_CONTRACTION' if v else None,'G3_status':'BLOCKED_TRANSFER_TO_POLYGON' if v else None,'F9_status':'BLOCKED_TRANSFER_TO_POLYGON' if v else None,'G8_status':'CONVERGENCE_ONLY' if v else None}
def main():
 a=argparse.ArgumentParser();a.add_argument('--lane',choices=L);a.add_argument('--aggregate-dir');a.add_argument('--output',required=True);x=a.parse_args();o=L[x.lane]() if x.lane else agg(x.aggregate_dir);print(json.dumps(o,indent=2,sort_keys=True));w(o,x.output);raise SystemExit(0 if o.get('valid') else 1)
if __name__=='__main__':main()
