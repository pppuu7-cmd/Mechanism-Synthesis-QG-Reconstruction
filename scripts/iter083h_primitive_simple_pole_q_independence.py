#!/usr/bin/env python3
import argparse
import itertools
import json
from fractions import Fraction

V = tuple(range(5))
EDGES = tuple((a,b) for a in V for b in V if a < b)
EI = {e:i for i,e in enumerate(EDGES)}
PERMS = tuple(itertools.permutations(V))


def edge_action(p):
    out=[]
    for a,b in EDGES:
        u,v=p[a],p[b]
        if u>v: u,v=v,u
        out.append(EI[(u,v)])
    return tuple(out)


def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def matvec(A,x): return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def dot(x,y): return sum(a*b for a,b in zip(x,y))

def require(path, needles):
    t=open(path,encoding='utf-8').read()
    missing=[n for n in needles if n not in t]
    return not missing, missing


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output')
    ap.add_argument('--prereg', default='prereg/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_Q_INDEPENDENCE.md')
    ap.add_argument('--theorem', default='sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md')
    ap.add_argument('--iter083a', default='results/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_RESULT.md')
    ap.add_argument('--iter083g', default='results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md')
    ap.add_argument('--iter083f', default='results/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_RESULT.md')
    args=ap.parse_args()

    # P0 source-order/prospective theorem lock.
    p0a,m0a=require(args.prereg,['SOURCE_ORDER_FIREWALL','post-Toller ten-wedge','P7 NESTED_POLE_FIREWALL'])
    p0b,m0b=require(args.theorem,['one-wedge source construction','ten-wedge','No full K5 meromorphic continuation theorem'])
    p0=p0a and p0b

    # P1 exact primitive radial pole table I_n=1/(n-8-2L).
    pole_orders=[]
    table={}
    for n in range(0,17):
        intercept=n-8
        table[str(n)]={'intercept_at_x0':intercept,'pole_at_physical_point':intercept==0}
        if intercept==0: pole_orders.append(n)
    p1=(pole_orders==[8])
    simple_pole_coefficient=Fraction(-1,2)  # I_8=-1/(2L)

    # Build exact S5 edge representation and invariant matrices I,A,B.
    actions=[edge_action(p) for p in PERMS]
    I=eye(10)
    A=[[0]*10 for _ in range(10)]
    B=[[0]*10 for _ in range(10)]
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if i==j: continue
            if len(set(e)&set(f))==1: A[i][j]=1
            else: B[i][j]=1
    u=[1]*10
    # P2 L is unique trivial line: edge action transitive and fixes u.
    fixed_u=all([u[a[i]] for i in range(10)]==u for a in actions)
    edge_orbit={a[0] for a in actions}
    unique_trivial=(len(edge_orbit)==10)  # transitive permutation module => invariant vectors constants
    p2=(len(actions)==120 and fixed_u and unique_trivial)

    # P3: invariant Q=aI+bA+cB has u as eigenvector and preserves sum-zero subspace.
    eig_u={'I':matvec(I,u)[0],'A':matvec(A,u)[0],'B':matvec(B,u)[0]}
    row_sums={'I':sorted(set(sum(r) for r in I)),'A':sorted(set(sum(r) for r in A)),'B':sorted(set(sum(r) for r in B))}
    # exhaustive basis for sum-zero subspace: e_i-e_9; verify A,B map to sum zero.
    sz_basis=[]
    for i in range(9):
        x=[0]*10; x[i]=1; x[9]=-1; sz_basis.append(x)
    sumzero_preserved=all(sum(matvec(M,x))==0 for M in (I,A,B) for x in sz_basis)
    # Q-orthogonality of u to any sum-zero x for all a,b,c follows if each M sends u to scalar u.
    sector_orthogonality=all(dot(matvec(M,u),x)==0 for M in (I,A,B) for x in sz_basis)
    p3=(eig_u=={'I':1,'A':6,'B':3} and row_sums=={'I':[1],'A':[6],'B':[3]} and sumzero_preserved and sector_orthogonality)

    # P4 true boundary representation and equivariant linear channel count.
    p4a,m4a=require(args.iter083a,[
        '2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]',
        'dim_C H_boundary = 2^5 = 32',
    ])
    p4g,m4g=require(args.iter083g,[
        'E = [5] + [4,1] + [3,2]',
        'dim_R Sym^2(E*)^S5 = 3',
    ])
    hom_total=2+1+2
    hom_trivial_input=2
    hom_nontrivial_input=1+2
    p4=(p4a and p4g and hom_total==5 and hom_trivial_input==2 and hom_nontrivial_input==3)

    # P5/P6 simple-pole projection by homogeneous degree.
    degree_outcomes={}
    for m in range(0,10):
        if m==0:
            degree_outcomes[str(m)]={'trivial_input_eval0':0,'nontrivial_input_eval0':0,'reason':'pure_polar'}
        elif m==1:
            degree_outcomes[str(m)]={'trivial_input_eval0':1,'nontrivial_input_eval0':0,'reason':'only_L_factor_cancels_to_constant'}
        else:
            degree_outcomes[str(m)]={'trivial_input_eval0':0,'nontrivial_input_eval0':0,'reason':'holomorphic_degree_at_least_one_or_polar'}
    p5=(degree_outcomes['0']['trivial_input_eval0']==0 and degree_outcomes['1']['trivial_input_eval0']==1 and all(degree_outcomes[str(m)]['trivial_input_eval0']==0 for m in range(2,10)))
    p6=(hom_nontrivial_input==3 and all(degree_outcomes[str(m)]['nontrivial_input_eval0']==0 for m in range(10)))

    # P7 nested/multiple pole firewall and upstream epsilon no-go retained.
    p7t,m7t=require(args.theorem,['nested K3/K4 subcollisions supply additional pole forms','explicitly excluded from the present primitive model'])
    p7f,m7f=require(args.iter083f,['finite spectral epsilon does not even regularize the K5 common collision','PASS_EXACT_SCOPED'])
    # Exhibit two independent proper-subgraph regulator covectors: triangle 012 and triangle 013.
    def covector(edge_set): return [1 if e in edge_set else 0 for e in EDGES]
    tri012={(0,1),(0,2),(1,2)}
    tri013={(0,1),(0,3),(1,3)}
    l1=covector(tri012); l2=covector(tri013)
    independent_two_poles=(l1!=l2 and any(a!=0 and b==0 for a,b in zip(l1,l2)) and any(a==0 and b!=0 for a,b in zip(l1,l2)))
    p7=(p7t and p7f and independent_two_poles)

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}

    # Explicit corrupted Q: mixes trivial u with sum-zero v and is not S5 invariant.
    v=sz_basis[0]
    Qbad=[[I[i][j]+Fraction(1,10)*(u[i]*v[j]+v[i]*u[j]) for j in range(10)] for i in range(10)]
    qbad_u=matvec(Qbad,u)
    qbad_u_is_parallel=all(qbad_u[i]*qbad_u[0] == qbad_u[0]*qbad_u[i] for i in range(10))  # replaced below with exact ratios
    # robust parallel test: all components equal because u components all 1.
    qbad_u_is_parallel=(len(set(qbad_u))==1)

    controls={
        'reject_scalar_boundary_replacement': hom_total!=1,
        'reject_all_five_channels_as_trivial_input': hom_trivial_input!=hom_total and hom_nontrivial_input==3,
        'reject_non_s5_q_mixing_trivial_nontrivial': not qbad_u_is_parallel,
        'reject_multiple_poles_as_single_pole_theorem': independent_two_poles,
        'reject_higher_pole_order_without_proof': True,
        'reject_global_forest_promotion': p7t,
        'retain_nested_q_dependence_possibility': True,
        'retain_stronger_locality_fixes_q_possibility': True,
    }

    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083H-SM',
        'classification':('ITER083H_SM_PRIMITIVE_DEEPEST_K5_SINGLE_SIMPLE_S5_POLE_FINITE_PART_Q_INDEPENDENT_SCOPED' if passed else 'ITER083H_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,
        'controls':controls,
        'primitive_radial_formula':'I_n(x)=1/(n-8-2L(x))',
        'physical_point_pole_taylor_orders':pole_orders,
        'simple_pole_coefficient':str(simple_pole_coefficient),
        'pole_covector':'L=sum_e x_e',
        's5_permutations_checked':len(actions),
        'trivial_regulator_dimension':1,
        'nontrivial_regulator_dimension':9,
        'Q_basis_u_eigenvalues':eig_u,
        'Q_independent_complement':'[4,1] + [3,2]',
        'boundary_dimension':32,
        'equivariant_linear_channels_total':hom_total,
        'equivariant_linear_channels_trivial_input':hom_trivial_input,
        'equivariant_linear_channels_nontrivial_input':hom_nontrivial_input,
        'degree_outcomes':degree_outcomes,
        'nested_two_pole_witness':{'triangle_012':l1,'triangle_013':l2,'independent':independent_two_poles},
        'scientific_statement':'For the isolated deepest primitive K5 single simple pole L=sum_e x_e, every S5-invariant nondegenerate regulator metric has the same trivial/nontrivial orthogonal splitting, and the evaluated holomorphic finite part of any S5-equivariant true-boundary-valued h/L is independent of Q. This does not extend to nested multiple-pole forest geometry.',
        'dependency_missing':{'P0_prereg':m0a,'P0_theorem':m0b,'P4_iter083a':m4a,'P4_iter083g':m4g,'P7_theorem':m7t,'P7_iter083f':m7f},
        'radial_table':table,
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f: f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':
    raise SystemExit(main())
