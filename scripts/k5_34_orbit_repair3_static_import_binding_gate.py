#!/usr/bin/env python3
from __future__ import annotations
# Frozen implementation-only gate; this comment intentionally triggers its workflow.
import importlib.util,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHARD=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_shard_repair3.py'
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py'
PREREG=ROOT/'prereg/K5_34_ORBIT_REPAIR3_STATIC_IMPORT_BINDING_GATE.md'
PREFLIGHT=ROOT/'results/raw/k5_34_orbit_matching_key_frame_repair3_preflight_control_repair1.json'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);assert spec.loader is not None;spec.loader.exec_module(m);return m

def main():
    checks={}
    checks['prereg_present']=PREREG.exists() and 'PASS_REPAIR3_STATIC_IMPORT_BINDING' in PREREG.read_text()
    shard_text=SHARD.read_text();core_text=CORE.read_text()
    checks['production_shard_exists']=SHARD.exists()
    checks['production_imports_repair3_core']="k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py" in shard_text
    checks['production_no_repair2_core_import']="core_repair2.py" not in shard_text
    checks['production_uses_bound_target_symbol']='c.S5_MATCH_COEFF_CYCLE)' in shard_text
    checks['core_alias_is_target']='S5_MATCH_COEFF_CYCLE = S5_MATCH_COEFF_CYCLE_TARGET' in core_text
    checks['core_builds_target_by_forward_map']='tmt = forward_matching(mt)' in core_text
    checks['no_direct_pullback_target_alias']='S5_MATCH_COEFF_CYCLE = S5_MATCH_COEFF_CYCLE_PULLBACK' not in core_text
    try:
        shard=load(SHARD,'repair3_prod_shard_static');c=shard.c
        st=c.static_checks()
        required=['canonical_matching_count_945','pullback_matching_count_945','target_matching_count_945','forward_map_bijection_all945','forward_inverse_roundtrip_all945','coefficient_multiset_preserved','all_coefficients_exact_fraction','target_pushforward_relation_all945','source_terms_100000']
        checks['import_success']=True
        checks['repair3_static_required_all_true']=all(st.get(k) is True for k in required)
        checks['matching_count_945']=len(c.MATCH_COEFF)==945 and len(c.S5_MATCH_COEFF_CYCLE)==945
        checks['proper_orbit_count_32']=len(c.proper_orbits())==32
        checks['channel_orbit_rows_64']=2*len(c.proper_orbits())==64
        checks['degree_N_27']=c.N_DEG==27
        checks['degree_B_31']=c.B_DEG==31
        checks['two_invariant_dual_channels']=len(c.W1)==2 and len(c.W2)==2
        checks['W1_W2_present']=c.W1 is not None and c.W2 is not None
        checks['exact_fraction_coefficients']=st.get('all_coefficients_exact_fraction') is True
        checks['q18_not_on_production_path']='q18' not in shard_text.lower() and 'q18' not in core_text.lower().replace("'q18_values_used': false",'')
        parent_prereg=(ROOT/'prereg/K5_34_ORBIT_REPAIR3_RESEARCHER_OUTCOME_BLIND_POSTPREFLIGHT_PRODUCTION_CONTRACT.md').read_text()
        checks['U_authority_5_locked']='N=27, B=31, U=5' in parent_prereg
        direct_bad=c.S5_MATCH_COEFF_CYCLE_PULLBACK
        checks['negative_direct_pullback_detected']=any(direct_bad.get(t)!=c.S5_MATCH_COEFF_CYCLE_TARGET.get(t) for t in c.S5_MATCH_COEFF_CYCLE_TARGET)
        checks['negative_inverse_convention_detected']=any(c.S5_MATCH_COEFF_CYCLE_TARGET.get(c.inverse_matching(mt))!=c.S5_MATCH_COEFF_CYCLE_PULLBACK.get(mt) for mt in c.S5_MATCH_COEFF_CYCLE_PULLBACK)
    except Exception as e:
        checks['import_success']=False;checks['import_error']=repr(e)
    mandatory=[k for k in checks if k!='import_error']
    if not checks.get('prereg_present') or not checks.get('import_success'):
        classification='INVALID_IMPLEMENTATION_OR_PROVENANCE'
    elif all(checks.get(k) is True for k in mandatory):
        classification='PASS_REPAIR3_STATIC_IMPORT_BINDING'
    else:
        classification='BLOCKED_REPAIR3_BINDING_NOT_PROVEN'
    out={'gate':'K5_34_ORBIT_REPAIR3_STATIC_IMPORT_BINDING_GATE','classification':classification,'checks':checks,'q18_values_used':False,'N_B_orders_or_coefficients_used':False,'heavy_resolver_executed':False}
    p=ROOT/'results/raw/k5_34_orbit_repair3_static_import_binding_gate.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True));print('CLASSIFICATION='+classification)
    raise SystemExit(0 if classification=='PASS_REPAIR3_STATIC_IMPORT_BINDING' else 2)
if __name__=='__main__':main()
