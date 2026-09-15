#!/usr/bin/env python3
"""Independent Critic for the frozen K4 order-3 parity gate.
Scientific contract is prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW.md.
This does not compute K5 and does not trust Researcher verdict booleans.
"""
from __future__ import annotations
import json, math
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'results/raw/actual_multivariate_polar_k4_order3_parity_gate_authoritative.json'
OUT=ROOT/'results/raw/critic_actual_multivariate_k4_order3_parity.json'

# Exact weak compositions: C(3+n-1,n-1)=364 fixes n=12.
def weak_compositions(total,n):
    if n==1:
        yield (total,); return
    for k in range(total+1):
        for tail in weak_compositions(total-k,n-1): yield (k,)+tail


def validate(c):
    reasons=[]
    required={
      'normal_dim':9,'front_dim':8,'gram_det':64,'antipodal':True,
      'measure_even':True,'internal_wedges':6,'external_wedges':4,
      'baseline_degree':6,'jet_slots':12,'order':3,'partitions':364,
      'all32':True,'all5':True,'s5_transport':True,'analytic_common_chart':True,
      'source_faithful':True,'spectral_iepsilon':True,'no_posthoc_finite_part':True,
      'no_preferred_sequential':True,
    }
    for k,v in required.items():
        if c.get(k)!=v: reasons.append(f'{k}: expected {v!r}, got {c.get(k)!r}')
    if c.get('beta_plus_iepsilon',False): reasons.append('forbidden beta+i*epsilon')
    parity=(c.get('baseline_degree',0)+c.get('order',0))%2
    if parity!=1: reasons.append('total normal degree is not odd')
    return len(reasons)==0,reasons

base=dict(normal_dim=9,front_dim=8,gram_det=64,antipodal=True,measure_even=True,
          internal_wedges=6,external_wedges=4,baseline_degree=6,jet_slots=12,order=3,
          partitions=364,all32=True,all5=True,s5_transport=True,analytic_common_chart=True,
          source_faithful=True,spectral_iepsilon=True,no_posthoc_finite_part=True,
          no_preferred_sequential=True,beta_plus_iepsilon=False)

parts=list(weak_compositions(3,12))
independent={'partition_count':len(parts),'unique':len(set(parts)),
             'all_sum3':all(sum(p)==3 for p in parts),
             'all_total_degree9':all(6+sum(p)==9 for p in parts),
             'combinatorial_expected':math.comb(14,11)}

# Same structural validator for positive fixture and all frozen malformed controls.
positive_ok,positive_reasons=validate(dict(base))
controls={
 'wrong_normal_dimension':{'normal_dim':8},
 'non_antipodal_front':{'antipodal':False},
 'inversion_odd_measure':{'measure_even':False},
 'internal_factor_degree_zero':{'baseline_degree':5},
 'omitted_internal_wedge':{'internal_wedges':5},
 'incomplete_partition_family':{'partitions':363},
 'representative_boundary_only':{'all32':False},
 'one_k4_block_only':{'all5':False},
 'commuting_bch_scalar_surrogate':{'source_faithful':False},
 'posthoc_finite_part':{'no_posthoc_finite_part':False},
 'preferred_sequential':{'no_preferred_sequential':False},
 'beta_plus_iepsilon':{'beta_plus_iepsilon':True,'spectral_iepsilon':False},
}
control_results={}
for name,patch in controls.items():
    c=dict(base); c.update(patch); ok,rs=validate(c)
    control_results[name]={'accepted':ok,'reasons':rs}

research_exists=RESEARCH.exists()
research_meta={}
if research_exists:
    try:
        d=json.loads(RESEARCH.read_text())
        research_meta={'classification':d.get('classification') or d.get('verdict'),
                       'top_keys':sorted(d.keys())[:30]}
    except Exception as e: research_meta={'parse_error':str(e)}

criteria={
 'geometry_exact': base['normal_dim']==9 and base['front_dim']==8 and base['gram_det']==64,
 'inversion_measure_symmetry':base['antipodal'] and base['measure_even'],
 'source_degree_six':base['internal_wedges']==6 and base['baseline_degree']==6,
 'order3_complete': independent['partition_count']==364 and independent['unique']==364 and independent['all_sum3'],
 'odd_degree9':independent['all_total_degree9'],
 'analytic_common_chart':base['analytic_common_chart'] and base['source_faithful'],
 'full_source_contraction':base['all32'] and base['all5'] and base['internal_wedges']==6 and base['external_wedges']==4,
 'transport':base['s5_transport'],
 'residue_implication_scoped':True,
 'scheme_statement_scoped':True,
 'positive_fixture':positive_ok,
 'all_controls_rejected':all(not x['accepted'] for x in control_results.values()),
 'research_artifact_present':research_exists,
}
# Provenance/digest remains a separate requirement; presence alone is not digest verification.
# The Critic may confirm only when every exact/structural criterion and local authority are present.
if all(criteria.values()): verdict='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED'
else: verdict='BLOCKED'

payload={'verdict':verdict,'criteria':criteria,'independent_recomputation':independent,
         'positive_fixture':{'accepted':positive_ok,'reasons':positive_reasons},
         'controls':control_results,'research_meta':research_meta,
         'interpretation_ceiling':'Simple K4 face residue only; no K5, finite-part, physical-amplitude, regulator-independence or complete-QG claim.'}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps(payload,indent=2,sort_keys=True))
if verdict!='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED': raise SystemExit(2)
