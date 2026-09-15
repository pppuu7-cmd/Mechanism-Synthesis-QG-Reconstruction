#!/usr/bin/env python3
"""Control-only repair 3: enforce consistency of independently recomputed baseline degree."""
from __future__ import annotations
import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
R2=ROOT/'scripts/critic_actual_multivariate_k4_order3_parity_repair2.py'
OUT=ROOT/'results/raw/critic_actual_multivariate_k4_order3_parity.json'
spec=importlib.util.spec_from_file_location('repair2',R2)
r2=importlib.util.module_from_spec(spec);spec.loader.exec_module(r2)
orig_validate=r2.m.validate
orig_provenance=r2.durable_provenance
REPAIR3='a4c735f1c6d1f5323b9b88e2026aa779a57639f5'

def validate3(e):
    ok,reasons=orig_validate(e)
    if e.get('recomputed'):
        source_baseline=e['source_degree'].get('baseline_degree')
        scaling_baseline=e['scaling'].get('baseline_degree')
        if not (source_baseline==scaling_baseline==6):
            reasons=list(reasons)+['SOURCE_SCALING_BASELINE_INCONSISTENCY']
    return not reasons,reasons

def provenance3():
    p=orig_provenance()
    p['ancestry']['repair3_prereg_in_history']=r2.m.ancestor(REPAIR3)
    p['ok']=all(p['fields'].values()) and all(p['ancestry'].values())
    return p

# The base malformed-control harness resolves its global validate symbol at runtime.
r2.m.validate=validate3
r2.durable_provenance=provenance3

def main():
    e=r2.repair_evidence(r2.m.evidence())
    ok,reasons=validate3(e)
    ctrl=r2.m.controls(e);ctrlok=all(v['rejected'] for v in ctrl.values())
    if not ctrlok:verdict='INVALID_IMPLEMENTATION'
    elif not e['provenance']['ok']:verdict='INVALID_PROVENANCE'
    elif ok:verdict='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED'
    else:verdict='SCIENTIFIC_FAIL_SCOPED'
    out={'gate':'ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW','repair':3,'verdict':verdict,
      'scientific_ok':ok,'scientific_reasons':reasons,'controls_ok':ctrlok,'controls':ctrl,'evidence':e,
      'parent_prereg':r2.m.PARENT,'repair1_prereg':r2.m.REPAIR,
      'repair2_prereg':'3a3516f799dd70c6a41b6ec84790d27683d64c40','repair3_prereg':REPAIR3,
      'next_gate_authorized':verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED',
      'interpretation_ceiling':'Simple K4 face residue only; no K5 order8, finite-part, physical amplitude, regulator independence, F9/G3, new physics or complete-QG claim.'}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':verdict,'scientific_ok':ok,'reasons':reasons,'controls_ok':ctrlok,
      'failed_controls':[k for k,v in ctrl.items() if not v['rejected']],
      'partition_count':e['partitions']['count'],'raw_terms':e['full_source']['total_raw_terms'],
      's5_failures':e['full_source']['s5_transport_failures'],'provenance_ok':e['provenance']['ok']},indent=2,sort_keys=True))
    return 0 if verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED' else 2
if __name__=='__main__':raise SystemExit(main())
