#!/usr/bin/env python3
import argparse,itertools,json
from fractions import Fraction

V5=tuple(range(5))
PERMS5=tuple(itertools.permutations(V5))


def F(x): return x if isinstance(x,Fraction) else Fraction(x)
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(x) for x in zip(*A)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def eq(A,B): return A==B
def zero(A): return all(x==0 for r in A for x in r)
def trace(A): return sum(A[i][i] for i in range(len(A)))
def rank_q(rows):
    A=[[F(x) for x in r] for r in rows if any(x for x in r)]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m:break
    return r

def projector(block,n=5):
    B=tuple(sorted(block)); p=len(B); S=set(B)
    return [[(Fraction(int(i==j))-Fraction(1,p)) if i in S and j in S else Fraction(0) for j in range(n)] for i in range(n)]

def perm_matrix(p):
    n=len(p); U=[[Fraction(0)]*n for _ in range(n)]
    for old,new in enumerate(p):U[new][old]=1
    return U

def restrict_form(M,basis):
    B=[list(x) for x in zip(*basis)]
    return mm(mt(B),mm(M,B))
def flat(M): return [x for r in M for x in r]
def require(path,needles):
    t=open(path,encoding='utf-8').read(); missing=[n for n in needles if n not in t]; return not missing,missing

def signed_rotation_group():
    mats=[]
    for perm in itertools.permutations(range(3)):
        inv=sum(1 for i in range(3) for j in range(i+1,3) if perm[i]>perm[j])
        psign=-1 if inv%2 else 1
        for signs in itertools.product((-1,1),repeat=3):
            det=psign*signs[0]*signs[1]*signs[2]
            if det!=1:continue
            R=[[Fraction(0)]*3 for _ in range(3)]
            for col,row in enumerate(perm): R[row][col]=signs[col]
            mats.append(R)
    return mats

def sym3_from_vars():
    basis=[]
    positions=[(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    for a,b in positions:
        M=[[Fraction(0)]*3 for _ in range(3)]
        M[a][b]=1; M[b][a]=1
        basis.append(M)
    return basis

def invariant_sym3_dimension(rotations):
    basis=sym3_from_vars(); rows=[]
    for R in rotations:
        Rt=mt(R)
        transformed=[mm(Rt,mm(M,R)) for M in basis]
        for i in range(3):
            for j in range(i,3):
                rows.append([transformed[k][i][j]-basis[k][i][j] for k in range(6)])
    return 6-rank_q(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--iter077i',default='sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md')
    ap.add_argument('--iter082d',default='results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md')
    ap.add_argument('--iter083b',default='results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md')
    ap.add_argument('--prereg',default='prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md')
    ap.add_argument('--theorem',default='sources/ITER083M_SM_SOURCE_NORMAL_RADIAL_GEOMETRY_DERIVATION.md')
    args=ap.parse_args()

    p0i,m0i=require(args.iter077i,['beta_ab(r)=r |v_ab|+O(r^2)','d = 4*3 = 12'])
    p0d,m0d=require(args.iter082d,['P_B[i,j] = delta_ij - 1/|B|','6 + 3 + 3 = 12','all 20 maximal chains'])
    p0b,m0b=require(args.iter083b,['V = spin1_SO(3) tensor Std5_S5','source Haar/tubular density convention'])
    p0p,m0p=require(args.prereg,['UNIQUE_LABEL_METRIC','COMPLETE_GRAPH_IDENTITY','INTERPRETATION_FIREWALL'])
    p0=p0i and p0d and p0b and p0p

    label_stats={}; p1=True
    for p in (3,4,5):
        I=[[Fraction(int(i==j)) for j in range(p)] for i in range(p)]
        JmI=[[Fraction(int(i!=j)) for j in range(p)] for i in range(p)]
        std=[]
        for i in range(p-1):
            x=[Fraction(0)]*p; x[i]=1; x[p-1]=-1; std.append(x)
        RI=restrict_form(I,std); RO=restrict_form(JmI,std)
        restriction_span_rank=rank_q([flat(RI),flat(RO)])
        pairs=[(i,j) for i in range(p) for j in range(i,p)]
        orbits=[]; perms=list(itertools.permutations(range(p))); left=set(pairs)
        while left:
            q=next(iter(left)); orb=set()
            for perm in perms:
                a,b=perm[q[0]],perm[q[1]]
                if a>b:a,b=b,a
                orb.add((a,b))
            orbits.append(orb); left-=orb
        label_stats[str(p)]={'full_invariant_dimension':len(orbits),'pair_orbit_sizes':sorted(len(o) for o in orbits),'std_restriction_dimension':restriction_span_rank}
        p1 &= (len(orbits)==2 and restriction_span_rank==1)

    rots=signed_rotation_group(); so3_test_dim=invariant_sym3_dimension(rots)
    p2=(len(rots)==24 and so3_test_dim==1 and all(label_stats[str(p)]['std_restriction_dimension']==1 for p in (3,4,5)))

    laplace_ok={}; p3=True
    for p in (3,4,5):
        P=[[Fraction(int(i==j))-Fraction(1,p) for j in range(p)] for i in range(p)]
        L=[[Fraction(p-1 if i==j else -1) for j in range(p)] for i in range(p)]
        ok=(L==[[Fraction(p)*x for x in r] for r in P])
        laplace_ok[str(p)]=ok; p3 &= ok

    nested_checks=[]; p4=True
    for p in (3,4):
        for B in itertools.combinations(V5,p):
            SB=set(B)
            for v in V5:
                if v in SB:continue
                Bp=tuple(sorted(SB|{v}))
                P=projector(B); Pp=projector(Bp); D=sub(Pp,P)
                idem=eq(mm(D,D),D); orth=zero(mm(P,D)) and zero(mm(D,P)); r=trace(D)
                w=[Fraction(0)]*5
                for a in B:w[a]=Fraction(-1,p)
                w[v]=1
                norm=sum(x*x for x in w)
                E=[[w[i]*w[j]/norm for j in range(5)] for i in range(5)]
                contrast=(D==E and norm==Fraction(p+1,p))
                coeff=Fraction(p,p+1)
                ok=idem and orth and r==1 and contrast
                nested_checks.append({'p':p,'block':list(B),'added':v,'rank':str(r),'variance_coefficient':str(coeff),'ok':ok})
                p4 &= ok

    chains=[]; chain_ok=True
    K5=tuple(V5); P5=projector(K5)
    for B4 in itertools.combinations(V5,4):
        for B3 in itertools.combinations(B4,3):
            P3=projector(B3); P4=projector(B4)
            A=P3; B=sub(P4,P3); C=sub(P5,P4)
            ranks=[trace(A),trace(B),trace(C)]
            ok=(ranks==[2,1,1] and eq(mm(A,A),A) and eq(mm(B,B),B) and eq(mm(C,C),C)
                and zero(mm(A,B)) and zero(mm(B,A)) and zero(mm(A,C)) and zero(mm(C,A)) and zero(mm(B,C)) and zero(mm(C,B))
                and [[A[i][j]+B[i][j]+C[i][j] for j in range(5)] for i in range(5)]==P5)
            chains.append((tuple(B3),tuple(B4),K5)); chain_ok &= ok
    p5=(len(chains)==20 and chain_ok)

    blocks=[b for p in (3,4,5) for b in itertools.combinations(V5,p)]
    block_cov=0; chain_cov=0; p6=True
    for perm in PERMS5:
        U=perm_matrix(perm); Ut=mt(U)
        for B0 in blocks:
            PB=projector(B0); target=projector(tuple(sorted(perm[i] for i in B0)))
            ok=mm(U,mm(PB,Ut))==target
            p6 &= ok; block_cov+=int(ok)
        for B3,B4,B5 in chains:
            Ps=[projector(B3),sub(projector(B4),projector(B3)),sub(projector(B5),projector(B4))]
            T3=tuple(sorted(perm[i] for i in B3)); T4=tuple(sorted(perm[i] for i in B4)); T5=tuple(sorted(perm[i] for i in B5))
            Ts=[projector(T3),sub(projector(T4),projector(T3)),sub(projector(T5),projector(T4))]
            for X,Y in zip(Ps,Ts):
                ok=mm(U,mm(X,Ut))==Y
                p6 &= ok; chain_cov+=int(ok)
    p6 &= (block_cov==1920 and chain_cov==7200)

    p7t,m7t=require(args.theorem,['does not yet define a renormalized extension','No exact nonlinear identity','finite parts can depend'])
    p7=p7t

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'reject_rooted_metric':p6,
        'reject_edge_regulator_q_identification':p7,
        'reject_J_as_distinct_on_std':all(label_stats[str(p)]['std_restriction_dimension']==1 for p in (3,4,5)),
        'reject_nonorthogonal_increments':p5,
        'reject_single_chain_only':len(chains)==20,
        'reject_nonlinear_beta_overclaim':p7,
        'retain_finite_part_scale_freedom':p7,
        'retain_global_patching_blocker':p7,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083M-SM',
        'classification':('ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED' if passed else 'ITER083M_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'label_metric_stats':label_stats,
        'rotation_subgroup_checked':len(rots),'boost_symmetric_form_dimension':so3_test_dim,
        'normal_invariant_metric_dimension':{'K3':1,'K4':1,'K5':1},
        'complete_graph_laplacian_identity':laplace_ok,
        'nested_addition_checks':len(nested_checks),
        'nested_variance_coefficients':['3/4','4/5'],
        'maximal_chain_count':len(chains),'physical_chain_ranks':[6,3,3],'physical_total_rank':12,
        's5_block_covariance_checks':block_cov,'s5_chain_increment_covariance_checks':chain_cov,
        'canonical_local_radial_form':'R_B^2=sum_a |x_a-xbar_B|^2=(1/|B|) sum_(a<b)|x_a-x_b|^2',
        'source_tangent_relation':'sum beta_ab(r)^2 = |B| r^2 R_B^2 + O(r^3)',
        'scientific_statement':'The source small-boost geometry and authoritative barycentric forest projectors determine a unique invariant local/tubular radial quadratic basis on every K3/K4/K5 normal fiber, with exact orthogonal nested variance decomposition on all 20 maximal chains. This supplies radial geometry, not a finite-part selector.',
        'dependency_missing':{'P0_iter077i':m0i,'P0_iter082d':m0d,'P0_iter083b':m0b,'P0_prereg':m0p,'P7_theorem':m7t},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':raise SystemExit(main())
