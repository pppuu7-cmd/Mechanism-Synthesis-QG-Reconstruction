#!/usr/bin/env python3
"""DSIR terminal handoff V2 refresh audit.

Frozen by prereg/DSIR_TERMINAL_HANDOFF_V2_REFRESH.md.
The audit measures interface completeness, not physical-gate completion.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RESULTS = {
    'V1': ('results/DSIR_TERMINAL_HANDOFF_RST_RESULT.md', 'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V1'),
    'X': ('results/ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_RESULT.md', 'ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED'),
    'Y': ('results/ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY_RESULT.md', 'ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED'),
    'Z': ('results/ITER076Z_TOLLER_FRONT_FACE_NONSCALAR_OBSTRUCTION_RESULT.md', 'ITER076Z_SCALAR_RADIAL_STRIP_LEAVES_NONSCALAR_DIRECTION_DEPENDENT_TOLLER_FRONT_FACE_BUNDLE_OBJECT_REQUIRED_EXACT_SCOPED'),
    'A-SM': ('results/ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md', 'ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED'),
    'B-BCH': ('results/ITER077B_BCH_SOURCE_K4_CYCLE_CURVATURE_RESULT.md', 'ITER077B_SOURCE_BCH_SECOND_ORDER_SELECTS_NONZERO_K4_CYCLE_CURVATURE_EXACT_COORDINATE_SCOPED'),
    'C-SM': ('results/ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md', 'ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED'),
    'D-SM': ('results/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md', 'ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED'),
    'E-SM': ('results/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION_RESULT.md', 'ITER077E_SM_GENERIC_SUBMERSION_PULLBACK_ALLOWED_RANK9_CONTACT_HORMANDER_CRITERION_COLLIDES_CORRELATED_BOUNDARY_VALUE_REQUIRED_EXACT_SCOPED'),
    'F-SM': ('results/ITER077F_SM_RANK9_CONTACT_SCALING_EXTENSION_RESULT.md', 'ITER077F_SM_ALL_SPIN_HALF_RANK9_CONTACT_REACHES_N3_SCALING_NONUNIQUENESS_SOURCE_I_EPSILON_EXTENSION_REQUIRED_EXACT_SCOPED'),
}


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def result_locks():
    out = {}
    for key, (path, classification) in RESULTS.items():
        p = ROOT / path
        exists = p.exists()
        body = p.read_text(encoding='utf-8') if exists else ''
        low = body.lower()
        out[key] = {
            'path': path,
            'exists': exists,
            'classification_present': classification in body,
            'has_authority_or_run': (('authoritative' in low and 'run' in low) or key == 'V1'),
        }
    return out


def lane_r2():
    locks = result_locks()
    funnel = text('docs/DSIR_TO_POLYGON_FUNNEL_V0_2.md')
    a = text(RESULTS['A-SM'][0]); c = text(RESULTS['C-SM'][0]); d = text(RESULTS['D-SM'][0]); e = text(RESULTS['E-SM'][0]); f = text(RESULTS['F-SM'][0])
    al, el, fl = a.lower(), e.lower(), f.lower()
    checks = {
        'required_results_classified': all(v['exists'] and v['classification_present'] for v in locks.values()),
        'generic_rank10_submersion': (('rank `10`' in a or 'rank 10' in al) and 'submersion' in el and 'pullback' in el and ('authoriz' in el or 'canonical' in el)),
        'scalar_cycle_nontransfer': ('ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED' in a),
        'rank9_codim3': 'codimension-3' in c or 'codimension 3' in c,
        'rank9_H6_nondegenerate': 'determinant `-1`' in d and 'inertia `(3 positive, 3 negative)`' in d,
        'rank9_Hormander_collision': 'RANK9_POINT_CONTACT_STANDARD_PULLBACK_CRITERION_FAILS=true' in e,
        'n0_unique': '`n=0`: scaling degree `2 < 6`, unique local extension' in f,
        'n3_exact': '`n_eff=3`' in f and '-8 gamma^3/(1+gamma^2)^3' in f,
        'n3_nonunique_scaling': '`n=3`: scaling degree `8 > 6`' in f and 'nonunique by scaling alone' in f,
        'broad_missing_object': 'SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' in funnel and 'SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' in f,
        'local_missing_object': 'SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL' in funnel and 'SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL' in f,
        'global_exceptional_coverage_exported': 'cover the other rank-deficient source strata' in funnel,
        'K5_remains_blocked': 'Terminal status remains\n\n`BLOCKED_TRANSFER_TO_POLYGON`' in funnel,
        'no_arbitrary_finite_part': ('arbitrary' in fl and ('finite part' in fl or 'counterterm' in fl) and 'forbid' in fl),
    }
    return {'audit':'DSIR-V2','lane':'R2','valid':all(checks.values()),'checks':checks}


def lane_s2():
    v1 = text(RESULTS['V1'][0]); funnel = text('docs/DSIR_TO_POLYGON_FUNNEL_V0_2.md')
    checks = {
        'V1_G3_blocked': 'CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION' in v1 and 'BLOCKED_TRANSFER_TO_POLYGON' in v1,
        'V2_G3_blocked': 'CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION' in funnel and 'Stage 8' in funnel,
        'source_vertex_not_silent_novelty': 'may not be silently copied as a novelty claim' in funnel,
        'no_G3_promotion': 'no G3/F9/G8/K5 promotion' in funnel,
    }
    return {'audit':'DSIR-V2','lane':'S2','valid':all(checks.values()),'checks':checks}


def lane_t2():
    v1 = text(RESULTS['V1'][0]); funnel = text('docs/DSIR_TO_POLYGON_FUNNEL_V0_2.md')
    checks = {
        'V1_F9_blocked': 'PHYSICAL_MULTISCALE_CCI_REALIZATION' in v1,
        'V2_F9_blocked': 'PHYSICAL_MULTISCALE_CCI_REALIZATION' in funnel and 'Stage 9' in funnel,
        'CCI_executable': 'multi-step cylindrical consistency and CCI' in funnel,
        'Toller_closure_required': 'closure of the Toller analytic/pole class' in funnel,
        'G4_G8_downstream': 'G4-G7 remain downstream polygon tests' in funnel and 'G8 remains `CONVERGENCE_ONLY`' in funnel,
    }
    return {'audit':'DSIR-V2','lane':'T2','valid':all(checks.values()),'checks':checks}


def lane_u2():
    locks = result_locks()
    ledger = text('status/ITER077_PROVENANCE_LEDGER.md')
    funnel = text('docs/DSIR_TO_POLYGON_FUNNEL_V0_2.md')
    prereg = text('prereg/DSIR_TERMINAL_HANDOFF_V2_REFRESH.md')
    aliases = ['Iter077A-SM','Iter077A-FF','Iter077B-BCH','Iter077C-SM','Iter077D-SM','Iter077E-SM','Iter077F-SM']
    computational = [k for k in RESULTS if k != 'V1']
    checks = {
        'all_result_classifications': all(locks[k]['classification_present'] for k in RESULTS),
        'all_new_results_have_authority': all(locks[k]['has_authority_or_run'] for k in computational),
        'stable_aliases_complete': all(alias in ledger for alias in aliases),
        'scope_nonmerge_firewall': 'cannot be imported as a source-amplitude existence theorem' in ledger and 'does not establish physical K4/Hodge transport' in ledger,
        'K5_named_missing_object': 'SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' in funnel,
        'G3_named_missing_object': 'CRQN_NORMALIZED_LOCAL_DYNAMICS_AND_COMPOSITION' in funnel,
        'F9_named_missing_object': 'PHYSICAL_MULTISCALE_CCI_REALIZATION' in funnel,
        'published_i_epsilon_locked': 'published spectral `i epsilon`' in funnel,
        'no_hidden_pushforward': 'cannot be imported into the physical source-amplitude/K4 numerator lane until an explicit source/Toller/front-face pushforward is constructed' in funnel,
        'epsilon_unclassified': 'no nominal `epsilon^-1` coefficient' in funnel,
        'V2_semantics_100_interface_only': 'It does **not** mean that all G1-G8 gates pass' in funnel,
        'prereg_frozen_classification': 'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V2_SOURCE_MAP_REFINED' in prereg,
    }
    return {'audit':'DSIR-V2','lane':'U2','valid':all(checks.values()),'checks':checks,'result_locks':locks}


LANES={'R2':lane_r2,'S2':lane_s2,'T2':lane_t2,'U2':lane_u2}


def write(obj,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8')


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if obj.get('audit')=='DSIR-V2' and obj.get('lane') in LANES:
                got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(bool(got[k].get('valid')) for k in LANES)
    return {
        'audit':'DSIR-V2','valid':bool(valid),
        'classification':'DSIR_FUNNEL_CONTRACT_COMPLETE_TERMINAL_HANDOFF_V2_SOURCE_MAP_REFINED' if valid else 'DSIR_TERMINAL_HANDOFF_V2_REFRESH_INCOMPLETE',
        'contract_completeness_percent':100 if valid else None,
        'meaning':'100% handoff-contract/interface completeness only; no physical gate promotion.' if valid else 'V2 refresh incomplete; inspect failed frozen predicate.',
        'lanes_found':sorted(got),'lane_valid':{k:bool(got.get(k,{}).get('valid')) for k in LANES},
        'K5_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,
        'K5_missing_object':'SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION' if valid else None,
        'first_local_subobject':'SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL' if valid else None,
        'G3_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,
        'F9_status':'BLOCKED_TRANSFER_TO_POLYGON' if valid else None,
        'G8_status':'CONVERGENCE_ONLY' if valid else None,
        'claim_lock':'No K5/G3/F9/G8 promotion, vertex finiteness/divergence theorem, regulator-independence theorem, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, new physics, or complete-QG claim.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True)
    args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj,indent=2,sort_keys=True)); write(obj,args.output)
    if not obj.get('valid'): raise SystemExit(1)

if __name__=='__main__': main()
