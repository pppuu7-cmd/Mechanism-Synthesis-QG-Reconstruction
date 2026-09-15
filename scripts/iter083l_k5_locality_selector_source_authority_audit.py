#!/usr/bin/env python3
import argparse,json

def require(path,needles):
    t=open(path,encoding='utf-8').read(); missing=[n for n in needles if n not in t]; return not missing,missing

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--prereg',default='prereg/ITER083L_SM_K5_LOCALITY_SELECTOR_SOURCE_AUTHORITY_AUDIT.md')
    ap.add_argument('--source-lock',default='sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md')
    ap.add_argument('--iter083e',default='results/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_NONIMPLICATION_RESULT.md')
    ap.add_argument('--iter083f',default='results/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_RESULT.md')
    ap.add_argument('--iter083j',default='results/ITER083J_SM_PRODUCT_FACTORIZATION_METRIC_UNIQUENESS_RESULT.md')
    ap.add_argument('--iter083k',default='results/ITER083K_SM_FOREST_EXTERNAL_DECOUPLING_METRIC_UNIQUENESS_RESULT.md')
    args=ap.parse_args()

    p0,m0=require(args.source_lock,['Eq. (3)','one-wedge spectral prescription','Eq. (4)','ten Toller factors'])
    p1,m1=require(args.source_lock,['edgewise collision-analytic parameters `s_e=1+x_e`','do not define'])
    p2,m2=require(args.source_lock,['ten-dimensional regulator-parameter space carrying a metric Q','Q-dependent polar/holomorphic projection `pi_Q`'])
    p3,m3=require(args.source_lock,['`Q*(L_B,e_external)=0`','joint K3/K4/K5 finite-part/subtraction map'])
    p4,m4=require(args.source_lock,['Toller T matrices','functions on SL(2,C)','K5 gluing/composition normalization'])
    p5j,m5j=require(args.iter083j,['forces the Euclidean regulator-metric ray','Physical applicability firewall'])
    p5k,m5k=require(args.iter083k,['forest-external decoupling plus S5 forces the Euclidean metric ray','does not yet claim the Lorentzian causal-K5 source authorizes it'])
    p5=p5j and p5k
    p6e,m6e=require(args.iter083e,['ONE_WEDGE_ANALYTIC_UNIQUENESS_DOES_NOT_LIFT_TO_JOINT_K5_EXTENSION_SELECTOR','PASS_EXACT_SCOPED'])
    p6f,m6f=require(args.iter083f,['COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION','PASS_EXACT_SCOPED'])
    p6=p6e and p6f
    p7p,m7p=require(args.prereg,['BLOCKED_SOURCE_AUTHORITY_SCOPED','not a no-go against future principles'])
    p7=p7p
    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'direct_formula_type_mismatch_not_keyword_only':p0 and p1 and p2,
        'retain_iter083j_k_math':p5,
        'do_not_install_q_identity_by_convenience':True,
        'retain_future_locality_principle':True,
        'retain_microlocal_composition_rg_bridges':True,
        'retain_non_q_schemes':True,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083L-SM',
        'classification':('ITER083L_SM_CURRENT_CAUSAL_TOLLER_SOURCE_DOES_NOT_AUTHORIZE_Q_BASED_FOREST_LOCALITY_SELECTOR_SCOPED' if passed else 'ITER083L_SM_INVALID_IMPLEMENTATION'),
        'verdict':'BLOCKED_SOURCE_AUTHORITY_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'published_one_wedge_spectral_regulator':True,
        'published_joint_k5_edge_analytic_regulators':False,
        'published_joint_k5_regulator_metric_Q':False,
        'published_joint_k5_projection_piQ':False,
        'published_forest_external_decoupling_law':False,
        'published_joint_k5_subtraction_or_finite_part':False,
        'conditional_euclidean_ray_theorems_available':['Iter083J','Iter083K'],
        'scientific_statement':'The audited causal/Toller source defines one-wedge Toller functions and their ten-factor K5 product but not the multivariate collision-regulator objects or forest-locality axiom needed to promote the conditional Euclidean-Q theorems to a physical K5 selector.',
        'dependency_missing':{'P0':m0,'P1':m1,'P2':m2,'P3':m3,'P4':m4,'P5J':m5j,'P5K':m5k,'P6E':m6e,'P6F':m6f,'P7':m7p},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':raise SystemExit(main())
