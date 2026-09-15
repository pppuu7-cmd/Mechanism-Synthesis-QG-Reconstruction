#!/usr/bin/env python3
import hashlib,json,re,sys
from pathlib import Path

ROOT=Path('.')
PREREG='prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY_INDEPENDENT_CRITIC_REVIEW.md'
RESEARCH_RAW='results/raw/actual_k4_order3_source_object_reachability.json'
RESEARCH_RESULT='results/ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_RESULT.md'
PROV='status/ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_PROVENANCE.md'
EXPECTED_JSON='60a4787f73d1b0908222ba85ae11eb3f55434465f1d1d5dcc386a090ec22957c'
EXPECTED_ART='22cc7680b651802c96f5ce4ca0de8d358df6d790f6b61deccf198510d01c6c47'

# Independent critic: infer capabilities from repository corpus, not Researcher R booleans.
# A capability counts present only if an explicit source-faithful cubic construction is found;
# prose saying it is needed/absent never counts as positive evidence.
TEXT=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.txt','.yml','.yaml'} and '.git' not in p.parts:
        try: TEXT.append((str(p),p.read_text(errors='ignore')))
        except Exception: pass

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def has_constructive(patterns, exclude=()):
    hits=[]
    for path,text in TEXT:
        if path in {RESEARCH_RAW,RESEARCH_RESULT,PROV,PREREG}: continue
        low=text.lower()
        if any(x.lower() in low for x in exclude): continue
        if all(re.search(q,text,re.I|re.S) for q in patterns): hits.append(path)
    return sorted(set(hits))

prov={
 'prereg_exists':Path(PREREG).exists(), 'research_raw_exists':Path(RESEARCH_RAW).exists(),
 'result_exists':Path(RESEARCH_RESULT).exists(), 'provenance_exists':Path(PROV).exists(),
 'research_json_sha256': sha(RESEARCH_RAW) if Path(RESEARCH_RAW).exists() else None,
}
prov['research_json_digest_ok']=prov['research_json_sha256']==EXPECTED_JSON
prov_text=Path(PROV).read_text(errors='ignore') if Path(PROV).exists() else ''
prov['artifact_digest_recorded']=EXPECTED_ART in prov_text
prov['run_recorded']='34964010302' in prov_text and '10394990199' in prov_text
provenance_ok=all([prov['prereg_exists'],prov['research_raw_exists'],prov['result_exists'],prov['provenance_exists'],prov['research_json_digest_ok'],prov['artifact_digest_recorded'],prov['run_recorded']])

# Conservative independent capability predicates. They require same-file constructive evidence
# for cubic/order-3 plus the physical/source object, preventing patchwork across incompatible charts.
req={
 'R1_K4_NORMAL_CHART': [r'(nested|simultaneous).*(K3|K4).*(K5)',r'(cubic|order[- ]?3|third order)',r'(coordinate|chart|pullback)'],
 'R2_BCH_ORDER3': [r'BCH|Baker.Campbell.Hausdorff',r'(cubic|order[- ]?3|third order)',r'(ten|10).*(relative|wedge|group)'],
 'R3_TOLLER_ORDER3': [r'Toller',r'(cubic|order[- ]?3|degree 3)',r'(component|branch).*(Taylor|jet|expansion)'],
 'R4_EXTERNAL_TOLLER_JETS': [r'external.*Toller|Toller.*external',r'(order[- ]?[123]|degree [123]|cubic)',r'(jet|Taylor|derivative)'],
 'R5_HAAR_JACOBIAN_ORDER3': [r'Haar|Jacobian',r'(cubic|order[- ]?3|degree 3)',r'(pullback|pulled.back|chart)'],
 'R6_Q_DEFINING_FUNCTION_ORDER3': [r'q_B|q_\{?B\}?',r'(cubic|order[- ]?3|degree 3)',r'(cross.coupl|nested.*pullback|pullback.*nested)'],
 'R8_FRONT_PAIRING': [r'(K4.*front|front.*K4)',r'(angular|sphere|projective)',r'(K3|K2).*(pairing|distribution|subface)'],
}
# Exclude files whose role is explicitly prereg/audit/result/status, so requirement prose cannot self-certify.
EXCL=('prereg','reachability','current research state','authority audit')
hits={k:has_constructive(v,EXCL) for k,v in req.items()}
present={k:bool(v) for k,v in hits.items()}

# Retained positive lanes: establish from independent pre-existing source/bridge/K3 authority corpus.
pos={
 'R7_FULL32_CONTRACTION_MAP': bool(has_constructive([r'(32|thirty.two).*(boundary|component)',r'(contraction|tensor|fiber)'],('reachability','prereg'))),
 'R9_BRANCH_NORMALIZATION': bool(has_constructive([r'Toller',r'i.?epsilon|i ε|spectral',r'(branch|kappa|causal)'],('reachability','prereg'))),
 'R10_S5_TRANSPORT': bool(has_constructive([r'S5|S_5',r'(transport|permutation|covarian)',r'(boundary|fiber|leg)'],('reachability','prereg'))),
}

# Same decision path for real and synthetic/malformed candidates.
KEYS=list(req)+['R7_FULL32_CONTRACTION_MAP','R9_BRANCH_NORMALIZATION','R10_S5_TRANSPORT']
def validate(c):
    missing=[k for k in KEYS if not c.get(k,False)]
    forbidden=[x for x in c.get('methods',[]) if x in {'commuting_bch','representative_boundary','frozen_angular_ray','one_parameter_regulator','termwise_contact','posthoc_finite_part','beta_plus_i_epsilon','partial_as_complete','scalar_hodge_surrogate'}]
    return {'accepted':not missing and not forbidden,'missing':missing,'forbidden':forbidden}

fixture={k:True for k in KEYS}; fixture['methods']=[]
controls={}
control_map={
 'missing_chart':'R1_K4_NORMAL_CHART','commuting_bch':'R2_BCH_ORDER3','missing_external_toller':'R4_EXTERNAL_TOLLER_JETS',
 'flat_haar':'R5_HAAR_JACOBIAN_ORDER3','incompatible_q':'R6_Q_DEFINING_FUNCTION_ORDER3','representative_boundary':'R7_FULL32_CONTRACTION_MAP',
 'frozen_angular_ray':'R8_FRONT_PAIRING','one_parameter_regulator':'R6_Q_DEFINING_FUNCTION_ORDER3','illegal_termwise_contact':'R8_FRONT_PAIRING',
 'posthoc_finite_part':'R8_FRONT_PAIRING','beta_plus_i_epsilon':'R9_BRANCH_NORMALIZATION','partial_as_complete':'R7_FULL32_CONTRACTION_MAP'}
method_for={'commuting_bch':'commuting_bch','representative_boundary':'representative_boundary','frozen_angular_ray':'frozen_angular_ray','one_parameter_regulator':'one_parameter_regulator','illegal_termwise_contact':'termwise_contact','posthoc_finite_part':'posthoc_finite_part','beta_plus_i_epsilon':'beta_plus_i_epsilon','partial_as_complete':'partial_as_complete'}
for name,key in control_map.items():
    c=dict(fixture); c[key]=False; c['methods']=[method_for[name]] if name in method_for else []
    controls[name]=validate(c)
controls_ok=validate(fixture)['accepted'] and all(not x['accepted'] for x in controls.values())
real={**present,**pos,'methods':[]}; real_v=validate(real)

if not provenance_ok: verdict='K4_ORDER3_REACHABILITY_CRITIC_INVALID_PROVENANCE'
elif not controls_ok: verdict='K4_ORDER3_REACHABILITY_CRITIC_INVALID_IMPLEMENTATION'
elif all(pos.values()) and not real_v['accepted']:
    verdict='K4_ORDER3_REACHABILITY_CRITIC_CONFIRMED_BLOCKED_OBJECT_DEFINITION_SCOPED'
elif real_v['accepted']:
    verdict='K4_ORDER3_REACHABILITY_CRITIC_SCIENTIFIC_FAIL_SCOPED'
else: verdict='K4_ORDER3_REACHABILITY_CRITIC_BLOCKED'

out={'verdict':verdict,'provenance':prov,'provenance_ok':provenance_ok,'independent_required_hits':hits,'required_present':present,'positive_lanes':pos,'real_validation':real_v,'synthetic_positive':validate(fixture),'controls':controls,'controls_ok':controls_ok,'interpretation_ceiling':'reachability/object-definition only; no K4 zero/nonzero, finiteness/divergence, regulator, finite-part, or new-physics claim'}
Path('results/raw').mkdir(parents=True,exist_ok=True)
Path('results/raw/critic_k4_order3_reachability.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
# valid scientific BLOCKED is success; implementation/provenance/access invalid is nonzero
sys.exit(0 if verdict in {'K4_ORDER3_REACHABILITY_CRITIC_CONFIRMED_BLOCKED_OBJECT_DEFINITION_SCOPED','K4_ORDER3_REACHABILITY_CRITIC_SCIENTIFIC_FAIL_SCOPED'} else 2)
