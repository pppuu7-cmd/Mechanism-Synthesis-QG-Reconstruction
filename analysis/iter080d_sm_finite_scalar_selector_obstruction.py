#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LOCK=ROOT/'analysis'/'iter080d_sm_source_lock.json'
DERIV=ROOT/'sources'/'ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md'
ERRATUM=ROOT/'status'/'ITER077_CONTACT_FORMULA_ERRATUM.md'
PREREG=ROOT/'prereg'/'ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md'
ITER='Iter080D-SM'
CLASSIFICATION='ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED'

def read(p): return p.read_text(encoding='utf-8')
def lock(): return json.loads(read(LOCK))

def lane_a():
    L=lock(); d=read(DERIV); e=read(ERRATUM); p=read(PREREG)
    checks={
      'prereg_precedes_gate':'PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE COMPUTATION' in p,
      'iter077q_derivation_blob_locked':L['authority']['iter077q']['derivation_blob_sha']=='1b15464e8f7d5ae9d87932938f76de1ac8f3351f',
      'actual_collision_manifold':'N = SU(2)^4 subset SL(2,C)^4' in d,
      'exact_Q_path':'Q(t)=12+8 cos(t)' in d,
      'linear_independence':'Therefore `{Q^n F}_{n>=0}` is linearly independent.' in d,
      'countably_infinite':'countably infinite-dimensional subspace' in d,
      'actual_boundary_nonzero':'not identically zero for at least one actual minimal-sector boundary state' in d,
      'source_not_surrogate':'not obtained from a scalar K4/K5 surrogate' in d,
      'erratum_correct_formula':"`delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)`" in e,
      'historical_invalid_quarantine':'Iter077E' in e and 'Iter077F' in e and 'NON_AUTHORITATIVE_SOURCE_LOCK_INVALID' in e,
    }
    valid=all(checks.values())
    return {'iteration':ITER,'lane':'A','purpose':'authoritative Iter077Q/erratum source lock','valid':valid,'scientific_outcome':'PASS_SOURCE_LOCK' if valid else 'INVALID_SOURCE_LOCK','checks':checks,'locked_run':L['authority']['iter077q']['run_id'],'locked_artifact':L['authority']['iter077q']['aggregate_artifact_id'],'locked_digest':L['authority']['iter077q']['aggregate_digest']}

def lane_b():
    L=lock(); pairs=[tuple(x) for x in L['frozen_controls']['pairs_m_N']]
    controls=[]
    for m,N in pairs:
        dim=N+1; lower=dim-m
        controls.append({'m':m,'N':N,'dim_W_N':dim,'universal_rank_upper_bound':m,'universal_nullity_lower_bound':lower,'coordinate_projection_rank':m,'coordinate_projection_nullity':lower,'valid':N>=m and lower>0})
    universal=[]
    for m in [1,2,4,8]:
      for R in [1,2,4,8,16,32]:
        N=m+R-1; lower=(N+1)-m
        universal.append({'fixed_m':m,'requested_kernel_dimension_R':R,'chosen_N':N,'rank_bound':m,'kernel_dimension_lower_bound':lower,'valid':lower>=R})
    checks={'iter077q_family_locked':L['selector_class']['space'].startswith('W=span_C{h_n:n>=0}'),'selector_codomain_finite':L['selector_class']['maps'].endswith('W->C^m'),'fixed_finite_m':'fixed finite m' in L['selector_class']['scope'],'all_frozen_projection_controls':all(x['valid'] for x in controls),'arbitrary_kernel_dimension_witnesses':all(x['valid'] for x in universal)}
    valid=all(checks.values())
    return {'iteration':ITER,'lane':'B','purpose':'universal exact rank-nullity obstruction','valid':valid,'scientific_outcome':'PASS_EXACT_THEOREM' if valid else 'INVALID_IMPLEMENTATION','theorem':'For fixed finite m and complex-linear L:W->C^m, dim(W_N)=N+1 and rank(L|W_N)<=m, hence dim ker(L|W_N)>=N+1-m. For arbitrary R choose N=m+R-1; then dim ker L>=R. Thus ker L is infinite-dimensional and L is not injective.','checks':checks,'frozen_controls':controls,'universal_witnesses':universal}

def lane_c():
    L=lock(); pairs=[tuple(x) for x in L['frozen_controls']['pairs_m_N']]
    neg=[]
    for _,N in pairs:
        dim=N+1; neg.append({'N':N,'condition_count':dim,'identity_rank':dim,'identity_nullity':0,'valid':dim>0})
    excluded=L['selector_class']['excluded']
    checks={'identity_negative_controls':all(x['valid'] and x['identity_nullity']==0 for x in neg),'growing_condition_family_excluded':any('grows without bound' in x for x in excluded),'function_valued_excluded':'function-valued constraints' in excluded,'differential_spectral_excluded':any('differential/spectral/microlocal' in x for x in excluded),'nonlinear_excluded':'nonlinear selectors' in excluded,'ceiling_in_prereg':'does **not** eliminate a source-derived function-valued constraint' in read(PREREG)}
    valid=all(checks.values())
    return {'iteration':ITER,'lane':'C','purpose':'negative controls and interpretation ceiling','valid':valid,'scientific_outcome':'PASS_SCOPE_CONTROL' if valid else 'INVALID_IMPLEMENTATION','checks':checks,'negative_controls':neg,'surviving_selector_classes':excluded}

LANES={'A':lane_a,'B':lane_b,'C':lane_c}

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
      for fn in files:
        if not fn.endswith('.json'): continue
        try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
        except Exception: continue
        if obj.get('iteration')==ITER and obj.get('lane') in LANES: got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(got[k].get('valid') for k in LANES)
    if valid:
      verdict='PASS_EXACT_SCOPED'; classification=CLASSIFICATION
      fact='The exact Iter077Q ambiguity W contains infinitely many linearly independent source-compatible directions, and every selector consisting of a fixed finite number of scalar-valued complex-linear conditions W->C^m has an infinite-dimensional kernel. Such finite scalar renormalization conditions cannot uniquely select the K5 extension.'
    else:
      verdict='INVALID'; classification='ITER080D_SM_INVALID_SOURCE_LOCK_OR_IMPLEMENTATION'; fact='No scientific promotion: at least one frozen required lane is invalid or missing.'
    return {'iteration':ITER,'execution_valid':valid,'lane_scientific_outcomes':{k:got.get(k,{}).get('scientific_outcome') for k in LANES},'verdict':verdict,'classification':classification,'new_scientific_fact':fact,'claim_ceiling':'This excludes only a fixed finite list of scalar-valued linear conditions. It does not exclude function-valued or infinite condition families, differential/spectral/microlocal equations, or nonlinear selectors; it does not prove a unique K5 extension, full-vertex divergence, regulator independence, E7/E8, G3, RG, F9/G8/K5 promotion, or new physics.','next_admissible_gate':'Audit primary Toller/causal source authority for a genuinely function-valued, differential, spectral, or microlocal joint-K5 extension condition acting on the full tangential ambiguity space; do not repeat finite symmetry or finite scalar-normalization controls.','claim_lock':'No NEW_PHYSICS_FOUND; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1; no G3 PASS; no F9/G8/K5 promotion; retain published spectral i epsilon.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=sorted(LANES)); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
    obj=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(obj,indent=2,sort_keys=True))
    if a.lane and not obj['valid']: raise SystemExit(1)
    if a.aggregate_dir and not obj['execution_valid']: raise SystemExit(1)
if __name__=='__main__': main()
