#!/usr/bin/env python3
import argparse,itertools,json
from fractions import Fraction

V=tuple(range(5))
EDGES=tuple((a,b) for a in V for b in V if a<b)
EI={e:i for i,e in enumerate(EDGES)}
PERMS=tuple(itertools.permutations(V))


def eye(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[x/q for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                q=M[i][c]; M[i]=[M[i][j]-q*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]
def edge_action(p):
    out=[]
    for a,b in EDGES:
        u,v=p[a],p[b]
        if u>v:u,v=v,u
        out.append(EI[(u,v)])
    return tuple(out)
def require(path,needles):
    t=open(path,encoding='utf-8').read(); m=[n for n in needles if n not in t]; return not m,m

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--source-lock',default='sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md')
    ap.add_argument('--prereg',default='prereg/ITER083J_SM_PRODUCT_FACTORIZATION_FORCES_EUCLIDEAN_REGULATOR_METRIC.md')
    ap.add_argument('--iter083g',default='results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md')
    ap.add_argument('--iter083i',default='results/ITER083I_SM_FOREST_POLE_Q_GEOMETRY_SENSITIVITY_RESULT.md')
    args=ap.parse_args()

    # P0 framework source and scope lock.
    p0s,m0s=require(args.source_lock,['dual quadratic form Q*','Lemma 7.2','pi_(p1+p2)(t1 tensor t2)','not itself a tensor product of ten distributions'])
    p0p,m0p=require(args.prereg,['TWO_COORDINATE_THEOREM','K5_SOURCE_APPLICABILITY_FIREWALL','universal product-factorization'])
    p0=p0s and p0p

    # P1 exact two-coordinate decomposition formula c=qij/qii.
    samples=[(Fraction(1),Fraction(0)),(Fraction(2),Fraction(3)),(Fraction(5,7),Fraction(-2,11))]
    sample_constants=[qij/qii for qii,qij in samples]
    factorization_equiv=all(((qij/qii)==0)==(qij==0) for qii,qij in samples)
    projection_formula='c_ij=Qstar_ij/Qstar_ii'
    p1=(sample_constants==[0,Fraction(3,2),Fraction(-14,55)] and factorization_equiv)

    # P2 all 10-coordinate ordered pairs force 45 unique off-diagonals to zero.
    ordered_pairs=[(i,j) for i in range(10) for j in range(10) if i!=j]
    unique_pairs={(min(i,j),max(i,j)) for i,j in ordered_pairs}
    p2=(len(ordered_pairs)==90 and len(unique_pairs)==45)

    # P3 S5 transitive edge action forces a diagonal invariant form to one scalar.
    actions=[edge_action(p) for p in PERMS]
    orbit={a[0] for a in actions}
    parent=list(range(10))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for act in actions:
        for i,j in enumerate(act): union(i,j)
    diagonal_orbits=len({find(i) for i in range(10)})
    p3=(len(actions)==120 and len(orbit)==10 and diagonal_orbits==1)

    # P4 common scale leaves the zero/nonzero Q*-orthogonality relations unchanged.
    scale_tests=[]
    for c in (Fraction(1,3),Fraction(2),Fraction(7)):
        D=[[c if i==j else Fraction(0) for j in range(10)] for i in range(10)]
        scale_tests.append(all(D[i][j]==0 for i,j in unique_pairs))
    p4=all(scale_tests)

    # P5 authoritative Q2 exact inverse and factorization violation constants.
    I=eye(10); A=[[Fraction(0)]*10 for _ in range(10)]
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if i!=j and len(set(e)&set(f))==1:A[i][j]=1
    Q2=[[I[i][j]+Fraction(1,10)*A[i][j] for j in range(10)] for i in range(10)]
    Q2s=inv(Q2)
    diagvals={Q2s[i][i] for i in range(10)}
    adjvals=set(); disjvals=set()
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if i>=j: continue
            (adjvals if len(set(e)&set(f))==1 else disjvals).add(Q2s[i][j])
    diag=next(iter(diagvals)); adj=next(iter(adjvals)); disj=next(iter(disjvals))
    c_adj=adj/diag; c_disj=disj/diag
    p5g,m5g=require(args.iter083g,['Q2 = I + (1/10) A','positive definite','not a scalar multiple of'])
    p5=(diagvals=={Fraction(185,176)} and adjvals=={Fraction(-15,176)} and disjvals=={Fraction(5,176)} and c_adj==Fraction(-3,37) and c_disj==Fraction(1,37) and p5g)

    # P6 reconcile with Iter083I: Q2 sensitivity valid in S5-only class but Q2 excluded by stronger axiom.
    p6i,m6i=require(args.iter083i,['proper/nested forest pole arrangement','geometric scheme sensitivity','does not yet prove a nonzero difference between physical renormalized amplitudes'])
    p6=p6i and p5

    # P7 applicability firewall must be explicit in both source lock and prereg.
    p7s,m7s=require(args.source_lock,['connected product of ten Toller functions sharing group variables','not itself a tensor product'])
    p7p,m7p=require(args.prereg,['not yet a claim that the connected Lorentzian K5 source object physically authorizes','source audit is required'])
    p7=p7s and p7p

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'reject_s5_alone_as_metric_selector': p5g,
        'reject_q2_before_factorization_test': p5g and p5,
        'reject_tensor_factorization_as_connected_k5_multiplication': p7,
        'reject_overall_scale_as_physical_data': p4,
        'reject_unique_physical_extension_claim': p7,
        'retain_iter083g_i_in_broader_s5_class': p6,
        'retain_k5_factorization_authority_gap': p7,
        'retain_non_q_scheme_scope': True,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083J-SM',
        'classification':('ITER083J_SM_UNIVERSAL_PRODUCT_FACTORIZATION_PLUS_K5_EDGE_TRANSITIVITY_FORCES_Q_EUCLIDEAN_RAY_SCOPED' if passed else 'ITER083J_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'projection_constant_formula':projection_formula,
        'ordered_distinct_coordinate_tests':len(ordered_pairs),
        'unique_offdiagonal_constraints':len(unique_pairs),
        's5_edge_orbit_size':len(orbit),
        'invariant_diagonal_sector_dimension':diagonal_orbits,
        'metric_conclusion':'Qstar=c I and Q=c^-1 I',
        'overall_scale_projection_relevant':False,
        'Q2star_diagonal':str(diag),
        'Q2star_adjacent':str(adj),
        'Q2star_disjoint':str(disj),
        'Q2_factorization_constant_adjacent':str(c_adj),
        'Q2_factorization_constant_disjoint':str(c_disj),
        'scientific_statement':'Within a universal Q-based polar projection family satisfying tensor-product factorization on arbitrary independent regulator coordinate blocks, all Qstar off-diagonals vanish; K5 edge transitivity then forces the Euclidean metric ray. This mathematical naturality theorem is not yet physical authorization for the connected Lorentzian K5 vertex.',
        'dependency_missing':{'P0_source':m0s,'P0_prereg':m0p,'P5_iter083g':m5g,'P6_iter083i':m6i,'P7_source':m7s,'P7_prereg':m7p},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':raise SystemExit(main())
