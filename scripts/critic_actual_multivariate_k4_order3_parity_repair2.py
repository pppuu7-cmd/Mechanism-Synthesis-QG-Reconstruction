#!/usr/bin/env python3
"""Control-only repair 2 for the independent K4 order-3 parity Critic."""
from __future__ import annotations
import importlib.util, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/critic_actual_multivariate_k4_order3_parity.py'
OUT=ROOT/'results/raw/critic_actual_multivariate_k4_order3_parity.json'
spec=importlib.util.spec_from_file_location('basecritic',BASE)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def durable_provenance():
    a=json.loads(m.PATH['aggregate'].read_text())
    fields={
      'run':a.get('authoritative_run')==m.RESEARCH_RUN,
      'head':a.get('head')==m.RESEARCH_HEAD,
      'artifact':a.get('artifact_id')==m.RESEARCH_ARTIFACT,
      'zip':a.get('artifact_zip_sha256')==m.RESEARCH_ZIP,
      'json':a.get('production_json_sha256')==m.RESEARCH_JSON,
      'invalid_runs_quarantined_in_aggregate':a.get('historical_invalid_implementation_runs')==m.INVALID_RUNS,
    }
    ancestry={
      'research_prereg_before_head':m.ancestor(m.RESEARCH_PREREG,m.RESEARCH_HEAD),
      'research_head_in_history':m.ancestor(m.RESEARCH_HEAD),
      'parent_critic_prereg_in_history':m.ancestor(m.PARENT),
      'repair1_prereg_in_history':m.ancestor(m.REPAIR),
      'repair2_prereg_in_history':m.ancestor('3a3516f799dd70c6a41b6ec84790d27683d64c40'),
    }
    return {'fields':fields,'ancestry':ancestry,'ok':all(fields.values()) and all(ancestry.values())}

def repair_evidence(e):
    # Derive the frozen grouping structurally: six internal Toller factors,
    # four external Toller factors, one Haar factor and one smooth joint q-family factor.
    internal=e['full_source']['internal_counts'][0]
    external=e['full_source']['external_counts'][0]
    slots=internal+external+1+1
    order=e['scaling']['omega']
    parts=list(m.weak(order,slots))
    e['partitions']={
      'slot_derivation':f'{internal}+{external}+1+1',
      'slots':slots,'order':order,'count':len(parts),'unique':len(set(parts)),
      'all_sum':all(sum(x)==order for x in parts),
      'total_degree_set':sorted({e['source_degree']['baseline_degree']+sum(x) for x in parts}),
      'stars_bars':math.comb(order+slots-1,slots-1),
      'regrouped_slots':internal+external+1+16,
    }
    rs=e['partitions']['regrouped_slots']
    e['partitions']['regrouped_count']=math.comb(order+rs-1,rs-1)
    e['partitions']['regrouped_total_degree']=e['source_degree']['baseline_degree']+order
    e['partitions']['regrouping_odd']=e['partitions']['regrouped_total_degree']%2==1
    e['provenance']=durable_provenance()
    e['residue_odd_pairing']=(e['partitions']['total_degree_set']==[9] and e['geometry']['inversion_preserves_gram'] and
      e['geometry']['positive_measure_even'] and e['geometry']['antipodal_front'] and e['common_chart_authority'])
    return e

def main():
    e=repair_evidence(m.evidence())
    ok,reasons=m.validate(e)
    ctrl=m.controls(e);ctrlok=all(v['rejected'] for v in ctrl.values())
    if not ctrlok:verdict='INVALID_IMPLEMENTATION'
    elif not e['provenance']['ok']:verdict='INVALID_PROVENANCE'
    elif ok:verdict='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED'
    else:verdict='SCIENTIFIC_FAIL_SCOPED'
    out={'gate':'ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW','repair':2,'verdict':verdict,
      'scientific_ok':ok,'scientific_reasons':reasons,'controls_ok':ctrlok,'controls':ctrl,'evidence':e,
      'parent_prereg':m.PARENT,'repair1_prereg':m.REPAIR,'repair2_prereg':'3a3516f799dd70c6a41b6ec84790d27683d64c40',
      'next_gate_authorized':verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED',
      'interpretation_ceiling':'Simple K4 face residue only; no K5 order8, finite-part, physical amplitude, regulator independence, F9/G3, new physics or complete-QG claim.'}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':verdict,'scientific_ok':ok,'reasons':reasons,'controls_ok':ctrlok,
      'partition_count':e['partitions']['count'],'regrouped_partition_count':e['partitions']['regrouped_count'],
      'raw_terms':e['full_source']['total_raw_terms'],'s5_failures':e['full_source']['s5_transport_failures'],
      'provenance_ok':e['provenance']['ok']},indent=2,sort_keys=True))
    return 0 if verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED' else 2
if __name__=='__main__':raise SystemExit(main())
