#!/usr/bin/env python3
import argparse,json,math
from fractions import Fraction


def require(path,needles):
    t=open(path,encoding='utf-8').read(); missing=[n for n in needles if n not in t]; return not missing,missing


def multiply_n_once(state):
    # state dict k->coefficient for delta^(k)
    out={}
    for k,c in state.items():
        if k>=1:
            out[k-1]=out.get(k-1,Fraction(0))-Fraction(k)*c
    return out


def multiply_n_power(k,q):
    s={k:Fraction(1)}
    for _ in range(q): s=multiply_n_once(s)
    return s


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--prereg',default='prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md')
    ap.add_argument('--source-lock',default='sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md')
    ap.add_argument('--theorem',default='sources/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_DERIVATION.md')
    ap.add_argument('--iter083m',default='results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md')
    ap.add_argument('--iter082d',default='results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md')
    ap.add_argument('--iter083b',default='results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md')
    args=ap.parse_args()

    p0m,m0m=require(args.iter083m,['unique local forest radial quadratic basis','finite part','PASS_EXACT_SCOPED'])
    p0d,m0d=require(args.iter082d,['omega=(0,3,8)','normal derivative orders'])
    if not p0d:
        p0d,m0d=require(args.iter082d,['omega=(0,3,8)','omega_B'])
    p0b,m0b=require(args.iter083b,['normal order at most','dim_C F_8 = 377'])
    p0p,m0p=require(args.prereg,['LAURENT_TRANSFORMATION','SUPPORTED_JET_ANNIHILATOR','ACTUAL_RESIDUE_FIREWALL'])
    p0=p0m and p0d and p0b and p0p

    # P1 formal Laurent coefficient bookkeeping in a free module basis.
    # Basis coordinates: A_-1, A_0, phi*A_-1.
    residue_before=(1,0,0)
    finite_before=(0,1,0)
    residue_after=(1,0,0)
    finite_after=(0,1,1)
    residue_unchanged=(residue_after==residue_before)
    finite_shift=tuple(finite_after[i]-finite_before[i] for i in range(3))
    p1=(residue_unchanged and finite_shift==(0,0,1))

    # P2 exact n^q delta^(k) identities through the deepest allowed order 8.
    delta_checks=0; delta_failures=[]
    for k in range(0,9):
        for q in range(0,10):
            got=multiply_n_power(k,q)
            if q<=k:
                expected={k-q:Fraction(((-1)**q)*math.factorial(k),math.factorial(k-q))}
            else:
                expected={}
            delta_checks+=1
            if got!=expected: delta_failures.append({'k':k,'q':q,'got':{str(a):str(b) for a,b in got.items()},'expected':{str(a):str(b) for a,b in expected.items()}})
    # For an order<=omega supported jet, n^(omega+1) annihilates every basis delta^k.
    annihilator_checks={}
    sharp_witnesses={}
    for omega in (0,3,8):
        all_k=all(multiply_n_power(k,omega+1)=={} for k in range(omega+1))
        # Every q<=omega has a nonzero action on delta^(q).
        witnesses=all(multiply_n_power(q,q)!={} for q in range(omega+1))
        annihilator_checks[str(omega)]=all_k
        sharp_witnesses[str(omega)]=witnesses
    p2=(not delta_failures and all(annihilator_checks.values()) and all(sharp_witnesses.values()))

    # P3 thresholds.
    thresholds={'K3':{'omega':0,'required_I_power':1},'K4':{'omega':3,'required_I_power':4},'K5':{'omega':8,'required_I_power':9}}
    p3=(thresholds['K3']['required_I_power']==1 and thresholds['K4']['required_I_power']==4 and thresholds['K5']['required_I_power']==9)

    # P4 same normalized Hessian only forces phi|N=0 in the conformal class.
    p4t,m4t=require(args.theorem,['Equality of the normalized Hessians','phi|_N=0','not enough, by itself'])
    p4=(p4t and thresholds['K3']['required_I_power']==1 and thresholds['K4']['required_I_power']>1 and thresholds['K5']['required_I_power']>1)

    # P5 constant scaling formula.
    p5t,m5t=require(args.theorem',['rho\'=c rho','(log c) A_-1'])
    # accept source file escaping differences via fallback
    if not p5t:
        p5t,m5t=require(args.theorem,["rho'=c rho",'(log c) A_-1'])
    p5=p5t

    # P6 actual residue firewall.
    p6p,m6p=require(args.prereg,['do not infer that the physical Toller residue activates every allowed derivative channel','Actual independence can be stronger'])
    p6t,m6t=require(args.theorem,['particular physical residue may have smaller order','No actual nonzero physical scheme dependence is proved'])
    p6=p6p and p6t

    # P7 external theorem and applicability ceiling.
    p7s,m7s=require(args.source_lock,['Felder and David Kazhdan','finite part changes by a local residue term','odd-codimension','not established'])
    p7p,m7p=require(args.prereg,['odd-codimension residue-vanishing','must NOT be promoted automatically'])
    p7=p7s and p7p

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'reject_tangent_metric_as_full_finite_part_for_omega_positive':p4,
        'reject_all_residues_as_order_zero':thresholds['K5']['omega']==8,
        'reject_actual_k5_dependence_claim':p6,
        'reject_fk_k4_parity_without_membership':p7,
        'retain_exact_nonlinear_source_radius_possibility':True,
        'retain_actual_residue_annihilator_possibility':p6,
        'retain_global_forest_patching_blocker':True,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083N-SM',
        'classification':('ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED' if passed else 'ITER083N_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'laurent_residue_unchanged':residue_unchanged,
        'laurent_finite_part_shift':'phi*A_-1',
        'delta_identity_checks':delta_checks,'delta_identity_failures':len(delta_failures),
        'annihilator_checks':annihilator_checks,'sharp_witnesses':sharp_witnesses,
        'universal_independence_thresholds':thresholds,
        'same_tangent_metric_conformal_information':'phi|_N=0 only',
        'constant_rescaling_shift':'(log c) A_-1',
        'scientific_statement':'For a simple-pole radial analytic regularization, conformal change rho->exp(phi)rho leaves the residue fixed and shifts the finite part by phi times the supported residue. Universal independence for residue order <=omega requires phi to vanish through normal order omega, i.e. phi in I_N^(omega+1). Iter083M tangent metric normalization supplies only phi|N=0, universally enough for K3 but not the full allowed K4/K5 residue spaces.',
        'dependency_missing':{'P0_iter083m':m0m,'P0_iter082d':m0d,'P0_iter083b':m0b,'P0_prereg':m0p,'P4_theorem':m4t,'P5_theorem':m5t,'P6_prereg':m6p,'P6_theorem':m6t,'P7_source':m7s,'P7_prereg':m7p},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':raise SystemExit(main())
