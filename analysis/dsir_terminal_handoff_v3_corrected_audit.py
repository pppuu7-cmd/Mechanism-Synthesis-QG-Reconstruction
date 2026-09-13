#!/usr/bin/env python3
"""Corrected DSIR terminal handoff V3 audit."""
from __future__ import annotations
import argparse, json, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def txt(p): return (ROOT/p).read_text(encoding='utf-8')

def lane_r3():
    err=txt('status/ITER077_CONTACT_FORMULA_ERRATUM.md')
    sup=txt('status/DSIR_V2_CONTACT_FORMULA_SUPERSESSION.md')
    g=txt('results/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md')
    a=txt('results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md')
    c=txt('results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md')
    f=txt('docs/DSIR_TO_POLYGON_FUNNEL_V0_3.md')
    checks={
      'EF_quarantined':'NON_AUTHORITATIVE_SOURCE_LOCK_INVALID' in err,
      'V2_superseded':'SUPERSEDED_PRE_ERRATUM' in sup,
      'correct_contact':'delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta\'(x)' in g,
      'rank10':'rank 10' in a.lower() or 'rank `10`' in a,
      'rank9':'xxxxxyyyzz' in c and 'codimension' in c,
      'G_class':'ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED' in g,
      'cubic':'P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2(gamma-t)' in g,
      'neff3':'`n_eff=3`' in g,
      'sd8':'| 3 | 8 |' in g,
      'not_nonexistence':'not** a theorem' in g or 'not** a theorem' in g.replace(' ',''),
      'K5_blocked':'`BLOCKED_TRANSFER_TO_POLYGON`' in f,
      'local_missing':'SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL' in f,
      'broad_missing':'SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' in f,
      'no_arbitrary':'forbid arbitrary finite parts' in f.lower() or 'no arbitrary finite part' in f.lower(),
    }
    return {'audit':'DSIR-V3','lane':'R3','valid':all(checks.values()),'checks':checks}

def lane_s3():
    f=txt('docs/DSIR_TO_POLYGON_FUNNEL_V0_3.md')
    checks={'G3_blocked':'CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION' in f and '`BLOCKED_TRANSFER_TO_POLYGON`' in f,
            'no_novelty_copy':'may not be silently copied as a novelty kernel' in f}
    return {'audit':'DSIR-V3','lane':'S3','valid':all(checks.values()),'checks':checks}

def lane_t3():
    f=txt('docs/DSIR_TO_POLYGON_FUNNEL_V0_3.md')
    checks={'F9_blocked':'PHYSICAL_MULTISCALE_CCI_REALIZATION' in f,
            'cci':'multi-step cylindrical consistency/CCI' in f,
            'toller':'closure of the Toller analytic/pole class' in f,
            'G4G8':'G4-G7 remain downstream' in f and 'G8 remains `CONVERGENCE_ONLY`' in f}
    return {'audit':'DSIR-V3','lane':'T3','valid':all(checks.values()),'checks':checks}

def lane_u3():
    led=txt('status/ITER077_PROVENANCE_LEDGER_V2.md'); err=txt('status/ITER077_CONTACT_FORMULA_ERRATUM.md'); sup=txt('status/DSIR_V2_CONTACT_FORMULA_SUPERSESSION.md'); g=txt('results/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md'); f=txt('docs/DSIR_TO_POLYGON_FUNNEL_V0_3.md'); pre=txt('prereg/DSIR_TERMINAL_HANDOFF_V3_CONTACT_ERRATUM_CORRECTED.md')
    checks={
      'G_authority':'Iter077G-SM' in led and 'authoritative corrected contact' in led.lower(),
      'EF_quarantine':'quarantined historical contact gates' in led.lower() and 'NON_AUTHORITATIVE_SOURCE_LOCK_INVALID' in err,
      'V2_quarantine':'SUPERSEDED_PRE_ERRATUM' in sup,
      'G_prereg':'prospective preregistration' in g and 'authoritative run' in g,
      'G_pass':'All frozen lanes A/B/C/D and aggregate passed.' in g,
      'scope_split':'Neither sibling is a physical source-amplitude/K4 pushforward theorem.' in led,
      'iepsilon':'published spectral `i epsilon`' in f,
      'no_pushforward':'not a physical coherent-spinor/Toller source-to-K4 pushforward theorem' in f,
      'no_epsilon':'no nominal epsilon^-1 coefficient' in f,
      'V3_frozen':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V3_CONTACT_FORMULA_CORRECTED' in pre,
    }
    return {'audit':'DSIR-V3','lane':'U3','valid':all(checks.values()),'checks':checks}
LANES={'R3':lane_r3,'S3':lane_s3,'T3':lane_t3,'U3':lane_u3}
def write(o,p):
    q=Path(p); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(json.dumps(o,indent=2,sort_keys=True),encoding='utf-8')
def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
      for fn in files:
        if fn.endswith('.json'):
          try:o=json.loads(Path(base,fn).read_text(encoding='utf-8'))
          except Exception:continue
          if o.get('audit')=='DSIR-V3' and o.get('lane') in LANES:got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('valid') for k in LANES)
    return {'audit':'DSIR-V3','valid':bool(valid),'classification':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V3_CONTACT_FORMULA_CORRECTED' if valid else 'DSIR_TERMINAL_HANDOFF_V3_CORRECTION_INCOMPLETE','contract_completeness_percent':100 if valid else None,'meaning':'100% handoff-contract/interface completeness only; no physical gate promotion.' if valid else 'Inspect failed frozen predicate.','lane_valid':{k:bool(got.get(k,{}).get('valid')) for k in LANES},'lanes_found':sorted(got),'K5_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,'K5_missing_object':'SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' if valid else None,'local_missing_object':'SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL' if valid else None,'G3_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,'F9_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,'G8_status':'CONVERGENCE_ONLY' if valid else None}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose one')
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir); print(json.dumps(o,indent=2,sort_keys=True)); write(o,a.output)
    if not o.get('valid'): raise SystemExit(1)
if __name__=='__main__': main()
